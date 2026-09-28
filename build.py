#!/usr/bin/env python3
"""Genera los CV (Markdown + HTML) y el README a partir de data/*.yaml.

Uso:
    python build.py              # todos los idiomas de enabled_languages
    python build.py --lang es    # solo un idioma
"""

import argparse
import datetime as dt
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).parent

LABELS = {
    "es": {
        "profile": "Perfil",
        "experience": "Experiencia profesional",
        "projects": "Proyectos destacados",
        "skills": "Habilidades técnicas",
        "soft_skills": "Habilidades profesionales",
        "education": "Formación",
        "languages": "Idiomas",
        "present": "Actualidad",
        "tech": "Tecnologías",
        "case_study": "Ver caso de estudio",
        "pj": "Contratación como PJ",
        "downloads": "Versiones del CV",
        "months": ["ene.", "feb.", "mar.", "abr.", "may.", "jun.",
                   "jul.", "ago.", "sep.", "oct.", "nov.", "dic."],
        "variants": {
            "main": "CV principal — Full Stack Senior / Tech Lead",
            "backend": "Backend y Arquitectura",
            "ai": "Desarrollo asistido por IA",
            "one-page": "Resumen de una página",
            "full": "Versión completa",
        },
    },
    "pt-BR": {
        "profile": "Perfil",
        "experience": "Experiência profissional",
        "projects": "Projetos em destaque",
        "skills": "Habilidades técnicas",
        "soft_skills": "Competências comportamentais",
        "education": "Formação acadêmica",
        "languages": "Idiomas",
        "present": "Atual",
        "tech": "Tecnologias",
        "case_study": "Ver estudo de caso (em espanhol)",
        "pj": "Contratação PJ",
        "downloads": "Versões do CV",
        "months": ["jan.", "fev.", "mar.", "abr.", "mai.", "jun.",
                   "jul.", "ago.", "set.", "out.", "nov.", "dez."],
        "variants": {
            "main": "CV principal — Full Stack Sênior / Tech Lead",
            "backend": "Backend e Arquitetura",
            "ai": "Desenvolvimento assistido por IA",
            "one-page": "Resumo de uma página",
            "full": "Versão completa",
        },
    },
    "en": {
        "profile": "Profile",
        "experience": "Professional experience",
        "projects": "Selected projects",
        "skills": "Technical skills",
        "soft_skills": "Soft skills",
        "education": "Education",
        "languages": "Languages",
        "present": "Present",
        "tech": "Tech",
        "case_study": "Case study (in Spanish)",
        "pj": "Contracting entity (Brazil)",
        "downloads": "CV versions",
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "variants": {
            "main": "Main CV — Senior Full Stack / Tech Lead",
            "backend": "Backend & Architecture",
            "ai": "AI-assisted development",
            "one-page": "One-page summary",
            "full": "Full version",
        },
    },
}

LANGUAGE_NAMES = {"es": "Español", "pt-BR": "Português (Brasil)", "en": "English"}


class MissingTranslation(Exception):
    pass


def load(name):
    with open(ROOT / "data" / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def make_t(lang):
    """Devuelve el texto en `lang` si es un mapa por idioma; si es un string, tal cual."""
    def t(value):
        if isinstance(value, dict):
            if lang not in value:
                raise MissingTranslation(f"falta traducción '{lang}' en: {value}")
            return value[lang].strip()
        return "" if value is None else str(value)
    return t


def make_fmt_date(labels):
    def fmt_date(value):
        if value is None:
            return labels["present"]
        value = str(value)
        if len(value) == 7:  # AAAA-MM
            year, month = value.split("-")
            return f"{labels['months'][int(month) - 1]} {year}"
        return value
    return fmt_date


def make_period(fmt_date):
    """Rol sin `end` = rol actual; si start y end coinciden, una sola fecha."""
    def period(role):
        start, end = role["start"], role.get("end")
        if end is not None and str(end) == str(start):
            return fmt_date(start)
        return f"{fmt_date(start)} – {fmt_date(end)}"
    return period


def years_since(start, today):
    year, month = (int(p) for p in str(start).split("-"))
    return today.year - year - (1 if today.month < month else 0)


def matches(item_tags, variant_tags):
    return variant_tags == "all" or bool(set(item_tags) & set(variant_tags))


def select_experience(profile, variant):
    jobs = []
    for i, job in enumerate(profile["experience"]):
        if job.get("internship") and not variant["include_internship"]:
            continue
        limit = variant["max_highlights"] if i == 0 else variant["max_highlights_previous"]
        highlights = [
            h for h in job["highlights"]
            if matches(h["tags"], variant["tags"]) and h["priority"] <= variant["max_priority"]
        ]
        # sort estable (respeta el orden del YAML); los logros del `focus` suben un nivel
        focus = variant.get("focus")
        highlights.sort(key=lambda h: h["priority"] - (1 if focus in h["tags"] else 0))
        jobs.append({**job, "highlights": highlights[:limit]})
    return jobs


def build_context(profile, variant, lang, today):
    t = make_t(lang)
    years = years_since(profile["basics"]["career_start"], today)
    return {
        "lang": lang,
        "L": LABELS[lang],
        "t": t,
        "period": make_period(make_fmt_date(LABELS[lang])),
        "b": profile["basics"],
        "headline": profile["headlines"][variant["headline"]],
        "summary": t(profile["summaries"][variant["summary"]]).replace("{years}", str(years)),
        "experience": select_experience(profile, variant),
        "projects": [p for p in profile["projects"] if matches(p["tags"], variant["tags"])]
        if variant["projects"] else [],
        "skills": [
            {"group": t(s["group"]), "items": [t(i) for i in s["items"]]}
            for s in profile["skills"] if variant["legacy_skills"] or not s.get("legacy")
        ],
        "soft_skills": profile["soft_skills"] if variant["soft_skills"] else [],
        "education": profile["education"],
        "languages": profile["languages"],
        "show_company": variant["show_company"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--lang", help="generar solo este idioma")
    args = parser.parse_args()

    profile = load("profile.yaml")
    variants = load("variants.yaml")
    langs = [args.lang] if args.lang else profile["enabled_languages"]
    today = dt.date.today()

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        undefined=StrictUndefined,
        autoescape=select_autoescape(enabled_extensions=("html.j2",)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )

    try:
        for lang in langs:
            out_dir = ROOT / "output" / lang
            out_dir.mkdir(parents=True, exist_ok=True)
            for name, variant in variants.items():
                ctx = build_context(profile, variant, lang, today)
                for ext in ("md", "html"):
                    out = env.get_template(f"cv.{ext}.j2").render(**ctx)
                    (out_dir / f"{variant['file']}.{ext}").write_text(out, encoding="utf-8")
                print(f"✓ output/{lang}/{variant['file']}.md|html")

        # El README se genera en el idioma principal (el primero habilitado)
        lang = profile["enabled_languages"][0]
        ctx = build_context(profile, variants["main"], lang, today)
        ctx["variants"] = variants
        ctx["enabled_languages"] = profile["enabled_languages"]
        ctx["language_names"] = LANGUAGE_NAMES
        ctx["all_labels"] = LABELS
        readme = env.get_template("readme.md.j2").render(**ctx)
        (ROOT / "README.md").write_text(readme, encoding="utf-8")
        print("✓ README.md")
    except MissingTranslation as e:
        sys.exit(f"✗ {e}")


if __name__ == "__main__":
    main()

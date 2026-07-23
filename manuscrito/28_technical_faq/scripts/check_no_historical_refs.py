#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `check no historical refs` associada ao capítulo `28_technical_faq`.

Classificação:
    Verificação documental, simbólica ou numérica preservada no manuscrito.

Verifica se o Capítulo 28 é autocontido e não depende de arquivos históricos.

O manuscrito final deve ser autocontido. Logo, este verificador procura termos
típicos de arquivos históricos externos, como códigos numéricos isolados por
letra e número. O script ignora a própria pasta scripts, pois este comentário
explica a regra auditada.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"\bquest(ão|oes|ões|ao)\b", re.IGNORECASE),
    re.compile(r"\bq[0-9]{1,3}\b", re.IGNORECASE),
    re.compile(r"\bQ[0-9]{1,3}\b"),
]


def scan() -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []
    for path in sorted(ROOT.glob("**/*.md")):
        if "/scripts/" in str(path):
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if any(pattern.search(line) for pattern in PATTERNS):
                hits.append((str(path.relative_to(ROOT)), lineno, line.strip()))
    return hits


def main() -> None:
    hits = scan()
    out = Path(__file__).with_name("saida_check_no_historical_refs.md")
    lines = [
        "---",
        'title: "Saída — verificação de autocontenção"',
        "---",
        "",
        "# Saída — verificação de autocontenção",
        "",
    ]
    if not hits:
        lines.append("Nenhuma referência a arquivos históricos externos foi encontrada nos arquivos Markdown do capítulo.")
    else:
        lines.append("| Arquivo | Linha | Trecho |")
        lines.append("|---|---:|---|")
        for rel, lineno, text in hits:
            lines.append(f"| `{rel}` | {lineno} | {text} |")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Ocorrências: {len(hits)}")
    print(f"Arquivo gerado: {out.name}")
    if hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `check overclaim terms` associada ao capítulo `28_technical_faq`.

Classificação:
    Verificação documental, simbólica ou numérica preservada no manuscrito.

Procura termos de possível sobrealegação no Capítulo 28.

Este verificador é deliberadamente simples. Ele não substitui revisão humana,
mas ajuda a detectar frases que poderiam violar o protocolo científico do
manuscrito, como declarar resolução universal quando o texto deve preservar
status condicional.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WATCH = [
    "resolve tudo",
    "prova definitiva",
    "sem hipótese",
    "universalmente provado",
    "ação de Yang--Mills fundamental",
    "BRST fundamental",
    "fantasma físico",
    "renormalização fundamental",
    "Perelman 8D universal",
]


def scan() -> list[tuple[str, int, str, str]]:
    hits: list[tuple[str, int, str, str]] = []
    for path in sorted(ROOT.glob("**/*.md")):
        if "/scripts/" in str(path):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            low = line.lower()
            for term in WATCH:
                if term.lower() in low:
                    hits.append((str(path.relative_to(ROOT)), lineno, term, line.strip()))
    return hits


def main() -> None:
    hits = scan()
    out = Path(__file__).with_name("saida_check_overclaim_terms.md")
    lines = [
        "---",
        'title: "Saída — verificação de sobrealegações"',
        "---",
        "",
        "# Saída — verificação de sobrealegações",
        "",
    ]
    if not hits:
        lines.append("Nenhuma expressão monitorada de sobrealegação foi encontrada.")
    else:
        lines.append("| Arquivo | Linha | Termo | Trecho |")
        lines.append("|---|---:|---|---|")
        for rel, lineno, term, text in hits:
            lines.append(f"| `{rel}` | {lineno} | {term} | {text} |")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Ocorrências: {len(hits)}")
    print(f"Arquivo gerado: {out.name}")
    if hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

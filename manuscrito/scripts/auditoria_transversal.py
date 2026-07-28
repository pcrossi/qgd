#!/usr/bin/env python3
"""Auditoria transversal autocontida do manuscrito GDQ.

Classificação:
    verificação documental e sintática.

O script verifica propriedades objetivas da edição reestruturada:

* presença de `index.md` e checklist nos 28 capítulos;
* links Wiki e Markdown locais;
* delimitadores matemáticos incompatíveis com Quartz;
* sintaxe dos scripts Python;
* dependências explícitas de arquivos históricos de questões;
* sinais constitutivos suspeitos para rho;
* cobertura bibliográfica e rastreabilidade dos scripts por capítulo.

Ausência de referência bibliográfica ou script não chamado é registrada como
pendência editorial, não como erro matemático. O script não decide se uma prova
física está correta e não substitui revisão científica humana.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "editorial" / "auditoria_transversal_final.md"

CHAPTER_RE = re.compile(r"^(?P<number>[0-9]{2})_")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HISTORICAL_RE = re.compile(
    r"(?:^|[/\\])quest(?:oes|ões)(?:[/\\])|quest(?:ão|ao)_[0-9]+",
    re.IGNORECASE,
)
POSITIVE_RHO_RE = re.compile(
    r"\\rho\s*=\s*e\^\{\s*(?:\\operatorname\{Re\}\s*)?f\s*\+\s*\\bar\s*f",
    re.IGNORECASE,
)
OFFICIAL_ACTION_RE = re.compile(
    r"\\mathcal\{S\}_\{\\(?:text|mathrm)\{GDQ\}\}",
)


@dataclass(frozen=True)
class Finding:
    kind: str
    path: Path
    line: int
    detail: str


def chapter_directories() -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and CHAPTER_RE.match(path.name)
    )


def manuscript_markdown() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if "ref" not in path.relative_to(ROOT).parts
    )


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def resolve_wikilink(source: Path, raw: str, markdown_files: list[Path]) -> bool:
    # Notas de rodapé Obsidian podem produzir `^[[[alvo|rótulo]]]`: o
    # primeiro colchete pertence à nota, não ao caminho Wiki.
    target = unquote(raw.strip()).lstrip("[")
    if "," in target and "/" not in target:
        # Matrizes SymPy como `Matrix([[0, 0]])` não são wikilinks.
        return True
    direct_candidates = [
        source.parent / target,
        Path(str(source.parent / target) + ".md"),
        Path(str(source.parent / target) + ".py"),
        source.parent / target / "index.md",
        ROOT / target,
        Path(str(ROOT / target) + ".md"),
        Path(str(ROOT / target) + ".py"),
        ROOT / target / "index.md",
    ]
    if any(candidate.exists() for candidate in direct_candidates):
        return True

    # Obsidian também resolve nomes únicos no cofre.
    wanted_name = Path(target).name
    wanted_md = wanted_name if wanted_name.endswith(".md") else f"{wanted_name}.md"
    matches = [path for path in markdown_files if path.name == wanted_md]
    return len(matches) == 1


def resolve_markdown_link(source: Path, raw: str) -> bool:
    target = unquote(raw.strip().split("#", 1)[0])
    if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
        return True
    if "/" not in target and not Path(target).suffix:
        # Expressões matemáticas como `[z^3](PN)` não são links Markdown.
        return True
    return (source.parent / target).resolve().exists()


def audit_structure(chapters: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    numbers = [int(CHAPTER_RE.match(path.name).group("number")) for path in chapters]
    expected = list(range(1, 29))
    if numbers != expected:
        findings.append(
            Finding("estrutura", ROOT, 0, f"capítulos encontrados: {numbers}; esperado: {expected}")
        )
    for chapter in chapters:
        if not (chapter / "index.md").exists():
            findings.append(Finding("estrutura", chapter, 0, "index.md ausente"))
        if not (chapter / "checklist_operacional.md").exists():
            findings.append(
                Finding("estrutura", chapter, 0, "checklist_operacional.md ausente")
            )
    return findings


def audit_markdown(markdown_files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        # O mapa de formalização escapa o separador de alias dentro de tabelas.
        link_text = text.replace(r"\|", "|")
        for match in WIKILINK_RE.finditer(link_text):
            if not resolve_wikilink(path, match.group(1), markdown_files):
                findings.append(
                    Finding(
                        "link Wiki",
                        path,
                        line_number(link_text, match.start()),
                        match.group(1),
                    )
                )
        for match in MARKDOWN_LINK_RE.finditer(text):
            if not resolve_markdown_link(path, match.group(1)):
                findings.append(
                    Finding(
                        "link Markdown",
                        path,
                        line_number(text, match.start()),
                        match.group(1),
                    )
                )
        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if any(token in line for token in (r"\(", r"\)", r"\[", r"\]")):
                findings.append(
                    Finding("Quartz", path, lineno, "delimitador \\(...\\) ou \\[...\\]")
                )
            if "$$" in line and stripped != "$$":
                findings.append(
                    Finding("Quartz", path, lineno, "`$$` deve ocupar linha própria")
                )
            if HISTORICAL_RE.search(line):
                findings.append(
                    Finding("dependência histórica", path, lineno, stripped)
                )
            if POSITIVE_RHO_RE.search(line):
                findings.append(
                    Finding("convenção constitutiva", path, lineno, stripped)
                )
    return findings


def audit_official_action(markdown_files: list[Path]) -> list[Finding]:
    """Confere os componentes literais em toda exibição da ação oficial."""

    findings: list[Finding] = []
    required = [
        r"\int_{\gamma}",
        r"\frac{\hbar}{\Lambda_C^2}",
        r"\tau\left(",
        r"\mathcalR+",
        r"g^{\mu\bar\nu}\partial_\muf\partial_{\bar\nu}\barf",
        r"+\frac{f+\barf}{2}-n",
        r"\mathcalU\sqrt{\detg}\,d^{2n}z",
        r"\frac{d\tau}{\tau}",
    ]
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if not OFFICIAL_ACTION_RE.search(text):
            continue
        compact = re.sub(r"\s+", "", text)
        missing = [token for token in required if token not in compact]
        if missing:
            findings.append(
                Finding(
                    "ação oficial",
                    path,
                    line_number(text, OFFICIAL_ACTION_RE.search(text).start()),
                    "componentes ausentes ou alterados: " + ", ".join(missing),
                )
            )
    return findings


def audit_python() -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(ROOT.rglob("*.py")):
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeError) as error:
            findings.append(
                Finding(
                    "sintaxe Python",
                    path,
                    getattr(error, "lineno", 0) or 0,
                    str(error),
                )
            )
    return findings


def chapter_reference_coverage(chapter: Path) -> bool:
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in chapter.rglob("*.md")
        if "scripts" not in path.relative_to(chapter).parts
    )
    return bool(re.search(r"(?:\.\./)+ref/|\[\[ref/|/ref/", text))


def unreferenced_scripts(chapter: Path) -> list[Path]:
    scripts = sorted(chapter.rglob("*.py"))
    if not scripts:
        return []
    documentation = "\n".join(
        path.read_text(encoding="utf-8") for path in chapter.rglob("*.md")
    )
    return [path for path in scripts if path.name not in documentation]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def render(
    chapters: list[Path],
    markdown_files: list[Path],
    findings: list[Finding],
) -> str:
    refs = {chapter.name: chapter_reference_coverage(chapter) for chapter in chapters}
    unreferenced = {
        chapter.name: unreferenced_scripts(chapter) for chapter in chapters
    }
    python_count = len(list(ROOT.rglob("*.py")))
    official_action_count = sum(
        bool(OFFICIAL_ACTION_RE.search(path.read_text(encoding="utf-8")))
        for path in markdown_files
    )

    lines = [
        "---",
        'title: "Auditoria transversal final do manuscrito"',
        "---",
        "",
        "# Auditoria transversal final do manuscrito",
        "",
        "Classificação: verificação documental e sintática reproduzível.",
        "",
        "Esta auditoria não certifica a física. Ela verifica a integridade editorial",
        "necessária para que as provas e cálculos possam ser examinados.",
        "",
        "## Resumo objetivo",
        "",
        f"- capítulos numerados: **{len(chapters)}**;",
        f"- arquivos Markdown auditados, excluindo OCR/referências: **{len(markdown_files)}**;",
        f"- scripts Python analisados sintaticamente: **{python_count}**;",
        f"- exibições literais da ação oficial conferidas: **{official_action_count}**;",
        f"- falhas objetivas: **{len(findings)}**;",
        f"- capítulos com ao menos uma chamada bibliográfica: **{sum(refs.values())}/28**;",
        f"- scripts ainda não citados nominalmente no próprio capítulo: "
        f"**{sum(len(value) for value in unreferenced.values())}**.",
        "",
        "## Resultado por capítulo",
        "",
        "| Capítulo | `index.md` | checklist | referência chamada | scripts | scripts não citados |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for chapter in chapters:
        scripts = list(chapter.rglob("*.py"))
        lines.append(
            f"| `{chapter.name}` | "
            f"{'sim' if (chapter / 'index.md').exists() else 'não'} | "
            f"{'sim' if (chapter / 'checklist_operacional.md').exists() else 'não'} | "
            f"{'sim' if refs[chapter.name] else 'não'} | "
            f"{len(scripts)} | {len(unreferenced[chapter.name])} |"
        )

    lines.extend(["", "## Falhas objetivas", ""])
    if findings:
        lines.extend(
            [
                "| Tipo | Arquivo | Linha | Detalhe |",
                "|---|---|---:|---|",
            ]
        )
        for finding in findings:
            detail = finding.detail.replace("|", r"\|")
            lines.append(
                f"| {finding.kind} | `{rel(finding.path)}` | "
                f"{finding.line or '—'} | {detail} |"
            )
    else:
        lines.append("Nenhuma falha objetiva foi encontrada pelos testes implementados.")

    lines.extend(["", "## Pendências editoriais", ""])
    missing_refs = [name for name, present in refs.items() if not present]
    if missing_refs:
        lines.append(
            "Os seguintes capítulos ainda não chamam uma entrada bibliográfica "
            "da pasta `ref/`:"
        )
        lines.append("")
        for name in missing_refs:
            lines.append(f"- `{name}`")
        lines.append("")
        lines.append(
            "Isso não invalida suas derivações internas, mas impede considerar "
            "concluída a edição citável."
        )
    else:
        lines.append("Todos os capítulos chamam ao menos uma entrada bibliográfica.")

    not_called = [
        path for values in unreferenced.values() for path in values
    ]
    lines.extend(["", "### Scripts não citados nominalmente", ""])
    if not_called:
        for path in not_called:
            lines.append(f"- `{rel(path)}`")
        lines.append("")
        lines.append(
            "A ausência de chamada pode ser legítima para módulos auxiliares, "
            "mas deve ser confirmada manualmente."
        )
    else:
        lines.append("Todos os scripts são citados nominalmente no próprio capítulo.")

    lines.extend(["", "## Veredito", ""])
    lines.append(
        "A estrutura é tecnicamente auditável quando as falhas objetivas são zero."
    )
    lines.append(
        "A publicação citável ainda depende da cobertura bibliográfica capítulo por capítulo."
    )
    if not_called:
        lines.append(
            "Também permanece necessária a confirmação manual dos módulos auxiliares não chamados."
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    chapters = chapter_directories()
    markdown_files = manuscript_markdown()
    findings = (
        audit_structure(chapters)
        + audit_markdown(markdown_files)
        + audit_official_action(markdown_files)
        + audit_python()
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(chapters, markdown_files, findings), encoding="utf-8")
    print(f"Capítulos: {len(chapters)}")
    print(f"Markdown: {len(markdown_files)}")
    print(f"Falhas objetivas: {len(findings)}")
    print(f"Relatório: {OUT.relative_to(ROOT)}")
    if findings:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

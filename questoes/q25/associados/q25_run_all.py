#!/usr/bin/env python3
"""Executa o pacote mínimo Q25 e consolida as saídas."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[0]
RESULTS = ROOT / "resultados"
OUT = RESULTS / "saida_q25_validacao.md"

SCRIPTS = [
    "q25_01_domain_interface.py",
    "q25_02_estimador_holonomia.py",
    "q25_03_autocorrelacao_variancia.py",
    "q25_04_referencias_experimentais.py",
    "q25_05_compare_experiment.py",
]

OUTPUTS = [
    RESULTS / "saida_q25_01_domain_interface.md",
    RESULTS / "saida_q25_02_estimador_holonomia.md",
    RESULTS / "saida_q25_03_autocorrelacao_variancia.md",
    RESULTS / "saida_q25_04_referencias_experimentais.md",
    RESULTS / "saida_q25_05_compare_experiment.md",
]


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    logs = []
    for script in SCRIPTS:
        path = HERE / script
        proc = subprocess.run([sys.executable, str(path)], cwd=str(ROOT), text=True, capture_output=True)
        logs.append((script, proc.returncode, proc.stdout.strip(), proc.stderr.strip()))
        if proc.returncode != 0:
            raise SystemExit(f"{script} falhou:\n{proc.stderr}")

    content = [
        "# Q25 — Validação algorítmica mínima\n\n",
        "Classificação global: teste de consistência + preparação de benchmark. "
        "Não é previsão cega e não fecha a complexidade assintótica geral.\n\n",
        "## Execução\n\n",
        "| script | status | saída |\n|---|---:|---|\n",
    ]
    for script, code, stdout, stderr in logs:
        content.append(f"| `{script}` | {code} | `{stdout}` |\n")
    content.append("\n## Resultados agregados\n\n")
    for output in OUTPUTS:
        content.append(f"\n---\n\n")
        content.append(output.read_text(encoding="utf-8"))
        content.append("\n")
    content.append(
        "\n## Status conservador\n\n"
        "O pacote prova que a rota positiva por domínios/holonomias é implementável "
        "em uma classe reduzida e reproduz solução exata finita sem reweighting "
        "de fase. A Q25 permanece aberta como fechamento computacional forte até "
        "existirem operador GDQ físico por benchmark, dados experimentais locais "
        "extraídos, estudo de escala por classe e cota de variância/complexidade.\n"
    )
    OUT.write_text("".join(content), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()

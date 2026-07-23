#!/usr/bin/env python3
"""Executa o benchmark físico reduzido da Q25."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[0]
RESULTS = ROOT / "resultados"
OUT = RESULTS / "saida_q25_benchmark_fisico.md"

SCRIPTS = [
    "q25_10_extract_experimental_data.py",
    "q25_11_build_physical_domains.py",
    "q25_12_derive_interface_from_hessian.py",
    "q25_13_spin_correlations_gdq.py",
    "q25_14_variance_scaling_physical.py",
    "q25_15_compare_experiment_physical.py",
    "q25_16_thermal_ensemble_map.py",
    "q25_17_hessian_thermal_map_candidates.py",
    "q25_18_thermal_apparatus_block.py",
    "q25_19_schur_apparatus_derivation.py",
    "q25_20_compare_schur_curve.py",
    "q25_21_bath_width_correction.py",
]


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    logs = []
    for script in SCRIPTS:
        proc = subprocess.run([sys.executable, str(HERE / script)], cwd=str(ROOT), text=True, capture_output=True)
        logs.append((script, proc.returncode, proc.stdout.strip(), proc.stderr.strip()))
        if proc.returncode != 0:
            raise SystemExit(f"{script} falhou:\n{proc.stderr}")

    content = [
        "# Q25 — Benchmark físico reduzido\n\n",
        "Classificação global: benchmark físico reduzido + preparação de comparação "
        "experimental. Não é ainda previsão metrológica, pois faltam dados "
        "experimentais quantitativos locais.\n\n",
        "## Execução\n\n",
        "| script | status | saída |\n|---|---:|---|\n",
    ]
    for script, code, stdout, stderr in logs:
        content.append(f"| `{script}` | {code} | `{stdout}` |\n")
    content.append("\n## Resultados\n\n")
    for script, _, stdout, _ in logs:
        if stdout:
            path = Path(stdout)
            if path.exists():
                content.append("\n---\n\n")
                content.append(path.read_text(encoding="utf-8"))
                content.append("\n")
    content.append(
        "\n## Veredito conservador\n\n"
        "A cadeia física reduzida foi executada: rede/aparelho, domínios positivos, "
        "Hessiana reduzida positiva, interfaces unitárias por impedância, "
        "correlações de circulação/spin comparadas com enumeração exata finita e "
        "teste inicial de escala. A comparação externa com Parsons et al. foi "
        "executada com dados locais extraídos. O resultado é parcial: sinal e "
        "ordem de grandeza do correlator frio de primeiro vizinho são reproduzidos, "
        "mas o conjunto completo, especialmente o comprimento de correlação, não "
        "é descrito metrologicamente pelo modelo reduzido. A Q25 ainda exige "
        "mapa térmico/aparelho e Hessiana GDQ completa para fechamento experimental.\n"
    )
    OUT.write_text("".join(content), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()

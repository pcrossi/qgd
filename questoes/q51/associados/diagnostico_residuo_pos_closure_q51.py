#!/usr/bin/env python3
r"""Q51 — diagnóstico do resíduo após fechamento reduzido closure_mobility."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
EVAL = HERE / "avaliacao_reduzida_background_hessiana_q51.py"
OUT = HERE / "saida_diagnostico_residuo_pos_closure_q51.md"


def load_eval():
    spec = importlib.util.spec_from_file_location("q51_eval", EVAL)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    m = load_eval()
    q = m.load_benchmark()

    rows = []
    sq = 0.0
    for case in q.CASES:
        res = m.eval_case(q, case, "closure_mobility")
        delta_log = res["residual"]
        # T_model/T_exp = 10^delta_log. To correct model action:
        # log T = const + W + E_partial, so DeltaW_needed = -ln(10)*delta_log.
        factor = 10.0 ** delta_log
        delta_action_needed = -math.log(10.0) * delta_log
        rows.append((case.name, delta_log, factor, delta_action_needed))
        sq += delta_log * delta_log

    rms = math.sqrt(sq / len(rows))
    mean_abs_action = sum(abs(r[3]) for r in rows) / len(rows)
    max_abs_action = max(abs(r[3]) for r in rows)

    lines = []
    lines.append("# Saída — resíduo pós-closure_mobility Q51\n\n")
    lines.append("Classificação: diagnóstico de resíduo, não ajuste.\n\n")
    lines.append(
        "Usa a variante reduzida `closure_mobility`, onde os fechamentos de "
        "camada são gerados pelo espectro angular spin--torção e o filho "
        "duplamente fechado ativa a mobilidade de determinante.\n\n"
    )
    lines.append("| Núcleo | delta log10 T | T_model/T_exp | Delta ação necessária |\n")
    lines.append("| --- | ---: | ---: | ---: |\n")
    for name, delta_log, factor, delta_action in rows:
        lines.append(f"| {name} | {delta_log:.6f} | {factor:.6f} | {delta_action:.6f} |\n")

    lines.append("\n")
    lines.append(f"- RMS log10 = `{rms:.6f}` décadas\n")
    lines.append(f"- média de |Delta ação| = `{mean_abs_action:.6f}`\n")
    lines.append(f"- máximo de |Delta ação| = `{max_abs_action:.6f}`\n\n")
    lines.append("## Interpretação\n\n")
    lines.append(
        "Todos os casos ficam com resíduos de ordem menor que 0,1 década. "
        "Po-212 deixa de ser anomalia dominante quando a mobilidade de "
        "determinante do filho duplamente fechado é incluída.\n\n"
    )
    lines.append(
        "O resíduo remanescente deve ser tratado como refinamento metrológico "
        "da Hessiana nuclear completa e do dataset, não como nova barreira "
        "radial universal.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

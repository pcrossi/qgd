#!/usr/bin/env python3
"""Q60 — auditoria do raio do próton.

Classificação:
- correção aritmética de fórmula legada;
- avaliação direta do raio canônico de superfície Q40;
- comparação fenomenológica com valores de referência usados no corpus.

Não usa o raio muônico como alvo para construir a fórmula canônica.
"""

from math import pi


def main() -> None:
    # Fórmula legada apontada no enunciado da Q60.
    r_old = 0.8778
    fano_boundary = 0.07479
    mass_quarter = 3.7915
    delta_legacy = r_old * fano_boundary * 1.0e-3 * mass_quarter

    # Cadeia vigente Q40.
    alpha_inv = 137.035999084
    alpha = 1.0 / alpha_inv
    epsilon_eff = 0.011591040463
    Lambda_C_fm = 386.159268
    C_r = (1.0 / 8.0) * (1.0 + alpha / 4.0)
    R_B = 1.5 * Lambda_C_fm
    r_p_q40 = C_r * epsilon_eff * R_B

    # Valores de referência usados historicamente no corpus.
    r_mu_ref = 0.84087
    r_e_legacy = 0.8778
    r_eff_legacy = 0.8354

    print("# Saída — Q60: raio do próton")
    print()
    print("## Correção aritmética da fórmula legada")
    print()
    print(f"0.8778 * 0.07479 * 1e-3 * 3.7915 = {delta_legacy:.12f} fm")
    print()
    print("| Quantidade | Valor |")
    print("| --- | ---: |")
    print(f"| Contração legada correta | {delta_legacy:.12f} fm |")
    print(f"| Contração legada escrita no texto antigo | {0.0369:.12f} fm |")
    print(f"| Fator de erro | {0.0369 / delta_legacy:.6f} |")
    print()
    print("## Raio canônico de superfície Q40")
    print()
    print("| Quantidade | Valor |")
    print("| --- | ---: |")
    print(f"| alpha^-1 | {alpha_inv:.12f} |")
    print(f"| epsilon_eff | {epsilon_eff:.12f} |")
    print(f"| Lambda_C | {Lambda_C_fm:.12f} fm |")
    print(f"| R_B = 3 Lambda_C / 2 | {R_B:.12f} fm |")
    print(f"| C_r = (1/8)(1+alpha/4) | {C_r:.15f} |")
    print(f"| r_p^Q40 = C_r epsilon_eff R_B | {r_p_q40:.12f} fm |")
    print()
    print("## Comparações fenomenológicas")
    print()
    print("| Comparação | Diferença | Diferença relativa |")
    print("| --- | ---: | ---: |")
    for label, ref in [
        ("vs referência muônica 0.84087 fm", r_mu_ref),
        ("vs legado eletrônico 0.8778 fm", r_e_legacy),
        ("vs legado efetivo 0.8354 fm", r_eff_legacy),
    ]:
        diff = r_p_q40 - ref
        rel = diff / ref
        print(f"| {label} | {diff:+.12f} fm | {rel:+.6%} |")
    print()
    print("## Conclusão numérica")
    print()
    print("A fórmula multiplicativa legada não explica uma contração de ~0.037 fm;")
    print("ela produz apenas ~0.000249 fm. O raio vigente deve ser o raio de")
    print("superfície Q40, e a diferença entre sondas deve ser tratada por resposta")
    print("linear do background/problema de contorno, não por essa fórmula antiga.")


if __name__ == "__main__":
    main()

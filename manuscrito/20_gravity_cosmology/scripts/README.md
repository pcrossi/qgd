---
title: "Scripts do Capítulo 20"
---

# Scripts do Capítulo 20

Estes scripts são autocontidos e comentados. Eles avaliam apenas as fórmulas
reduzidas finais usadas no capítulo.

| Script | Saída | Função |
|---|---|---|
| `calcular_G_newton.py` | `saida_calculo_G_newton.md` | Avalia a fórmula reduzida de $\Pi_G$ e compara com $G$ aceito. |
| `calcular_cadeia_termico_axial_G.py` | `saida_calcular_cadeia_termico_axial_G.md` | Verifica o saddle térmico-axial e a condição de colagem que gera $e^{-1/(2\alpha)}$. |
| `derivacao_rho_lambda_simbolica.py` | `saida_derivacao_rho_lambda_simbolica.md` | Registra a derivação algébrica, contagem $28$ e análise dimensional de $\rho_\Lambda$. |
| `calcular_rho_lambda.py` | `saida_calculo_rho_lambda.md` | Avalia a densidade de energia escura e compara com o valor inferido. |
| `derivacao_a0_simbolica.py` | `saida_derivacao_a0_simbolica.md` | Registra a dedução simbólica e dimensional de $a_0=cH_0/(2\pi)$. |
| `calcular_a0_galactico.py` | `saida_calculo_a0_galactico.md` | Avalia a escala $a_0$ e compara com escala MOND típica. |

Classificação:

1. `calcular_G_newton.py`: comparação fenomenológica forte, não previsão ab initio completa;
2. `calcular_cadeia_termico_axial_G.py`: avaliação simbólico-numérica de cadeia condicional;
3. `derivacao_rho_lambda_simbolica.py`: verificação simbólica/dimensional da cadeia estrutural;
4. `calcular_rho_lambda.py`: avaliação direta de fórmula estrutural condicionada a contorno cosmológico;
5. `derivacao_a0_simbolica.py`: verificação simbólica/dimensional sem entrada experimental;
6. `calcular_a0_galactico.py`: avaliação direta de escala de horizonte e comparação fenomenológica.

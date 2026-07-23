---
title: "Checklist operacional — Capítulo 18"
---

# Checklist operacional — Capítulo 18

## 1. Enunciado

Consolidar problema do sinal, confinamento, cor efetiva, Wilson loops, lei de
área, gap transversal e relação setorial GDQ--Yang--Mills.

## 2. Cadeias construtivas

Problema do sinal:

$$
\rho>0
\to
S_R
\to
\operatorname{Hol}(P_{ij})=-1
\to
\mathsf S_{ab}
\to
\text{benchmark positivo}.
$$

Confinamento:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm tube}
\to
K_{\perp}^{\rm phys}
\equiv
P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}[\Phi_{\rm tube}]P_{\rm phys}
\to
\sigma_{\rm GDQ}
\to
V(r)
\to
\langle W(C)\rangle.
$$

Setor de cor:

$$
E_{\rm int}
\to
SU(3)_C
\to
A_C
\to
F_C
\to
\mathfrak H_\Theta.
$$

## 3. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| sinal como fase | fechado estruturalmente | medida positiva |
| interface Cayley | benchmark fechado | unitariedade de máquina |
| variância geral | aberta | exige cota assintótica |
| tubo Ricci--Bohm | fechado estruturalmente | tensão positiva |
| lei de área | fechada efetiva | setor geométrico/isomorfo |
| gap | fechado condicionalmente | operador geométrico efetivo |
| Yang--Mills | redução efetiva setorial | não ação fundamental |
| $\alpha_s^{\rm eff}$ | proposta preservada | não running completo |
| raio/fator de forma | fechado condicionalmente | raio canônico e sonda comprimida separados |
| Hessiana torsional | fechada setorialmente | modo homogêneo vinculado estável |

## 4. Scripts finais/reduzidos

| Script | Classificação |
|---|---|
| `interface_cayley_sinal.py` | Teste de consistência de interface unitária/contrativa. |
| `benchmark_positivo_sinal.py` | Benchmark reduzido de correlação positiva. |
| `benchmark_fisico_reduzido_sinal.py` | Benchmark físico reduzido com comparação externa preservada. |
| `variancia_autocorrelacao_sinal.py` | Teste de escala reduzido. |
| `integrar_tubo_ricci_bohm_confinamento.py` | Avaliação direta da tensão transversal. |
| `coeficiente_cap_ricci_bohm.py` | Derivação numérica do coeficiente $C_{\rm GDQ}=\pi$. |
| `comparar_tensao_raios_confinamento.py` | Comparação de tensão por raios. |
| `raio_fator_forma_tensao.py` | Cálculo do raio canônico, fator de forma e tensão. |
| `hessiana_torcional_vinculada.py` | Avaliação da Hessiana radial vinculada. |
| `heaviside_yang_mills_operacional.py` | Verificação simbólica da ponte operacional GDQ--YM. |
| `alpha_s_fredholm_confinamento.py` | Avaliação da proposta Fredholm. |
| `polarizacao_hiperons_confinamento.py` | Avaliação fenomenológica preservada. |

## 5. Pontos preservados

- GDQ não postula Yang--Mills como ação fundamental.
- Quarks/cor são linguagem operacional do setor reduzido.
- Problema do sinal não é declarado resolvido algoritmicamente em geral.
- Lei de área e gap valem no setor geométrico/isomorfo declarado.
- A comparação com $\sigma_{\rm had}\simeq0{,}89\,{\rm GeV/fm}$ é posterior;
  não entra na derivação de $C_{\rm GDQ}$, $r_p$ ou $F_{\rm shape}$.
- Scripts `required` e ajustes térmicos de aparelho permanecem históricos/futuros.
- Nenhum script final reduzido das o problema do sinal e o confinamento foi omitido deste capítulo; scripts
  exploratórios ou de engenharia inversa ficam fora do manuscrito principal por
  não serem a cadeia final adotada.

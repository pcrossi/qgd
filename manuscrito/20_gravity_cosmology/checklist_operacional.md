---
title: "Checklist operacional — Capítulo 20"
---

# Checklist operacional — Capítulo 20

## 1. Enunciado do capítulo

O capítulo responde como a GDQ trata:

1. constante de Newton;
2. energia do vácuo;
3. equação de estado da energia escura;
4. aceleração crítica galáctica;
5. limites metrológicos da cosmologia perturbativa.

## 2. Construções preservadas

| Construção | Local | Status |
|---|---|---|
| separação $M_{\rm loc}=\mathbb R^4\times T^4$ e $M_E=T^5\times S^3$ | `index`, `20.1` | definição operacional |
| grupo $\Pi_G=GM_p^2/(\hbar c)$ | `20.2`, nota `prova_grupo_pi_newton` | derivação dimensional exata |
| resposta $G=c^4R_H/(2E_H)$ | `20.2` | condição global de contorno |
| cadeia térmico-axial | `20.3`, nota `cadeia_termico_axial_newton` | condicional à colagem |
| prefator Buckingham | `20.2`, nota `auditoria_prefator_buckingham` | fenomenologia forte |
| $\rho_\Lambda$ a energia do vácuo | `20.4`, `20.5`, nota `derivacao_rho_lambda` | estrutural condicional |
| $w=-1$ homogêneo | `20.6` | fechado no background estacionário |
| perturbações por Hessiana | `20.6`, nota `perturbacoes_hessiana_cosmologica` | programa metrológico |
| $a_0=cH_0/(2\pi)$ | `20.7`, nota `aceleracao_critica` | estrutural |
| camada algébrica certificada | nota `formalizacao_lean_gravidade_cosmologia`, `formal/GDQ/GravityCosmology.lean` | formalizada |

## 3. Hessiana, projetores e vínculos

A construção variacional completa foi registrada como:

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm phys}
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast^{\rm cos}]
P_{\rm phys}.
$$

O texto explicita que $P_{\rm phys}$ remove:

1. difeomorfismos puros;
2. modos de normalização;
3. modos de bordo;
4. gauge interno não observável.

O capítulo não afirma ter diagonalizado a Hessiana cosmológica completa. Ele
mantém isso como próximo nível metrológico.

## 4. Scripts incorporados

| Script | Saída | Resultado principal |
|---|---|---|
| `scripts/calcular_G_newton.py` | `scripts/saida_calculo_G_newton.md` | com $\alpha_E$: $G_{\rm GDQ}=6{,}656497635372\times10^{-11}$, erro $-0{,}266730\%$; com $\alpha$ metrológica: erro $-0{,}262330\%$ |
| `scripts/calcular_cadeia_termico_axial_G.py` | `scripts/saida_calcular_cadeia_termico_axial_G.md` | verifica $\Delta u_v=1/(2\alpha)$ sob colagem $R=\pi^2\sqrt\alpha R_H$ |
| `scripts/derivacao_rho_lambda_simbolica.py` | `scripts/saida_derivacao_rho_lambda_simbolica.md` | verifica a cadeia algébrica, $28=\binom82$ e dimensão final ${\rm kg/m^3}$ |
| `scripts/calcular_rho_lambda.py` | `scripts/saida_calculo_rho_lambda.md` | $\rho_\Lambda^{\rm GDQ}=6{,}136532599384\times10^{-27}\,{\rm kg/m^3}$, erro $+5{,}033622\%$ |
| `scripts/derivacao_a0_simbolica.py` | `scripts/saida_derivacao_a0_simbolica.md` | verifica $R_H=c/H_0$, $a_H=c^2/R_H=cH_0$ e $a_0=a_H/(2\pi)$ |
| `scripts/calcular_a0_galactico.py` | `scripts/saida_calculo_a0_galactico.md` | $a_0=1{,}042197881145\times10^{-10}\,{\rm m/s^2}$ para $H_0=67{,}4$ |

Todos são autocontidos, comentados e não usam o valor aceito como entrada da
fórmula GDQ. Os valores aceitos entram apenas na comparação final.

## 4.1 Certificação Lean

O módulo `formal/GDQ/GravityCosmology.lean` certifica as identidades exatas do
capítulo. Ele não certifica como teorema fundamental a fórmula fenomenológica
completa de $G$, nem a escolha do contorno cosmológico, nem a metrologia
CMB/BAO/SNe.

Em particular, a igualdade $\Delta u_v=1/(2\alpha)$ aparece como consequência
da hipótese explícita $R=\pi^2\sqrt{\alpha}R_H$, e não como derivação dessa
colagem.

## 5. Scripts históricos não incorporados

Os solvers exploratórios de `o laboratório numérico gravitacional histórico` foram preservados como
histórico. Eles não foram copiados para o capítulo porque testam ansätze locais
e warps exploratórios que a conclusão final da o cálculo reduzido de Newton não usa como fundamento.

O capítulo usa apenas a rota consolidada:

$$
\text{contorno global}
\to
\text{fórmula reduzida final}
\to
\text{comparação explícita}.
$$

## 6. Comparações obrigatórias

| Quantidade | GDQ | Referência usada | Erro |
|---|---:|---:|---:|
| $G$ com $\alpha_E$ | $6{,}656497635372\times10^{-11}$ | $6{,}67430\times10^{-11}$ | $-0{,}266730\%$ |
| $G$ com $\alpha$ metrológica | $6{,}656791325455\times10^{-11}$ | $6{,}67430\times10^{-11}$ | $-0{,}262330\%$ |
| $\rho_\Lambda$ | $6{,}136532599384\times10^{-27}$ | $5{,}842445930612\times10^{-27}$ | $+5{,}033622\%$ |
| $a_0$, $H_0=67{,}4$ | $1{,}042197881145\times10^{-10}$ | $1{,}20\times10^{-10}$ | $-13{,}150177\%$ |
| $a_0$, $H_0=73$ | $1{,}128789989964\times10^{-10}$ | $1{,}20\times10^{-10}$ | $-5{,}934168\%$ |

## 7. Resultado editorial

Nada essencial foi omitido para o nível estrutural do capítulo.

O que fica fora não é tentativa falha a preservar no texto principal, mas
programa metrológico:

1. resolver $\Phi_\ast^{\rm cos}$ completo;
2. diagonalizar $K_{\rm cos}^{\rm phys}$;
3. calcular funções de transferência;
4. comparar com CMB, BAO, SNe, lentes e crescimento de estrutura.

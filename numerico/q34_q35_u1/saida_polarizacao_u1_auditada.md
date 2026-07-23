# Saída auditada — polarização $U(1)$ das Q34/Q35

## Classificação

**Avaliação direta e teste de consistência.** A equação vem de
questoes/q34/associados/polarizacao_U1_heat_kernel.md. O cálculo não deriva
$\Lambda_{\rm EM}$ e não ajusta dados experimentais.

## Entrada

$$
\alpha_0=0.0072973525692838,\qquad \eta=\tau m^2=1.000000e-06.
$$

$\eta$ é um cenário de teste, não uma constante derivada.

## Avaliação e controle independente

| $r$ | $\Pi_\eta(r)$ | adaptativa | diferença |
|---:|---:|---:|---:|
| 0.000e+00 | 0.000000000000e+00 | 0.000000000000e+00 | 0.000e+00 |
| 1.000e-04 | 1.548528170657e-08 | 1.548528170627e-08 | 2.939e-19 |
| 1.000e+00 | 1.403667635567e-04 | 1.403667635567e-04 | 2.711e-20 |
| 1.000e+04 | 5.839780438507e-03 | 5.839780438512e-03 | 5.171e-15 |
| 1.000e+08 | 1.024957923792e-02 | 1.024957923846e-02 | 5.391e-13 |
| 1.000e+12 | 1.025005713135e-02 | 1.025005713135e-02 | 1.214e-17 |

$$
\Pi_\eta(\infty)=1.025005713135e-02,\qquad \alpha_{\rm eff}^{-1}(\infty)=135.631372264.
$$

## Identidade de Ward

$$
\lVert q^\mu\Pi_{\mu\nu}\rVert=6.985e-21,\qquad \varepsilon_{\rm Ward}=3.218e-17.
$$

O teste verifica a forma tensorial transversal já derivada; não substitui
a derivação funcional da identidade de Ward.

## Refinamento

| pontos | $\Pi_\eta(10^4)$ |
|---:|---:|
| 32 | 5.83977842241677e-03 |
| 64 | 5.83978033561918e-03 |
| 128 | 5.83978043623730e-03 |
| 256 | 5.83978043850670e-03 |
| 512 | 5.83978043851185e-03 |

Erro entre as duas últimas ordens: **5.150e-15**.

## Limite de QED

| $r$ | $\eta=10^{-12}$ | limite $\eta\to0$ | diferença |
|---:|---:|---:|---:|
| 1.000e-04 | 1.548529719120e-08 | 1.548529719193e-08 | 7.232e-19 |
| 1.000e+00 | 1.403669184111e-04 | 1.403669184113e-04 | 1.564e-16 |
| 1.000e+04 | 5.841328153326e-03 | 5.841328154880e-03 | 1.554e-12 |

## Veredito computacional

- monotonicidade: **True**;
- limitado pelo valor assintótico: **True**;
- condição sem polo no cenário: **True**;
- conjunto dos testes: **PASSOU**.

A avaliação física ainda requer derivar $\Lambda_{\rm EM}$ e inserir o
espectro completo de espécies carregadas.

---
title: "Status derivacional, Hessiana e poder preditivo do setor bariônico"
---

# Status derivacional, Hessiana e poder preditivo do setor bariônico

## 1. Enunciado e domínio

O problema bariônico considerado neste capítulo é:

$$
\text{construir um background trimodal }
\Phi_B=(g_B,f_B,H_B,\mathcal A_B)
$$

no bulk local $\mathbb R^4\times T^4$, com três interfaces de estômato, e
extrair seus observáveis na seção física reconstruída.

O ciclo

$$
\mathcal C_B\simeq T^5_{\rm trançado}\times S^3_{\rm hol}
$$

é usado para calcular invariantes globais. Ele não é identificado com o bulk
local.

## 2. Cadeia que uma predição completa deve satisfazer

$$
\mathcal S_{\rm GDQ}
\longrightarrow
\Phi_B
\longrightarrow
K_B^{\rm phys}
\longrightarrow
\text{espectro estável}
\longrightarrow
\text{observável}.
$$

Com vínculos $\mathcal C_i[\Phi_B]=c_i$, a Hessiana física correta é a
segunda variação do funcional aumentado:

$$
K_B^{\rm phys}
=
P_{\rm phys}^{\dagger}
\left.
\delta^2
\left(
\mathcal S_{\rm GDQ}
-
\sum_i\lambda_i\mathcal C_i
\right)
\right|_{\Phi_B}
P_{\rm phys}.
$$

O projetor $P_{\rm phys}$ remove difeomorfismos, modos nulos de calibre e
variações incompatíveis com normalização, carga, fluxo, classe trimodal e
condições de interface. Ele não pode remover um modo físico apenas porque esse
modo torna a Hessiana indefinida.

O capítulo possui uma construção colada reduzida e blocos de Hessiana de
superfície. Ainda não possui uma solução suave geral do sistema 8D acoplado em
toda a garganta. Por isso, os observáveis que dependem dos perfis completos
são resultados condicionais do modelo reduzido.

## 3. O que é exato

Fixada a decomposição em três câmaras:

$$
3(2\pi^5)=6\pi^5.
$$

Fixada a orientação neutra:

$$
1+1-2=0,
$$

e:

$$
(1-1)^2+(1+2)^2+(1+2)^2=18.
$$

Também são exatas:

1. a integralidade do resíduo de Cauchy sob as hipóteses do princípio do
   argumento;
2. a cinemática contínua do beta livre;
3. a identidade de Fierz e a norma
   $2|C_S|^2+6|C_T|^2$;
4. a eliminação de Schur
   $V_{4,\rm eff}=V_4-3G^2/K$;
5. as normalizações $G_E^p(0)=1$ e $G_E^n(0)=0$ para densidades já
   normalizadas.

Essas identidades foram formalizadas em
[[../../../../formal/GDQ/BaryonicReduction.lean|GDQ/BaryonicReduction.lean]].

## 4. O que é condicional

As fórmulas:

$$
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right),
$$

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5},
$$

$$
r_p
=
\frac18
\left(
1+\frac{\alpha}{4}
\right)
\epsilon_{\rm eff}
\left(
\frac32\Lambda_C
\right),
$$

e as fórmulas reduzidas de $\mu_p$ e $\mu_n$ dependem, respectivamente, de:

1. normalização do integrando bariônico por uma unidade eletrônica;
2. identificação de $\pi/2$ por estômato e da impedância mínima por volume;
3. projeção Fredholm--Fano $3$--$4$--$5$;
4. projeção octante e vestimento de borda;
5. redução da corrente completa à corrente de superfície.

Essas hipóteses são geométricas e não usam os valores posteriores de
próton/nêutron como argumentos algébricos. Contudo, ainda não foram todas
obtidas pela avaliação direta da sela 8D e de sua Hessiana completa. Portanto,
os excelentes erros numéricos são comparações fenomenológicas condicionais,
não uma previsão cega já fechada.

## 5. O que é ajuste

O script `modos_coletivos_superficie.py` determina três coeficientes por
mínimos quadrados contra a parametrização de Galster. Esse bloco é:

$$
\boxed{\text{ajuste/benchmark de forma em }q\text{ intermediário}.}
$$

Ele demonstra que uma impedância de Schur com três modos pode reproduzir a
forma de referência. Não demonstra que a Hessiana oficial possui aqueles três
coeficientes.

## 6. Vida média do nêutron

A fórmula:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}
$$

é uma lei reduzida histórica. O expoente $11$ foi associado no legado ao
número de modos de deformação e $32/15$ a uma projeção volumétrica, mas esses
dois números ainda não foram calculados a partir do determinante da Hessiana
bariônica e dos jatos causais $[z^3]F_S,[z^3]F_T$.

Logo, seu estatuto é:

$$
\boxed{
\text{ansatz fenomenológico condicional, avaliado sem pós-ajuste contínuo.}
}
$$

Uma vez assumido o ansatz, a taxa, a meia-vida, o espaço de fase e a conversão
para a norma contraída $\mathcal J_3$ seguem exatamente. A concordância no
nível $10^{-3}$ é evidência numérica interessante, mas não fecha a derivação
variacional do acoplamento.

## 7. Tabela de estatuto

| Resultado | Estatuto |
|---|---|
| aritmética $6\pi^5$ | identidade exata sob a decomposição em três câmaras |
| seleção de três câmaras | hipótese do background trimodal |
| carga inteira | teorema sob meromorfia e contorno fechado |
| equilíbrio $(1,1,-2)$ | identidade de conservação do ansatz neutro |
| massa de próton/nêutron | redução geométrica condicional |
| raio e momentos | redução de superfície condicional |
| normalizações de Sachs | identidades exatas |
| curva de Galster | ajuste/benchmark, não predição |
| cinemática beta contínua | fechada |
| base $S,T$ e norma contraída | fechada estruturalmente |
| $C_S,C_T$ físicos | abertos à quarta variação completa |
| $\alpha^{-11}$ e $32/15$ | ansatz fenomenológico histórico |
| vida média obtida desse ansatz | avaliação direta e comparação |

## 8. Critério para promoção futura

O setor será promovido de redução condicional a predição bariônica completa
quando forem calculados, sem usar os alvos:

$$
\Phi_B^{8D},
\qquad
K_B^{\rm phys},
\qquad
[z^3]F_S,
\qquad
[z^3]F_T,
\qquad
\mathsf R_{\rm EM}(q).
$$

Esses cálculos devem reproduzir ou corrigir os coeficientes reduzidos atuais,
com estudo de convergência e sensibilidade às condições de contorno.

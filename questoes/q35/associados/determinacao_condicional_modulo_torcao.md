# Q35 — Determinação condicional do módulo torsional por $\alpha$

## 1. Classificação

Este cálculo é uma **determinação condicional/inversa**, não uma previsão cega.
Usa como entrada $\alpha_{m IR}=1/137$ e a ponte constitutiva
$\operatorname{Re}_{\rm Q}=\alpha$. O valor $1/128$ não participa.

## 2. Sistema

Para $n_B=1$, a conservação torsional e a ponte constitutiva fornecem

$$
R^4=\frac{1}{12\pi^2\alpha}.
$$

O potencial do relatório `auditorias/RELATORIO_TORCAO_SPIN_S3_R4T4.md` é

$$
V(R,b)=-\frac{12\pi^2}{R^5}+\frac{\pi^2b^2}{6R^9}.
$$

A condição $V'(R)=0$ dá

$$
R^4=\frac{b^2}{40}.
$$

Assim, as duas relações determinam

$$
b^2=\frac{10}{3\pi^2\alpha},
\qquad
|b|=\sqrt{\frac{10}{3\pi^2\alpha}}.
$$

O sinal de $b$ permanece a orientação do fluxo; as grandezas de escala
dependem de $b^2$.

## 3. Resultado para $\alpha=1/137$

$$
R=1{,}03707435228632,
\qquad
|b|=6{,}80220605367609.
$$

Na convenção $\hbar=1$ e $\kappa=3/4$ usada no relatório,
$b=\kappa\langle S\rangle$, logo

$$
|\langle S\rangle|=9{,}06960807156811.
$$

O equilíbrio radial fornece

$$
\tau_{\rm EM}^{\rm dimless}=0{,}274900522513626,
\qquad
\widehat\Lambda_{\rm EM}=1{,}90727017413475,
$$

e a condição de colagem torna-se

$$
\frac{L}{\ell_C}=1{,}64716708528985.
$$

Pela convenção oficial $\widehat\tau=\tau/\ell_C^2$ da Q2,

$$
\Lambda_{\rm EM}^{\rm phys}
=1{,}90727017413475\,\Lambda_C.
$$

## 4. Limite do resultado

O cálculo determina o valor de condensado **requerido** pela compatibilidade
entre $\operatorname{Re}_{\rm Q}=\alpha$ e o mínimo do módulo. Ele não prova
que o traço coincidente de Dirac--Bismut produz esse mesmo número. Essa prova
exigiria especificar e resolver o operador, o espectro, a multiplicidade, o
domínio e a prescrição UV da equação de gap. Esses dados não estão completos
no relatório.

Portanto, este resultado fecha numericamente a rota constitutiva da Q35, mas
não deve ser apresentado como solução independente da equação de gap.

Além disso, $\widehat\Lambda_{\rm EM}$ é uma razão interna. Sua conversão
direta por $M_e$ exigiria conhecer o autovalor eletrônico do mesmo operador.
Ver `questoes/q35/associados/auditoria_calibracao_escala_em.md`.

## 5. Reprodutibilidade

Script:
`numerico/q34_q35_u1/determinar_modulo_torcao_alpha.py`.

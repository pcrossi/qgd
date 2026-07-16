# Q30 — Bloco raio--dilatão sob normalização de Perelman

## 1. Pergunta

Verificar se o acoplamento entre o raio torsional $R$ e
$u=\operatorname{Re}f$ pode destruir a rigidez radial positiva já calculada.

O vínculo físico da medida é

$$
\int_{\Sigma_3}e^{-u}dV=1.
$$

## 2. Modo homogêneo

Para $u=u_0$ constante numa garganta homogênea de volume $V(R)$,

$$
e^{-u_0}V(R)=1,
$$

logo

$$
\boxed{u_0(R)=\log V(R).}
$$

Como $V(S^3_R)\propto R^3$,

$$
u_0(R)=3\log R+\text{constante}.
$$

Portanto, o termo $3\log R$ do funcional radial não é um potencial externo:
é o pullback exato do dilatão homogêneo ao subespaço normalizado. A variação
tangente satisfaz

$$
\boxed{\delta u_0=3\frac{\delta R}{R}.}
$$

Consequentemente, o modo homogêneo de $u$ já foi eliminado pelo vínculo antes
do cálculo

$$
K_R=\frac{6(3R^2-8\tau)}{R^4}.
$$

Não existe um complemento de Schur homogêneo adicional a subtrair de $K_R$;
fazê-lo contaria duas vezes a resposta do dilatão.

## 3. Modos não homogêneos normalizados

Escreva

$$
u=u_0+\phi+c(\phi),
\qquad
\langle\phi\rangle=0,
$$

onde a média usa a medida homogênea normalizada. O vínculo determina

$$
c(\phi)=\log\langle e^{-\phi}\rangle
=\frac12\langle\phi^2\rangle+O(\phi^3).
$$

A expansão do setor oficial
$\int e^{-u}[\tau|\nabla u|^2+u]dV$ fornece, até segunda ordem,

$$
\boxed{
\delta^2\mathcal W_u[\phi]
\sim
\tau\langle|\nabla\phi|^2\rangle
-\frac12\langle\phi^2\rangle.
}
$$

As parcelas homogêneas de curvatura e torção multiplicam uma medida
normalizada e não geram massa adicional para $\phi$ nessa truncagem. Para um
harmônico escalar com

$$
-\Delta\phi_\ell
=\lambda_\ell\phi_\ell,
\qquad
\lambda_\ell=\frac{\ell(\ell+2)}{R^2},
$$

o coeficiente quadrático é

$$
\boxed{\mu_\ell=\tau\lambda_\ell-\frac12.}
$$

O modo $\ell=0$ não pertence a esse bloco porque já está fixado pela
normalização. O menor modo admissível é $\ell=1$:

$$
\boxed{\mu_1=\frac{3\tau}{R^2}-\frac12.}
$$

## 4. Mistura com o raio

Uma variação radial homogênea pertence à representação $\ell=0$, enquanto
$\phi_{\ell\ge1}$ tem média zero. Por ortogonalidade,

$$
\int_{S^3}\phi_{\ell\ge1}dV=0,
\qquad
\int_{S^3}\nabla\phi_{\ell\ge1}dV=0,
$$

e o bloco misto linearizado anula-se:

$$
\boxed{B_{R\phi_\ell}=0\quad(\ell\ge1).}
$$

A Hessiana física homogênea--escalar é, portanto, bloco-diagonal depois de
impor a normalização.

## 5. Avaliação da solução vigente

Para

$$
R=1.03707435228632,
\qquad
\tau=0.274900522513626,
$$

obtém-se

$$
\lambda_1=\frac3{R^2}=2.78934007751156,
$$

$$
\tau\lambda_1=0.766791044776126
$$

e

$$
\boxed{\mu_1=0.266791044776126>0.}
$$

Na convenção em que a Hessiana é duas vezes o coeficiente quadrático, o menor
autovalor desse bloco é $0.533582089552252>0$.

## 6. Resultado

No setor homogêneo normalizado:

$$
\boxed{
K_R>0,
\qquad
\mu_1>0,
\qquad
B_{R\phi}=0.
}
$$

Logo, o dilatão de Bohm não fecha o gap radial nessa truncagem. O resultado é
condicional ao background homogêneo, à normalização de Perelman e à solução
constitutiva de Q35 com $\alpha=1/137$.

## 7. Limites

Ainda não estão incluídos:

1. perfis radiais não homogêneos no colar;
2. termos de bordo/Robin da interface do estômato;
3. mistura com modos métricos que não pertencem ao setor $S=0$;
4. mobilidade causal.

## 8. Classificação

- eliminação do modo homogêneo: consequência exata da normalização;
- espectro escalar em $S^3$: avaliação direta;
- anulação do bloco misto por representações: derivação exata no background
  homogêneo;
- positividade numérica: condicional à solução constitutiva vigente.


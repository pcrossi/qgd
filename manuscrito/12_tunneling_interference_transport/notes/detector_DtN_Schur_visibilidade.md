---
title: "Detector DtN/Schur e visibilidade"
---

# Detector DtN/Schur e visibilidade

## Enunciado

Em um detector linear reduzido:

$$
K_{\rm det}
=
-\partial_s^2+\lambda^2,
\qquad
s\in[0,L],
$$

com $\varphi(0)=\varphi_0$ e $\varphi(L)=0$, a impedância DtN é:

$$
\mathsf R_{\rm det}=\lambda\coth(\lambda L).
$$

## Prova

A solução estacionária de:

$$
(-\partial_s^2+\lambda^2)\varphi=0
$$

com $\varphi(0)=\varphi_0$ e $\varphi(L)=0$ é:

$$
\varphi(s)=
\varphi_0
\frac{\sinh(\lambda(L-s))}{\sinh(\lambda L)}.
$$

Derivando:

$$
\partial_s\varphi(0)
=
-\lambda\coth(\lambda L)\varphi_0.
$$

O fluxo normal de saída é:

$$
-\partial_s\varphi(0)
=
\lambda\coth(\lambda L)\varphi_0.
$$

Logo:

$$
\mathsf R_{\rm det}=\lambda\coth(\lambda L).
$$

## Visibilidade

Se o detector distingue caminhos por $\Delta\Phi_\partial$, então:

$$
\Gamma_{\rm det}
=
\frac12
\langle
\Delta\Phi_\partial,
\mathsf R_{\rm det}
\Delta\Phi_\partial
\rangle.
$$

O coeficiente de coerência é:

$$
\mathcal C_{\rm det}=e^{-\Gamma_{\rm det}}.
$$

Para dois marcadores normalizados $w_1$ e $w_2$ no contorno:

$$
\Delta\Phi_\partial
=
\zeta_{\rm det}(w_1-w_2),
$$

com:

$$
\int_{\partial\Omega}(w_1-w_2)^2d\Sigma=C_{\rm path}.
$$

Então:

$$
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda\coth(\lambda L).
$$

Para marcador primitivo:

$$
C_{\rm path}=1.
$$

O padrão observado é:

$$
\rho_{\rm det}
=
I_1+I_2
+
2e^{-\Gamma_{\rm det}}
\sqrt{I_1I_2}\cos\Delta\phi.
$$

## Validação numérica preservada

No teste reduzido autocontido do capítulo, foram usados:

$$
\lambda_{\rm det}=1.1,
\qquad
L=1,
\qquad
C_{\rm path}=1.
$$

Assim:

$$
\mathsf R_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L)
=
1.37414284103.
$$

Para $N=8000$:

| $\zeta_{\rm det}$ | $\Gamma_{\rm det}$ | $e^{-\Gamma_{\rm det}}$ | visibilidade bruta central |
|---:|---:|---:|---:|
| $0$ | $0$ | $1$ | $0.987400675$ |
| $0.5$ | $0.171767855$ | $0.842174657$ | $0.893408543$ |
| $1.25$ | $1.073549095$ | $0.341793305$ | $0.547559863$ |
| $2.5$ | $4.294196378$ | $0.013647535$ | $0.270891364$ |

O refinamento de malha de $N=1000$ até $N=8000$ preserva
$\Gamma_{\rm det}$ e mostra estabilidade da visibilidade bruta central.

O observável diretamente controlado pela GDQ reduzida é
$e^{-\Gamma_{\rm det}}$, não a visibilidade bruta, pois esta também contém o
envelope incoerente $I_1+I_2$.

## Comparação com a descrição operacional padrão

O limite padrão coerente corresponde a:

$$
\Gamma_{\rm det}=0.
$$

O limite padrão com marcador perfeito de caminho corresponde a:

$$
\Gamma_{\rm det}\gg1.
$$

A GDQ reduzida fornece a curva intermediária:

$$
\mathcal C_{\rm det}(\zeta_{\rm det})
=
\exp\left[
-\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L)
\right].
$$

Essa curva é o elemento distintivo do tratamento: não se muda a ação oficial;
calcula-se a perda de coerência pela impedância de interface do aparelho.

## Alcance

Esse é fechamento estrutural para detector linear reduzido. Um detector real
exige calcular $\lambda$, $L$ e acoplamentos a partir do aparelho.

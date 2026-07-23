# Q30 — derivação reduzida de $C_{\rm GDQ}$ no tubo Ricci--Bohm

## Enunciado

Queremos remover a ambiguidade do coeficiente na fórmula reduzida:

$$
\sigma_{\rm GDQ}
=C_{\rm GDQ}\frac{\hbar c}{r_\perp^2}.
$$

A pergunta é se $C_{\rm GDQ}$ foi ajustado ou se sai da geometria
transversal da ação oficial reduzida.

## Setor usado

Usamos o setor transversal Ricci--Bohm já adotado na Q30. Ele é uma redução da
ação oficial na seção normal ao tubo, não uma ação Yang--Mills/QCD.

O cap transversal primitivo é uma 2-seção compacta com bordo geodésico. Em
coordenadas internas:

$$
ds_\perp^2
=r_\perp^2(d\chi^2+\sin^2\chi\,d\theta^2),
\qquad
0\le\chi\le\frac\pi2.
$$

O bordo em $\chi=\pi/2$ é geodésico. Assim, pelo Gauss--Bonnet:

$$
\int_{\rm cap}K\,dA=2\pi.
$$

Como em duas dimensões $R_2=2K$:

$$
\int_{\rm cap}R_2\,dA=4\pi.
$$

## Coeficiente on-shell

Na equação transversal Ricci--Bohm da GDQ, o balanço entre curvatura e pressão
de Bohm deixa, no setor on-shell primitivo, o índice reduzido:

$$
C_{\rm GDQ}
=\frac14\int_{\rm cap}R_2\,dA.
$$

Logo:

$$
C_{\rm GDQ}
=\frac14(4\pi)
=\boxed{\pi}.
$$

Portanto, o fator $\pi$ não vem do dado hadrônico. Ele é a carga geométrica do
cap Ricci--Bohm primitivo.

## Avaliação numérica

Com:

$$
r_\perp=0.860000000000\,\mathrm{fm},
\qquad
\hbar c=0.1973269804\,\mathrm{GeV\,fm},
$$

temos:

| quantidade | valor |
|---|---:|
| área intrínseca do cap | 4.647043853190 fm$^2$ |
| área projetada do disco | 2.323521926595 fm$^2$ |
| $R_2$ | 2.704164413196 fm$^{-2}$ |
| $\int R_2 dA$ | 12.566370614359 |
| $C_{\rm GDQ}$ | 3.141592653590 |
| $\Delta_{\rm GDQ}$ | 0.229449977209 GeV |
| $\sigma_{\rm GDQ}$ | 0.838184142752 GeV/fm |
| $\sigma_{\rm GDQ}$ | 0.165396345908 GeV$^2$ |
| $\sqrt{\sigma_{\rm GDQ}}$ | 0.406689495695 GeV |

Comparação posterior com
$\sigma_{\rm had}\simeq0.890000\,\mathrm{GeV/fm}$:

$$
\frac{\sigma_{\rm GDQ}-\sigma_{\rm had}}{\sigma_{\rm had}}
=-5.822006\%.
$$

Em $\sqrt{\sigma}$:

$$
-2.954653\%.
$$

## Relação com a integração do disco

A integração anterior do disco usava:

$$
\varepsilon_\sigma=\frac{\hbar c}{r_\perp^4}.
$$

Agora essa densidade reduzida fica interpretada como a representação projetada
do índice de curvatura do cap Ricci--Bohm. Integrando no disco projetado:

$$
\int_0^{r_\perp}2\pi s\,ds\,
\frac{\hbar c}{r_\perp^4}
=\pi\frac{\hbar c}{r_\perp^2},
$$

que coincide com $C_{\rm GDQ}\hbar c/r_\perp^2$.

## Limite de validade

Este fechamento é forte no setor transversal reduzido. Ele ainda não equivale
à solução 8D geral de:

$$
\sigma_{\rm GDQ}
=\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}],
$$

com todos os modos de $g$, $J$, $H$, $f$ e os contornos da ação oficial. A
integração 8D completa pode corrigir o valor por um fator de forma:

$$
\sigma_{\rm full}
=F_{\rm shape}\,\pi\frac{\hbar c}{r_\perp^2}.
$$

No setor primitivo Ricci--Bohm:

$$
F_{\rm shape}=1.
$$

## Auditoria de discrepância

O cap primitivo não bate metrologicamente com a escala hadrônica de referência.
O desvio em tensão é:

$$
-5.822006\%.
$$

Mantendo $r_\perp=0.860000000000\,\mathrm{fm}$, o coeficiente
necessário para igualar
$\sigma_{\rm had}\simeq0.890000\,\mathrm{GeV/fm}$
seria:

$$
C_{\rm req}=3.335803338528.
$$

Logo, o fator de forma requerido é:

$$
F_{\rm shape,req}
=\frac{C_{\rm req}}{\pi}
=1.061819181018.
$$

Isto equivale a uma correção de forma de
$6.181918\%$ sobre o cap primitivo.

Se mantivermos $F_{\rm shape}=1$, o raio efetivo necessário seria:

$$
r_{\rm req}=0.834589983421\,\mathrm{fm}.
$$

Na parametrização por cap esférico, $C=\pi(1-\cos\chi_0)$. O coeficiente
requerido corresponderia a:

$$
\chi_0=93.544238^\circ,
$$

isto é, cerca de
$3.544238^\circ$ acima do hemisfério.

## Status

O coeficiente do cap primitivo fica derivado:

$$
\boxed{
C_{\rm GDQ}=\pi
}
$$

e a tensão reduzida do cap primitivo permanece:

$$
\boxed{
\sigma_{\rm GDQ}
=0.838184142752\,\mathrm{GeV/fm}.
}
$$

Status conservador: não fechado metrologicamente. O que está fechado é o cap
Ricci--Bohm primitivo. O valor físico final exige derivar
$F_{\rm shape}$ ou $r_{\rm eff}$ a partir do perfil transversal completo.

# Q30 — fator de forma pelo raio efetivo legado

## Enunciado

O cap Ricci--Bohm primitivo com $r_\perp=0,86\,\mathrm{fm}$
gera:

$$
C_{\rm GDQ}=\pi.
$$

Mas esse cap não bate metrologicamente com a escala hadrônica de tensão. O
corpus legado já contém um raio efetivo contraído:

$$
r_{\rm eff}=0,8354\,\mathrm{fm},
$$

registrado em `pt-br/notas/27/nota_27.4_raio_do_proton.md` como raio efetivo
do próton sob compressão muônica.

## Cálculo do fator de forma

Se a contração efetiva atua na seção transversal do tubo, então:

$$
F_{\rm shape}
=\left(\frac{r_\perp}{r_{\rm eff}}\right)^2.
$$

Logo:

$$
F_{\rm shape}
=1.059761067152.
$$

O coeficiente efetivo é:

$$
C_{\rm eff}
=\pi F_{\rm shape}
=3.329337583127.
$$

E a tensão corrigida fica:

$$
\sigma_{\rm GDQ}^{\rm eff}
=F_{\rm shape}\pi\frac{\hbar c}{r_\perp^2}
=\pi\frac{\hbar c}{r_{\rm eff}^2}.
$$

## Resultado

| quantidade | valor |
|---|---:|
| $r_\perp$ primitivo | 0.860000000000 fm |
| $r_{\rm eff}$ | 0.835400000000 fm |
| $F_{\rm shape}$ | 1.059761067152 |
| $C_{\rm eff}$ | 3.329337583127 |
| $\Delta_{\rm eff}=\hbar c/r_{\rm eff}$ | 0.236206584151 GeV |
| $\sigma_{\rm GDQ}^{\rm eff}$ | 0.888274921594 GeV/fm |
| $\sigma_{\rm GDQ}^{\rm eff}$ | 0.175280608043 GeV$^2$ |
| $\sqrt{\sigma_{\rm GDQ}^{\rm eff}}$ | 0.418665269688 GeV |

## Comparação posterior

Com:

$$
\sigma_{\rm had}\simeq0.890000\,\mathrm{GeV/fm},
$$

o desvio fica:

$$
-0.193829\%.
$$

Em $\sqrt{\sigma}$:

$$
-0.096962\%.
$$

## Status conservador

O fator de forma calculado a partir do raio efetivo legado praticamente fecha a
escala de tensão:

$$
\sigma_{\rm GDQ}^{\rm eff}
=0,888274921594\,\mathrm{GeV/fm}.
$$

Isso ainda deve ser classificado como fechamento condicionado ao raio efetivo
setorial $r_{\rm eff}=0,8354\,\mathrm{fm}$.
Para virar previsão metrológica final da Q30, o mesmo $r_{\rm eff}$ precisa
ser rederivado no background transversal da ação oficial, e não apenas
importado do setor legado de raio do próton.

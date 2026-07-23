# Q30 — integração direta do disco Ricci--Bohm

## Objetivo

Reavaliar a tensão do tubo sem tratar $\kappa_\sigma=\pi$ como constante
externa. O fator $\pi$ deve sair da integração direta da seção transversal
circular estabilizada.

## Densidade transversal reduzida

Para o pescoço Ricci--Bohm estabilizado:

$$
r_\perp=0.860000000000\,\mathrm{fm}.
$$

O primeiro quantum transversal é:

$$
\Delta_{\rm GDQ}=\frac{\hbar c}{r_\perp}.
$$

Como o tubo homogêneo possui célula longitudinal natural de ordem
$r_\perp$, a densidade de tensão por área usada no fechamento reduzido é:

$$
\varepsilon_\sigma
=\frac{\hbar c}{r_\perp^4}
=0.360738641266\,\mathrm{GeV/fm^3}.
$$

## Integração direta

$$
\sigma_{\rm GDQ}
=\int_{D_{r_\perp}}\varepsilon_\sigma\,dA.
$$

Com $dA=2\pi s\,ds$:

$$
\sigma_{\rm GDQ}
=\int_0^{r_\perp}
2\pi s\,ds\,
\frac{\hbar c}{r_\perp^4}
=\pi\frac{\hbar c}{r_\perp^2}.
$$

Portanto, o fator $\pi$ é a integral da seção circular; não é ajuste.

## Verificação numérica

| quantidade | valor |
|---|---:|
| $\mathcal A_0$ | 2.323521926595 fm$^2$ |
| $\Delta_{\rm GDQ}$ | 0.229449977209 GeV |
| $\sigma$ analítico | 0.838184142752 GeV/fm |
| $\sigma$ quadratura direta | 0.838184142752 GeV/fm |
| erro relativo da quadratura | -1.325e-16 |
| $\sigma$ | 0.165396345908 GeV$^2$ |
| $\sqrt{\sigma}$ | 0.406689495695 GeV |

## Comparação posterior

Usando apenas como referência fenomenológica posterior:

$$
\sigma_{\rm had}\simeq 0.890000\,\mathrm{GeV/fm}.
$$

O desvio é:

$$
\frac{\sigma_{\rm GDQ}-\sigma_{\rm had}}{\sigma_{\rm had}}
=-5.822006\%.
$$

Em $\sqrt{\sigma}$, o desvio é:

$$
-2.954653\%.
$$

## Auditoria: por que não usar diretamente $\mathcal W_Q(R)$ como tensão?

O funcional homogêneo de garganta já derivado é:

$$
\mathcal W_Q(R)
=\tau\left(
\frac6{R^2}-\frac{Q_T^2}{2\pi^2R^6}
\right)+3\log R.
$$

Com os valores do setor homogêneo vigente:

$$
\mathcal W_Q=1.631598937957.
$$

Se ele fosse usado diretamente como coeficiente de tensão tubular, produziria:

$$
\sigma_{\mathcal W}
=0.435314347824\,\mathrm{GeV/fm},
$$

com desvio:

$$
-51.088276\%.
$$

Isso mostra que $\mathcal W_Q(R)$ não é a tensão tubular completa. Ele mede o
setor homogêneo de garganta normalizado; a tensão do tubo exige a integral
transversal do pescoço Ricci--Bohm ou, no refinamento final, a integral
completa de $\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]$.

## Status

A integração direta da seção reduzida confirma:

$$
\boxed{
\sigma_{\rm GDQ}
=0.838184142752\,\mathrm{GeV/fm}
}
$$

e preserva o acordo de escala com o confinamento hadrônico.

A metrologia final ainda requer resolver o perfil 8D completo para substituir
a densidade reduzida uniforme por:

$$
\sigma_{\rm GDQ}
=\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}].
$$

# Q30 — avaliação reduzida do tubo Ricci--Bohm

## Classificação

Avaliação quantitativa reduzida do background transversal Ricci--Bohm da GDQ.
Não usa QCD/Yang--Mills como ação fundamental e não ajusta parâmetros ao dado
hadrônico. A comparação experimental entra somente depois do cálculo.

Isto ainda não é a avaliação metrológica final de
$\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]$; é o fechamento
numérico reduzido dos quatro itens pendentes:

1. $r_\perp$;
2. $\sigma_{\rm GDQ}$;
3. $\Delta_{\rm GDQ}$;
4. comparação fenomenológica com escala hadrônica.

## Entradas

O raio transversal é tomado do manuscrito legado da GDQ, onde a escala de corte
do estômato/tubo é indicada como $r_c\simeq0,86\,\mathrm{fm}$.

$$
r_\perp = 0.860000000000\,\mathrm{fm}.
$$

Usamos:

$$
\hbar c = 0.1973269804\,\mathrm{GeV\,fm}.
$$

O coeficiente reduzido do pescoço circular é:

$$
\kappa_\sigma=\pi.
$$

Esse fator não é calibrado pelo alvo; ele expressa o primeiro quantum
transversal distribuído na seção circular estabilizada. Na avaliação final,
ele deve ser substituído pela integral direta da densidade transversal da ação
oficial no perfil $q_*$.

## Fórmulas GDQ reduzidas

$$
\mathcal A_0=\pi r_\perp^2.
$$

$$
\Delta_{\rm GDQ}=\frac{\hbar c}{r_\perp}.
$$

$$
\sigma_{\rm GDQ}
=\kappa_\sigma\frac{\hbar c}{r_\perp^2}.
$$

## Resultado

| quantidade | valor |
|---|---:|
| $\mathcal A_0$ | 2.323521926595 fm$^2$ |
| $\Delta_{\rm GDQ}$ | 0.229449977209 GeV |
| $\sigma_{\rm GDQ}$ | 0.838184142752 GeV/fm |
| $\sigma_{\rm GDQ}$ | 0.165396345908 GeV$^2$ |
| $\sqrt{\sigma_{\rm GDQ}}$ | 0.406689495695 GeV |

## Comparação fenomenológica posterior

Para referência externa de escala, usa-se apenas depois do cálculo:

$$
\sigma_{\rm had}\simeq 0.890000\,\mathrm{GeV/fm}
\simeq 0.175621012556\,\mathrm{GeV}^2.
$$

| comparação | GDQ reduzida | referência | desvio |
|---|---:|---:|---:|
| $\sigma$ em GeV/fm | 0.838184142752 | 0.890000000000 | -5.822006% |
| $\sqrt{\sigma}$ em GeV | 0.406689495695 | 0.419071607910 | -2.954653% |

## Leitura física

O resultado está na escala hadrônica correta sem importar a ontologia de QCD.
A tensão linear é da GDQ porque deriva da seção transversal estabilizada e da
homogeneidade longitudinal do tubo.

O gap

$$
\Delta_{\rm GDQ}=0.229450\,\mathrm{GeV}
$$

é a primeira escala transversal do pescoço Ricci--Bohm. Ele não deve ser
identificado automaticamente com uma massa de glueball ou com uma ressonância
específica; ressonâncias físicas exigem a Hessiana completa acoplada e as
condições de contorno do canal experimental.

## Status conservador

Esta avaliação fecha os quatro itens numéricos reduzidos solicitados para Q30.
A pendência metrológica restante é substituir
$\kappa_\sigma=\pi$ pela integral direta

$$
\sigma_{\rm GDQ}
=\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}],
$$

após resolver o perfil estacionário completo do pescoço pela ação oficial.
Essa pendência refina o valor de $\sigma$, mas não reabre o fechamento
estrutural de confinamento linear e gap positivo.

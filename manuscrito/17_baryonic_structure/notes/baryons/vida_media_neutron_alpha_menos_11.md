---
title: "Vida média do nêutron e alpha menos 11"
---

# Vida média do nêutron e $\alpha^{-11}$

Esta nota registra a derivação reduzida da vida média total do nêutron no
setor não polarizado. O resultado é condicional porque usa a norma contraída
do canal beta, não a separação diferencial completa dos coeficientes.

## 1. Espaço de fase

O espaço de fase reduzido é:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

Com:

$$
m_e=0.51099895069\,{\rm MeV},
\qquad
\Delta M=1.29333251\,{\rm MeV},
$$

obtém-se:

$$
I_\beta
=
5.700456936530352\times10^{-17}\,{\rm GeV}^5.
$$

O script preservado calcula esse valor por fórmula analítica e por Simpson.
No refinamento $N=80000$, o erro relativo contra a fórmula analítica fica:

$$
1.377\times10^{-8}.
$$

## 2. Taxa total

A taxa total é:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta.
$$

Com:

$$
\mathcal J_3^2
=
\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

Segue:

$$
\Gamma_n
=
\frac{15}{32}
\alpha^{11}
\frac{m_ec^2}{\hbar}.
$$

Portanto:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}.
$$

Usando:

$$
\alpha^{-1}=137.035999177,
$$

resulta:

$$
\Gamma_n
=
1.137140542406870\times10^{-3}\,{\rm s}^{-1},
$$

$$
\tau_n
=
879.398775004012\,{\rm s},
$$

e:

$$
T_{1/2}
=
609.552781481901\,{\rm s}.
$$

## 3. Comparação

Com a referência:

$$
\tau_n^{\rm ref}
=
878.3\pm0.4\,{\rm s},
$$

o desvio é:

$$
\Delta\tau
=
1.098775004\,{\rm s},
$$

isto é:

$$
\frac{\Delta\tau}{\tau_n^{\rm ref}}
\simeq
1.25\times10^{-3}.
$$

Em unidades do erro $0.4\,{\rm s}$:

$$
\frac{\Delta\tau}{0.4\,{\rm s}}
\simeq
2.75.
$$

Com a referência alternativa $878.4\pm0.5\,{\rm s}$, o desvio fica próximo
de $2.0\sigma$.

## 4. Leitura física

Esse fechamento é para a taxa total reduzida. Ele não substitui o cálculo
diferencial completo de correlações angulares, recoil e termos de superfície.

A distinção é:

$$
\boxed{
\text{taxa total depende de }\mathcal J_3^2;
\qquad
\text{observáveis diferenciais dependem de }C_S,C_T.
}
$$

Verificação autocontida:
[[../../scripts/saida_validar_beta_livre_completo|Saída — validação beta livre GDQ]].

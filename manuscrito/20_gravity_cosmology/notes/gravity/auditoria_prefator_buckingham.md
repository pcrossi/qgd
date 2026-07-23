---
title: "Auditoria do prefator de Buckingham"
---

# Auditoria do prefator de Buckingham

A fórmula reduzida usada para comparação é:

$$
\Pi_G^{\rm GDQ}
=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)}.
$$

Com:

$$
\chi_{\rm Fano}
=
\frac{3\sqrt2}{5}.
$$

Ela é aplicada ao grupo adimensional:

$$
\Pi_G
=
\frac{GM_p^2}{\hbar c}.
$$

Assim:

$$
G_{\rm GDQ}
=
\frac{\hbar c}{M_p^2}
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)}.
$$

## 1. Separação dos fatores

O fator $\alpha^4$ é interpretado como determinante reduzido do canal
Hermitiano bidimensional quando a transmissão efetiva é proporcional a
$\alpha^2I_2$:

$$
\det_{\mathbb C}(\alpha^2I_2)
=
\alpha^4.
$$

O fator $1+\alpha$ é uma correção efetiva de primeira ordem. Ele não deve ser
chamado de classe de Chern, porque classes de Chern são integrais.

O fator $\chi_{\rm Fano}=3\sqrt2/5$ representa uma admitância motivada por
canais. Para virar resultado metrológico, deve sair de um operador espectral
de colagem.

## 2. Leitura do expoente

O expoente não deve ser lido como instanton de Yang--Mills ou como termo novo
na ação. No cálculo reduzido ele vem da cadeia:

$$
\beta_E=2\pi R_H,
\qquad
\tau_\ast=\frac{\beta_E^2}{16},
\qquad
\lambda_{\rm ax}=\frac2{R^2}.
$$

Logo:

$$
\Delta u_v
=
\tau_\ast\pi^2\lambda_{\rm ax}
=
\frac{\pi^4}{2}\frac{R_H^2}{R^2}.
$$

Se a colagem global impõe:

$$
R=\pi^2\sqrt\alpha\,R_H,
$$

então:

$$
\Delta u_v=\frac1{2\alpha},
\qquad
\frac{\mathcal U_\ast}{\mathcal U_0}=e^{-1/(2\alpha)}.
$$

Portanto o expoente é condicional à colagem global. Ele não foi derivado do
bulk local plano isolado.

## 3. O que não deve ser feito

Não se deve adicionar uma correção posterior escolhida para zerar o erro de
$G$. Isso transformaria uma comparação em ajuste.

O resíduo de cerca de $0{,}262\%$ fica registrado como diferença entre a
fórmula reduzida e a metrologia aceita.

Também não se deve:

1. interpretar $1+\alpha$ como classe de Chern literal;
2. esconder planificação dentro de $\chi_{\rm Fano}$ e depois aplicar outro
   jacobiano externo;
3. chamar a rota BPST/Yang--Mills de derivação oficial da GDQ;
4. usar uma correção eletromagnética posterior para remover o resíduo.

## 4. Próximo cálculo necessário

O prefator completo deve vir de:

$$
K_{\rm grav}^{\rm phys}
\to
\det{}'K_{\rm grav}^{\rm phys}
\to
\chi_{\rm Fano}^{\rm spec}
\to
\Pi_G.
$$

Esse é programa metrológico futuro, não falta estrutural do capítulo.

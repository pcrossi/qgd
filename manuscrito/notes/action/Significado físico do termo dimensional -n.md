---
title: "Significado físico do termo dimensional -n"
---

# Significado físico do termo dimensional $-n$

## O que precisa ser explicado

Na ação oficial aparece

$$
\frac{f+\bar f}{2}-n
=
\operatorname{Re}f-n.
$$

Esse termo não é um potencial acrescentado para reproduzir um observável. O
número $n$ já está fixado pela dimensão complexa do domínio:

$$
\dim_{\mathbb R}M=2n.
$$

Seu papel pode ser determinado examinando o estado difusivo de referência da
medida oficial.

## O gaussiano normalizado

Na seção euclidiana plana, tome

$$
F_G
=
\operatorname{Re}f_G
=
\frac{|x|^2}{4\tau},
\qquad
\tau>0.
$$

A medida é

$$
d\mu_G
=
(4\pi\tau)^{-n}
\exp\left(-\frac{|x|^2}{4\tau}\right)d^{2n}x.
$$

Ela é normalizada porque cada uma das $2n$ integrais gaussianas fornece
$\sqrt{4\pi\tau}$:

$$
\int_{\mathbb R^{2n}}d\mu_G=1.
$$

Cada coordenada real tem variância $2\tau$. Portanto,

$$
\langle |x|^2\rangle_G
=
2n(2\tau)
=
4n\tau,
$$

e

$$
\boxed{
\langle F_G\rangle_G
=
\left\langle\frac{|x|^2}{4\tau}\right\rangle_G
=n.
}
$$

Logo $-n$ é a única constante dimensional que faz

$$
\langle F_G-n\rangle_G=0.
$$

## Significado físico

O número $n$ representa a contribuição basal de equipartição das $2n$
direções reais: cada direção quadrática contribui $1/2$. Subtrair $n$ remove
essa contribuição inevitável da dimensionalidade e define o gaussiano
normalizado como zero do setor entrópico.

Assim, a ação não mede como excitação física o simples fato de a densidade
existir em $2n$ dimensões. Ela conserva como conteúdo não trivial:

- curvatura;
- gradientes de densidade e fase;
- torção contida na geometria Hermitiana;
- condições globais e de bordo;
- afastamento em relação ao equilíbrio difusivo.

Sob segundo momento fixo, essa afirmação possui uma forma informacional
exata. Para

$$
u=(4\pi\tau)^{-n}e^{-F}
$$

e para o gaussiano $u_G$,

$$
D_{\rm KL}(u\|u_G)
=
\int u\ln\left(\frac{u}{u_G}\right)d^{2n}x
=
n-\langle F\rangle_u.
$$

Consequentemente,

$$
\boxed{
\langle F-n\rangle_u
=
-D_{\rm KL}(u\|u_G)
\le0.
}
$$

O termo $F-n$ mede, nesse setor, o déficit entrópico em relação ao gaussiano
de referência.

## Por que isso não é a subtração completa de Perelman

Para o mesmo gaussiano,

$$
\nabla F_G=\frac{x}{2\tau}
$$

e, na norma riemanniana real usual,

$$
\left\langle\tau|\nabla F_G|^2\right\rangle_G=n.
$$

O funcional auxiliar real de Perelman usa a dimensão real completa $d=2n$:

$$
\left\langle
\tau|\nabla F_G|^2+F_G-2n
\right\rangle_G
=
n+n-2n
=0.
$$

Portanto, as duas escolhas respondem a perguntas diferentes:

$$
-n
\quad\Longrightarrow\quad
\text{centralização do setor entrópico},
$$

$$
-2n
\quad\Longrightarrow\quad
\text{anulação do funcional real completo de Perelman no gaussiano}.
$$

A ação GDQ conserva a primeira escolha. Ela não deve ser identificada
silenciosamente com o funcional auxiliar $\mathcal W$.

## Efeito sobre as equações variacionais

No setor de dimensão fixa e medida normalizada,

$$
\int_M\mathcal U\,dV_g=1,
$$

uma constante dimensional integrada altera apenas o valor de referência:

$$
\int_M C\mathcal U\,dV_g=C.
$$

Para variações tangentes ao vínculo de normalização,

$$
\delta\int_M C\mathcal U\,dV_g=0,
\qquad
\delta^2\int_M C\mathcal U\,dV_g=0.
$$

Assim, $-n$ não altera a sela nem a Hessiana física nesse setor. Ele define o
zero entrópico. Fora do vínculo normalizado, porém, a constante participa da
variação e não pode ser retirada como se fosse um calibre universal.

## O espaço cosmológico

O espaço cosmológico auxiliar $T^5\times S^3$ possui dimensão real oito. Para
inseri-lo na escrita complexa da ação é necessário especificar uma estrutura
Hermitiana admissível ou um mapa de redução para o bulk oficial. Quando essa
compatibilidade fornece dimensão complexa quatro,

$$
n=4
$$

continua sendo o zero dimensional universal.

Isso não obriga o background cosmológico a possuir ação nula. Sua contribuição
residual é

$$
\mathcal A_{\rm cos}
=
\left\langle
\tau\left(
\mathcal R_{\rm cos}
+
g^{\mu\bar\nu}
\partial_\mu f_{\rm cos}
\partial_{\bar\nu}\bar f_{\rm cos}
\right)
+
\operatorname{Re}f_{\rm cos}
-4
\right\rangle_{\rm cos}.
$$

A curvatura de $S^3$, a torção, o perfil térmico e as condições globais podem
tornar $\mathcal A_{\rm cos}$ diferente de zero. Esse resíduo é conteúdo
físico do background, não erro de normalização.

Se for conveniente medir excitações em relação ao universo cosmológico
estacionário $\Phi_{\rm cos}$, define-se a quantidade relativa

$$
\mathcal S_{\rm rel}[\Phi]
=
\mathcal S_{\rm GDQ}[\Phi]
-
\mathcal S_{\rm GDQ}[\Phi_{\rm cos}].
$$

Essa subtração não modifica a ação oficial nem suas equações. Ela apenas
escolhe o background cosmológico como origem para a comparação de energias.

Portanto existem dois níveis de referência:

$$
\boxed{
-n
=
\text{zero dimensional universal},
}
$$

e

$$
\boxed{
\mathcal S_{\rm GDQ}[\Phi_{\rm cos}]
=
\text{zero físico opcional de um background cosmológico específico}.
}
$$

Eles não devem ser confundidos.

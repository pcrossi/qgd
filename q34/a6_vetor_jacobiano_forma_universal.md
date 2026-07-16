# Q34 — $a_6$ do bloco vetor--jacobiano na forma universal

## 1. Objetivo

Aplicar a fórmula universal de Seeley--DeWitt ao bloco não abeliano

$$
a_6^{\rm VJ}
=
a_6(\Delta_1)-2a_6(\Delta_0),
$$

na convenção de traço usada para Yang--Mills por Vassilevich. O fator dois
representa o par complexo do jacobiano de Faddeev--Popov. Na ação efetiva,
essa combinação recebe o fator global $1/2$:

$$
\Gamma_{\rm VJ}^{(1)}
\sim
\frac12
\left[
a_6(\Delta_1)-2a_6(\Delta_0)
\right].
$$

## 2. Operadores em fundo plano

No gauge de fundo,

$$
(\Delta_1)_\nu{}^\rho
=
-D^2\delta_\nu{}^\rho-E_\nu{}^\rho,
$$

com

$$
E_\nu{}^\rho
=
2\,\operatorname{ad}(F^\rho{}_\nu).
$$

A curvatura da conexão do fibrado vetorial é

$$
\Omega_{\mu\nu}^{(1)}
=
\operatorname{ad}(F_{\mu\nu})\otimes I_{T^*M}.
$$

Para o jacobiano escalar,

$$
\Delta_0=-D^2,
\qquad
E^{(0)}=0,
\qquad
\Omega_{\mu\nu}^{(0)}
=
\operatorname{ad}(F_{\mu\nu}).
$$

## 3. Fórmula universal em espaço plano

Para $f=1$, curvatura de base nula e sem bordo, a fórmula universal integrada
pode ser escrita, após integração por partes, como

$$
\boxed{
\begin{aligned}
a_6(\Delta)
=
\frac1{(4\pi)^2\,360}
\int\operatorname{tr}\big[
&-4\Omega_{ij;k}\Omega_{ij;k}
+2\Omega_{ij;j}\Omega_{ik;k}\\
&-12\Omega_{ij}\Omega_{jk}\Omega_{ki}
-30E_{;i}E_{;i}\\
&+60E^3
+30E\Omega_{ij}\Omega_{ij}
\big]\,d^4x.
\end{aligned}
}
$$

Essa forma segue da expressão não integrada de Vassilevich mediante

$$
\int\operatorname{tr}
(\Omega_{ij;kk}\Omega_{ij})
=
-\int\operatorname{tr}
(\Omega_{ij;k}\Omega_{ij;k}),
$$

$$
\int\operatorname{tr}(EE_{;ii})
=
-\int\operatorname{tr}(E_{;i}E_{;i}),
$$

descartando apenas termos de bordo. Em presença de interface, esses termos
devem ser restaurados e combinados com os coeficientes de bordo.

## 4. Combinação vetor--jacobiano

Como $\Omega^{(1)}=\Omega^{(0)}\otimes I_4$ em quatro dimensões,

$$
\operatorname{tr}_{\rm vec,ad}
\mathcal P(\Omega^{(1)})
=
4\operatorname{tr}_{\rm ad}
\mathcal P(\Omega^{(0)})
$$

para cada monômio $\mathcal P$ que contenha apenas $\Omega$.

Depois da subtração dos dois jacobianos, os termos puros de $\Omega$ recebem
fator líquido

$$
\boxed{4-2=2.}
$$

Os termos que contêm $E$ vêm apenas do operador vetorial. Assim,

$$
\boxed{
\begin{aligned}
a_6^{\rm VJ}
=
\frac1{(4\pi)^2\,360}
\int\bigg\{
&2\operatorname{tr}_{\rm ad}\left[
-4(D_kF_{ij})(D_kF_{ij})
+2(D_jF_{ij})(D_kF_{ik})\right.\\
&\left.\qquad
-12F_{ij}F_{jk}F_{ki}
\right]\\
&+\operatorname{tr}_{\rm vec,ad}\left[
-30(D_iE)(D_iE)
+60E^3
+30E\Omega_{ij}\Omega_{ij}
\right]
\bigg\}\,d^4x.
\end{aligned}
}
$$

Essa é a forma universal do bloco vetor--jacobiano antes da redução de
índices vetoriais.

## 5. Verificação em $a_4$

As mesmas convenções fornecem

$$
\operatorname{tr}_{\rm vec,ad}(E^2)
=
4F_{\mu\nu}^\delta F_{\mu\nu}^\gamma
K_{\delta\gamma},
$$

$$
\operatorname{tr}_{\rm vec,ad}(\Omega^2)
=
-4F_{\mu\nu}^\delta F_{\mu\nu}^\gamma
K_{\delta\gamma},
$$

e, para o jacobiano,

$$
\operatorname{tr}_{\rm ad}(\Omega_0^2)
=
-F_{\mu\nu}^\delta F_{\mu\nu}^\gamma
K_{\delta\gamma}.
$$

Substituindo em $a_4$:

$$
\boxed{
a_4^{\rm VJ}
=
\frac{11}{96\pi^2}
\int
F_{\mu\nu}^\delta F_{\mu\nu}^\gamma
K_{\delta\gamma}\,d^4x,
}
$$

reproduzindo o coeficiente $11/3$. Essa checagem fixa a convenção antes de
reduzir $a_6$.

## 6. Redução ainda necessária

Para chegar à base

$$
\mathcal O_{2G}
=
\operatorname{tr}(D_\rho F_{\mu\nu})^2,
\qquad
\mathcal O_{3G}
=
\operatorname{tr}(F_\mu{}^\nu F_\nu{}^\rho F_\rho{}^\mu),
$$

ainda é necessário:

1. contrair explicitamente os índices vetoriais dos termos com $E$;
2. aplicar a identidade de Bianchi;
3. integrar por partes numa convenção única;
4. restaurar termos de bordo quando o domínio tiver interface;
5. acrescentar curvatura e torção de Bismut no background GDQ.

Nenhum coeficiente final de $\mathcal O_{3G}$ é declarado antes dessa redução.

## 7. Contrações dos termos com \(E\)

Na convenção matricial

$$
[D_\mu,D_\nu]=F_{\mu\nu},
\qquad
E_\nu{}^\rho=2F^\rho{}_\nu,
$$

as contrações vetoriais são

$$
\boxed{
\operatorname{tr}_{\rm vec,ad}(D_iE\,D_iE)
=
-4\operatorname{tr}_{\rm ad}
(D_iF_{\mu\nu}D_iF_{\mu\nu}),
}
$$

$$
\boxed{
\operatorname{tr}_{\rm vec,ad}(E^3)
=
8\operatorname{tr}_{\rm ad}
(F_\mu{}^\nu F_\nu{}^\rho F_\rho{}^\mu),
}
$$

$$
\boxed{
\operatorname{tr}_{\rm vec,ad}
(E\Omega_{ij}\Omega_{ij})=0.
}
$$

O último resultado decorre do traço vetorial
$E_\mu{}^\mu=2F^\mu{}_\mu=0$.

É essencial não misturar esse traço matricial, naturalmente negativo para
geradores anti-Hermitianos no termo quadrático, com uma forma de Killing
positiva definida por sinal oposto. A checagem de $a_4$ fixa a tradução entre
as convenções.

## 8. Redução por Bianchi

Defina

$$
\mathcal A
=
\int\operatorname{tr}
(D_\rho F_{\mu\nu}D_\rho F_{\mu\nu}),
$$

$$
\mathcal B
=
\int\operatorname{tr}
(D_\mu F_{\mu\nu}D_\rho F_{\rho\nu}),
$$

$$
\mathcal C
=
\int\operatorname{tr}
(F_\mu{}^\nu F_\nu{}^\rho F_\rho{}^\mu).
$$

Usando

$$
D_\rho F_{\mu\nu}
+D_\mu F_{\nu\rho}
+D_\nu F_{\rho\mu}=0,
$$

integração por partes e

$$
[D_\rho,D_\mu]X=[F_{\rho\mu},X],
$$

obtém-se

$$
\boxed{
\mathcal A=2\mathcal B-4\mathcal C.
}
$$

Antes dessa identidade, a soma vetor--jacobiano vale

$$
\frac1{(4\pi)^2\,360}
\left(
112\mathcal A+4\mathcal B+456\mathcal C
\right).
$$

Substituindo $\mathcal A$:

$$
\boxed{
a_6^{\rm VJ}
=
\frac1{(4\pi)^2}
\left[
\frac{19}{30}\mathcal B
+\frac1{45}\mathcal C
\right].
}
$$

Esse é o resultado plano, integrado e sem bordo, na convenção de traço
matricial acima.

Na ação efetiva de um loop aparece o fator global $1/2$:

$$
\boxed{
\Gamma_{\rm VJ}^{(1)}\big|_{a_6}
\propto
\frac1{2(4\pi)^2}
\left[
\frac{19}{30}\mathcal B
+\frac1{45}\mathcal C
\right].
}
$$

O sinal físico final também depende da convenção Hermitiana ou
anti-Hermitiana dos geradores e da continuação euclidiana. Os coeficientes
racionais acima pertencem à convenção explicitamente declarada.

## 9. Status

$$
\boxed{
\text{o bloco vetor--jacobiano plano, integrado e sem bordo está reduzido a }
(\mathcal B,\mathcal C).
}
$$

$$
\boxed{
\text{permanecem os termos de bordo e os invariantes mistos Bismut.}
}
$$

## 10. Referências

1. D. V. Vassilevich, “Heat kernel expansion: user's manual”,
   *Physics Reports* **388** (2003) 279--360,
   DOI: 10.1016/j.physrep.2003.09.002,
   arXiv:hep-th/0306138. Fórmulas de $a_4$ e $a_6$ sem bordo e exemplo de
   Yang--Mills em espaço plano.
2. P. B. Gilkey, “The spectral geometry of a Riemannian manifold”,
   *Journal of Differential Geometry* **10** (1975) 601--618. Cálculo
   original do coeficiente $a_6$, conforme a atribuição histórica registrada
   por Vassilevich.

# Q30 — Redução tubular da medida e do setor cinético fundamental

## 1. Escopo

Este passo reduz exatamente as parcelas da ação oficial que não exigem ainda
a fórmula explícita da curvatura escalar de Bismut. Nenhum termo de
Yang--Mills, plaqueta ou potencial confinante é acrescentado.

Trabalha-se no bulk local oficial $\mathbb R^4\times T^4$, em assinatura
euclidiana, por unidade de tempo e de comprimento longitudinal.

## 2. Ansatz KK axisimétrico

Use $(t,z,r,\theta)$ na base e $y^i$ no $T^4$:

$$
\begin{aligned}
ds^2={}&e^{2C(r)}dt^2+e^{2A(r)}dz^2
+e^{2B(r)}\left(dr^2+r^2d\theta^2\right)\\
&+G_{ij}(r)
\left(dy^i+K^i{}_a\mathcal A^a\right)
\left(dy^j+K^j{}_b\mathcal A^b\right).
\end{aligned}
$$

$\mathcal A^a$ é a conexão que resulta das componentes fora da diagonal da
métrica. O rótulo $a$ pode ser projetado posteriormente no setor efetivo da
Q28; ele não é um campo fundamental adicional.

Para o campo fundamental, tome

$$
f(r,\theta)=u(r)+i\left[v(r)+n_C\theta\right],
\qquad n_C\in\mathbb Z.
$$

O inteiro $n_C$ fixa a classe de circulação. Ele não deve ser confundido com
$n=4$, a dimensão complexa do bulk na ação oficial.

## 3. Determinante KK

Pela fórmula de Schur para a métrica KK, as componentes de conexão não alteram
o determinante:

$$
\det g_8=\det h_4\det G_4.
$$

Como

$$
\sqrt{\det h_4}=e^{C+A+2B}r,
$$

segue

$$
\boxed{
\sqrt{\det g_8}
=e^{C+A+2B}r\sqrt{\det G}.
}
$$

Esse resultado é exato e mostra que a conexão entra pela curvatura, não por um
fator de volume escolhido separadamente.

## 4. Medida fundamental

Pela convenção oficial,

$$
\rho=e^{-u},
\qquad
\mathcal U
=\frac{e^{-u}}{(4\pi z_\tau)^4}.
$$

Portanto,

$$
\boxed{
\mathcal U\sqrt{\det g_8}
=\frac{r\,e^{C+A+2B-u}\sqrt{\det G}}
{(4\pi z_\tau)^4}.
}
$$

## 5. Termo cinético de $f$

No ansatz sem dependência em $t,z,y^i$,

$$
g^{M\bar N}\partial_Mf\partial_{\bar N}\bar f
=e^{-2B}
\left[
(u')^2+(v')^2+\frac{n_C^2}{r^2}
\right].
$$

Logo, a densidade radial cinética é

$$
\boxed{
r\,e^{C+A-u}\sqrt{\det G}
\left[
(u')^2+(v')^2+\frac{n_C^2}{r^2}
\right].
}
$$

O cancelamento de $e^{2B}$ é exato. A circulação produz um termo positivo,
mas isoladamente sua integral é logarítmica; uma solução de energia finita
exige que a geometria, a densidade ou a conexão horizontal regularizem o
núcleo e o infinito. Isso deve resultar das equações acopladas, não de um
cutoff manual.

## 6. Integração do contorno causal e do toro

Defina os dois momentos do contorno, mantendo explícita sua possível
dependência no background:

$$
\mathfrak c_1
:=\operatorname{Re}\int_\gamma
\frac{d\tau}{(4\pi z_\tau)^4},
\qquad
\mathfrak c_0
:=\operatorname{Re}\int_\gamma
\frac{d\tau}{\tau(4\pi z_\tau)^4}.
$$

Seja $V_{T^4}^{\rm coord}=\int_{T^4}d^4y$. Após integrar $\theta$ e o toro,
a contribuição por unidade de $t$ e $z$ fica

$$
\boxed{
\begin{aligned}
\sigma_{f,\rm bare}[q]
=\frac{2\pi\hbar V_{T^4}^{\rm coord}}{\Lambda_C^2}
\int_0^\infty dr\,r\sqrt{\det G}\,e^{C+A-u}
\Bigg\{&
\mathfrak c_1
\left[(u')^2+(v')^2+\frac{n_C^2}{r^2}\right]\\
&+\mathfrak c_0e^{2B}(u-4)
\Bigg\}.
\end{aligned}
}
$$

O índice $\rm bare$ significa que ainda faltam a parcela de curvatura e a
subtração do background. Não significa ação nua de uma QFT externa.

## 7. Parcela de curvatura ainda separada

A contribuição restante é

$$
\boxed{
\sigma_{\mathcal R}[q]
=\frac{2\pi\hbar V_{T^4}^{\rm coord}}{\Lambda_C^2}
\mathfrak c_1
\int_0^\infty dr\,
r\,e^{C+A+2B-u}\sqrt{\det G}\,
\mathcal R^B[g,H].
}
$$

A tensão física será

$$
\boxed{
\sigma_{\rm GDQ}
=\left(\sigma_{f,\rm bare}+\sigma_{\mathcal R}\right)[q_*]
-\left(\sigma_{f,\rm bare}+\sigma_{\mathcal R}\right)[q_{\rm vac}].
}
$$

## 8. Resultado e próximo elo

Já estão fixados diretamente pela ação:

1. a medida radial;
2. o peso $e^{-u}$;
3. o coeficiente relativo entre gradientes radial e angular;
4. o termo topológico $n_C^2/r^2$;
5. a separação correta entre os momentos $\mathfrak c_1$ e
   $\mathfrak c_0$;
6. a subtração obrigatória do background.

O próximo elo é calcular $\mathcal R^B[g,H]$ no mesmo ansatz. Para isso é
necessário fixar a 3-forma de torção admissível e sua relação com a métrica
Hermitiana, sem importar um termo $H^2$ independente.

## 9. Classificação

- determinante e medida: identidade exata;
- redução cinética: derivação direta da ação oficial;
- momentos $\mathfrak c_0,\mathfrak c_1$: dados do contorno causal;
- existência do minimizador: ainda não demonstrada;
- valor de $\sigma$: ainda não calculado.

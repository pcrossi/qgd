# Q29 — Contração relativística do triângulo e Berger

## 1. Relação cinemática

Se o comprimento próprio da fibra é reconstruído a partir da contração no
laboratório, a identificação candidata é

$$
q=\gamma_v
=\frac1{\sqrt{1-v^2/c^2}}.
$$

O valor diagnóstico $q^2=14/3$ corresponderia a

$$
\boxed{
\frac{v^2}{c^2}=\frac{11}{14},
\qquad
v=0{,}8864052604c.
}
$$

Isso mostra compatibilidade causal, mas não prova equilíbrio dinâmico.

## 2. Duas energias relativísticas

Para momento angular conservado,

$$
E_J(R,q)
=3\sqrt{\mu^2c^4+\frac{J^2c^2}{R^2q^2}}.
$$

Para velocidade angular fixada por um contorno rotante,

$$
E_\Omega(R,q)
=\frac{3\mu c^2}{\sqrt{1-\Omega^2R^2q^2/c^2}}.
$$

Ambas dependem somente do produto $Rq$. Portanto,

$$
\boxed{
R\partial_RE_{\rm rel}
=q\partial_qE_{\rm rel}.
}
$$

## 3. Condição de equilíbrio conjunto

Se

$$
\partial_R(\mathcal W+E_{\rm rel})=0,
\qquad
\partial_q(\mathcal W+E_{\rm rel})=0,
$$

então necessariamente

$$
R\partial_R\mathcal W
-q\partial_q\mathcal W=0.
$$

Para o funcional de Berger com fluxo conservado, a combinação é exatamente

$$
\boxed{
R\mathcal W_R-q\mathcal W_q
=2+\frac{8(q^2-2)}{R^2}
+\frac{2}{\pi^2R^6q^2}.
}
$$

Para

$$
q^2=\frac{14}{3}>2,
$$

todos os termos são estritamente positivos para qualquer $R>0$. Assim, não
existe solução estacionária no valor requerido, independentemente de $J$,
$\Omega$ ou da massa $\mu$.

## 4. Interpretação

A contração relativística gera uma anisotropia cinemática e uma energia
positiva, mas, quando depende apenas da circunferência $Rq$, suas forças radial
e axial estão presas à mesma proporção. Essa proporção não cancela o gradiente
bidimensional do bulk.

Portanto,

$$
\boxed{
\text{a circulação relativística homogênea, sozinha, não estabiliza }
q^2=14/3.
}
$$

Ela poderá contribuir se a dinâmica do triângulo depender separadamente de
$R$ e $q$ — por exemplo, através de retardamento entre os três centros,
curvatura extrínseca ou velocidades não colineares projetadas — mas esse
operador causal ainda precisaria ser derivado.

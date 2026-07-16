# Q28 — Seleção numérica de três estômatos

## 1. Escopo

O script `solve_selection_q28.py` testa numericamente o teorema horizontal
reduzido de equilíbrio torsional. O número de estômatos e os ângulos não são
fixados no alvo: o programa percorre $N=2,\ldots,8$ e usa 64 condições
iniciais aleatórias para cada $N$.

O funcional é

$$
\mathcal E_{\rm close}
=\frac12\left|\sum_{a=1}^{N}\mathbf T_a\right|^2,
\qquad
|\mathbf T_a|=1.
$$

A rotação global é removida fixando apenas $\theta_1=0$.

## 2. Resultado da execução

| $N$ | Norma do fechamento | Taxa de sucesso | Zeros internos | Gap positivo |
|---:|---:|---:|---:|---:|
| 2 | $1.225\times10^{-16}$ | 1,000 | 0 | 2,000000 |
| 3 | $3.724\times10^{-16}$ | 1,000 | 0 | 1,500000 |
| 4 | $7.988\times10^{-16}$ | 1,000 | 1 | 1,778117 |
| 5 | $4.578\times10^{-16}$ | 1,000 | 2 | 1,838918 |
| 6 | $4.041\times10^{-16}$ | 1,000 | 3 | 1,357519 |
| 7 | $6.206\times10^{-16}$ | 1,000 | 4 | 2,759307 |
| 8 | $5.551\times10^{-16}$ | 1,000 | 5 | 2,295624 |

Todos os casos admitem resultante nula. Entretanto, $N=2$ é colinear. Entre
os junctions não colineares, somente $N=3$ não possui modos zero internos.

## 3. Configuração emergente para $N=3$

Sem fornecer os ângulos finais, a minimização convergiu para

$$
(\theta_1,\theta_2,\theta_3)
=(0^\circ,120^\circ,240^\circ).
$$

As separações são

$$
(120^\circ,120^\circ,120^\circ),
$$

e o espectro angular é

$$
\boxed{
\operatorname{spec}H_3
=\{0,1{,}5,1{,}5\}.
}
$$

O único modo zero é a rotação comum já identificada analiticamente.

## 4. Modos com $N>3$

Os resultados confirmam

$$
\boxed{
\dim\ker H_N-1=N-3,
\qquad
N>3,
}
$$

onde o menos um remove a rotação global. Assim, polígonos maiores fecham, mas
não são críticos isolados do funcional horizontal universal.

## 5. Modo radial homogêneo

Foi incluído o resultado já derivado da ação oficial:

$$
\lambda_{r,0}
=\frac{3}{2\tau}.
$$

Para $\tau=1$,

$$
\lambda_{r,0}=1{,}5>0.
$$

## 6. Veredito

O teste confirma, sem inicializar o triângulo,

$$
\boxed{
N=3
\text{ é o único junction não colinear, fechado e isolado no modelo
horizontal reduzido.}
}
$$

Classificação:

$$
\boxed{
\text{teste numérico convergente do teorema reduzido.}
}
$$

Não é ainda uma avaliação direta da Hessiana multicítrica completa da ação
GDQ. Permanecem por calcular no background real de três centros:

$$
\kappa_{\rm rel},
\qquad
K_\perp,
\qquad
J,
$$

e verificar

$$
H_{\rm rel}-JK_\perp^{-1}J^\dagger>0.
$$


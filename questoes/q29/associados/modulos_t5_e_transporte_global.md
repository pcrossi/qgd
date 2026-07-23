# Q29 — Módulos de $T^5$ e transporte global dos acoplamentos

## 1. Background steady

Considere

$$
K=T^5_{L_1,\ldots,L_5}\times S^3_R
$$

com torção homogênea em $S^3$. O volume é

$$
V_K
=\left[\prod_{A=1}^{5}(2\pi L_A)\right]2\pi^2R^3.
$$

A curvatura e a densidade torsional homogêneas dependem de $R$, mas não dos
$L_A$.

## 2. Cancelamento pela medida normalizada

O modo constante de $f$ é fixado por

$$
\int_K\mathcal U_*dV=1.
$$

Consequentemente, qualquer fator global $V_K$ da integral é cancelado pela
normalização de $\mathcal U_*$. No setor steady,

$$
\mathcal W_{\rm steady}
=\tau\left(
\frac6{R^2}
-\frac{n_B^2}{2\pi^2R^6}
\right)
+\text{constante},
$$

e

$$
\boxed{
\frac{\partial\mathcal W_{\rm steady}}{\partial L_A}=0,
\qquad
\frac{\partial^2\mathcal W_{\rm steady}}
{\partial L_A\partial L_B}=0.
}
$$

Os cinco raios toroidais são módulos planos da ação homogênea.

## 3. Consequência

A ação oficial local não pode determinar numericamente $L_1,ldots,L_5$ nesse
background. Eles só podem ser fixados por:

1. condições cosmológicas de contorno;
2. fluxos mistos com pernas em $T^5$;
3. warp não produto;
4. identificação térmica de $S^1_\beta$;
5. uma condição global de volume/calibração.

Isso explica por que a integração local da interface preservou
$\sin^2\theta_W=3/8$.

## 4. Redução mínima das incógnitas

A decomposição térmica já usada na teoria impõe

$$
T^5=T^4_{\rm int}\times S^1_\beta.
$$

Se a isotropia de $T^4$ for mantida,

$$
L_1=L_2=L_3=L_4=L,
$$

restam apenas

$$
L,qquad L_\beta.
$$

$L_\beta$ é dado pela temperatura/periodicidade causal, e $L$ pode ser obtido
de uma condição global de volume. Essas são condições de contorno, não
resultados da minimização local.

## 5. Transporte dos acoplamentos

Se os modos $W$ e $Y$ forem constantes no toro, os fatores toroidais cancelam
em ambas as normas e

$$
\sin^2\theta_W=\frac38
$$

permanece inalterado. Para haver transporte, os modos devem possuir perfis
toroidais diferentes:

$$
\psi_W(\theta)\ne\psi_Y(\theta).
$$

Então

$$
\frac1{g_a^2}
\propto
\int_{T^5}\!|\psi_a|^2d\mu_T
\int_{S^3}\!|\xi_a|^2d\mu_S.
$$

Nenhum perfil toroidal distinto para $W$ e $Y$ foi ainda derivado nos
documentos. Portanto, o valor operacional do ângulo não pode ser calculado
somente escolhendo raios $L_A$.

## 6. Veredito

O bloqueio é agora um teorema simples:

$$
\boxed{
\text{background produto + modos toroidais constantes}
\Longrightarrow
\sin^2\theta_W=3/8.
}
$$

Para obter outro valor, é necessário calcular a mistura global não produto ou
os modos de Fourier/holonomia distintos do setor fraco e de hipercarga.

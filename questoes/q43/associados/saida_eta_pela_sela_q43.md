# Q43 — amplitude de densidade calculada pela sela

## Classificação

Avaliação direta de uma sela Galerkin reduzida normalizada e teste de
convergência. Não é a sela leptônica física completa em oito dimensões.
O alvo experimental de `g-2` não participa do cálculo.

## 1. Problema variacional

Com circulação unitária fixada, variam-se:

$$
y=(a_1,a_2,\eta,\sigma).
$$

A fase com monodromia é diferenciada por:

$$
P'=\frac{1}{2\pi}+a_1\cos\theta+2a_2\cos2\theta.
$$

A medida é restringida por:

$$
\frac1{2\pi}\int_0^{2\pi}\rho\sqrt g\,d\theta=1.
$$

O modo constante de $\operatorname{Re}f$ fica então determinado por:

$$
F_0=\log I_0(2\sigma-\eta).
$$

A sela resolve $\nabla_y S_{\rm red}=0$.

## 2. Convergência

| N | raízes | a1 | a2 | eta | sigma | norma U | ||grad S|| | eig min |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 | 1 | 5.478823037e-10 | -2.054013509e-12 | 3.472867244e-09 | 1.720979579e-09 | 1.000000000000e+00 | 0.000e+00 | -6.247154919e-02 |
| 2048 | 1 | 3.243608548e-10 | 2.271665450e-12 | 2.026916669e-09 | 1.016777962e-09 | 1.000000000000e+00 | 5.921e-11 | -6.247203793e-02 |
| 4096 | 1 | -7.249600845e-11 | -1.032349560e-13 | -4.699924510e-10 | -2.482808855e-10 | 1.000000000000e+00 | 5.921e-11 | -6.247150832e-02 |
| 8192 | 1 | -2.103530131e-10 | -6.996303574e-13 | -1.339190334e-09 | -6.640015440e-10 | 1.000000000000e+00 | 0.000e+00 | -6.247246698e-02 |

## 3. Resultado

Dentro da caixa de busca $[-5,5]^4$, iniciada a partir de nove pontos,
a única raiz estacionária normalizada é a sela homogênea:

$$
a_1=a_2=\eta_\ell=\sigma=0
$$

com valor numérico final `eta_l = -1.339190333605100e-09`.

A Hessiana reduzida ainda possui um autovalor negativo. Portanto,
a raiz é uma sela do funcional reduzido, não um mínimo estável nem
o background leptônico físico 8D já projetado.

## 4. Consequência para o canal superior

Como $\eta_\ell=0$ nesta sela,

$$
\Delta H_{12}=\eta_\ell T_{123}=0.
$$

A solução não normalizada com $|\eta|\simeq1{,}064$ é excluída:
ela altera a norma total de $\mathcal U\sqrt g$ e não pertence ao
domínio variacional normalizado da GDQ.

O cálculo demonstra um resultado negativo útil: a sela angular
homogênea não gera a correção metrológica superior. Um valor não nulo
de $\eta_\ell$ só pode vir do background 8D não homogêneo, warped ou
misto, com domínio, bordos e projetor físico especificados.

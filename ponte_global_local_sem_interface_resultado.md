# Ponte global--local — teste apontado sem interface artificial

## 1. Hipótese testada

O espaço cosmológico global e o bulk planar local não são duas regiões
físicas separadas por um colar. O segundo é o limite apontado do primeiro.
Somente a fronteira do estômato é uma interface física.

## 2. Operador de referência

No canal radial de uma esfera $S^3_R$, escreva

$$
u(r)=R\sin(r/R)\,\psi(r).
$$

O Laplaciano radial transforma-se em

$$
-\Delta_{S^3_R}^{\rm rad}\psi
=\frac1{R\sin(r/R)}\left(-u''-\frac1{R^2}u\right).
$$

O limite planar radial contém $-u''$. Foi incluído

$$
V(r)=-10e^{-r^2}
$$

somente para produzir um estado ligado de teste; ele não é a Hessiana GDQ.

## 3. Resultado

O limite planar forneceu $\lambda_{\rm flat}=-2{,}5435168586$.

| $R$ | $\lambda_R$ | $\lambda_R-\lambda_{\rm flat}$ | norma em $r\le5$ |
|---:|---:|---:|---:|
| 5 | $-2{,}58351683$ | $-3{,}999997\times10^{-2}$ | $0{,}999998883$ |
| 10 | $-2{,}55351683$ | $-9{,}999970\times10^{-3}$ | $0{,}999998883$ |
| 20 | $-2{,}54601683$ | $-2{,}499970\times10^{-3}$ | $0{,}999998883$ |
| 40 | $-2{,}54414185$ | $-6{,}249885\times10^{-4}$ | $0{,}999998885$ |
| 80 | $-2{,}54367311$ | $-1{,}562476\times10^{-4}$ | $0{,}999998885$ |

Após transportar e normalizar as autofunções no compacto $r\le10$, o erro em
norma do projetor de posto um foi:

| $R$ | erro do projetor |
|---:|---:|
| 5 | $1{,}2094\times10^{-6}$ |
| 10 | $1{,}2094\times10^{-6}$ |
| 20 | $1{,}2091\times10^{-6}$ |
| 40 | $4{,}7192\times10^{-7}$ |
| 80 | $9{,}6571\times10^{-8}$ |

Em toda a sequência,

$$
R^2|\lambda_R-\lambda_{\rm flat}|\simeq1.
$$

Assim,

$$
\boxed{
\lambda_R=\lambda_{\rm flat}-R^{-2}+o(R^{-2}),
}
$$

sem colar, matching bulk--bulk ou sela global--local. A localização permanece
uniforme.

## 4. Consequência

O teste demonstra num canal escalar de referência que a arquitetura

$$
\text{operador global com defeito localizado}
\longrightarrow
\text{operador planar apontado}
$$

é consistente e possui a taxa $O(R^{-2})$ do Lema 2A. Os resultados negativos
dos solvers de colagem não testam necessariamente a ponte correta.

A formulação corrigida distingue:

1. limite cosmológico--local: convergência apontada, sem sela de interface;
2. estômato--bulk: interface física, carga relativa e DtN;
3. herança espectral: convergência de formas, resolventes e projetores.

Ainda é necessário repetir a prova para a Hessiana oficial projetada.

Classificação: teste de consistência; não é prova da Hessiana completa.

Script: `ponte_global_local_teste_sem_colar.py`.

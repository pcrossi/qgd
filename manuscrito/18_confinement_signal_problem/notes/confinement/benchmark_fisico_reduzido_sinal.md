---
title: "Benchmark físico reduzido do problema do sinal"
---

# Benchmark físico reduzido do problema do sinal

Esta nota registra a versão autocontida do benchmark físico reduzido usado para
testar a leitura da GDQ para o problema do sinal fermiônico. O objetivo não é
provar que todo problema fermiônico fortemente correlacionado se torna
polinomial. O objetivo é mais restrito e verificável:

1. construir um ensemble positivo coerente com a GDQ;
2. manter a antissimetria fermiônica como holonomia de fase;
3. obter uma interface unitária a partir de uma impedância Hermitiana reduzida;
4. calcular uma correlação de spin/circulação sem pesos negativos;
5. comparar o sinal e a ordem de grandeza com dados frios de átomos em rede.

## 1. Dados do problema reduzido

O aparelho experimental é representado por uma rede quadrada finita $L\times L$.
No benchmark mínimo foi usado $L=4$, logo $N=L^2=16$. A variável local
$\sigma_i=\pm1$ representa o sinal observado no setor de spin/circulação. Para
separar a alternância antiferromagnética da positividade da medida, define-se
a variável escalonada

$$
x_i=\eta_i\sigma_i,
\qquad
\eta_i=(-1)^{x(i)+y(i)}.
$$

A rede bipartida transfere o sinal alternado para o observável, não para a
medida. Assim, a energia reduzida usada para amostragem é a forma quadrática
positiva

$$
E_{\rm GDQ}(x)
=
\frac{1}{2}x^T K_{\rm red}x,
$$

com

$$
K_{\rm red}
=
m_{\rm gap}I+\kappa_H\Delta_{\rm lat}.
$$

Aqui $\Delta_{\rm lat}$ é o Laplaciano de grafo da rede periódica, $m_{\rm gap}>0$
é o gap reduzido do setor transversal e $\kappa_H>0$ é a rigidez reduzida
herdada da Hessiana física. No teste preservado foram usados

$$
L=4,
\qquad
\beta_{\rm eff}=0.45,
\qquad
\kappa_H=0.35,
\qquad
m_{\rm gap}=0.18.
$$

Esses números pertencem ao benchmark reduzido. Eles não são declarados como
constantes fundamentais da GDQ.

## 2. Medida positiva e sinal como holonomia

A medida de Monte Carlo é

$$
\rho_{\rm MC}(x)
=
\frac{1}{Z}\exp\left(-\beta_{\rm eff}E_{\rm GDQ}(x)\right),
\qquad
Z=\sum_x \exp\left(-\beta_{\rm eff}E_{\rm GDQ}(x)\right).
$$

Como $E_{\rm GDQ}(x)$ é real, a medida é estritamente positiva:

$$
\rho_{\rm MC}(x)>0.
$$

A antissimetria fermiônica não entra como peso negativo. Ela entra como
holonomia de troca,

$$
\operatorname{Hol}(P_{ij})=-1.
$$

Esta é a distinção essencial da GDQ neste setor: o sinal fermiônico é mantido
na fase/circulação, enquanto a densidade usada para amostragem permanece
positiva.

## 3. Interface pela Hessiana reduzida

Para cada aresta $(i,j)$, extrai-se o bloco local da Hessiana reduzida:

$$
K_{ij}
=
K_{\rm red}\big|_{\{i,j\}}.
$$

Normalizando por sua norma espectral, obtém-se a impedância Hermitiana

$$
\mathsf R_{ij}
=
\frac{K_{ij}}{\|K_{ij}\|_2}.
$$

A matriz de interface é então a transformada de Cayley

$$
\mathsf S_{ij}
=
\left(I+i\mathsf R_{ij}\right)^{-1}
\left(I-i\mathsf R_{ij}\right),
$$

com a holonomia fermiônica aplicada ao canal de troca. Como
$\mathsf R_{ij}=\mathsf R_{ij}^\dagger$, segue diretamente que

$$
\mathsf S_{ij}^\dagger\mathsf S_{ij}=I.
$$

No teste numérico autocontido, o erro máximo de unitariedade foi da ordem de
$10^{-16}$, isto é, erro de máquina.

## 4. Observável de correlação

O observável de primeiro vizinho é

$$
C_s(1)
=
\left\langle
\sigma_i\sigma_{i+\hat e}
\right\rangle.
$$

Como $\sigma_i=\eta_i x_i$, o sinal antiferromagnético aparece no observável:

$$
\sigma_i\sigma_j
=
\eta_i\eta_j x_i x_j.
$$

Para primeiros vizinhos em rede bipartida,

$$
\eta_i\eta_j=-1.
$$

Portanto, uma correlação positiva e suave de $x_i x_j$ gera
$C_s(1)<0$ sem introduzir peso negativo na medida.

## 5. Resultados internos do benchmark

Para $L=4$ existem $2^{16}=65536$ configurações, permitindo enumeração exata.
O teste também foi repetido por Metropolis com medida positiva.

| Quantidade | Valor |
|---|---:|
| configurações exatas | $65536$ |
| $C_s(1)$ exato | $-0.1698717343244$ |
| $C_s(1)$ Monte Carlo | $-0.16836$ |
| erro padrão MC | $6.2963\times10^{-4}$ |
| $C_s(2)$ exato | $0.05714802778502$ |
| $C_s(2)$ Monte Carlo | $0.05517$ |
| aceitação MC | $0.75515$ |
| ajuste observado | $\tau_{\rm corr}\sim N^{0.934}$ |

A leitura física é limitada, mas clara: no intervalo de tamanhos testado não
há sinal de explosão exponencial de autocorrelação, e a correlação
antiferromagnética surge com sinal correto usando peso positivo.

## 6. Comparação fenomenológica externa

Os dados externos abaixo são valores locais preservados para comparação com
experimentos de átomos frios em rede. A referência bibliográfica completa deve
ser inserida na pasta de referências do manuscrito; aqui registramos apenas os
valores usados na verificação.

### 6.1 Comparação direta fria

| Fonte local | $k_BT/t$ | Observável | Experimental | GDQ reduzida | Desvio |
|---|---:|---|---:|---:|---:|
| dado frio central | $0.45$ | $C_s(1)$ | $-0.190\pm0.008$ | $-0.1698717$ | $2.516\sigma$ |
| ponto digitizado | $0.45$ | $C_s(1)$ | $-0.210\pm0.020$ | $-0.1698717$ | $2.006\sigma$ |

O benchmark reproduz sinal e ordem de grandeza, mas não é acordo metrológico
com todos os pontos experimentais.

### 6.2 Mapa térmico reduzido

Invertendo a curva positiva do ensemble reduzido para os pontos digitizados,
obtém-se a família fenomenológica

$$
\beta_{\rm eff}
\simeq
\frac{0.291786}{k_BT/t+0.050000}.
$$

Essa inversão mostra que a forma da curva pode ser representada por uma
família térmica positiva da GDQ reduzida, mas ainda não prova que esse mapa
térmico foi derivado diretamente da Hessiana completa do aparelho.

### 6.3 Complemento de Schur do aparelho

O modo observado foi tomado como diferença de circulação no primeiro vínculo da
rede. O complemento ortogonal funciona como banho/aparelho reduzido. A
decomposição dá

$$
K_H=1.93,
\qquad
\chi_A=J K_A^{-1}J^T=0.2229537798681,
$$

e, portanto,

$$
K_{\rm Schur}
=
K_H-JK_A^{-1}J^T
=
1.707046220132.
$$

O segundo momento de resposta reduzido é

$$
\chi_2
=
J K_A^{-2}J^T
=
0.1593233959409.
$$

O melhor mapa Schur não ajustado usado na comparação foi

$$
\beta_{\rm Schur}(\Theta)
=
\frac{\mu_A}{\Theta+\Theta_A},
\qquad
\mu_A=0.554521554,
\qquad
\Theta_A=0.616921719,
$$

com $\Theta=k_BT/t$.

| $k_BT/t$ | $C_s(1)$ experimental | $C_s(1)$ GDQ--Schur | Desvio |
|---:|---:|---:|---:|
| $0.00$ | $-0.350\pm0.020$ | $-0.450850$ | $-5.042\sigma$ |
| $0.45$ | $-0.210\pm0.020$ | $-0.210714$ | $-0.036\sigma$ |
| $0.55$ | $-0.240\pm0.020$ | $-0.180111$ | $2.994\sigma$ |
| $0.90$ | $-0.110\pm0.020$ | $-0.129634$ | $-0.982\sigma$ |
| $1.50$ | $-0.050\pm0.020$ | $-0.093611$ | $-2.181\sigma$ |

O ponto $k_BT/t=0.45$ é reproduzido muito bem. A curva completa ainda mostra
resíduos, especialmente no limite frio e em alta temperatura. O ponto
$k_BT/t=0.55$ deve ser tratado com cautela porque a digitização preservada não
é monotônica em relação aos pontos vizinhos.

## 7. Correção de largura térmica

A largura Schur reduzida foi

$$
\Theta_A^{\rm Schur}
\simeq
0.616921719.
$$

O mapa efetivo ajustado à curva pedia

$$
\Theta_A^{\rm fit}
\simeq
0.721527850.
$$

Logo o resíduo de largura era

$$
\Delta\Theta_A
\simeq
0.104606131.
$$

Correções espectrais do banho geraram contribuições positivas da ordem correta,
por exemplo

$$
\Delta\Theta_A
\simeq
0.0690713
$$

para o candidato $\sum J_k^2/(\lambda_k(\lambda_k+K_{\rm Schur}))$. Isso indica
que a direção física é plausível, mas que o modelo reduzido ainda omite canais
dissipativos, mobilidade causal ou pesos térmicos reais do aparelho.

## 8. Veredito

O benchmark físico reduzido fecha a afirmação estrutural da GDQ:

$$
\boxed{
\text{é possível amostrar o setor fermiônico testado com medida positiva,}
\quad
\text{mantendo o sinal como holonomia.}
}
$$

Ele também fornece comparação fenomenológica útil:

$$
C_s(1)_{\rm GDQ}
=
-0.1698717
$$

contra valores frios experimentais/digitizados da ordem de $-0.19$ a $-0.21$.

O que não está provado por este benchmark é uma solução algorítmica universal
do problema do sinal. Para essa afirmação forte ainda seriam necessários:

1. uma Hessiana GDQ completa, não apenas reduzida;
2. mapa térmico do aparelho derivado de $\mathsf R_{\rm app}$ e da mobilidade
   causal;
3. cotas assintóticas de variância e autocorrelação;
4. benchmarks em famílias maiores de Hamiltonianos/contornos, com parâmetros
   congelados antes da comparação.

Assim, o status correto é: problema do sinal fechado estruturalmente na GDQ e
validado em benchmark reduzido; solução computacional geral permanece programa
futuro.

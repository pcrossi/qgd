# Resultado numérico do ramo integrável discreto $J_{\pi/2}$

## 1. Classificação

Teste numérico de existência no ansatz homogêneo cohomogeneidade--1. O
resultado é negativo para uma sela não degenerada; não é um no-go para modos
integráveis não homogêneos.

## 2. DAE implementada

`ponte_global_local_ramo_J_discreto_dae.py` implementa o funcional
Lagrangiano restrito com os multiplicadores auxiliares $\beta$ e $\ell$.
Velocidades e multiplicadores são eliminados simultaneamente pelo sistema
algébrico bordado.

Os testes deram:

$$
\|\dot q_{\rm rec}-\dot q\|_{\rm colar}
=4{,}88\times10^{-15},
$$

$$
\|\dot q_{\rm rec}-\dot q\|_{\rm ext}
=1{,}28\times10^{-15},
$$

com erros dos multiplicadores abaixo de $1{,}4\times10^{-16}$. A condição
$\mathcal F_I=0$ é uma linha do bloco algébrico e não uma reprojeção posterior.

## 3. Regularidade e redundância

Cada garganta foi parametrizada por

$$
(r_0,\beta_0,\ell_0,L),
$$

com $a_0=c_0$ e velocidades refletidas nulas. Na seção exatamente simétrica,
$\ddot a_0=\ddot c_0$ não fixa $\ell_0$ isoladamente; o matching deve
selecionar sua classe.

A SVD encontrou uma redundância exata:

1. os resíduos de continuidade de $y$ e $z$ são idênticos;
2. existe uma nulidade correspondente nos multiplicadores $\ell_L,\ell_R$.

Removeu-se somente o traço duplicado e acrescentou-se uma condição de gauge
transversal ao vetor nulo. O sistema resultante possui posto completo. Nenhuma
equação física foi descartada.

## 4. Normalização global corrigida

O acumulador usado pela energia deve integrar todo o domínio:

$$
Z=Z_L+Z_{\rm ext}+Z_R.
$$

O solver do ramo discreto foi implementado dessa forma. Usar apenas
$Z_{\rm ext}$ produz divergência artificial quando o comprimento exterior é
ligado por homotopia.

## 5. Homotopia e fuga para o bordo

Como a semente histórica era off-constraint e explodia no exterior, iniciou-se
uma âncora regular com comprimento exterior $L_{\rm ext}=0{,}02$. Raio e
energia foram inicialmente congelados nos valores da própria semente, sem
usar alvos experimentais.

Depois da redução de gauge e da ampliação apenas dos limites numéricos dos
comprimentos, observou-se:

$$
\|\mathfrak F\|_\infty:
1{,}807\times10^{-3}
\longrightarrow
4{,}484\times10^{-4},
$$

simultaneamente a

$$
\log L_L:-3{,}52\longrightarrow-4{,}08,
$$

$$
\log L_R:-4{,}00\longrightarrow-5{,}63.
$$

A redução do resíduo ocorre pela contração dos colares em direção ao bordo
degenerado $L_L=L_R=0$, não pela aproximação de uma raiz interior. O resíduo
estrito final foi

$$
\begin{aligned}
(&7{,}1795\times10^{-5},
1{,}8847\times10^{-5},
-5{,}6864\times10^{-6},
2{,}1085\times10^{-6},\\
&3{,}3477\times10^{-7},
-4{,}2521\times10^{-7},
4{,}4836\times10^{-4},
3{,}5702\times10^{-5},\\
&-3{,}8637\times10^{-7},
1{,}1128\times10^{-5},
-9{,}5596\times10^{-8}).
\end{aligned}
$$

O termo dominante é o matching do momento dilatônico $p_u$.

## 6. Veredito

$$
\boxed{
\text{o ramo homogêneo discreto }J_{\pi/2}
\text{ não fornece uma sela bulk--interface não degenerada.}
}
$$

Como não foi obtida base exata nem mesmo na âncora anterior aos alvos físicos,
não é legítimo continuar para $K_\gamma=1$, $h=1$ e comprimento exterior
completo. Não há background para as Portas C/D.

O resultado preserva aberta apenas a rota por modos integráveis não
homogêneos, como o setor Beltrami já reservado no motor extensível.

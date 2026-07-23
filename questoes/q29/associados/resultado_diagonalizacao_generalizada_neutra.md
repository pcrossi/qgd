# Q29 — Resultado da diagonalização generalizada neutra

## 1. Matrizes sem entrada experimental

A matriz cinética on-shell calculada é

$$
\mathbf K
=
\frac{\mathcal K_{\rm base}}4
\begin{pmatrix}
1&\delta_B\\
\delta_B&1
\end{pmatrix},
$$

com

$$
\mathcal K_{\rm base}=41{,}594825709,
\qquad
\delta_B=-0{,}2709378871.
$$

A Hessiana de massa da interface, sem sua escala positiva comum, é

$$
\mathbf M^2
=
\frac14
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
$$

Nenhum ângulo de Weinberg ou massa experimental entra nessas matrizes.

## 2. Problema generalizado

Foi resolvido

$$
\mathbf M^2v_a
=
m_a^2\mathbf Kv_a.
$$

Os autovalores são

$$
\boxed{
m_\gamma^2=0,
\qquad
m_Z^2=0{,}0378326150
}
$$

na escala comum omitida da Hessiana de interface.

O kernel é exatamente

$$
v_\gamma\propto
\begin{pmatrix}1\\1\end{pmatrix},
$$

confirmando

$$
Q=T_3+Y
$$

sem inserir previamente $\theta_W$.

## 3. Norma física do gerador não quebrado

Como $Q$ possui cargas inteiras já fixadas, seu vetor de coeficientes não pode
ser reescalado para ajustar o acoplamento. Sua norma cinética é

$$
\frac1{e^2}
=
\begin{pmatrix}1&1\end{pmatrix}
\mathbf K
\begin{pmatrix}1\\1\end{pmatrix}
=
\frac{\mathcal K_{\rm base}}2(1+\delta_B).
$$

Numericamente,

$$
\boxed{
\frac1{e^2}=15{,}1626057595.
}
$$

Isso produziria

$$
\boxed{
\alpha^{-1}=190{,}5389235.
}
$$

e não $132{,}4576690$.

## 4. Consequência

A diagonalização final desta rota funciona estruturalmente:

1. encontra exatamente um fóton sem massa;
2. encontra um modo neutro massivo e positivo;
3. deriva $Q=T_3+Y$ sem usar o ângulo experimental.

Entretanto, ela exclui a hipótese de que a matriz cinética construída com o
background radial atual forneça a normalização eletromagnética observada.

Não há mais um fator pequeno faltante nessa cadeia. A divergência indica que
ao menos uma identificação anterior é incompleta:

1. o background cohomogeneidade-um $Y=\cos\chi$ não representa sozinho a
   métrica Hermitiana completa do fibrado de Hopf;
2. a redução radial perde componentes horizontais da matriz cinética;
3. a matriz on-shell deve ser calculada na geometria anisotrópica completa,
   não reconstruída apenas por uma média condicional sobre $S^2$.

## 5. Veredito científico

$$
\boxed{
\text{a Q29 permanece aberta na predição absoluta de }\alpha.
}
$$

O mecanismo eletrofraco, o fóton sem massa e o modo $Z$ permanecem válidos.
O que falhou foi somente a suficiência da truncagem radial para a norma
cinética absoluta.

O cálculo reproduzível está em
`questoes/q29/associados/diagonalizacao_generalizada_neutra_q29.py`.

# Q28 — Fibrado de Berry do kernel sobre $T^5$

## 1. Kernel explícito

No setor

$$
j=\frac12,
\qquad
m=1,
\qquad
\beta=-\frac32,
$$

o operador adimensional é

$$
aD
=2\boldsymbol\sigma\cdot\boldsymbol L-\sigma_3.
$$

Na base

$$
\left{
|\uparrow,-\tfrac12\rangle,
|\uparrow,+\tfrac12\rangle,
|\downarrow,-\tfrac12\rangle,
|\downarrow,+\tfrac12\rangle
\right},
$$

sua matriz é

$$
aD
=
\begin{pmatrix}
0&0&0&0\\
0&-2&2&0\\
0&2&0&0\\
0&0&0&2
\end{pmatrix}.
$$

O kernel interno desse bloco é unidimensional:

$$
v_0
=|\uparrow,-\tfrac12\rangle
=
\begin{pmatrix}
1\\0\\0\\0
\end{pmatrix}.
$$

Entretanto, cada bloco de spin $j$ possui multiplicidade espectadora
$2j+1$. Para $j=1/2$, escolha uma base $r_+,r_-$ desse fator. Os dois modos
zero completos são

$$
\boxed{
\psi_+=v_0\otimes r_+,
\qquad
\psi_-=v_0\otimes r_-.
}
$$

Isso explica

$$
h_1=2
$$

sem duplicar artificialmente o kernel da matriz $4\times4$.

## 2. Uma holonomia toroidal

Seja $\theta_1\sim\theta_1+2\pi$ o primeiro ciclo de $T^5$. A ação unitária
mais geral no kernel que preserva sua dimensão é

$$
\Psi(\theta_1)
=\Psi(0)U_1(\theta_1),
$$

com

$$
U_1(\theta_1)=e^{i\theta_1Q_1},
$$

onde $Q_1$ é Hermitiano e possui autovalores inteiros para periodicidade
ordinária.

Em uma base que diagonaliza $Q_1$,

$$
Q_1
=
\begin{pmatrix}
q_{1+}&0\\
0&q_{1-}
\end{pmatrix}.
$$

Logo,

$$
\psi_A(\theta_1)
=e^{iq_{1A}\theta_1}\psi_A(0).
$$

## 3. Conexão de Berry em $S^1$

Com a convenção anti-Hermitiana,

$$
\mathcal A_1
=\Psi^\dagger\partial_{\theta_1}\Psi
=iQ_1.
$$

Como a base possui uma única coordenada,

$$
\boxed{
\mathcal F_{11}=0.
}
$$

A holonomia pode ser não trivial:

$$
\operatorname{Hol}_1
=\exp\left(\oint\mathcal A_1d\theta_1\right)
=e^{2\pi iQ_1},
$$

mas, para cargas inteiras, ela é a identidade no fibrado ordinário. Cargas
fracionárias exigiriam o quociente global já tratado, não gerariam curvatura
local por si mesmas.

## 4. Generalização para $T^5$

Para cinco ciclos,

$$
U(\boldsymbol\theta)
=\exp\left(i\sum_{k=1}^5\theta_kQ_k\right).
$$

Como

$$
\pi_1(T^5)=\mathbb Z^5
$$

é abeliano, uma representação unitária ordinária exige

$$
[Q_i,Q_j]=0.
$$

Assim, os cinco geradores podem ser diagonalizados simultaneamente e

$$
\mathcal A
=i\sum_{k=1}^5Q_kd\theta_k.
$$

A curvatura é

$$
\mathcal F
=d\mathcal A+\mathcal A\wedge\mathcal A.
$$

Como $Q_k$ são constantes e comutam,

$$
\boxed{
\mathcal F=0.
}
$$

## 5. Segundo número de Chern

Segue imediatamente:

$$
c_2(E_G)
=-\frac1{8\pi^2}
\operatorname{tr}(\mathcal F\wedge\mathcal F)
=0.
$$

Como $H^*(T^5,\mathbb Z)$ não possui torção, um fibrado plano não esconde um
$c_2$ torsional não detectado pelas formas diferenciais.

Portanto,

$$
\boxed{c_2(E_G)=0}
$$

para a família mínima de holonomias toroidais ordinárias.

## 6. Avaliação de $N_{ab}$

Na decomposição

$$
c_2(E_G)=a_4+b_1\smile u_3,
$$

temos

$$
a_4=0,
\qquad
b_1=0.
$$

Logo,

$$
\boxed{
N_{ab}
=\left\langle a_4\smile b_1,[T^5]\right\rangle
=0.
}
$$

Consequentemente,

$$
\boxed{
N_G=\frac{N_{ab}}6=0
}
$$

para a família mínima construída apenas por holonomias abelianas de $T^5$.

## 7. Significado do resultado negativo

Esse resultado não elimina o índice APS local unitário. Ele mostra que o
transporte plano e fatorizado dos dois modos zero pelo toro não produz uma
família geracional global quiral.

Para obter $c_2\ne0$, é necessário pelo menos um dos seguintes mecanismos:

1. dependência não fatorizada dos modos zero em $T^5\times S^3$;
2. textura que misture coordenadas toroidais e a 3-forma $u_3$;
3. holonomias projetivas não comutativas, com cociclo central;
4. cruzamentos de nível que tornem o projetor do kernel não globalmente
   constante;
5. uma conexão de Berry derivada de uma Hessiana global não produto.

Nenhum desses mecanismos está especificado atualmente pela família mínima.

## 8. Status

$$
\boxed{
\text{os seis passos foram executados para a família toroidal mínima e
produzem }\mathcal F=c_2=N_{ab}=0.
}
$$

Portanto, o número três não emerge de holonomias abelianas fatorizadas. A
próxima hipótese a testar deve ser a colagem projetiva $\mathbb Z_6$, pois ela
é a única estrutura não fatorizada já presente na Q28.

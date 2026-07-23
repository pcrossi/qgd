# Q30 — Torção de Bismut no ansatz tubular Hermitiano

## 1. Convenção oficial

Adota-se a convenção já fixada no corpus:

$$
\boxed{
\mathcal R_{\rm GDQ}
=R_{\rm LC}-\frac1{12}H_{MNP}H^{MNP},
\qquad
H=d^c\omega.
}
$$

$H$ não é acrescentado como campo fundamental independente: ele é a torção da
estrutura Hermitiana $(g,J)$.

## 2. Subansatz diagonal compatível com $J$

Para executar uma primeira auditoria exata, restrinja o ansatz anterior a
quatro planos Hermitianos:

$$
\begin{aligned}
ds^2={}&e^{2W(r)}(dt^2+dz^2)
+e^{2B(r)}(dr^2+r^2d\theta^2)\\
&+e^{2P(r)}[(dy^1)^2+(dy^2)^2]
+e^{2Q(r)}[(dy^3)^2+(dy^4)^2].
\end{aligned}
$$

A estrutura complexa atua por

$$
Jdt=dz,
\qquad
Jdr=r\,d\theta,
\qquad
Jdy^1=dy^2,
\qquad
Jdy^3=dy^4,
$$

com $J^2=-1$ completado nos parceiros. A forma Hermitiana é

$$
\omega
=e^{2W}dt\wedge dz
+e^{2B}r\,dr\wedge d\theta
+e^{2P}dy^1\wedge dy^2
+e^{2Q}dy^3\wedge dy^4.
$$

## 3. Cálculo de $H=d^c\omega$

Como $d[r e^{2B}dr\wedge d\theta]=0$,

$$
d\omega
=2W'e^{2W}dr\wedge dt\wedge dz
+2P'e^{2P}dr\wedge dy^1\wedge dy^2
+2Q'e^{2Q}dr\wedge dy^3\wedge dy^4.
$$

Até o sinal global de $d^c$, que não altera $|H|^2$,

$$
\boxed{
\begin{aligned}
H={}&2rW'e^{2W}d\theta\wedge dt\wedge dz\\
&+2rP'e^{2P}d\theta\wedge dy^1\wedge dy^2\\
&+2rQ'e^{2Q}d\theta\wedge dy^3\wedge dy^4.
\end{aligned}
}
$$

## 4. Norma torsional

Usando $|H|^2=H_{MNP}H^{MNP}$, cada componente independente de 3-forma
aparece $3!=6$ vezes na contração. Os fatores de warp cancelam nos pares e
resulta

$$
\boxed{
|H|^2
=24e^{-2B}\left[(W')^2+(P')^2+(Q')^2\right].
}
$$

Portanto,

$$
\boxed{
-\frac1{12}|H|^2
=-2e^{-2B}\left[(W')^2+(P')^2+(Q')^2\right].
}
$$

Esse coeficiente sai da convenção oficial; não é o valor escolhido no solver
histórico.

## 5. Teste de torção fechada

Se o background exige a condição strong-KT $dH=0$, então

$$
\boxed{
(rW'e^{2W})'=0,
\qquad
(rP'e^{2P})'=0,
\qquad
(rQ'e^{2Q})'=0.
}
$$

Equivalentemente,

$$
r(e^{2W})'=c_W,
\qquad
r(e^{2P})'=c_P,
\qquad
r(e^{2Q})'=c_Q.
$$

Logo,

$$
e^{2W}=a_W+c_W\log r,
$$

e analogamente para $P,Q$. Regularidade simultânea no eixo $r=0$ e
aproximação a constantes quando $r\to\infty$ impõem

$$
\boxed{c_W=c_P=c_Q=0.}
$$

Assim, no subansatz diagonal, regular, assintoticamente produto e strong-KT,

$$
\boxed{H=0.}
$$

## 6. No-go do tubo diagonal simples

O resultado não exclui confinamento na GDQ. Ele exclui uma realização
específica:

$$
\boxed{
\text{o tubo torsional não pode ser simultaneamente diagonal,
axisimétrico, regular, assintoticamente produto e strong-KT não trivial.}
}
$$

Para obter torção não nula sem violar as condições oficiais, pelo menos uma
das seguintes estruturas deve estar presente e ser derivada:

1. componentes KK fora da diagonal com curvatura não trivial;
2. fluxo harmônico/topológico no $T^4$;
3. geometria de colagem com mais de um patch;
4. fonte/defeito no eixo, tratada como dado de bordo da classe topológica;
5. relaxamento explícito de $dH=0$, caso a tarefa use KT geral em vez de
   strong-KT.

## 7. Consequência para $\sigma$

No subansatz auditado, a parcela torsional da tensão reduz-se a zero sob as
condições globais acima. A positividade de $\sigma$ não pode ser atribuída a
um $|H|^2$ escolhido. Ela deve vir do setor de circulação de $f$, da
curvatura Levi--Civita e/ou de componentes KK não diagonais derivadas.

## 8. Classificação

- fórmula de $H$ e de $|H|^2$: derivação direta no subansatz;
- no-go: teorema condicional às hipóteses de regularidade, assíntota e
  strong-KT;
- exclusão global do confinamento: não demonstrada;
- próximo passo: incluir a conexão KK não diagonal já exigida pelo setor de
  holonomia de cor.

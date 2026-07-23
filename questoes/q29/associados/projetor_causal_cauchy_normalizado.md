# Q29 — Projetor causal de Cauchy sem alteração da ação oficial

## 1. A ação oficial permanece intacta

A ação da GDQ continua sendo

$$
\mathcal S_{\rm GDQ}
=
\oint_\gamma
\mathscr L(\tau)
\frac{d\tau}{\tau}.
$$

Não se insere o fator $1/(2\pi i)$ dentro de sua definição e não se altera o
funcional variacional.

## 2. O que já era usado nas equações locais

Na Q4, a variação foi expandida como

$$
E(\tau)=\sum_{m\in\mathbb Z}E_m\tau^m
$$

e calculou-se

$$
\oint_\gamma
E(\tau)\frac{d\tau}{\tau}
=2\pi iE_0
$$

para winding unitário. Portanto, quando a teoria identifica a equação física
com $E_0=0$, ela já está usando implicitamente o operador de extração do
coeficiente de Laurent.

## 3. Definição do mapa físico

Para um contorno com número de winding

$$
w_\gamma
=
\frac1{2\pi i}
\oint_\gamma\frac{d\tau}{\tau}
\in\mathbb Z,
$$

defina o projetor causal

$$
\boxed{
\mathfrak P_\gamma[F]
:=
\frac1{2\pi i\,w_\gamma}
\oint_\gamma
F(\tau)\frac{d\tau}{\tau}.
}
$$

Para $w_\gamma=1$,

$$
\mathfrak P_\gamma[F]=F_0.
$$

Isso não é uma nova constante física. É a fórmula de Cauchy para o coeficiente
que a formulação local da GDQ já declara físico.

## 4. Ação física reconstruída

A ação oficial é o funcional complexo de contorno. A ação física reconstruída
é seu coeficiente causal orientado:

$$
\boxed{
\mathcal S_{\rm phys}
=
\mathfrak P_\gamma[\mathscr L].
}
$$

Se for necessário impor explicitamente a condição de realidade hermitiana,
usa-se

$$
\mathcal S_{\rm phys}^{\mathbb R}
=
\frac12
\left(
\mathfrak P_{\gamma_+}[\mathscr L]
+
\overline{\mathfrak P_{\gamma_-}[\mathscr L]}
\right),
$$

onde $\gamma_-$ é o contorno conjugado com orientação causal correspondente.
Para um coeficiente hermitiano, essa expressão retorna simplesmente $F_0$
real.

## 5. Compatibilidade variacional

Como $\mathfrak P_\gamma$ é linear,

$$
\delta\mathcal S_{\rm phys}
=
\mathfrak P_\gamma[\delta\mathscr L].
$$

Logo, as equações previamente derivadas não mudam. Um fator global não nulo
jamais alteraria os extremos; aqui, além disso, o projetor apenas explicita a
extração de Laurent já empregada na Q4.

## 6. Localização causal

Para uma inserção meromorfa $F$, a mesma definição fornece

$$
\mathfrak P_\gamma[F]
=
\frac1{w_\gamma}
\sum_{a\in\operatorname{Int}\gamma}
\operatorname{Res}_{\tau_a}
\frac{F(\tau)}{\tau}.
$$

O contorno é determinado pela classe causal; não se escolhe um polo para
ajustar um observável. Para uma função regular na origem, o resultado é apenas
$F(0)$. Para o resolvente, contribuem todos os polos que pertencem ao domínio
analítico definido pela mesma prescrição causal.

## 7. Consequência para a normalização eletromagnética

Na redução de Hopf,

$$
\mathscr L_Q(\tau)
=
\frac14K_Q(\tau)
\int_{M_4}|F_Q|^2dV_4.
$$

Portanto,

$$
\frac1{e^2}
=
\mathfrak P_\gamma[K_Q].
$$

A contribuição causal para $\mathcal C_{\rm em}$ é exatamente unitária:

$$
\boxed{\mathcal N_{\rm causal}=1.}
$$

Não resta um fator arbitrário $2\pi$, $2\pi i$ ou uma escolha da parte real.
Esses fatores pertencem à representação integral do projetor e se cancelam
na extração normalizada.

## 8. O que ainda não foi determinado

Depois dessa localização, a constante absoluta depende somente de:

1. normalização do gerador de Hopf na métrica interna;
2. conversão dimensional do coeficiente $\hbar/\Lambda_C^2$ para a ação 4D;
3. valor on-shell de $K_Q$ no background interno.

O item 3 já foi calculado numericamente. O contorno causal não é mais uma
pendência de normalização.

## 9. Normalização do gerador eletromagnético

O modo fundamental satisfaz

$$
u\sim(1,2)_{1/2}.
$$

No dupleto,

$$
T_3
=
\begin{pmatrix}
1/2&0\\
0&-1/2
\end{pmatrix},
\qquad
Y=\frac12I,
$$

e portanto

$$
Q=T_3+Y
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
$$

Assim,

$$
e^{2\pi iQ}=I,
$$

e a órbita carregada possui período mínimo $2\pi$. Seja $K_Q$ o vetor de
Killing dessa órbita e normalize a conexão de Hopf pela própria condição de
conexão principal

$$
\eta(K_Q)=1.
$$

Na deformação métrica

$$
\eta\longmapsto\eta+\kappa_QA_Q,
$$

uma transformação $A_Q\mapsto A_Q+d\lambda$ deve ser compensada pela
translação da fibra gerada por $K_Q$ com o mesmo parâmetro $\lambda$. Como
$\lambda\sim\lambda+2\pi$, segue

$$
\boxed{\kappa_Q=1.}
$$

Escolher $\kappa_Q\ne1$ equivaleria a redefinir simultaneamente a carga
inteira ou o período da fibra. Isso não é permitido depois de fixados
$Q=T_3+Y$ e a classe primitiva de Hopf.

Com isso, a normalização do gerador também deixa de ser pendência. O único
fator restante é a conversão dimensional absoluta do prefator da ação.

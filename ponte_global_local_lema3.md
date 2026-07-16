# Ponte global--local da GDQ — Lema 3: transporte dos campos e da Hessiana

> [!important] Atualização arquitetural
> BI foi substituída pela família apontada com estômato localizado. Ver
> `ponte_global_local_lemas_sem_colar.md`.

## 1. Escopo e dependência lógica

Este lema é demonstrado sob a Hipótese BI, registrada em
`ponte_global_local_hipotese_BI.md`. Seu objetivo é construir corretamente os
espaços de Hilbert variáveis, o transporte local e a convergência das formas
quadráticas da segunda variação oficial.

Não se presume gap espectral. Consequentemente, o lema pode fornecer
convergência de formas e resolvente forte, mas não ainda convergência em norma
dos projetores de um modo isolado.

## 2. Medidas físicas

Para cada valor admissível de $\tau$, defina

$$
d\mu_{\varepsilon,\tau}
=\mathcal U_\varepsilon(\tau),dV_{g_\varepsilon},
$$

e

$$
d\mu_{P,\tau}=\mathcal U_P(\tau),dV_{g_P}.
$$

Os espaços de Hilbert para um fibrado físico $E$ são

$$
\mathcal H_{\varepsilon,\tau}
=L^2(M_\varepsilon,E_\varepsilon,d\mu_{\varepsilon,\tau}),
$$

$$
\mathcal H_{P,\tau}
=L^2(M_P,E_P,d\mu_{P,\tau}).
$$

O fibrado $E$ deve ser escolhido para cada bloco da Hessiana. Para a variação
fundamental mínima,

$$
E
=\operatorname{Sym}^2_JT^*M
\oplus\mathbb C,
$$

onde o primeiro fator contém variações Hermitianas da métrica e o segundo
contém $\delta f$. Variações de $H$ não constituem um terceiro campo livre:

$$
\delta H
=\delta(d^c_J\omega)
$$

é determinada por $(\delta g,\delta J)$.

## 3. Densidade de transporte

Em uma carta apontada, escreva

$$
\iota_\varepsilon^*d\mu_{\varepsilon,\tau}
=w_{\varepsilon,\tau},d\mu_{P,\tau}.
$$

Pela Hipótese BI,

$$
w_{\varepsilon,\tau}longrightarrow1
$$

em $C^{k'-1,\alpha}_{\rm loc}$, uniformemente nos subconjuntos dominados do
contorno causal. Para uma seção limite compactamente suportada $\Psi$, defina
a identificação para o espaço variável por

$$
I_{\varepsilon,\tau}\Psi
=w_{\varepsilon,\tau}^{-1/2}
(\iota_\varepsilon^{-1})^*\Psi.
$$

Então, enquanto o suporte estiver contido na carta,

$$
\|I_{\varepsilon,\tau}\Psi\|_{
\mathcal H_{\varepsilon,\tau}}
=\|\Psi\|_{\mathcal H_{P,\tau}}.
$$

Para seções não compactamente suportadas, introduzem-se cortes
$\chi_A$ antes do transporte e toma-se primeiro $\varepsilon\to0$ e depois
$A\to\infty$. A tightness da medida controla o erro dessa segunda passagem.

## 4. Transporte tensorial

O pullback comum não basta para comparar componentes em fibrados diferentes.
Use transporte paralelo nas geodésicas das cartas e a projeção Hermitiana

$$
\Pi_J(h)(X,Y)
=\frac12\left[h(X,Y)+h(JX,JY)\right].
$$

Denote a identificação resultante dos fibrados por
$\mathscr P_\varepsilon$. O transporte completo é

$$
\boxed{
I_{\varepsilon,\tau}\Psi
=w_{\varepsilon,\tau}^{-1/2}
\mathscr P_\varepsilon
(\iota_\varepsilon^{-1})^*\Psi.
}
$$

As estimativas do Lema 2 e BI.5 implicam

$$
\mathscr P_\varepsilon\longrightarrow\operatorname{Id}
$$

em $C^{k'-1,\alpha}_{\rm loc}$.

## 5. Convergência dos dados geométricos

Por BI.6,

$$
\iota_\varepsilon^*J_\varepsilon\to J_P,
\qquad
\iota_\varepsilon^*f_\varepsilon\to f_P,
$$

e, como $H=d^c_J\omega$ é uma expressão diferencial de primeira ordem,

$$
\iota_\varepsilon^*H_\varepsilon\to H_P.
$$

A convergência não é uma hipótese independente para $H$ depois que
$(g,J)$ convergem com uma derivada suficiente. Da mesma forma,

$$
\iota_\varepsilon^*\mathcal U_\varepsilon
\to\mathcal U_P.
$$

## 6. Hessiana física oficial

Seja

$$
\Phi=(h,\phi),
\qquad
h=\delta g\in\operatorname{Sym}^2_JT^*M,
\qquad
\phi=\delta f.
$$

Defina a forma quadrática por segunda variação, e não por analogia:

$$
q_\varepsilon[\Phi]
:=\delta^2\mathcal S_{\rm GDQ}
[\mathfrak B_\varepsilon](\Phi,\Phi),
$$

com

$$
\delta H=D_{(g,J)}(d^c_J\omega)[h,\delta J].
$$

Depois da restrição ao espaço tangente dos vínculos, a estrutura de blocos é

$$
\boxed{
K_\varepsilon
=\begin{pmatrix}
K_{gg}^{(\varepsilon)}&K_{gf}^{(\varepsilon)}\\
K_{fg}^{(\varepsilon)}&K_{ff}^{(\varepsilon)}
\end{pmatrix}.
}
$$

Uma escrita com um bloco $K_{HH}$ independente supercontaria graus de
liberdade. Se for útil introduzir $\eta=\delta H$ durante o cálculo, deve-se
impor o vínculo linear

$$
\eta-D(d^c_J\omega)[h,\delta J]=0
$$

e eliminá-lo antes de interpretar o espectro físico.

O termo principal de $K_\varepsilon$ é elíptico após uma escolha de gauge para
análise e a imposição das condições complementares de interface. A escolha de
gauge não altera a ação nem adiciona fantasmas à ontologia.

## 7. Núcleo comum

Escolha

$$
\mathscr D
=C_c^\infty(M_P\setminus Y_P,E_P)
$$

inicialmente. Para funções que alcançam $Y_P$, use o subespaço suave que
satisfaz a condição limite $\mathsf B_P\Phi=0$ e os vínculos linearizados.
Esse conjunto é um núcleo de formas candidato; a densidade no domínio fechado
deve ser verificada para cada condição Robin, DtN ou APS adotada.

## 8. Convergência no núcleo

Para $\Phi,\Psi\in\mathscr D$, a segunda variação é uma soma finita de termos
locais com a forma

$$
\int
A_\varepsilon^{IJ}(x)
(D_I\Phi)(D_J\Psi),d\mu_\varepsilon
$$

e termos de ordem inferior, além das formas de interface. A convergência
$C^{k',\alpha}_{\rm loc}$ dos backgrounds implica convergência uniforme dos
coeficientes em cada suporte compacto. Portanto,

$$
\boxed{
q_\varepsilon[
I_\varepsilon\Phi,I_\varepsilon\Psi]
\longrightarrow q_P[\Phi,\Psi].
}
$$

A passagem pela integral causal segue de BI.8 e do teorema da convergência
dominada. Esse passo falharia se polos dependentes de $\varepsilon$ cruzassem
$\gamma$ ou se a segunda variação não tivesse majorante uniforme.

## 9. Mosco: o que já segue e o que falta

A convergência no núcleo fornece a condição de recuperação de Mosco:
para cada $\Phi$ no núcleo limite, existe
$\Phi_\varepsilon=I_\varepsilon\Phi$ tal que

$$
\limsup_{\varepsilon\to0}q_\varepsilon[\Phi_\varepsilon]
\leq q_P[\Phi].
$$

Para obter a condição liminf completa,

$$
q_P[\Phi]
\leq\liminf_{\varepsilon\to0}q_\varepsilon[\Phi_\varepsilon],
$$

é necessário impedir que energia ou norma escapem para a região que se abre.
BI.7 controla a medida, mas a concentração dos modos da Hessiana requer a
coercividade/localização do Lema 4. Assim:

$$
\boxed{
\text{convergência no núcleo: demonstrada sob BI;}
\quad
\text{Mosco completo: depende do Lema 4.}
}
$$

## 10. Consequência espectral permitida nesta etapa

Se, adicionalmente, a condição liminf for estabelecida, o teorema de
convergência de formas fechadas fornece convergência forte dos resolventes:

$$
I_\varepsilon^*(K_\varepsilon-z)^{-1}I_\varepsilon
\longrightarrow(K_P-z)^{-1}.
$$

Não se conclui ainda:

1. convergência em norma do resolvente;
2. constância da multiplicidade de um autovalor;
3. convergência de projetores de Riesz;
4. preservação de massas ou acoplamentos.

Essas conclusões exigem o gap uniforme dos Lemas 4--5.

## 11. Status

### Demonstrado sob a Hipótese BI

1. transporte local isométrico com a medida física;
2. convergência de $g,J,H,f$ e $\mathcal U$;
3. identificação correta do espaço físico de variações;
4. convergência da Hessiana oficial em um núcleo comum;
5. condição de recuperação de Mosco.

### Ainda aberto

1. condição liminf global;
2. ausência de perda de energia no infinito;
3. coercividade no complemento dos modos de simetria;
4. gap uniforme.

$$
\boxed{
\text{Lema 3A local: demonstrado condicionalmente a BI;}
\qquad
\text{Lema 3B global: depende do Lema 4.}
}
$$

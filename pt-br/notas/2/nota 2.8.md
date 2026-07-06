## Fundamentos: a estrutura complexa $J$ e as coordenadas $(q,p)$

Antes de mergulhar na notação $h_{\alpha\bar\beta}$, é preciso entender dois objetos que aparecerão o tempo todo: a **estrutura complexa** $J$ e as **coordenadas canônicas** $(q,p)$. Começamos do zero.

### O que é a estrutura complexa $J$?

No plano $\mathbb R^2$, multiplicar um vetor $(x,y)$ por $i$ é uma rotação de $90^\circ$ no sentido anti-horário:

$$
i \cdot (x, y) = (-y, x).
$$

Essa operação é linear e, aplicada duas vezes, dá uma rotação de $180^\circ$, que equivale a multiplicar por $-1$. A **estrutura complexa** $J$ é a generalização dessa ideia para qualquer espaço vetorial real: $J$ é uma transformação linear que satisfaz

$$
\boxed{\; J^2 = -\,\text{Identidade} \; } .
$$

Em $\mathbb R^2$ com coordenadas $(x^1, x^2)$, a matriz de $J$ é

$$
J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
\qquad
J \begin{pmatrix} x^1 \\ x^2 \end{pmatrix} = \begin{pmatrix} -x^2 \\ x^1 \end{pmatrix}.
$$

**Por que $J$ é útil?** Porque ela permite "multiplicar vetores por $i$" mesmo em espaços que não são $\mathbb C$. Um espaço vetorial real com uma estrutura $J$ torna-se um espaço vetorial complexo: definimos $(a + ib) \cdot v = a v + b\, J v$.

**Exemplo concreto:** No plano $(q,p)$ do oscilador harmônico, podemos definir

$$
J(\partial_q) = \partial_p, \qquad J(\partial_p) = -\partial_q .
$$

Isso significa: o vetor que aponta na direção $q$, quando "multiplicado por $i$", gira para a direção $p$. Verifique que $J^2(\partial_q) = J(\partial_p) = -\partial_q$, e o mesmo para $\partial_p$.

**Em coordenadas complexas:** Se definimos $z = q + i p$, então $J$ age como multiplicação por $i$:

$$
J(\partial_q + i\partial_p) = i(\partial_q + i\partial_p),
\qquad
J(\partial_q - i\partial_p) = -i(\partial_q - i\partial_p).
$$

Os autovetores de $J$ com autovalor $+i$ são os vetores holomorfos (tipo $(1,0)$); os com autovalor $-i$ são os anti-holomorfos (tipo $(0,1)$).

### O que são as coordenadas $(q,p)$?

Imagine que você quer descrever o movimento de uma partícula. Para saber tudo sobre ela em um instante, precisa de duas informações: **onde ela está** (posição $q$) e **como ela se move** (momento $p$). O conjunto de todos os pares $(q,p)$ possíveis é o **espaço de fases**.

Neste espaço existe uma estrutura geométrica fundamental: a **forma simplética**

$$
\boxed{\; \omega = dq \wedge dp \; } .
$$

Não se assuste com o símbolo $\wedge$. A expressão $dq \wedge dp$ é uma **2-forma** — um objeto que mede áreas orientadas no plano $(q,p)$. Dados dois vetores infinitesimais $A = (A_q, A_p)$ e $B = (B_q, B_p)$, o número

$$
\omega(A, B) = A_q B_p - A_p B_q
$$

é a área (com sinal) do paralelogramo formado por $A$ e $B$. É exatamente o determinante $2\times2$. A forma $\omega$ é **não degenerada**: se $\omega(A, \cdot) = 0$ para todo $B$, então $A = 0$. Não há vetor não nulo que tenha área zero com todos os outros.

As coordenadas $(q,p)$ que tornam $\omega = dq \wedge dp$ são chamadas de **coordenadas de Darboux** ou **coordenadas canônicas**. O Teorema de Darboux garante que, localmente, **sempre** podemos encontrar tais coordenadas em qualquer variedade simplética.

### Como construir $q$ e $p$ na prática?

Dada uma forma simplética $\omega$ qualquer, existe um procedimento local para encontrar $(q,p)$:

1. Escolha uma função $q$ tal que $dq \neq 0$.
2. Como $\omega$ é não degenerada, existe um campo vetorial $X$ tal que $\omega(X, \cdot) = dq$.
3. Encontre uma função $p$ tal que $dp = -\omega(\cdot, X)$ (ou equivalentemente, $\omega = dq \wedge dp$).

Na prática, porém, as coordenadas $(q,p)$ já vêm da física: $q$ é a posição medida por uma régua, $p$ é o momento medido pela dinâmica.

**Exemplo:** Para uma partícula em uma reta, o espaço de fases é $\mathbb R^2$. Escolha $q$ como a coordenada da reta. A forma simplética é $\omega = dq \wedge dp$, onde $p$ é o momento linear $m\dot q$. Não há escolha: $q$ e $p$ são as coordenadas naturais do problema.

**Exemplo em coordenadas complexas:** Dada a coordenada $z = x + i y$, se a forma simplética for $\omega = dx \wedge dy$, então podemos identificar $q = x$, $p = y$. Ou, equivalentemente, $z = q + i p$. A estrutura complexa $J$ que age como rotação de $90^\circ$ no plano $(q,p)$ é exatamente a multiplicação por $i$ no plano complexo.

**Exemplo do oscilador (antecipando):** Mais adiante usaremos $z = (q + i p)/\sqrt{2}$. O fator $1/\sqrt{2}$ é apenas uma normalização para que $dz\,d\bar z = (dq^2 + dp^2)/2$ em vez de $dq^2 + dp^2$. A forma simplética continua sendo $\omega = dq \wedge dp = i\, dz \wedge d\bar z$.

### A trindade $(g, J, \omega)$

Quando um espaço possui simultaneamente:
- uma **métrica** $g$ (mede distâncias e ângulos),
- uma **estrutura complexa** $J$ (multiplicação por $i$),
- uma **forma simplética** $\omega$ (mede áreas orientadas),

e eles são compatíveis pela relação

$$
\boxed{\; \omega(X, Y) = g(JX, Y) \; } ,
$$

dizemos que o espaço é **Kähler**. Essa equação é o vínculo central: conhecendo dois dos três objetos, o terceiro está determinado. Grande parte do que segue explora exatamente essa relação.

**Exemplo no plano $(q,p)$:** Tomando $g = dq^2 + dp^2$, $J(\partial_q) = \partial_p$, $J(\partial_p) = -\partial_q$, e $\omega = dq \wedge dp$, verifica-se:

$$
g(J\partial_q, \partial_q) = g(\partial_p, \partial_q) = 0 = \omega(\partial_q, \partial_q),
$$
$$
g(J\partial_q, \partial_p) = g(\partial_p, \partial_p) = 1 = \omega(\partial_q, \partial_p),
$$

e assim por diante. A relação $\omega(X,Y) = g(JX,Y)$ vale para todos os pares.

---

## Métrica Hermitiana e a notação $h_{\alpha\bar\beta}$

Em geometria complexa, as coordenadas locais de uma variedade são escritas como

$$
(z^1,\dots,z^n), \qquad z^\alpha = x^\alpha + i y^\alpha,
$$

e suas conjugadas complexas

$$
\bar z^\alpha = x^\alpha - i y^\alpha .
$$

Isso naturalmente divide os índices em dois tipos: $\alpha,\beta,\gamma,\dots$ para as coordenadas holomorfas $z^\alpha$, e $\bar\alpha,\bar\beta,\dots$ para as anti-holomorfas $\bar z^\alpha$. A barra no índice não significa que o valor da componente foi conjugado — ela indica que aquele índice pertence ao fibrado tangente anti-holomorfo.

Uma **métrica hermitiana** é o análogo complexo de uma métrica riemanniana. Em coordenadas, escreve-se

$$
ds^2 = h_{\alpha\bar\beta} \; dz^\alpha \otimes d\bar z^\beta .
$$

Cada termo carrega um diferencial holomorfo e um anti-holomorfo. Isso não é acidental: a **estrutura complexa** $J$ da variedade — a transformação linear que satisfaz $J^2 = -\,\text{Id}$ e que "multiplica vetores por $i$" (explicada em detalhes na seção anterior) — impõe a condição $h(JX, JY) = h(X,Y)$, que força o desaparecimento das componentes puras

$$
h_{\alpha\beta} = 0, \qquad h_{\bar\alpha\bar\beta} = 0 .
$$

As únicas componentes independentes são $h_{\alpha\bar\beta}$, e a métrica se reduz a

$$
g = h_{\alpha\bar\beta} \; dz^\alpha \otimes d\bar z^\beta .
$$

O nome "hermitiana" vem da condição de que a matriz $H = (h_{\alpha\bar\beta})$ deve satisfazer

$$
h_{\alpha\bar\beta} = \overline{h_{\beta\bar\alpha}} \quad\Longleftrightarrow\quad H = H^\dagger .
$$

É a generalização complexa de uma matriz simétrica real: onde uma métrica riemanniana tem $g_{ij}=g_{ji}$, uma métrica hermitiana tem $H = H^\dagger$.

### Exemplo físico: o oscilador harmônico unidimensional

O espaço de fases de uma partícula de massa $m=1$ sob um potencial harmônico tem coordenadas $(q, p)$. Definindo a coordenada complexa

$$
z = \frac{1}{\sqrt{2}} (q + i p),
$$

a métrica euclidiana no plano $(q,p)$ torna-se

$$
ds^2 = dq^2 + dp^2 = 2 \, dz \, d\bar z .
$$

A componente mista é $h_{z\bar z} = 1$. Não há componentes $h_{zz}$ nem $h_{\bar z\bar z}$ — exatamente o padrão de uma métrica hermitiana. A matriz métrica é $H = (1)$, que é trivialmente hermitiana.

### Exemplo: o espaço complexo $\mathbb C^n$

No espaço complexo plano,

$$
ds^2 = \sum_{\alpha=1}^n dz^\alpha \, d\bar z^\alpha,
\qquad
h_{\alpha\bar\beta} = \delta_{\alpha\beta},
\qquad
H = \mathbb I_{n\times n}.
$$

Um sistema físico de $n$ osciladores harmônicos desacoplados tem essa métrica: cada par $(q_\alpha, p_\alpha)$ vira a coordenada complexa $z^\alpha$, e o espaço de fases total é $\mathbb C^n$ com métrica plana.

---

## Variedades de Kähler e o potencial de Kähler

Quando a métrica hermitiana pode ser obtida de uma única função escalar real $K$, dizemos que a variedade é **Kähler**. A relação é

$$
h_{\alpha\bar\beta} = \frac{\partial^2 K}{\partial z^\alpha \, \partial\bar z^\beta}.
$$

A função $K$ é o **potencial de Kähler**, e dela extrai-se toda a geometria local da variedade.

### Exemplo físico 1: oscilador harmônico

Para o oscilador harmônico com $z = (q + i p)/\sqrt{2}$, o potencial de Kähler é

$$
K = |z|^2 = \frac{q^2 + p^2}{2}.
$$

Calculando a segunda derivada,

$$
\frac{\partial^2 K}{\partial z \, \partial\bar z} = 1 = h_{z\bar z}.
$$

Aqui $K$ é exatamente a energia do oscilador (Hamiltoniano) dividida pela frequência. Física e geometria coincidem.

### Exemplo físico 2: a esfera de Bloch (qubit)

Um sistema quântico de dois níveis tem como espaço de estados puros a esfera $S^2$, que é $\mathbb C P^1$ — a variedade complexa mais simples depois de $\mathbb C$. O potencial de Kähler é

$$
K = \log(1 + |z|^2),
$$

onde $z$ é a coordenada estereográfica que cobre a esfera (exceto o polo norte). A métrica resultante é

$$
h_{z\bar z} = \frac{\partial^2 K}{\partial z \, \partial\bar z} = \frac{1}{(1 + |z|^2)^2}.
$$

O elemento de linha é

$$
ds^2 = \frac{dz \, d\bar z}{(1 + |z|^2)^2},
$$

que é a métrica de Fubini-Study na esfera. Em coordenadas reais $z = e^{i\phi}\tan(\theta/2)$, recupera-se

$$
ds^2 = \frac{1}{4}(d\theta^2 + \sin^2\theta \, d\phi^2),
$$

a métrica padrão da esfera de raio $1/2$. Essa é a geometria natural do espaço de estados de um qubit.

---

## A forma de Kähler

Dada a métrica $g$ e a estrutura complexa $J$ (a transformação $J^2 = -\,\text{Id}$ que age como multiplicação por $i$, explicada na seção de fundamentos), define-se a **forma de Kähler**

$$
\boxed{\; \omega(X,Y) = g(JX,Y) \; } .
$$

Ela é uma 2-forma antissimétrica por construção. Em coordenadas complexas, sua expressão é

$$
\boxed{\; \omega = i \, h_{\alpha\bar\beta} \; dz^\alpha \wedge d\bar z^\beta \; } .
$$

(Alguns autores escrevem $\omega = \frac{i}{2} h_{\alpha\bar\beta} \, dz^\alpha \wedge d\bar z^\beta$; a diferença é apenas de normalização.)

### Exemplo físico 1: o oscilador harmônico

Para o oscilador com $h_{z\bar z} = 1$,

$$
\omega = i \, dz \wedge d\bar z .
$$

Usando $z = (q + i p)/\sqrt{2}$, temos $dz \wedge d\bar z = -i \, dq \wedge dp$, logo

$$
\omega = dq \wedge dp .
$$

Essa é a forma simplética canônica do espaço de fases. Ela mede áreas no plano $(q,p)$. Quando o oscilador evolui, as trajetórias são elipses — a área $dq \wedge dp$ é preservada, e é exatamente isso que o Teorema de Liouville afirma.

### Exemplo físico 2: a esfera de Bloch

Na esfera de Bloch com $h_{z\bar z} = (1 + |z|^2)^{-2}$,

$$
\omega = i \, \frac{dz \wedge d\bar z}{(1 + |z|^2)^2}.
$$

Em coordenadas angulares $(\theta, \phi)$,

$$
\omega = \frac{1}{4} \sin\theta \, d\theta \wedge d\phi .
$$

A área total da esfera é

$$
\int_{S^2} \omega = \frac{1}{4} \int_0^\pi \int_0^{2\pi} \sin\theta \, d\phi \, d\theta = \pi .
$$

Essa forma simplética controla a geometria dos estados quânticos: o transporte paralelo de um spin ao longo de um circuito fechado adquire uma fase geométrica proporcional à área simplética (fase de Berry).

---

## Estrutura simplética

Uma **variedade simplética** é um par $(M, \omega)$ onde $\omega$ é uma 2-forma que satisfaz duas condições:

1. **Não degenerescência**: se $\omega_p(X,\cdot)=0$ para algum $X$, então $X=0$.
2. **Fechamento**: $d\omega = 0$.

A não degenerescência já força $\dim M = 2n$ (dimensão par). Além disso, a forma de volume natural

$$
\frac{\omega^n}{n!}
$$

é nunca nula, o que torna toda variedade simplética automaticamente orientável. A não degenerescência também estabelece um isomorfismo entre vetores e 1-formas:

$$
X \longmapsto i_X\omega .
$$

Esse isomorfismo é análogo ao fornecido por uma métrica, mas aqui quem o fornece é a forma simplética.

O fechamento $d\omega = 0$ tem uma consequência local profunda: o **Teorema de Darboux** garante que, em torno de qualquer ponto, existem coordenadas $(q^1,\dots,q^n,p_1,\dots,p_n)$ tais que

$$
\boxed{\; \omega = dq^i \wedge dp_i \; } .
$$

Isso significa que **não existem invariantes locais** em geometria simplética: todas as variedades simpléticas de mesma dimensão são localmente indistinguíveis. É uma diferença marcante em relação à geometria riemanniana, onde a curvatura fornece invariantes locais não triviais.

### Exemplo físico: partícula livre em 1D

O espaço de fases de uma partícula livre de massa $m$ é $\mathbb R^2$ com coordenadas $(q, p)$. A forma simplética é

$$
\omega = dq \wedge dp .
$$

A condição $d\omega = 0$ é trivial (não há dependência espacial ou temporal). A não degenerescência: se $\omega(X, \cdot) = 0$, então $X = 0$, pois a matriz de $\omega$ na base $(q,p)$ é

$$
\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},
$$

cujo determinante é $1 \neq 0$. O volume simplético é

$$
\omega = dq \wedge dp,
$$

e a forma de volume é a própria área do espaço de fases.

### Exemplo físico: pêndulo simples

Para o pêndulo de comprimento $\ell$ e massa $m$, o espaço de fases é um cilindro: $q \in S^1$ (ângulo) e $p \in \mathbb R$ (momento angular). A forma simplética é a mesma,

$$
\omega = dq \wedge dp .
$$

Localmente, o Teorema de Darboux diz que essa é a única forma possível. A diferença entre o pêndulo e a partícula livre não está na estrutura simplética local, mas no Hamiltoniano:

$$
H_{\text{livre}} = \frac{p^2}{2m},
\qquad
H_{\text{pêndulo}} = \frac{p^2}{2m\ell^2} + mg\ell(1 - \cos q).
$$

A dinâmica é diferente, mas a geometria subjacente do espaço de fases é a mesma. Isso ilustra por que a estrutura simplética é independente da dinâmica: ela é o "palco" onde a dinâmica acontece.

### Transformações simpléticas: exemplo

A rotação no espaço de fases do oscilador harmônico,

$$
\begin{pmatrix} q(t) \\ p(t) \end{pmatrix} =
\begin{pmatrix} \cos\omega t & \sin\omega t \\ -\sin\omega t & \cos\omega t \end{pmatrix}
\begin{pmatrix} q_0 \\ p_0 \end{pmatrix},
$$

é uma transformação simplética: preserva $dq \wedge dp$, pois a matriz tem determinante $1$. Geometricamente, a área de qualquer região no espaço de fases é preservada pela evolução temporal.

---

## Mecânica hamiltoniana em linguagem simplética

Dada uma função $H: M \to \mathbb R$, a não degenerescência de $\omega$ garante que existe um único campo vetorial $X_H$ satisfazendo

$$
\boxed{\; i_{X_H}\omega = dH \; } .
$$

$X_H$ é o **campo hamiltoniano** gerado por $H$, e $H$ funciona como o potencial do campo. Em coordenadas de Darboux, essa equação se reduz às equações familiares de Hamilton:

$$
\boxed{\; \dot q^i = \frac{\partial H}{\partial p_i} \; },
\qquad
\boxed{\; \dot p_i = -\frac{\partial H}{\partial q^i} \; } .
$$

O **colchete de Poisson** também tem uma definição puramente geométrica:

$$
\boxed{\; \{f,g\} = \omega(X_f, X_g) \; } .
$$

Ele satisfaz antissimetria, identidade de Jacobi e regra de Leibniz, fazendo de $C^\infty(M)$ uma álgebra de Poisson.

Como $d\omega = 0$, a derivada de Lie do fluxo hamiltoniano sobre $\omega$ é nula:

$$
\mathcal L_{X_H}\omega = 0,
\qquad
\mathcal L_{X_H}\omega^n = 0 .
$$

Essa é a versão geométrica do **Teorema de Liouville**: o volume no espaço de fases permanece constante durante a evolução.

### Exemplo físico: oscilador harmônico

O Hamiltoniano é $H = (p^2 + \omega^2 q^2)/2$. A equação $i_{X_H}\omega = dH$ dá

$$
X_H = \frac{\partial H}{\partial p} \partial_q - \frac{\partial H}{\partial q} \partial_p = p \, \partial_q - \omega^2 q \, \partial_p .
$$

As curvas integrais são

$$
\dot q = p, \qquad \dot p = -\omega^2 q,
$$

cuja solução é

$$
q(t) = q_0 \cos\omega t + \frac{p_0}{\omega} \sin\omega t,
\qquad
p(t) = p_0 \cos\omega t - \omega q_0 \sin\omega t .
$$

Verifica-se que $dq(t) \wedge dp(t) = dq_0 \wedge dp_0$: a área é preservada. O colchete de Poisson $\{q, p\} = 1$ dá a regra de quantização canônica $[\hat q, \hat p] = i\hbar$.

### Exemplo: partícula livre

Para $H = p^2/(2m)$, o campo hamiltoniano é $X_H = (p/m)\,\partial_q$, e as equações de Hamilton são

$$
\dot q = \frac{p}{m}, \qquad \dot p = 0 .
$$

A solução é $q(t) = q_0 + (p_0/m)t$, $p(t) = p_0$. O fluxo translada $q$ sem alterar $p$, e claramente $dq \wedge dp$ é preservado. O volume de qualquer região no espaço de fases permanece constante — uma faixa de momentos diferentes se distorce, mas sua área não muda.

---

## Da Lagrangeana à estrutura simplética

A estrutura simplética não precisa ser postulada — ela emerge naturalmente de uma Lagrangeana regular. Até aqui tratamos $(q,p)$ como coordenadas do espaço de fases; agora veremos como elas surgem de uma Lagrangeana $L(q, \dot q, t)$. O momento canônico é definido como

$$
p_i = \frac{\partial L}{\partial \dot q^i},
$$

que é a generalização natural do momento $p = mv$ da mecânica elementar.

Quando o hessiano $\det(\partial^2 L / \partial\dot q^i \partial\dot q^j) \neq 0$, a transformação de Legendre é invertível.

No espaço de fases aparece a **1-forma canônica**

$$
\theta = p_i \, dq^i .
$$

Ela contém toda a informação sobre os momentos. Sua derivada exterior

$$
\boxed{\; \omega = d\theta = dq^i \wedge dp_i \; }
$$

é exatamente a forma simplética canônica. Observe que ela **não foi imposta** — surgiu da própria Lagrangeana.

### Exemplo físico: partícula livre

A Lagrangeana é $L = \tfrac12 m \dot q^2$. O momento é $p = m\dot q$. A 1-forma canônica é

$$
\theta = p \, dq = m\dot q \, dq .
$$

A derivada exterior dá

$$
\omega = d\theta = dp \wedge dq = dq \wedge dp .
$$

A transformação de Legendre $H = p\dot q - L = p^2/(2m)$ produz o Hamiltoniano, e as equações de Hamilton seguem imediatamente.

### Exemplo físico: oscilador harmônico

A Lagrangeana é $L = \tfrac12 m\dot q^2 - \tfrac12 m\omega^2 q^2$. O momento é $p = m\dot q$, e

$$
\theta = p \, dq .
$$

A forma simplética é a mesma: $\omega = dq \wedge dp$. O Hamiltoniano é

$$
H = \frac{p^2}{2m} + \frac12 m\omega^2 q^2 .
$$

Toda a dinâmica está codificada na trinca $(\theta, \omega, H)$. A lição importante é que $\omega$ independe do potencial: ela é determinada apenas pela estrutura cinética da Lagrangeana.

### Exemplo: pêndulo simples em coordenadas complexas

Para o pêndulo, $L = \tfrac12 m\ell^2 \dot q^2 - mg\ell(1 - \cos q)$. O momento é $p = m\ell^2 \dot q$, e a 1-forma é $\theta = p \, dq$. A forma simplética é $\omega = dq \wedge dp$, que em coordenadas complexas $z = (q + ip)/\sqrt{2}$ (com $m=\ell=1$) se escreve $\omega = i \, dz \wedge d\bar z$. Localmente, o espaço de fases do pêndulo é indistinguível do da partícula livre — a diferença está apenas no Hamiltoniano.

---

## Interpretação física

### O espaço de fases como espaço de estados

Cada ponto $(q,p)$ da variedade simplética representa um **estado físico completo** do sistema. Para uma partícula em $\mathbb R^3$, a variedade tem dimensão 6 (posição e momento), enquanto o espaço físico tem dimensão 3. A variedade não é o espaço onde a partícula está — é o **espaço de todos os estados possíveis**.

- Um ponto é um estado.
- O campo $X_H$ é a lei de evolução: ele diz, dado o estado atual, para qual estado o sistema evolui.
- A trajetória integral é a história temporal completa do sistema.

**Exemplo:** para o oscilador harmônico com condições iniciais $(q_0, p_0)$, o estado em qualquer instante $t$ é $(q(t), p(t))$ dado pelas equações acima. O conjunto de todos os pontos $(q,p)$ possíveis é $\mathbb R^2$ inteiro. Cada condição inicial é um ponto, e a evolução é uma curva nesse plano.

### O que $\omega$ mede

A 2-forma $\omega = dq \wedge dp$ não mede distâncias. Ela mede **como variações de posição e momento estão acopladas**. O elemento $dq \wedge dp$ é uma área infinitesimal no espaço de fases, e é justamente essa área que permanece invariante sob evolução hamiltoniana.

**Exemplo:** Considere um ensemble de partículas com posições iniciais entre $q_0$ e $q_0 + \Delta q$ e momentos entre $p_0$ e $p_0 + \Delta p$. A área ocupada é $\Delta q \, \Delta p$. Sob a evolução do oscilador harmônico, essa região se deforma, mas sua área permanece $\Delta q \, \Delta p$ — o Teorema de Liouville em ação.

### $d\omega = 0$ e a conservação de energia

Em cálculo vetorial, um campo conservativo satisfaz $\nabla \times \mathbf F = 0$, ou em formas, $dF = 0$, o que implica $F = d\phi$ (potencial). Na geometria simplética, $d\omega = 0$ implica $\omega = d\theta$, onde $\theta = p_i\,dq^i$ é a 1-forma canônica — o **potencial simplético**.

A sequência conceitual é notável:

$$
d\omega = 0 \;\Longrightarrow\; \omega = d\theta \;\Longrightarrow\; i_{X_H}\omega = dH \;\Longrightarrow\; \frac{dH}{dt} = 0 .
$$

Ela mostra que a **conservação da energia não é uma hipótese adicional** na mecânica hamiltoniana autônoma: ela decorre naturalmente da estrutura simplética.

**Exemplo:** Para o oscilador, $H = (p^2 + \omega^2 q^2)/2$. Calculemos:

$$
\frac{dH}{dt} = X_H(H) = dH(X_H) = \omega(X_H, X_H) = 0,
$$

pois $\omega$ é antissimétrica. A energia é constante porque a estrutura simplética torna impossível que ela varie.

### A geometria como consequência da dinâmica

Invertendo a ordem lógica usual, podemos enxergar a variedade não como um palco pré-existente, mas como a **codificação geométrica das relações dinâmicas impostas pela ação**:

$$
\boxed{\; \text{Lagrangeana} \;\longrightarrow\; \text{Ação} \;\longrightarrow\; \text{Estrutura simplética} \;\longrightarrow\; \text{Geometria da variedade} \; } .
$$

Nessa perspectiva, a estrutura geométrica é consequência das leis dinâmicas, e não seu ponto de partida.

**Exemplo:** Comece com a Lagrangeana $L = \tfrac12 m\dot q^2 - V(q)$.
1. A partir dela, defina $p = m\dot q$ e construa $\theta = p\,dq$.
2. Tire $\omega = d\theta = dq \wedge dp$.
3. O espaço de fases $\mathbb R^2$ com essa $\omega$ é uma variedade simplética.
4. A geometria (plana, simplética) não foi postulada — surgiu da forma mais simples possível de Lagrangeana.

Se a Lagrangeana tivesse um termo de acoplamento mais complicado (como em teorias de campo ou em sistemas com vínculos), a estrutura simplética resultante poderia ser não trivial — mas ainda assim seria consequência da ação.

---

## A trindade Kähler

Se existe uma estrutura complexa $J$ (a transformação linear com $J^2 = -\,\text{Id}$ que "multiplica vetores por $i$", explicada nos fundamentos) compatível com $\omega$ tal que

$$
g(X,Y) = \omega(X, JY)
$$

define uma métrica riemanniana, e se $J$ é integrável, então $(M, g, J, \omega)$ é uma **variedade de Kähler**. A mesma estrutura geométrica é simultaneamente:

- **riemanniana** (a métrica $g$ mede comprimentos e ângulos);
- **complexa** (a estrutura $J$ define o que significa multiplicar vetores por $i$);
- **simplética** (a forma $\omega$ mede áreas orientadas e fornece a estrutura dinâmica).

Essas três estruturas estão ligadas pela relação central

$$
\boxed{\; \omega(X,Y) = g(JX,Y) \; },
$$

que unifica a geometria métrica, a geometria complexa e a geometria simplética em um único objeto.

### Exemplo físico: o oscilador harmônico como variedade de Kähler

O espaço de fases do oscilador, $\mathbb R^2$ com coordenadas $(q,p)$, é a variedade de Kähler mais simples possível — $\mathbb C$.

- A estrutura complexa $J$ gira vetores no sentido anti-horário: $J(\partial_q) = \partial_p$, $J(\partial_p) = -\partial_q$.
- A métrica é a euclidiana: $g = dq^2 + dp^2$.
- A forma de Kähler é $\omega = dq \wedge dp$.

Verifica-se: $\omega(X, JY) = g(X,Y)$ para quaisquer $X,Y$. O potencial de Kähler é $K = |z|^2 = (q^2 + p^2)/2$.

### Exemplo físico: a esfera de Bloch como variedade de Kähler

A esfera $S^2$ com a métrica de Fubini-Study é $\mathbb C P^1$ — uma variedade de Kähler compacta.

- A estrutura complexa é a rotação de $90^\circ$ no plano tangente.
- A métrica é $g = (d\theta^2 + \sin^2\theta \, d\phi^2)/4$.
- A forma de Kähler é $\omega = (\sin\theta \, d\theta \wedge d\phi)/4$.

A relação $\omega(X,Y) = g(JX,Y)$ é satisfeita. O potencial de Kähler é $K = \log(1 + |z|^2)$.

Essa variedade aparece naturalmente na mecânica quântica: o espaço de estados puros de um sistema de dois níveis é $\mathbb C P^1$, e a fase de Berry adquirida por um spin em um campo magnético que varia adiabaticamente é exatamente a área simplética varrida no espaço de parâmetros. A geometria de Kähler está codificada na física mais fundamental dos sistemas quânticos.

---

## Subvariedades Lagrangianas e o Espaço-Tempo Físico

### A. Decomposição da métrica de Kähler

A métrica hermitiana $h_{\alpha\bar\beta}$ que caracteriza a variedade complexa $M_{\mathbb C}$ pode ser decomposta localmente em suas partes real e imaginária. Escrevendo as coordenadas complexas como $z^\alpha = x^\mu + i y^\mu$, o elemento de linha

$$
ds^2 = h_{\alpha\bar\beta} \, dz^\alpha \otimes d\bar z^\beta
$$

se reescreve em coordenadas reais $(x^\mu, y^\mu)$ como

$$
ds^2 = \bigl(g_{\mu\nu} + i\, \omega_{\mu\nu}\bigr) \, dx^\mu \otimes dx^\nu + \text{termos mistos e puramente imaginários},
$$

onde $g_{\mu\nu}$ é simétrico (a parte riemanniana) e $\omega_{\mu\nu}$ é antissimétrico (a parte simplética). A relação entre eles é fixada pela estrutura quase-complexa $J$ (a transformação $J^2 = -\,\text{Id}$ da seção de fundamentos):

$$
\boxed{\; \omega(X,Y) = g(JX, Y) \; } .
$$

A métrica hermitiana codifica simultaneamente a geometria métrica (comprimentos e ângulos) e a geometria simplética (áreas e acoplamentos dinâmicos) em um único tensor.

**Exemplo: o oscilador harmônico.** Em coordenadas reais $(q,p)$,

$$
z = \frac{q + i p}{\sqrt{2}}, \qquad
ds^2 = dz\,d\bar z = \frac12(dq^2 + dp^2).
$$

A matriz da métrica em coordenadas reais é

$$
g_{\mu\nu} = \frac12 \begin{pmatrix}1&0\\0&1\end{pmatrix}, \qquad
\omega_{\mu\nu} = \frac12 \begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

de modo que $g_{\mu\nu} + i\omega_{\mu\nu} = \frac12 \begin{pmatrix}1 & i \\ -i & 1\end{pmatrix}$. Verifica-se que $\omega(X,Y) = g(JX,Y)$: a parte imaginária é inteiramente determinada pela estrutura complexa.

**Exemplo: $\mathbb C P^1$ (esfera de Bloch).** Em coordenadas estereográficas $z$,

$$
h_{z\bar z} = \frac{1}{(1+|z|^2)^2}, \qquad
ds^2 = \frac{dz\,d\bar z}{(1+|z|^2)^2}.
$$

Escrevendo $z = x + iy$, a métrica se decompõe em

$$
g = \frac{dx^2 + dy^2}{(1 + x^2 + y^2)^2}, \qquad
\omega = \frac{dx \wedge dy}{(1 + x^2 + y^2)^2},
$$

que são respectivamente a métrica e a forma de área da esfera $S^2$ (com raio $1/2$). Novamente, $g$ e $\omega$ compartilham o mesmo fator conforme — a estrutura de Kähler as unifica.

---

### B. O embedding Lagrangiano do espaço-tempo físico

Postula-se que o espaço-tempo físico real onde a matéria bariônica e os observadores macroscópicos coexistem é uma **subvariedade real $M_{\mathbb R}$ integrada de forma Lagrangiana maximal** dentro de $M_{\mathbb C}$. Esta incorporação topológica é caracterizada por duas condições matemáticas estritas:

1. **Condição dimensional maximal:** a dimensão real de $M_{\mathbb R}$ é exatamente a metade da dimensão real da variedade hospedeira:

   $$
   \dim_{\mathbb R}(M_{\mathbb R}) = \frac12 \dim_{\mathbb R}(M_{\mathbb C}) = 4 .
   $$

2. **Anulamento simplético do pullback:** a injeção canônica $i: M_{\mathbb R} \hookrightarrow M_{\mathbb C}$ força o pullback da 2-forma de Kähler a anular-se identicamente em qualquer par de vetores tangentes à subvariedade:

   $$
   \boxed{\; i^*\omega \equiv 0 \;\Longrightarrow\; \omega(X, Y) = 0 \quad \forall\, X, Y \in T_x M_{\mathbb R} \; } .
   $$

Uma subvariedade que satisfaz essas duas condições é chamada de **subvariedade Lagrangiana maximal** — ou simplesmente **Lagrangiana**. Fisicamente, ela representa a "fatia real" do espaço de fases complexo onde a dinâmica observável se manifesta.

**Exemplo: o oscilador harmônico.** A variedade complexa $M_{\mathbb C} = \mathbb C$ tem dimensão real 2. Uma subvariedade Lagrangiana maximal deve ter dimensão real 1. O eixo real $M_{\mathbb R} = \{z = q/\sqrt{2} \mid q \in \mathbb R\}$ (isto é, $p = 0$) satisfaz:

- $\dim_{\mathbb R}(M_{\mathbb R}) = 1 = \frac12 \dim_{\mathbb R}(\mathbb C)$;
- Para $X = \partial_q$, $Y = \partial_q$ (os únicos vetores tangentes disponíveis), $\omega(\partial_q, \partial_q) = 0$ por antissimetria.

Pontos com $p = 0$ são estados de momento nulo — a subvariedade Lagrangiana seleciona configurações de "velocidade zero". Se tomarmos $M_{\mathbb R} = \{z = i p/\sqrt{2} \mid p \in \mathbb R\}$ (isto é, $q = 0$), temos outra Lagrangiana, correspondente a posições fixas na origem.

Mais geralmente, qualquer curva unidimensional em $\mathbb C$ que não envolva área (isto é, cujo vetor tangente nunca tenha componentes $q$ e $p$ simultaneamente não nulas) é Lagrangiana.

**Exemplo: espaço de fases de $n$ partículas.** Para $M_{\mathbb C} = \mathbb C^{2n}$ com coordenadas $(z^\alpha, w_\alpha)$, uma Lagrangiana natural é o espaço de configurações $M_{\mathbb R} = \{(q^\alpha, 0) \mid q^\alpha \in \mathbb R\}$, que fixa todos os momentos a zero. Outra é o espaço dos momentos $M_{\mathbb R} = \{(0, p_\alpha) \mid p_\alpha \in \mathbb R\}$, que fixa todas as posições.

**Exemplo: $\mathbb C P^1$.** O equador da esfera de Bloch (latitude $\theta = \pi/2$) é uma subvariedade Lagrangiana: tem dimensão real 1 (metade de 2) e, ao longo do equador, a forma $\omega = \frac14 \sin\theta \, d\theta \wedge d\phi$ se anula porque $d\theta = 0$ na restrição.

---

### C. Consequências físicas da restrição Lagrangiana

Ao restringirmos a dinâmica macroscópica a $M_{\mathbb R}$, a componente imaginária da métrica hermitiana desaparece do elemento de linha clássico, restando apenas o campo métrico hiperbólico padrão $g_{\mu\nu}$ com assinatura $(-,+,+,+)$.

As quatro dimensões reais complementares — o fibrado normal $T^\perp M_{\mathbb R}$ — não representam "dimensões espaciais extras compactificadas" como nas teorias de Kaluza–Klein ou supercordas. Elas constituem o **setor simplético oculto**: a estrutura $\omega$ restrita a $T^\perp M_{\mathbb R}$ permanece não degenerada e codifica as relações canônicas entre variáveis dinâmicas não acessíveis classicamente.

**Exemplo: oscilador harmônico revisitado.** A subvariedade Lagrangiana $M_{\mathbb R} = \{p = 0\}$ tem métrica induzida $ds^2|_{M_{\mathbb R}} = \frac12 dq^2$ — a métrica espacial unidimensional usual. A direção complementar (o eixo $p$) carrega a forma simplética $\omega = dq \wedge dp$, que é não degenerada quando restrita ao fibrado normal. Fisicamente, $p$ não é uma coordenada espacial extra, mas o momento canônico conjugado a $q$ — uma variável dinâmica, não geométrica no sentido métrico.

**Exemplo: teoria de campos escalar em 4D.** Suponha que a variedade complexa subjacente tenha 8 dimensões reais (4 complexas). O espaço-tempo físico $M_{\mathbb R}$ é uma subvariedade Lagrangiana de dimensão 4. A métrica induzida $g_{\mu\nu}$ tem assinatura lorentziana $(-,+,+,+)$. As 4 dimensões normais carregam a estrutura simplética que, no limite clássico, dá origem aos colchetes de Poisson entre os campos e seus momentos conjugados:

$$
\{\phi(x), \pi(y)\} = \delta(x - y).
$$

Esses colchetes são a manifestação quântica da estrutura simplética do fibrado normal: a não comutatividade entre $\phi$ e $\pi$ reflete a não degenerescência de $\omega$ na direção transversal a $M_{\mathbb R}$.

**Exemplo: dois osciladores acoplados (modos normais).** Considere duas massas $m$ conectadas por molas de constante $k$ numa linha. A Lagrangeana é

$$
L = \frac12 m(\dot q_1^2 + \dot q_2^2) - \frac12 k\bigl[q_1^2 + (q_2 - q_1)^2 + q_2^2\bigr].
 $$

O espaço de fases tem dimensão real 4, com coordenadas $(q_1, q_2, p_1, p_2)$ e forma simplética $\omega = dq_1 \wedge dp_1 + dq_2 \wedge dp_2$. Este sistema é equivalente a $\mathbb C^2$ com coordenadas

$$
z_1 = \frac{q_1 + i p_1}{\sqrt{2}}, \qquad
z_2 = \frac{q_2 + i p_2}{\sqrt{2}},
$$

e métrica de Kähler $ds^2 = dz_1 d\bar z_1 + dz_2 d\bar z_2$.

Os **modos normais** diagonalizam o sistema: definindo

$$
q_+ = \frac{q_1 + q_2}{\sqrt{2}}, \quad
q_- = \frac{q_1 - q_2}{\sqrt{2}}, \quad
\omega_+ = \sqrt{\frac{k}{m}}, \quad
\omega_- = \sqrt{\frac{3k}{m}},
$$

o Hamiltoniano separa-se em $H = H_+ + H_-$, cada um da forma de um oscilador independente.
Em coordenadas complexas $z_\pm = (q_\pm + i p_\pm)/\sqrt{2}$, a métrica permanece plana:

$$
ds^2 = dz_+ d\bar z_+ + dz_- d\bar z_- .
$$

A **subvariedade Lagrangiana** natural é o espaço de configurações

$$
M_{\mathbb R} = \{(q_1, q_2, 0, 0) \mid q_1, q_2 \in \mathbb R\} \cong \mathbb R^2 .
$$

Sobre ela, $\omega$ se anula identicamente: $dq_i \wedge dp_i$ restrito a $p_i = 0$ é zero. A métrica induzida é

$$
ds^2|_{M_{\mathbb R}} = \frac12(dq_1^2 + dq_2^2),
$$

que é simplesmente a métrica euclidiana do plano de configurações. As direções normais (os eixos $p_1, p_2$) carregam a forma simplética e correspondem aos momentos — não a direções espaciais extras. Fisicamente, isso significa que o estado do sistema é especificado por duas posições e dois momentos: as posições são observáveis diretamente (métrica), os momentos são inferidos pela dinâmica (estrutura simplética).

**Exemplo: partícula carregada em campo magnético uniforme.** Considere uma partícula de massa $m$ e carga $e$ em $\mathbb R^3$ sujeita a um campo magnético constante $\mathbf B = B \hat z$. A Lagrangeana é

$$
L = \frac12 m \dot{\mathbf q}^2 + \frac{e}{c} \mathbf A \cdot \dot{\mathbf q},
\qquad
\mathbf A = \frac{B}{2}(-y, x, 0).
 $$

O momento canônico é $\mathbf p = m\dot{\mathbf q} + (e/c)\mathbf A$, e a forma simplética canônica

$$
\omega = dq^i \wedge dp_i
$$

adquire um termo magnético quando escrita em termos da velocidade:

$$
\omega = m \, dq^i \wedge d\dot q_i + \frac{eB}{c} \, dx \wedge dy .
$$

O termo $dx \wedge dy$ é a projeção do campo magnético na forma simplética — ele mostra que o campo magnético contribui diretamente para a geometria simplética do espaço de fases.

A variedade complexa subjacente tem dimensão real 6 (3 complexas). A subvariedade Lagrangiana $M_{\mathbb R} = \{(\mathbf q, \mathbf p = 0)\}$ é o espaço de configurações $\mathbb R^3$, com $\dim = 3 = 6/2$. Sobre ela,

$$
i^*\omega = \frac{eB}{c} \, dx \wedge dy \neq 0 .
$$

Isso parece violar a condição Lagrangiana — e de fato $\mathbf p = 0$ **não** é Lagrangiana quando há campo magnético. A Lagrangiana correta é dada pelo momento cinético $\boldsymbol\pi = m\dot{\mathbf q} = \mathbf p - (e/c)\mathbf A$: a subvariedade $\boldsymbol\pi = 0$ é Lagrangiana. Fisicamente, $\boldsymbol\pi$ é o momento que realmente importa para a dinâmica (a velocidade vezes a massa), enquanto $\mathbf p$ é uma combinação que mistura posição e campo.

**Interpretação física:** o campo magnético deforma a estrutura simplética, "torcendo" a identificação entre momentos e velocidades. A subvariedade Lagrangiana que corresponde ao espaço de configurações não é mais $\mathbf p = 0$, mas $\boldsymbol\pi = 0$, que equivale a $\dot{\mathbf q} = 0$. Isso mostra que o embedding Lagrangiano não é único — diferentes escolhas de coordenadas no espaço de fases correspondem a diferentes "fatias reais" da variedade complexa. O campo magnético, nessa linguagem, é uma manifestação da **curvatura simplética**: a não trivialidade de $\omega$ reflete a presença de um campo de calibre no fibrado normal.

**Exemplo: relatividade geral e a superfície de Cauchy.** Na formulação ADM da relatividade geral, o espaço-tempo é folheado por hipersuperfícies espaciais $\Sigma_t$ de coordenada $t$. O estado geométrico de cada fatia é descrito pela métrica induzida $h_{ij}$ e seu momento conjugado $\pi^{ij}$. Esta dupla $(h_{ij}, \pi^{ij})$ é exatamente a generalização para campos do par $(q,p)$ da seção de fundamentos: $h_{ij}$ é a "posição" (a geometria da fatia espacial) e $\pi^{ij}$ é o "momento" (a taxa de variação dessa geometria). A relação entre eles é

$$
\pi^{ij} = \sqrt{h} \, (K^{ij} - K h^{ij}),
$$

onde $K_{ij}$ é a curvatura extrínseca. O espaço de fases da RG é o conjunto de todos os pares $(h_{ij}, \pi^{ij})$ sobre uma 3-variedade — um espaço de dimensão infinita, mas ainda com estrutura simplética:

$$
\omega = \int_{\Sigma} \delta h_{ij} \wedge \delta\pi^{ij} \, d^3x .
$$

A variedade complexa ambiente $M_{\mathbb C}$ teria "dimensão real infinita". A subvariedade Lagrangiana $M_{\mathbb R}$ é a superfície de Cauchy $\Sigma_t$ com $\pi^{ij} = 0$, i.e., a fatia onde a curvatura extrínseca é nula. Sobre ela, a métrica induzida $h_{ij}$ é puramente espacial, e $\omega$ se anula. As direções normais (os momentos $\pi^{ij}$) carregam a informação sobre como a geometria evolui no tempo.

**Interpretação física:** A superfície de Cauchy é uma "fatia real" do espaço de fases geométrico. As três dimensões espaciais de $\Sigma$ são o que medimos como espaço; as três "dimensões canônicas" $\pi^{ij}$ codificam a dinâmica — a taxa de variação da métrica. A estrutura simplética entre $h_{ij}$ e $\pi^{kl}$ gera o colchete de Poisson

$$
\{h_{ij}(x), \pi^{kl}(y)\} = \delta_i^{(k} \delta_j^{l)} \, \delta(x - y),
$$

que é a base da quantização canônica da gravidade (equação de Wheeler–DeWitt). Nessa linguagem, a métrica de Kähler ambiente unificaria a geometria espacial (parte real) com a dinâmica temporal (parte simplética) em um único objeto.

**Interpretação física.** Nessa construção, o espaço-tempo observável emerge como uma "fatia real" de uma estrutura complexa maior. A métrica $g_{\mu\nu}$ que medimos é a projeção Riemanniana da métrica de Kähler; a forma simplética $\omega$ permanece oculta na direção normal, manifestando-se apenas através das relações de comutação canônicas e da dinâmica hamiltoniana. As dimensões extras não são espaciais — são **dimensionais canônicas**, carregando os momentos conjugados aos graus de liberdade do espaço-tempo.

Essa perspectiva unifica a geometria do espaço-tempo (métrica) com a estrutura algébrica da mecânica quântica (colchetes de Poisson, comutadores) em um único objeto geométrico: a métrica de Kähler da variedade complexa ambiente.

---

## Apêndice: Reconstrução passo a passo a partir da mecânica analítica

Este apêndice refaz o caminho desde o princípio de Lagrange até a estrutura simplética **sem usar geometria diferencial avançada**, apenas cálculo multivariável e exemplos físicos. O objetivo é mostrar que a estrutura simplética não é um formalismo abstrato, mas uma consequência natural da mecânica analítica.

---

### 1. A construção de Lagrange: a física vem primeiro

Lagrange parte de uma pergunta física: **como a Natureza escolhe a trajetória de um sistema?**

**Passo 1 — Coordenadas generalizadas.** Escolhem-se $q = (q^1,\dots,q^n)$ que descrevem a configuração do sistema. Neste ponto existe apenas o **espaço de configurações** $Q$.

**Passo 2 — Velocidades.** A trajetória é $q(t)$ e sua derivada $\dot q(t)$ dá as velocidades. O espaço relevante passa a ser o fibrado tangente $TQ$.

**Passo 3 — Lagrangeana.** Escreve-se $L(q,\dot q,t)$, normalmente $L = T - V$. Toda a física entra aqui.

**Passo 4 — A ação.** Define-se o funcional

$$
S[q] = \int L \, dt .
$$

**Passo 5 — Princípio variacional.** Impõe-se $\delta S = 0$. Dali surgem as equações de Euler–Lagrange:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q^i}\right) - \frac{\partial L}{\partial q^i} = 0 .
$$

Nada foi imposto além do princípio de ação estacionária. Toda a dinâmica está pronta.

**Exemplo: partícula livre.** $L = \frac12 m \dot q^2$. A equação de Euler–Lagrange dá $m\ddot q = 0$, i.e., velocidade constante.

**Exemplo: oscilador harmônico.** $L = \frac12 m\dot q^2 - \frac12 m\omega^2 q^2$. A equação é $m\ddot q + m\omega^2 q = 0$, cuja solução é $q(t) = A\cos(\omega t + \phi)$.

---

### 2. A construção de Hamilton: a geometria do espaço de estados

Hamilton pergunta: **como descrever geometricamente toda a dinâmica?**

**Passo 1 — Momento canônico.** Define-se

$$
p_i = \frac{\partial L}{\partial \dot q^i}.
$$

Para a partícula livre, $p = m\dot q$ (momento linear). Para o oscilador, $p = m\dot q$ (o mesmo, pois o potencial não depende da velocidade).

**Passo 2 — Transformação de Legendre.** Troca-se $(q,\dot q)$ por $(q,p)$. O espaço deixa de ser $TQ$ e passa a ser o **espaço de fases** $T^*Q$.

**Passo 3 — Hamiltoniano.** Define-se

$$
H = p_i \dot q^i - L .
$$

A energia aparece naturalmente. Para a partícula livre, $H = p^2/(2m)$. Para o oscilador, $H = p^2/(2m) + \frac12 m\omega^2 q^2$.

**Passo 4 — A 1-forma canônica.** Hamilton percebe que existe naturalmente o objeto

$$
\boxed{\; \theta = p_i \, dq^i \; } .
$$

Aqui começa a geometria. $\theta$ associa a cada deslocamento $dq^i$ o momento correspondente $p_i$. Fisicamente, é o trabalho infinitesimal.

**Passo 5 — A forma simplética.** Toma-se a derivada exterior:

$$
\boxed{\; \omega = d\theta = dq^i \wedge dp_i \; } .
$$

Essa é a **estrutura simplética** — uma área orientada no espaço de fases.

**Passo 6 — O campo hamiltoniano.** Dado $H(q,p)$, a equação fundamental

$$
\boxed{\; i_{X_H}\omega = dH \;}
$$

determina o campo vetorial $X_H$ que gera a evolução temporal. Resolvendo-a, obtêm-se as equações de Hamilton:

$$
\dot q^i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q^i}.
$$

---

### 3. O que é a derivada exterior $d$? (sem geometria diferencial)

A derivada exterior $d$ é o operador que **aumenta em um a dimensão geométrica do objeto**:

- uma função (0-forma) → variação ao longo de curvas (1-forma)
- uma 1-forma → circulação em superfícies (2-forma)
- uma 2-forma → fluxo através de volumes (3-forma)

**Exemplo 1: função → 1-forma.** Considere a temperatura de uma chapa metálica $T(x,y) = x^2 + y^2$. A derivada exterior é

$$
dT = 2x \, dx + 2y \, dy .
$$

Isso responde: "se eu andar um pouquinho, quanto a temperatura muda?" No ponto $(1,2)$, $dT = 2\,dx + 4\,dy$. Andando apenas em $x$, a temperatura aumenta 2; andando apenas em $y$, aumenta 4.

**Exemplo 2: 1-forma → 2-forma.** Considere uma força $F = x\,dy - y\,dx$. Aplicando $d$,

$$
dF = dx \wedge dy - (-dy \wedge dx) = 2\,dx \wedge dy .
$$

Essa 2-forma mede a **circulação local** — o quanto uma pequena hélice giraria se colocada nesse campo. No cálculo vetorial, isso é o rotacional.

**Exemplo 3: campo conservativo.** Se $F = 2x\,dx + 2y\,dy$, note que $F = d(x^2 + y^2)$. Então $dF = 0$ — não há circulação. É um campo conservativo.

**Exemplo 4: campo não conservativo.** Se $F = -y\,dx + x\,dy$, então $dF = 2\,dx \wedge dy \neq 0$. Existe circulação. É o típico campo de uma rotação.

**Exemplo 5: eletromagnetismo.** O potencial eletromagnético é uma 1-forma $A = A_\mu dx^\mu$. Aplicando $d$, obtém-se o tensor de campo $F = dA$, uma 2-forma que contém simultaneamente o campo elétrico e o magnético. Aplicando $d$ novamente, $dF = 0$ — que são duas das equações de Maxwell (ausência de monopolos magnéticos e lei de Faraday).

---

### 4. Por que $d^2 = 0$?

A demonstração é simples. Para uma função $f$,

$$
df = \frac{\partial f}{\partial x^i} dx^i .
$$

Aplicando $d$ novamente,

$$
d(df) = \frac{\partial^2 f}{\partial x^j \partial x^i} \, dx^j \wedge dx^i .
$$

Como $dx^j \wedge dx^i = - dx^i \wedge dx^j$, os termos cancelam **desde que as derivadas mistas comutem** (teorema de Clairaut/Schwarz):

$$
\frac{\partial^2 f}{\partial x^j \partial x^i} = \frac{\partial^2 f}{\partial x^i \partial x^j}.
$$

Portanto, $d^2 = 0$ é uma identidade matemática que decorre da comutatividade das derivadas parciais, válida para funções suficientemente suaves.

É importante distinguir: $d^2 = 0$ é **sempre verdadeiro** para a derivada exterior. Campos conservativos ($d\alpha = 0 \Rightarrow \alpha = df$) são uma consequência do lema de Poincaré, que vale localmente e depende da topologia do domínio.

---

### 5. Por que $\wedge$? O produto exterior como área orientada

O produto exterior $\wedge$ representa a **área orientada** de um paralelogramo. Dados dois deslocamentos infinitesimais $d\mathbf r_1 = (dx_1, dy_1)$ e $d\mathbf r_2 = (dx_2, dy_2)$, a área é

$$
A = dx_1\,dy_2 - dx_2\,dy_1 = \begin{vmatrix} dx_1 & dy_1 \\ dx_2 & dy_2 \end{vmatrix}.
$$

Define-se $dx \wedge dy$ para representar exatamente essa área orientada. As propriedades:

- $dx \wedge dy = - dy \wedge dx$ (orientação: trocar a ordem inverte o sinal)
- $dx \wedge dx = 0$ (caminhar duas vezes na mesma direção não gera área)

**Exemplo físico: o espaço de fases.** Uma partícula sofre um deslocamento $dq$ e uma variação de momento $dp$. Esses dois deslocamentos formam um paralelogramo de área $dq \wedge dp$. Hamilton percebeu que essa área é mais importante que a distância: a evolução temporal pode deformar o paralelogramo, mas sua área permanece constante. Essa é a essência do Teorema de Liouville.

**Exemplo numérico:** Um ensemble de partículas ocupa inicialmente um retângulo $q \in [0,1]$, $p \in [0,1]$ de área 1. Após evoluir sob o oscilador harmônico por um tempo $t$, a região se deforma em um paralelogramo inclinado, mas sua área continua sendo 1.

---

### 6. Derivada exterior vs. derivada covariante

A derivada exterior $d$ **não precisa** de métrica, conexão ou curvatura. Ela existe em qualquer variedade diferenciável — é um objeto topológico/diferencial.

A derivada covariante $\nabla$, por outro lado, precisa de uma conexão $\Gamma^\alpha_{\beta\gamma}$ para comparar vetores em pontos diferentes. O comutador $[\nabla_\mu, \nabla_\nu]$ mede a curvatura:

$$
[\nabla_\mu, \nabla_\nu] V^\rho = R^\rho_{\ \sigma\mu\nu} V^\sigma,
$$

onde $R^\rho_{\ \sigma\mu\nu}$ é o tensor de Riemann.

**Por que a mecânica hamiltoniana usa $d$ e não $\nabla$?** Porque Hamilton não está preocupado com curvatura — ele quer apenas descrever como um sistema evolui no espaço de fases. A estrutura simplética $\omega$ é suficiente para isso.

**Mas e se o espaço de fases for curvo?** Aí a história muda. Em variedades de Kähler, por exemplo, existe simultaneamente a forma simplética $\omega$, a métrica $g$ e a estrutura complexa $J$, e a conexão de Levi-Civita satisfaz

$$
\nabla g = 0, \qquad \nabla J = 0, \qquad \nabla\omega = 0 .
$$

As três estruturas são preservadas simultaneamente. A condição $\nabla\omega = 0$ é chamada de **conexão simplética**.

**Interpretação:** Em teorias mais avançadas (como supergravidade ou teoria de cordas), a geometria do espaço de fases pode ser curva, e aí a derivada covariante se torna essencial. Mas a estrutura simplética — vinda da ação — continua sendo a camada geométrica fundamental.

---

### 7. O teorema de Noether e os três fluxos

Noether perguntou: **como a ação muda quando deformamos continuamente a trajetória?** Considere uma família $q(t,\varepsilon)$ com $\varepsilon$ pequeno. Se

$$
\frac{dS}{d\varepsilon} = 0,
$$

então existe uma quantidade conservada. Essa é a essência do teorema de Noether.

Agora compare três "fluxos" distintos:

| Fluxo | Espaço | Objeto | Ideia |
|---|---|---|---|
| Noether | Trajetórias $q(t)$ | Ação $S$ | Deformar trajetórias, encontrar simetrias |
| Lagrange | $TQ$: $(q,\dot q)$ | $L(q,\dot q)$ | Dinâmica via Euler–Lagrange |
| Hamilton | $T^*Q$: $(q,p)$ | $H(q,p)$ | Evolução no espaço de fases |

**Exemplo: conservação da energia.** Se $L$ não depende explicitamente do tempo, a simetria é translação temporal. Noether dá $H = p\dot q - L$ como quantidade conservada. No espaço de fases, $H$ gera o fluxo hamiltoniano.

**Exemplo: conservação do momento linear.** Se $L$ não depende de uma coordenada $q^k$ (simetria de translação), Noether dá $p_k = \partial L/\partial \dot q^k$ como quantidade conservada. Para a partícula livre, $p$ é constante — e o fluxo hamiltoniano translada $q$ sem alterar $p$.

**Exemplo: conservação do momento angular.** Para uma partícula em potencial central, $L = \frac12 m\dot{\mathbf r}^2 - V(r)$. A simetria de rotação dá $L = \mathbf r \times \mathbf p$ conservado. No espaço de fases, o momento angular gera rotações que preservam $\omega$.

---

### 8. Unificação: a ação gera a estrutura simplética

O elo entre tudo é a sequência

$$
\boxed{\text{Lagrangeana} \longrightarrow \text{Ação} \longrightarrow \theta \longrightarrow \omega \longrightarrow \text{Fluxo hamiltoniano}} .
$$

Em mais detalhe:

1. A Lagrangeana $L$ define a ação $S = \int L\,dt$.
2. Das variações de $S$ surge o momento $p_i = \partial L/\partial \dot q^i$.
3. O momento define a 1-forma canônica $\theta = p_i\,dq^i$, que é o **trabalho infinitesimal**.
4. A derivada exterior $\omega = d\theta$ dá a estrutura simplética — a **área orientada do espaço de fases**.
5. Dado $H$, a equação $i_{X_H}\omega = dH$ define o fluxo hamiltoniano.

**A unificação física:** A ação é o ponto de partida. Dela emergem:
- as equações de movimento (Euler–Lagrange)
- as leis de conservação (Noether)
- a estrutura geométrica do espaço de fases (simplética)
- a dinâmica hamiltoniana

**Exemplo completo: oscilador harmônico.** Começamos com $L = \frac12 m\dot q^2 - \frac12 m\omega^2 q^2$.
1. A ação é $S = \int L\,dt$.
2. O momento é $p = m\dot q$.
3. A 1-forma canônica é $\theta = p\,dq = m\dot q\,dq$.
4. A forma simplética é $\omega = d\theta = dq \wedge dp$.
5. O Hamiltoniano é $H = p^2/(2m) + \frac12 m\omega^2 q^2$.
6. A equação $i_{X_H}\omega = dH$ dá $\dot q = p/m$, $\dot p = -m\omega^2 q$.
7. A órbita no espaço de fases é uma elipse $p^2/(2m) + \frac12 m\omega^2 q^2 = E$.
8. A área $dq \wedge dp$ é preservada — o fluxo é simplético.
9. Se variarmos $t \to t + \varepsilon$, Noether dá $H$ conservado.

Toda a geometria emerge da ação. Nenhum postulado geométrico foi adicionado.

---

### 9. A 1-forma de Poincaré–Cartan: o objeto unificador

Existe um objeto que unifica Lagrange e Hamilton em um só: a **1-forma de Poincaré–Cartan**

$$
\Theta_L = \frac{\partial L}{\partial \dot q^i} \, dq^i - L\, dt = p_i\,dq^i - H\,dt .
$$

Ela vive no espaço estendido $(q,\dot q,t)$ e contém:
- a informação da Lagrangeana (via $L$)
- a informação dos momentos (via $p_i$)
- a informação do Hamiltoniano (via $H$)

A derivada exterior de $\Theta_L$ dá uma forma (pré-)simplética no espaço estendido, e as equações de Euler–Lagrange surgem da condição $i_X \Omega_L = 0$, sem precisar escolher entre formalismo lagrangiano ou hamiltoniano.

**Exemplo: partícula livre.** $\Theta_L = p\,dq - H\,dt = m\dot q\,dq - (p^2/(2m))\,dt$. A condição variacional $\delta\int\Theta_L = 0$ sobre curvas no espaço $(q,p,t)$ reproduz as equações de Hamilton.

**Interpretação:** $\Theta_L$ é a **ação infinitesimal** — o integrando da ação escrito no espaço de fases. Ela mostra que a estrutura simplética e a dinâmica hamiltoniana são meras consequências de reescrever a ação em coordenadas canônicas. A ação, e apenas ela, é o objeto fundamental.
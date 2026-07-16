# Questão 41 — O poço e o oscilador testam a GDQ?

## 1. Veredito

A Questão 41 fica respondida da seguinte forma:

\[
\boxed{
\text{o poço infinito e o oscilador harmônico não validam sozinhos a GDQ,
mas são testes obrigatórios de consistência do limite quântico estacionário.}
}
\]

Eles mostram que a GDQ recupera corretamente o setor
Schrödinger--Madelung em problemas elementares. Porém, recuperar esses
resultados depois de assumir a forma estacionária de Madelung, as condições de
contorno usuais e o ansatz correto para \(R\) não constitui uma predição nova da
teoria.

O teste real da GDQ, nesses exemplos, não é apenas obter:

\[
E_n^{\rm poço}
=
\frac{\hbar^2\pi^2 n^2}{2mL^2},
\qquad
E_n^{\rm osc}
=
\hbar\omega\left(n+\frac12\right).
\]

O teste real é separar quais partes são:

1. consequência direta da equação de Schrödinger reescrita em variáveis de
   Madelung;
2. consequência das condições de contorno;
3. consequência topológica da fase;
4. consequência adicional da dinâmica geométrica da GDQ.

Com essa separação, o capítulo 6 deve ser interpretado como um capítulo de
**recuperação do limite quântico conhecido**, não como demonstração independente
da teoria completa.

Mas isso não significa que o capítulo deva ser descartado. Ele deve ser
reestruturado como uma demonstração da cadeia:

\[
\boxed{
\mathcal S_{\rm GDQ}
\longrightarrow
(\rho,S_R,g)
\longrightarrow
\text{Madelung geométrico}
\longrightarrow
\text{poço/oscilador no limite estacionário}.
}
\]

Assim, o objeto testado deixa de ser a equação de Schrödinger isolada e passa
a ser a coerência da redução GDQ até o regime elementar conhecido.

---

## 2. O problema da auditoria

A crítica central é correta:

\[
\boxed{
\text{recuperar a solução depois de assumir seu ansatz não valida uma teoria nova.}
}
\]

No poço, se já se assume:

\[
\rho(0)=\rho(L)=0,
\qquad
R=\sqrt{\rho},
\qquad
S_R=-Et,
\qquad
\nabla S_R=0,
\]

então a equação de Hamilton--Jacobi--Bohm reduz-se a:

\[
E
=
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
\]

Isso equivale a:

\[
R''+k^2R=0,
\qquad
k^2=\frac{2mE}{\hbar^2}.
\]

Com Dirichlet nas paredes, segue:

\[
R_n(x)=A\sin\left(\frac{n\pi x}{L}\right),
\qquad
k_n=\frac{n\pi}{L},
\]

e:

\[
E_n
=
\frac{\hbar^2 k_n^2}{2m}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
\]

Esse resultado é exatamente o resultado de Schrödinger. A GDQ o recupera, mas
a recuperação depende de uma redução já equivalente ao setor estacionário de
Madelung.

No oscilador, se já se assume o estado fundamental gaussiano:

\[
R(x)=A e^{-\alpha x^2/2},
\]

então:

\[
\frac{R''}{R}=\alpha^2x^2-\alpha.
\]

A equação:

\[
E
=
\frac12m\omega^2x^2
-
\frac{\hbar^2}{2m}
\left(\alpha^2x^2-\alpha\right)
\]

fica independente de \(x\) somente se:

\[
\alpha=\frac{m\omega}{\hbar},
\]

e então:

\[
E_0=\frac12\hbar\omega.
\]

Novamente, isso é uma recuperação correta, mas não é uma dedução autônoma se a
gaussiana foi escolhida como ansatz.

---

## 3. O que é apenas Schrödinger--Madelung

Os seguintes resultados pertencem ao setor padrão de Schrödinger reescrito em
forma hidrodinâmica:

1. a equação estacionária:

   \[
   E
   =
   V
   -
   \frac{\hbar^2}{2m}
   \frac{\nabla^2R}{R};
   \]

2. a interpretação:

   \[
   \rho=R^2;
   \]

3. a condição de corrente nula em estado estacionário real:

   \[
   \nabla S_R=0;
   \]

4. o potencial de Bohm:

   \[
   Q
   =
   -
   \frac{\hbar^2}{2m}
   \frac{\nabla^2R}{R};
   \]

5. os autovalores do poço infinito;
6. a gaussiana do estado fundamental do oscilador;
7. a energia de ponto zero;
8. a escada:

   \[
   E_n=\hbar\omega\left(n+\frac12\right),
   \]

   quando se usa quantização de ação ou operadores usuais.

Portanto, esses pontos não devem ser apresentados como predições novas da GDQ.
Eles são testes de compatibilidade.

---

## 4. Cadeia GDQ correta para esses exemplos

Para trabalhar com a GDQ, o capítulo 6 deve começar da redução variacional já
fechada nas Questões 10, 11 e 12.

A ação oficial é preservada. No setor físico reduzido, as variáveis são:

\[
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
R=\sqrt\rho.
\]

O par canônico é:

\[
\boxed{
(\rho,S_R).
}
\]

A redução Madelung da ação GDQ produz:

\[
I_{\rm Mad}[\rho,S_R,g]
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac12G^{AB}\partial_AS_R\partial_BS_R
+V_{\rm ext}
\right)
+\frac{\hbar^2}{8m}
\frac{G^{AB}\partial_A\rho\,\partial_B\rho}{\rho}
\right]d\mu_g.
\]

Variando a fase:

\[
\frac{\delta I_{\rm Mad}}{\delta S_R}=0
\]

obtém-se:

\[
\boxed{
\partial_t\rho+\nabla_A(\rho v^A)=0,
\qquad
v^A=G^{AB}\partial_BS_R.
}
\]

Variando a densidade:

\[
\frac{\delta I_{\rm Mad}}{\delta\rho}=0
\]

obtém-se:

\[
\boxed{
\partial_tS_R
+\frac12G^{AB}\partial_AS_R\partial_BS_R
+V_{\rm ext}
-
\frac{\hbar^2}{2m}
\frac{\Delta_G\sqrt\rho}{\sqrt\rho}
=0.
}
\]

A variação métrica:

\[
\frac{\delta\mathcal S_{\rm GDQ}}{\delta g^{\mu\bar\nu}}=0
\]

fecha o setor que a mecânica quântica usual não possui:

\[
\boxed{
\mathcal E_{\mu\bar\nu}^{\rm GDQ}
=
\mathcal E_{\mu\bar\nu}^{\rm Ricci}
+\mathcal E_{\mu\bar\nu}^{(f)}
+\mathcal E_{\mu\bar\nu}^{(B)}
=0.
}
\]

No limite de teste elementar, assume-se:

\[
g\to g_{\rm plano},
\qquad
B\to0,
\qquad
\partial_t g\simeq0,
\]

e a equação métrica fica congelada como fundo. Nesse limite, a GDQ deve
recuperar Schrödinger--Madelung. Logo:

\[
\boxed{
\text{poço e oscilador testam a redução plana/estacionária da GDQ.}
}
\]

Eles não testam ainda a retroação métrica completa.

---

## 5. Poço infinito como redução GDQ

No poço infinito, o dado físico não é apenas um potencial externo abstrato. Na
linguagem GDQ, a parede representa uma obstrução geométrica de fluxo:

\[
j^x=\rho\,v^x=0
\quad\text{na fronteira}.
\]

No limite de barreira infinita, essa obstrução força:

\[
\rho|_{\partial\Sigma}=0,
\qquad
R|_{\partial\Sigma}=0.
\]

No interior:

\[
V_{\rm ext}=0,
\qquad
G^{xx}=1/m,
\qquad
\partial_xS_R=0,
\qquad
S_R=-Et.
\]

A equação Hamilton--Jacobi--Bohm reduzida fica:

\[
E
=
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
\]

Portanto:

\[
R''+k^2R=0,
\qquad
k^2=\frac{2mE}{\hbar^2}.
\]

Com:

\[
R(0)=R(L)=0,
\]

segue:

\[
R_n(x)=A\sin\left(\frac{n\pi x}{L}\right),
\qquad
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.
\]

O ponto GDQ não é a equação diferencial em si. O ponto GDQ é a interpretação
constitutiva:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}
\quad\text{é densidade geométrica,}
}
\]

e a parede impõe uma condição de não escoamento da medida geométrica.

Além disso, a condição de fase pode ser escrita como circulação:

\[
\oint_\gamma dS_R
=
\oint_\gamma p\,dx
=
nh.
\]

Para o poço:

\[
2pL=nh,
\qquad
p=\frac{nh}{2L},
\]

e:

\[
E_n=\frac{p^2}{2m}.
\]

Essa segunda rota é a versão topológica/Sudarshan--Sommerfeld da mesma
quantização. Ela é importante para a GDQ porque expressa o espectro como
condição de holonomia da fase \(S_R\), não como postulado de operador.

---

## 6. Oscilador harmônico como redução GDQ

No oscilador:

\[
V_{\rm ext}(x)=\frac12m\omega^2x^2.
\]

No estado estacionário fundamental:

\[
S_R=-E_0t,
\qquad
\nabla S_R=0.
\]

A equação reduzida é:

\[
E_0
=
\frac12m\omega^2x^2
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
\]

Agora, para evitar a crítica do ansatz gratuito, a gaussiana deve ser
apresentada como minimizador do funcional reduzido:

\[
\mathcal E[R]
=
\int_{\mathbb R}
\left[
\frac{\hbar^2}{2m}|R'|^2
+\frac12m\omega^2x^2R^2
\right]dx,
\qquad
\int_{\mathbb R}R^2dx=1.
\]

Com multiplicador de Lagrange \(E\), a variação:

\[
\delta
\left(
\mathcal E[R]-E\int R^2dx
\right)=0
\]

produz:

\[
-
\frac{\hbar^2}{2m}R''
+\frac12m\omega^2x^2R
=
ER.
\]

O estado fundamental é o minimizador positivo. Testando a forma:

\[
R_0(x)=A e^{-\alpha x^2/2},
\]

a condição de cancelamento dos termos em \(x^2\) exige:

\[
\alpha=\frac{m\omega}{\hbar},
\]

e:

\[
E_0=\frac12\hbar\omega.
\]

Assim, no texto revisado, a gaussiana não deve aparecer como chute físico
primário. Ela deve aparecer como solução do problema variacional reduzido.

Para estados excitados, a quantização GDQ deve ser formulada por circulação no
espaço de fase:

\[
\oint p\,dx
=
h\left(n+\frac{\mu}{4}\right).
\]

Para o oscilador unidimensional há dois pontos de retorno, logo:

\[
\mu=2,
\qquad
\oint p\,dx=h\left(n+\frac12\right).
\]

Como:

\[
\oint p\,dx=\frac{2\pi E}{\omega},
\]

segue:

\[
E_n=\hbar\omega\left(n+\frac12\right).
\]

Na linguagem GDQ, o índice de Maslov é reinterpretado como fase de
fronteira/cáustica do contorno de Sudarshan--Cartan.

---

## 7. O que a GDQ acrescenta nesses exemplos

A GDQ acrescenta conteúdo apenas quando algum elemento não é meramente copiado
da formulação estacionária de Schrödinger. Nos dois exemplos, os acréscimos
defensáveis são:

### 7.1 Interpretação geométrica de \(\rho\)

Na GDQ, \(\rho\) não é apenas uma densidade probabilística operacional. Ela é a
densidade geométrica induzida pelo campo fundamental:

\[
\rho=e^{-(f+\bar f)/2}.
\]

Assim, a regra de Born e a hidrodinâmica de Madelung entram como setor
reconstruído da geometria, não como postulado isolado.

### 7.2 Condição de contorno como obstrução geométrica

No poço infinito, a condição:

\[
R(0)=R(L)=0
\]

pode ser reinterpretada como impossibilidade de escoamento da densidade
geométrica através de uma fronteira topologicamente intransponível.

Mas essa interpretação não altera o espectro. Ela apenas dá leitura geométrica
para uma condição de Dirichlet que já existia.

### 7.3 Quantização por circulação

A condição:

\[
\oint p\,dx=nh
\]

ou, no caso com pontos de retorno,

\[
\oint p\,dx
=
h\left(n+\frac12\right),
\]

pode ser lida na GDQ como condição de holonomia/circulação da fase no contorno
causal fechado.

O acréscimo real aqui é interpretativo e topológico: a fase não é apenas uma
variável auxiliar da função de onda, mas a circulação do setor \(S_R\).

### 7.4 Índice de Maslov como torção de fronteira

No oscilador, o termo:

\[
\frac12
\]

é o índice de Maslov associado aos dois pontos de retorno. Na GDQ, ele pode ser
reinterpretado como contribuição de torção/holonomia nas cáusticas.

Isso é coerente com a estrutura da teoria, mas deve ser apresentado como
identificação geométrica de uma fase semiclassicamente conhecida, não como
descoberta independente.

---

## 8. O que ainda seria um teste propriamente GDQ

Para que poço e oscilador se tornem testes reais da GDQ, seria necessário
mostrar algum efeito que dependa da dinâmica métrica adicional e desapareça no
limite Schrödinger--Madelung puro.

Exemplos de testes válidos:

### 8.1 Correção de parede finita

Substituir a parede ideal por uma fronteira geométrica de espessura finita:

\[
R(0)=R(L)=0
\quad\longrightarrow\quad
\text{condição Robin/impedância geométrica}.
\]

Então a GDQ deveria prever o deslocamento:

\[
E_n
=
\frac{\hbar^2\pi^2 n^2}{2mL^2}
+\Delta E_n^{\rm GDQ},
\]

com \(\Delta E_n^{\rm GDQ}\) derivado da geometria de contorno, não ajustado.

Uma forma mínima de fazer isso sem alterar a ação oficial é manter o bulk
plano e substituir a parede ideal por uma ação quadrática de fronteira:

\[
I_{\partial}
=
\frac{\hbar^2}{2m}
\int dt
\left[
\lambda_0 R^2(0,t)
+\lambda_L R^2(L,t)
\right].
\]

Somando:

\[
I_{\rm bulk}
=
\int dt\int_0^L
\left[
\frac{\hbar^2}{2m}|R'|^2
+V R^2
\right]dx,
\]

a variação em \(R\) gera, no bulk:

\[
-
\frac{\hbar^2}{2m}R''
+VR
=
ER,
\]

e nas fronteiras:

\[
\boxed{
R'(0)=\lambda_0 R(0),
\qquad
R'(L)=-\lambda_L R(L).
}
\]

Esse é o problema Robin geométrico. O limite:

\[
\lambda_0,\lambda_L\to+\infty
\]

recupera Dirichlet:

\[
R(0)=R(L)=0.
\]

Para \(V=0\), a solução:

\[
R(x)=A\cos(kx)+B\sin(kx)
\]

obedece à equação espectral:

\[
\boxed{
(\lambda_0\lambda_L-k^2)\sin(kL)
+k(\lambda_0+\lambda_L)\cos(kL)=0.
}
\]

No caso simétrico:

\[
\lambda_0=\lambda_L=\lambda_\partial,
\]

e no regime de parede quase rígida:

\[
\lambda_\partial L\gg1,
\]

os autovalores têm expansão:

\[
k_n
=
\frac{n\pi}{L}
\left[
1-\frac{2}{\lambda_\partial L}
+O((\lambda_\partial L)^{-2})
\right].
\]

Logo:

\[
\boxed{
E_n^{\rm Robin}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}
\left[
1-\frac{4}{\lambda_\partial L}
+O((\lambda_\partial L)^{-2})
\right].
}
\]

Interpretação GDQ:

\[
\boxed{
\lambda_\partial
\text{ é a impedância geométrica da fronteira.}
}
\]

O teste forte seria derivar \(\lambda_\partial\) da Hessiana de contorno da
ação GDQ, por complemento de Schur dos modos de superfície, exatamente como foi
feito em Q40 para a impedância coletiva:

\[
\lambda_\partial(q)
=
\lambda_{\rm bare}
-
J_\partial^\dagger(q)K_\partial^{-1}(q)J_\partial(q).
\]

Nesse caso, a correção \(\Delta E_n^{\rm GDQ}\) deixaria de ser parametrização
de Robin e passaria a ser previsão geométrica.

### 8.2 Oscilador em fundo curvo

Resolver o oscilador não em \(\mathbb R\) plano, mas sobre fundo efetivo
curvo:

\[
\Delta
\longrightarrow
\Delta_g,
\]

com medida:

\[
d\mu_g=\sqrt g\,dx.
\]

O teste seria obter correções geométricas:

\[
E_n
=
\hbar\omega\left(n+\frac12\right)
+\Delta E_n[g,f,B],
\]

controladas por curvatura, torção ou fluxo de Perelman.

A extensão mínima é escrever a energia reduzida em uma dimensão com métrica:

\[
ds^2=a^2(x)\,dx^2,
\qquad
d\mu_g=a(x)\,dx.
\]

O operador cinético é o Laplace--Beltrami:

\[
\Delta_g R
=
\frac1a\partial_x
\left(
\frac1a\partial_x R
\right).
\]

O funcional estacionário torna-se:

\[
\mathcal E_g[R]
=
\int
\left[
\frac{\hbar^2}{2m}
g^{xx}|\partial_xR|^2
+\frac12m\omega^2x^2R^2
+V_{\rm tor}(x)R^2
\right]d\mu_g.
\]

Para uma perturbação fraca:

\[
a(x)=1+\varepsilon h(x),
\qquad
V_{\rm tor}(x)=\varepsilon W_T(x),
\qquad
|\varepsilon|\ll1,
\]

o deslocamento espectral de primeira ordem é:

\[
\boxed{
\Delta E_n^{\rm GDQ}
=
\varepsilon
\langle n|
\delta\mathcal H_g+\delta V_T
|n\rangle
}
\]

com:

\[
\delta V_T=W_T(x),
\]

e \(\delta\mathcal H_g\) vindo da expansão do Laplace--Beltrami e da medida.
De modo equivalente, usando coordenada geodésica \(y\), definida por:

\[
dy=a(x)\,dx,
\]

o efeito aparece como uma deformação do potencial harmônico:

\[
x(y)=y-\varepsilon H(y)+O(\varepsilon^2),
\qquad
H'(y)=h(y),
\]

logo:

\[
\frac12m\omega^2x^2
=
\frac12m\omega^2y^2
-
\varepsilon m\omega^2yH(y)
+O(\varepsilon^2).
\]

Portanto:

\[
\boxed{
\Delta E_n^{\rm geom}
=
-
\varepsilon m\omega^2
\langle n|yH(y)|n\rangle
+
\varepsilon\langle n|W_T(y)|n\rangle.
}
\]

Esse é um teste realmente GDQ porque:

1. desaparece no limite plano:

   \[
   h=W_T=0;
   \]

2. depende de dados geométricos \(g,B,f\);
3. pode ser comparado com o espectro estacionário;
4. exige derivar \(h\) e \(W_T\) da equação métrica, não escolhê-los livremente.

### 8.3 Relaxação por fluxo geométrico

Em vez de assumir diretamente a gaussiana do oscilador, deve-se mostrar que o
fluxo GDQ leva genericamente a ela como atrator:

\[
R(\tau,x)
\xrightarrow{\tau\to\infty}
A e^{-m\omega x^2/(2\hbar)}.
\]

Isso transformaria o ansatz em consequência dinâmica.

No formalismo GDQ, a versão correta é estudar o fluxo de gradiente do
funcional:

\[
\partial_\tau R
=
-
\frac{\delta}{\delta R}
\left[
\mathcal E[R]-E\int R^2dx
\right].
\]

Para o oscilador plano:

\[
\partial_\tau R
=
\frac{\hbar^2}{2m}R''
-
\frac12m\omega^2x^2R
+ER.
\]

Expandindo em autofunções do oscilador:

\[
R(\tau,x)=\sum_n c_n(\tau)R_n(x),
\]

tem-se:

\[
c_n(\tau)=c_n(0)e^{-(E_n-E_0)\tau}
\]

após normalização pelo modo fundamental. Como:

\[
E_n-E_0>0
\qquad(n>0),
\]

segue:

\[
R(\tau,x)\to R_0(x).
\]

Essa é a forma limpa de dizer que a gaussiana é atrator: não por escolha, mas
por dominância espectral do fluxo.

### 8.4 Estabilidade Hessiana

Calcular a Hessiana da ação reduzida ao redor do estado estacionário:

\[
\delta^2\mathcal S_{\rm GDQ}[R_n,S_n,g_n,f_n].
\]

O teste real seria mostrar:

\[
\delta^2\mathcal S_{\rm GDQ}\ge 0
\]

para estados permitidos e instabilidade para configurações que violam a
quantização topológica.

No poço, a Hessiana reduzida ao redor de \(R_n\) é:

\[
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
-E_n
\]

no subespaço ortogonal ao modo \(R_n\), com a mesma condição de contorno.

Para o estado fundamental:

\[
\lambda_k(\mathcal J_1)
=
E_k-E_1\ge0
\qquad(k\ge1),
\]

módulo a direção de normalização. Portanto o estado fundamental é estável.

Para estados excitados, existem direções inferiores:

\[
E_j-E_n<0
\qquad(j<n),
\]

ou seja, eles são estacionários, mas não minimizadores globais. Essa distinção
é importante para o texto: estados excitados são permitidos por holonomia e
estabilidade dinâmica de fase, mas não são mínimos absolutos do funcional de
energia.

No oscilador ocorre o mesmo:

\[
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
+\frac12m\omega^2x^2
-E_n.
\]

O estado \(n=0\) é mínimo; os estados \(n>0\) são pontos críticos com índice de
Morse \(n\). Na linguagem GDQ, esse índice de Morse deve ser compatível com o
índice de Maslov/contorno.

---

## 8.5 Produto técnico sugerido para fechar o teste forte

Para transformar a Q41 em teste forte, sem alongar o manuscrito principal,
deve-se criar um adendo técnico:

\[
\boxed{
\texttt{q41/testes\_gdq\_poco\_oscilador.md}
}
\]

Esse adendo foi criado como documento técnico complementar.

Conteúdo mínimo:

1. derivação do Robin geométrico por variação de \(I_{\partial}\);
2. equação espectral Robin;
3. limite Dirichlet;
4. deslocamento \(\Delta E_n^{\rm GDQ}\);
5. oscilador em métrica fraca \(a(x)=1+\varepsilon h(x)\);
6. fórmula de primeira ordem para \(\Delta E_n^{\rm geom}\);
7. fluxo de relaxação para provar atrator gaussiano;
8. Hessiana/índice de Morse para poço e oscilador.

Com isso, a Q41 deixa de ser apenas uma resposta defensiva e passa a indicar
um programa concreto de testes elementares da GDQ.

---

## 9. Como o capítulo 6 deve ser reclassificado

O capítulo 6 deve ser mantido, mas com linguagem mais precisa.

Classificação correta:

\[
\boxed{
\text{capítulo de correspondência e consistência, não capítulo de validação forte.}
}
\]

Formulação recomendada:

> O poço infinito e o oscilador harmônico demonstram que a GDQ contém o limite
> estacionário de Schrödinger--Madelung e oferece uma interpretação geométrica
> para densidade, potencial de Bohm, condições de contorno e índice de Maslov.
> Esses exemplos não constituem, por si só, predições novas; eles estabelecem
> compatibilidade com o setor quântico elementar.

Evitar frases do tipo:

1. “a GDQ prova o poço infinito”;
2. “a GDQ deriva o oscilador sem Schrödinger”;
3. “a energia de ponto zero foi obtida sem postulado quântico”;
4. “isso valida a teoria”.

Usar em vez disso:

1. “a GDQ recupera o limite estacionário”;
2. “a GDQ reinterpreta geometricamente”;
3. “a GDQ identifica a fase de Maslov como holonomia/torção de fronteira”;
4. “isso é um teste de consistência do limite conhecido”.

---

## 10. Resposta direta à questão

O poço e o oscilador testam a GDQ apenas em sentido fraco:

\[
\boxed{
\text{eles testam se a teoria contém corretamente a mecânica quântica elementar.}
}
\]

Eles não testam, sozinhos, o conteúdo novo da GDQ:

\[
\boxed{
\text{não testam de modo decisivo a dinâmica métrica adicional.}
}
\]

Para transformá-los em testes fortes, o documento deve acrescentar pelo menos
uma das seguintes derivações:

1. correções de energia por contorno geométrico finito;
2. oscilador em fundo curvo/torsional;
3. prova de atrator do estado fundamental pelo fluxo GDQ;
4. Hessiana de estabilidade da ação oficial;
5. deslocamento espectral dependente de \(g,f,B\), com limite plano recuperando
   Schrödinger.

Assim, a Questão 41 fica fechada como auditoria conceitual:

\[
\boxed{
\text{os exemplos são válidos como correspondência, mas não devem ser usados
como prova independente da GDQ.}
}
\]

Com a reestruturação acima, a formulação fica mais forte:

\[
\boxed{
\text{Q41 fica fechada como teste de redução GDQ}
\quad
\mathcal S_{\rm GDQ}
\to
\text{Madelung geométrico}
\to
\text{limite estacionário elementar}.
}
\]

O fechamento não afirma que poço e oscilador provam a teoria completa. Afirma
que eles verificam que a ação GDQ, quando reduzida ao regime plano e
estacionário, contém exatamente a mecânica quântica elementar e fornece uma
leitura geométrica para densidade, contorno, fase e índice de Maslov.

---

## 11. Consolidação oficial da Q41

### 11.1 Resultados efetivamente demonstrados

1. A redução plana e estacionária da ação produz as equações de
   continuidade e Hamilton--Jacobi--Bohm.
2. O poço com Dirichlet recupera
   \[
   E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.
   \]
3. A condição de circulação recupera a mesma quantização e deve ser lida como
   holonomia da fase, não como previsão adicional independente.
4. O estado fundamental do oscilador é obtido como minimizador do funcional,
   e não precisa ser postulado como ansatz:
   \[
   R_0(x)\propto e^{-m\omega x^2/(2\hbar)},
   \qquad E_0=\frac12\hbar\omega.
   \]
5. O fluxo de gradiente normalizado converge para \(R_0\) com taxas
   \(E_n-E_0>0\); a gaussiana é atrator espectral.
6. A Hessiana possui índices de Morse corretos: \(n-1\) para o nível \(n\ge1\)
   do poço e \(n\) para o nível \(n\ge0\) do oscilador.
7. A correção de Maslov \(1/2\) decorre dos dois pontos de retorno; sua leitura
   como torção de Cartan é uma interpretação GDQ da fase semiclassicamente
   conhecida.

### 11.2 Resultados formulados, mas dependentes de dados físicos adicionais

1. A parede finita satisfaz a equação Robin
   \[
   (\lambda_0\lambda_L-k^2)\sin(kL)
   +k(\lambda_0+\lambda_L)\cos(kL)=0,
   \]
   mas \(\lambda_0,\lambda_L\) só se tornam previsões depois que a geometria
   material da parede for especificada e sua Hessiana calculada.
2. O oscilador curvo possui correção
   \[
   \Delta E_n^{\rm geom}
   =-\varepsilon m\omega^2\langle n|yH(y)|n\rangle
   +\varepsilon\langle n|W_T(y)|n\rangle,
   \]
   mas \(h\) e \(W_T\) dependem do background escolhido.

Essas dependências não são lacunas da resposta à Q41: um deslocamento
espectral de parede ou de curvatura não pode ser um número universal sem
definir a parede ou a geometria perturbadora.

### 11.3 Veredito oficial

\[
\boxed{
\text{Q41 encerrada como teste de correspondência e consistência da redução
GDQ.}
}
\]

\[
\boxed{
\text{Poço e oscilador não constituem validação independente da dinâmica
métrica completa.}
}
\]

Os testes fortes universais que podiam ser realizados sem introduzir um
background arbitrário — atrator, Hessiana, índice de Morse e limite plano — já
foram realizados. Correções numéricas de Robin ou curvatura devem ser tratadas
posteriormente como previsões de experimentos concretos, não como condição
para encerrar esta questão conceitual.

### 11.4 Fechamento formal da impedância do poço

A derivação que faltava para a parede física foi consolidada em
`q41/adendo_impedancia_parede_gdq.md`.

Ela demonstra que a condição Robin não precisa ser imposta arbitrariamente.
Para a continuação do modo do poço no material, a impedância é o mapa
Dirichlet--Neumann da Hessiana física da parede:

\[
\lambda_\partial(E,q)=\Lambda_{\rm DN}[K_{\rm w}](E,q).
\]

Quando a parede contém modos auxiliares de superfície acoplados ao valor de
fronteira, a resposta aparece como complemento de Schur:

\[
\lambda_\partial
=
\lambda_{\rm bare}
-J_\partial^\dagger K_{\rm w}^{-1}J_\partial.
\]

Para uma parede homogênea semi-infinita, com operador projetado

\[
K_{\rm w}=-A_\partial\partial_y^2+M_\partial^2,
\]

obtém-se

\[
\boxed{
\lambda_\partial=A_\partial\Omega,
\qquad
\Omega^2=A_\partial^{-1}M_\partial^2.
}
\]

O limite \(A_\partial\Omega\to\infty\) recupera Dirichlet. Assim, a falta
formal universal foi removida; a obtenção de um número requer escolher um
material concreto e avaliar sua Hessiana GDQ estacionária.

### 11.5 Verificação numérica da redução de parede

A implementação está em `q41/solve_poco_gdq.py` e seu relatório reproduzível
em `q41/resultado_poco_gdq.md`.

O teste usa unidades

\[
L=1,
\qquad
\frac{\hbar^2}{2mL^2}=1,
\]

uma parede homogênea com

\[
V_0=1000,
\qquad
d=0.25L,
\]

e compara três cálculos:

1. mapa Dirichlet--Neumann/Robin;
2. diagonalização direta da barreira finita;
3. espectro padrão do poço infinito.

Na malha mais fina, com \(9599\) pontos, o erro relativo máximo entre os cinco
primeiros níveis obtidos pelas duas descrições da parede foi

\[
\boxed{
\varepsilon_{\max}=3.437\times10^{-7}.
}
\]

O refinamento de malha forneceu ordem empírica

\[
\boxed{
p\simeq2.002,
}
\]

compatível com o esquema de diferenças finitas de segunda ordem. O teste
adicional \(V_0\to\infty\) mostrou a aproximação monotônica ao espectro

\[
E_n^{(\infty)}=(n\pi)^2.
\]

Portanto, a implementação confirma numericamente a equivalência entre a
eliminação variacional da parede e a mecânica quântica padrão da barreira
finita. Trata-se de teste de consistência, não de previsão material nova:
\(V_0\) ainda representa o background reduzido escolhido, e não um coeficiente
calculado para um material real pela ação oficial.

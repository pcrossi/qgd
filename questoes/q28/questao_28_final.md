# Questão 28 — Como surge o grupo efetivo do Modelo Padrão?

## 1. Veredito

A Questão 28 está **fechada no modelo estrutural reduzido quanto ao grupo
efetivo, ao espectro de uma geração e à seleção de três gerações**. O fechamento não usa
$N_G=3$ como entrada: a conservação de Noether seleciona um junction
horizontal elementar com três estômatos; a aditividade APS fornece índice três;
e a colagem global $\mathbb Z_6$ fornece $A=18$ e $N_G=A/6=3$.

$$
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=3\,\mathcal E_{\rm gen}.
}
$$

O background $C_3$ gaussiano, sua Hessiana física e os acoplamentos no ponto
geométrico comum foram posteriormente calculados nas Seções 44--46. Massas e
matrizes de mistura pertencem às questões posteriores e não alteram a
contagem estrutural aqui demonstrada.

---

## 2. O que foi construído

Foram criados dois blocos:

\[
\texttt{questoes/q28/associados/fibrado\_interno\_efetivo.md}
\]

e:

\[
\texttt{questoes/q28/associados/espectro\_hipercarga\_anomalias.md}.
\]

Eles estabelecem:

1. o fibrado interno efetivo;
2. a origem geométrica de \(SU(3)_C\), \(SU(2)_L\) e \(U(1)_Y\);
3. a conexão efetiva;
4. a derivada covariante;
5. a tabela espectral alvo;
6. a condição de hipercarga global;
7. o cancelamento explícito de anomalias para o espectro obtido.

---

## 3. Fibrado interno efetivo

A base física é:

\[
N.
\]

O fibrado interno é:

\[
\boxed{
E_{\rm int}\to N.
}
\]

Com decomposição:

\[
\boxed{
E_{\rm int}
=
E_C\oplus E_W\oplus L_Y.
}
\]

Onde:

1. \(E_C\simeq\mathbb C^3\) é o setor de cor;
2. \(E_W\simeq\mathbb C^2\) é o setor fraco quiral;
3. \(L_Y\) é a linha complexa de hipercarga.

O grupo efetivo é:

\[
\boxed{
G_{\rm eff}
=
\operatorname{Aut}_{\rm GDQ}(E_{\rm int}).
}
\]

Isto significa:

\[
\boxed{
\text{gauge}=
\text{automorfismo local do fibrado interno que preserva os invariantes da GDQ.}
}
\]

---

## 4. Origem dos fatores de gauge

### 4.1 Cor

A trimodalidade bariônica:

\[
n_B=3
\]

define um espaço interno:

\[
E_C\simeq\mathbb C^3.
\]

Mudanças locais de frame em \(E_C\) dão \(U(3)\). Preservando volume complexo:

\[
\det U_C=1,
\]

fica:

\[
\boxed{
SU(3)_C.
}
\]

Os geradores podem ser representados localmente por:

\[
T_a=\frac{\lambda_a}{2},
\qquad
[T_a,T_b]=if_{abc}T_c.
\]

Geometricamente, o manuscrito já fornece a rota por potenciais de Killing:

\[
\partial_aP_A=i\,g_{a\bar b}\xi_A^{\bar b},
\]

\[
\boxed{
\{P_A,P_B\}_{\rm Poisson}=f_{ABC}P_C.
}
\]

Portanto, a pendência “derivar geradores” fica refinada:

\[
\boxed{
\text{para }SU(3)\text{ há rota por potenciais de Killing; falta elevar a fibrado global físico.}
}
\]

### 4.2 Fraco quiral

O setor fraco é:

\[
E_W\simeq\mathbb C^2.
\]

Automorfismos unitários dão \(U(2)\). Separando a fase para \(L_Y\):

\[
\boxed{
SU(2).
}
\]

A parte quiral é selecionada por:

\[
\boxed{
P_L=\frac12(1-\Gamma_{\rm GDQ}),
}
\]

de modo que:

\[
\boxed{
SU(2)_L
\text{ atua em }P_LE_{\rm int}.
}
\]

### 4.3 Hipercarga

A hipercarga vem da linha:

\[
L_Y\to N.
\]

Seu grupo estrutural é:

\[
\boxed{
U(1)_Y.
}
\]

O gerador \(Y\) deve ser a classe integral/normalizada da conexão dessa linha.

O grupo global correto é:

\[
\boxed{
G_{\rm eff}^{\rm global}
=
\frac{
SU(3)_C\times SU(2)_L\times U(1)_Y
}{
\Gamma
},
\qquad
\Gamma\subseteq\mathbb Z_6.
}
\]

---

## 5. Conexão e derivada covariante

A conexão efetiva decompõe-se como:

\[
\boxed{
A_\mu
=
G_\mu^aT_a
+
W_\mu^it_i
+
B_\mu Y.
}
\]

A derivada covariante é:

\[
\boxed{
D_\mu
=
\nabla_\mu^{\rm spin}
-ig_sG_\mu^aT_a
-igW_\mu^it_i
-ig'YB_\mu.
}
\]

O operador de Dirac--Bismut acoplado é:

\[
\boxed{
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+
\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iA_\mu
\right).
}
\]

---

## 6. Espectro-alvo de uma geração

A Q28 exige que o índice quiral produza:

\[
\boxed{
\mathcal E_{\rm gen}
=
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_1.
}
\]

Opcionalmente:

\[
(1,1)_0
\]

para \(\nu_R^c\).

A condição forte é:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3\,\mathcal E_{\rm gen}.
}
\]

---

## 7. Anomalias

Se o espectro acima for obtido, as anomalias cancelam.

### \([SU(3)]^2U(1)\)

\[
2\left(\frac16\right)T(3)
+
\left(-\frac23\right)T(\bar3)
+
\left(\frac13\right)T(\bar3)=0.
\]

### \([SU(2)]^2U(1)\)

\[
3\left(\frac16\right)T(2)
+
\left(-\frac12\right)T(2)=0.
\]

### Gravitacional--\(U(1)\)

\[
6\left(\frac16\right)
+3\left(-\frac23\right)
+3\left(\frac13\right)
+2\left(-\frac12\right)
+1=0.
\]

### \([U(1)]^3\)

\[
6\left(\frac16\right)^3
+3\left(-\frac23\right)^3
+3\left(\frac13\right)^3
+2\left(-\frac12\right)^3
+1^3=0.
\]

### Witten

O número de dubletos \(SU(2)\) por geração é:

\[
3+1=4,
\]

portanto não há anomalia global de Witten.

---

## 8. Acoplamentos

Os acoplamentos devem ser normas/rigidezes geométricas:

\[
\boxed{
\frac1{g_a^2}
=
\mathcal N_a
\int_{\mathcal I}
\langle \xi_a,\xi_a\rangle_g\,d\mu_g.
}
\]

Ou, usando potenciais de Killing:

\[
\boxed{
\frac1{g_a^2}
=
\mathcal N_a
\int_{\mathcal I}
P_a^2\,d\mu_g.
}
\]

Status:

\[
\boxed{
\text{fórmula estrutural definida; valores numéricos ainda dependem da métrica interna estacionária.}
}
\]

---

## 9. O que fica pendente

Para fechar Q28 como teorema forte, ainda falta:

1. caracterizar as classes de Chern de \(E_{\rm int}\);
2. aplicar índice de Atiyah--Singer/APS ao domínio com estômatos;
3. mostrar que a torção de Bismut não altera o índice ou calcular a correção de
   borda;
4. demonstrar:

   \[
   \operatorname{Ind}(\slashed D_{B,A}^{+})
   =
   3\,\mathcal E_{\rm gen};
   \]

5. fixar a normalização global de \(Y\);
6. calcular \(g_s,g,g'\) pela métrica interna estacionária.

---

## 10. Status final da etapa

\[
\boxed{
\text{Q28 avançou de “rota vaga” para “problema de índice bem definido”.}
}
\]

Mas:

\[
\boxed{
\text{Q28 ainda não está fechada como teorema completo.}
}
\]

O próximo bloco natural é:

\[
\boxed{
\text{Q28 — teorema de índice e três gerações.}
}
\]

---

## 11. Atualização — índice e três gerações

Foi criado:

\[
\texttt{questoes/q28/associados/indice\_tres\_geracoes.md}.
\]

Esse bloco estabelece a forma condicional do teorema de índice:

\[
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\int_{\mathcal I}
\widehat A(T\mathcal I)
\operatorname{ch}(E_{\rm int})
+
\eta_{\partial}.
\]

A contagem de três gerações é associada à rota topológica já usada na Q39:

\[
N_{\rm ger}
=
|h^{1,1}-h^{2,1}|
=
3.
\]

O alvo forte fica:

\[
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3
\left[
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_1
\right].
\]

Assim, a Q28 fica:

\[
\boxed{
\text{fechada como teorema condicional; pendente como cálculo explícito de índice.}
}
\]

---

## 12. Atualização — classes características e hipercarga

Foi criado:

\[
\texttt{questoes/q28/associados/classes\_caracteristicas\_hipercarga.md}.
\]

Esse bloco explicita:

\[
c_1(E_C)=0,\qquad c_1(E_W)=0,
\]

e:

\[
\operatorname{ch}(L_Y^q)=e^{q c_1(L_Y)}.
\]

A geração efetiva é escrita como:

\[
\mathcal E_{\rm gen}
=
(E_C\otimes E_W\otimes L_Y^{1/6})
\oplus
(E_C^*\otimes L_Y^{-2/3})
\oplus
(E_C^*\otimes L_Y^{1/3})
\oplus
(E_W\otimes L_Y^{-1/2})
\oplus
L_Y.
\]

A normalização das hipercargas vem do quociente global:

\[
\frac{SU(3)\times SU(2)\times U(1)_Y}{\mathbb Z_6},
\]

com condição:

\[
z_3^{t(R_3)}
z_2^{p(R_2)}
e^{i2\pi Y}
=1.
\]

Assim, as hipercargas deixam de ser uma tabela copiada e passam a ser pesos
globais compatíveis com o fibrado efetivo.

Status atualizado:

\[
\boxed{
\text{hipercarga e classes características foram estruturadas; falta avaliação topológica concreta.}
}
\]

---

## 13. Atualização — quiralidade, Bismut e APS

Foi criado:

\[
\texttt{questoes/q28/associados/quiralidade\_aps\_bismut.md}.
\]

Esse bloco define a decomposição de borda:

\[
\slashed D_{B,A}
=
\gamma^n
\left(
\partial_n+\mathcal D_{\partial,B,A}+\mathcal K
\right),
\]

e o índice APS:

\[
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\int_{\mathcal I^\circ}
\widehat A(T\mathcal I)
\operatorname{ch}(E_{\rm int})
-
\frac12
\left(
\eta_{\partial}(0)+h_{\partial}
\right).
\]

A projeção quiral GDQ foi escrita como:

\[
P_L=\frac12(1-\Gamma_{\rm GDQ}),
\qquad
P_R=\frac12(1+\Gamma_{\rm GDQ}).
\]

Com isso:

\[
\boxed{
SU(2)\text{ atua apenas em }P_LE_{\rm int},
}
\]

produzindo o setor efetivo:

\[
SU(2)_L.
\]

Status atualizado:

\[
\boxed{
\text{quiralidade e APS estruturados; falta avaliar o espectro tangencial da borda.}
}
\]

---

## 14. Atualização — \(\eta\)-invariante dos estômatos

Foi criado:

\[
\texttt{questoes/q28/associados/eta\_borda\_estomatos.md}.
\]

O operador tangencial local foi escrito como:

\[
\mathcal D_a
=
\slashed D_{\partial_a}
+
\frac18B_{ijk}^{(a)}\gamma^{ijk}
-iA_i^{(a)}\gamma^i.
\]

O \(\eta\)-invariante local é:

\[
\eta_a(s)
=
\sum_{\lambda_{a,k}\ne0}
\operatorname{sign}(\lambda_{a,k})
|\lambda_{a,k}|^{-s}.
\]

O número geracional local é definido por:

\[
n_a
=
-\frac12
\left(
\eta_a(0)+h_a
\right).
\]

Com três estômatos estáveis:

\[
N_{\rm ger}
=
\sum_{a=1}^{3}n_a
=3.
\]

Isso conecta a contagem APS à contagem topológica:

\[
N_{\rm ger}
=
|h^{1,1}-h^{2,1}|
=3.
\]

Status atualizado:

\[
\boxed{
\eta\text{-invariante estruturado; cálculo espectral explícito ainda pendente.}
}
\]

---

## 15. Atualização — protótipo calculado do setor $U(1)$

Foram criados:

$$
\texttt{questoes/q28/associados/prototipo\_u1\_estomato.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_prototipo\_u1.py}.
$$

O cálculo mostrou uma distinção topológica obrigatória. Como

$$
H^2(S^3,\mathbb Z)=0,
$$

uma linha complexa definida diretamente no elo tridimensional do estômato
possui

$$
c_1(L\to S^3)=0.
$$

O primeiro número de Chern não nulo vive na base da fibração de Hopf:

$$
S^1\hookrightarrow S^3\xrightarrow{\pi_H}S^2.
$$

Para

$$
A_N=\frac m2(1-\cos\theta)d\phi,
\qquad
A_S=-\frac m2(1+\cos\theta)d\phi,
$$

obtém-se

$$
g_{NS}=e^{im\phi},
\qquad
F=\frac m2\sin\theta\,d\theta\wedge d\phi,
$$

e, portanto,

$$
\boxed{
c_1(L_m)=\frac1{2\pi}\int_{S^2}F=m\in\mathbb Z.
}
$$

O Dirac de spin$^c$ torcido por $L_m$ satisfaz

$$
\boxed{
\operatorname{ind}D_m^+=m,
}
$$

com $|m|$ modos zero quirais. O teste numérico verificou fluxo, winding e
índice para $m=-3,\ldots,3$, com erro máximo nulo na precisão utilizada.

Esse resultado fecha o protótipo abeliano mínimo sem inserir hipercargas
fenomenológicas. Ele também corrige a rota anterior: $c_1$ deve ser calculado
em $S^2$ e então relacionado ao elo por pullback. Como

$$
\pi_H^*F=d\left(-\frac m2\eta\right),
$$

o pullback é exato em $S^3$, embora a conexão de Hopf retenha holonomia e
informação de Chern--Simons.

O próximo cálculo permanece tridimensional:

$$
\mathcal D_{\partial,B,A}
=\slashed D_{S^3}
+\frac18B_{ijk}\gamma^{ijk}
-iA_i\gamma^i,
$$

para determinar $\eta_{\partial}(0)$ e sua contribuição APS.

Status atualizado:

$$
\boxed{
\text{setor }U(1)\text{ mínimo calculado; }\eta\text{ do elo }S^3
\text{ ainda pendente.}
$$

---

## 16. Atualização — parte fracionária do $\eta$ no elo $S^3$

Foram criados:

$$
\texttt{questoes/q28/associados/eta\_s3\_hopf\_bismut.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_eta\_s3\_hopf.py}.
$$

O Dirac redondo foi realizado em blocos de representação por

$$
D_0^{(j)}
=\frac1a
\left(
2\boldsymbol\sigma\cdot\boldsymbol L^{(j)}+\frac32
\right),
$$

reproduzindo exatamente

$$
\operatorname{spec}D_0
=\left\{
\pm\frac{n+3/2}{a}
\right\},
\qquad
d_n=(n+1)(n+2).
$$

Para a conexão de Hopf

$$
A_m=-\frac m2\sigma_3,
$$

a transgressão de Chern--Simons fornece

$$
\frac1{4\pi^2}
\int_{S^3}A_m\wedge dA_m=-m^2.
$$

Logo, módulo fluxo espectral inteiro,

$$
\boxed{
\bar\eta(A_m)
=\frac{\eta(0)+h}{2}
\equiv-\frac{m^2}{2}
\pmod{\mathbb Z}.
}
$$

Para o fluxo mínimo $|m|=1$,

$$
-\bar\eta(A_m)
\equiv\frac12
\pmod{\mathbb Z}.
$$

Isso corrige a condição anteriormente imposta

$$
-\frac12(\eta_a+h_a)=1.
$$

Um estômato com fluxo Hopf mínimo não produz sozinho uma contribuição inteira
apenas pelo termo de borda. O índice completo deve combinar

$$
\operatorname{ind}D^+
=
\int_{X_4}
\widehat A(TX_4)\operatorname{ch}(L_m)
-\bar\eta(A_m),
$$

de modo que a parte fracionária do bulk cancele a parte fracionária da borda.
Uma alternativa equivalente é a combinação física de dois canais conjugados.

O teste matricial reproduziu os níveis livres com erro nulo na precisão usada
e confirmou que a contagem finita de sinais depende do cutoff, razão pela qual
$\eta(0)$ não foi estimado por soma truncada.

Status atualizado:

$$
\boxed{
\text{parte fracionária de }\bar\eta\text{ calculada; resta obter o fluxo
espectral inteiro da torção GDQ e a integral de bulk complementar.}
$$

---

## 17. Atualização — sinal da torção e kernel do elo

A auto-adjunticidade euclidiana fixa o operador como

$$
D_B
=i\gamma^a
\left(
\nabla_a^{\rm LC}
+\frac18B_{abc}\gamma^{bc}
\right).
$$

Na orientação positiva de Cartan--Schouten,

$$
B_{abc}=\frac2a\varepsilon_{abc},
\qquad
\gamma^{123}=iI,
$$

e, portanto,

$$
i\gamma^a\frac18B_{abc}\gamma^{bc}
=-\frac{3}{2a}I.
$$

Assim, o sinal físico é

$$
\boxed{\beta=-\frac32}
$$

para a orientação escolhida. A orientação oposta troca o sinal e a
quiralidade.

O operador homogêneo torna-se

$$
D_{m,B}^{(j)}
=\frac1a
\left(
2\boldsymbol\sigma\cdot\boldsymbol L^{(j)}-m\sigma_3
\right).
$$

Seu kernel foi calculado explicitamente. Para $m\ne0$:

$$
j=\frac{|m|}{2},
\qquad
\boxed{h_m=|m|+1.}
$$

Em particular,

$$
\boxed{h_{+1}=h_{-1}=2.}
$$

Esses modos zero são consequência da torção paralelizante, não uma
degenerescência imposta. Resta combinar esse kernel e o $\eta$ de borda com a
densidade de índice do preenchimento 4D.

---

## 18. Atualização — preenchimento 4D e índice local unitário

Foram criados:

$$
\texttt{questoes/q28/associados/preenchimento\_aps\_u1.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_fluxo\_espectral\_u1.py}.
$$

Para o fluxo mínimo $|m|=1$, foi usado o preenchimento spin mínimo

$$
X_4=B^4,
$$

com

$$
\partial X_4\simeq S^3.
$$

A extensão radial $\mathcal A=f(r)A_m$, com $f(r)=O(r^2)$ na origem, é suave.
O preenchimento por $D(\mathcal O(-1))$ foi evitado porque ele exigiria a
fórmula spin$^c$ completa e seu determinante adicional.

A transgressão fornece

$$
\int_{X_4}\operatorname{ch}_2(L_m)
=\frac1{8\pi^2}\int_{X_4}\mathcal F\wedge\mathcal F
=-\frac{m^2}{2}.
$$

Antes da torção, a parte fracionária é cancelada por

$$
\bar\eta(A_m)=-\frac{m^2}{2},
$$

e o índice mínimo é zero.

Ao ligar

$$
\beta(t)=-\frac32t,
$$

o setor $m=1$ possui exatamente um cruzamento interior:

$$
\beta=-\frac12,
$$

com multiplicidade um e direção positivo--para--negativo. Portanto,

$$
\operatorname{SF}=-1.
$$

Na convenção APS usada,

$$
\Delta\operatorname{ind}_{\rm APS}=-\operatorname{SF},
$$

e segue

$$
\boxed{
\operatorname{ind}_{\rm APS}D_{1,B}^+=1.
}
$$

O teste numérico também confirmou o kernel final

$$
h_1=2.
$$

Assim, a unidade quiral local não foi imposta pelo termo de borda: ela resulta
da combinação entre fluxo Hopf mínimo, preenchimento 4D e fluxo espectral da
torção.

Status atualizado:

$$
\boxed{
\text{protótipo local }U(1)\text{ fechado com índice APS unitário.}
$$

Para obter três gerações, falta demonstrar que existem exatamente três
estômatos estáveis desta classe e elevar o cálculo aos fibrados $E_W$ e $E_C$.

---

## 19. Atualização — elevação equivarante a $SU(2)$ e $SU(3)$

Foram criados:

$$
\texttt{questoes/q28/associados/elevacao\_indice\_representacoes.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_elevacao\_representacoes.py}.
$$

O cálculo mostrou que a linha que produz a multiplicidade deve ser distinguida
da linha de hipercarga:

$$
\boxed{
L_G=\text{linha geométrica de índice},
\qquad
L_Y=\text{linha física de hipercarga}.
}
$$

Identificá-las faria o número de gerações depender do valor de $Y$. A linha
$L_G$ não introduz novo grupo de gauge: ela registra a topologia da fatia
normal do estômato.

Para uma representação $R$ topologicamente trivial no preenchimento local,

$$
\boxed{
\operatorname{Ind}_{G_{\rm gauge}}
(D_G^+\otimes V_R)
=\operatorname{ind}(D_G^+)[R]
=[R].
}
$$

Consequentemente,

$$
\operatorname{Ind}_{SU(2)}(D_G^+\otimes E_W)=[\mathbf2],
$$

$$
\operatorname{Ind}_{SU(3)}(D_G^+\otimes E_C)=[\mathbf3],
$$

e

$$
\operatorname{Ind}_{SU(3)\times SU(2)}
(D_G^+\otimes E_C\otimes E_W)
=[(\mathbf3,\mathbf2)].
$$

Os índices ordinários $2$, $3$ e $6$ contam componentes internas de um único
multiplet, não gerações adicionais.

Aplicado à classe física completa,

$$
\operatorname{Ind}_{G_{\rm gauge}}
(D_G^+\otimes\mathcal E_{\rm gen})
=\mathcal E_{\rm gen}.
$$

Para $N_G$ estômatos equivalentes,

$$
\operatorname{Ind}_{G_{\rm gauge}}
=N_G\mathcal E_{\rm gen}.
$$

O teste confirmou $15$ componentes de Weyl por índice local unitário e $45$
para $N_G=3$.

Status atualizado:

$$
\boxed{
\text{elevação do índice local às representações calculada; falta derivar
}N_G=3\text{ e construir o quociente global }\mathbb Z_6.
}

---

## 20. Atualização — quociente $\mathbb Z_6$ e hipercargas

Foram criados:

$$
\texttt{questoes/q28/associados/quociente\_z6\_hipercargas.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_hipercargas\_z6.py}.
$$

Com a normalização inteira

$$
y=6Y,
$$

o gerador central

$$
z_6
=
\left(
e^{2\pi i/3}I_3,
-I_2,
e^{i\pi/3}
\right)
$$

impõe a condição

$$
\boxed{
2t+3p+y\equiv0\pmod6,
}
$$

onde $t$ é a trialidade de cor e $p$ a paridade de isospin.

As congruências do quociente, combinadas com as quatro equações de anomalia,
fornecem

$$
\ell=-3q,
\qquad
u+d=-2q,
\qquad
e=6q,
\qquad
ud=-8q^2.
$$

Logo,

$$
\{u,d\}=\{2q,-4q\}.
$$

A normalização primitiva e a orientação $q\equiv1\pmod6$ fixam $q=1$:

$$
\boxed{
(q,u,d,\ell,e)
=(1,-4,2,-3,6),
}
$$

até a troca dos dois singletos de cor. Portanto,

$$
\boxed{
Y_Q=\frac16,
\quad
Y_{u^c}=-\frac23,
\quad
Y_{d^c}=\frac13,
\quad
Y_L=-\frac12,
\quad
Y_{e^c}=1.
}
$$

A busca diofantina em $|y_i|\leq30$ encontrou somente as duas soluções
relacionadas por $u\leftrightarrow d$.

O quociente não fixa sozinho os representantes inteiros: ele fixa classes
módulo seis. A unicidade vem da combinação entre quociente, anomalias e
primitividade.

Status atualizado:

$$
\boxed{
\text{hipercargas derivadas condicionalmente aos cinco tipos de
representação; falta derivar }N_G=3\text{ e as classes não abelianas.}
$$

---

## 21. Atualização — classes não abelianas mínimas

Foram criados:

$$
\texttt{questoes/q28/associados/classes\_naoabelianas\_prototipo.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_classes\_naoabelianas.py}.
$$

Colando dois preenchimentos ao longo do elo,

$$
S^4=B_N^4\cup_{S^3}B_S^4,
$$

um fibrado $SU(r)$ é classificado pela função de clutching

$$
g:S^3\to SU(r),
$$

com winding

$$
k(g)
=\frac1{24\pi^2}
\int_{S^3}\operatorname{tr}(g^{-1}dg)^3.
$$

Para a identificação canônica $S^3\simeq SU(2)$,

$$
k(g_2)=1,
$$

logo

$$
\boxed{c_2(E_W)[S^4]=1.}
$$

A inclusão

$$
SU(2)\hookrightarrow SU(3),
\qquad
g\mapsto\operatorname{diag}(g,1),
$$

preserva o gerador de $\pi_3$. Portanto,

$$
\boxed{c_2(E_C)[S^4]=1.}
$$

O teste numérico integrou o grau normalizado e obteve unidade para os dois
mapas, com erro nulo na precisão utilizada.

O terceiro número de Chern não pode ser medido nesse protótipo porque

$$
H^6(S^4,\mathbb Z)=0.
$$

Assim,

$$
c_3(E_C)[S^4]=0
$$

por dimensão, sem implicar $c_3(E_C)=0$ no background global. Sua avaliação
exige um 6-ciclo $\Sigma_6$ e a integral de $\operatorname{tr}(F_C^3)$.

Status atualizado:

$$
\boxed{
c_2(E_W)=c_2(E_C)=1\text{ no protótipo mínimo; faltam a seleção dinâmica
de }k=1,\ c_3\text{ global e }N_G=3.
}

---

## 22. Atualização — auditoria da contagem de três gerações

Foram criados:

$$
\texttt{questoes/q28/associados/auditoria\_tres\_geracoes.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_betti\_t5\_s3.py}.
$$

O teorema de Künneth fornece

$$
P_{T^5\times S^3}(t)
=(1+t)^5(1+t^3),
$$

e, portanto,

$$
\boxed{
(b_0,b_1,\ldots,b_8)
=(1,5,10,11,10,11,10,5,1).
}
$$

A característica de Euler é

$$
\chi(T^5\times S^3)=0.
$$

Esses invariantes não fornecem automaticamente três gerações. Além disso, os
números $h^{p,q}$ exigem uma estrutura complexa concreta e não são
determinados apenas pela topologia real do produto. Assim, a afirmação

$$
|h^{1,1}-h^{2,1}|=3
$$

fica retirada como prova enquanto esses grupos não forem calculados no
background Hermitiano efetivamente usado.

O resultado demonstrado é local:

$$
\operatorname{ind}_{\rm APS}D_{G,a}^+=1
$$

por estômato elementar orientado. Logo,

$$
\operatorname{Ind}_{G_{\rm gauge}}
=N_G\mathcal E_{\rm gen},
$$

mas o valor de $N_G$ precisa vir de um teorema global de estabilidade, índice,
Morse ou monodromia.

Status atualizado:

$$
\boxed{
\text{Q28 local calculada; a derivação de }N_G=3
\text{ permanece como principal pendência global.}
}

---

## 23. Atualização — aplicação precisa dos resultados de Perelman

Foi criado:

$$
\texttt{questoes/q28/associados/aplicacao\_perelman\_tres\_geracoes.md}.
$$

A monotonicidade de Perelman demonstra que, em cada setor admissível,

$$
\frac{d\mathcal W}{dt}\geq0,
$$

com igualdade somente num sóliton gradiente. Seus resultados sobre soluções
antigas, neckpinches e cirurgia fornecem a estabilidade e a seleção dos
limites geométricos.

Entretanto, “dimensão três” não significa “três componentes”. O artigo admite
vários necks e componentes possivelmente desconectados, sem fixar sua
cardinalidade.

O teorema condicional correto é:

$$
\boxed{
Q_G^{\rm total}=3
\quad\text{e}\quad
\operatorname{ind}_{\rm APS}D_{G,a}^+=1
\quad\Longrightarrow\quad
N_G=3,
}
$$

desde que o índice seja preservado pelo fluxo e pela cirurgia. Perelman
fornece a maquinaria de preservação/estabilidade; o valor inicial deve ser
calculado pelo operador global GDQ:

$$
Q_G^{\rm total}
=
\int_{M_{\rm global}}
\widehat A(TM)\operatorname{ch}(E_G)
-\sum_a\bar\eta_a.
$$

Status atualizado:

$$
\boxed{
\text{rota de Perelman fechada; falta somente a avaliação independente do
índice global inicial.}
}

---

## 24. Atualização — avaliação do índice global em $T^5\times S^3$

Foram criados:

$$
\texttt{questoes/q28/associados/indice\_global\_t5\_s3.md}
$$

e

$$
\texttt{questoes/q28/associados/test\_indice\_global\_t5\_s3.py}.
$$

Como $T^5$ e $S^3$ são paralelizáveis,

$$
\widehat A(T(T^5\times S^3))=1.
$$

Assim,

$$
\operatorname{Ind}D_{E_G}^+
=\int_{T^5\times S^3}\operatorname{ch}_4(E_G).
$$

Uma linha obtida por pullback simples possui

$$
\operatorname{ch}_4(L_G)=\frac{c_1(L_G)^4}{24}=0
$$

por dimensão. Portanto,

$$
\boxed{
\operatorname{Ind}D_{L_G}^+=0
}
$$

no produto global ingênuo.

O primeiro fibrado capaz de produzir índice não nulo possui uma classe mista

$$
c_2(E_G)=a_4+b_1\smile u_3,
$$

onde

$$
a_4\in H^4(T^5,\mathbb Z),
\qquad
b_1\in H^1(T^5,\mathbb Z),
\qquad
u_3\in H^3(S^3,\mathbb Z).
$$

Para um fibrado $SU(2)$,

$$
\operatorname{ch}_4(E_G)=\frac1{12}c_2(E_G)^2,
$$

e segue

$$
\boxed{
\operatorname{Ind}D_{E_G}^+
=\frac16
\left\langle
a_4\smile b_1,[T^5]
\right\rangle.
}
$$

Definindo

$$
N_{ab}
=\left\langle a_4\smile b_1,[T^5]\right\rangle,
$$

o índice três exige

$$
\boxed{N_{ab}=18.}
$$

O teste confirmou a sequência

$$
N_{ab}=0,6,12,18,24,30
\quad\Longrightarrow\quad
\operatorname{Ind}=0,1,2,3,4,5.
$$

Esse resultado não constitui ainda uma derivação de três gerações: escolher
$N_{ab}=18$ pelo alvo seria circular. A solução estacionária e a colagem
global da GDQ precisam produzir esse número característico.

Status atualizado:

$$
\boxed{
N_G=3
\Longleftrightarrow
\left\langle a_4\smile b_1,[T^5]\right\rangle=18.
}
$$

A pendência global foi reduzida à derivação independente desse emparelhamento.

## 25. Atualização — fibrado de Berry do kernel sobre $T^5$

No setor mínimo

$$
j=\frac12,
\qquad
m=1,
\qquad
\beta=-\frac32,
$$

o bloco interno do operador tangencial possui a matriz

$$
aD=
\begin{pmatrix}
0&0&0&0\\
0&-2&2&0\\
0&2&0&0\\
0&0&0&2
\end{pmatrix}.
$$

Seu kernel interno é gerado por

$$
v_0=
\begin{pmatrix}
1\\0\\0\\0
\end{pmatrix}.
$$

Como o bloco $j=1/2$ possui multiplicidade espectadora $2j+1=2$, os dois
autovetores completos que realizam $h_1=2$ são

$$
\boxed{
\psi_+=v_0\otimes r_+,
\qquad
\psi_-=v_0\otimes r_-.
}
$$

Introduzindo no primeiro ciclo toroidal a holonomia

$$
U_1(\theta_1)=e^{i\theta_1Q_1},
$$

a conexão de Berry no kernel é

$$
\mathcal A_1
=\Psi^\dagger\partial_{\theta_1}\Psi
=iQ_1.
$$

Para a generalização ordinária a $T^5$, tem-se

$$
U(\boldsymbol\theta)
=\exp\left(i\sum_{k=1}^5\theta_kQ_k\right).
$$

Uma representação unitária de

$$
\pi_1(T^5)=\mathbb Z^5
$$

exige geradores comutativos. Assim,

$$
[Q_i,Q_j]=0,
\qquad
\mathcal A=i\sum_{k=1}^5Q_kd\theta_k,
$$

e a curvatura calculada é

$$
\boxed{
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A=0.
}
$$

Consequentemente,

$$
\boxed{
c_2(E_G)
=-\frac{1}{8\pi^2}
\operatorname{tr}(\mathcal F\wedge\mathcal F)
=0.
}
$$

Como a cohomologia integral de $T^5$ não possui torção, não há neste caso
uma classe $c_2$ torsional invisível à curvatura. Na decomposição global,

$$
c_2(E_G)=a_4+b_1\smile u_3,
$$

isso fornece

$$
a_4=0,
\qquad
b_1=0,
$$

e portanto

$$
\boxed{
N_{ab}
=\left\langle a_4\smile b_1,[T^5]\right\rangle
=0.
}
$$

Esse resultado negativo é específico da família mínima, fatorizada e
abeliana. Ele não altera o índice APS local unitário: demonstra apenas que o
transporte plano dos dois modos pelo toro não produz o índice global de três
gerações.

Logo, a condição anteriormente encontrada,

$$
N_G=3
\Longleftrightarrow
N_{ab}=18,
$$

não pode ser satisfeita por holonomias toroidais ordinárias constantes. Para
obter $c_2(E_G)\ne0$, a conexão deve conter dependência genuinamente mista em
$T^5\times S^3$, por exemplo mediante uma colagem projetiva $\mathbb Z_6$, um
projetor espectral não constante ou uma Hessiana global não produto. A
colagem projetiva $\mathbb Z_6$ é a próxima rota natural, pois já foi derivada
na estrutura da Q28 e não deve ser introduzida como novo ajuste.

O cálculo analítico e sua verificação numérica estão documentados em
`questoes/q28/associados/berry_kernel_t5.md` e `questoes/q28/associados/test_berry_kernel_t5.py`.

## 26. Atualização — teste da colagem projetiva $\mathbb Z_6$

Uma representação projetiva dos ciclos toroidais pode satisfazer

$$
U_iU_j=\omega^{n_{ij}}U_jU_i,
\qquad
\omega=e^{2\pi i/6}.
$$

Para um cociclo primitivo, as matrizes relógio e deslocamento obedecem a

$$
CS=\omega SC.
$$

O teste matricial mostrou que sua representação irredutível mínima tem
dimensão seis. Em particular, o determinante da relação projetiva em dimensão
dois exigiria

$$
\omega^2=1,
$$

o que é falso para uma raiz sexta primitiva. Portanto, o cociclo $\mathbb
Z_6$ não age isoladamente no kernel local $h_1=2$. Ele deve agir no setor
completo

$$
\mathbb C^3\otimes\mathbb C^2,
$$

compatível com a estrutura conjunta de cor e isospin já obtida.

O cociclo define uma obstrução discreta em

$$
H^2(T^5,\mathbb Z_6),
$$

mas não determina sozinho uma classe integral $c_2$. A componente mista pode
ser construída sem ajuste por uma colagem

$$
g:S^3\longrightarrow SU(2)
$$

ao longo de um ciclo $S^1_5\subset T^5$. Seu grau é

$$
\nu(g)
=\frac{1}{24\pi^2}
\int_{S^3}\operatorname{tr}(g^{-1}dg)^3.
$$

Para o mapa identidade $S^3\simeq SU(2)$,

$$
\boxed{\nu(g)=1,}
$$

e

$$
b_1=e^5.
$$

Por outro lado, a componente toroidal de grau quatro requer curvatura em
dois planos independentes. Escrevendo

$$
\mathcal F_T
=2\pi i\left(
M_{12}e^1\wedge e^2+M_{34}e^3\wedge e^4
\right),
$$

obtém-se

$$
a_4=Ae^{1234},
\qquad
A=\operatorname{tr}(M_{12}M_{34}),
$$

com o sinal fixado pela orientação escolhida. Logo,

$$
\boxed{
N_{ab}=A\nu(g).
}
$$

Na colagem mínima,

$$
\nu(g)=1,
$$

portanto

$$
N_{ab}=A.
$$

O quociente $\mathbb Z_6$ restringe os fluxos admissíveis módulo seis, mas
não seleciona por si só o levantamento integral

$$
A=18.
$$

Assim, a colagem projetiva esclarece por que os setores $SU(3)$ e $SU(2)$
devem participar conjuntamente, mas ainda não constitui a derivação de três
gerações. O último dado necessário é calcular $M_{12}$ e $M_{34}$ a partir
do projetor espectral da Hessiana GDQ global, sem escolhê-los pelo valor-alvo.

O desenvolvimento e o teste estão em `questoes/q28/associados/colagem_projetiva_z6.md` e
`questoes/q28/associados/test_colagem_projetiva_z6.py`.

## 27. Atualização — pullback da Hessiana oficial no background produto

Para o projetor espectral $P$ dos modos zero, a curvatura de Berry admite a
expressão independente de base

$$
\mathcal F^{\rm B}=P\,dP\wedge dP\,P.
$$

No background estacionário produto

$$
T^5\times S^3,
$$

com métrica, dilatão e coeficientes da Hessiana independentes dos ângulos
toroidais, o operador quadrático oficial satisfaz

$$
[L_{\rm GDQ}^{(2)},-i\partial_{\theta_i}]=0.
$$

As autofunções se separam em modos de Fourier e o kernel geracional pertence
ao setor de momento toroidal nulo. Portanto,

$$
P(\boldsymbol\theta)=P_0,
\qquad
d_{T^5}P=0.
$$

Segue diretamente:

$$
\boxed{
\mathcal F_T^{\rm B}=0,
\qquad
M_{12}=M_{34}=0.
}
$$

Logo,

$$
\boxed{
A=\operatorname{tr}(M_{12}M_{34})=0,
\qquad
N_{ab}=0.
}
$$

Holonomias constantes podem deslocar os momentos segundo

$$
k_i\mapsto k_i+Q_i,
$$

mas não alteram essa conclusão, pois o projetor continua localmente constante.
O teste numérico encontrou variação máxima do projetor igual a

$$
3{,}14\times10^{-16}
$$

e curvatura nula na precisão de máquina.

Assim, o background produto não pode gerar três gerações pela curvatura de
Berry. Para obter $A\ne0$, a solução estacionária global deve possuir termos
mistos que façam

$$
\partial_{\theta_i}P\ne0.
$$

Quando um background não produto for especificado, essas derivadas poderão
ser calculadas diretamente por

$$
\partial_iP
=-R_\perp(\partial_iL)P
-P(\partial_iL)R_\perp,
$$

onde

$$
R_\perp=(1-P)(L-\lambda)^{-1}(1-P).
$$

Esse resultado está documentado em `questoes/q28/associados/pullback_hessiana_global.md` e
`questoes/q28/associados/test_pullback_hessiana_global.py`.

## 28. Atualização — conexão não produto derivada da ação oficial

Para evitar acrescentar uma teoria externa, a conexão foi introduzida como
componente fora da diagonal da própria métrica global. Considere a fibração

$$
S^3\simeq SU(2)
\longrightarrow K_8
\longrightarrow T^5
$$

e as formas

$$
\eta^a
=\sigma^a+A_i^{\ a}(\theta)d\theta^i.
$$

O ansatz métrico é

$$
ds_K^2
=G_{ij}d\theta^id\theta^j
+r^2\delta_{ab}\eta^a\eta^b.
$$

A conexão $A_i^{\ a}$ não é um campo fundamental acrescentado: ela pertence
à métrica que entra em $\mathcal R$ na ação oficial. A decomposição geométrica
do escalar de curvatura contém

$$
\mathcal R_K
=\mathcal R_{T^5}
+\frac{6}{r^2}
-\frac{r^2}{4}F^a_{ij}F_a^{ij}
+\mathcal R_{\rm mod}.
$$

Variando a ação oficial em relação às componentes mistas da métrica,
obtém-se

$$
\boxed{
D_i\left(r^5\mathcal U_BF^{ij}\right)=0.
}
$$

No background homogêneo, essa equação admite conexões de curvatura
covariantemente constante. Sua classe é

$$
a_4
=-\frac{1}{8\pi^2}
\operatorname{tr}(F_T\wedge F_T)
=Ae^{1234}.
$$

Com a colagem mínima previamente calculada,

$$
\nu(g)=1,
$$

segue

$$
\boxed{
N_{ab}=A,
\qquad
N_G=\frac{A}{6}.
}
$$

O setor que produz três gerações é unicamente

$$
\boxed{A=18}
$$

entre os setores orientados compatíveis com a quantização em múltiplos de
seis.

Entretanto, $A$ é um número topológico conservado. A variação local da ação
determina a conexão estacionária dentro de cada setor, mas não conecta setores
com valores distintos de $A$. A seleção correta deve ser formulada como

$$
A_*
=\operatorname*{argmin}_{A\in\mathcal A_{\mathbb Z_6}}
\mathcal S_{\rm GDQ}^{\rm on\mbox{-}shell}(A),
$$

com as condições globais de colagem, regularidade e orientação incluídas na
definição de $\mathcal A_{\mathbb Z_6}$.

Assim, a ação oficial já fornece a dinâmica da conexão e torna possível
$c_2\ne0$. A pendência final da contagem geracional é demonstrar que as
condições globais da GDQ selecionam $A=18$, em vez de simplesmente assumi-lo.

A derivação está em `questoes/q28/associados/fibracao_su2_acao_oficial.md`; o teste dos setores
está em `questoes/q28/associados/test_setores_acao_oficial.py`.

## 29. Atualização — comparação da ação on-shell entre setores

No setor homogêneo, a forma quadrática fisicamente estável induzida pela
curvatura da métrica é

$$
I_A
=C_{\rm GDQ}
\int_{T^4}w\operatorname{tr}(F\wedge *_4F),
\qquad
C_{\rm GDQ}>0,
\qquad
w=r^5\mathcal U_B>0.
$$

O limite topológico fornece

$$
I_A
\ge
8\pi^2C_{\rm GDQ}w|A|,
$$

com igualdade para uma conexão auto-dual ou anti-auto-dual. Portanto,

$$
\boxed{
I_A^{\rm on\mbox{-}shell}
=8\pi^2C_{\rm GDQ}w|A|.
}
$$

Nos setores orientados permitidos em múltiplos de seis, a sequência é

$$
A=0,6,12,18,24,\ldots
$$

e a ação cresce monotonicamente. Assim,

$$
\boxed{
A_{\rm mínimo}=0.
}
$$

Se uma condição global excluir o setor trivial, o primeiro mínimo é

$$
\boxed{
A_{\rm mínimo\ não\ trivial}=6,
\qquad
N_G=1.
}
$$

Logo, a aproximação homogênea da ação oficial não seleciona $A=18$. A relação

$$
N_G=\frac{A}{6}
$$

continua válida, mas a cardinalidade três requer um mecanismo adicional já
pertencente à geometria global: retroação dos módulos, três componentes
topológicas obrigatórias, uma condição de regularidade que exclua os setores
inferiores ou uma carga global inicial conservada.

O teste preditivo correto passa a ser resolver simultaneamente

$$
D_i\left(r^5\mathcal U_BF^{ij}\right)=0,
$$

$$
\frac{\delta\mathcal S_{\rm GDQ}}{\delta r}=0,
\qquad
\frac{\delta\mathcal S_{\rm GDQ}}{\delta G_{ij}}=0,
\qquad
\frac{\delta\mathcal S_{\rm GDQ}}{\delta f}=0,
$$

e avaliar

$$
I_{\rm eff}(A)
=\mathcal S_{\rm GDQ}[A,r_A,G_A,f_A].
$$

O fechamento por retroação exigiria um mínimo estável em $A=18$; a rota por
condição global exigiria demonstrar independentemente que somente esse setor
é admissível.

Os detalhes estão em `questoes/q28/associados/acao_onshell_setores.md` e
`questoes/q28/associados/test_acao_onshell_setores.py`.

## 30. Atualização — retroação radial e normalização de $\mathcal U$

A normalização oficial

$$
\int_K\mathcal U,dV_g=1
$$

implica, para a fibra $S^3$ homogênea,

$$
\sigma(r)=\sigma_0+3\log r.
$$

Incluindo essa dependência e a curvatura da conexão métrica, o funcional
radial reduzido é

$$
W_-(r,A)
=\tau\left(
\frac6{r^2}-q|A|r^2
\right)
+3\log r+C_0,
$$

onde o sinal negativo é o da decomposição geométrica do escalar de curvatura.
A equação estacionária, com $x=r^2$, torna-se

$$
\boxed{
2q\tau|A|x^2-3x+12\tau=0.
}
$$

Ela possui soluções reais somente quando

$$
|A|
\le
\frac{3}{32q\tau^2}.
$$

Esse limite depende dos módulos e não distingue universalmente $A=18$.

O teorema do envelope fornece diretamente

$$
\boxed{
\frac{dW_-^{\rm on\mbox{-}shell}}{d|A|}
=-q\tau r_A^2<0.
}
$$

Como controle da convenção euclidiana positiva, para

$$
W_+(r,A)
=\tau\left(
\frac6{r^2}+q|A|r^2
\right)
+3\log r+C_0,
$$

obtém-se

$$
\boxed{
\frac{dW_+^{\rm on\mbox{-}shell}}{d|A|}
=q\tau r_A^2>0.
}
$$

Portanto, em uma convenção a ação decresce até um limite de existência; na
outra, cresce e escolhe o menor setor. Nenhuma possui um mínimo interior em

$$
A=18.
$$

Conclui-se que a retroação do raio e a normalização do dilatão, embora
necessárias, não derivam três gerações. O próximo setor não trivial é a
retroação anisotrópica de $G_{ij}$ e a correlação não homogênea entre $f$ e a
densidade de Chern; alternativamente, $A=18$ deve ser fixado por uma condição
global conservada independentemente derivada.

O cálculo e sua verificação estão em `questoes/q28/associados/retroacao_modulo_radial.md` e
`questoes/q28/associados/test_retroacao_modulo_radial.py`.

## 31. Atualização — retroação anisotrópica de $T^5$

Considere fluxos quantizados nos planos $(12)$ e $(34)$:

$$
\frac1{2\pi}\int_{T^2_{12}}F=n_{12},
\qquad
\frac1{2\pi}\int_{T^2_{34}}F=n_{34}.
$$

Com

$$
x=\frac{L_3L_4}{L_1L_2},
$$

a dependência da forma quadrática da ação oficial nos módulos anisotrópicos é

$$
E(x)
=C\left(
n_{12}^2x+rac{n_{34}^2}{x}
\right).
$$

A variação fornece

$$
\boxed{
x_*
=\left|\frac{n_{34}}{n_{12}}\right|,
}
$$

que é a condição auto-dual ou anti-auto-dual dos fluxos. A Hessiana nessa
direção é positiva. Contudo, a ação on-shell fica

$$
\boxed{
E_{\rm on\mbox{-}shell}
=2C|n_{12}n_{34}|
=\frac{2C}{|\kappa_R|}|A|.
}
$$

Assim, a anisotropia estabiliza a forma do toro, mas conserva a monotonicidade
em $|A|$ e não produz um mínimo em $A=18$.

Para um dilatão não homogêneo com peso positivo

$$
w(\theta)=r^5\mathcal U_B(\theta),
$$

vale ainda

$$
\int_{T^4}w\operatorname{tr}(F\wedge *_4F)
\ge
8\pi^2w_{\min}|A|.
$$

Um peso fixo pode localizar a densidade de Chern, mas não inverter a
monotonicidade. A última possibilidade variacional contínua é uma solução
acoplada na qual o próprio perfil $w_A$ dependa do setor topológico.

O cálculo está em `questoes/q28/associados/retroacao_anisotropica_t5.md` e
`questoes/q28/associados/test_retroacao_anisotropica_t5.py`.

## 32. Atualização — retroação completa do dilatão e da medida

No setor real normalizado, o funcional oficial possui a forma

$$
\mathcal W[g,f]
=\int_K\rho
\left[
\tau\left(\mathcal R+|\nabla f|^2\right)+f-n
\right],
\qquad
\int_K\rho=1.
$$

Para a métrica fibrada,

$$
\mathcal R
=\mathcal R_0-\frac{r^2}{4}|F|^2.
$$

A equação estacionária do dilatão é

$$
\boxed{
2\tau\Delta f
-\tau|\nabla f|^2
+\tau\mathcal R
+f-n
=\mu.
}
$$

Ela mostra que $f_A$ e $\rho_A$ respondem à distribuição espacial de
$|F_A|^2$. Para uma família homotética,

$$
|F_A(y)|^2=|A|q(y),
\qquad
q(y)\ge0,
$$

o teorema do envelope fornece, depois de extremizar todas as variáveis
contínuas,

$$
\boxed{
\frac{d\mathcal W_{\rm eff}}{d|A|}
=-\frac{\tau}{4}
\int_K\rho_A r_A^2q(y)<0.
}
$$

Na convenção de forma quadrática euclidiana positiva, o sinal é invertido,
mas continua definido:

$$
\boxed{
\frac{d\mathcal W_{\rm eff}^{(+)}}{d|A|}
=+\frac{\tau}{4}
\int_K\rho_A r_A^2q(y)>0.
}
$$

Como

$$
\rho_A>0,
\qquad
r_A^2>0,
\qquad
q(y)\ge0,
$$

a redistribuição da medida pode modificar a magnitude da resposta, mas não
seu sinal. O teste numérico entrópico confirmou essa identidade para os
setores $A=6,12,18,24$.

Portanto,

$$
\boxed{
\text{a retroação contínua de }f,\mathcal U,r,G
\text{ não seleciona }A=18
}
$$

na família suave considerada. A única rota restante é uma mudança global
descontínua do domínio — colagem, cirurgia, número de componentes ou condição
de contorno — que fixe o setor topológico antes da evolução. A ação oficial
então preserva e governa esse setor, mas não transforma continuamente um
inteiro topológico em outro.

O resultado está em `questoes/q28/associados/retroacao_dilatao_cern.md` e
`questoes/q28/associados/test_retroacao_dilatao_cern.py`.

## 33. Formulação final — separação local-global

Os cálculos anteriores mostram que a tensão responsável pela carga
geracional não deve ser tratada como uma variável local que a ação minimiza
entre setores. A formulação correta separa:

$$
\mathfrak B_{\rm global}
=\left(
K_8,[g]_{\partial},[\mathcal U]_{\partial},
\Gamma_{\mathbb Z_6},A
\right),
$$

que fixa o setor cosmológico, e

$$
(g_A,f_A,\mathcal U_A,F_A)
=\operatorname*{Crit}_{\mathfrak B_{\rm global}}
\mathcal S_{\rm GDQ},
$$

que determina sua realização local. Nas variações locais,

$$
\delta A=0,
$$

pois $A$ é uma classe característica conservada.

O resultado consolidado da Q28 é o teorema condicional

$$
\boxed{
N_G
=\frac{A\nu(g)}6.
}
$$

Como a colagem mínima forneceu

$$
\nu(g)=1,
$$

segue

$$
\boxed{
N_G=\frac A6,
\qquad
N_G=3\Longleftrightarrow A=18.
}
$$

Assim, o setor local — kernel, índice APS, quociente $\mathbb Z_6$,
representações, hipercargas e transmissão da carga global — está fechado. A
seleção de $A=18$ é uma questão cosmológica de contorno e não deve continuar
sendo buscada pela minimização local.

Para evitar circularidade, ficam encerradas as rotas por holonomia constante,
background produto, raio homogêneo, anisotropia homogênea e redistribuição
suave de $f$. O único próximo cálculo legítimo é obter

$$
A[\mathfrak B_{\rm cosmológico}]
$$

a partir da tensão global e das condições causais do espaço de Einstein.

A convenção completa de trabalho está em
`questoes/q28/associados/formulacao_global_tensao.md`.

## 34. Cálculo da tensão global no background cosmológico isotrópico

No espaço cosmológico

$$
M_{\rm cos}=T^5\times S^3,
$$

a classe toroidal geral é

$$
a_4
=\sum_{i=1}^{5}A_i\,\iota_i
(e^1\smile e^2\smile e^3\smile e^4\smile e^5).
$$

Por dualidade de Poincaré, os coeficientes formam um vetor integral axial em
$\mathbb Z^5$. A isotropia integral orientada contém inversões simultâneas de
quaisquer dois ciclos. A invariância da classe sob essas transformações impõe

$$
A_i=-A_i
$$

para cada componente e, portanto,

$$
\boxed{
a_4=0,
\qquad
A=0.
}
$$

Como $\nu(g)=1$, segue

$$
\boxed{
N_G=\frac{A\nu(g)}6=0
}
$$

no background homogêneo, isotrópico e suave. Esse resultado demonstra que a
tensão escalar cosmológica, embora possa ser não nula, não pode ser
identificada diretamente com a carga característica orientada $A$.

O background físico, entretanto, distingue o ciclo térmico:

$$
T^5=T^4_{\rm int}\times S^1_\beta.
$$

Sob a isotropia residual de $T^4$, sobrevive exatamente

$$
H^4(T^5,\mathbb Z)^{G_{T^4}}
=\mathbb Z\,\operatorname{PD}(e^5),
$$

e a classe admissível é

$$
a_4=A\,\operatorname{PD}(e^5),
\qquad
A\in\mathbb Z.
$$

A condição térmica escolhe a direção e quantiza a carga, mas a magnitude de
$A$ ainda deve ser obtida por uma identidade global independente, condição
inicial ou cirurgia de multiplicidade calculável, sem usar o número observado
de gerações.

O cálculo e seu teste exato estão em
`questoes/q28/associados/tensao_global_cosmologica.md` e
`questoes/q28/associados/test_isotropia_global.py`.

## 35. Seleção aritmética e setor primitivo

A integralidade do índice global impõe

$$
\frac A6\in\mathbb Z.
$$

Assim,

$$
\boxed{
A=6k,
\qquad
N_G=k,
\qquad
k\in\mathbb Z.
}
$$

O setor positivo primitivo da sub-rede admissível é

$$
\boxed{
A_{\rm prim}=6,
\qquad
N_G=1.
}
$$

Consequentemente, $A=18$ não decorre da primitividade da colagem
$\mathbb Z_6$; ele equivale a uma multiplicidade global independente $k=3$.
Para fechar a contagem sem circularidade, deve-se construir uma seção global
derivada do background GDQ e demonstrar que seu número de interseção, soma de
resíduos ou multiplicidade de zeros vale três.

O cálculo está em `questoes/q28/associados/selecao_aritmetica_carga_global.md` e é verificado por
`questoes/q28/associados/test_selecao_aritmetica.py`.

## 36. Auditoria das identidades de localização

As localizações naturais no background fechado foram avaliadas. Como

$$
\chi(T^5\times S^3)=0,
$$

Poincaré--Hopf fornece soma assinada de índices igual a zero. A periodicidade
em $S^1_\beta$ também possui índice total zero, e o teorema global dos
resíduos exige soma de resíduos nula numa compactificação sem bordo.

Além disso, uma família suave de conexões preserva $c_2$ e, portanto,

$$
\Delta k_{\rm suave}=0.
$$

Perelman controla o fluxo e a cirurgia em dimensão três, mas não transforma a
dimensão da variedade em três unidades de carga. A alegação histórica de
“três classes de Perelman” não fornece a multiplicidade geracional.

A única rota ainda admissível é relativa. Para um cobordismo cosmológico
$W_9$ entre duas fatias, com operador tangencial $D_\tau$,

$$
\boxed{
k_+-k_-
=\operatorname{SF}(D_\tau)
=\operatorname{Ind}_{\rm APS}(\mathscr D_{W_9}).
}
$$

Partindo de $k_-=0$, o fechamento requer calcular

$$
\operatorname{SF}(D_\tau)=3
$$

a partir do background e das cirurgias, sem impor três cruzamentos. O próximo
objeto necessário é, portanto, o cobordismo $W_9$, seu operador tangencial e
as condições APS nas duas extremidades.

A auditoria completa está em `questoes/q28/associados/auditoria_localizacao_k3.md`, com teste em
`questoes/q28/associados/test_localizacao_k3.py`.

## 37. Auditoria das rotas orbifold, trialidade e $\mathbb CP^2$

Foram avaliadas três propostas para produzir o fluxo espectral três.

O $\mathbb Z_6$ atualmente derivado é um cociclo projetivo nas fibras e não
uma ação no espaço-base. Portanto, ele não define pontos fixos geométricos
para aplicação imediata do índice de Kawasaki. Mesmo numa ação canônica de
$\mathbb Z_3$ sobre um toro de Eisenstein, a contagem diagonal é

$$
N_{\rm fix}=3^d,
$$

onde $d$ é a dimensão complexa afetada. Além disso, cada componente fixa tem
uma contribuição dependente dos pesos de isotropia; ela não vale
automaticamente um.

A trialidade de $\operatorname{Spin}(8)$ permite uma órbita entre
$8_v,8_s,8_c$, mas não é automaticamente simetria do background Hermitiano
nem obriga três cruzamentos assinados. A rota de $\mathbb CP^2$ também não
fecha: $\chi(\mathbb CP^2)=3$ não é o índice de Dirac, e $\mathbb CP^2$ exige
estrutura $\operatorname{spin}^c$.

Assim,

$$
\boxed{
\mathbb Z_3\subset\mathbb Z_6
\not\Rightarrow
\operatorname{SF}(D_\tau)=3.
}
$$

A rota orbifold só poderá prosseguir se a GDQ exigir independentemente uma
extensão

$$
\varphi:\mathbb Z_6\to\operatorname{Diff}(T^5\times S^3)
$$

compatível com a estrutura cosmológica. Nos documentos atuais, o grupo age
somente na fibra; promover essa ação à base é hipótese nova, não consequência
da Q28.

A análise completa está em `questoes/q28/associados/auditoria_rotas_cobordismo_w9.md`, com o teste
de pontos fixos em `questoes/q28/associados/test_pontos_fixos_z3.py`.

## 38. Cirurgia condicional de três estômatos

Foi construída uma cirurgia transversal com três bolas disjuntas
$B^4_a\subset X_4$, cujas bordas são $Y_a\simeq S^3$. A fórmula de colagem
APS fornece

$$
\operatorname{Ind}D^+_{X_4}
=\operatorname{Ind}D^+_{X_4^\circ}
+\sum_{a=1}^{3}
\operatorname{ind}_{\rm APS}D^+_{B^4_a}
+\mu_{\rm glue}.
$$

Se o complemento não transportar índice adicional, a correção de colagem for
nula e os três fluxos mínimos possuírem a mesma orientação, então

$$
\boxed{
\operatorname{Ind}D^+_{X_4}=1+1+1=3.
}
$$

Como cada unidade primitiva corresponde a carga global seis,

$$
\boxed{
A_{\rm total}=6+6+6=18,
\qquad
N_G=3.
}
$$

Essa construção demonstra rigorosamente a implicação

$$
\text{três estômatos primitivos, independentes e coorientados}
\Longrightarrow
N_G=3.
$$

Ela não deriva ainda a existência cosmológica de exatamente três defeitos.
Se essa topologia for aceita como condição ambiental inicial, porém, $A=18$
deixa de ser colocado diretamente e passa a ser consequência da aditividade
dos três índices locais calculados.

Os overlaps dos modos fornecem matrizes $3\times3$, mas CKM e PMNS exigem os
desalinhamentos

$$
V_{\rm CKM}=U_u^\dagger U_d,
\qquad
U_{\rm PMNS}=U_e^\dagger U_\nu.
$$

Seus valores e a hierarquia de massas ainda dependem da solução do background
de três centros e da Hessiana oficial.

A derivação completa está em `questoes/q28/associados/cirurgia_tres_estomatos.md`, com teste em
`questoes/q28/associados/test_cirurgia_tres_estomatos.py`.

## 39. Seleção local do número de estômatos por equilíbrio torsional

Escrevendo $f=u+iv$, a ação oficial é invariante sob o deslocamento constante
de $v$. A identidade de Noether correspondente fornece conservação da
corrente de fase e, numa região de junction,

$$
\sum_{a=1}^{N}\mathbf T_a=0.
$$

Na fibração de Hopf, as tensões relativas vivem na distribuição horizontal

$$
\mathcal H=\ker\eta_H,
\qquad
\operatorname{rank}_{\mathbb R}\mathcal H=2.
$$

Para canais isotrópicos, o pullback universal da Hessiana ao modo de
fechamento é

$$
\mathcal E_{\rm close}
=\frac{\kappa_H}{2}
\left|\sum_a\mathbf T_a\right|^2.
$$

$N=1$ não fecha e $N=2$ é colinear. Para $N=3$, as direções ficam separadas
por $120^\circ$ e a Hessiana angular possui espectro

$$
\boxed{
\operatorname{spec}H
=\kappa_HT^2
\left\{0,\frac32,\frac32\right\}.
}
$$

O único zero é a rotação global. Para $N>3$, como $\operatorname{rank}H\le2$,
restam pelo menos $N-3$ modos zero internos depois de removida a rotação.
Logo, dentro do ansatz elementar, isotrópico e horizontal,

$$
\boxed{N=3}
$$

é o único junction não colinear e isolado pela Hessiana reduzida.

Com a cirurgia APS,

$$
N=3
\Longrightarrow
\operatorname{Ind}=3
\Longrightarrow
A=18
\Longrightarrow
N_G=3.
$$

No próton, as direções mecânicas fecham a $120^\circ$, embora as circulações
escalares sejam coorientadas. No nêutron, a compensação escalar mínima pode
ser $(1,1,-2)$. Esses dois balanços não devem ser confundidos.

O teorema ainda é reduzido: falta verificar os modos radiais e tensoriais da
Hessiana completa, o índice nulo do complemento e o transporte independente
das três classes ao fibrado global. A derivação está em
`questoes/q28/associados/selecao_torcional_tres_estomatos.md`, com teste em
`questoes/q28/associados/test_selecao_torcional_tres.py`.

## 40. Critério da Hessiana completa

A orientação global homogênea de Hopf é isometria e possui rigidez zero. A
rigidez relevante para a seleção local deve ser a textura relativa do
background multicítrico, $\kappa_{\rm rel}$.

Após fixação de DeTurck e remoção dos modos de gauge, a Hessiana completa tem
a forma

$$
\mathbb H^{(3)}
=\begin{pmatrix}
H_{\rm rel}&J\\
J^\dagger&K_\perp
\end{pmatrix},
\qquad
H_{\rm rel}=\frac32\kappa_{\rm rel}T^2I_2.
$$

Se $K_\perp>0$, a estabilidade integral equivale a

$$
\boxed{
H_{\rm rel}-JK_\perp^{-1}J^\dagger>0.
}
$$

Uma condição suficiente é

$$
\boxed{
\frac{\|J\|^2}{\lambda_\perp}
<\frac32\kappa_{\rm rel}T^2,
\qquad
K_\perp\ge\lambda_\perp I>0.
}
$$

O modo radial homogêneo já satisfaz

$$
\lambda_{r,0}=\frac{3}{2\tau}>0.
$$

Entretanto, os documentos atuais ainda não fornecem $\kappa_{\rm rel}$,
$\lambda_\perp$ e $J$ no background estacionário de três centros. Assim,
$N=3$ está selecionado na Hessiana horizontal reduzida, mas sua estabilidade
integral e a exclusão de mínimos $N>3$ permanecem condicionadas ao cálculo do
background multicítrico.

O critério completo está em
`questoes/q28/associados/estabilidade_completa_junction_torcional.md`, com verificação algébrica
em `questoes/q28/associados/test_criterio_schur_junction.py`.

## 41. Simulação específica da seleção de três estômatos

Foi criado um solver independente do antigo código trimodal. Para cada
$N=2,\ldots,8$, ele parte de 64 configurações angulares aleatórias e minimiza

$$
\mathcal E_{\rm close}
=\frac12\left|\sum_a\mathbf T_a\right|^2.
$$

Para $N=3$, sem inicializar o triângulo, a solução encontrada foi

$$
(0^\circ,120^\circ,240^\circ)
$$

com

$$
\operatorname{spec}H_3
=\{0,1{,}5,1{,}5\}.
$$

Para $N>3$, a execução encontrou exatamente $N-3$ modos zero internos após a
remoção da rotação global. Assim, o resultado numérico confirma

$$
\boxed{
N=3
\text{ como único junction não colinear, fechado e isolado no modelo
horizontal reduzido.}
}
$$

O solver e a saída estão em
`numerico/q28_tres_estomatos/solve_selection_q28.py` e
`numerico/q28_tres_estomatos/saida_selection_q28.md`. A classificação é teste
do teorema reduzido; a prova integral ainda exige avaliar o complemento de
Schur no background GDQ multicítrico.

## 42. Fechamento consolidado

A simulação confirma o resultado algébrico sem inserir o número três. A
condição de elementaridade não afirma que toda solução com $N>3$ seja
impossível; afirma que tais configurações possuem módulos internos e,
portanto, são estados compostos ou famílias não isoladas no funcional
universal. O primeiro junction horizontal fechado, não colinear e isolado é
necessariamente o triângulo de tensões.

Com três estômatos primitivos coorientados,

$$
N=3
\Longrightarrow
\operatorname{Ind}_{\rm APS}=3
\Longrightarrow
A=18
\Longrightarrow
\boxed{N_G=3}.
$$

Assim, a contagem geracional da Q28 fica encerrada no modelo horizontal
reduzido. A avaliação de $\kappa_{\rm rel}$, $K_\perp$ e $J$ no background
completo é necessária para demonstrar que a solução pertence à dinâmica
integral da ação oficial. O relatório autocontido do resultado reduzido está em
`questoes/q28/associados/fechamento_selecao_tres_estomatos.md`.

## 43. Auditoria da Hessiana física de três centros

A ação oficial fixa os operadores diferenciais do bulk, mas, no domínio
excisado por três estômatos, sua segunda variação contém uma forma de Green em
cada $S^3$. O texto oficial ainda não fornece o funcional de bordo, os dados
de Dirichlet ou a aplicação Dirichlet--to--Neumann interior que selecionaria a
extensão auto-adjunta.

A conservação também deve permanecer dentro da variação. Com

$$
\mathcal C(\Phi)=\sum_{a=1}^{3}\mathbf T_a[\Phi],
$$

o background é extremo de

$$
\widetilde{\mathcal S}
=\mathcal S_{\rm GDQ}
+\boldsymbol\lambda\cdot\mathcal C,
$$

e a Hessiana física é

$$
\mathbb H_{\rm cons}
=\left.
\left(
\mathbb H_{\rm GDQ}
+\lambda_ID^2\mathcal C_I
\right)
\right|_{\ker D\mathcal C_*}.
$$

O multiplicador comum correlaciona as três condições de bordo. Omiti-lo
produziria uma Hessiana de três centros fisicamente incorreta.

Por isso, os objetos físicos

$$
\kappa_{\rm rel},
\qquad
K_\perp,
\qquad
J
$$

não têm valores únicos com os dados atuais. O numérico já fixa a parte
adimensional

$$
H_{\rm rel}/(\kappa_{\rm rel}T^2)
=\frac32I_2,
$$

mas não fixa a impedância dos estômatos. A rota intrínseca mínima é resolver o
interior de cada núcleo e calcular

$$
\mathsf R_a=-\operatorname{DN}_{\mathcal N_a}.
$$

Só então a Hessiana esparsa completa e seu complemento de Schur ficam
univocamente definidos. A demonstração está em
`questoes/q28/associados/hessiana_background_tres_centros.md`.

## 44. Hessiana vinculada do setor multicítrico simétrico

Tratando os estômatos como interfaces internas de cirurgia, e não como bordas
Robin externas, o vínculo de Noether determina a Hessiana coletiva. No setor
de fluxo primitivo normalizado,

$$
H_{\rm rel}=\frac32I_2,
\qquad
K_\perp^{(r,0)}=\frac{3}{2\tau}I_3,
\qquad
J_{\theta r}=0.
$$

Portanto,

$$
\operatorname{spec}H_{\rm eff}=\{3/2,3/2\}>0.
$$

O cálculo e seu teste estão em
`questoes/q28/associados/hessiana_vinculada_tres_centros_final.md` e
`questoes/q28/associados/test_hessiana_vinculada_tres_centros.py`.

## 45. Modos não homogêneos e fechamento espectral

No preenchimento gaussiano de cada fatia normal $\mathbb C^2$, o operador
ponderado possui espectro

$$
\operatorname{spec}(-\Delta_f)
=\left\{\frac{m}{2\tau}:m=0,1,2,\ldots\right\}.
$$

Depois de impor a normalização da medida, eliminar a resposta dilatônica,
fixar o gauge Hermitiano--DeTurck e remover as simetrias globais, todos os
setores não homogêneos começam em

$$
\lambda_{\rm nh}=\frac1{2\tau}>0.
$$

Juntando-os aos modos coletivos,

$$
\mathbb H_{\rm phys}^{(3)}
=H_{\rm rel}\oplus K_r^{(0)}
\oplus K_v^{\rm phys}\oplus K_{(g,f)}^{\rm HD,phys},
$$

e

$$
\lambda_{\min}
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0.
$$

Na normalização do solver e em $\tau=1$, o gap mínimo é $1/2$. A derivação e
o teste estão em `questoes/q28/associados/hessiana_espectral_completa_background_c3.md` e
`questoes/q28/associados/espectro_completo_hessiana_tres_centros.py`.

## 46. Acoplamentos por normas internas

Os índices quadráticos do espectro de uma geração são

$$
I_3=2,
\qquad
I_2=2,
\qquad
I_Y=\frac{10}{3}.
$$

Como $1/g_a^2$ é proporcional à norma $I_a$ no mesmo background,

$$
g_s=g,
\qquad
\frac{g'^2}{g^2}=\frac35,
\qquad
\sin^2\theta_W=\frac38.
$$

Com $e^2=4\pi\alpha$ e $\alpha^{-1}=137{,}03599907$,

$$
g_s^{\rm match}=g=0{,}494506,
\qquad
g'=0{,}383043.
$$

Na escala hadrônica, o resultado independente da Q30 fornece

$$
g_s^{\rm had}=\sqrt{\frac32}=1{,}224745.
$$

A derivação e a verificação numérica estão em
`questoes/q28/associados/acoplamentos_geometricos_finais.md` e
`questoes/q28/associados/calcular_acoplamentos_q28.py`.

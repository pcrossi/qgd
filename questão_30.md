# Questão 30 — Como confinamento e mass gap são demonstrados?

## 1. Status

A Questão 30 não está fechada como demonstração matemática completa do problema
de Yang-Mills/mass gap.

O texto original fornece uma rota geométrica plausível dentro da GDQ:

1. vorticidade/torsão como origem efetiva da carga de cor;
2. formação de tubo de fluxo;
3. crescimento linear da energia;
4. gap espectral associado a modos transversais ou a um operador elíptico com
   curvatura efetiva positiva.

Mas, para responder à auditoria, isso ainda não basta. A formulação atual ainda
faz uma passagem frágil:

\[
\text{área transversal finita}
\quad+\quad
\text{densidade de energia constante}
\quad\Longrightarrow\quad
V(r)=\sigma r.
\]

Essa conclusão é fisicamente coerente, mas não é uma derivação rigorosa da lei
de área nem do mass gap de Yang-Mills.

Portanto:

\[
\boxed{
\text{a Questão 30 está estruturalmente formulada, mas não fechada como
teorema completo.}
}
\]

---

## 2. Divergência de numeração

O arquivo `30-0.md` pergunta sobre:

\[
\text{confinamento e mass gap.}
\]

Entretanto, o arquivo original:

\[
\texttt{pt-br/30 - Resolução Eletro-Geometrica do Problema CP Forte.md}
\]

trata do problema CP forte, não de confinamento.

O material correto para esta questão é o capítulo:

\[
\texttt{pt-br/27 - O Confinamento e o Mass Gap de Yang-Mills.md}.
\]

Logo, a Questão 30 deve ser respondida usando o conteúdo do capítulo 27, não o
capítulo 30 original.

---

## 3. Qual é a teoria de calibre não abeliana?

Se a pergunta for respondida no sentido físico padrão, a teoria de calibre é
Yang-Mills com grupo compacto simples \(G\), em particular:

\[
\boxed{
G=SU(3)_C
}
\]

para a cromodinâmica quântica efetiva.

A conexão de calibre é:

\[
A_\mu(x)=A_\mu^a(x)T_a,
\]

com:

\[
[T_a,T_b]=if_{abc}T_c.
\]

A curvatura é:

\[
\boxed{
F_{\mu\nu}
=
\partial_\mu A_\nu
-
\partial_\nu A_\mu
+
g[A_\mu,A_\nu].
}
\]

Em componentes:

\[
\boxed{
F_{\mu\nu}^a
=
\partial_\mu A_\nu^a
-
\partial_\nu A_\mu^a
+
g f^{abc}A_\mu^bA_\nu^c.
}
\]

Na GDQ, essa teoria não deve ser tomada como ontologia fundamental. Ela deve
aparecer como setor efetivo de conexões internas/torsionais sobre o espaço
físico reconstruído.

A tradução estrutural é:

\[
\boxed{
A_\mu
\quad\leftrightarrow\quad
\text{conexão efetiva induzida pela geometria/torsão interna.}
}
\]

Mas a derivação de \(SU(3)_C\) depende da Questão 28. Portanto, para a Questão
30, \(SU(3)_C\) ainda deve ser tratado como setor efetivo condicional.

---

## 4. Qual é a ação?

A ação Yang-Mills euclidiana padrão é:

\[
\boxed{
S_{\rm YM}[A]
=
\frac{1}{4g^2}
\int_{\mathbb R^4}
F_{\mu\nu}^aF_{\mu\nu}^a\,d^4x.
}
\]

Em forma geométrica:

\[
\boxed{
S_{\rm YM}[A]
=
\frac{1}{2g^2}
\int
\operatorname{Tr}(F_A\wedge *F_A).
}
\]

Na GDQ, o análogo efetivo deve vir da expansão da ação oficial no setor de
conexões internas:

\[
\mathcal S_{\rm GDQ}
\quad\Longrightarrow\quad
S_{\rm eff}[A,g,f,B]
=
S_{\rm geom}[g,f,B]
+
\frac{1}{2g_{\rm eff}^2}
\int\operatorname{Tr}(F_A\wedge *F_A)
+
\cdots.
\]

O texto original sugere a identificação:

\[
\operatorname{Tr}(F_{\mu\nu}F^{\mu\nu})
\sim
|\mathcal R_B|^2,
\]

onde \(\mathcal R_B\) é a curvatura associada à conexão com torsão de Bismut.

Essa ideia é aproveitável, mas precisa ser formalizada. Falta mostrar:

1. qual é exatamente o fibrado principal;
2. qual conexão efetiva \(A\) é extraída da geometria;
3. como \(F_A\) aparece na expansão da ação;
4. como \(g_{\rm eff}\) é normalizado;
5. qual domínio funcional define a medida quântica.

Sem isso, a ação de Yang-Mills ainda está sendo importada como setor efetivo,
não derivada completamente da GDQ.

---

## 5. Como se definem Wilson loops?

Para uma curva fechada \(C\), o Wilson loop na representação \(R\) é:

\[
\boxed{
W_R(C)
=
\operatorname{Tr}_R
\mathcal P
\exp
\left(
i\oint_C A_\mu dx^\mu
\right).
}
\]

Em teoria de calibre, o diagnóstico de confinamento vem do valor esperado:

\[
\boxed{
\langle W_R(C)\rangle.
}
\]

Uma teoria confinante deve apresentar lei de área para laços grandes:

\[
\boxed{
\langle W_R(C)\rangle
\sim
\exp[-\sigma\,{\rm Area}(C)]
}
\]

com:

\[
\sigma>0.
\]

Na GDQ, o Wilson loop pode ser reinterpretado como holonomia geométrica da
conexão efetiva:

\[
\boxed{
\operatorname{Hol}_C(A)
=
\mathcal P
\exp
\left(
i\oint_C A
\right).
}
\]

Ou, no vocabulário torsional:

\[
\operatorname{Hol}_C(B)
\sim
\exp
\left(
\frac{i}{\hbar}
\oint_C dS_R
\right).
\]

Mas essa identificação não substitui o cálculo de \(\langle W(C)\rangle\). Para
fechar a questão, ainda é necessário calcular o valor esperado do loop na medida
efetiva da GDQ e demonstrar o decaimento por área.

---

## 6. A lei de área é derivada?

No texto atual, não plenamente.

O argumento existente é:

1. duas fontes de vorticidade deformam o fluido geométrico;
2. o fluxo de Ricci contrai as direções transversais;
3. o potencial de Bohm impede o colapso singular;
4. forma-se um tubo de fluxo com seção transversal finita;
5. a energia fica concentrada ao longo do eixo;
6. se a densidade de energia e a área forem constantes, então:

   \[
   V(r)=\sigma r.
   \]

O problema é que o passo 4 para 6 ainda contém uma hipótese forte. A lei linear
segue se:

\[
\mathcal A(r)\to\mathcal A_0,
\qquad
\mathcal E(r)\to\mathcal E_0,
\]

com:

\[
\mathcal A_0>0,
\qquad
\mathcal E_0>0.
\]

Então:

\[
V(r)
=
\int_0^r \mathcal E(z)\mathcal A(z)\,dz
\sim
\mathcal E_0\mathcal A_0 r
=
\sigma r.
\]

Mas isso é uma consequência condicional, não uma prova independente.

Para derivar a lei de área, seria necessário provar:

\[
\boxed{
\langle W(C)\rangle
\le
C_0\exp[-\sigma\,{\rm Area}(C)]
}
\]

para laços grandes, com \(\sigma>0\) obtido da geometria.

A versão geométrica equivalente seria provar que a superfície mínima \(S_C\)
preenchendo o laço \(C\) carrega energia mínima:

\[
E[S_C]\ge\sigma\,{\rm Area}(S_C).
\]

Ou seja:

\[
\boxed{
\text{a lei de área ainda não foi demonstrada; ela foi motivada por tubo de
fluxo.}
}
\]

---

## 7. A seção transversal do tubo emerge ou é assumida?

No texto atual, ela é parcialmente motivada, mas ainda não rigorosamente
derivada.

A ideia proposta é:

\[
R_{\perp\perp}
=
\frac14\nabla_\perp\nabla_\perp Q.
\]

Essa condição estacionária deveria fixar o raio transversal \(r_\perp\) e:

\[
\mathcal A_0=\pi r_\perp^2.
\]

O problema é que o texto não resolve explicitamente o problema transversal:

\[
\boxed{
\frac{\delta E_{\perp}}{\delta r_\perp}=0,
\qquad
\frac{\delta^2 E_{\perp}}{\delta r_\perp^2}>0.
}
\]

Para dizer que \(\mathcal A_0\) emerge, é preciso fornecer:

1. ansatz métrico transversal;
2. densidade \(\rho_\perp\);
3. potencial de Bohm \(Q_\perp\);
4. equação estacionária completa;
5. solução \(r_\perp=r_0\);
6. estabilidade linear dessa solução;
7. independência assintótica em relação a \(r\).

Sem isso, a seção transversal deve ser tratada como hipótese geométrica
plausível:

\[
\boxed{
\mathcal A_0
\text{ ainda está assumida/estabilizada por argumento qualitativo, não
derivada por solução explícita.}
}
\]

---

## 8. Qual é o espectro do Hamiltoniano?

Para uma prova de mass gap, é preciso definir um Hamiltoniano físico.

Na formulação Yang-Mills canônica, em calibre temporal \(A_0=0\), os campos são
\(A_i^a\) e \(E_i^a\), com vínculo de Gauss:

\[
\boxed{
D_iE_i=0.
}
\]

O Hamiltoniano é:

\[
\boxed{
H_{\rm YM}
=
\frac12
\int_{\mathbb R^3}
\left(
E_i^aE_i^a
+
B_i^aB_i^a
\right)d^3x.
}
\]

O espaço físico é o subespaço invariante por calibre:

\[
\mathcal H_{\rm phys}
=
\{\Psi[A]\;|\;D_iE_i\Psi=0\}.
\]

O problema do mass gap exige:

\[
\boxed{
\operatorname{Spec}(H)
=
\{0\}
\cup
[\Delta,\infty)
}
\]

ou, em volume finito seguido de limite termodinâmico:

\[
E_1(L)-E_0(L)\to\Delta>0.
\]

No texto da GDQ, aparece uma rota espectral alternativa, usando um operador
geométrico tipo Liouville-Madelung:

\[
\boxed{
\mathcal H_{\rm LM}\phi
=
-\Delta_{\rm LB}\phi
+
\left(
R+|\nabla f|^2-\frac{1}{12}|H|^2
\right)\phi.
}
\]

E a reivindicação é que:

\[
\lambda_1
\ge
\frac{D}{D-1}\Lambda_0
>0.
\]

Então:

\[
\boxed{
\Delta
\ge
\hbar
\sqrt{
\frac{D}{D-1}\Lambda_0
}
>0.
}
\]

Essa rota é matematicamente promissora, mas precisa ser conectada ao
Hamiltoniano físico de Yang-Mills. Falta demonstrar que:

\[
\mathcal H_{\rm LM}
\quad
\text{é espectralmente equivalente ao setor físico de}
\quad
H_{\rm YM}.
\]

Sem essa equivalência, a GDQ prova no máximo um gap geométrico interno, não o
mass gap de Yang-Mills no sentido forte.

---

## 9. Como se prova gap positivo?

A prova estrutural proposta pela GDQ tem a seguinte forma:

1. existe uma curvatura de Ricci-Bismut efetiva limitada inferiormente:

   \[
   R_{ij}
   +\nabla_i\nabla_j f
   -\frac14H_{ikm}H_j{}^{km}
   \ge
   \Lambda_0g_{ij},
   \qquad
   \Lambda_0>0;
   \]

2. isso limita o diâmetro do suporte das flutuações:

   \[
   \operatorname{Diam}(M)
   \le
   \pi
   \sqrt{\frac{D-1}{\Lambda_0}};
   \]

3. pela desigualdade espectral de Lichnerowicz/Obata/Poincaré, o primeiro
   autovalor não nulo satisfaz:

   \[
   \lambda_1
   \ge
   c_D\Lambda_0
   >0;
   \]

4. logo:

   \[
   \Delta
   =
   \hbar\sqrt{\lambda_1}
   >0.
   \]

Essa cadeia é coerente como prova de gap para um operador geométrico elíptico
em domínio compacto/efetivamente compacto.

Mas, para ser prova de mass gap de Yang-Mills, faltam três identificações:

1. provar que \(\Lambda_0>0\) segue da ação oficial, não de hipótese externa;
2. provar que o operador geométrico é o Hamiltoniano físico ou seu equivalente
   espectral;
3. provar que o limite de volume infinito preserva o gap.

Portanto:

\[
\boxed{
\text{o gap positivo é demonstrável condicionalmente no operador geométrico,
mas ainda não como teorema completo de Yang-Mills.}
}
\]

---

## 10. O que pode ser aproveitado do texto original

Pode ser aproveitado:

1. confinamento como rigidez geométrica/torsional;
2. tubo de fluxo como solução efetiva de mínima energia;
3. papel do potencial de Bohm em impedir colapso transversal;
4. interpretação da tensão de corda como energia geométrica por comprimento;
5. rota espectral com operador elíptico;
6. uso de cota inferior de Ricci-Bismut;
7. uso de desigualdades tipo Poincaré, Lichnerowicz, Obata, Myers e Cheng;
8. equação de Fredholm para o valor efetivo
   \(\alpha_s^{\rm eff}=3/(8\pi)\);
9. previsão fenomenológica de polarização de híperons
   \(P_\Lambda\approx0{,}85\%\).

Não deve ser aproveitado como prova final, na forma original:

1. assumir \(\mathcal A_0\) constante sem o adendo variacional;
2. assumir \(\mathcal E\) constante sem Euler-Lagrange/Beltrami;
3. concluir \(V(r)=\sigma r\) apenas por integral unidimensional;
4. afirmar resolução do problema do Clay sem construir a teoria quântica de
   Yang-Mills;
5. substituir Wilson loops por holonomia sem calcular valor esperado;
6. chamar \(\alpha_s^{\rm eff}=3/(8\pi)\) de acoplamento forte completo, pois
   isso ainda não inclui running nem esquema de renormalização;
7. identificar o gap transversal do tubo automaticamente com o mass gap de
   Yang-Mills sem equivalência espectral.

---

## 11. Respostas diretas às perguntas obrigatórias

### 1. Qual é a teoria de calibre não abeliana?

Efetivamente, Yang-Mills com grupo compacto simples, especialmente:

\[
G=SU(3)_C.
\]

Na GDQ, esse grupo ainda precisa ser derivado como setor efetivo da Questão 28.

### 2. Qual é a ação?

No setor efetivo:

\[
S_{\rm YM}
=
\frac{1}{2g^2}
\int\operatorname{Tr}(F\wedge *F).
\]

Na GDQ, falta derivar esse termo da expansão da ação oficial.

### 3. Como se definem Wilson loops?

\[
W_R(C)
=
\operatorname{Tr}_R
\mathcal P
\exp
\left(
i\oint_C A
\right).
\]

Na GDQ, eles devem ser holonomias da conexão geométrica efetiva.

### 4. A lei de área é derivada?

Ainda não. O texto motiva \(V(r)=\sigma r\) por tubo de fluxo, mas não prova:

\[
\langle W(C)\rangle
\sim
\exp[-\sigma{\rm Area}(C)].
\]

### 5. A seção transversal do tubo emerge ou é assumida?

Ainda é parcialmente assumida. Para emergir, é necessário resolver o problema
transversal estacionário e provar estabilidade de \(\mathcal A_0\).

### 6. Qual é o espectro do Hamiltoniano?

O espectro necessário é:

\[
\operatorname{Spec}(H)
=
\{0\}
\cup
[\Delta,\infty),
\qquad
\Delta>0.
\]

O texto fornece uma rota via operador geométrico \(\mathcal H_{\rm LM}\), mas
ainda falta provar equivalência com o Hamiltoniano físico de Yang-Mills.

### 7. Como se prova gap positivo?

Condicionalmente, por cota inferior de Ricci-Bismut:

\[
\operatorname{Ric}^{B}_f
\ge
\Lambda_0g,
\qquad
\Lambda_0>0,
\]

seguida de desigualdade espectral:

\[
\lambda_1\ge c_D\Lambda_0>0.
\]

Mas falta provar que isso é exatamente o mass gap de Yang-Mills.

---

## 12. Fechamento

A Questão 30 deve ficar com o seguinte status:

\[
\boxed{
\text{confinamento geométrico: encaminhado;}
}
\]

\[
\boxed{
\text{lei de área de Wilson: não demonstrada;}
}
\]

\[
\boxed{
\text{mass gap geométrico: condicional;}
}
\]

\[
\boxed{
\text{mass gap de Yang-Mills no sentido Clay: ainda não fechado.}
}
\]

Para fechar oficialmente, será necessário construir uma ponte rigorosa:

\[
\boxed{
\mathcal S_{\rm GDQ}
\Longrightarrow
S_{\rm YM}^{\rm eff}
\Longrightarrow
\langle W(C)\rangle\sim e^{-\sigma A(C)}
\Longrightarrow
\operatorname{Spec}(H)=\{0\}\cup[\Delta,\infty).
}
\]

---

## 13. Adendo — Rota variacional para provar a lei de área e a constante de área

Este adendo registra a rota mais promissora para transformar o argumento
geométrico de confinamento em uma demonstração mais forte.

A ideia central é não começar assumindo o tubo de fluxo com seção transversal
constante. Em vez disso, deve-se provar uma desigualdade variacional de energia
por superfície:

\[
\boxed{
E[A;S]\ge \sigma\,{\rm Area}(S),
\qquad
\sigma>0,
}
\]

para toda superfície \(S\) tal que:

\[
\partial S=C.
\]

Se essa desigualdade for provada, então a lei de área dos Wilson loops segue
naturalmente:

\[
\boxed{
\langle W_R(C)\rangle
\le
C_0
\exp[-\sigma\,{\rm Area}_{\min}(C)].
}
\]

Com isso, o potencial linear deixa de ser uma hipótese e passa a ser
consequência.

Para um Wilson loop retangular \(C_{r,T}\), com extensão espacial \(r\) e tempo
euclidiano \(T\),

\[
{\rm Area}_{\min}(C_{r,T})=rT.
\]

Logo:

\[
V(r)
=
-
\lim_{T\to\infty}
\frac{1}{T}
\log
\langle W(C_{r,T})\rangle.
\]

Se:

\[
\langle W(C_{r,T})\rangle
\sim
e^{-\sigma rT},
\]

então:

\[
\boxed{
V(r)=\sigma r.
}
\]

Assim, a sequência correta passa a ser:

\[
\boxed{
\text{mínimo variacional transversal}
\Longrightarrow
\sigma>0
\Longrightarrow
\text{lei de área}
\Longrightarrow
V(r)=\sigma r.
}
\]

---

## 14. A constante de área como mínimo geométrico

A constante \(\sigma\), chamada usualmente de tensão de corda, deve ser
reinterpretada na GDQ como constante de área geométrica. Ela não deve ser
inserida manualmente.

Ela deve emergir como o menor custo energético por unidade de área necessário
para sustentar uma superfície de holonomia não trivial:

\[
\boxed{
\sigma
=
\inf_{\mathcal C}
\frac{E_{\rm geom}[\mathcal C]}{{\rm Area}(\mathcal C)}.
}
\]

Aqui \(\mathcal C\) representa a classe de configurações geométricas admissíveis
que preenchem o Wilson loop \(C\) e carregam a holonomia de cor.

Uma forma mais explícita seria:

\[
\boxed{
\sigma
=
\inf_{\text{setor topológico}}
\left[
\frac{1}{2g_{\rm eff}^2}|F_A|^2
+
\frac{1}{12}|H_B|^2
+
\rho|\nabla_\perp S_R|^2
+
\frac{\hbar^2}{2m}
|\nabla_\perp\sqrt\rho|^2
+
V_{\rm Ricci-Bohm}
\right]_{\perp}.
}
\]

Nessa leitura:

1. \(|F_A|^2\) mede a curvatura de calibre efetiva;
2. \(|H_B|^2\) mede a rigidez torsional de Bismut/Cartan;
3. \(\rho|\nabla_\perp S_R|^2\) mede a energia de escoamento transversal;
4. \(|\nabla_\perp\sqrt\rho|^2\) é o termo de pressão de Bohm;
5. \(V_{\rm Ricci-Bohm}\) representa o custo de curvatura/contra-pressão
   geométrica.

O ponto decisivo é que:

\[
\boxed{
\sigma>0
}
\]

deve ser provado a partir da positividade desse funcional no setor topológico
não trivial.

---

## 15. Emergência da seção transversal

A seção transversal do tubo deve ser obtida como solução de um problema
variacional local.

Defina a energia transversal:

\[
E_\perp[R]
=
\int_{\Sigma_\perp}
\left[
\frac{1}{2g_{\rm eff}^2}|F_\perp|^2
+
\frac{1}{12}|H_\perp|^2
+
\rho|\nabla_\perp S_R|^2
+
\frac{\hbar^2}{2m}
|\nabla_\perp\sqrt\rho|^2
\right]
d\mu_\perp.
\]

A seção transversal emerge se existir um minimizador não degenerado:

\[
\boxed{
\frac{\delta E_\perp}{\delta R}=0,
\qquad
\frac{\delta^2E_\perp}{\delta R^2}>0.
}
\]

Então:

\[
\boxed{
R=R_0,
\qquad
\mathcal A_0=\pi R_0^2.
}
\]

O que precisa ser provado é:

\[
\boxed{
0<R_0<\infty.
}
\]

Isso pode ser obtido se forem demonstrados dois limites:

\[
\lim_{R\to0}E_\perp[R]=+\infty,
\]

por causa da pressão de Bohm e da concentração de curvatura, e:

\[
\lim_{R\to\infty}E_\perp[R]=+\infty,
\]

por causa da rigidez torsional/curvatura efetiva que impede a dispersão
transversal no setor confinado.

Pelo argumento variacional direto, se \(E_\perp[R]\) é coerciva e
semicontínua inferiormente, existe minimizador:

\[
\boxed{
E_\perp[R_0]
=
\inf_R E_\perp[R].
}
\]

Assim, a área transversal não é assumida. Ela é consequência do mínimo
geométrico.

---

## 16. Relação entre seção transversal e constante de área

Uma vez encontrado o minimizador transversal, a tensão de área pode ser escrita
como:

\[
\boxed{
\sigma
=
\frac{E_\perp[R_0]}{\mathcal A_0}
}
\]

ou, dependendo da normalização do funcional efetivo, como energia por unidade
de comprimento do tubo:

\[
\boxed{
\sigma
=
E_\perp[R_0].
}
\]

A distinção depende de como \(E_\perp\) é definido:

1. se \(E_\perp\) for energia integrada na seção, então \(\sigma=E_\perp\);
2. se \(E_\perp\) for densidade superficial, então
   \(\sigma=E_\perp\mathcal A_0\);
3. se o funcional for normalizado por área, então
   \(\sigma=E_\perp/\mathcal A_0\).

O importante é que \(\sigma\) passa a ser calculável:

\[
\boxed{
\sigma
\text{ é a constante de área determinada pelo mínimo transversal da GDQ.}
}
\]

Essa é a peça que faltava para substituir o argumento fraco:

\[
\text{assume-se } \mathcal A_0 \text{ constante}
\Longrightarrow
V(r)=\sigma r
\]

por uma cadeia mais forte:

\[
\boxed{
E_\perp
\text{ coercivo}
\Longrightarrow
R_0
\Longrightarrow
\mathcal A_0
\Longrightarrow
\sigma>0
\Longrightarrow
\langle W(C)\rangle\sim e^{-\sigma A(C)}
\Longrightarrow
V(r)=\sigma r.
}
\]

---

## 17. Consequência para o mass gap

Depois de obtida a constante de área \(\sigma>0\), o mass gap deve ser provado
por um operador efetivo de flutuações confinadas:

\[
\mathcal H_{\rm conf}
=
-\Delta_A
+
V_{\rm geom}.
\]

O potencial geométrico efetivo deve conter:

\[
V_{\rm geom}
=
R
+
|\nabla f|^2
-
\frac{1}{12}|H|^2
+
Q_{\rm Bohm}
+
V_{\rm area}.
\]

O termo \(V_{\rm area}\) representa a penalização energética associada à
constante de área positiva \(\sigma\). Se:

\[
V_{\rm geom}\ge V_0>0
\]

no setor físico sem modos de calibre puros, então:

\[
\lambda_1(\mathcal H_{\rm conf})\ge cV_0>0.
\]

Logo:

\[
\boxed{
\Delta=\hbar\sqrt{\lambda_1}>0.
}
\]

Assim, a constante de área não serve apenas para obter confinamento linear; ela
também fornece a escala positiva que pode entrar na demonstração do gap.

---

## 18. Fechamento variacional da constância de \(\sigma\)

O ponto que faltava não é encontrar primeiro um valor numérico para \(\sigma\),
mas provar que \(\sigma\) é constante ao longo do tubo. Isso pode ser feito pelo
princípio variacional.

Considere o tubo de fluxo entre duas fontes separadas ao longo de uma coordenada
geodésica \(z\in[0,r]\). O perfil transversal é descrito coletivamente por:

\[
q(z)=
\left(
R(z),
A_\perp(z),
H_\perp(z),
\rho_\perp(z),
S_R^\perp(z)
\right).
\]

A energia efetiva do tubo pode ser escrita como:

\[
\boxed{
E[q]
=
\int_0^r
\mathcal L_\perp(q(z),q'(z))\,dz.
}
\]

Aqui \(\mathcal L_\perp\) é a energia transversal integrada na seção:

\[
\mathcal L_\perp
=
\int_{\Sigma_z}
\left[
\frac{1}{2g_{\rm eff}^2}|F_\perp|^2
+
\frac{1}{12}|H_\perp|^2
+
\rho|\nabla_\perp S_R|^2
+
\frac{\hbar^2}{2m}|\nabla_\perp\sqrt\rho|^2
+
V_{\rm Ricci-Bohm}
\right]
d\mu_\perp
+
\text{termos com }q'(z).
\]

No regime assintótico entre as fontes, a ação não depende explicitamente de
\(z\). Isto é:

\[
\boxed{
\frac{\partial\mathcal L_\perp}{\partial z}=0.
}
\]

Essa é a simetria de translação longitudinal do tubo. Pelo teorema de Noether,
ou equivalentemente pela identidade de Beltrami do cálculo variacional, qualquer
extremo satisfaz:

\[
\boxed{
\mathcal H_z
=
\sum_a
q_a'
\frac{\partial\mathcal L_\perp}{\partial q_a'}
-
\mathcal L_\perp
=
\text{constante}.
}
\]

No bulk confinado, longe das calotas de fechamento nas extremidades, o
minimizador estável é translacionalmente invariante:

\[
\boxed{
q'(z)=0.
}
\]

Então a identidade de Beltrami reduz-se a:

\[
\boxed{
\mathcal L_\perp(q_0,0)=\text{constante}.
}
\]

Definimos essa constante como a tensão geométrica do tubo:

\[
\boxed{
\sigma
\equiv
\mathcal L_\perp(q_0,0).
}
\]

Portanto:

\[
\boxed{
\frac{d\sigma}{dz}=0.
}
\]

Essa é a prova variacional da constância de \(\sigma\). Ela substitui a
hipótese anterior de que a densidade de energia era simplesmente constante.

---

## 19. Constância da área transversal

Como \(q_0\) inclui o raio transversal \(R_0\), a constância de \(q_0\) implica:

\[
\boxed{
R(z)=R_0,
\qquad
\mathcal A(z)=\pi R(z)^2=\pi R_0^2=\mathcal A_0.
}
\]

Logo:

\[
\boxed{
\frac{d\mathcal A}{dz}=0.
}
\]

Essa é a forma correta de demonstrar a constância da área: ela vem da solução
estacionária do problema variacional transversal, não de uma suposição
externa.

A equação de Euler-Lagrange para \(R\) é:

\[
\boxed{
\frac{d}{dz}
\left(
\frac{\partial\mathcal L_\perp}{\partial R'}
\right)
-
\frac{\partial\mathcal L_\perp}{\partial R}
=0.
}
\]

No bulk, \(R'=0\), então:

\[
\boxed{
\frac{\partial\mathcal L_\perp}{\partial R}(R_0)=0.
}
\]

A estabilidade exige:

\[
\boxed{
\frac{\partial^2\mathcal L_\perp}{\partial R^2}(R_0)>0.
}
\]

Assim, \(R_0\) é determinado pela competição entre:

1. compressão de Ricci/torsão;
2. pressão quântica de Bohm;
3. energia de curvatura de calibre;
4. rigidez topológica do setor de holonomia.

O argumento de existência do raio finito é:

\[
\lim_{R\to0}\mathcal L_\perp(R)=+\infty,
\qquad
\lim_{R\to\infty}\mathcal L_\perp(R)=+\infty.
\]

Logo, por coercividade, existe:

\[
\boxed{
R_0=\operatorname*{arg\,min}_{R>0}\mathcal L_\perp(R).
}
\]

E, consequentemente:

\[
\boxed{
\mathcal A_0=\pi R_0^2
}
\]

é uma constante determinada variacionalmente.

---

## 20. Conclusão variacional: lei linear sem assumir densidade constante

Com o resultado anterior, a energia do tubo no bulk é:

\[
E(r)
=
\int_0^r
\mathcal L_\perp(q_0,0)\,dz
+
E_{\rm borda}.
\]

Como:

\[
\mathcal L_\perp(q_0,0)=\sigma,
\]

temos:

\[
\boxed{
E(r)=\sigma r+E_{\rm borda}.
}
\]

No limite assintótico:

\[
\boxed{
V(r)
=
\sigma r+O(1).
}
\]

Portanto:

\[
\boxed{
\lim_{r\to\infty}\frac{V(r)}{r}
=
\sigma.
}
\]

Isso fecha o ponto criticado pela auditoria:

\[
\boxed{
\text{não se assume densidade constante;}
\quad
\text{ela é consequência da equação variacional e da simetria longitudinal.}
}
\]

O papel da área é:

\[
\boxed{
\mathcal A_0
=
\pi R_0^2
\quad
\text{com}
\quad
R_0=\operatorname*{arg\,min}\mathcal L_\perp.
}
\]

E o papel da tensão é:

\[
\boxed{
\sigma
=
\mathcal L_\perp(q_0,0)
=
\inf_q\mathcal L_\perp(q,0)
>0.
}
\]

Assim, a constante de área/tensão é obtida do princípio variacional.

---

## 21. Consequência para Wilson loops

Para um Wilson loop retangular \(C_{r,T}\), a superfície mínima tem área:

\[
A_{\min}=rT.
\]

O resultado variacional acima mostra que qualquer configuração que transporte a
holonomia confinante através dessa superfície possui custo mínimo:

\[
\boxed{
E_{\min}[C_{r,T}]
\ge
\sigma rT.
}
\]

Portanto, no funcional euclidiano:

\[
\boxed{
\langle W(C_{r,T})\rangle
\lesssim
\exp(-\sigma rT).
}
\]

Logo:

\[
V(r)
=
-
\lim_{T\to\infty}
\frac1T
\log\langle W(C_{r,T})\rangle
\ge
\sigma r.
\]

Quando o minimizador \(q_0\) é atingido, a desigualdade satura
assintoticamente:

\[
\boxed{
V(r)\sim\sigma r.
}
\]

Essa é a forma correta de obter a lei de área:

\[
\boxed{
\langle W(C)\rangle
\sim
\exp[-\sigma A_{\min}(C)].
}
\]

---

## 22. Fechamento atualizado da Questão 30

Com o adendo variacional, a parte fraca do argumento original é corrigida.

Antes:

\[
\text{assume-se } \mathcal A_0,\mathcal E_0 \text{ constantes}
\Longrightarrow
V(r)=\sigma r.
\]

Agora:

\[
\boxed{
\delta E[q]=0
\quad+\quad
\partial_z\mathcal L_\perp=0
\quad\Longrightarrow\quad
\mathcal L_\perp(q_0,0)=\sigma=\text{constante}
\quad\Longrightarrow\quad
V(r)=\sigma r+O(1).
}
\]

Portanto, dentro do setor geométrico efetivo da GDQ:

\[
\boxed{
\text{a constância da área e da tensão pode ser demonstrada variacionalmente.}
}
\]

O que ainda fica condicionado à Questão 28 é a identificação completa desse
setor geométrico com \(SU(3)_C\) Yang-Mills no sentido forte.

---

## 23. Adendo — Fredholm para \(\alpha_s\) e polarização de híperons

O capítulo `pt-br/27 - O Confinamento.md` contém dois cálculos físicos que não
devem ser classificados como ausentes.

### 23.1 Equação de Fredholm para \(\alpha_s\)

O manuscrito propõe uma equação integral de Fredholm de segunda espécie:

\[
\boxed{
\psi(\theta)
=
\phi_0(\theta)
+
\lambda\int_0^{2\pi}K(\theta,\theta')\psi(\theta')\,d\theta'.
}
\]

Com:

\[
\boxed{
\phi_0=\frac{n}{4\pi},
\qquad
n=3,
\qquad
K=I,
\qquad
\lambda=-\frac1{2\pi}.
}
\]

Na discretização periódica usada no texto:

\[
\boxed{
(I-\lambda KW)\psi=\phi_0
\quad\Longrightarrow\quad
2\psi=\phi_0.
}
\]

Logo, o fator de transmissão fica:

\[
\boxed{
T_{\rm transm}=\frac12.
}
\]

E o acoplamento forte efetivo proposto é:

\[
\boxed{
\alpha_s
=
T_{\rm transm}\frac{3}{4\pi}
=
\frac{3}{8\pi}
\approx0{,}119366.
}
\]

Portanto, o manuscrito não trata \(\alpha_s\) apenas qualitativamente. Há uma
proposta analítica explícita.

A ressalva é que esse valor deve ser entendido como:

\[
\boxed{
\alpha_s^{\rm eff}
\text{ em uma escala/topologia hadrônica específica,}
}
\]

não como running completo de QCD:

\[
\boxed{
\alpha_s(\mu)
}
\]

em um esquema de renormalização. Para fechar a ponte com Yang-Mills/QCD, ainda
faltam:

1. identificar a escala \(\mu\) associada ao circuito geométrico;
2. derivar a equação de grupo de renormalização efetiva;
3. mostrar como \(\alpha_s^{\rm eff}=3/(8\pi)\) se conecta a
   \(\alpha_s(\mu)\);
4. justificar globalmente o núcleo \(K=I\) e o parâmetro
   \(\lambda=-1/(2\pi)\) a partir da ação oficial.

### 23.2 Polarização de híperons \(\Lambda\)

O capítulo também propõe uma previsão fenomenológica para a polarização global:

\[
\boxed{
P_\Lambda
=
\frac{\hbar\omega_{\rm fluid}}{2k_BT}
\left(
\frac{\chi_{{\rm Fano},n}}{\delta^2}
\right).
}
\]

Com os valores indicados no manuscrito, obtém-se:

\[
\boxed{
P_\Lambda\approx0{,}85\%.
}
\]

Esse cálculo é relevante como teste fenomenológico do acoplamento spin-órbita
Madelung/torsão de Cartan em QGP. Ele deve ser preservado como previsão física
da GDQ.

A ressalva é que ele não substitui a prova de confinamento/mass gap. Ele é um
teste de consistência fenomenológica do setor torsional-vorticial.

### 23.3 Correção de status

Assim, a Questão 30 deve distinguir:

\[
\boxed{
\text{confinamento geométrico e tensão: fortalecidos variacionalmente;}
}
\]

\[
\boxed{
\alpha_s^{\rm eff}=3/(8\pi)
\text{ via Fredholm: proposta analítica presente;}
}
\]

\[
\boxed{
P_\Lambda\approx0{,}85\%
\text{ via torsão/vorticidade: previsão fenomenológica presente;}
}
\]

\[
\boxed{
\text{lei de área de Wilson e mass gap Yang-Mills completo: ainda pendentes.}
}
\]

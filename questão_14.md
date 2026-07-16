# Questão 14 — Qual é o mapeamento Perelman--Madelung?

## 1. Pergunta

A Questão 14 pergunta:

\[
\boxed{
\text{qual é o mapa entre a formulação Perelman da GDQ e a formulação
Madelung?}
}
\]

As perguntas obrigatórias de `14-0.md` são:

1. qual é o mapa entre \((g,f,\tau)\) e \((\rho,S,t)\)?
2. o mapa preserva equações?
3. é injetivo, sobrejetivo ou apenas parcial?
4. como trata nós \(\rho=0\)?
5. como trata fase multivalorada?
6. como trata estados dependentes do tempo?
7. como trata superposição?

A resposta aceitável é:

\[
\boxed{
\text{um teorema preciso com prova ou uma delimitação explícita do domínio em
que a correspondência funciona.}
}
\]

---

## 2. Resposta curta

O mapeamento Perelman--Madelung da GDQ é real, útil e matematicamente
controlável, mas não é uma bijeção global entre todos os campos geométricos
\((g,f,\tau)\) e todos os estados quânticos \((\rho,S,t)\).

Ele é uma correspondência parcial, válida no setor regular de Madelung:

\[
\boxed{
\rho>0,
\qquad
S_R\text{ localmente monovalorado},
\qquad
f\in C^2,
\qquad
g\text{ regular}.
}
\]

Nesse domínio:

\[
\boxed{
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\ln\rho
+i\frac{S_R}{\hbar}
\quad
\text{com a convenção da GDQ}
}
\]

de forma equivalente a:

\[
\boxed{
\rho
=
e^{-(f+\bar f)/2},
\qquad
S_R
=
\frac{\hbar}{2i}(f-\bar f).
}
\]

A função de onda efetiva é:

\[
\boxed{
\Psi
=
\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

O mapa preserva as equações no setor Madelung regular:

\[
\boxed{
\frac{\delta I}{\delta S_R}=0
\Longleftrightarrow
\partial_t\rho+\nabla\cdot(\rho v)=0,
}
\]

e:

\[
\boxed{
\frac{\delta I}{\delta\rho}=0
\Longleftrightarrow
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
}
\]

Fora desse domínio, o mapa precisa de cartas, ramos, dados topológicos ou
decomposição em modos.

---

## 3. Convenção correta para \(f\)

Nas questões anteriores foi fixado:

\[
\boxed{
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
}
\]

Também foi fixado:

\[
\boxed{
\rho
=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2}.
}
\]

Como:

\[
\frac{f+\bar f}{2}
=
-\frac{S_I}{\hbar},
\]

temos:

\[
\boxed{
S_I=\hbar\ln\rho.
}
\]

Então:

\[
\boxed{
f
=
-\ln\rho
+i\frac{S_R}{\hbar}
}
\]

ou, equivalentemente:

\[
\boxed{
\operatorname{Re}f=-\ln\rho,
\qquad
\operatorname{Im}f=\frac{S_R}{\hbar}.
}
\]

Essa é a convenção que mantém:

\[
\boxed{
e^{-(f+\bar f)/2}=\rho.
}
\]

Observação: se algum rascunho anterior escreveu \(f=\ln\rho+iS_R/\hbar\), o
sinal da parte real deve ser corrigido. A convenção oficial da GDQ é:

\[
\boxed{
f=-\ln\rho+iS_R/\hbar.
}
\]

---

## 4. Mapa direto

No domínio regular:

\[
\boxed{
\rho>0.
}
\]

O mapa direto de Perelman para Madelung é:

\[
\boxed{
(g,f,\tau)
\longmapsto
(G,\rho,S_R,\lambda).
}
\]

Com:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}.
}
\]

\[
\boxed{
S_R=\frac{\hbar}{2i}(f-\bar f).
}
\]

\[
\boxed{
R=\sqrt\rho.
}
\]

\[
\boxed{
\Psi=R\,e^{iS_R/\hbar}.
}
\]

E:

\[
\boxed{
\lambda=\tau
\quad
\text{no setor de fluxo;}
}
\]

ou:

\[
\boxed{
\lambda=t
\quad
\text{no setor físico.}
}
\]

A relação entre ambos é dada por:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

A métrica \(G\) usada no setor Madelung é a métrica efetiva do setor
considerado:

1. no bulk geométrico, \(G=g\);
2. na camada física, \(G=h\);
3. em uma folha espacial, \(G\) é a métrica espacial induzida.

---

## 5. Mapa inverso

Dado um par Madelung regular:

\[
\boxed{
\rho>0,
\qquad
S_R\in C^1_{\rm loc},
}
\]

define-se:

\[
\boxed{
f=-\ln\rho+i\frac{S_R}{\hbar}.
}
\]

Então:

\[
\boxed{
\bar f=-\ln\rho-i\frac{S_R}{\hbar}.
}
\]

E:

\[
\boxed{
e^{-(f+\bar f)/2}=\rho.
}
\]

Logo, localmente, o mapa inverso existe.

Mas ele exige:

1. \(\rho>0\);
2. escolha de ramo para \(S_R\);
3. métrica \(g\) ou \(h\) especificada;
4. identificação do parâmetro de evolução \(\lambda\).

Sem esses dados, \((\rho,S_R)\) não reconstrói unicamente \((g,f,\tau)\).

---

## 6. O mapa preserva equações?

Sim, dentro do setor regular e com a ação reduzida correta.

O setor Madelung/canônico da ação é:

\[
\boxed{
I_{\rm Mad}[\rho,S_R]
=
\int d\lambda
\int_{\Sigma_\lambda}
\rho
\left[
\partial_\lambda S_R
+\frac12
G^{AB}\partial_AS_R\partial_BS_R
+V_{\rm eff}[\rho,g]
\right]d\mu_G.
}
\]

Com massa explícita no setor não relativístico:

\[
\boxed{
I_{\rm Mad}[\rho,S_R]
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
\right)
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx.
}
\]

Variando \(S_R\):

\[
\boxed{
\frac{\delta I}{\delta S_R}=0
\Longrightarrow
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
\]

Com:

\[
\boxed{
v=\frac{\nabla S_R}{m}.
}
\]

Variando \(\rho\):

\[
\boxed{
\frac{\delta I}{\delta\rho}=0
\Longrightarrow
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+Q
=0.
}
\]

Com:

\[
\boxed{
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
\]

Juntas, essas duas equações são equivalentes à equação de Schrödinger para:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

Portanto:

\[
\boxed{
\text{o mapa preserva as equações no setor Madelung regular.}
}
\]

---

## 7. Teorema local de correspondência

### Teorema

Seja \(\Omega\subset M\) um aberto simplesmente conexo, sem nós da densidade:

\[
\boxed{
\rho(x)>0
\quad
\forall x\in\Omega.
}
\]

Suponha:

\[
\rho\in C^2(\Omega),
\qquad
S_R\in C^2(\Omega),
\qquad
g\in C^2(\Omega).
\]

Então existe uma correspondência local entre:

\[
\boxed{
(g,f)
}
\]

e:

\[
\boxed{
(g,\rho,S_R)
}
\]

dada por:

\[
\boxed{
f=-\ln\rho+iS_R/\hbar.
}
\]

Essa correspondência é inversível localmente por:

\[
\boxed{
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
}
\]

Além disso, no setor em que a ação reduzida é \(I_{\rm Mad}\), a equação
variacional em \(S_R\) é a continuidade, e a equação variacional em \(\rho\) é
Hamilton--Jacobi--Bohm.

### Prova

A prova é direta.

Se \(\rho>0\), então \(\ln\rho\) está bem definido.

Defina:

\[
f=-\ln\rho+iS_R/\hbar.
\]

Então:

\[
f+\bar f=-2\ln\rho.
\]

Logo:

\[
e^{-(f+\bar f)/2}=e^{\ln\rho}=\rho.
\]

Também:

\[
f-\bar f=2iS_R/\hbar.
\]

Logo:

\[
\frac{\hbar}{2i}(f-\bar f)=S_R.
\]

As variações da ação reduzida em \(S_R\) e \(\rho\) foram demonstradas nas
Questões 10 e 11. Portanto, dentro desse domínio regular, o mapa preserva o par
de equações Madelung.

\[
\boxed{\text{QED}}
\]

---

## 8. Injetividade, sobrejetividade e parcialidade

### 8.1 Injetividade local

Fixados:

1. \(g\);
2. o ramo de \(S_R\);
3. a convenção de fase;
4. a normalização de \(\rho\);

o mapa:

\[
f\mapsto(\rho,S_R)
\]

é localmente injetivo.

De fato:

\[
\rho=e^{-\operatorname{Re}f},
\qquad
S_R=\hbar\operatorname{Im}f.
\]

Logo \(f\) é recuperado por:

\[
f=-\ln\rho+iS_R/\hbar.
\]

### 8.2 Não injetividade global

Globalmente, há ambiguidade de fase:

\[
\boxed{
S_R\sim S_R+2\pi\hbar k,
\qquad
k\in\mathbb Z.
}
\]

pois:

\[
e^{iS_R/\hbar}
=
e^{i(S_R+2\pi\hbar k)/\hbar}.
\]

Assim, se a fase for considerada módulo \(2\pi\hbar\), o mapa não é
globalmente injetivo sem escolher ramo ou classe de homotopia.

### 8.3 Não sobrejetividade global

Nem todo estado quântico abstrato corresponde a um único par regular
\((\rho,S_R)\) global.

Estados com:

1. nós;
2. interferência destrutiva;
3. fase multivalorada;
4. superposições com zeros;
5. setores spinoriais;
6. estados em fibrados não triviais;

exigem atlas, ramos ou dados topológicos adicionais.

Logo:

\[
\boxed{
\text{o mapeamento Perelman--Madelung é parcial, não uma bijeção global.}
}
\]

---

## 9. Como tratar nós \(\rho=0\)

Em nós:

\[
\boxed{
\rho=0.
}
\]

Então:

\[
\ln\rho
\]

diverge.

Logo:

\[
f=-\ln\rho+iS_R/\hbar
\]

fica singular.

Além disso:

\[
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\]

pode divergir.

Portanto:

\[
\boxed{
\rho=0\text{ não pertence ao domínio regular do mapa.}
}
\]

O tratamento correto é:

1. remover o conjunto nodal:

\[
\Omega^\ast=\Omega\setminus\{\rho=0\};
\]

2. trabalhar por cartas em cada componente conexa de \(\Omega^\ast\);
3. impor condições de compatibilidade ao redor dos nós;
4. interpretar nós como defeitos, vórtices, estômatos ou singularidades
   topológicas;
5. controlar a energia de Bohm/Fisher perto do nó.

Assim:

\[
\boxed{
\text{nós são fronteiras/singularidades do atlas Madelung, não pontos
regulares do mapa.}
}
\]

---

## 10. Como tratar fase multivalorada

A fase pode satisfazer:

\[
\boxed{
\oint_\Gamma \nabla S_R\cdot dx
=
2\pi\hbar N,
\qquad
N\in\mathbb Z.
}
\]

Nesses casos, \(S_R\) não é uma função global monovalorada. Mas:

\[
e^{iS_R/\hbar}
\]

continua sendo monovalorada se a quantização acima vale.

O tratamento correto é:

1. escolher cartas locais \(U_a\);
2. definir fases locais \(S_R^{(a)}\);
3. impor transições:

\[
\boxed{
S_R^{(a)}-S_R^{(b)}
=
2\pi\hbar k_{ab}.
}
\]

Então:

\[
\boxed{
f^{(a)}-f^{(b)}
=
i\,2\pi k_{ab}.
}
\]

Logo, \(f\) também é definido por ramos.

Conclusão:

\[
\boxed{
\text{fase multivalorada exige atlas e dados topológicos; não invalida o mapa
local.}
}
\]

---

## 11. Como tratar estados dependentes do tempo

Estados dependentes do tempo são tratados pela variável:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

A GDQ distingue:

1. \(\tau\): parâmetro de fluxo geométrico, escala e relaxação;
2. \(t\): tempo físico da camada lorentziana;
3. \(z_\tau\): combinação causal complexificada.

No setor Madelung físico:

\[
\boxed{
\rho=\rho(t,x),
\qquad
S_R=S_R(t,x).
}
\]

No setor de fluxo:

\[
\boxed{
\rho=\rho(\tau,x),
\qquad
S_R=S_R(\tau,x).
}
\]

Na ação de contorno:

\[
\boxed{
f=f(z_\tau,x).
}
\]

O mapa continua válido ponto a ponto:

\[
\boxed{
f(z_\tau,x)
=
-\ln\rho(z_\tau,x)
+iS_R(z_\tau,x)/\hbar.
}
\]

Mas as interpretações de \(\tau\) e \(t\) não devem ser confundidas:

\[
\boxed{
\tau\text{ não é tempo físico;}
\qquad
t\text{ é o parâmetro físico causal na camada }N^4.
}
\]

---

## 12. Como tratar superposição

A transformação de Madelung é não linear:

\[
\Psi
=
\sqrt\rho\,e^{iS_R/\hbar}.
\]

Portanto, se:

\[
\Psi=\Psi_1+\Psi_2,
\]

não vale, em geral:

\[
\rho=\rho_1+\rho_2
\]

nem:

\[
S_R=S_{R,1}+S_{R,2}.
\]

Na verdade:

\[
\boxed{
\rho
=
|\Psi_1+\Psi_2|^2
=
\rho_1+\rho_2
+2\sqrt{\rho_1\rho_2}
\cos\left(
\frac{S_1-S_2}{\hbar}
\right).
}
\]

E:

\[
\boxed{
S_R
=
\hbar\,\arg(\Psi_1+\Psi_2).
}
\]

Logo:

\[
\boxed{
\text{o mapa trata superposição depois de somar as amplitudes complexas, não
somando diretamente os pares }(\rho,S_R).
}
\]

Consequência:

1. superposição pode criar nós \(\rho=0\);
2. nesses nós, o mapa Madelung local quebra;
3. a descrição deve ser feita por ramos/células nodais;
4. a linearidade pertence a \(\Psi\), não a \((\rho,S_R)\).

---

## 13. Relação com \(\mathcal U\)

Pela Questão 13:

\[
\boxed{
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

Logo:

\[
\boxed{
(4\pi z_\tau)^n\mathcal U=\rho.
}
\]

Assim, a medida da ação é a densidade Madelung multiplicada pelo kernel
geométrico/difusivo.

Isso não adiciona novo campo independente.

---

## 14. Relação com a métrica

O mapa:

\[
f\leftrightarrow(\rho,S_R)
\]

não determina sozinho a métrica \(g\).

A métrica é um campo fundamental independente da ação oficial:

\[
\boxed{
g_{\mu\bar\nu}.
}
\]

Ela satisfaz sua própria equação variacional:

\[
\boxed{
\frac{\delta S_{\rm phys}}{\delta g^{\mu\bar\nu}}=0.
}
\]

Portanto:

\[
\boxed{
(g,f,\tau)
\mapsto
(g,\rho,S_R,\tau)
}
\]

é direto, mas:

\[
\boxed{
(\rho,S_R,t)
\not\mapsto
g
}
\]

sem uma equação métrica, dados de bordo e escolha de setor.

Na camada física, usa-se a métrica lorentziana constitutiva \(h\), já definida
na Questão 2:

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-2
\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
}
\]

---

## 15. Delimitação final do domínio

O mapeamento Perelman--Madelung da GDQ é válido no domínio:

\[
\boxed{
\mathcal D_{\rm reg}
=
\{
(g,f):
g\in C^2,\ 
f\in C^2,\ 
\rho=e^{-(f+\bar f)/2}>0,\ 
S_R=\hbar\operatorname{Im}f
\text{ localmente monovalorado}
\}.
}
\]

Com:

\[
\boxed{
\rho\in C^2,
\qquad
S_R\in C^2,
\qquad
\Psi=\sqrt\rho e^{iS_R/\hbar}.
}
\]

Fora desse domínio:

1. nós exigem remoção do conjunto nodal;
2. fases multivaloradas exigem atlas;
3. superposição exige reconstrução via \(\Psi\);
4. setores spinoriais/gauge exigem fibrados adicionais;
5. estados singulares exigem tratamento distribucional ou topológico.

Portanto:

\[
\boxed{
\text{o mapa é local, regular e setorial; não é uma equivalência global de
toda a teoria.}
}
\]

---

## 16. Status da Questão 14

\[
\boxed{
\text{Questão 14 fechada oficialmente.}
}
\]

A correspondência Perelman--Madelung é:

\[
\boxed{
f=-\ln\rho+iS_R/\hbar,
\qquad
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
}
\]

Ela preserva as equações no setor regular:

\[
\boxed{
\delta_{S_R}I=0
\Longleftrightarrow
\text{continuidade},
}
\]

\[
\boxed{
\delta_\rho I=0
\Longleftrightarrow
\text{Hamilton--Jacobi--Bohm}.
}
\]

Mas:

\[
\boxed{
\text{não é uma bijeção global.}
}
\]

Ela é uma correspondência parcial, local e regular. Nós, fases multivaloradas,
superposições, spin, gauge e setores topológicos exigem dados adicionais.

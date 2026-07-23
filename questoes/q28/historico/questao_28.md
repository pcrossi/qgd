# Questão 28 — Como surge o grupo do Modelo Padrão?

## 1. Pergunta

A Questão 28 pergunta:

\[
\boxed{
\text{como a GDQ obtém }SU(3)_C\times SU(2)_L\times U(1)_Y?
}
\]

O arquivo `28-0.md` exige que sejam especificados:

1. geradores;
2. constantes de estrutura;
3. representações;
4. hipercargas;
5. quiralidade;
6. bósons de calibre;
7. acoplamentos;
8. cancelamento de anomalias.

Também impõe a restrição correta:

\[
\boxed{
\text{vetores de Killing genéricos não bastam.}
}
\]

---

## 2. Resposta curta

Na forma atual da teoria, a Questão 28 ainda não está fechada como derivação
fundamental.

O que pode ser afirmado de modo rigoroso é:

\[
\boxed{
\text{a GDQ pode acomodar um setor efetivo com simetria de calibre do Modelo
Padrão.}
}
\]

Mas ainda não foi demonstrado que:

\[
\boxed{
SU(3)_C\times SU(2)_L\times U(1)_Y
\text{ emerge inevitavelmente da ação oficial da GDQ.}
}
\]

A resposta oficial, portanto, deve ser:

\[
\boxed{
\text{Questão 28 parcialmente estruturada, mas não fechada como teorema.}
}
\]

Isso não é uma falha fatal da GDQ. É uma delimitação de escopo. As questões
anteriores fecharam a base geométrica, Hilbert, unitariedade, Born, spin e
estatística. A emergência completa do grupo do Modelo Padrão exige um cálculo
adicional de fibrados, índice, representações e anomalias.

---

## 3. Cuidado conceitual

A GDQ não deve ser transformada no Modelo Padrão por definição.

O objetivo correto não é escrever:

\[
\boxed{
\text{assuma }G_{\rm SM}=SU(3)_C\times SU(2)_L\times U(1)_Y.
}
\]

O objetivo correto é demonstrar:

\[
\boxed{
\text{as estruturas geométricas efetivas da GDQ selecionam exatamente um setor
com a álgebra de calibre do Modelo Padrão.}
}
\]

Ou seja:

\[
\boxed{
\text{GDQ deve recuperar o setor de calibre efetivo; não postular o Modelo
Padrão inteiro.}
}
\]

---

## 4. O que o texto original fornece

O capítulo `pt-br/31 - Emergência Geométrica das Interações de Calibre.md`
contém uma ideia útil:

\[
\boxed{
\text{simetrias internas podem ser vistas como isometrias/holonomias de dados
geométricos internos.}
}
\]

Essa intuição é compatível com uma rota de geometrização.

Porém, o texto original não fecha a Questão 28 por quatro motivos.

### 4.1 Incompatibilidade com a base oficial

O capítulo original usa uma variedade complexa tridimensional:

\[
\mathcal M_{\mathbb C}^3.
\]

Mas a base oficial já foi fixada nas Questões 2 e 3 como:

\[
\boxed{
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb C}M=4.
}
\]

Portanto, qualquer argumento baseado em \(\mathcal M_{\mathbb C}^3\) não pode
ser usado como prova oficial sem rederivação.

### 4.2 Isometria não é automaticamente grupo de gauge

Mesmo que uma subvariedade possua isometrias, isso não determina
automaticamente:

1. o fibrado principal de gauge;
2. as representações dos férmions;
3. as hipercargas;
4. a quiralidade;
5. o cancelamento de anomalias.

Em particular:

\[
\boxed{
\text{Killing vectors}\neq\text{derivação do Modelo Padrão.}
}
\]

### 4.3 Problema com \(CP^2\)

O texto sugere:

\[
\operatorname{Isom}(CP^2)=SU(3)/U(1)\cong SU(3).
\]

Essa identificação não está correta como escrita.

A isometria holomorfa de \(CP^2\) com métrica de Fubini--Study é:

\[
\boxed{
\operatorname{Isom}_{\rm hol}(CP^2)\simeq PSU(3)=SU(3)/\mathbb Z_3.
}
\]

Já:

\[
CP^2\simeq SU(3)/S(U(2)\times U(1)).
\]

Portanto, \(CP^2\) pode sugerir uma relação com \(SU(3)\), mas não prova por si
só o setor cromodinâmico.

### 4.4 Problema com \(S^3\)

O texto sugere que:

\[
\operatorname{Isom}(S^3)\cong SU(2)_L\times SU(2)_R.
\]

Mais precisamente:

\[
\boxed{
\operatorname{Isom}^+(S^3)\simeq SO(4)
\simeq
\frac{SU(2)_L\times SU(2)_R}{\mathbb Z_2}.
}
\]

Isso fornece uma estrutura \(SU(2)_L\times SU(2)_R\) possível, mas não seleciona
sozinho:

\[
SU(2)_L
\]

nem a hipercarga \(U(1)_Y\).

A seleção quiral precisa ser demonstrada por um operador quiral, índice,
condição de bordo, torção ou projeção efetiva. Ela não pode ser apenas
declarada.

---

## 5. Dados algébricos que precisam emergir

O grupo efetivo do Modelo Padrão é:

\[
\boxed{
G_{\rm SM}
=
SU(3)_C\times SU(2)_L\times U(1)_Y
}
\]

ou, globalmente, possivelmente:

\[
\boxed{
G_{\rm SM}^{\rm global}
=
\frac{SU(3)_C\times SU(2)_L\times U(1)_Y}{\Gamma},
\qquad
\Gamma\subseteq\mathbb Z_6.
}
\]

A álgebra de Lie é:

\[
\boxed{
\mathfrak g_{\rm SM}
=
\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1).
}
\]

---

## 6. Geradores e constantes de estrutura

### 6.1 Setor \(SU(3)_C\)

Os geradores fundamentais são:

\[
\boxed{
T_a=\frac{\lambda_a}{2},
\qquad
a=1,\dots,8,
}
\]

onde \(\lambda_a\) são as matrizes de Gell-Mann.

A álgebra fecha como:

\[
\boxed{
[T_a,T_b]=if_{abc}T_c.
}
\]

Aqui \(f_{abc}\) são as constantes de estrutura de \(\mathfrak{su}(3)\).

Os bósons de calibre são:

\[
\boxed{
G_\mu^a,
\qquad a=1,\dots,8.
}
\]

### 6.2 Setor \(SU(2)_L\)

Os geradores fundamentais são:

\[
\boxed{
t_i=\frac{\sigma_i}{2},
\qquad
i=1,2,3,
}
\]

onde \(\sigma_i\) são as matrizes de Pauli.

A álgebra fecha como:

\[
\boxed{
[t_i,t_j]=i\epsilon_{ijk}t_k.
}
\]

Os bósons de calibre são:

\[
\boxed{
W_\mu^i,
\qquad i=1,2,3.
}
\]

### 6.3 Setor \(U(1)_Y\)

O gerador abeliano é a hipercarga:

\[
\boxed{
Y.
}
\]

Como \(U(1)\) é abeliano:

\[
\boxed{
[Y,Y]=0.
}
\]

O bóson de calibre é:

\[
\boxed{
B_\mu.
}
\]

A carga elétrica é:

\[
\boxed{
Q=T_3+Y.
}
\]

---

## 7. Representações e hipercargas mínimas

Para uma geração fermiônica do Modelo Padrão, usando campos de Weyl de mão
esquerda, as representações são:

| Campo | Representação em \(SU(3)_C\times SU(2)_L\) | \(Y\) |
|---|---:|---:|
| \(Q_L=(u_L,d_L)\) | \((3,2)\) | \(1/6\) |
| \(u_R^c\) | \((\bar 3,1)\) | \(-2/3\) |
| \(d_R^c\) | \((\bar 3,1)\) | \(1/3\) |
| \(L_L=(\nu_L,e_L)\) | \((1,2)\) | \(-1/2\) |
| \(e_R^c\) | \((1,1)\) | \(1\) |

Se houver neutrino de mão direita:

| Campo | Representação | \(Y\) |
|---|---:|---:|
| \(\nu_R^c\) | \((1,1)\) | \(0\) |

O Higgs efetivo, se usado no setor de quebra eletrofraca, teria:

| Campo | Representação | \(Y\) |
|---|---:|---:|
| \(H\) | \((1,2)\) | \(1/2\) |

Na GDQ, esses dados não devem ser simplesmente copiados. Eles devem aparecer
como espectro efetivo de modos geométricos/espinoriais:

\[
\boxed{
\ker \slashed D_{B,A}^{+}
\ominus
\ker \slashed D_{B,A}^{-}
\quad
\text{deve produzir essas representações.}
}
\]

---

## 8. Derivada covariante efetiva

Se o setor do Modelo Padrão for recuperado, a derivada covariante efetiva sobre
um campo \(\psi\) deve ter a forma:

\[
\boxed{
D_\mu\psi
=
\left[
\nabla_\mu^{\rm spin}
-ig_sG_\mu^aT_a
-igW_\mu^it_i
-ig'YB_\mu
\right]\psi.
}
\]

O operador de Dirac efetivo da GDQ ficaria:

\[
\boxed{
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-ig_sG_\mu^aT_a
-igW_\mu^it_i
-ig'YB_\mu
\right).
}
\]

Aqui:

- \(B_{\mu\nu\lambda}\) é a torção/Bismut/Cartan efetiva;
- \(G_\mu^a\), \(W_\mu^i\), \(B_\mu\) são conexões de calibre efetivas;
- \(g_s\), \(g\), \(g'\) são acoplamentos efetivos;
- \(T_a,t_i,Y\) atuam no fibrado interno \(E\).

---

## 9. Cancelamento de anomalias

O cancelamento de anomalias é uma restrição obrigatória.

Usando uma geração de Weyl à esquerda, as anomalias relevantes são:

### 9.1 \([SU(3)_C]^2U(1)_Y\)

\[
\boxed{
2\left(\frac16\right)T(3)
+\left(-\frac23\right)T(\bar3)
+\left(\frac13\right)T(\bar3)
=0.
}
\]

Como \(T(3)=T(\bar3)=1/2\):

\[
\frac16-\frac13+\frac16=0.
\]

### 9.2 \([SU(2)_L]^2U(1)_Y\)

\[
\boxed{
3\left(\frac16\right)T(2)
+\left(-\frac12\right)T(2)
=0.
}
\]

Como \(T(2)=1/2\):

\[
\frac14-\frac14=0.
\]

### 9.3 Anomalia gravitacional--hipercarga

\[
\boxed{
6\left(\frac16\right)
+3\left(-\frac23\right)
+3\left(\frac13\right)
+2\left(-\frac12\right)
+1
=0.
}
\]

Isto dá:

\[
1-2+1-1+1=0.
\]

### 9.4 \([U(1)_Y]^3\)

\[
\boxed{
6\left(\frac16\right)^3
+3\left(-\frac23\right)^3
+3\left(\frac13\right)^3
+2\left(-\frac12\right)^3
+1^3
=0.
}
\]

Explicitamente:

\[
\frac1{36}
-\frac89
+\frac19
-\frac14
+1
=0.
\]

### 9.5 Anomalia global de Witten em \(SU(2)\)

O número de dubletos de Weyl de \(SU(2)\) por geração é:

\[
\boxed{
3+1=4.
}
\]

Como é par:

\[
\boxed{
\text{não há anomalia global de Witten.}
}
\]

Essas identidades mostram a consistência do espectro do Modelo Padrão. Mas, na
GDQ, ainda falta provar que esse espectro é produzido pela geometria.

---

## 10. O que a GDQ já fornece para essa rota

A GDQ já fornece alguns ingredientes compatíveis:

1. variedade oficial:

\[
M=\mathbb R^4\times T^4;
\]

2. setor físico Lorentziano \((N,h)\);
3. estrutura spin;
4. operador de Dirac com torção:

\[
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA_\mu^a
\right);
\]

5. quantização de fase por fibrados \(U(1)\);
6. holonomias internas no toro;
7. possibilidade de conexões efetivas em fibrados internos;
8. reconstrução Hilbertiana e energia positiva;
9. estatística fermiônica no setor spinorial.

Isso é suficiente para dizer:

\[
\boxed{
\text{há infraestrutura para um setor gauge efetivo.}
}
\]

Mas ainda não é suficiente para dizer:

\[
\boxed{
\text{o grupo do Modelo Padrão foi derivado.}
}
\]

---

## 11. Rota mínima para fechar a Questão 28 futuramente

Para fechar a Questão 28 como teorema, seria necessário demonstrar os seguintes
passos.

### Passo 1 — Definir o fibrado interno efetivo

Introduzir um fibrado vetorial interno:

\[
\boxed{
E\to N
}
\]

e provar que seu grupo estrutural efetivo reduz para:

\[
\boxed{
G_E
=
SU(3)_C\times SU(2)_L\times U(1)_Y
}
\]

ou para o quociente global correto por \(\Gamma\subseteq\mathbb Z_6\).

### Passo 2 — Derivar a álgebra de gauge

Mostrar que as conexões admissíveis em \(E\) decompõem-se como:

\[
\boxed{
A_\mu
=
G_\mu^aT_a
+W_\mu^it_i
+B_\mu Y.
}
\]

Isto deve vir da geometria/holonomia/automorfismos admissíveis, não de uma
imposição externa.

### Passo 3 — Derivar as representações fermiônicas

Calcular o índice quiral do operador de Dirac--Bismut acoplado:

\[
\boxed{
\slashed D_{B,A}^{+}:
\Gamma(S^+\otimes E)
\longrightarrow
\Gamma(S^-\otimes E).
}
\]

O resultado deve produzir:

\[
\boxed{
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

### Passo 4 — Derivar a hipercarga

Provar que \(Y\) é um caráter geométrico ou classe integral do fibrado:

\[
\boxed{
Y:\;G_E\to U(1),
}
\]

com normalização tal que:

\[
\boxed{
Q=T_3+Y.
}
\]

A hipercarga não pode ser escolhida manualmente.

### Passo 5 — Derivar a quiralidade

Mostrar por que apenas os dubletos de mão esquerda carregam \(SU(2)_L\):

\[
\boxed{
Q_L,L_L\text{ são dubletos de }SU(2)_L,
\qquad
u_R,d_R,e_R\text{ são singletos.}
}
\]

Na GDQ, uma rota possível é usar:

1. orientação complexa;
2. torção de Bismut/Cartan;
3. condições de bordo;
4. índice APS;
5. projeção quiral estável.

Mas isso ainda precisa ser calculado.

### Passo 6 — Provar cancelamento de anomalias

Após obter o espectro, deve-se demonstrar:

\[
\boxed{
I_6(F,R)=0
}
\]

para o polinômio de anomalia efetivo em quatro dimensões físicas.

Isso inclui:

1. ausência de anomalia cúbica de cor no espectro vetorial de \(SU(3)\);
2. \([SU(3)]^2U(1)\);
3. \([SU(2)]^2U(1)\);
4. \([U(1)]^3\);
5. anomalia gravitacional--\(U(1)\);
6. anomalia global de Witten.

### Passo 7 — Acoplamentos

Os acoplamentos efetivos:

\[
\boxed{
g_s,\quad g,\quad g'
}
\]

devem ser extraídos de integrais geométricas, normas de modos ou rigidez dos
fibrados:

\[
\boxed{
\frac1{g_a^2}
\sim
\int_{\mathcal I}
\|\xi_a\|_g^2\,d\mu_g,
}
\]

ou fórmula equivalente.

Sem isso, os acoplamentos permanecem parâmetros efetivos.

---

## 11.5 Adendo — potenciais de Killing e colchete de Poisson

O capítulo `pt-br/31 - Emergência Geométrica das Interações de Calibre.md`
contém um elemento algébrico mais forte do que apenas “vetores de Killing
genéricos”.

Para uma variedade de Kähler, cada vetor de Killing holomorfo \(\xi_A\) pode
ser associado a um potencial de Killing \(P_A\) por:

\[
\boxed{
\partial_aP_A
=
i\,g_{a\bar b}\xi_A^{\bar b}.
}
\]

Com a forma simplética de Kähler, esses potenciais fecham uma álgebra por
colchete de Poisson:

\[
\boxed{
\{P_A,P_B\}_{\rm Poisson}
=
f_{ABC}P_C.
}
\]

Esse ponto deve ser aproveitado. Ele fornece uma rota geométrica para obter os
geradores de \(\mathfrak{su}(3)\) como funções Hamiltonianas no espaço interno,
em vez de simplesmente importar as matrizes de Gell-Mann.

O status correto é:

\[
\boxed{
\text{geradores de um setor } \mathfrak{su}(3)
\text{ via potenciais de Killing: rota presente no manuscrito;}
}
\]

\[
\boxed{
\text{grupo completo }SU(3)_C\times SU(2)_L\times U(1)_Y
\text{ e espectro fermiônico: ainda não derivados.}
}
\]

Resta demonstrar que esses \(P_A\):

1. são globalmente bem definidos no fibrado interno efetivo oficial;
2. possuem exatamente oito geradores independentes no setor de cor;
3. atuam nas representações corretas \(3\), \(\bar3\) e singletos;
4. acoplam-se à conexão física \(A_\mu^A\);
5. são compatíveis com a quiralidade e as hipercargas do setor eletrofraco.

Logo, a pendência “derivar geradores” deve ser refinada: para \(SU(3)\), há uma
proposta explícita por potenciais de Killing; falta elevá-la a construção global
do fibrado e das representações físicas.

---

## 12. O que pode ser aproveitado do texto original

Podem ser aproveitadas como ideias:

1. simetrias de calibre como automorfismos/holonomias internas;
2. conexões efetivas vindas de flutuações geométricas;
3. torção de Cartan como seletor quiral possível;
4. quebra eletrofraca como transição geométrica efetiva;
5. acoplamentos como rigidez/norma de modos internos;
6. uso futuro de índice para quiralidade e anomalias;
7. potenciais de Killing \(P_A\) fechando \(\mathfrak{su}(3)\) por colchete de
   Poisson.

Não devem ser aproveitadas como prova final:

1. a dedução baseada em \(\mathcal M_{\mathbb C}^3\);
2. a identificação direta \(CP^2\Rightarrow SU(3)\);
3. a identificação direta \(S^3\Rightarrow SU(2)_L\);
4. a escolha manual de \(U(1)_Y\);
5. a afirmação de que vetores de Killing bastam para obter todo o Modelo
   Padrão;
6. a afirmação de cancelamento de anomalias sem cálculo do espectro.

---

## 13. Resposta final da Questão 28

A GDQ ainda não derivou completamente:

\[
\boxed{
SU(3)_C\times SU(2)_L\times U(1)_Y.
}
\]

O que existe é uma rota geométrica plausível para recuperar um setor de calibre
efetivo por fibrados internos, holonomia, torção, estrutura spinorial e índice.

O fechamento rigoroso exige demonstrar que o operador efetivo de Dirac--Bismut
acoplado produz exatamente o espectro:

\[
\boxed{
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_1,
}
\]

e que esse espectro cancela todas as anomalias.

Portanto:

\[
\boxed{
\text{Questão 28 não está fechada como teorema.}
}
\]

Mas ela está bem delimitada:

\[
\boxed{
\text{para fechá-la, deve-se derivar o fibrado interno }E,\text{ seu grupo
estrutural, suas representações, hipercargas, quiralidade e anomalias.}
}
\]

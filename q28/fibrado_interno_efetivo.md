# Q28 — Bloco 1 — Fibrado interno efetivo

## 1. Objetivo

A Questão 28 exige explicar como surge:

\[
SU(3)_C\times SU(2)_L\times U(1)_Y.
\]

O objetivo deste bloco não é postular o Modelo Padrão. O objetivo é definir o
fibrado interno efetivo que a GDQ precisa produzir para que o setor de calibre
apareça como limite local.

A base física é o espaço-tempo efetivo:

\[
N.
\]

O fibrado interno é:

\[
\boxed{
E_{\rm int}\to N.
}
\]

O grupo de calibre efetivo deve ser o grupo de automorfismos unitários de
\(E_{\rm int}\) que preservam:

1. métrica Hermitiana interna;
2. orientação complexa;
3. volume/fase global;
4. estrutura spinorial;
5. dados de torção/cola.

Assim:

\[
\boxed{
G_{\rm eff}
=
\operatorname{Aut}_{\rm GDQ}(E_{\rm int}).
}
\]

---

## 2. Separação conceitual

Na GDQ, o grupo de calibre não deve ser lido como simetria fundamental
postulada. Ele deve ser a redundância de descrição dos modos internos.

Portanto:

\[
\boxed{
\text{gauge}=
\text{automorfismo local do fibrado interno que preserva os invariantes físicos.}
}
\]

Isso evita transformar a teoria em uma cópia do Modelo Padrão.

O Modelo Padrão deve aparecer como:

\[
\boxed{
\text{limite efetivo local da GDQ.}
}
\]

---

## 3. Decomposição mínima do fibrado interno

Propomos a decomposição:

\[
\boxed{
E_{\rm int}
=
E_C\oplus E_W\oplus L_Y.
}
\]

Onde:

1. \(E_C\) é o setor cromodinâmico efetivo;
2. \(E_W\) é o setor fraco quiral;
3. \(L_Y\) é uma linha complexa associada à hipercarga.

Essa decomposição é uma decomposição efetiva de modos, não uma nova dimensão
fundamental.

---

## 4. Setor de cor \(E_C\)

O setor de cor é associado à trimodalidade bariônica:

\[
n_B=3.
\]

Localmente, os três estômatos/folhas/câmaras definem um espaço interno:

\[
E_C\simeq\mathbb C^3.
\]

A escolha de base em \(\mathbb C^3\) não é observável. O que é observável é a
classe geométrica global do sóliton. Portanto, há uma liberdade unitária local:

\[
U(3).
\]

A fase \(U(1)\) comum já pertence ao setor de fase/hipercarga e à normalização
global. Ao impor preservação de volume complexo:

\[
\det U_C=1,
\]

resta:

\[
\boxed{
G_C=SU(3).
}
\]

Assim, \(SU(3)_C\) aparece como grupo de automorfismos unitários de base das
três câmaras internas que preserva volume e orientação.

Importante:

\[
\boxed{
\text{as três componentes não são quarks pontuais fundamentais;}
}
\]

elas são modos internos de uma estrutura solitônica. A linguagem de cor surge
como redundância de frame interno.

---

## 5. Geradores de \(SU(3)\)

No nível algébrico, os geradores podem ser descritos de duas formas
equivalentes.

### 5.1 Forma matricial local

Escolhendo uma trivialização local:

\[
T_a=\frac{\lambda_a}{2},
\qquad a=1,\dots,8,
\]

com:

\[
[T_a,T_b]=if_{abc}T_c.
\]

Essa é a forma local efetiva.

### 5.2 Forma geométrica por potenciais de Killing

No espaço interno Kähler, cada vetor de Killing holomorfo \(\xi_A\) define um
potencial de Killing \(P_A\):

\[
\partial_aP_A
=
i\,g_{a\bar b}\xi_A^{\bar b}.
\]

Com a forma simplética de Kähler:

\[
\boxed{
\{P_A,P_B\}_{\rm Poisson}
=
f_{ABC}P_C.
}
\]

Essa é a versão geométrica dos geradores de cor. As matrizes de Gell-Mann são
a representação local desses Hamiltonianos internos.

---

## 6. Setor fraco \(E_W\)

O setor fraco deve ser quiral.

O candidato geométrico natural é um fibrado de posto 2 associado à dupla
orientação estável da circulação de Hopf/spin:

\[
E_W\simeq\mathbb C^2.
\]

Automorfismos unitários locais dariam:

\[
U(2).
\]

Separando a fase abeliana para \(L_Y\), a parte especial é:

\[
\boxed{
G_W=SU(2).
}
\]

A seleção de mão esquerda deve vir da estrutura de torção/orientação complexa.
Define-se um projetor quiral efetivo:

\[
\boxed{
P_L=\frac12(1-\Gamma_{\rm GDQ}),
}
\]

onde \(\Gamma_{\rm GDQ}\) é o operador de orientação quiral induzido pela
estrutura spinorial, torção de Bismut e condição causal de Sudarshan.

Então:

\[
\boxed{
SU(2)_L
\text{ atua em }P_LE_{\rm int}.
}
\]

E:

\[
\boxed{
P_RE_{\rm int}
\text{ é singlete de }SU(2)_L.
}
\]

Essa é a condição geométrica mínima para reproduzir a quiralidade fraca.

---

## 7. Linha de hipercarga \(L_Y\)

A hipercarga deve vir de uma linha complexa:

\[
\boxed{
L_Y\to N.
}
\]

Seu grupo estrutural é:

\[
U(1)_Y.
\]

O gerador \(Y\) deve ser a classe integral da conexão dessa linha:

\[
\boxed{
\frac{1}{2\pi}\int_{\Sigma}F_Y\in\mathbb Z.
}
\]

As hipercargas fracionárias observadas devem aparecer por normalização global
do quociente do grupo total, não por escolha arbitrária.

O grupo global correto esperado é:

\[
\boxed{
G_{\rm SM}^{\rm global}
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

Essa estrutura permite que cargas fracionárias sejam compatíveis com
representações globais bem definidas.

---

## 8. Grupo efetivo resultante

Com as três reduções:

\[
U(3)\to SU(3)_C,
\]

\[
U(2)\to SU(2)_L,
\]

\[
U(1)\to U(1)_Y,
\]

obtemos:

\[
\boxed{
G_{\rm eff}
=
SU(3)_C\times SU(2)_L\times U(1)_Y
}
\]

ou globalmente:

\[
\boxed{
G_{\rm eff}^{\rm global}
=
\frac{
SU(3)_C\times SU(2)_L\times U(1)_Y
}{
\Gamma
}.
}
\]

---

## 9. Conexão efetiva

Uma conexão em \(E_{\rm int}\) decompõe-se como:

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

A derivada covariante efetiva é:

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

Na GDQ, os campos \(G_\mu^a,W_\mu^i,B_\mu\) são componentes de conexão
efetiva associadas aos automorfismos internos, não campos postulados
independentemente.

---

## 10. Acoplamentos como normas geométricas

Os acoplamentos devem vir de normas cinéticas dos modos internos:

\[
\boxed{
\frac1{g_a^2}
=
\mathcal N_a
\int_{\mathcal I}
\langle \xi_a,\xi_a\rangle_g\,d\mu_g.
}
\]

Ou, na forma de potenciais de Killing:

\[
\boxed{
\frac1{g_a^2}
=
\mathcal N_a
\int_{\mathcal I}
P_a^2\,d\mu_g.
}
\]

Aqui \(\mathcal N_a\) é normalização fixada pela ação oficial e pela
normalização dos geradores.

Status:

\[
\boxed{
\text{fórmula estrutural definida; valores numéricos ainda dependem da métrica interna estacionária.}
}
\]

---

## 11. O que este bloco resolve

Este bloco resolve a primeira falta da Q28:

\[
\boxed{
\text{definir o fibrado interno efetivo }E_{\rm int}\to N.
}
\]

Também fornece uma rota não postulada para:

1. \(SU(3)_C\) como automorfismos de três câmaras internas;
2. \(SU(2)_L\) como automorfismos de um fibrado quiral de posto 2;
3. \(U(1)_Y\) como linha complexa de hipercarga;
4. geradores de \(SU(3)\) via potenciais de Killing;
5. bósons de calibre como componentes de conexão efetiva;
6. acoplamentos como normas/rigidezes de modos internos.

---

## 12. O que ainda falta

Para fechar Q28 completamente, ainda faltam:

1. derivar o espectro fermiônico como índice de Dirac--Bismut;
2. derivar as hipercargas;
3. provar a seleção quiral \(SU(2)_L\);
4. demonstrar cancelamento de anomalias a partir do espectro derivado;
5. determinar os acoplamentos \(g_s,g,g'\) pela métrica interna.

Status:

\[
\boxed{
\text{Bloco 1 fechado; Q28 ainda depende de espectro, hipercargas e anomalias.}
}

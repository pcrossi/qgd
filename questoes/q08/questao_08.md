# Questão 8 — Como a causalidade é preservada?

## 1. Pergunta

A Questão 8 pergunta:

\[
\boxed{
\text{como a causalidade é preservada na GDQ?}
}
\]

As exigências são:

1. definir o cone causal;
2. definir propagadores retardado, avançado e de Feynman;
3. explicar por que a combinação avançado-retardado de Sudarshan não permite
   sinalização para o passado;
4. mostrar o comportamento dos comutadores de observáveis espacialmente
   separados;
5. explicar escolha retardada sem retrocausalidade observável.

O critério de fechamento é:

\[
\boxed{
\text{microcausalidade ou alternativa operacional compatível com no-signalling.}
}
\]

---

## 2. Cone causal

A causalidade física da GDQ é definida na camada efetiva \(N^4\), com métrica
lorentziana:

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
}
\]

O cone causal em \(p\in N\) é:

\[
\boxed{
\mathcal C_h(p)
=
\{v\in T_pN:h_p(v,v)\le0\}.
}
\]

Vetores nulos satisfazem:

\[
\boxed{
h_p(v,v)=0.
}
\]

Vetores temporais satisfazem:

\[
\boxed{
h_p(v,v)<0.
}
\]

No setor plano:

\[
\boxed{
h=-dt^2+d\mathbf x^2.
}
\]

Logo:

\[
h(v,v)
=
-(v^0)^2+|\mathbf v|^2.
\]

Assim:

\[
\boxed{
h(v,v)\le0
\Longleftrightarrow
|\mathbf v|\le |v^0|.
}
\]

Em unidades com \(c=1\), isso é o cone de luz usual.

---

## 3. Cone comum dos campos

A causalidade não é definida por cada campo separadamente, mas pelo símbolo
principal comum das equações efetivas.

Para campos escalares, gauge, torção e gravidade linearizada, o símbolo
principal é:

\[
\boxed{
h^{\mu\nu}k_\mu k_\nu.
}
\]

Para espinores:

\[
\boxed{
(\gamma^\mu k_\mu)^2
=
h^{\mu\nu}k_\mu k_\nu.
}
\]

Portanto:

\[
\boxed{
\text{matéria escalar, torção, gauge, gravidade e espinores compartilham o
cone causal de }h.
}
\]

Consequência:

\[
\boxed{
\text{a velocidade frontal é determinada pelo cone de }h.
}
\]

A velocidade de grupo de aproximações hidrodinâmicas truncadas, como termos
\(k^4\), não deve ser usada para definir causalidade no ultravioleta.

---

## 4. Operador hiperbólico efetivo

Seja \(P_h\) um operador hiperbólico efetivo com símbolo principal:

\[
\sigma(P_h)(x,k)=h^{\mu\nu}(x)k_\mu k_\nu.
\]

Para um campo escalar massivo, por exemplo:

\[
\boxed{
P_h
=
\Box_h+m^2+\cdots
}
\]

onde os termos adicionais são de menor ordem ou acoplamentos que não alteram o
cone principal.

Os propagadores fundamentais são definidos a partir de:

\[
\boxed{
P_hG(x,y)=\delta_h(x,y).
}
\]

---

## 5. Propagador retardado

O propagador retardado satisfaz:

\[
\boxed{
P_hG_{\rm ret}(x,y)=\delta_h(x,y).
}
\]

com suporte:

\[
\boxed{
\operatorname{supp}G_{\rm ret}(\cdot,y)
\subset
J_h^+(y).
}
\]

Ou seja, uma fonte em \(y\) só influencia \(x\) se:

\[
\boxed{
x\in J_h^+(y).
}
\]

Este é o propagador de resposta física causal.

Se uma fonte externa local \(J\) é ligada em uma região \(O\), a resposta
linear em um observável de campo tem a forma:

\[
\boxed{
\delta\Phi(x)
=
\int_NG_{\rm ret}(x,y)J(y)\,dV_h(y).
}
\]

Portanto:

\[
\boxed{
x\notin J_h^+(O)
\Longrightarrow
\delta\Phi(x)=0.
}
\]

---

## 6. Propagador avançado

O propagador avançado satisfaz:

\[
\boxed{
P_hG_{\rm adv}(x,y)=\delta_h(x,y).
}
\]

com suporte:

\[
\boxed{
\operatorname{supp}G_{\rm adv}(\cdot,y)
\subset
J_h^-(y).
}
\]

Ele é matematicamente legítimo e aparece na decomposição global de contorno.

Mas, na GDQ final, ele não é interpretado como canal livre de envio de
mensagens para o passado.

A interpretação correta é:

\[
\boxed{
G_{\rm adv}
\text{ codifica restrição global de contorno/fase, não sinal físico
controlável.}
}
\]

---

## 7. Propagador de Feynman

O propagador de Feynman é:

\[
\boxed{
G_F(x,y)
=
\langle\Omega|
T\{\Phi(x)\Phi(y)\}
|\Omega\rangle.
}
\]

No setor plano:

\[
\boxed{
G_F(k)
=
\frac{i}{k_h^2-m^2+i\varepsilon},
}
\]

com:

\[
k_h^2=h^{\mu\nu}k_\mu k_\nu.
\]

Esse propagador organiza amplitudes perturbativas e ordenamento temporal, mas
não altera o cone causal operacional.

---

## 8. Propagador de Pauli--Jordan e comutador

Define-se:

\[
\boxed{
\Delta(x,y)
=
G_{\rm ret}(x,y)-G_{\rm adv}(x,y).
}
\]

Para campo escalar:

\[
\boxed{
[\Phi(x),\Phi(y)]
=
i\hbar\,\Delta(x,y).
}
\]

Como:

\[
\operatorname{supp}\Delta
\subset
J_h^+(y)\cup J_h^-(y),
\]

temos, se \(x\) e \(y\) são separados espacialmente:

\[
x\perp_h y
\Longrightarrow
\Delta(x,y)=0.
\]

Logo:

\[
\boxed{
x\perp_h y
\Longrightarrow
[\Phi(x),\Phi(y)]=0.
}
\]

Essa é a microcausalidade.

Para observáveis locais gerais:

\[
\boxed{
O_1\perp_h O_2
\Longrightarrow
[\mathcal A(O_1),\mathcal A(O_2)]=0.
}
\]

---

## 9. Propagador simétrico de Sudarshan

A GDQ usa a prescrição:

\[
\boxed{
G_{\rm sym}
=
\frac12
\left(
G_{\rm ret}
+G_{\rm adv}
\right).
}
\]

Esse objeto deve ser entendido corretamente.

Ele não é o propagador de sinal físico controlável.

Ele é:

\[
\boxed{
\text{a parte simétrica/global/de contorno da solução.}
}
\]

Sua função é:

1. impor fechamento causal global;
2. selecionar polos físicos;
3. cancelar termos exatos de fronteira;
4. representar o balanço avançado-retardado;
5. fixar a solução admissível da fase/holonomia.

Mas a resposta operacional a uma fonte local controlável é retardada:

\[
\boxed{
\delta\langle\mathcal O(x)\rangle
\sim
\int G_{\rm ret}(x,y)J(y)dV_y.
}
\]

Portanto, a parte avançada não pode ser usada para enviar mensagens ao passado.

---

## 10. Por que metade avançado + metade retardado não sinaliza para o passado?

A resposta é:

\[
\boxed{
\text{porque a parte avançada não é grau de liberdade operacional
controlável por um agente.}
}
\]

Ela é determinada por:

1. condições globais de contorno;
2. fechamento do contorno \(\gamma\);
3. quantização/filtro de estabilidade;
4. consistência da solução;
5. projeção aos polos físicos;
6. estado global do experimento.

Um agente pode escolher uma intervenção local \(J\) ou uma operação de medição
em uma região. A influência física controlável dessa intervenção é governada
por:

\[
G_{\rm ret}.
\]

Não por \(G_{\rm adv}\).

Portanto:

\[
\boxed{
G_{\rm adv}
\text{ entra como restrição de consistência, não como transmissor de bits.}
}
\]

---

## 11. Demonstração operacional de no-signalling

Sejam \(O_A\) e \(O_B\) regiões espacialmente separadas:

\[
O_A\perp_h O_B.
\]

Então:

\[
[\mathcal A(O_A),\mathcal A(O_B)]=0.
\]

Considere uma operação local não seletiva em \(O_B\), descrita por operadores
de Kraus \(M_\alpha\in\mathcal A(O_B)\):

\[
\sum_\alpha M_\alpha^\dagger M_\alpha=1.
\]

Para um observável \(A\in\mathcal A(O_A)\), a estatística após a operação em
\(O_B\) é:

\[
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
\left(
M_\alpha\rho M_\alpha^\dagger A
\right).
\]

Como:

\[
[A,M_\alpha]=0,
\]

temos:

\[
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
\left(
\rho M_\alpha^\dagger A M_\alpha
\right)
=
\sum_\alpha
\operatorname{Tr}
\left(
\rho A M_\alpha^\dagger M_\alpha
\right).
\]

Usando:

\[
\sum_\alpha M_\alpha^\dagger M_\alpha=1,
\]

segue:

\[
\boxed{
\langle A\rangle'
=
\operatorname{Tr}(\rho A)
=
\langle A\rangle.
}
\]

Logo, operações locais em \(O_B\) não alteram estatísticas locais em \(O_A\).

Portanto:

\[
\boxed{
\text{a GDQ preserva no-signalling.}
}
\]

---

## 12. Escolha retardada sem Copenhague clássico

A escolha retardada é resolvida sem o malabarismo clássico de Copenhague.

Não é necessário dizer que:

1. a partícula “decidiu retroativamente” por qual caminho passou;
2. o observador colapsou magicamente o passado;
3. houve envio de informação para trás no tempo.

Na GDQ, a leitura correta é:

\[
\boxed{
\text{a escolha retardada altera a condição de contorno global do experimento,
não o passado observável local.}
}
\]

O arranjo experimental completo define uma solução global admissível para a
fase, a densidade e a holonomia.

A prescrição de Sudarshan:

\[
G_{\rm sym}
=
\frac12(G_{\rm ret}+G_{\rm adv})
\]

entra como fechamento avançado-retardado da solução global.

Mas os registros locais continuam obedecendo:

\[
\boxed{
\text{nenhum agente consegue modular uma mensagem para o passado.}
}
\]

---

## 13. Marginais locais e escolha tardia

Se \(x\) é uma escolha/preparação local inicial e \(y\) é uma escolha tardia do
arranjo de medição, a condição operacional de no-signalling é:

\[
\boxed{
P(a|x,y)=P(a|x,y')
}
\]

sempre que a escolha \(y\) não pertence ao passado causal de \(a\).

Equivalente:

\[
\boxed{
\sum_bP(a,b|x,y)
=
\sum_bP(a,b|x,y').
}
\]

O que pode mudar com \(y\) são as correlações finais:

\[
P(a,b|x,y).
\]

Mas a marginal local:

\[
P(a|x)
\]

não carrega mensagem sobre \(y\).

Portanto:

\[
\boxed{
\text{a escolha retardada muda o contexto global de correlação, não uma
estatística local acessível no passado.}
}
\]

---

## 14. Leitura correta do Apêndice 9 e da dupla fenda

O Apêndice 9 e o capítulo da dupla fenda podem ser aproveitados com a seguinte
correção conceitual.

Onde o texto diz que a componente avançada “retropropaga” ou que a escolha
tardia “altera o percurso anterior”, deve-se ler:

\[
\boxed{
\text{a solução global de contorno é recalculada como um todo, mas não há
sinal físico controlável para o passado.}
}
\]

O detector tardio altera o conjunto de condições de contorno. A solução
admissível resultante pode ter:

1. padrão interferométrico;
2. padrão de caminho;
3. decoerência geométrica;
4. amortecimento do termo cruzado;
5. transição de correlação.

Mas os dados locais antes da comparação clássica não permitem inferir uma
mensagem enviada pela escolha futura.

Assim, a escolha retardada é:

\[
\boxed{
\text{condição de contorno global + no-signalling local.}
}
\]

---

## 15. Decoerência geométrica e perda de interferência

No capítulo da dupla fenda, a densidade coerente é:

\[
\rho_{\rm total}
=
R_1^2+R_2^2
+2R_1R_2
\cos\left(\frac{S_1-S_2}{\hbar}\right).
\]

O detector introduz uma impedância/decoerência geométrica que amortece o termo
cruzado:

\[
\boxed{
\rho_{\rm total}
\longrightarrow
R_1^2+R_2^2
+2R_1R_2D
\cos\left(\frac{S_1-S_2}{\hbar}\right),
}
\]

com:

\[
0\le D\le1.
\]

No regime coerente:

\[
D=1.
\]

No regime com informação de caminho:

\[
D\to0.
\]

Então:

\[
\boxed{
\rho_{\rm total}
\to
R_1^2+R_2^2.
}
\]

Essa é a transição física sem colapso mágico: a interferência desaparece
porque o termo de coerência é suprimido pela condição de medição/decoerência.

---

## 16. Compatibilidade com microcausalidade

Mesmo que a solução global use \(G_{\rm sym}\), os observáveis locais obedecem:

\[
\boxed{
[\mathcal O_1(x),\mathcal O_2(y)]=0
\quad
\text{se}
\quad
x\perp_h y.
}
\]

Isso garante:

1. nenhuma mensagem superluminal;
2. nenhuma mensagem para o passado;
3. compatibilidade com relatividade operacional;
4. consistência com o Hamiltoniano positivo da Questão 7;
5. compatibilidade com o cone de \(h\) da Questão 2.

---

## 17. Resposta às perguntas obrigatórias

### 17.1 Qual é o cone causal?

O cone causal é:

\[
\boxed{
\mathcal C_h(p)=\{v\in T_pN:h_p(v,v)\le0\}.
}
\]

No setor plano:

\[
\boxed{
h=-dt^2+d\mathbf x^2.
}
\]

### 17.2 Quais são os propagadores retardado, avançado e de Feynman?

Retardado:

\[
\boxed{
P_hG_{\rm ret}=\delta_h,
\qquad
\operatorname{supp}G_{\rm ret}(\cdot,y)\subset J_h^+(y).
}
\]

Avançado:

\[
\boxed{
P_hG_{\rm adv}=\delta_h,
\qquad
\operatorname{supp}G_{\rm adv}(\cdot,y)\subset J_h^-(y).
}
\]

Feynman:

\[
\boxed{
G_F(x,y)
=
\langle\Omega|T\{\Phi(x)\Phi(y)\}|\Omega\rangle.
}
\]

No plano:

\[
\boxed{
G_F(k)=\frac{i}{k_h^2-m^2+i\varepsilon}.
}
\]

Sudarshan:

\[
\boxed{
G_{\rm sym}
=
\frac12(G_{\rm ret}+G_{\rm adv}).
}
\]

### 17.3 Por que metade avançado e metade retardado não permite sinalização para o passado?

Porque:

\[
\boxed{
G_{\rm adv}
\text{ não é grau de liberdade operacional controlável.}
}
\]

Ele é restrição global de contorno/fase. A resposta física a fontes locais é
governada por \(G_{\rm ret}\).

Além disso:

\[
\boxed{
[\mathcal A(O_A),\mathcal A(O_B)]=0
\quad
\text{para}
\quad
O_A\perp_hO_B.
}
\]

Logo, operações locais em \(O_B\) não alteram estatísticas locais em \(O_A\).

### 17.4 Como comutadores separados espacialmente se comportam?

Para campo escalar:

\[
\boxed{
[\Phi(x),\Phi(y)]
=
i\hbar
\left(
G_{\rm ret}(x,y)-G_{\rm adv}(x,y)
\right).
}
\]

Se:

\[
x\perp_h y,
\]

então:

\[
\boxed{
[\Phi(x),\Phi(y)]=0.
}
\]

Para observáveis locais:

\[
\boxed{
[\mathcal O_1(x),\mathcal O_2(y)]=0
\quad
\text{quando}
\quad
x\perp_hy.
}
\]

### 17.5 Como o modelo trata escolha retardada sem retrocausalidade observável?

O modelo trata escolha retardada como:

\[
\boxed{
\text{mudança de condição de contorno global do experimento.}
}
\]

Essa mudança pode alterar correlações finais:

\[
P(a,b|x,y),
\]

mas não altera marginais locais anteriores:

\[
\boxed{
P(a|x,y)=P(a|x,y').
}
\]

Portanto:

\[
\boxed{
\text{há solução global avançada-retardada, mas não há sinalização para o
passado.}
}
\]

---

## 18. Consequência lógica

A causalidade da GDQ é preservada em três níveis.

### 18.1 Nível geométrico

\[
\boxed{
\text{o cone causal é o cone de }h.
}
\]

### 18.2 Nível algébrico

\[
\boxed{
O_A\perp_hO_B
\Longrightarrow
[\mathcal A(O_A),\mathcal A(O_B)]=0.
}
\]

### 18.3 Nível operacional

\[
\boxed{
\text{operações locais não alteram marginais em regiões espacialmente
separadas.}
}
\]

Assim:

\[
\boxed{
\text{microcausalidade}
\Longrightarrow
\text{no-signalling}.
}
\]

---

## 19. Status da Questão 8

\[
\boxed{
\text{Questão 8 fechada oficialmente.}
}
\]

A resposta final é:

\[
\boxed{
\text{a causalidade é preservada porque a propagação física segue o cone de
}h,
\text{ os comutadores locais somem fora desse cone, e a parte avançada de
Sudarshan é uma restrição global sem canal operacional de sinalização.}
}
\]

A escolha retardada é resolvida sem Copenhague clássico:

\[
\boxed{
\text{ela é mudança de condição de contorno global + no-signalling local,
não colapso retroativo do passado.}
}


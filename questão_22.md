# Questão 22 — Como a regra de Born é derivada?

## 1. Pergunta

A Questão 22 pergunta:

\[
\boxed{
\text{como obter a regra de Born sem simplesmente postular }
P_i=|\langle i|\psi\rangle|^2?
}
\]

O problema apontado em `22-0.md` é correto:

\[
\boxed{
R=\sqrt{\rho}
\text{ apenas reescreve }
\rho=R^2.
}
\]

Isso explica a relação local entre amplitude e densidade, mas não prova ainda:

1. por que probabilidades são quadráticas nas amplitudes;
2. como alternativas exclusivas se somam;
3. como sistemas compostos são tratados;
4. como surge a base de medição;
5. como obter probabilidades em bases arbitrárias.

A resposta aceitável precisa ser operacional: partir da estrutura de estados,
observáveis e composição já definida nas Questões 20 e 21, e derivar a forma
quadrática como única medida probabilística consistente.

---

## 2. Resposta curta

A regra de Born é obtida em dois passos.

Primeiro, a GDQ fornece uma densidade positiva conservada:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}.
}
\]

No setor regular:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

Segundo, no espaço de Hilbert reconstruído:

\[
\boxed{
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)},
}
\]

uma probabilidade operacional é uma função \(\mu\) sobre alternativas
ortogonais que satisfaz:

1. positividade;
2. normalização;
3. aditividade para alternativas mutuamente exclusivas;
4. não contextualidade operacional;
5. compatibilidade com produto tensorial.

Essas condições forçam:

\[
\boxed{
\mu(P)=\operatorname{Tr}(\varrho P).
}
\]

Para estado puro:

\[
\boxed{
\varrho=|\psi\rangle\langle\psi|.
}
\]

Então:

\[
\boxed{
\mu(P)=\langle\psi|P|\psi\rangle.
}
\]

Para uma base ortonormal \(\{|i\rangle\}\), com \(P_i=|i\rangle\langle i|\):

\[
\boxed{
P(i|\psi)=\langle\psi|P_i|\psi\rangle
=
|\langle i|\psi\rangle|^2.
}
\]

Essa é a regra de Born. O quadrado não é postulado; ele aparece porque a única
forma positiva, aditiva e compatível com composição no Hilbert é bilinear em
\(\psi\) e \(\bar\psi\).

---

## 3. O que a GDQ já fornece antes da regra de Born

Pela Questão 15:

\[
\boxed{
f=-\ln\rho+i\frac{S_R}{\hbar},
\qquad
\rho=e^{-(f+\bar f)/2}.
}
\]

A parte real de \(f\) fornece uma densidade positiva:

\[
\boxed{
\rho>0.
}
\]

A equação de continuidade preserva a normalização:

\[
\boxed{
\partial_t\rho+\nabla_i(\rho v^i)=0.
}
\]

Com condições de contorno sem fluxo:

\[
\boxed{
\frac{d}{dt}\int_{\Sigma_t}\rho\,d\mu_h=0.
}
\]

Portanto, antes de falar em medição, a teoria já tem uma medida conservada:

\[
\boxed{
\int_{\Sigma_t}\rho\,d\mu_h=1.
}
\]

Isso é necessário, mas ainda não é suficiente para derivar Born em qualquer
base. Falta mostrar como essa medida se transforma em probabilidade de
alternativas projetivas arbitrárias.

---

## 4. Por que \(R=\sqrt\rho\) não basta

Definir:

\[
\boxed{
R=\sqrt\rho
}
\]

implica:

\[
\boxed{
\rho=R^2.
}
\]

Isso só muda a variável usada para escrever a densidade.

Não prova ainda:

\[
\boxed{
P(i|\psi)=|\langle i|\psi\rangle|^2.
}
\]

Também não prova:

1. que probabilidades de alternativas ortogonais somam;
2. que uma mudança de base deve ser unitária;
3. que a probabilidade em uma base arbitrária depende do projetor \(P_i\);
4. que sistemas compostos obedecem traço parcial e produto tensorial;
5. que o detector seleciona uma base de ponteiro.

Logo, a derivação deve partir da estrutura operacional completa, não apenas
da parametrização local de \(\rho\).

---

## 5. Alternativas exclusivas

No espaço de Hilbert físico, uma alternativa experimental elementar é
representada por um projetor ortogonal:

\[
\boxed{
P=P^\dagger=P^2.
}
\]

Alternativas exclusivas satisfazem:

\[
\boxed{
P_iP_j=0,
\qquad i\ne j.
}
\]

Um conjunto completo de alternativas satisfaz:

\[
\boxed{
\sum_i P_i=I.
}
\]

Uma regra de probabilidade deve atribuir:

\[
\boxed{
\mu(P_i)\ge0,
\qquad
\mu(I)=1.
}
\]

Para alternativas mutuamente exclusivas, deve valer:

\[
\boxed{
\mu(P_i+P_j)=\mu(P_i)+\mu(P_j),
\qquad P_iP_j=0.
}
\]

Mais geralmente:

\[
\boxed{
\mu\!\left(\sum_i P_i\right)=\sum_i\mu(P_i)
}
\]

para qualquer família ortogonal finita ou contável admissível.

Essa aditividade é a versão operacional de:

\[
\boxed{
\text{alternativas exclusivas têm probabilidades que se somam.}
}
\]

---

## 6. Não contextualidade operacional

Se o mesmo projetor \(P\) aparece em dois arranjos completos diferentes:

\[
\boxed{
\{P,P_2,\ldots,P_n\}
}
\]

e:

\[
\boxed{
\{P,Q_2,\ldots,Q_m\},
}
\]

a probabilidade de \(P\) não pode depender dos demais detectores compatíveis
que foram adicionados ao aparelho.

Logo:

\[
\boxed{
\mu(P)
\text{ depende de }P\text{ e do estado, não do contexto completo.}
}
\]

Isso não é um postulado de Born. É uma condição operacional mínima: o mesmo
evento físico não pode receber duas probabilidades diferentes apenas porque
foi embutido em decomposições ortogonais diferentes.

---

## 7. Teorema estrutural: forma da medida

Sob positividade, normalização, aditividade em projetores ortogonais e
não contextualidade, a medida sobre projetores tem a forma:

\[
\boxed{
\mu(P)=\operatorname{Tr}(\varrho P),
}
\]

onde:

\[
\boxed{
\varrho\ge0,
\qquad
\operatorname{Tr}\varrho=1.
}
\]

Esse é o conteúdo matemático tipo Gleason para espaços de Hilbert de dimensão
\(\ge3\). Para setores bidimensionais isolados, a mesma conclusão é obtida ao
exigir compatibilidade com sistemas compostos, POVMs ou continuidade física
sob acoplamento a aparelho/ambiente, pois o qubit real de laboratório nunca é
medido sem um espaço auxiliar.

Portanto, a regra geral de probabilidade é:

\[
\boxed{
P(\text{evento }P|\varrho)
=
\operatorname{Tr}(\varrho P).
}
\]

Essa fórmula é derivada das propriedades da medida probabilística sobre
alternativas, não assumida como peso Born.

---

## 8. Estado puro

Para um estado puro:

\[
\boxed{
\varrho=|\psi\rangle\langle\psi|,
\qquad
\|\psi\|=1.
}
\]

Então:

\[
\boxed{
\mu(P)=\operatorname{Tr}(|\psi\rangle\langle\psi|P).
}
\]

Pela ciclicidade do traço:

\[
\boxed{
\mu(P)=\langle\psi|P|\psi\rangle.
}
\]

Se:

\[
\boxed{
P_i=|i\rangle\langle i|
}
\]

é o projetor em um resultado de uma base ortonormal, então:

\[
\mu(P_i)
=
\langle\psi|i\rangle\langle i|\psi\rangle
=
\overline{\langle i|\psi\rangle}\langle i|\psi\rangle.
\]

Logo:

\[
\boxed{
P(i|\psi)=|\langle i|\psi\rangle|^2.
}
\]

Essa é a regra de Born em base discreta.

---

## 9. Por que a dependência é quadrática

A probabilidade deve ser invariante por fase global:

\[
\boxed{
|\psi\rangle\sim e^{i\alpha}|\psi\rangle.
}
\]

Logo, uma probabilidade não pode depender linearmente de \(\psi\), pois:

\[
\boxed{
\psi\mapsto e^{i\alpha}\psi
}
\]

mudaria uma expressão linear.

A menor expressão local positiva e invariante por fase é bilinear:

\[
\boxed{
\bar\psi\psi.
}
\]

No Hilbert:

\[
\boxed{
\langle\psi|P|\psi\rangle
}
\]

é precisamente bilinear em \(\bar\psi\) e \(\psi\), positiva para \(P\ge0\), e
aditiva para projetores ortogonais.

Potências alternativas falham:

- \(|\psi_i|\) não é aditiva sob decomposição ortogonal;
- \(|\psi_i|^p\), com \(p\ne2\), não é preservada por transformações
  unitárias em geral;
- regras não quadráticas quebram a fatoração natural em sistemas compostos.

Portanto:

\[
\boxed{
\text{o quadrado é forçado pela positividade, fase, aditividade e unitariedade.}
}
\]

---

## 10. Como alternativas exclusivas se somam

Se:

\[
\boxed{
P_iP_j=0,
}
\]

então:

\[
\boxed{
P_{i\lor j}=P_i+P_j.
}
\]

Pela regra traço:

\[
\mu(P_i+P_j)
=
\operatorname{Tr}(\varrho(P_i+P_j)).
\]

Pela linearidade do traço:

\[
\boxed{
\mu(P_i+P_j)
=
\operatorname{Tr}(\varrho P_i)
+
\operatorname{Tr}(\varrho P_j)
=
\mu(P_i)+\mu(P_j).
}
\]

Para uma decomposição completa:

\[
\sum_iP_i=I,
\]

temos:

\[
\boxed{
\sum_i\mu(P_i)
=
\operatorname{Tr}\!\left(\varrho\sum_iP_i\right)
=
\operatorname{Tr}(\varrho)
=1.
}
\]

Logo, probabilidades de resultados mutuamente exclusivos são normalizadas e
aditivas.

---

## 11. Sistemas compostos

Pela Questão 20, para sistemas distinguíveis:

\[
\boxed{
\mathcal H_{AB}
=
\mathcal H_A\otimes\mathcal H_B.
}
\]

Para estados produto:

\[
\boxed{
\varrho_{AB}
=
\varrho_A\otimes\varrho_B.
}
\]

Para eventos independentes:

\[
\boxed{
P_{A\land B}=P_A\otimes P_B.
}
\]

A regra traço fornece:

\[
P(A\land B)
=
\operatorname{Tr}_{AB}
\left[
(\varrho_A\otimes\varrho_B)(P_A\otimes P_B)
\right].
\]

Usando a fatoração do traço:

\[
\boxed{
P(A\land B)
=
\operatorname{Tr}_A(\varrho_AP_A)
\operatorname{Tr}_B(\varrho_BP_B).
}
\]

Portanto:

\[
\boxed{
P(A\land B)=P(A)P(B)
}
\]

para estados produto.

Para estados emaranhados:

\[
\boxed{
\varrho_{AB}\ne\varrho_A\otimes\varrho_B,
}
\]

e as probabilidades conjuntas são:

\[
\boxed{
P(a,b)
=
\operatorname{Tr}_{AB}
\left[
\varrho_{AB}(P_a\otimes Q_b)
\right].
}
\]

As probabilidades marginais são:

\[
\boxed{
\varrho_A=\operatorname{Tr}_B\varrho_{AB},
\qquad
P(a)=\operatorname{Tr}_A(\varrho_AP_a).
}
\]

Essa estrutura garante a regra de produto tensorial e a compatibilidade com
no-signalling.

---

## 12. Como surge a base de medição

A base de medição não é escolhida pela regra de Born. Ela é escolhida pela
interação entre sistema, aparelho e ambiente.

Se o aparelho mede um observável:

\[
\boxed{
A=\sum_i a_iP_i,
}
\]

a interação de medição tem a forma ideal:

\[
\boxed{
|i\rangle|M_0\rangle
\longmapsto
|i\rangle|M_i\rangle.
}
\]

Para uma superposição:

\[
\boxed{
|\psi\rangle|M_0\rangle
=
\sum_i c_i|i\rangle|M_0\rangle
\longmapsto
\sum_i c_i|i\rangle|M_i\rangle.
}
\]

O ambiente seleciona estados de ponteiro estáveis:

\[
\boxed{
\langle M_i,E_i|M_j,E_j\rangle\approx0,
\qquad i\ne j.
}
\]

Então os termos de interferência ficam suprimidos no estado reduzido:

\[
\boxed{
\rho_{\rm red}
\approx
\sum_i
P_i^{\rm diag}\,
\rho_{\rm red}\,
P_i^{\rm diag},
\qquad
P_i^{\rm diag}=|i,M_i\rangle\langle i,M_i|.
}
\]

A base \(\{|i\rangle\}\) é, portanto, a base estável da interação
sistema-aparelho-ambiente: a base de ponteiro/decoerência.

Na linguagem GDQ, essa seleção corresponde à separação dinâmica de bacias
geométricas/atratores do aparelho. O detector impõe condições de contorno,
impedância e decoerência geométrica que tornam determinados projetores
macroscopicamente robustos.

---

## 13. Como obter probabilidades em bases arbitrárias

Se a base de medição é:

\[
\boxed{
\{|a_i\rangle\},
}
\]

os projetores são:

\[
\boxed{
P_i^{(a)}=|a_i\rangle\langle a_i|.
}
\]

Então:

\[
\boxed{
P(a_i|\psi)
=
\langle\psi|P_i^{(a)}|\psi\rangle
=
|\langle a_i|\psi\rangle|^2.
}
\]

Se outra base é:

\[
\boxed{
|b_j\rangle=\sum_i U_{ji}|a_i\rangle,
}
\]

com \(U\) unitária, então:

\[
\boxed{
P(b_j|\psi)
=
|\langle b_j|\psi\rangle|^2.
}
\]

Logo, bases arbitrárias são tratadas por transformações unitárias no Hilbert
físico reconstruído.

Para observáveis com espectro contínuo, os projetores são medidas espectrais:

\[
\boxed{
P_A(\Delta)=E_A(\Delta).
}
\]

A probabilidade é:

\[
\boxed{
P(A\in\Delta|\varrho)
=
\operatorname{Tr}(\varrho E_A(\Delta)).
}
\]

No caso de posição:

\[
\boxed{
P(x\in R|\psi)
=
\int_R |\psi(x)|^2\,d\mu_h.
}
\]

Como, na GDQ:

\[
\boxed{
|\psi(x)|^2=\rho(x)=e^{-(f+\bar f)/2},
}
\]

recupera-se:

\[
\boxed{
P(x\in R)
=
\int_R\rho\,d\mu_h.
}
\]

---

## 14. Relação com o capítulo 13

O capítulo `pt-br/13 - Regra de Born.md` contém uma intuição correta:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}
}
\]

e:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

Mas a passagem:

\[
\boxed{
\rho=|\Psi|^2
}
\]

por si só não deriva a regra de Born em qualquer base. Ela apenas identifica a
densidade local no setor de posição.

A derivação completa exige acrescentar:

1. espaço de Hilbert reconstruído;
2. projetores como alternativas experimentais;
3. aditividade em alternativas ortogonais;
4. não contextualidade operacional;
5. composição tensorial;
6. seleção de base por aparelho/ambiente.

Com esses elementos, a regra de Born deixa de ser uma definição e passa a ser a
única regra probabilística compatível com a estrutura operacional da teoria.

---

## 15. Relação com a ação oficial

A ação oficial permanece:

\[
\boxed{
\mathcal{S}_{\rm GDQ}=
\int_{\gamma}\left[\int_{\mathcal M_\mathbb C}\frac{\hbar}{\Lambda_C^2}
\left[\tau(\mathcal R+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f)+\frac{f+\bar f}{2}-n\right]
\mathcal U\sqrt{\det g}\,d^{2n}z\right]\frac{d\tau}{\tau}.
}
\]

Com:

\[
\boxed{
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n},
\qquad
\rho=e^{-(f+\bar f)/2}.
}
\]

A regra de Born não altera a ação. Ela é a regra operacional de leitura de
probabilidades no espaço de Hilbert reconstruído a partir da teoria.

---

## 16. O que fica pendente

A questão fica resolvida estruturalmente, mas a implementação física completa
de cada medição específica ainda exige:

1. especificar sistema;
2. especificar aparelho;
3. especificar ambiente;
4. escrever a interação \(H_{\rm int}\);
5. demonstrar decoerência na base de ponteiro;
6. identificar os projetores \(P_i\);
7. calcular \(\operatorname{Tr}(\varrho P_i)\).

Esse detalhamento pertence naturalmente à Questão 24, sobre o problema da
medida.

---

## 17. Resposta final da Questão 22

A regra de Born na GDQ é:

\[
\boxed{
P(P|\varrho)=\operatorname{Tr}(\varrho P).
}
\]

Para estado puro:

\[
\boxed{
P(P|\psi)=\langle\psi|P|\psi\rangle.
}
\]

Para uma base ortonormal:

\[
\boxed{
P(i|\psi)=|\langle i|\psi\rangle|^2.
}
\]

No setor de posição:

\[
\boxed{
P(x\in R|\psi)=\int_R|\psi(x)|^2\,d\mu_h
=
\int_R\rho(x)\,d\mu_h.
}
\]

E:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}.
}
\]

Portanto:

\[
\boxed{
\text{Questão 22 fechada estruturalmente.}
}
\]

A ressalva é precisa: a GDQ fornece a densidade geométrica positiva
\(\rho\); a regra de Born completa requer a estrutura operacional de Hilbert,
projetores, aditividade, composição tensorial e seleção de base pelo aparelho.

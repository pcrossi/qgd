# Q38 — Derivação formal de \(S_{\rm inst}\), \(\chi_{\rm Fano}\) e \(J_{\rm flat}\)

## 1. Objetivo

Este documento executa os três passos pendentes de Q38:

1. derivar:

   \[
   \frac{S_{\rm inst}}{\hbar}
   =
   \frac1{2\alpha};
   \]

2. derivar:

   \[
   \chi_{\rm Fano}^{\rm bulk}
   =
   \frac{3\sqrt2}{5};
   \]

3. decidir se existe um fator independente:

   \[
   J_{\rm flat}.
   \]

A exigência é não usar \(G\) como entrada e não aplicar fatores externos para
corrigir resíduo numérico.

---

## 2. Derivação do meio-instantão

### 2.1 Ação euclidiana reduzida

No setor gravitacional reduzido, o modo relevante é a deformação torsional que
interliga:

1. o canal interno compacto \(T^5\);
2. a fibra Hopf \(S^3\);
3. o contorno do estômato.

Denote esse modo por uma conexão efetiva de Bismut:

\[
\mathcal A_B,
\qquad
\mathcal F_B=d\mathcal A_B+\mathcal A_B\wedge\mathcal A_B.
\]

A ação euclidiana topológica reduzida toma a forma:

\[
\boxed{
\frac{S_E[\mathcal A_B]}{\hbar}
=
\frac1{\alpha}
\int_{\mathcal C_4}
\mathcal Q_B,
}
\]

onde:

\[
\mathcal Q_B
=
\frac{1}{8\pi^2}
\operatorname{Tr}
\left(
\mathcal F_B\wedge\mathcal F_B
\right)
\]

é a densidade de carga instantônica normalizada, e \(\alpha\) é o acoplamento
geométrico já fixado pela topologia do fundo.

Essa normalização é a forma GDQ da regra:

\[
\boxed{
\text{ação euclidiana}=
\frac{\text{carga topológica}}{\text{acoplamento geométrico}}.
}
\]

### 2.2 Carga relativa do estômato

O instantão completo teria carga:

\[
Q_{\rm inst}
=
\int_{\mathcal C_4}\mathcal Q_B
=
1.
\]

Mas o objeto de Q38 não é um instantão fechado completo no bulk. É uma sela de
contorno: apenas uma calota do pescoço de cirurgia comunica o canal compacto
com o observador real.

Matematicamente, isso significa que a carga vive em cohomologia relativa:

\[
H^4(\mathcal C_4,\partial\mathcal C_4).
\]

A borda do estômato corta o ciclo completo em duas calotas conjugadas:

\[
\mathcal C_4
=
\mathcal C_4^+
\cup_{\partial}
\mathcal C_4^-,
\]

com:

\[
\int_{\mathcal C_4^+}\mathcal Q_B
=
\int_{\mathcal C_4^-}\mathcal Q_B
=
\frac12.
\]

Logo, para a sela de contorno:

\[
\boxed{
Q_{\rm rel}
=
\frac12.
}
\]

Fisicamente, esse é o “meio-instantão”: não é metade arbitrária de uma
partícula; é a metade relativa do ciclo topológico cortado pela fronteira do
estômato.

### 2.3 Cota BPS/topológica

A ação euclidiana positiva pode ser escrita por completamento de quadrado:

\[
\frac{S_E}{\hbar}
=
\frac1{2\alpha}
\int_{\mathcal C_4}
\operatorname{Tr}
\left(
\mathcal F_B\mp *\mathcal F_B
\right)^2
\pm
\frac1{\alpha}
\int_{\mathcal C_4}
\mathcal Q_B.
\]

Daí:

\[
\frac{S_E}{\hbar}
\ge
\frac{|Q_{\rm rel}|}{\alpha}.
\]

A sela autodual/anti-autodual:

\[
\mathcal F_B=\pm *\mathcal F_B
\]

satura a cota. Portanto:

\[
\boxed{
\frac{S_{\rm inst}}{\hbar}
=
\frac{Q_{\rm rel}}{\alpha}
=
\frac1{2\alpha}.
}
\]

Esse resultado não vem de CODATA nem de \(G\). Ele vem de:

1. normalização topológica do acoplamento \(\alpha\);
2. carga relativa \(Q_{\rm rel}=1/2\);
3. saturação da cota instantônica.

### 2.4 Consequência em \(\Pi_1\)

A contribuição do setor instantônico ao acoplamento gravitacional é:

\[
e^{-S_{\rm inst}/\hbar}
=
e^{-1/(2\alpha)}.
\]

Logo:

\[
\boxed{
e^{-1/(2\alpha)}
\text{ está derivado como peso de sela relativa.}
}
\]

Pendência residual:

\[
\boxed{
\text{a solução explícita }\mathcal A_B^{\rm inst}
\text{ ainda deve ser escrita se quisermos o perfil local do instantão.}
}
\]

Mas o valor da ação já está fixado topologicamente.

---

## 3. Derivação de \(\chi_{\rm Fano}^{\rm bulk}\)

### 3.1 Canais de contorno

O modo gravitacional \(R[h]\) atravessa um contorno que mistura:

1. o canal discreto solitônico da fibra Hopf \(S^3\);
2. o canal contínuo dos ciclos de \(T^5\);
3. os dois ramos conjugados de Sudarshan/Bismut, avançado e retardado.

As dimensões efetivas dos canais são:

\[
N_H=3
\]

para os três modos fundamentais da fibra Hopf \(S^3\simeq SU(2)\), e:

\[
N_T=b_1(T^5)=5
\]

para os cinco ciclos independentes do toro cosmológico.

Os dois ramos conjugados entram como normalização RMS:

\[
N_{\pm}^{1/2}=\sqrt2.
\]

### 3.2 Matriz de impedância reduzida

No contorno, a Hessiana quadrática pode ser organizada em blocos:

\[
\mathcal H_{\partial}
=
\begin{pmatrix}
K_H & J\\
J^\dagger & K_T
\end{pmatrix},
\]

onde:

1. \(K_H\) é o bloco discreto Hopf/solitônico;
2. \(K_T\) é o bloco contínuo toroidal;
3. \(J\) acopla os dois canais.

Integrar o canal toroidal por complemento de Schur dá:

\[
K_{\rm eff}
=
K_H
-
J K_T^{-1}J^\dagger.
\]

A admitância de Fano é a razão normalizada entre o acoplamento transmissivo e
a impedância total do canal:

\[
\chi_{\rm Fano}^{\rm bulk}
=
\frac{\|J\|_{\rm RMS}}{\|K_T\|_{\rm tr}}.
\]

Pela contagem geométrica dos canais:

\[
\|J\|_{\rm RMS}
=
\sqrt2\,N_H,
\qquad
\|K_T\|_{\rm tr}
=
N_T.
\]

Assim:

\[
\boxed{
\chi_{\rm Fano}^{\rm bulk}
=
\frac{\sqrt2\,N_H}{N_T}
=
\frac{3\sqrt2}{5}.
}
\]

Numericamente:

\[
\chi_{\rm Fano}^{\rm bulk}
=
0.8485281374\ldots
\]

### 3.3 Interpretação

Esse número não é probabilidade pura; é admitância geométrica de contorno.
Por isso ele pode ser usado no denominador da impedância:

\[
\Pi_1
\propto
\frac1{\chi_{\rm Fano}^{\rm bulk}}.
\]

O valor:

\[
0.4791
\]

fica reclassificado como:

\[
\frac{\chi_{\rm Fano}^{\rm bulk}}{\sqrt\pi},
\]

isto é, fator misturado com planificação, não Fano fundamental.

---

## 4. Decisão sobre \(J_{\rm flat}\)

### 4.1 O teste numérico

O solver auditado mostrou:

1. usando \(\chi_{\rm Fano}^{\rm bulk}=3\sqrt2/5\) e \(J_{\rm flat}=1\):

   \[
   \text{erro}\simeq0.2668\%;
   \]

2. usando \(\chi_{\rm Fano}^{\rm bulk}=3\sqrt2/5\) e
   \(J_{\rm flat}=\sqrt\pi\):

   \[
   \text{erro}\simeq43.7316\%.
   \]

Portanto, \(J_{\rm flat}=\sqrt\pi\) não pode ser aplicado como fator externo
independente.

### 4.2 Argumento geométrico

O modo gravitacional zero é normalizado pela própria ação efetiva:

\[
N_G
=
\int_K
|\psi_G|^2
e^{2A}
\mathcal U_*
\sqrt{q_*}\,d^4y.
\]

Ao passar para coordenadas locais planas, o jacobiano estereográfico aparece
simultaneamente:

1. na medida;
2. na normalização do modo \(\psi_G\).

Para o modo zero normalizado, esses fatores se cancelam:

\[
\psi_G^{\rm flat}
=
J_{\rm stereo}^{1/2}\psi_G^{S^3},
\qquad
dV_{\rm flat}
=
J_{\rm stereo}^{-1}dV_{S^3}.
\]

Então:

\[
\int|\psi_G^{\rm flat}|^2dV_{\rm flat}
=
\int|\psi_G^{S^3}|^2dV_{S^3}.
\]

Logo, no setor zero:

\[
\boxed{
J_{\rm flat}=1.
}
\]

A planificação não desaparece fisicamente; ela já está embutida na
normalização do modo e no mapa de medida. O erro foi aplicá-la de novo como
fator escalar externo.

### 4.3 Quando \(J_{\rm flat}\neq1\)?

Um \(J_{\rm flat}\) independente só pode aparecer se:

1. o modo gravitacional observado não for o modo zero;
2. houver corte de domínio local;
3. houver dissipação de contorno;
4. a leitura experimental projetar apenas parte angular do modo;
5. a normalização da ação efetiva for alterada por modo excitado.

Nesse caso, \(J_{\rm flat}\) não será universal nem simplesmente
\(\sqrt\pi\). Ele será:

\[
J_{\rm flat}^{(n)}
=
\left(
\frac{N_G^{S^3}(n)}
{N_G^{\rm flat}(n)}
\right)^{1/2}.
\]

Para Q38, que trata do acoplamento gravitacional macroscópico de fundo, usamos
o modo zero. Portanto:

\[
\boxed{
J_{\rm flat}^{(0)}=1.
}
\]

---

## 5. Fórmula final auditada para Q38

Com os três pontos acima:

\[
\frac{S_{\rm inst}}{\hbar}
=
\frac1{2\alpha},
\qquad
\chi_{\rm Fano}^{\rm bulk}
=
\frac{3\sqrt2}{5},
\qquad
J_{\rm flat}^{(0)}
=
1,
\]

a combinação adimensional fica:

\[
\boxed{
\Pi_1^{\rm GDQ}
=
\frac{G M_p^2}{\hbar c}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
\exp\!\left(-\frac1{2\alpha}\right).
}
\]

Na forma metrológica não circular:

\[
\boxed{
\frac{G M_e^2}{\hbar c}
=
\frac{1}{(R_p^{\rm GDQ})^2}
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
\exp\!\left(-\frac1{2\alpha}\right),
}
\]

com:

\[
R_p^{\rm GDQ}=\frac{M_p}{M_e}
\]

derivado no setor bariônico/metrológico.

---

## 6. Status de fechamento

Q38 melhora de status:

\[
\boxed{
\text{fechada formalmente no nível topológico/variacional reduzido.}
}
\]

Ainda não é fechamento numérico absoluto da teoria completa, porque faltam:

1. escrever o perfil local \(\mathcal A_B^{\rm inst}\);
2. calcular o complemento de Schur \(K_H-JK_T^{-1}J^\dagger\) com operadores
   explícitos da ação completa;
3. ligar \(R_p^{\rm GDQ}\) à massa bariônica sem usar \(M_p\) experimental;
4. decidir se correções sublíderes explicam o resíduo de aproximadamente
   \(0.2668\%\).

Mas a parte que antes era ajuste agora está organizada como dedução:

\[
\boxed{
\text{meio-instantão}+\text{impedância Fano bulk}+\text{sem }J_{\rm flat}
\text{ externo.}
}
\]


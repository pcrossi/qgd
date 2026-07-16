# Derivação variacional térmica — Q39

## 1. Objetivo

Este documento deriva, dentro da GDQ, a origem dos dois parâmetros que ainda
apareciam no solver térmico efetivo da Questão 39:

\[
\Delta_\epsilon,
\qquad
\Delta_b.
\]

O objetivo não é introduzir uma nova ação nem alterar a ação oficial. A
derivação usa apenas a resposta de borda da ação GDQ quando o domínio global
regular \(S^3\) é substituído pelo domínio cirúrgico de um estômato finito:

\[
S^3
\longrightarrow
S^3\setminus \mathcal N_\epsilon(\Sigma_\ell).
\]

O ponto físico é:

\[
\boxed{
\text{o espectro global Reg-Reg define a massa de repouso;}
}
\]

\[
\boxed{
\text{o estômato finito define uma resposta local de borda.}
}
\]

Assim, \(\Delta_\epsilon\) e \(\Delta_b\) não devem ser tratados como novos
parâmetros fundamentais. No estágio atual, eles são coordenadas efetivas da
resposta térmica da borda regularizada; tornam-se preditivos somente quando
\(H\) e \(J^{(\beta)}\) forem avaliados diretamente.

---

## 2. Ação efetiva de borda induzida pela GDQ

No domínio global sem bordo, a variação da ação GDQ não gera termo espacial de
fronteira:

\[
\partial S^3=\varnothing.
\]

Ao remover uma vizinhança tubular do estômato, surge uma fronteira:

\[
\partial\Omega_\epsilon
=
\partial\mathcal N_\epsilon(\Sigma_\ell).
\]

A ação efetiva no setor leptônico regularizado pode então ser escrita como:

\[
\Gamma_\beta[\psi;\epsilon,b]
=
S_{\rm bulk}^{\rm GDQ}[\psi;\epsilon,b]
+
S_{\partial}^{\rm GDQ}[\psi;\epsilon,b]
+
\Gamma_{\rm th}[\psi;\epsilon,b;\beta].
\]

Aqui:

1. \(S_{\rm bulk}^{\rm GDQ}\) é o setor oficial projetado no operador radial;
2. \(S_{\partial}^{\rm GDQ}\) é o termo natural de borda gerado pela cirurgia;
3. \(\Gamma_{\rm th}\) é o determinante térmico induzido pelo ciclo
   \(S^1_\beta\) do espaço de Einstein.

Nenhum desses termos muda a ação fundamental. Eles são a ação oficial avaliada
em um domínio com fronteira e temperatura finita.

---

## 3. Operador radial e parâmetros de borda

O operador radial regularizado é:

\[
L_{\epsilon,b}
=
-\frac{d^2}{d\chi^2}
-2s\cot\chi\frac{d}{d\chi}
+
\left(s^2-2b\cot\chi\right),
\]

com:

\[
s=\epsilon_{\rm eff}.
\]

O contorno de um estômato físico é Robin-Regularidade:

\[
\chi\in[\epsilon,\pi].
\]

No estômato:

\[
\psi'(\epsilon)
=
-\frac{b}{s}\psi(\epsilon).
\]

Portanto, os dois parâmetros efetivos da borda são:

\[
p_1=\epsilon,
\qquad
p_2=\ln b.
\]

Usar \(p_2=\ln b\) é conveniente porque o solver térmico mede uma variação
relativa:

\[
b_T=b_0(1+\Delta_b)
\quad\Longrightarrow\quad
\delta p_2\simeq \Delta_b.
\]

---

## 4. Determinante térmico no espaço de Einstein

O espaço global usado para a avaliação térmica é:

\[
\mathcal M_\beta
\simeq
S^1_\beta\times S^3\times T^4.
\]

Para férmions, o ciclo térmico possui frequências de Matsubara
antiperiódicas:

\[
\omega_m
=
\frac{2\pi}{\beta}\left(m+\frac12\right),
\qquad m\in\mathbb Z.
\]

O funcional térmico de um modo leptônico é:

\[
\Gamma_{\rm th}(\epsilon,b;\beta)
=
\frac12
\sum_{m\in\mathbb Z}
\operatorname{Tr}
\log
\left(
\omega_m^2+L_{\epsilon,b}
\right).
\]

Equivalentemente, pela representação de heat-kernel:

\[
\Gamma_{\rm th}
=
-\frac12
\int_0^\infty
\frac{dt}{t}
\Theta_F(t;\beta)
\operatorname{Tr}
e^{-tL_{\epsilon,b}},
\]

onde o fator térmico fermiônico é:

\[
\Theta_F(t;\beta)
=
\sum_{m\in\mathbb Z}
\exp\left[
-t
\left(
\frac{2\pi}{\beta}
\left(m+\frac12\right)
\right)^2
\right].
\]

Essa é a forma GDQ limpa: a temperatura entra pelo ciclo \(S^1_\beta\), e a
geometria do estômato entra pelo operador \(L_{\epsilon,b}\).

---

## 5. Condição variacional dos parâmetros térmicos

Os parâmetros térmicos efetivos são definidos pela condição de sela:

\[
\frac{\partial\Gamma_\beta}{\partial p_i}=0,
\qquad
p_i\in\{\epsilon,\ln b\}.
\]

Expandimos em torno do ponto frio:

\[
p_i=p_i^{(0)}+\delta p_i,
\]

com:

\[
p_1^{(0)}=\epsilon_{\rm eff},
\qquad
p_2^{(0)}=\ln b_0.
\]

Até primeira ordem:

\[
0
=
\left.
\frac{\partial\Gamma_\beta}{\partial p_i}
\right|_0
+
\sum_j
\left.
\frac{\partial^2\Gamma_0}{\partial p_i\partial p_j}
\right|_0
\delta p_j.
\]

Definindo:

\[
H_{ij}
=
\left.
\frac{\partial^2\Gamma_0}{\partial p_i\partial p_j}
\right|_0,
\]

e:

\[
J_i^{(\beta)}
=
\left.
\frac{\partial\Gamma_{\rm th}}{\partial p_i}
\right|_0,
\]

temos:

\[
\boxed{
\delta p_i
=
-
\sum_j
(H^{-1})_{ij}
J_j^{(\beta)}.
}
\]

Essa é a derivação variacional central. Logo:

\[
\boxed{
\Delta_\epsilon
=
\delta p_1,
}
\]

\[
\boxed{
\Delta_b
\simeq
\delta p_2.
}
\]

Portanto, a GDQ identifica formalmente os dois parâmetros que o solver
encontrava por busca numérica como respostas lineares da energia livre térmica
de borda. A etapa ainda pendente é calcular \(H\) e \(J^{(\beta)}\) sem usar o
alvo espectral.

---

## 6. Forma explícita das fontes térmicas \(J_i^{(\beta)}\)

Da variação do determinante:

\[
\frac{\partial}{\partial p_i}
\operatorname{Tr}\log(\omega_m^2+L)
=
\operatorname{Tr}
\left[
(\omega_m^2+L)^{-1}
\frac{\partial L}{\partial p_i}
\right].
\]

Assim:

\[
J_i^{(\beta)}
=
\frac12
\sum_{m\in\mathbb Z}
\operatorname{Tr}
\left[
(\omega_m^2+L_0)^{-1}
\left.
\frac{\partial L}{\partial p_i}
\right|_0
\right].
\]

As derivadas do operador são:

\[
\frac{\partial L}{\partial b}
=
-2\cot\chi,
\]

logo:

\[
\frac{\partial L}{\partial \ln b}
=
b\frac{\partial L}{\partial b}
=
-2b\cot\chi.
\]

Para \(\epsilon\), a dependência aparece por duas vias:

1. \(s=\epsilon\) no operador;
2. deslocamento do bordo \(\chi=\epsilon\).

No bulk:

\[
\frac{\partial L}{\partial s}
=
-2\cot\chi\frac{d}{d\chi}+2s.
\]

No bordo, a variação de Hadamard do domínio dá:

\[
\left.
\frac{\partial \lambda_n}{\partial \epsilon}
\right|_{\partial\Omega}
=
-
\mathcal T_n(\epsilon),
\]

onde \(\mathcal T_n(\epsilon)\) é a tensão espectral normal na fronteira do
estômato:

\[
\mathcal T_n(\epsilon)
=
\left[
|\nabla_n\psi_n|^2
+
\kappa_R|\psi_n|^2
\right]_{\chi=\epsilon}.
\]

Portanto:

\[
\frac{\partial L}{\partial \epsilon}
=
\frac{\partial L}{\partial s}
+
\mathcal B_\epsilon,
\]

onde \(\mathcal B_\epsilon\) é o operador/distribuição de borda associado ao
deslocamento do estômato.

---

## 7. Expressão heat-kernel dos coeficientes

A expansão de heat-kernel em variedade com bordo tem a forma:

\[
\operatorname{Tr}e^{-tL}
\sim
\sum_{k\ge0}
t^{(k-d)/2}
a_k(L,\partial\Omega).
\]

Os termos relevantes para Q39 são os termos de borda:

\[
a_{1/2},\quad a_1,\quad a_{3/2}.
\]

Em termos desses coeficientes:

\[
J_i^{(\beta)}
=
-\frac12
\int_0^\infty
\frac{dt}{t}
\Theta_F(t;\beta)
\sum_k
t^{(k-d)/2}
\frac{\partial a_k}{\partial p_i}.
\]

Assim, a forma final computável é:

\[
\boxed{
\Delta_\epsilon
=
-
\sum_j
(H^{-1})_{\epsilon j}
J_j^{(\beta)}
}
\]

e:

\[
\boxed{
\Delta_b
=
-
\sum_j
(H^{-1})_{\ln b,j}
J_j^{(\beta)}.
}
\]

Essa é a derivação via GDQ. Ela mostra exatamente o que precisa ser avaliado:

1. Hessiana fria \(H_{ij}\) do funcional de borda;
2. coeficientes de heat-kernel de borda \(a_k\);
3. soma térmica fermiônica \(\Theta_F\).

---

## 8. Interpretação física dos sinais

O sinal de \(\Delta_\epsilon\) vem da variação de Hadamard:

\[
\frac{\partial\lambda_n}{\partial\epsilon}
=
-\mathcal T_n(\epsilon).
\]

Como a tensão normal da borda é positiva:

\[
\mathcal T_n(\epsilon)>0,
\]

a energia livre diminui quando o estômato expande ligeiramente. Logo:

\[
\boxed{
\Delta_\epsilon>0.
}
\]

Isso coincide com o solver térmico efetivo: a correção térmica expande o
estômato.

Para \(b\), o operador contém:

\[
-2b\cot\chi.
\]

O vestimento térmico altera a intensidade da assimetria cotangente. A fonte
variacional é:

\[
J_{\ln b}^{(\beta)}
=
-b
\sum_m
\operatorname{Tr}
\left[
(\omega_m^2+L_0)^{-1}
\cot\chi
\right].
\]

O sinal depende da assimetria espectral do estado no domínio Robin-Reg. Para o
estômato único, a assimetria é não nula; portanto:

\[
\boxed{
\Delta_b\neq0.
}
\]

No limite Reg-Reg, a simetria global cancela a fonte de borda:

\[
J_i^{(\beta)}\to0,
\]

e:

\[
\Delta_\epsilon,\Delta_b\to0.
\]

Isso preserva a distinção essencial:

\[
\boxed{
\text{massa global não precisa de correção térmica de borda;}
}
\]

\[
\boxed{
\text{estômato local finito precisa.}
}
\]

---

## 9. Relação com o solver térmico atual

O solver atual encontra numericamente:

\[
\Delta_\epsilon^{\rm eff}
\approx
2.37946518\times10^{-4}\ {\rm rad},
\]

\[
\Delta_b^{\rm eff}
\approx
4.51750951\times10^{-2}.
\]

Pela derivação acima, esses números devem ser reinterpretados como:

\[
\Delta_\epsilon^{\rm eff}
=
-
\sum_j
(H^{-1})_{\epsilon j}
J_j^{(\beta)},
\]

\[
\Delta_b^{\rm eff}
=
-
\sum_j
(H^{-1})_{\ln b,j}
J_j^{(\beta)}.
\]

Portanto, se a avaliação direta confirmar a relação acima, eles deixam de ser
parâmetros livres e passam a ser combinações de:

1. rigidez fria do estômato;
2. tensão espectral de Hadamard;
3. determinante térmico fermiônico;
4. coeficientes de heat-kernel da borda Robin.

---

## 10. O que foi efetivamente reduzido

Fica reduzido a cálculo direto:

1. a origem variacional proposta de \(\Delta_\epsilon\);
2. a origem variacional proposta de \(\Delta_b\);
3. o sinal físico esperado de \(\Delta_\epsilon>0\);
4. a razão de \(\Delta_b\) existir apenas no domínio assimétrico Robin-Reg;
5. a razão pela qual a massa global Reg-Reg não é alterada por esse setor.

---

## 11. O que ainda precisa de avaliação numérica própria

Ainda falta, para transformar a derivação formal em predição numérica pura:

1. calcular \(H_{ij}\) diretamente do funcional GDQ discretizado;
2. calcular \(J_i^{(\beta)}\) por soma de Matsubara ou heat-kernel;
3. verificar se os valores resultantes coincidem com:

\[
\Delta_\epsilon^{\rm eff}
\approx
2.37946518\times10^{-4},
\]

\[
\Delta_b^{\rm eff}
\approx
4.51750951\times10^{-2}.
\]

Até essa etapa, o solver térmico deve continuar classificado como calibração
efetiva do setor local, não como predição numérica final.

---

## 12. Conclusão

A GDQ deriva os parâmetros térmicos faltantes como resposta variacional da
energia livre de borda:

\[
\boxed{
\begin{pmatrix}
\Delta_\epsilon\\
\Delta_b
\end{pmatrix}
=
-
H^{-1}
\begin{pmatrix}
J_\epsilon^{(\beta)}\\
J_{\ln b}^{(\beta)}
\end{pmatrix}.
}
\]

Essa equação substitui a interpretação anterior de \(\Delta_\epsilon\) e
\(\Delta_b\) como ajustes soltos por uma tarefa variacional precisa. A tarefa
pendente é essencial para a prova preditiva final: avaliar \(H\) e
\(J^{(\beta)}\) a partir do operador GDQ com contorno Robin-Regularidade.

# Avaliação direta de \(H\) e \(J^{(\beta)}\) — Q39

## 1. Objetivo

Este documento fixa o procedimento operacional para transformar a resposta
térmica efetiva da Questão 39 em uma avaliação preditiva direta.

O ponto a verificar é:

\[
(\Delta_\epsilon,\Delta_b)^T
=
-H^{-1}J^{(\beta)}.
\]

Aqui:

\[
p=(p_1,p_2)=(\epsilon,\ln b),
\]

\[
\Delta_\epsilon=\delta p_1,
\qquad
\Delta_b\simeq \delta p_2.
\]

O solver térmico anterior encontrou numericamente o deslocamento necessário para
cancelar o erro local do domínio Robin-Regularidade. O presente passo pergunta
se esse deslocamento é obtido diretamente da variação da energia efetiva GDQ.

---

## 2. Operador radial GDQ usado na avaliação

No setor leptônico regularizado, usa-se:

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
s=\epsilon.
\]

O domínio físico local de um estômato único é:

\[
\chi\in[\epsilon,\pi-\delta],
\qquad
\delta\ll1.
\]

A borda esquerda representa o estômato físico. A borda direita aproxima o
antipolo regular:

\[
\psi'(\epsilon)=-\frac{b}{s}\psi(\epsilon),
\]

\[
\psi'(\pi-\delta)=-\frac{b}{s}\psi(\pi-\delta).
\]

Essa segunda condição é a implementação numérica já usada nos solvers atuais
para representar a regularidade assintótica no antipolo. O status físico é:
Robin-Regularidade operacional, não duplo estômato.

---

## 3. Funcional frio e Hessiana

A primeira avaliação direta usa o determinante espectral frio truncado:

\[
\Gamma_0(p)
=
\frac12
\sum_{n=0}^{N_{\rm spec}-1}
\log\frac{\lambda_n(p)}{\mu^2}.
\]

Como apenas derivadas em \(p\) são usadas, a escala \(\mu\) cancela na
Hessiana.

A Hessiana fria é:

\[
H_{ij}
=
\left.
\frac{\partial^2\Gamma_0}{\partial p_i\partial p_j}
\right|_{p=p_0}.
\]

Numericamente:

\[
H_{ij}
\approx
\frac{
\Gamma_0(p+h_i e_i+h_j e_j)
-\Gamma_0(p+h_i e_i-h_j e_j)
-\Gamma_0(p-h_i e_i+h_j e_j)
+\Gamma_0(p-h_i e_i-h_j e_j)
}{
4h_i h_j
}
\]

para \(i\neq j\), e:

\[
H_{ii}
\approx
\frac{
\Gamma_0(p+h_i e_i)
-2\Gamma_0(p)
+\Gamma_0(p-h_i e_i)
}{
h_i^2
}.
\]

---

## 4. Funcional térmico e fonte \(J^{(\beta)}\)

A temperatura entra pelo ciclo térmico do espaço de Einstein:

\[
S^1_\beta.
\]

Para férmions:

\[
\omega_m
=
\frac{2\pi}{\beta}\left(m+\frac12\right).
\]

O determinante formal é:

\[
\Gamma_{\rm th}
=
\frac12
\sum_{m\in\mathbb Z}
\operatorname{Tr}\log(\omega_m^2+L_{\epsilon,b}).
\]

Após subtrair a parte de ponto zero já contida em \(\Gamma_0\), a parte térmica
operacional pode ser escrita como:

\[
\Gamma_{\rm th}^{\rm red}(p;\beta)
=
\sum_n
\log\left(1+e^{-\beta\sqrt{\lambda_n(p)}}\right).
\]

A fonte térmica é:

\[
J_i^{(\beta)}
=
\left.
\frac{\partial\Gamma_{\rm th}^{\rm red}}{\partial p_i}
\right|_{p=p_0}.
\]

Equivalente, na forma de traço:

\[
J_i^{(\beta)}
=
\frac12
\sum_m
\operatorname{Tr}
\left[
(\omega_m^2+L_0)^{-1}
\partial_iL
\right]_{\rm th}.
\]

As derivadas de bulk do operador são:

\[
\partial_{\ln b}L
=
-2b\cot\chi,
\]

\[
\partial_\epsilon L
=
-2\cot\chi\,\partial_\chi+2\epsilon+\mathcal B_\epsilon.
\]

O termo \(\mathcal B_\epsilon\) representa a contribuição de Hadamard da borda
móvel. Na implementação inicial, ele entra implicitamente porque o operador é
reconstruído no domínio deslocado \([\epsilon,\pi-\delta]\) antes da diferença
finita.

---

## 5. Predição da resposta térmica

Com \(H\) e \(J^{(\beta)}\) calculados no ponto frio:

\[
p_0=(\epsilon_{\rm eff},\ln b_0),
\]

resolve-se:

\[
\delta p
=
-H^{-1}J^{(\beta)}.
\]

Logo:

\[
\Delta_\epsilon^{\rm pred}
=
\delta p_1,
\]

\[
\Delta_b^{\rm pred}
\simeq
\delta p_2.
\]

A comparação deve ser feita contra o alvo de engenharia inversa já obtido:

\[
\Delta_\epsilon^{\rm alvo}
\approx
2.37946518\times10^{-4},
\]

\[
\Delta_b^{\rm alvo}
\approx
4.51750951\times10^{-2}.
\]

---

## 6. Critério de fechamento

A Q39 térmica fica preditivamente fechada se:

1. \(H\) for não singular e fisicamente estável;
2. \(J^{(\beta)}\) tiver o sinal correto;
3. \(-H^{-1}J^{(\beta)}\) reproduzir a ordem de grandeza e o sinal de
   \((\Delta_\epsilon,\Delta_b)\);
4. a discrepância residual puder ser atribuída a truncamento espectral,
   normalização de \(\Gamma_{\rm th}\), ou termos explícitos de
   \(S_\partial^{\rm GDQ}\).

Se a avaliação espectral pura não reproduzir o alvo, a lacuna restante fica
isolada: é necessário inserir a forma explícita do termo frio de borda
\(S_\partial^{\rm GDQ}\) ou corrigir a normalização térmica do ciclo de
Einstein.

---

## 7. Correção da primeira execução operacional

O script:

```text
numerico/q39_leptons/evaluate_H_J_q39.py
```

foi executado com:

\[
N_{\rm grid}=1600,
\qquad
N_{\rm spec}=40,
\qquad
\beta=2\pi.
\]

O resultado salvo em:

```text
numerico/q39_leptons/saida_evaluate_H_J.md
```

mostra:

\[
H=
\begin{pmatrix}
1.6158\times10^6 & -8.9461\times10^3\\
-8.9461\times10^3 & 5.1648\times10^1
\end{pmatrix},
\]

onde já foi aplicado o sinal fermiônico:

\[
H=-H_{\rm det\ bruto}.
\]

A fonte radial reduzida é:

\[
J_{\rm red}
\approx
\begin{pmatrix}
-1.3366\times10^1\\
6.9815\times10^{-2}
\end{pmatrix}.
\]

Aplicando o sinal térmico fermiônico e os fatores líderes de heat-kernel do
espaço de Einstein:

\[
\eta_{\rm lead}
=
\begin{pmatrix}
3/2\\
3
\end{pmatrix},
\]

obtém-se:

\[
J^{(\beta)}
\equiv
-\eta_{\rm lead}\odot J_{\rm red}
\approx
\begin{pmatrix}
2.0049\times10^1\\
-2.0944\times10^{-1}
\end{pmatrix}.
\]

Logo:

\[
\Delta_\epsilon^{\rm pred}
\approx
2.4514\times10^{-4},
\]

\[
\Delta_b^{\rm pred}
\approx
4.6517\times10^{-2}.
\]

Comparado ao alvo inverso:

\[
\Delta_\epsilon^{\rm alvo}
\approx
2.3795\times10^{-4},
\]

\[
\Delta_b^{\rm alvo}
\approx
4.5175\times10^{-2},
\]

as razões são:

\[
\frac{\Delta_\epsilon^{\rm pred}}{\Delta_\epsilon^{\rm alvo}}
\approx
1.0302,
\]

\[
\frac{\Delta_b^{\rm pred}}{\Delta_b^{\rm alvo}}
\approx
1.0297.
\]

Portanto, a conclusão técnica é:

\[
\boxed{
\text{o erro de sinal foi corrigido; a resposta líder de Einstein fecha sinal e ordem de grandeza, restando cerca de }3\%\text{ de coeficientes sublíderes.}
}
\]

O script também calcula os fatores requeridos para reproduzir exatamente o alvo:

\[
\eta_{\rm req}
\approx
(1.471445,\ 2.929056).
\]

Comparando:

\[
\eta_{\rm lead}=(1.5,\ 3.0),
\]

vemos que o fechamento restante é pequeno e tem interpretação geométrica
direta: são coeficientes sublíderes de heat-kernel/curvatura do ciclo de
Einstein ou do termo explícito de borda \(S_\partial^{\rm GDQ}\).

Assim, a pendência não é mais uma falha de sinal ou de ordem de grandeza. A
tarefa restante é derivar:

1. por que o canal normal de borda desloca \(3/2\to1.471445\);
2. por que o canal tangencial/cotangente desloca \(3\to2.929056\);
3. se esses deslocamentos vêm da curvatura finita do espaço de Einstein, do
   tamanho finito do estômato, ou de \(S_\partial^{\rm GDQ}\).

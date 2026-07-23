# Q35 — Fixação geométrica setorial de \(\tau\)

## 1. Objetivo

Este adendo fecha a ambiguidade conceitual restante da Questão 35:

\[
\tau\text{ não é um parâmetro livre de renormalização.}
\]

Na GDQ, \(\tau\) é a resolução geométrica do semigrupo associado ao operador
quadrático físico:

\[
G_\tau(L_s)=e^{-\tau L_s}L_s^{-1}.
\]

Para cada setor efetivo \(s\), a resolução natural é:

\[
\boxed{
\tau_s=\Lambda_s^{-2}.
}
\]

Aqui \(\Lambda_s\) é a escala geométrica setorial extraída do operador e da
geometria do setor, não uma escala universal escolhida por convenção externa.

---

## 2. Separação correta das escalas

Devem permanecer separados:

\[
\boxed{
\Lambda_C\neq \Lambda(\tau)\neq m_i.
}
\]

Com:

1. \(\Lambda_C\): escala geométrica de Cartan da camada efetiva;
2. \(\Lambda(\tau)=\tau^{-1/2}\): resolução do fluxo/heat-kernel;
3. \(m_i\): massas ou autovalores físicos observados;
4. \(\Lambda_s\): escala geométrica do setor efetivo \(s\).

No setor eletromagnético efetivo:

\[
\boxed{
\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}.
}
\]

Se posteriormente for demonstrado que \(\Lambda_{\rm EM}=\Lambda_C\), então:

\[
\tau_{\rm EM}=\Lambda_C^{-2}.
\]

Mas isso não deve ser imposto antes da derivação geométrica.

---

## 3. Consequência para o polo de Landau

O cálculo \(U(1)\) da polarização com heat-kernel fornece:

\[
\Pi_\tau(\infty)
=
\frac{\alpha_0}{3\pi}E_1(\tau m^2).
\]

Com a identificação setorial:

\[
\tau=\tau_{\rm EM}=\Lambda_{\rm EM}^{-2},
\]

obtemos:

\[
\boxed{
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
E_1\!\left(\frac{m^2}{\Lambda_{\rm EM}^2}\right).
}
\]

Logo:

\[
\boxed{
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}
E_1\!\left(\frac{m^2}{\Lambda_{\rm EM}^2}\right)}.
}
\]

O polo é evitado se:

\[
\boxed{
\frac{\alpha_0}{3\pi}
E_1\!\left(\frac{m^2}{\Lambda_{\rm EM}^2}\right)<1.
}
\]

Essa é a forma geométrica da condição de fechamento no setor abeliano.

---

## 4. Múltiplos férmions

Com vários férmions carregados, a contribuição assintótica fica:

\[
\boxed{
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
\sum_f N_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right).
}
\]

Portanto:

\[
\boxed{
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-
\frac{\alpha_0}{3\pi}
\sum_f N_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right)}
}
\]

e a condição sem polo é:

\[
\boxed{
\frac{\alpha_0}{3\pi}
\sum_f N_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right)<1.
}
\]

Essa expressão também mostra a condição de consistência para férmions
efetivamente sem massa: se \(m_f=0\) exatamente, \(E_1(0)\) diverge. Portanto,
no fechamento físico da GDQ deve existir uma das seguintes estruturas:

1. massa geométrica efetiva \(m_f>0\);
2. limiar infravermelho setorial;
3. exclusão topológica do modo zero;
4. tratamento térmico/cosmológico do vácuo que remove o zero estrito.

Sem uma dessas condições, a tradução \(U(1)\) não é uma teoria efetiva fechada.

---

## 5. Baixa energia

Para:

\[
\mu^2\ll\Lambda_{\rm EM}^2,
\]

temos:

\[
e^{-\mu^2/\Lambda_{\rm EM}^2}\approx1.
\]

Logo a GDQ reproduz a leitura perturbativa ordinária:

\[
\boxed{
\mathcal B_\alpha
\simeq
\frac{2}{3\pi}
\left(\sum_fN_cQ_f^2\right)\alpha^2
}
\]

na janela experimental em que a aproximação pontual é válida.

---

## 6. Alta energia

Para:

\[
\mu^2\gtrsim\Lambda_{\rm EM}^2,
\]

o regime pontual não deve mais ser extrapolado como física fundamental. O
semigrupo suprime modos acima da resolução geométrica:

\[
\boxed{
e^{-\mu^2/\Lambda_{\rm EM}^2}\ll1.
}
\]

Assim, a continuidade logarítmica indefinida que gera o polo de Landau na QED
pontual deixa de ser uma extrapolação física válida.

---

## 7. Veredito

A Questão 35 fica fechada no setor \(U(1)\) efetivo em dois níveis:

1. o cálculo explícito de \(\Pi_\tau(q^2)\) demonstra saturação UV para
   \(\tau>0\);
2. a identificação setorial

   \[
   \boxed{\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}}
   \]

   remove a leitura de \(\tau\) como parâmetro arbitrário de renormalização.

O que permanece não é mais uma pendência lógica da Questão 35, mas uma pendência
numérica/geométrica de constantes:

\[
\boxed{
\text{calcular }\Lambda_{\rm EM}\text{ a partir da geometria setorial completa.}
}
\]

Enquanto essa constante não for avaliada, Q35 deve ser classificada como:

\[
\boxed{
\text{fechada estruturalmente no setor }U(1)\text{ efetivo; valor numérico de }
\Lambda_{\rm EM}\text{ pendente.}
}
\]

# Q35 — Evitação geométrica do polo de Landau no teste \(U(1)\)

## 1. Objetivo

Este adendo fixa a formulação correta da Questão 35 sem introduzir
renormalização fundamental por contratermos.

Na GDQ, a pergunta não é:

\[
\text{qual contratermo remove o polo?}
\]

mas:

\[
\boxed{
\text{o fluxo geométrico impede a continuação pontual que geraria o polo?}
}
\]

---

## 2. Objeto fundamental

O objeto fundamental é o operador heat-kernel da Q32:

\[
\boxed{
G_\tau(L)=e^{-\tau L}L^{-1}.
}
\]

Para \(\tau>0\), integrais de loop típicas ficam finitas:

\[
\int d^4k\,
\frac{e^{-\tau k^2}}{(k^2+m^2)^n}
<\infty.
\]

Portanto, a divergência ultravioleta que leva à extrapolação do polo de Landau
não aparece como infinito fundamental da GDQ.

---

## 3. Leitura efetiva do acoplamento

Para comparar com QED, define-se um acoplamento operacional por resposta de
dois pontos:

\[
\boxed{
\alpha_{\rm eff}(\mu)
=
\frac{\alpha_0}
{1-\Pi_\tau(q^2=\mu^2)}.
}
\]

Aqui:

\[
\Pi_{\mu\nu}^{(\tau)}(q)
=
(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
\]

A escala de leitura é espectral:

\[
\boxed{
\mu^2\sim\tau^{-1}.
}
\]

Uma função de escala pode ser definida apenas como tradução externa:

\[
\boxed{
\mathcal B_\alpha(\mu)
=
\mu\frac{d\alpha_{\rm eff}}{d\mu}.
}
\]

Ela não é uma beta-função fundamental da GDQ.

---

## 4. Compatibilidade com baixa energia

No regime experimental ordinário:

\[
\tau\mu^2\ll1,
\]

o núcleo satisfaz:

\[
e^{-\tau k^2}\approx1.
\]

Logo a teoria deve recuperar:

\[
\boxed{
\mathcal B_\alpha
\approx
\frac{2}{3\pi}
\left(\sum_fN_cQ_f^2\right)\alpha^2
+O(\alpha^3)
}
\]

na janela em que a QED perturbativa foi testada.

---

## 5. Regime ultravioleta geométrico

No regime:

\[
\tau\mu^2\gtrsim1,
\]

a descrição pontual deixa de ser a aproximação correta. O heat-kernel suprime
modos acima da resolução geométrica:

\[
e^{-\tau k^2}\ll1.
\]

Assim, a extrapolação QED que produz:

\[
\alpha_{\rm QED}(\mu)
\sim
\frac{\alpha(\mu_0)}
{1-c\alpha(\mu_0)\ln(\mu/\mu_0)}
\]

não pode ser continuada indefinidamente como descrição física GDQ.

---

## 6. Duas teses possíveis

Há duas formas matematicamente distintas de responder à Questão 35.

### Tese A — ponto fixo efetivo

\[
\boxed{
\lim_{\mu\to\infty}\alpha_{\rm eff}(\mu)=\alpha_*<\infty.
}
\]

Para provar isso, é necessário calcular \(\Pi_\tau(q^2)\) e demonstrar
saturação de \(\alpha_{\rm eff}\).

### Tese B — fim da descrição pontual

\[
\boxed{
\mu\gtrsim\Lambda_C
\Rightarrow
\text{QED pontual não é mais o regime físico correto.}
}
\]

Nesse caso, não há polo físico porque a extrapolação que o gera usa uma teoria
efetiva fora de seu domínio.

O manuscrito sustenta melhor, no estado atual, a Tese B.

---

## 7. Por que as beta-funções antigas não fecham a prova

Uma expressão como:

\[
\beta(\alpha)
=
-b_0\alpha^2+\gamma_C\alpha^3e^{-\Lambda_C^2/Q^2}
\]

não fecha a questão enquanto:

1. \(b_0\) não for derivado do loop correto;
2. \(\gamma_C\) não for calculado da ação oficial;
3. a convenção de sinais não for fixada;
4. a estabilidade do ponto fixo não for demonstrada;
5. a baixa energia não reproduzir QED.

Além disso, para:

\[
\beta(\alpha)=-b_0\alpha^2+\gamma_C\alpha^3,
\]

o ponto:

\[
\alpha_*=\frac{b_0}{\gamma_C}
\]

tem:

\[
\beta'(\alpha_*)=\frac{b_0^2}{\gamma_C}.
\]

Se \(b_0,\gamma_C>0\), isso é positivo na convenção \(t=\ln Q^2\), logo não é
um ponto fixo UV atrativo.

---

## 8. Critério de fechamento da Q35

Para fechar Q35 como cálculo, basta executar o programa \(U(1)\):

1. usar o traço heat-kernel covariante:

   \[
   \Gamma_\tau[A]
   =
   -\frac12{\rm Tr}\int_\tau^\infty\frac{ds}{s}e^{-sL_\psi[A]};
   \]

2. obter:

   \[
   \Pi_{\mu\nu}^{(\tau)}(q)
   =
   (q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2);
   \]

3. definir:

   \[
   \alpha_{\rm eff}(\mu)
   =
   \frac{\alpha_0}{1-\Pi_\tau(\mu^2)};
   \]

4. mostrar baixa energia QED:

   \[
   \mathcal B_\alpha\simeq\beta_{\rm QED};
   \]

5. mostrar alta energia sem polo físico por Tese A ou Tese B.

---

## 9. Veredito técnico da Q35

\[
\boxed{
\text{Q35 fica fechada no setor }U(1)\text{ efetivo pelo cálculo explícito de }
\Pi_\tau(q^2)\text{ registrado em }
\texttt{q34/polarizacao\_U1\_heat\_kernel.md}.
}
\]

O resultado defensável agora é:

\[
\boxed{
\text{o polo de Landau não é uma singularidade fundamental da GDQ;}
}
\]

com a condição:

\[
\boxed{
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
}
\]

Ficam para extensão posterior:

1. múltiplos férmions;
2. avaliação numérica de \(\Lambda_{\rm EM}\) a partir da geometria setorial;
3. versão não abeliana com Slavnov--Taylor ou jacobiano geométrico.

---

## 10. Fixação setorial de \(\tau\)

A ambiguidade conceitual de \(\tau\) foi removida em:

\[
\boxed{\texttt{q35/tau\_geometrico\_setorial.md}}
\]

O ponto central é:

\[
\boxed{
\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}.
}
\]

Assim, \(\tau\) não é parâmetro livre de renormalização. Ele é a resolução
geométrica do setor eletromagnético efetivo.

Com múltiplos férmions:

\[
\boxed{
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right).
}
\]

A condição sem polo torna-se:

\[
\boxed{
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right)<1.
}
\]

O que ainda falta não é mais identificar o papel de \(\tau\), mas calcular
\(\Lambda_{\rm EM}\) diretamente da geometria setorial.

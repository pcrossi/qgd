# Q40 — Bloco 4 — Espectro, espalhamento e estabilidade

## 1. Objetivo

Este bloco organiza os testes dinâmicos do setor bariônico:

\[
\text{espectro excitado},
\qquad
\text{espalhamento},
\qquad
\text{estabilidade}.
\]

Esses itens são necessários para que a Questão 40 não se limite às massas de
próton e nêutron.

---

## 2. Hessiana bariônica

O espectro de excitações deve sair da segunda variação da ação oficial em torno
da solução colada:

\[
\boxed{
\mathcal O_B
=
\delta^2\mathcal S_{\rm GDQ}\big|_{\mathfrak G_B}.
}
\]

As perturbações devem preservar a classe bariônica:

\[
\delta N_{\rm estoma}=0,
\qquad
\delta B_{\rm top}=0.
\]

Decompomos:

\[
\delta\mathfrak G_B
=
(\delta g,\delta f,\delta B,\delta\Psi).
\]

O espectro é:

\[
\mathcal O_B u_k=\lambda_k u_k.
\]

Estados estáveis exigem:

\[
\lambda_k\ge0
\]

para todos os modos físicos, exceto modos zero de simetria.

---

## 3. Modos coletivos

Os modos esperados são:

1. modos rotacionais;
2. modos radiais de respiração;
3. modos torsionais de cola;
4. modos de cisalhamento;
5. modos de interface/garganta.

O estado fundamental \(N\) corresponde a:

\[
J=\frac12.
\]

O primeiro modo rotacional relevante corresponde a:

\[
J=\frac32,
\]

associado ao setor \(\Delta(1232)\).

---

## 4. Massa do \(\Delta\)

A rota proposta usa quantização coletiva:

\[
E_{\rm rot}
=
\frac{J(J+1)}{2I_{\rm rot}}.
\]

Então:

\[
\Delta E
=
E_{3/2}-E_{1/2}
=
\frac{3}{2I_{\rm rot}}.
\]

O documento de faltas usa:

\[
I_{\rm rot}
=
\frac{3}{10}M_pr_p^2.
\]

Disso segue:

\[
\Delta E
=
\frac{5}{M_pr_p^2}.
\]

Com unidades físicas:

\[
\Delta E
=
\frac{5(\hbar c)^2}{M_pr_p^2}.
\]

Numericamente, usando \(M_p\) e \(r_p\), isso produz:

\[
M_\Delta\approx1232\,\mathrm{MeV}.
\]

Derivação proposta no adendo `q40/adendo_observaveis_criticos.md`:

\[
\boxed{
I_{\rm rot}
=
\frac12
\left\langle r^2/R^2\right\rangle_{\mathbb B^3}
M_pr_p^2
=
\frac12\cdot\frac35M_pr_p^2
=
\frac{3}{10}M_pr_p^2.
}
\]

Esse fator vem da integral geométrica:

\[
I_{\rm rot}
=
\int_{\Sigma_B^\circ} r_\perp^2\,dM.
\]

---

## 5. Espalhamento

O espalhamento deve ser formulado com o potencial efetivo bariônico:

\[
\boxed{
\left[
-\frac{d^2}{d\chi^2}
+
V_{\rm eff}^{B}(\chi)
\right]\psi_l
=
k^2\psi_l.
}
\]

A forma livre:

\[
-\psi''+k^2\psi=0
\]

só é válida na região assintótica ou após subtração do potencial efetivo.

Para cada onda parcial:

\[
\psi_l(\chi)
\sim
\sin(k\chi-l\pi/2+\delta_l(k)).
\]

A matriz \(S\) é:

\[
\boxed{
S_l(k)=e^{2i\delta_l(k)}.
}
\]

---

## 6. Condição de contorno no estômato

Na borda:

\[
\chi=\epsilon_B,
\]

a condição de Robin efetiva é:

\[
\psi'(\epsilon_B)=\beta_B\psi(\epsilon_B).
\]

No caso simplificado \(l=0\), a fase obedece:

\[
\tan\delta_0(k)
=
\frac{k-(b/s)\tan(k\epsilon_B)}
{(b/s)+k\tan(k\epsilon_B)}.
\]

Status: essa é uma boa fórmula de primeiro teste, mas ainda não fecha o
espalhamento completo. É preciso incluir \(V_{\rm eff}^{B}\), canais parciais e
acoplamentos eletromagnéticos/fracos quando aplicável.

---

## 7. Estabilidade topológica do próton

A carga bariônica topológica é:

\[
\boxed{
B_{\rm top}
=
\frac{1}{24\pi^2}
\int_{\Sigma_B^\circ}
\operatorname{Tr}
\left(
\omega\wedge d\omega
+
\frac23\omega\wedge\omega\wedge\omega
\right).
}
\]

Para três estômatos confinados:

\[
B_{\rm top}=1.
\]

Como:

\[
\pi_3(S^3)\cong\mathbb Z,
\]

o próton não pode decair continuamente para o vácuo dentro do setor que
preserva a topologia.

Portanto:

\[
\boxed{
\Gamma_p=0
}
\]

no setor topologicamente conservativo.

Se forem admitidos processos não perturbativos que mudam a classe topológica,
a forma correta é:

\[
\Gamma_p\sim e^{-S_{\rm inst}}.
\]

Não se deve declarar um número específico de vida média sem calcular
\(S_{\rm inst}\).

---

## 8. Instabilidade do nêutron livre

O nêutron tem:

\[
B_{\rm top}=1,
\qquad
Q_n=0,
\qquad
J_n=\frac12.
\]

Ele é topologicamente bariônico, mas possui cisalhamento torsional antiparalelo:

\[
\delta_B=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
\]

Esse cisalhamento gera a diferença:

\[
M_n-M_p.
\]

O decaimento beta pode ser tratado como transição efetiva:

\[
n\to p+e^-+\bar\nu_e.
\]

No limite efetivo padrão:

\[
\Gamma_n
=
\frac{G_F^2(1+3g_A^2)}{2\pi^3}
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e.
\]

Na GDQ, para isso ser derivado e não importado, é preciso obter:

\[
G_F,
\qquad
g_A,
\qquad
\Delta M
\]

das integrais de acoplamento da cola quiral/torsional.

Neste momento, apenas \(\Delta M\) está estruturalmente derivado via
\(\delta_B\). \(G_F\) e \(g_A\) ainda são pendências.

---

## 9. Pendências deste bloco

1. calcular os modos radiais/torsionais além do \(\Delta\);
2. resolver numericamente \(V_{\rm eff}^{B}\) para fases parciais;
3. derivar \(G_F\) e \(g_A\) geometricamente para o decaimento do nêutron;
4. calcular ou limitar \(S_{\rm inst}\) se houver canais de decaimento do próton
   fora do setor conservativo.

Status:

\[
\boxed{
\text{dinâmica bariônica fechada estruturalmente; espectro completo e espalhamento numérico ficam posteriores.}
}
\]

# Q40 — Bloco 1 — Solução global colada do bárion

## 1. Objetivo

Este bloco fixa o objeto geométrico comum usado para derivar os observáveis
bariônicos. A meta é evitar que massa, carga, spin, raio, momentos magnéticos e
estabilidade sejam calculados por estruturas diferentes.

O bárion da GDQ deve ser tratado como uma solução colada:

\[
\boxed{
\mathfrak G_B=
\{\mathcal F_a,\Psi_{ab},\mathcal A_{ab},B_{ab},g_B,f_B\}_{a,b=1}^{3}.
}
\]

Aqui \(B=p,n\) distingue próton e nêutron.

---

## 2. Ponto de cautela: \(T^5\times S^3\)

O uso de \(T^5\times S^3\) não substitui a base local oficial da GDQ nem altera
a ação fundamental.

A interpretação correta é:

\[
\boxed{
T^5\times S^3
=
\text{ciclo interno/global efetivo de calibração bariônica}.
}
\]

A ação oficial permanece escrita no domínio Hermitiano da GDQ. O ciclo
\(T^5\times S^3\) entra como subestrutura global usada para extrair invariantes
de massa, holonomia, torção e carga do sóliton bariônico.

Portanto, não se deve escrever que:

\[
\mathcal M_{\mathbb C}\equiv T^5\times S^3
\]

como identidade fundamental geral. O correto é escrever:

\[
T^5\times S^3\subset_{\rm eff}\mathcal M_{\mathbb C}
\]

ou:

\[
\mathcal C_B\simeq T^5_{\rm trançado}\times S^3_{\rm hol}
\]

como setor/ciclo bariônico efetivo.

---

## 3. Câmaras de bulk

O bulk bariônico reduzido é decomposto em três câmaras:

\[
T^5_{\rm trançado}
=
\bigsqcup_{a=1}^{3}\mathcal F_a.
\]

Cada câmara é:

\[
\mathcal F_a
=
[0,2\pi]_{\phi_1}
\times
[0,\pi]_{\phi_2}
\times
[0,\pi]_{\phi_3}
\times
[0,\pi]_{\phi_4}
\times
[0,\pi]_{\phi_5}.
\]

Assim:

\[
\operatorname{Vol}(\mathcal F_a)=2\pi^5,
\]

e:

\[
\operatorname{Vol}(T^5_{\rm trançado})
=3(2\pi^5)=6\pi^5.
\]

Esse é o termo de bulk da massa do próton.

---

## 4. Dados locais em cada câmara

No interior de cada câmara:

\[
g_B^{(a)}=\sum_{A=1}^{5}d\phi_A^2,
\]

\[
f_B^{(a)}=f_0,
\]

\[
B^{(a)}=0.
\]

Logo:

\[
\mathcal R_{AB}=0,
\qquad
\nabla_A\nabla_B f_B=0.
\]

O setor de bulk satisfaz a equação estacionária reduzida:

\[
\mathcal R_{AB}+\nabla_A\nabla_B f_B=\lambda_B g_{AB},
\]

com:

\[
\lambda_B=0
\]

no interior plano de cada câmara.

Isso não significa que o bárion inteiro seja plano. A curvatura/torsão física
fica concentrada nas colas e gargantas.

---

## 5. Colagem global

O bárion físico não é a soma desconexa das três câmaras. Ele é obtido pelas
identificações:

\[
\Psi_{ab}:\partial\mathcal F_a\to\partial\mathcal F_b.
\]

Nas interfaces vivem:

\[
\mathcal A_{ab}\neq0,
\qquad
B_{ab}\neq0.
\]

Assim:

\[
\boxed{
B^{(a)}=0\text{ no interior,}
\qquad
B_{ab}\neq0\text{ na cola.}
}
\]

A torção é portanto termo de superfície/transgressão, não termo de volume.

---

## 6. Condição de compatibilidade de cociclo

Para que a colagem defina um objeto global, os mapas de transição devem
satisfazer uma condição de compatibilidade.

No caso trivial:

\[
\Psi_{ab}\circ\Psi_{bc}\circ\Psi_{ca}=\mathrm{id}.
\]

No caso bariônico, a composição pode carregar holonomia:

\[
\boxed{
\Psi_{ab}\circ\Psi_{bc}\circ\Psi_{ca}
=
\mathcal H_B.
}
\]

Para o próton:

\[
\mathcal H_p
\quad\text{codifica}\quad
Q_p=+1,\qquad J_p=\frac12.
\]

Para o nêutron:

\[
\mathcal H_n
\quad\text{codifica}\quad
Q_n=0,\qquad J_n=\frac12,
\]

com cisalhamento torsional antiparalelo adicional.

---

## 7. Massa como volume + superfície

A integral bariônica adimensional deve ser escrita como:

\[
\mathcal I_B
=
\mathcal I_B^{\rm bulk}
+
\mathcal I_B^{\partial}.
\]

Para o próton:

\[
\mathcal I_p^{\rm bulk}=6\pi^5.
\]

O termo de superfície é:

\[
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
\]

Logo:

\[
\boxed{
\frac{M_p}{M_e}
=
6\pi^5+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
\]

Para o nêutron:

\[
\mathcal I_n
=
\mathcal I_p+\delta_B,
\]

com:

\[
\delta_B=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
\]

Logo:

\[
\boxed{
\frac{M_n}{M_e}
=
6\pi^5+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
+
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

---

## 8. Lemas de fechamento estrutural

Para declarar a solução global colada fechada estruturalmente, adotam-se os
seguintes lemas, desenvolvidos nos adendos da Q40:

1. os mapas \(\Psi_{ab}\) preservam a medida reduzida por serem isometrias de
   fronteira do ciclo interno;
2. a composição de colas gera a holonomia bariônica \(\mathcal H_B\), que fixa
   \(Q_B\) e \(J_B\);
3. o termo de transgressão de superfície é
   \(\frac{3\pi}{2}+\frac{3}{4\pi^3}\);
4. o cisalhamento torsional do nêutron é
   \(\delta_B=\ln(2\pi^2)3\sqrt2/5\);
5. a Hessiana restrita às deformações que preservam \(B_{\rm top}=1\) é não
   negativa.

Status deste bloco:

\[
\boxed{
\text{estrutura global colada fechada em nível estrutural.}
}
\]

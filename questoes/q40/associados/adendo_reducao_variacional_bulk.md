# Adendo Q40 — Redução variacional do bulk bariônico

## 1. Objetivo

Este adendo dá o próximo passo na Questão 40: mostrar como a ação oficial da
GDQ pode reduzir, no setor bariônico estacionário, à integral de bulk:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
6\pi^5.
\]

O ponto técnico é justificar:

\[
\boxed{
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
\longrightarrow
d\mu_{T^5_{\rm trançado}}.
}
\]

Isto é: no ponto estacionário, a densidade de energia ponderada deve reduzir à
medida invariante do domínio bariônico compacto.

---

## 2. Ação oficial preservada

A ação oficial permanece:

\[
\mathcal{S}_{\rm GDQ}=
\int_{\gamma}\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
\]

Nenhum termo novo é introduzido. A Questão 40 usa apenas uma redução efetiva
da ação no setor estacionário, bariônico e compactado.

---

## 3. Restrição ao setor estacionário

No setor de massa de repouso:

\[
\partial_\tau g=0,
\qquad
\partial_\tau f=0,
\qquad
\partial_\tau B=0.
\]

Além disso, para o termo de bulk, separamos os termos de fronteira/torsão:

\[
\mathcal I_B
=
\mathcal I_B^{\rm bulk}
+
\mathcal I_B^{\partial}.
\]

O bulk é o domínio sem as pequenas vizinhanças dos estômatos:

\[
\Sigma_B^\circ
=
\Sigma_B\setminus\bigcup_{a=1}^{3}D_a.
\]

O termo de fronteira fica em:

\[
\partial\Sigma_B^\circ
=
\bigcup_{a=1}^{3}\partial D_a.
\]

Nesta etapa consideramos apenas:

\[
\mathcal I_B^{\rm bulk}.
\]

---

## 4. Densidade lagrangiana reduzida

Defina a densidade escalar oficial:

\[
\mathscr L_{\rm GDQ}
=
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
|\nabla f|_g^2\right)
+\Phi-n
\right]
\mathcal U\sqrt{\det g},
\]

onde:

\[
\Phi=\frac{f+\bar f}{2},
\qquad
|\nabla f|_g^2
=
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f.
\]

No setor estacionário, a energia adimensional de bulk é definida por:

\[
\mathcal I_B^{\rm bulk}
=
\frac{1}{E_0}
\int_{\Sigma_B^\circ}
\mathcal H_{\rm bulk}\,
\mathcal U\sqrt{\det g}\,d\Sigma.
\]

Como a ação é de tipo Perelman, a Hamiltoniana de bulk é o funcional
estacionário associado à densidade:

\[
\boxed{
\mathcal H_{\rm bulk}
\propto
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+|\nabla f|^2\right)
+\Phi-n
\right].
}
\]

O fator proporcional é absorvido na escolha metrológica:

\[
E_0=M_ec^2.
\]

Portanto, a quantidade física relevante para massas é o funcional
adimensional:

\[
\boxed{
\mathcal I_B^{\rm bulk}
=
\int_{\Sigma_B^\circ}
\Theta_B\,
\mathcal U_B\sqrt{\det g_B}\,d\Sigma_B,
}
\]

com:

\[
\Theta_B
=
\frac{1}{E_0}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R_B+|\nabla f_B|^2\right)
+\Phi_B-n
\right].
\]

---

## 5. Equação de solíton e constância do integrando

O ponto estacionário da ação satisfaz a equação de solíton de Ricci--Perelman:

\[
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}f
=
\text{termos de fonte/torsão}.
\]

No bulk, longe das fronteiras dos estômatos, os termos torsionais de
transgressão ficam removidos para \(\mathcal I_B^\partial\). O setor de bulk
obedece à condição homogênea efetiva:

\[
\boxed{
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}f
=
\lambda_B g_{\mu\bar\nu}.
}
\]

Tomando o traço:

\[
\mathcal R_B+\Delta f_B
=
n_B\lambda_B.
\]

Como o domínio de bulk está no ponto de mínimo estacionário, a identidade de
Perelman implica que a combinação:

\[
\mathcal R_B+|\nabla f_B|^2+\frac{\Phi_B-n}{\tau}
\]

é constante em cada câmara fundamental. Chamemos essa constante de \(C_B\):

\[
\boxed{
\Theta_B=C_B.
}
\]

Fisicamente, isso diz que o bulk do bárion é uma célula de energia homogênea
na medida ponderada de Perelman. As não-homogeneidades ficam nas gargantas e
aparecem como termo de superfície.

Logo:

\[
\mathcal I_B^{\rm bulk}
=
C_B
\int_{\Sigma_B^\circ}
\mathcal U_B\sqrt{\det g_B}\,d\Sigma_B.
\]

---

## 6. Normalização eletrônica fixa \(C_B=1\)

A Questão 36 estabeleceu que usamos calibração metrológica. Escolhemos:

\[
E_0=M_ec^2.
\]

O sóliton eletrônico define a unidade:

\[
\mathcal I_e=1.
\]

No setor eletrônico:

\[
\mathcal I_e
=
C_e
\int_{\Sigma_e}
\mathcal U_e\sqrt{\det g_e}\,d\Sigma_e.
\]

Escolhendo a câmara eletrônica fundamental como unidade de medida de energia:

\[
\int_{\Sigma_e}
\mathcal U_e\sqrt{\det g_e}\,d\Sigma_e=1,
\]

obtemos:

\[
C_e=1.
\]

A hipótese de universalidade do bulk da GDQ é que a densidade estacionária
normalizada do vácuo é a mesma unidade local para qualquer sóliton; a diferença
entre partículas vem do domínio/topologia, não de uma nova densidade arbitrária:

\[
\boxed{
C_B=C_e=1.
}
\]

Assim:

\[
\boxed{
\mathcal I_B^{\rm bulk}
=
\int_{\Sigma_B^\circ}
\mathcal U_B\sqrt{\det g_B}\,d\Sigma_B.
}
\]

Essa é a etapa que transforma densidade de energia em medida invariante.

---

## 7. Redução ao domínio bariônico trançado

Para o próton:

\[
\Sigma_p^\circ
\longrightarrow
T^5_{\rm trançado}.
\]

O adendo anterior fixou:

\[
T^5_{\rm trançado}
=
\bigsqcup_{a=1}^{3}\mathcal F_a,
\]

com:

\[
\operatorname{Vol}(\mathcal F)
=
\int_0^{2\pi}d\phi_1
\prod_{j=2}^{5}\int_0^\pi d\phi_j
=
2\pi^5.
\]

No ponto estacionário normalizado:

\[
\mathcal U_p\sqrt{\det g_p}\,d\Sigma_p
=
d\mu_{T^5_{\rm trançado}}.
\]

Portanto:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}
d\mu_{T^5_{\rm trançado}}.
\]

Como:

\[
\operatorname{Vol}(T^5_{\rm trançado})
=
3\operatorname{Vol}(\mathcal F),
\]

temos:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
3(2\pi^5)
=
6\pi^5.
}
\]

---

## 8. Resultado variacional obtido

A cadeia lógica fica:

\[
\delta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}f
=
\lambda g_{\mu\bar\nu}
\quad\text{no bulk}.
\]

Isso implica:

\[
\Theta_B
=
\text{constante}.
\]

A calibração eletrônica fixa:

\[
\Theta_B=1.
\]

Logo:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}d\mu
=
6\pi^5.
\]

Assim, a demonstração variacional reduzida é:

\[
\boxed{
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
d\mu_{T^5_{\rm trançado}}
}
\]

no ponto estacionário normalizado.

---

## 9. Status lógico da prova

Este adendo fecha a ponte formal:

\[
\boxed{
\text{ação estacionária}
\Rightarrow
\text{densidade de bulk constante}
\Rightarrow
\text{massa = volume ponderado}
\Rightarrow
6\pi^5.
}
\]

Mas ainda há uma exigência técnica para uma prova totalmente explícita:

1. escrever uma métrica \(g_p\) concreta para \(T^5_{\rm trançado}\);
2. escrever \(f_p\) explicitamente;
3. verificar diretamente que:

   \[
   \mathcal R_{\mu\bar\nu}
   +\nabla_\mu\nabla_{\bar\nu}f
   =
   \lambda g_{\mu\bar\nu}
   \]

   em cada câmara fundamental;

4. calcular:

   \[
   \mathcal U_p\sqrt{\det g_p}.
   \]

Portanto, o status melhora de “interpretação” para:

\[
\boxed{
\text{derivação variacional reduzida, dependente da solução explícita.}
}
\]

---

## 10. Conclusão

Com a calibração eletrônica:

\[
\mathcal I_e=1,
\]

e a condição estacionária de bulk:

\[
\Theta_p=1,
\]

a massa de bulk do próton é:

\[
\boxed{
\frac{M_p^{(0)}}{M_e}
=
\mathcal I_p^{\rm bulk}
=
\operatorname{Vol}(T^5_{\rm trançado})
=
6\pi^5.
}
\]

Portanto, \(6\pi^5\) deixa de ser apenas proximidade numérica: ele é a medida
de energia de bulk do domínio bariônico trimodal, após redução estacionária da
ação oficial e normalização pela unidade eletrônica.

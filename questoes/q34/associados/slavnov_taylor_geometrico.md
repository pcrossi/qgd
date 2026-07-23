# Q34 — Extensão não abeliana: Slavnov--Taylor como identidade geométrica

## 1. Objetivo

Este adendo estende o teste \(U(1)\) da Questão 34 para um setor efetivo não
abeliano \(G\), por exemplo \(SU(3)_C\), sem transformar fantasmas em ontologia
fundamental da GDQ.

A pergunta correta é:

\[
\boxed{
\text{o traço efetivo GDQ preserva a simetria de gauge após a escolha de seção
na órbita de conexões?}
}
\]

Na GDQ, fantasmas são variáveis auxiliares de auditoria do jacobiano da projeção
de gauge, não campos físicos fundamentais.

---

## 2. Espaço de conexões e órbitas de gauge

Seja \(P\to M\) um fibrado principal com grupo compacto \(G\). O campo de gauge
efetivo é uma conexão:

\[
A\in\mathcal A(P),
\qquad
F_A=dA+A\wedge A.
\]

O grupo de gauge \(\mathcal G\) age por:

\[
A\mapsto A^g=g^{-1}Ag+g^{-1}dg.
\]

A física vive no quociente:

\[
\boxed{
\mathcal A(P)/\mathcal G.
}
\]

Uma fixação de gauge é apenas uma escolha local de seção desse quociente.

---

## 3. Gauge de fundo e jacobiano geométrico

Decompomos:

\[
A=\bar A+a.
\]

Uma escolha natural é o gauge de fundo:

\[
\boxed{
F^a[A;\bar A]=\bar D^\mu a_\mu^a=0.
}
\]

O operador de Faddeev--Popov associado é:

\[
\boxed{
M_{\rm FP}^{ab}
=
-\bar D^\mu D_\mu^{ab}[A].
}
\]

O determinante:

\[
\boxed{
\Delta_{\rm FP}[A,\bar A]=\det M_{\rm FP}
}
\]

é o jacobiano da mudança de variáveis transversal/longitudinal na órbita de
gauge. Ele pode ser representado por campos fantasmas:

\[
\det M_{\rm FP}
=
\int D\bar cDc\,
\exp\left[-\int\bar c^aM_{\rm FP}^{ab}c^b\right],
\]

mas essa representação é auxiliar. A estrutura física continua sendo o
quociente geométrico \(\mathcal A/\mathcal G\).

---

## 4. Operador covariante GDQ

O operador efetivo deve ser função covariante da conexão:

\[
\boxed{
L_A=-D_A^2+\mathcal R_{\rm eff}(A,g,f,\Omega)+{\rm ad}(F_A).
}
\]

Sob gauge:

\[
\boxed{
L_{A^g}=g^{-1}L_Ag.
}
\]

Portanto o traço heat-kernel é invariante:

\[
\boxed{
{\rm Tr}\,F_\tau(L_{A^g})
=
{\rm Tr}\,F_\tau(L_A),
}
\]

para qualquer função admissível \(F_\tau\), em particular:

\[
F_\tau(L)=e^{-\tau L}
\qquad\text{ou}\qquad
F_\tau(L)=\int_\tau^\infty\frac{ds}{s}e^{-sL}.
\]

Essa é a origem geométrica da preservação de gauge.

---

## 5. Funcional efetivo gauge-fixado

O funcional efetivo de auditoria pode ser escrito como:

\[
\boxed{
e^{-\Gamma_\tau[\bar A]}
=
\int Da\,D\bar c\,Dc\,
\exp\left[
-S_{\rm GDQ}^{(2)}[\bar A,a]
-S_{\rm gf}[\bar A,a]
-S_{\rm gh}[\bar A,a,\bar c,c]
\right].
}
\]

Com:

\[
S_{\rm gf}
=
\frac{1}{2\xi}\int(\bar D^\mu a_\mu)^2,
\]

\[
S_{\rm gh}
=
\int\bar c^a(-\bar D^\mu D_\mu^{ab}[A])c^b.
\]

O heat-kernel entra nos operadores quadráticos:

\[
\boxed{
G_\tau(L)=e^{-\tau L}L^{-1}.
}
\]

Desde que os mesmos operadores covariantes sejam usados nos setores físico,
longitudinal e jacobiano, a simetria de gauge de fundo é preservada.

---

## 6. Identidade Slavnov--Taylor

Introduzindo fontes BRST externas \(K,L\) para auditar a simetria:

\[
sA_\mu^a=D_\mu^{ab}c^b,
\qquad
sc^a=-\frac12f^{abc}c^bc^c,
\qquad
s\bar c^a=\frac{1}{\xi}\bar D^\mu a_\mu^a,
\]

a invariância BRST do funcional gauge-fixado implica:

\[
\boxed{
\mathcal S(\Gamma_\tau)=0.
}
\]

Esquematicamente:

\[
\boxed{
\mathcal S(\Gamma_\tau)
=
\int d^4x
\left[
\frac{\delta\Gamma_\tau}{\delta A_\mu^a}
\frac{\delta\Gamma_\tau}{\delta K_\mu^a}
+
\frac{\delta\Gamma_\tau}{\delta c^a}
\frac{\delta\Gamma_\tau}{\delta L^a}
+
B^a\frac{\delta\Gamma_\tau}{\delta\bar c^a}
\right]
=0.
}
\]

Essa é a versão não abeliana da identidade de Ward. No limite abeliano,
\(f^{abc}=0\), ela reduz a:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

---

## 7. Termos locais permitidos

A expansão heat-kernel gera termos locais gauge-invariantes:

\[
\boxed{
\Gamma_{\tau,{\rm loc}}[A]
=
c_0(\tau)\int{\rm tr}\,\mathbf 1
+
c_F(\tau)\int{\rm tr}(F_{\mu\nu}F^{\mu\nu})
+
c_{DF}(\tau)\int{\rm tr}(D_\rho F_{\mu\nu}D^\rho F^{\mu\nu})
+\cdots
}
\]

Os coeficientes podem depender da geometria setorial, mas os operadores devem
ser invariantes de gauge. Portanto, a projeção finita não pode gerar termo de
massa local do tipo:

\[
\boxed{
m_A^2\int{\rm tr}(A_\mu A^\mu)
}
\]

sem quebra de gauge ou mecanismo geométrico explícito.

---

## 8. Independência admissível do kernel

Se o núcleo for deformado por uma função inteira admissível:

\[
F_\tau(L)\to F_\tau(L)+\delta F_\tau(L),
\]

com:

\[
\delta F_\tau(L_{A^g})=g^{-1}\delta F_\tau(L_A)g,
\]

então:

\[
{\rm Tr}\,\delta F_\tau(L_{A^g})
=
{\rm Tr}\,\delta F_\tau(L_A).
\]

Logo a identidade de gauge não depende do detalhe do kernel, mas da sua
covariância funcional. Mudanças admissíveis alteram coeficientes locais
efetivos, não a identidade Slavnov--Taylor.

---

## 9. Veredito

A Questão 34 fica fechada estruturalmente também no setor não abeliano:

\[
\boxed{
L_{A^g}=g^{-1}L_Ag
\quad\Rightarrow\quad
{\rm Tr}\,F_\tau(L_A)\text{ é gauge-invariante}
\quad\Rightarrow\quad
\mathcal S(\Gamma_\tau)=0.
}
\]

O que permanece para cálculo posterior não é a preservação formal de gauge, mas:

1. calcular coeficientes locais \(c_F(\tau),c_{DF}(\tau),\ldots\);
2. avaliar o jacobiano geométrico em fundos topológicos não triviais;
3. conectar o setor \(SU(3)_C\) a confinamento, lei de área e mass gap;
4. testar numericamente a independência sob classes admissíveis de kernel.

# Q34 — Teste mínimo de calibre em loops no setor \(U(1)\)

## 1. Objetivo

Este adendo define o cálculo mínimo que deve ser usado para auditar preservação
de calibre em loops na GDQ.

O setor \(U(1)\) é suficiente como primeiro teste porque:

1. evita a álgebra não abeliana;
2. testa diretamente a identidade de Ward;
3. conecta Q32 ao problema de loops;
4. prepara Q35, onde o polo de Landau é originalmente um problema da QED.

---

## 2. Campo de fundo e gauge

Usamos a decomposição:

\[
A_\mu=\bar A_\mu+a_\mu.
\]

No caso abeliano plano mínimo:

\[
\bar A_\mu=0.
\]

A fixação de gauge é:

\[
\boxed{
F[a]=\partial^\mu a_\mu=0.
}
\]

O termo de gauge-fixing é:

\[
\boxed{
S_{\rm gf}
=
\frac{1}{2\xi}
\int(\partial^\mu a_\mu)^2\,d^4x.
}
\]

No setor abeliano, o determinante de Faddeev--Popov é independente de \(A\):

\[
\boxed{
\Delta_{\rm FP}^{U(1)}=\det(-\partial^2).
}
\]

Portanto fantasmas não contribuem dinamicamente ao loop abeliano. Eles podem ser
mantidos apenas como auditoria do jacobiano de gauge.

---

## 3. Propagadores com núcleo GDQ

Pela Q32:

\[
G_\tau=e^{-\tau L^{(2)}}(L^{(2)})^{-1}.
\]

No limite plano:

\[
\boxed{
D_{\mu\nu}^{(\tau)}(k)
=
\frac{e^{-\tau k_E^2}}{k_E^2}
\left[
\delta_{\mu\nu}
-(1-\xi)\frac{k_\mu k_\nu}{k_E^2}
\right].
}
\]

Para férmions efetivos:

\[
\boxed{
S_\tau(k)
=
e^{-\tau(k_E^2+m^2)}
\frac{-i\slashed{k}+m}{k_E^2+m^2}.
}
\]

O exponencial é tradução plana do heat-kernel geométrico, não regulador
externo.

---

## 4. Polarização de vácuo

O teste mínimo é:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
-e^2
\int\frac{d^4k}{(2\pi)^4}
{\rm Tr}
\left[
\gamma_\mu S_\tau(k)\gamma_\nu S_\tau(k+q)
\right]
+\Pi_{\mu\nu}^{\rm loc}(q,\tau).
}
\]

\(\Pi_{\mu\nu}^{\rm loc}\) representa os termos locais finitos permitidos pela
projeção geométrica. Eles não são contratermos fundamentais para remover
infinitos; são coeficientes efetivos necessários para preservar a simetria na
leitura perturbativa.

A identidade de Ward exige:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

Equivalente:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
}
\]

---

## 5. Ponto técnico: o heat-kernel deve ser gauge-covariante

Um corte escrito como \(e^{-\tau k^2}\) em cada linha pode quebrar Ward se for
aplicado de forma não covariante.

A forma correta é:

\[
\boxed{
e^{-\tau L_A},
\qquad
L_A=-D_A^2+\mathcal R_{\rm eff}.
}
\]

No setor de matéria:

\[
\boxed{
e^{-\tau L_\psi},
\qquad
L_\psi=\slashed D_A^\dagger\slashed D_A+m^2.
}
\]

Com operadores covariantes, o traço funcional efetivo é:

\[
\boxed{
\Gamma_\tau[A]
=
-\log\det_\tau(\slashed D_A+m)
=
-\frac12{\rm Tr}
\int_{\tau}^{\infty}\frac{ds}{s}
e^{-sL_\psi}.
}
\]

Como \(L_\psi\) transforma por conjugação sob calibre, o traço é invariante:

\[
\Gamma_\tau[A^g]=\Gamma_\tau[A].
\]

Da invariância funcional segue:

\[
\boxed{
\partial_\mu
\frac{\delta\Gamma_\tau}{\delta A_\mu}=0,
}
\]

e, diferenciando duas vezes:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

Esta é a forma mais limpa de provar Ward sem transformar fantasmas em ontologia.

---

## 6. Termos locais permitidos

Em quatro dimensões, a projeção finita pode gerar:

\[
\boxed{
c_F(\tau)\int F_{\mu\nu}F^{\mu\nu},
\qquad
c_\psi(\tau)\int \bar\psi i\slashed D\psi,
\qquad
c_m(\tau)\int m\bar\psi\psi.
}
\]

No setor abeliano, Ward impõe:

\[
\boxed{
Z_1=Z_2
}
\]

na tradução perturbativa externa.

Na linguagem GDQ, isso significa que os coeficientes efetivos de vértice e
campo de matéria precisam vir do mesmo traço covariante, não de escolhas
independentes.

---

## 7. Veredito técnico da Q34

\[
\boxed{
\text{Q34 fica estruturalmente reduzida a um cálculo mínimo bem definido.}
}
\]

O que está estabelecido:

1. fixação de gauge \(U(1)\);
2. determinante FP abeliano como jacobiano não dinâmico;
3. propagadores heat-kernel vindos da Q32;
4. condição de Ward;
5. rota sem ontologia de fantasmas via traço covariante;
6. termos locais finitos compatíveis com gauge.

O que faltava antes da execução de `questoes/q34/associados/polarizacao_U1_heat_kernel.md`:

1. executar a integral de \(\Pi_{\mu\nu}^{(\tau)}\);
2. extrair explicitamente \(\Pi_\tau(q^2)\);
3. verificar transversalidade no resultado regularizado;
4. repetir para \(SU(3)\) com determinante/jacobiano não abeliano ou BRST;
5. mostrar independência de escolha admissível do kernel geométrico.

Após `questoes/q34/associados/polarizacao_U1_heat_kernel.md`, os itens 1--3 ficam resolvidos no
teste abeliano. Permanecem os itens 4--5 como extensão não abeliana e teste de
robustez do kernel.

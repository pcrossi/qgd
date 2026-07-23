# Polarização \(U(1)\) com heat-kernel covariante — núcleo comum de Q34/Q35

## 1. Objetivo

Este documento executa o cálculo mínimo exigido para as Questões 34 e 35:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2)
}
\]

com heat-kernel covariante. O objetivo é demonstrar:

1. preservação de Ward no setor \(U(1)\);
2. finitude ultravioleta para \(\tau>0\);
3. recuperação da QED em baixa energia;
4. evitação do polo de Landau como singularidade física fundamental.

---

## 2. Formulação covariante

O ponto de partida é o determinante fermiônico efetivo:

\[
\Gamma_\tau[A]
=
-\log\det_\tau(\slashed D_A+m).
\]

Usando a representação de Schwinger:

\[
\boxed{
\Gamma_\tau[A]
=
\frac12
{\rm Tr}
\int_\tau^\infty\frac{ds}{s}
e^{-sL_\psi[A]},
}
\]

onde:

\[
\boxed{
L_\psi[A]
=
\slashed D_A^\dagger\slashed D_A+m^2.
}
\]

No setor euclidiano plano:

\[
L_\psi[A]
=
-D_A^2
\frac{e}{2}\sigma^{\mu\nu}F_{\mu\nu}
m^2.
\]

Como \(L_\psi[A]\) transforma por conjugação sob transformação de calibre:

\[
L_\psi[A^g]=g^{-1}L_\psi[A]g,
\]

o traço é invariante:

\[
\boxed{
\Gamma_\tau[A^g]=\Gamma_\tau[A].
}
\]

Essa é a razão técnica pela qual Ward é preservada: o corte é covariante, não
um corte manual em componentes de momento.

---

## 3. Consequência funcional: identidade de Ward

Da invariância:

\[
\Gamma_\tau[A+\partial\lambda]=\Gamma_\tau[A],
\]

segue:

\[
0
=
\delta_\lambda\Gamma_\tau
=
\int d^4x\,
\frac{\delta\Gamma_\tau}{\delta A_\mu(x)}
\partial_\mu\lambda(x).
\]

Integrando por partes:

\[
\boxed{
\partial_\mu
\frac{\delta\Gamma_\tau}{\delta A_\mu(x)}
=0.
}
\]

Diferenciando uma segunda vez em \(A_\nu\) e indo para o espaço de momento:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

Logo, no setor \(U(1)\), a polarização tem necessariamente a forma:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
}
\]

Isso fecha a parte de calibre da Questão 34 no teste mínimo.

---

## 4. Função escalar \(\Pi_\tau(q^2)\)

O cálculo padrão por parâmetro de Feynman, com corte próprio-tempo inferior
\(\tau\), dá:

\[
\boxed{
\Pi_\tau(q^2)
=
\frac{2\alpha_0}{\pi}
\int_0^1 dx\,x(1-x)
\left[
E_1(\tau m^2)
-
E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right].
}
\]

Aqui:

\[
\boxed{
E_1(z)=\int_z^\infty\frac{e^{-t}}{t}\,dt.
}
\]

Esta expressão já está subtraída em \(q^2=0\), isto é:

\[
\boxed{
\Pi_\tau(0)=0.
}
\]

Essa escolha corresponde a calibrar a carga em escala infravermelha de
referência. Não é renormalização fundamental por contratermos; é definição
operacional da carga medida.

---

## 5. Baixa energia: recuperação da QED

Para:

\[
\tau[m^2+x(1-x)q_E^2]\ll1,
\]

usa-se:

\[
E_1(z)
=
-\gamma-\ln z+O(z).
\]

Logo:

\[
E_1(\tau m^2)
-
E_1(\tau[m^2+x(1-x)q_E^2])
=
\ln
\left(
\frac{m^2+x(1-x)q_E^2}{m^2}
\right)
+O(\tau q_E^2).
\]

Então:

\[
\boxed{
\Pi_\tau(q^2)
\to
\frac{2\alpha_0}{\pi}
\int_0^1 dx\,x(1-x)
\ln
\left(
1+\frac{x(1-x)q_E^2}{m^2}
\right).
}
\]

No regime \(q_E^2\gg m^2\), mas ainda abaixo da escala geométrica
\(\tau q_E^2\ll1\):

\[
\int_0^1x(1-x)\,dx=\frac16,
\]

e:

\[
\boxed{
\Pi_\tau(q^2)
\simeq
\frac{\alpha_0}{3\pi}\ln\frac{q_E^2}{m^2}
+\text{constante finita}.
}
\]

Portanto:

\[
\boxed{
\mathcal B_\alpha
\simeq
\frac{2}{3\pi}\alpha^2
}
\]

para um férmion de carga unitária, na janela em que a QED convencional é válida.
Com múltiplos férmions, multiplica-se por:

\[
\sum_fN_cQ_f^2.
\]

---

## 6. Ultravioleta geométrico: saturação finita

Para \(q_E^2\to\infty\) com \(\tau>0\) fixo:

\[
E_1(\tau[m^2+x(1-x)q_E^2])\to0
\]

exceto em regiões de borda de medida efetivamente nula. Assim:

\[
\boxed{
\Pi_\tau(\infty)
=
\frac{2\alpha_0}{\pi}
\left(\int_0^1dx\,x(1-x)\right)
E_1(\tau m^2).
}
\]

Logo:

\[
\boxed{
\Pi_\tau(\infty)
=
\frac{\alpha_0}{3\pi}E_1(\tau m^2).
}
\]

Este valor é finito para qualquer \(\tau>0\).

A carga efetiva definida por:

\[
\boxed{
\alpha_{\rm eff}(\mu)
=
\frac{\alpha_0}{1-\Pi_\tau(\mu^2)}
}
\]

tem limite:

\[
\boxed{
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}.
}
\]

Portanto não há polo físico se:

\[
\boxed{
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
}
\]

Como \(\alpha_0\simeq1/137\), essa condição é:

\[
\boxed{
E_1(\tau m^2)<\frac{3\pi}{\alpha_0}\approx1291.
}
\]

Para qualquer escala geométrica realista, essa desigualdade é extremamente
fraca. Mesmo se \(\tau m^2\ll1\):

\[
E_1(\tau m^2)\simeq-\gamma-\ln(\tau m^2),
\]

seria necessário um intervalo logarítmico absurdo para atingir o polo
perturbativo.

---

## 7. Interpretação GDQ

A GDQ não precisa dizer que existe uma renormalização fundamental. A leitura
correta é:

\[
\boxed{
\tau>0
\text{ é resolução geométrica do fluxo, não artifício externo.}
}
\]

Assim:

1. abaixo da escala geométrica, a leitura efetiva recupera QED;
2. perto da escala geométrica, o heat-kernel modifica a extrapolação pontual;
3. acima da escala geométrica, a noção de partícula pontual deixa de ser a
   variável fundamental;
4. o polo de Landau não aparece como singularidade física da GDQ.

---

## 8. Veredito para Q34

No setor \(U(1)\):

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0
}
\]

segue diretamente da invariância do traço heat-kernel covariante.

Portanto:

\[
\boxed{
\text{Q34 fica fechada no teste mínimo abeliano.}
}
\]

O setor não abeliano ainda exige a versão Slavnov--Taylor ou jacobiano
geométrico equivalente.

---

## 9. Veredito para Q35

A função:

\[
\boxed{
\Pi_\tau(q^2)
=
\frac{2\alpha_0}{\pi}
\int_0^1 dx\,x(1-x)
\left[
E_1(\tau m^2)
-
E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right]
}
\]

recupera QED em baixa energia e satura no ultravioleta:

\[
\boxed{
\Pi_\tau(\infty)
=
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<\infty.
}
\]

Assim:

\[
\boxed{
\text{o polo de Landau é evitado no setor }U(1)\text{ efetivo para }\tau>0,
\text{ desde que }
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
}
\]

Esse é o fechamento quantitativo mínimo da Q35 na tradução perturbativa
externa.

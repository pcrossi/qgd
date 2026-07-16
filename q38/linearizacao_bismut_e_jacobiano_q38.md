# Q38 — Linearização constitutiva de Bismut e jacobiano do canal gravitacional

## 1. Relação constitutiva já presente no texto

O Capítulo 17 e a nota 29.2 fixam a convenção

\[
\mathcal R_{\rm GDQ}
=R_{\rm LC}-\frac1{12}|H|^2
\]

e a torção de Bismut como função da estrutura Hermitiana:

\[
\boxed{
H(X,Y,Z)=d\omega(JX,JY,JZ),
\qquad
\omega(X,Y)=g(JX,Y).
}
\]

Assim, \(H\) não precisa ser acrescentado como novo campo independente à
ação oficial. A leitura compatível é que o símbolo \(\mathcal R\) da ação
oficial representa o escalar generalizado acima, com \(H=H[g,J]\).

## 2. Linearização

Considere

\[
g=g_*+h,
\qquad
J=J_*
\]

no setor Hermitiano que preserva a estrutura quase-complexa. Então

\[
\delta\omega_h(X,Y)=h(J_*X,Y)
\]

e

\[
\boxed{
\bigl(\delta H_h\bigr)(X,Y,Z)
=d\!\left(\delta\omega_h\right)(J_*X,J_*Y,J_*Z)
=:\bigl(D_Hh\bigr)(X,Y,Z).
}
\]

Em notação usual, a mesma expressão é \(\delta H_h=d^c\delta\omega_h\), até
o sinal escolhido para \(d^c\). Portanto, o mapa constitutivo que faltava é o
operador diferencial de primeira ordem

\[
\boxed{D_H:h\mapsto d^c[h(J_*\cdot,\cdot)].}
\]

Se \(J\) também flutuar, aparecem os termos

\[
d\omega_*(\delta J\,\cdot,J_*\cdot,J_*\cdot)+\text{permutações}.
\]

Q38 usa o setor Hermitiano de \(J\) fixo; esses termos pertencem a outro
bloco da Hessiana e não devem ser incluídos silenciosamente.

## 3. Contribuição torsional à Hessiana

O setor

\[
S_H=-\frac{\tau}{12}
\int |H[g,J_*]|_g^2,d\mu_{f,g}
\]

produz, na segunda variação,

\[
Q_H(h,h)
=-\frac{\tau}{12}
\int\left[
|D_Hh|^2
+\mathcal A_{H_*}(h,h)
\right]d\mu_{f_*,g_*}.
\]

\(\mathcal A_{H_*}\) reúne termos algébricos provenientes da variação dos
três inversos métricos de \(|H|^2\), da medida e da contração com o background
\(H_*\). O símbolo principal torsional é, portanto,

\[
\boxed{
L_H^{\rm prin}=-\frac16D_H^\dagger D_H,
}
\]

na convenção em que \(Q_H=\frac12\langle h,L_Hh\rangle\). A positividade não
é decidida por esse bloco isolado: ela pertence à soma com o operador de
Lichnerowicz--drift, exatamente como mostram as equações estacionárias do
Capítulo 17.

Logo, o bloco métrico físico usado em Q38 é

\[
\boxed{
L_{gg}^{B,\rm phys}
=\Pi_{\rm phys}
\left(
L_{\rm Lich,f}
-\frac16D_H^\dagger D_H
+\mathcal A_{H_*}
\right)
\Pi_{\rm phys}.
}
\]

Os operadores do Schur ficam agora definidos sem criar um setor novo:

\[
K_H=P_HL_{gg}^{B,\rm phys}P_H,
\quad
K_T=P_TL_{gg}^{B,\rm phys}P_T,
\quad
J=P_HL_{gg}^{B,\rm phys}P_T.
\]

## 4. Reconciliação das dimensões complexas

A teoria global usa \(n_{\mathbb C}=4\), isto é, oito dimensões reais. Na
redução gravitacional,

\[
\mathcal M_{\mathbb C}^{(4)}\longrightarrow N_{\mathbb R}^{(4)}\times
K_{\mathbb R}^{(4)},
\]

o setor interno \(K\) possui dimensão real quatro, equivalente a dimensão
complexa dois. Portanto, o \(n_{\mathbb C}=2\) do Apêndice 2 pode ser
interpretado como a fibra interna após a projeção, não como a dimensão global
da GDQ.

Essa distinção remove a contradição dimensional, mas não gera sozinha
\(\alpha^4\). O determinante de uma deformação \(D=\alpha I_2\) seria
\(\alpha^2\).

## 5. Quando a fibra complexa 2 produz \(\alpha^4\)

O manuscrito afirma que a conexão entra quadraticamente no estresse do canal.
Escreva a amplitude da conexão projetada como

\[
\mathcal A_B=\alpha\widehat{\mathcal A}_B.
\]

No setor isotrópico estacionário, o tensor de resposta quadrática tem a forma

\[
\mathcal Q_{a\bar b}
\propto
\mathcal F_{a c}\mathcal F_{\bar b}{}^c
=\alpha^2\widehat{\mathcal Q}_{a\bar b}.
\]

Se a normalização da sela satisfizer

\[
\widehat{\mathcal Q}_{a\bar b}=\widehat g_{a\bar b},
\]

o mapa do **canal transmitido**, e não o volume total do background, é

\[
D_{\rm tr}=\alpha^2I_2.
\]

Assim,

\[
\boxed{
J_{\rm tr}
=\det_{\mathbb C}D_{\rm tr}
=\det_{\mathbb C}(\alpha^2I_2)
=\alpha^4.
}
\]

Esta é a única reconciliação coerente com os dois enunciados existentes:

1. fibra interna de dimensão complexa dois;
2. resposta quadraticamente induzida pela conexão.

O teste variacional restante é verificar no background instantônico que
\(\widehat{\mathcal Q}_{a\bar b}=\widehat g_{a\bar b}\). Sem essa igualdade,
a expressão geral é

\[
J_{\rm tr}=\alpha^4\det_{\mathbb C}\widehat{\mathcal Q},
\]

e existe um fator geométrico adicional que não pode ser descartado.

## 6. O que ainda impede o número do determinante

A linearização constitutiva está agora definida. Para calcular
\(\mathcal P_{\rm GDQ}\), ainda faltam dados funcionais, não conceitos:

1. \(g_*\), \(f_*\) e \(H_*\) como perfis no domínio interno;
2. as bases normalizadas de \(P_H\) e \(P_T\);
3. o termo algébrico \(\mathcal A_{H_*}\) avaliado nesses perfis;
4. a extensão auto-adjunta determinada pela cola de contorno.

Sem esses quatro itens, qualquer valor numérico do prefator seria ajuste.

# Projeção da Hessiana oficial no ciclo de Noether

## 1. Objetivo

Avaliar diretamente o setor isotrópico responsável pelo fator angular do
momento magnético, sem inverter um operador radial ou escolher kernels.

## 2. Modo harmônico correto

No ciclo \(S^1\), com \(\vartheta\in[0,2\pi)\), o objeto físico não é o modo
zero escalar, que é gauge, mas a 1-forma harmônica normalizada

\[
h=\frac{d\vartheta}{2\pi},
\qquad
\oint_{S^1}h=1.
\]

Sua norma na métrica angular unitária é

\[
\boxed{
\langle h,h\rangle
=\int_0^{2\pi}\frac{d\vartheta}{(2\pi)^2}
=\frac1{2\pi}.
}
\]

Uma circulação de Noether \(C\) possui componente harmônica

\[
a_C=C h.
\]

Logo,

\[
\boxed{
\|a_C\|^2=\frac{C^2}{2\pi}.
}
\]

## 3. Redução da ação oficial

Escrevendo \(f=F+iS_R/\hbar\), a parte de fase da ação oficial reduzida no
ciclo tem a forma

\[
S_{\rm fase}^{(2)}
=\frac{K_C}{2}\langle a,a\rangle,
\]

onde \(K_C>0\) reúne a integração transversal, \(\tau\), \(\mathcal U\), a
métrica e \(\Lambda_C\). No setor harmônico, \(a=xh\), portanto

\[
S_{\rm harm}^{(2)}(x)
=\frac{K_C}{4\pi}x^2.
\]

A Hessiana reduzida é

\[
\boxed{
H_{\rm harm}=\frac{K_C}{2\pi}.
}
\]

Impondo \(x=C\) com multiplicador \(\lambda\):

\[
\mathscr I_0(x,\lambda)
=\frac{K_C}{4\pi}x^2-\lambda(x-C).
\]

A solução livre é

\[
x=C,
\qquad
\lambda_0=\frac{K_C}{2\pi}C.
\]

O denominador \(2\pi\) é, portanto, consequência direta da Hessiana oficial
projetada na 1-forma harmônica.

## 4. Fonte magnética geral

Se a projeção harmônica da fonte externa é \(j_BB\), o funcional é

\[
\mathscr I_B
=\frac{K_C}{4\pi}x^2-j_BBx-\lambda(x-C).
\]

As equações dão

\[
x=C,
\qquad
\boxed{
\lambda(B)=\frac{K_C}{2\pi}C-j_BB.
}
\]

Assim,

\[
\boxed{
-\frac{\partial\lambda}{\partial B}=j_B.
}
\]

Esse cálculo confirma que a resposta do multiplicador é exatamente a
projeção da fonte no modo harmônico.

## 5. Separação mínima e geométrica

Escreva

\[
j_B=\gamma_0+\Delta\gamma_{\rm geom}.
\]

A dupla cobertura e a normalização eletromagnética fixam

\[
\gamma_0=\frac q{mc}.
\]

Uma auto-resposta geométrica elementar com intensidade adimensional \(\alpha\)
e suportada pela mesma forma harmônica possui projeção

\[
\Delta\gamma_{\rm geom}
=\alpha\gamma_0\langle h,h\rangle.
\]

Como \(\langle h,h\rangle=1/(2\pi)\), segue

\[
\boxed{
\Delta\gamma_{\rm geom}
=\gamma_0\frac\alpha{2\pi}.
}
\]

Portanto,

\[
\boxed{
-\frac{\partial\lambda}{\partial B}
=\frac q{mc}\left(1+\frac\alpha{2\pi}\right)
}
\]

e

\[
\boxed{
g_{\rm GDQ}^{(1)}
=2\left(1+\frac\alpha{2\pi}\right).
}
\]

## 6. O que foi calculado e o que é entrada constitutiva

Foram calculados diretamente da projeção da ação:

1. o modo físico é a 1-forma harmônica \(h\), não o modo zero escalar;
2. \(\langle h,h\rangle=1/(2\pi)\);
3. \(H_{\rm harm}=K_C/(2\pi)\);
4. a resposta magnética é \(-\partial_B\lambda=j_B\).

A igualdade

\[
\Delta\gamma_{\rm geom}
=\alpha\gamma_0\langle h,h\rangle
\]

é válida se a auto-resposta eletrogeométrica elementar projetar-se uma vez no
mesmo modo harmônico. A ação oficial escrita apenas em \((g,f,\bar f)\), sem
o mapa explícito do setor eletromagnético para essa auto-resposta, não fixa
sozinha o numerador \(\alpha\gamma_0\). Esse numerador deve vir da conexão de
Chern acoplada ou da derivação geométrica de \(\alpha\) já realizada no setor
eletromagnético da GDQ.

Portanto, o fator angular \(1/(2\pi)\) está demonstrado; a prova integral do
produto \(\alpha/(2\pi)\) requer citar ou inserir explicitamente o mapa que
identifica a intensidade da auto-resposta como \(\alpha\).

## 7. Fechamento do numerador pelo setor geométrico de \(\alpha\)

O Capítulo 29 identifica \(\alpha\) como a razão entre a energia de deformação
topológica da carga e a rigidez elástica \(\hbar c\), fornecendo

\[
\alpha_{\rm GDQ}
=\frac{9}{8\pi^4}
\left(\frac{\pi^5}{1920}\right)^{1/4}.
\]

Essa é precisamente a intensidade adimensional exigida no numerador da
auto-resposta harmônica. Assim, dentro do dicionário entre o setor
eletromagnético do Capítulo 29 e a conexão de fase usada aqui,

\[
\Delta\gamma_{\rm geom}
=\gamma_0\alpha_{\rm GDQ}\langle h,h\rangle
=\gamma_0\frac{\alpha_{\rm GDQ}}{2\pi}.
\]

O fechamento é interno à GDQ desde que essa identificação de normalização seja
mantida: a mesma \(\alpha_{\rm GDQ}\) que mede a deformação de um vórtice de
carga deve multiplicar sua auto-resposta magnética harmônica.

## 8. Resultado numérico independente

Da fórmula geométrica do Capítulo 29:

\[
\alpha_{\rm GDQ}=0.007297348130032,
\qquad
\alpha_{\rm GDQ}^{-1}=137.036082448164.
\]

Consequentemente,

\[
\frac{\alpha_{\rm GDQ}}{2\pi}
=0.001161409026357,
\]

e

\[
\boxed{
g_{\rm GDQ}^{(1)}=2.002322818052714.
}
\]

Esse é o valor líder inteiramente interno da GDQ. Comparado com
\(g_e\simeq2.00231930436092\), fica acima por

\[
3.51369\times10^{-6},
\]

ou aproximadamente \(1.755\) ppm em \(g\). Essa diferença é compatível com o
fato de a expressão reter apenas o primeiro vestido geométrico.

## 9. Avaliação usando \(\alpha\) metrológica apenas para comparação

Para \(\alpha^{-1}=137.035999177\):

\[
\frac\alpha{2\pi}=0.001161409732098,
\]

\[
\boxed{
g_{\rm GDQ}^{(1)}=2.002322819464196.
}
\]

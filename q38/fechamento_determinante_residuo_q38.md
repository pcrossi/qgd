# Q38 — Determinante Kähler e auditoria do resíduo

## 1. Origem condicional de \(\alpha^4\)

Se o setor interno usado na redução gravitacional for o setor global de
dimensão complexa quatro, no background estacionário isotrópico pode-se
escrever a deformação Hermitiana como

\[
g^{(*)}_{a\bar b}=\alpha\,\widehat g_{a\bar b},
\qquad a,b=1,\ldots,4.
\]

Então

\[
\det_{\mathbb C}g^{(*)}
=\det_{\mathbb C}(\alpha\widehat g)
=\alpha^4\det_{\mathbb C}\widehat g.
\]

Para uma métrica Hermitiana, a forma de volume real coincide, a menos da
convenção constante já absorvida na normalização, com o determinante complexo:

\[
d\mu_{g_*}
=\frac{\omega_*^4}{4!}
=\det_{\mathbb C}(g^{(*)}_{a\bar b}),d^8x.
\]

Consequentemente,

\[
\boxed{
\frac{d\mu_{g_*}}{d\mu_{\widehat g}}=\alpha^4.
}
\]

Sob essas hipóteses, a quarta potência é consequência da dimensão complexa
quatro da forma de volume Kähler. Entretanto, o Apêndice 2 e o Capítulo 22
declaram que o setor gravitacional relevante tem dimensão complexa dois. Nesse
caso uma deformação \(g_*=\alpha\widehat g\) produz \(\alpha^2\), não
\(\alpha^4\). A incompatibilidade e o critério correto
\(J_g=\det_{\mathbb C}(\widehat g^{-1}g_*)\) estão auditados em
`q38/auditoria_operadores_oficiais_q38.md`.

Esta derivação exige que a solução estacionária imponha a deformação uniforme
\(g_* = \alpha\widehat g\). Para um background anisotrópico, a expressão geral
é

\[
\det_{\mathbb C}(\widehat g^{-1}g_*)
=\prod_{a=1}^4\alpha_a,
\]

e só reduz a \(\alpha^4\) quando \(\alpha_a=\alpha\) para os quatro modos.

## 2. Teste da hipótese de superfície bariônica

Q40 deriva

\[
M_B^{(0)}/M_e=6\pi^5
\]

e

\[
\Delta M_B^\partial/M_e
=\alpha\left(\frac{3\pi}{2}+\frac{3}{4\pi^3}\right).
\]

Logo, a fração de superfície prevista por essa decomposição é

\[
\delta_{\partial,Q40}
=\frac{\Delta M_B^\partial}{M_B^{(0)}}
=\frac{\alpha(3\pi/2+3/(4\pi^3))}{6\pi^5}
=1.88247454\times10^{-5}.
\]

Isto é,

\[
\boxed{\delta_{\partial,Q40}=0.00188247\%.}
\]

Já o resíduo de Q38 corresponderia, se interpretado como massa, a

\[
\delta_{\partial,Q38}^{\rm req}=0.13366325\%.
\]

A razão é

\[
\frac{\delta_{\partial,Q38}^{\rm req}}
{\delta_{\partial,Q40}}
=71.0040.
\]

Portanto:

\[
\boxed{
\text{a superfície torsional de massa derivada em Q40 não explica o resíduo de Q38.}
}
\]

Usá-la dessa forma misturaria duas definições distintas de massa nua e ainda
criaria uma inconsistência com a fórmula bariônica já consolidada.

## 3. Local correto do resíduo

A aproximação usada até aqui reteve somente a ação clássica da sela:

\[
Z_{\rm inst}^{(0)}=e^{-S_{\rm inst}/\hbar}.
\]

A expansão estacionária completa contém também o prefator de flutuações:

\[
Z_{\rm inst}
=e^{-S_{\rm inst}/\hbar}\,
\mathcal P_{\rm 1-loop}^{\rm GDQ},
\]

com

\[
\boxed{
\mathcal P_{\rm 1-loop}^{\rm GDQ}
=\left[
\frac{\det{}'K_{\rm eff}^{\rm inst}}
{\det K_{\rm eff}^{(0)}}
\right]^{-1/2}
\frac{\det K_{\rm gh}^{\rm inst}}
{\det K_{\rm gh}^{(0)}}
}
\]

e

\[
K_{\rm eff}=K_H-JK_T^{-1}J^\dagger.
\]

Aqui o determinante com linha exclui modos zero coletivos. \(K_{\rm gh}\)
representa o jacobiano geométrico da órbita de gauge; se a formulação GDQ
elimina fantasmas por construção, o mesmo fator deve ser obtido diretamente
da medida reduzida, e não omitido.

A previsão completa torna-se

\[
\Pi_1^{\rm GDQ}
=\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}^{\rm bulk}}
e^{-1/(2\alpha)}
\mathcal P_{\rm 1-loop}^{\rm GDQ}.
\]

O valor exigido pelos dados,

\[
\mathcal P_{\rm req}=1.00267505\ldots,
\]

é apenas um diagnóstico posterior. Ele não pode ser imposto ao determinante.
O cálculo preditivo deve obter \(\mathcal P_{\rm 1-loop}^{\rm GDQ}\) dos
espectros de \(K_{\rm eff}^{\rm inst}\) e \(K_{\rm eff}^{(0)}\), usando as
mesmas condições Robin--regularidade.

## 4. Prescrição espectral sem pós-ajuste

Para cada operador positivo \(K\), defina

\[
\zeta_K(s)=\sum_{\lambda_n>0}\lambda_n^{-s},
\qquad
\log\det{}'K=-\zeta_K'(0).
\]

Equivalentemente, por heat kernel,

\[
\log\frac{\det{}'K_1}{\det K_0}
=-\int_0^\infty\frac{dt}{t}
\left[
\operatorname{Tr}'e^{-tK_1}-\operatorname{Tr}e^{-tK_0}
\right],
\]

onde a subtração entre backgrounds torna explícito quais coeficientes locais
se cancelam. A sequência operacional é:

1. inserir \(\mathcal A_B^{\rm inst}\) em \(D_B\);
2. discretizar \(K_H\), \(K_T\) e \(J\) com o mesmo domínio e contorno;
3. formar o Schur para a sela e para o vácuo;
4. remover apenas os modos zero identificados por simetria;
5. calcular a diferença de log-determinantes;
6. comparar o prefator previsto com \(1.00267505\), somente ao final.

## 5. Status

Ficam agora resolvidos:

1. a origem determinantal **condicional** de \(\alpha^4\), junto da
   identificação da inconsistência entre dimensão complexa dois e quatro;
2. a exclusão quantitativa da superfície de massa Q40 como explicação do
   resíduo;
3. a identificação formal do termo realmente ausente: o determinante de
   flutuações do Schur.

Ainda falta uma entrada que os documentos atuais não fornecem numericamente:
os potenciais completos \(V_H(g_*,f_*,H_*)\), \(Z_T^{\rm Rob}\) e o mapa de
cola \(\mathcal C_\partial\) no background instantônico e no vácuo. Sem esses
operadores não existe avaliação honesta do determinante, apenas engenharia
inversa do seu valor.

A auditoria adicional em `q38/auditoria_background_estacionario_q38.md`
mostrou que o modo constante do solver atual não é uma solução demonstrada do
sistema estacionário global. Portanto, os backgrounds de sela precisam ser
resolvidos antes da avaliação desses operadores.

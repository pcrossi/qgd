# Q38 — Auditoria do background estacionário usado no determinante

## 1. Descoberta

O solver auditado de Q38 usa a equação radial

\[
f''+2\cot\chi\,f'=0
\]

e, sob contornos regulares, obtém o modo constante

\[
f(\chi)=S_{\rm inst}.
\]

Esse modo é suficiente para conferir a aritmética de
\(e^{-1/(2\alpha)}\), Fano e normalização radial. Ele não demonstra que
\((g_*,f_*,H_*)\) resolve simultaneamente todas as equações estacionárias da
ação.

O arquivo `src/solve_dilaton.py`, construído para a ação restrita e o vínculo
constitutivo antigo, obtém no background estático \(b=1\):

\[
\ddot u+\frac32u=0,
\qquad
u=e^{-f/2}.
\]

Toda solução real não trivial possui zeros, nos quais \(f=-2\log|u|\)
diverge. Logo, naquele setor restrito não existe dilaton global positivo e
regular sobre toda a evolução.

## 2. O que isso significa para Q38

Não há contradição direta entre as duas EDOs: elas são reduções diferentes.
A primeira é radial e fixa a média instantônica; a segunda inclui a direção
de evolução do background cosmológico e o vínculo da imersão. O erro seria
usar a solução da primeira como se ela resolvesse automaticamente a segunda.

Consequentemente:

\[
\boxed{
\text{o solver Q38 atual é uma auditoria de normalização, não uma sela global.}
}
\]

Um determinante semiclassico só é fisicamente definido em torno de uma sela:

\[
\left.\frac{\delta\mathcal S_{\rm GDQ}}{\delta g}\right|_*=0,
\quad
\left.\frac{\delta\mathcal S_{\rm GDQ}}{\delta f}\right|_*=0,
\quad
H_*=d^c\omega_*.
\]

Se o termo linear da expansão não se anula, a razão de determinantes depende
da escolha artificial do ponto de expansão.

## 3. Sistema estacionário correto

Com a convenção torsional já presente no Capítulo 17, a sela deve satisfazer

\[
R_{ij}-\frac14H_{ikm}H_j{}^{km}
+\nabla_i\nabla_jf
=\frac{1}{2\sigma}g_{ij},
\]

\[
d_f^\dagger H
:=d^\dagger H+i_{\nabla f}H=0,
\]

\[
H=d^c\omega,
\qquad
\int e^{-f}dV=1,
\]

acrescido das condições de cola no estômato. Esse é o background que deve
ser usado em \(K_{\rm eff}^{\rm inst}\). O vácuo de referência deve obedecer
ao mesmo sistema, na classe topológica trivial e com a mesma normalização.

## 4. Como remover o bloqueio sem mudar a ação

O próprio diagnóstico antigo identifica que o problema surge do vínculo que
fixa simultaneamente a imersão e \(b=1\). Não é necessário alterar a ação
oficial. É preciso evitar impor uma redução incompatível antes da variação.

A ordem correta é:

1. variar \(g\), \(f\) e a imersão/projeção permitida pela construção;
2. resolver o sistema estacionário torsional;
3. somente depois escolher a representação de Einstein e a fatia física;
4. normalizar os modos Hopf e toroidais nesse fundo;
5. calcular o determinante.

Se a imersão for por definição um dado fixo da teoria, e não uma variável,
então é necessário demonstrar que existe outra solução global regular dentro
desse vínculo. O arquivo atual não a fornece.

## 5. Consequência para o status da Q38

Q38 possui agora:

1. fórmula clássica reduzida consistente;
2. classe topológica local do meio-instantão;
3. Hessiana constitutiva formal de Bismut;
4. definição espectral correta do prefator;
5. auditoria do resíduo sem pós-ajuste.

Mas o cálculo do prefator deve esperar a solução global da sela. O próximo
objeto matemático não é um novo fator corretivo: é o par de backgrounds

\[
(g_*,f_*,H_*)_{\rm inst},
\qquad
(g_*,f_*,H_*)_0.
\]

Uma solução explícita do background assintótico comum foi construída em
`q38/solucao_background_estacionario_q38.md`, usando a superfície de Hopf
\(S^3\times S^1\) com torção canônica, multiplicada por \(T^4\). Ainda falta
resolver a retroação local do meio-instantão antes do determinante espectral.

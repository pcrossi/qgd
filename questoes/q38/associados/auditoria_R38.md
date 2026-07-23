# Auditoria de `questoes/q38/historico/R38.md`

## Veredito

`questoes/q38/historico/R38.md` identifica corretamente o tipo de mecanismo que seria necessário
para escapar do teorema de anulação do setor suave: um defeito causal deve
produzir uma condição de salto e um termo \((z-z_*)^{-1}\). Entretanto, o
arquivo ainda **não deriva esse mecanismo da ação oficial**. A conclusão
“temos gravidade” não segue dos cálculos apresentados.

\[
\boxed{\text{R38 é um ansatz exploratório; Q38 continua numericamente aberta.}}
\]

## 1. Variável causal incorreta

O documento usa \(z=x^0+ix^4\), mas a definição consolidada da GDQ é

\[
z_\tau=\tau+i\nu_0t,
\]

pois \(\tau\) e \(\nu_0t\) têm dimensão \(L^2\). A identificação de R38 não
preserva essa estrutura nem suas dimensões.

## 2. Grau diferencial incorreto da torção

A torção de Bismut é uma 3-forma,

\[
H=d^c\omega\in\Omega^3(M).
\]

O script define apenas \(H_{r\theta}\), componente de uma 2-forma. Logo, a
quantidade calculada não é a torção de Bismut usada em
\(R-|H|^2/12\). Para um colar com fibra \(S^1\) ou ciclo interno apropriado,
seria necessário, por exemplo, um componente \(H_{r\theta a}\), e o fluxo
topológico deveria ser integrado sobre um 3-ciclo.

## 3. Perfis postulados, não derivados

As escolhas

\[
f=Q_{\rm dil}\log r,
\qquad
H_{r\theta}=H_0r^{-Q_{\rm dil}-1}
\]

não foram obtidas das equações de Euler--Lagrange da ação oficial. Os novos
coeficientes \(Q_{\rm dil}\) e \(H_0\) permanecem livres. Assim, mesmo que o
fluxo fosse matematicamente correto, ele não produziria uma previsão.

## 4. A corrente não foi extraída da ação

O script chama

\[
-\frac1{\sqrt g}\partial_r(\sqrt g H_{r\theta})
\]

de corrente de Bismut. Essa expressão é uma divergência escolhida para o
ansatz; não é a corrente de Noether nem o termo de bordo obtido pela primeira
variação da ação oficial com \(H=d^c\omega(g,J)\). Em particular, como \(H\)
é constitutivo, não se pode variá-lo como campo independente.

## 5. O fluxo calculado não é topológico

O resultado

\[
Q_{\rm geom}=2\sqrt2\pi H_0\epsilon^{-Q_{\rm dil}}
\]

depende continuamente de \(H_0\), \(Q_{\rm dil}\) e \(\epsilon\). Portanto,
ele não é, na forma apresentada, um número de Hopf ou uma carga integral
quantizada. Além disso, o script avalia \(r\to\epsilon\), e não o limite da
punção \(r\to0\). A métrica

\[
ds^2=dr^2+(r^2+\epsilon^2)d\theta^2
\]

descreve uma garganta com círculo mínimo de raio \(\epsilon\), não um defeito
pontual no qual o disco colapsa.

## 6. A equação que gera o polo foi assumida

O passo central

\[
\bar\partial F_R=Q_{\rm geom}\delta^{(2)}(z-z_*)
\]

não foi deduzido. O \(F_R\) oficial é

\[
F_R(z)=\int_K\eta_Re^{2A}\mathcal U\,dV_K.
\]

É necessário demonstrar que a variação da ação e a integração do colar
transformam precisamente essa esperança geométrica em solução da equação de
Dolbeault com fonte. O script, ao definir diretamente
\(F_R=Q_{\rm geom}/(\pi z)\), calcula o resíduo da função que ele próprio
postulou.

## 7. Inconsistência de fase e fatores de \(\pi\)

Se

\[
\operatorname{Res}F_R=\frac{Q_{\rm geom}}\pi,
\]

então a fórmula do contorno fornece

\[
C_R
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\left(2\pi i\frac{Q_{\rm geom}}\pi\right)
=\frac{2\hbar}{\Lambda_C^2}\operatorname{Re}(iQ_{\rm geom}).
\]

R38 alterna essa expressão com
\(2\pi\hbar\operatorname{Re}(iQ_{\rm geom})/\Lambda_C^2\) e o script usa
\(2\hbar Q_{\rm geom}/\Lambda_C^2\), removendo tanto a operação de realidade
quanto o fator \(i\). Para \(Q_{\rm geom}\) real, como declarado no script,

\[
\operatorname{Re}(iQ_{\rm geom})=0.
\]

Logo, sob a prescrição física consolidada, o ansatz apresentado ainda produz
\(C_R=0\). É necessário derivar uma fase causal imaginária do resíduo ou
corrigir explicitamente a normalização/orientação da ação; isso não pode ser
feito silenciosamente.

## 8. Uso de uma ação diferente e circularidade

R38 substitui a ação oficial por

\[
S=S_{EH}+S_\Psi+S_B,
\]

que não é a ação oficial fornecida. Também propõe um termo GHY contendo
\(1/G\). Usar um termo cujo coeficiente já contém \(G\) para derivar \(G\) é
circular. Uma extensão da ação seria uma nova hipótese teórica e contrariaria
a exigência de mantê-la intacta.

## 9. O que o script realmente demonstra

O `solve_stoma_jump.py` verifica corretamente apenas a álgebra seguinte:

1. dado o perfil postulado de uma 2-forma;
2. dado o raio de avaliação \(r=\epsilon\);
3. dado diretamente \(F_R=Q/(\pi z)\);
4. a integração e o resíduo simbólicos têm os valores impressos.

Isso é uma verificação interna do ansatz, não uma solução das equações GDQ.

## 10. Correção necessária

Para transformar a ideia em prova, devem ser executados, nesta ordem:

1. escrever um colar real de dimensão compatível, com 3-forma
   \(H=d^c\omega(g,J)\);
2. substituir esse ansatz na ação oficial, sem acrescentar \(S_B\) ou GHY;
3. variar \((g,f)\), incluindo todos os termos de bordo induzidos pela
   curvatura e pela dependência constitutiva de \(H\);
4. resolver as equações radiais e determinar \(H_0,Q_{\rm dil}\) pelas
   condições de regularidade e topologia;
5. calcular o fluxo da forma correta sobre um 3-ciclo e provar sua
   quantização;
6. derivar, e não assumir, a equação distribucional obedecida pelo
   \(F_R\) oficial;
7. determinar a fase causal do resíduo e somente então avaliar \(C_R\).

Até que esses passos sejam feitos, a frase correta é:

\[
\boxed{\text{o estômato é um candidato a fonte do resíduo gravitacional,
mas o resíduo não foi derivado.}}
\]

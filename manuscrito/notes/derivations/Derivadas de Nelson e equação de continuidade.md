---
title: "Derivadas de Nelson e equação de continuidade"
tipo: derivacao
status: reducao-estocastica
---

# Derivadas de Nelson e equação de continuidade

## 1. Processo progressivo

Considere, em espaço plano e com coeficiente constante $\nu>0$,

$$
dX_t=b_+(X_t,t)dt+\sqrt{2\nu}\,dW_t.
$$

Para uma função teste suave $F$, a fórmula de Itô fornece o gerador

$$
D_+F
=\partial_tF+b_+\cdot\nabla F+\nu\Delta F.
$$

A densidade $\rho$ satisfaz a equação de Fokker--Planck progressiva

$$
\partial_t\rho
=-\nabla\cdot(b_+\rho)+\nu\Delta\rho.
$$

## 2. Processo regressivo

A descrição condicionada ao futuro possui deriva regressiva $b_-$ e gerador

$$
D_-F
=\partial_tF+b_-\cdot\nabla F-\nu\Delta F.
$$

A mesma densidade satisfaz

$$
\partial_t\rho
=-\nabla\cdot(b_-\rho)-\nu\Delta\rho.
$$

Os sinais opostos do laplaciano codificam as duas orientações condicionais;
eles não representam dois processos físicos independentes.

## 3. Velocidades de corrente e osmótica

Defina

$$
v=\frac{b_++b_-}{2}
$$

e

$$
u=\frac{b_+-b_-}{2}.
$$

Somando as duas equações de Fokker--Planck e dividindo por dois,

$$
\boxed{
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
$$

Subtraindo-as,

$$
0
=-\nabla\cdot[(b_+-b_-)\rho]+2\nu\Delta\rho.
$$

Logo,

$$
\nabla\cdot(\rho u-\nu\nabla\rho)=0.
$$

Sob decaimento adequado no infinito, ou com fluxo normal nulo no bordo e sem
componente solenoidal adicional, segue

$$
\rho u=\nu\nabla\rho,
$$

isto é,

$$
\boxed{
u=\nu\nabla\ln\rho.
}
$$

A última igualdade requer as condições globais declaradas. A equação de
divergência, e não a igualdade pontual, é o resultado geral sem hipóteses
adicionais.

## 4. Aceleração simétrica

Uma escolha reversível de aceleração média é

$$
a
=\frac12(D_+D_-+D_-D_+)X_t.
$$

Usando $b_\pm=v\pm u$, obtém-se

$$
a
=\partial_tv+(v\cdot\nabla)v
-(u\cdot\nabla)u
-\nu\Delta u.
$$

Se $v=\nabla S/m$, $u=\nu\nabla\ln\rho$ e a força média é conservativa,
$ma=-\nabla V$, a integração espacial dessa equação conduz à equação de
Hamilton--Jacobi com o termo quântico, até uma função apenas do tempo que pode
ser absorvida em $S$.

## 5. Estatuto na GDQ

Essas identidades pertencem à redução estocástica de Nelson. Na GDQ, elas
servem como teste do limite hidrodinâmico. Para constituírem uma derivação
fundamental, $b_\pm$, $\nu$ e a aceleração simétrica devem emergir da ação
oficial e da prescrição causal, em vez de serem postulados separadamente.

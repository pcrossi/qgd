---
title: "Estrutura Hermitiana, Kähler e conexão de Bismut"
tipo: derivacao
status: definicao-geometrica
---

# Estrutura Hermitiana, Kähler e conexão de Bismut

## 1. Estrutura Hermitiana

Uma estrutura quase-complexa é um endomorfismo

$$
J:TM\to TM
$$

tal que

$$
J^2=-I.
$$

Quando seu tensor de Nijenhuis se anula, $J$ é integrável. Uma métrica $g$ é
Hermitiana quando

$$
g(JX,JY)=g(X,Y).
$$

A forma fundamental associada é

$$
\omega_H(X,Y)=g(JX,Y).
$$

Ela é antissimétrica porque a compatibilidade implica

$$
g(JX,Y)=-g(X,JY).
$$

## 2. Caso Kähler

A estrutura Hermitiana é Kähler quando

$$
d\omega_H=0.
$$

Nesse caso, a conexão de Levi--Civita preserva $J$ e não possui torção.

## 3. Conexão de Bismut

Numa variedade Hermitiana integrável existe uma única conexão que preserva
$g$ e $J$ e cuja torção é totalmente antissimétrica. Ela é a conexão de
Bismut. Esquematicamente,

$$
\nabla^B=\nabla^{\rm LC}+\frac12g^{-1}H,
$$

com o sinal dependendo da convenção, e

$$
H=d_J^c\omega_H.
$$

Se $d\omega_H=0$, então $H=0$ na convenção usual. Assim,

$$
H\neq0
\quad\Longrightarrow\quad
\text{o setor não é Kähler estrito}.
$$

## 4. Setor pluriclosed

Uma condição adicional frequentemente considerada é

$$
dH=0,
$$

equivalente, sob convenções usuais, a uma condição pluriclosed ou strong KT.
Ela não decorre apenas da definição Hermitiana e precisa ser imposta pelo
setor ou demonstrada pela dinâmica.

## 5. Estatuto na GDQ

Na ação oficial atual, os campos variados são $g$, $f$ e $\bar f$; $J$ é
estrutura da teoria e $H$ é derivado da estrutura Hermitiana conforme a
convenção adotada. Se uma redução tratar $H$ como variável auxiliar, isso deve
ser identificado como formulação efetiva, não como alteração silenciosa da
ação fundamental.

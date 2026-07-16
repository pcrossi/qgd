---
title: "Decomposição de Madelung passo a passo"
tipo: derivacao
status: identidade-exata
---

# Decomposição de Madelung passo a passo

## 1. Hipóteses e domínio

Considere a equação de Schrödinger não relativística

$$
i\hbar\partial_t\psi
=
-\frac{\hbar^2}{2m}\Delta\psi+V\psi,
$$

com $m>0$, potencial real $V$ e solução suficientemente regular numa região
em que $\psi\neq0$. Escrevemos

$$
\psi=R e^{iS/\hbar},
\qquad
R>0,
\qquad
\rho=R^2.
$$

A decomposição é local. Em torno de zeros de $\psi$, a fase pode ser
multivalorada e deve ser descrita por cartas, circulação ou holonomia.

## 2. Derivada temporal

Pela regra do produto,

$$
\partial_t\psi
=e^{iS/\hbar}
\left(
\partial_tR+\frac{i}{\hbar}R\partial_tS
\right).
$$

Multiplicando por $i\hbar$,

$$
i\hbar\partial_t\psi
=e^{iS/\hbar}
\left(
i\hbar\partial_tR-R\partial_tS
\right).
$$

## 3. Gradiente e laplaciano

O gradiente é

$$
\nabla\psi
=e^{iS/\hbar}
\left(
\nabla R+\frac{i}{\hbar}R\nabla S
\right).
$$

Aplicando novamente a divergência,

$$
\Delta\psi
=e^{iS/\hbar}
\left[
\Delta R
+\frac{2i}{\hbar}\nabla R\cdot\nabla S
+\frac{i}{\hbar}R\Delta S
-\frac{1}{\hbar^2}R|\nabla S|^2
\right].
$$

## 4. Substituição na equação

Cancelando o fator não nulo $e^{iS/\hbar}$, obtemos

$$
i\hbar\partial_tR-R\partial_tS
=
-\frac{\hbar^2}{2m}\Delta R
-\frac{i\hbar}{m}\nabla R\cdot\nabla S
-\frac{i\hbar}{2m}R\Delta S
+\frac{R}{2m}|\nabla S|^2
+VR.
$$

Como $R$, $S$ e $V$ são reais, as partes real e imaginária devem coincidir
separadamente.

## 5. Parte imaginária: continuidade

A parte imaginária fornece

$$
\hbar\partial_tR
=
-\frac{\hbar}{m}\nabla R\cdot\nabla S
-\frac{\hbar}{2m}R\Delta S.
$$

Multiplicando por $2R/\hbar$,

$$
2R\partial_tR
=
-\frac{2R}{m}\nabla R\cdot\nabla S
-\frac{R^2}{m}\Delta S.
$$

Usando

$$
\partial_t\rho=2R\partial_tR
$$

e

$$
\nabla\cdot(\rho\nabla S)
=2R\nabla R\cdot\nabla S+R^2\Delta S,
$$

segue

$$
\partial_t\rho
+\nabla\cdot\left(\rho\frac{\nabla S}{m}\right)=0.
$$

Definindo

$$
v=\frac{\nabla S}{m},
$$

obtemos a equação de continuidade

$$
\boxed{
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
$$

## 6. Parte real: Hamilton--Jacobi quântica

A parte real fornece

$$
-R\partial_tS
=
-\frac{\hbar^2}{2m}\Delta R
+\frac{R}{2m}|\nabla S|^2
+VR.
$$

Dividindo por $R>0$ e levando todos os termos para o mesmo lado,

$$
\partial_tS
+\frac{|\nabla S|^2}{2m}
+V
-\frac{\hbar^2}{2m}\frac{\Delta R}{R}
=0.
$$

Como $R=\sqrt\rho$, definimos

$$
Q[\rho]
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho},
$$

e portanto

$$
\boxed{
\partial_tS+\frac{|\nabla S|^2}{2m}+V+Q[\rho]=0.
}
$$

## 7. O papel do conjugado

A equação para $\bar\psi$ é o conjugado da equação para $\psi$. Subtrair as
duas equações elimina os termos reais e produz a conservação da corrente;
somá-las, depois da decomposição polar, produz a equação dinâmica da fase.
Assim, o conjugado não é uma decoração algébrica: ele permite construir a
forma bilinear positiva $\rho=\bar\psi\psi$ e a corrente conservada.

Na formulação Hamilton--Jacobi isolada, $S$ não contém por si só a informação
de normalização. Por isso a representação hidrodinâmica possui duas equações:
uma para a fase e outra para a densidade.

## 8. Limitações

Esta nota demonstra uma equivalência local entre a equação de Schrödinger e o
par continuidade--Hamilton--Jacobi quântica. Ela não demonstra que $\rho$ é
ontologicamente um fluido clássico, nem deriva a equação de Schrödinger da
ação oficial da GDQ.

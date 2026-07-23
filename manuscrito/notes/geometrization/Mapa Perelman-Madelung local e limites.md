---
title: "Mapa Perelman--Madelung local e limites"
tipo: teorema-condicional
status: demonstrado-localmente
---

# Mapa Perelman--Madelung local e limites

Esta nota registra a correspondência precisa entre o campo complexo usado na
GDQ e as variáveis de Madelung. Ela não transforma o funcional de Perelman em
ação física. O termo “Perelman” aqui identifica a gramática geométrica
ponderada da medida; a ação física continua sendo $\mathcal S_{\rm GDQ}$.

## 1. Domínio regular

Seja $\Omega\subset M$ um aberto no qual:

$$
\rho(x)>0,
\qquad
f\in C^2(\Omega),
\qquad
g\in C^2(\Omega),
$$

e onde a fase $S_R$ possa ser escolhida como função local monovalorada.
Chamaremos esse aberto de domínio regular de Madelung:

$$
\mathcal D_{\rm reg}
=
\left\{
(g,f):
\rho=e^{-(f+\bar f)/2}>0,
\quad
S_R=\frac{\hbar}{2i}(f-\bar f)
\text{ localmente definido}
\right\}.
$$

## 2. Mapa direto

No domínio regular, o campo complexo determina densidade e fase por

$$
\rho=e^{-(f+\bar f)/2},
$$

e

$$
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

Também podemos escrever a amplitude e a função projetiva:

$$
R=\sqrt\rho,
\qquad
\Psi=R\,e^{iS_R/\hbar}.
$$

Logo, o mapa direto é

$$
(g,f)
\longmapsto
(g,\rho,S_R,\Psi).
$$

Se a medida da ação também for considerada, então

$$
\mathcal U
=\frac{\rho}{(4\pi z_\tau)^n}.
$$

## 3. Mapa inverso local

Dado um par regular $(\rho,S_R)$, com $\rho>0$, define-se

$$
f=-\ln\rho+i\frac{S_R}{\hbar}.
$$

Então

$$
\bar f=-\ln\rho-i\frac{S_R}{\hbar}.
$$

Somando,

$$
f+\bar f=-2\ln\rho,
$$

portanto

$$
e^{-(f+\bar f)/2}
=e^{\ln\rho}
=\rho.
$$

Subtraindo,

$$
f-\bar f=2i\frac{S_R}{\hbar},
$$

e, portanto,

$$
\frac{\hbar}{2i}(f-\bar f)=S_R.
$$

Assim, fixado o ramo local da fase, o mapa é invertível localmente.

## 4. Preservação das equações no setor reduzido

No setor em que a ponte física reduziu a ação para a forma canônica de
Madelung,

$$
I_{\rm Mad}
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
\right)
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx,
$$

a variação em $S_R$ fornece

$$
\partial_t\rho+\nabla\cdot(\rho v)=0,
\qquad
v=\frac{\nabla S_R}{m},
$$

e a variação em $\rho$ fornece

$$
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

Essas duas equações são a representação de Madelung. A preservação das
equações vale nesse setor reduzido; ela não afirma que toda solução off shell
da ação oficial já esteja nessa polarização canônica.

## 5. Injetividade e sobrejetividade

Localmente, com $g$ fixado, ramo de fase escolhido e $\rho$ normalizada, o
mapa $f\mapsto(\rho,S_R)$ é injetivo. De fato,

$$
\operatorname{Re}f=-\ln\rho,
\qquad
\operatorname{Im}f=\frac{S_R}{\hbar}.
$$

Globalmente, há ambiguidade de fase:

$$
S_R\sim S_R+2\pi\hbar k,
\qquad
k\in\mathbb Z.
$$

Portanto, se a fase for tomada módulo $2\pi\hbar$, é preciso escolher ramo,
atlas ou classe topológica para recuperar $f$ globalmente.

O mapa também não é sobrejetivo sobre todos os estados quânticos abstratos.
Estados com nós, fases multivaloradas, setores spinoriais, setores de gauge ou
fibrados não triviais exigem dados adicionais.

## 6. Nós

Em um nó,

$$
\rho=0.
$$

Então $\ln\rho$ diverge e

$$
f=-\ln\rho+i\frac{S_R}{\hbar}
$$

não é regular. Além disso, o termo

$$
\frac{\Delta\sqrt\rho}{\sqrt\rho}
$$

pode divergir. O tratamento correto é remover o conjunto nodal:

$$
\Omega^\ast=\Omega\setminus\{\rho=0\},
$$

trabalhar por cartas em cada componente conexa e impor compatibilidade
topológica ao redor dos nós. Na GDQ, esses conjuntos podem ser lidos como
defeitos, bordos efetivos ou estômatos, dependendo do problema.

## 7. Fase multivalorada

Se

$$
\oint_\Gamma\nabla S_R\cdot dx
=2\pi\hbar N,
\qquad
N\in\mathbb Z,
$$

então $S_R$ não é uma função global monovalorada, mas
$e^{iS_R/\hbar}$ continua monovalorada. Em cartas locais $U_a$,

$$
S_R^{(a)}-S_R^{(b)}
=2\pi\hbar k_{ab},
$$

e, portanto,

$$
f^{(a)}-f^{(b)}
=i\,2\pi k_{ab}.
$$

Assim, a fase multivalorada não invalida o mapa local; ela exige atlas e dados
topológicos.

## 8. Superposição

A transformação de Madelung é não linear. Se

$$
\Psi=\Psi_1+\Psi_2,
$$

não segue que

$$
\rho=\rho_1+\rho_2,
\qquad
S_R=S_{R,1}+S_{R,2}.
$$

Na verdade,

$$
\rho
=|\Psi_1+\Psi_2|^2
=\rho_1+\rho_2
+2\sqrt{\rho_1\rho_2}
\cos\left(\frac{S_1-S_2}{\hbar}\right),
$$

e

$$
S_R=\hbar\,\arg(\Psi_1+\Psi_2).
$$

Portanto a superposição deve ser feita em $\Psi$ e só depois traduzida para
$(\rho,S_R)$. Interferência destrutiva pode criar nós, nos quais o atlas
regular precisa ser trocado.

## 9. Estatuto final

O mapa Perelman--Madelung da GDQ é:

- local;
- regular;
- setorial;
- invertível apenas após escolha de ramo e dados geométricos;
- preservador das equações apenas no setor Madelung reduzido.

Ele não é uma bijeção global de toda a teoria.

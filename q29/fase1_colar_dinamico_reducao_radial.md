# Q29 — Fase 1 do colar dinâmico: redução radial da ação oficial

## 1. Escopo e status

Este documento inicia a Fase 1 do problema do colar não-produto. O objetivo é
derivar o funcional unidimensional antes de qualquer ajuste numérico. A
redução abaixo é uma truncagem real de cohomogeneidade um da extensão
Perelman--Bismut já usada na Q29; ela não introduz uma ação de
Einstein--Hilbert, Yang--Mills ou Higgs independente.

A integral externa em $\tau$ e os fatores positivos constantes são mantidos
implícitos nesta primeira derivação. Eles não alteram as equações radiais, mas
deverão ser restaurados antes de uma normalização absoluta de $\alpha$.

## 2. Ansatz não redundante

Adotamos formas invariantes à esquerda em $S^3$ normalizadas de modo que

$$
ds^2_{S^3(R)}=R^2(\sigma_1^2+\sigma_2^2+\sigma_3^2)
$$

tenha curvatura escalar $6/R^2$. O colar deve inicialmente conservar o lapse
radial:

$$
ds^2_4
=N(r)^2dr^2+a(r)^2(\sigma_1^2+\sigma_2^2)+c(r)^2\sigma_3^2,
$$

e o squashing físico é

$$
q(r)=\frac{c(r)}{a(r)}.
$$

Não se introduzem simultaneamente $b(r)$ e $q(r)$ na componente vertical,
pois apenas seu produto apareceria na métrica.

Tomamos o dilatão real no setor estacionário,

$$
f=f(r),
$$

e a torção invariante

$$
B=h(r)\,\sigma_1\wedge\sigma_2\wedge\sigma_3.
$$

## 3. Geometria do colar

A densidade de volume, omitindo o volume constante das órbitas, é

$$
\sqrt g=Na^2c.
$$

Na gauge própria $N=1$, a curvatura escalar é

$$
\mathcal R
=
-4\frac{a''}{a}
-2\frac{c''}{c}
-2\left(\frac{a'}a\right)^2
-4\frac{a'c'}{ac}
+\frac8{a^2}
-2\frac{c^2}{a^4}.
$$

O teste isotrópico fornece

$$
a=c=R,\qquad a'=c'=0
\quad\Longrightarrow\quad
\mathcal R=\frac6{R^2},
$$

fixando a convenção das formas $\sigma_i$.

O lapse deve ser variado antes da escolha $N=1$, pois sua equação é a
restrição radial. Fixá-lo antecipadamente eliminaria essa equação e criaria
direções espúrias na Hessiana.

Para a 3-forma acima,

$$
|B|^2=\frac{6h(r)^2}{a^4c^2}.
$$

## 4. A torção não é um quarto perfil livre neste ansatz

No interior do colar, sem fonte magnética distribuída,

$$
dB=0.
$$

Como

$$
dB=h'(r)\,dr\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3,
$$

segue

$$
\boxed{h'(r)=0.}
$$

Além disso, a convenção topológica já fixada na Q29 é

$$
\frac1{2\pi}\int_{S^3}B=n_B\in\mathbb Z.
$$

Portanto, $h=h_{n_B}$ é determinado pela carga e pela normalização das formas
invariantes. A densidade física varia radialmente porque

$$
|B|^2\propto\frac1{a^4c^2},
$$

mesmo quando o coeficiente de fluxo $h$ é constante.

Um perfil $h(r)$ não constante exigiria uma fonte, uma corrente de torção ou
uma transgressão de interface explicitamente derivada. Ele não pode ser
adicionado como grau de liberdade silencioso.

## 5. Funcional radial antes da integração por partes

Para a extensão Perelman--Bismut usada na Q29, o integrando estacionário é

$$
\tau\left(
\mathcal R+f'^2-\frac1{12}|B|^2
\right)+f-n.
$$

Definindo

$$
w(r)=e^{-f(r)}a(r)^2c(r),
$$

o funcional radial não normalizado é

$$
I[a,c,f;h]
=
\int_{r_c}^{r_\infty}dr\,w
\left[
\tau\left(
\mathcal R+f'^2-\frac{h^2}{2a^4c^2}
\right)+f-n
\right].
$$

A medida física de Perelman deve ser normalizada. Equivalentemente, pode-se
variar $I$ sob o vínculo

$$
\int_{r_c}^{r_\infty}e^{-f}a^2c\,dr=\mathcal N
$$

com multiplicador de Lagrange $\lambda$. O valor de $\mathcal N$ inclui os
volumes constantes omitidos nesta redução.

## 6. Funcional de primeira ordem com lapse

Integrando os termos de segunda derivada por partes e incluindo a completação
variacional correspondente, obtém-se

$$
I_{\mathrm{bulk}}=\int dr\,e^{-f}\mathcal L_N,
$$

$$
\mathcal L_N
=\frac{\tau}{N}T_r+N\tau V_r+Na^2c(f-n-\lambda),
$$

onde

$$
T_r
=2ca'^2+4aa'c'-4acf'a'-2a^2f'c'+a^2cf'^2
$$

e

$$
V_r=8c-2\frac{c^3}{a^2}-\frac{h^2}{2a^2c}.
$$

O termo GHY ponderado cancela precisamente o termo gerado pela integração por
partes,

$$
-4\tau e^{-f}aca'-2\tau e^{-f}a^2c',
$$

e não constitui, isoladamente, uma mola de Berger.

## 7. Restrição radial e equações explícitas

A variação do lapse fornece a restrição

$$
\boxed{-\tau T_r+\tau V_r+a^2c(f-n-\lambda)=0.}
$$

Somente depois dessa variação escolhemos $N=1$. Dividindo as demais equações
por um fator comum $2e^{-f}$, resulta

$$
\begin{aligned}
E_a={}&2\tau ac(a''-f'')+2\tau a(c''-c'f')
-2\tau ca'f'+2\tau a'c'\\
&+\tau acf'^2-2\tau\frac{c^3}{a^3}
-\frac{\tau h^2}{2a^3c}+ac(\lambda+n-f)=0,
\end{aligned}
$$

$$
\begin{aligned}
E_c={}&2\tau aa''+\tau a'^2-2\tau aa'f'-\tau a^2f''
+\frac{\tau a^2}{2}f'^2\\
&-4\tau+3\tau\frac{c^2}{a^2}
-\frac{\tau h^2}{4a^2c^2}
+\frac{a^2}{2}(\lambda+n-f)=0,
\end{aligned}
$$

e

$$
\begin{aligned}
E_f={}&\tau a^2cf''+\tau a^2c'f'+2\tau aca'f'
-\frac{\tau a^2c}{2}f'^2\\
&-\tau a^2c''-2\tau aca''-2\tau aa'c'-\tau ca'^2
+4\tau c-\tau\frac{c^3}{a^2}-\frac{\tau h^2}{4a^2c}\\
&+\frac{a^2c}{2}(f-1-n-\lambda)=0.
\end{aligned}
$$

Completam o sistema

$$
\int e^{-f}a^2c\,dr=\mathcal N,
\qquad h'=0,
\qquad \frac1{2\pi}\int_{S^3}B=n_B.
$$

As quatro equações $(E_a,E_c,E_f,E_N)$ obedecem à identidade de
reparametrização radial; a derivada da restrição é combinação das equações
dinâmicas.

## 8. Forma de bordo e condições naturais

A primeira variação contém

$$
\delta I\big|_{\partial}
=\left[\Pi_a\delta a+\Pi_c\delta c+\Pi_f\delta f\right]_{r_c}^{r_\infty},
$$

com

$$
\Pi_a=\frac{4\tau e^{-f}}N(ca'+ac'-acf'),
$$

$$
\Pi_c=\frac{2\tau e^{-f}a}{N}(2a'-af'),
$$

$$
\Pi_f=\frac{2\tau e^{-f}a}{N}(acf'-ac'-2ca').
$$

Em uma extremidade livre sem ação de interface, as condições naturais seriam

$$
\Pi_a=\Pi_c=\Pi_f=0.
$$

No estômato há uma ação de colagem $I_{\mathrm{int}}$. Incorporando a
orientação do normal no sinal, as condições Robin corretas são

$$
\boxed{
\Pi_A+\frac{\partial I_{\mathrm{int}}}{\partial X^A}=0,
\qquad X^A=(a,c,f).
}
$$

Se o valor de um campo for fixado, sua variação se anula em vez de se impor a
condição natural. Os coeficientes de $I_{\mathrm{int}}$ devem vir do pullback
da interface Q29/Q42, nunca de um ajuste de estabilidade ou de $\alpha$.

## 9. Dados de contorno admissíveis

No estômato $r=r_c$ são necessários:

1. $a(r_c)>0$ e $c(r_c)>0$;
2. carga de Bismut/Cauchy $n_B=1$;
3. condições Robin da ação conjunta bulk--interface;
4. normalização de $f$ por $\mathcal N$.

Na extremidade exterior devem ser usados os dados do background GDQ:

$$
(a,c,f)\longrightarrow(a_\infty,c_\infty,f_\infty).
$$

A condição $c_\infty/a_\infty=1$ só é lícita se o background global for
isotrópico. Em domínio infinito também devem convergir a medida e as normas
dos modos físicos.

## 10. Operador de Jacobi e domínio auto-adjunto

Para $X^A=X_*^A+\eta^A$, a matriz principal da segunda variação é

$$
P_{AB}
=\frac{\tau e^{-f}}N
\begin{pmatrix}
4c&4a&-4ac\\
4a&0&-2a^2\\
-4ac&-2a^2&2a^2c
\end{pmatrix}.
$$

Seu determinante é

$$
\det P=16\frac{\tau^3e^{-3f}}{N^3}a^4c.
$$

Ele é não nulo para $a,c,\tau,N>0$, mas indefinido. A estabilidade só pode ser
avaliada depois da restrição linearizada do lapse e da remoção do modo de
reparametrização.

Definindo

$$
C_{AB}=\left.
\frac{\partial^2(e^{-f}\mathcal L_N)}
{\partial X'^A\partial X^B}\right|_{X_*},
\qquad
V_{AB}=\left.
\frac{\partial^2(e^{-f}\mathcal L_N)}
{\partial X^A\partial X^B}\right|_{X_*},
$$

o operador de Jacobi é

$$
\boxed{
\mathcal J\eta
=-\frac{d}{dr}(P\eta'+C\eta)+C^T\eta'+V\eta.
}
$$

O concomitante de Green é

$$
\mathfrak B(\eta,\zeta)
=\left[
\eta^T(P\zeta'+C\zeta)-(P\eta'+C\eta)^T\zeta
\right]_{r_c}^{r_\infty}.
$$

O domínio é auto-adjunto quando $\mathfrak B=0$. Isso vale para Dirichlet e
para condições Robin provenientes de uma Hessiana de interface real e
simétrica. A restrição $\delta E_N=0$ deve ser imposta antes da diagonalização.

## 11. Veredito da Fase 1

Os passos 1--3 estão concluídos no nível analítico:

1. ação radial sem redundância e com lapse;
2. torção corretamente tratada como fluxo fechado de carga discreta;
3. EDOs, restrição, forma de bordo e operador auto-adjunto derivados.

A Fase 2 pode começar quando forem inseridos dois dados físicos já externos à
redução local: o pullback específico da ação de interface do estômato e o
background exterior de colagem. Usar $\Pi_A=0$ ou um exterior plano por
conveniência mudaria o problema físico.

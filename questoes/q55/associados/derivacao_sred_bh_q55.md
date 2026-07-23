# Q55 — Redução radial covariante da ação oficial

## Classificação

Resultado formal/condicional.

Este documento executa a primeira fase do plano de Q55: reduzir a dinâmica
covariante de buraco negro ao setor radial esfericamente simétrico sem trocar
a ação oficial da GDQ por Einstein--Hilbert como fundamento.

## 1. Campo reduzido

No setor estático esfericamente simétrico, tome a métrica física efetiva:

$$
ds^2
=
-e^{2\Phi(r)}A(r)c^2dt^2
+A(r)^{-1}dr^2
+r^2d\Omega^2.
$$

Defina:

$$
A(r)=1-\frac{2Gm(r)}{c^2r}.
$$

Os campos reduzidos são:

$$
X(r)
=
\{\Phi(r),m(r),f_R(r),S_R(r),H(r)\}.
$$

As variáveis constitutivas continuam:

$$
\rho=e^{-f_R},
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
$$

## 2. Ação radial como redução da ação oficial

A ação oficial é:

$$
\mathcal S_{\rm GDQ}
=
\int_\gamma
\left[
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\mathcal L_0
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau},
$$

com:

$$
\mathcal L_0
=
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n.
$$

No setor radial, a integração angular e interna define uma densidade efetiva:

$$
S_{\rm red}^{\rm BH}
=
C_\Omega
\int_\gamma\frac{d\tau}{\tau}
\int_0^\infty dr\,
e^{\Phi(r)}
r^2
\mathcal U(r,\tau)
\mathcal L_{\rm red}(X,X';\tau).
$$

Aqui $C_\Omega$ inclui o volume angular e os fatores internos transportados.
Esse fator não deve ser usado para ajustar observáveis; ele deve vir da
normalização global já separada nas Q36/Q38/Q54.

## 3. Equação métrica ponderada

A variação em relação à métrica já foi consolidada na Q54:

$$
\begin{aligned}
0={}&\tau\mathcal U
\left(R_{\mu\nu}+P_{\mu\nu}^{(f)}\right)
\\
&+\tau
\left(
g_{\mu\nu}\Delta\mathcal U
-\nabla_\mu\nabla_\nu\mathcal U
\right)
\\
&-\frac12\mathcal U
\left(
\mathcal L_0-\lambda
\right)
g_{\mu\nu}.
\end{aligned}
$$

Na carta real:

$$
f=f_R+i\theta,
\qquad
\theta=\frac{S_R}{\hbar}.
$$

Como:

$$
f_R=-\ln\rho,
$$

vale a identidade:

$$
\nabla_\mu\nabla_\nu f_R
=
\nabla_\mu f_R\nabla_\nu f_R
-\frac1\rho\nabla_\mu\nabla_\nu\rho.
$$

Essa identidade é o mecanismo anti-singular: quando $\rho$ tenta formar uma
delta central, a Hessiana de $f_R$ cresce e gera tensão geométrica.

## 4. Definição variacional da fonte

Defina a fonte efetiva macroscópica da GDQ por:

$$
T_{\mu\nu}^{\rm GDQ}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\rm eff}^{\rm mat}}{\delta g^{\mu\nu}},
$$

onde $S_{\rm eff}^{\rm mat}$ é a parte da redução que sobra após isolar o
bloco métrico macroscópico. Essa definição não adiciona matéria externa; ela
nomeia a tensão média dos campos GDQ.

Na simetria esférica:

$$
T^\mu{}_\nu
=
\operatorname{diag}
(-\epsilon,p_r,p_t,p_t).
$$

Portanto:

$$
\epsilon=-T^t{}_t,
\qquad
p_r=T^r{}_r,
\qquad
p_t=T^\theta{}_\theta.
$$

## 5. Equações radiais efetivas

Da forma macroscópica da Q54:

$$
G_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}^{\rm GDQ}
-\Lambda g_{\mu\nu},
$$

obtemos as leituras radiais:

$$
m'(r)
=
\frac{4\pi r^2}{c^2}\epsilon(r).
$$

Definindo:

$$
\nu(r)
=
\log\sqrt{-g_{tt}}
=
\Phi(r)+\frac12\log A(r),
$$

a equação efetiva de TOV fornece:

$$
\nu'(r)
=
\frac{Gm(r)/c^2+4\pi Gr^3p_r(r)/c^4}
{r^2A(r)}.
$$

A equação para o lapso $\Phi$ é, portanto:

$$
\Phi'(r)
=
\frac{Gm(r)/c^2+4\pi Gr^3p_r(r)/c^4}
{r^2A(r)}
-\frac{A'(r)}{2A(r)}.
$$

A conservação de Bianchi fornece a equação anisotrópica:

$$
p_r'
=
-(\epsilon+p_r)
\left(
\Phi'
+
\frac{A'}{2A}
\right)
+\frac{2}{r}(p_t-p_r).
$$

Essas equações não são postulado novo; são a leitura radial da equação
métrica ponderada depois da correspondência macroscópica da Q54.

## 6. Condições de regularidade

Para um core regular:

$$
\epsilon(r)=\epsilon_0+\epsilon_2r^2+O(r^4),
$$

então:

$$
m(r)=\frac{4\pi\epsilon_0}{3c^2}r^3+O(r^5).
$$

Daí:

$$
A(r)=1-\frac{\Lambda_{\rm core}}{3}r^2+O(r^4),
$$

com:

$$
\Lambda_{\rm core}
=
\frac{8\pi G}{c^4}\epsilon_0.
$$

No centro, a conservação exige isotropia:

$$
p_r(0)=p_t(0).
$$

Para core de Sitter:

$$
p_r(0)=p_t(0)=-\epsilon_0.
$$

## 7. Resultado da fase 1

Concluído:

1. a redução radial admissível foi escrita;
2. a fonte foi definida por variação, não por postulado externo;
3. as equações radiais efetivas foram obtidas;
4. a condição suficiente de regularidade central foi demonstrada.

Não concluído:

1. calcular $\epsilon(r)$, $p_r(r)$, $p_t(r)$ diretamente de uma sela explícita
   da ação oficial;
2. resolver numericamente a sela completa em $(g,f,H)$.

Portanto, esta fase fecha a estrutura variacional, mas ainda não fecha a
solução global.

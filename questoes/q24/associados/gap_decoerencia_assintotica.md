# Q24 — Gap setorial e decoerência assintótica

## 1. Objetivo

Provar que a dominância espectral do operador de medição implica supressão
exponencial das coerências entre registros.

---

## 2. Operadores restritos

Para cada registro:

\[
\mathcal H_i
=
\Pi_i\mathcal H_\rho\Pi_i.
\]

Assumimos:

\[
\boxed{
0\le\lambda_{i,0}<\lambda_{i,1}\le\lambda_{i,2}\le\cdots
}
\]

e definimos o gap interno:

\[
\boxed{
\Delta_i=\lambda_{i,1}-\lambda_{i,0}>0.
}
\]

Entre registros distintos, definimos o gap de separação:

\[
\boxed{
\Delta_{ij}
=
\operatorname{dist}(\sigma_i,\sigma_j)>0.
}
\]

O gap de medição é:

\[
\boxed{
\Delta_{\rm meas}
=
\min\left\{\min_i\Delta_i,\min_{i\ne j}\Delta_{ij}\right\}>0.
}
\]

---

## 3. Dominância dentro de cada setor

Para dado setor:

\[
\rho_i(\tau)
=
e^{-\tau\mathcal H_i}\rho_i(0)
=
\sum_n c_{i,n}e^{-\lambda_{i,n}\tau}\psi_{i,n}.
\]

Separando o modo dominante:

\[
\rho_i(\tau)
=
e^{-\lambda_{i,0}\tau}
\left[
c_{i,0}\psi_{i,0}
+
\sum_{n\ge1}
c_{i,n}
e^{-(\lambda_{i,n}-\lambda_{i,0})\tau}
\psi_{i,n}
\right].
\]

Logo:

\[
\boxed{
\left\|
\rho_i(\tau)
-
c_{i,0}e^{-\lambda_{i,0}\tau}\psi_{i,0}
\right\|
\le
C_i e^{-(\lambda_{i,0}+\Delta_i)\tau}.
}
\]

Isso formaliza a dominância assintótica já presente no Capítulo 16.

---

## 4. Supressão fora da diagonal

O estado correlacionado após interação ideal é:

\[
|\Psi_{SAE}\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
\]

Os termos fora da diagonal no traço reduzido têm fator:

\[
\Gamma_{ij}(\tau)
=
\langle A_j(\tau),E_j(\tau)|A_i(\tau),E_i(\tau)\rangle.
\]

Como \(A_iE_i\) e \(A_jE_j\) pertencem a setores espectrais separados:

\[
\Gamma_{ij}(\tau)
=
\langle
e^{-\tau\mathcal H_j}R_j(0),
e^{-\tau\mathcal H_i}R_i(0)
\rangle_{\mathcal U}.
\]

Pela quase-ortogonalidade dos projetores e pela separação espectral:

\[
\boxed{
|\Gamma_{ij}(\tau)|
\le
C_{ij}
e^{-\Delta_{ij}\tau}
+
O(e^{-S_{\rm sep}/\hbar}).
}
\]

No limite macroscópico:

\[
\boxed{
|\Gamma_{ij}(\tau)|
\to0,
\qquad
i\ne j.
}
\]

---

## 5. Mistura reduzida

O estado reduzido fica:

\[
\rho_{SA}(\tau)
=
\sum_{ij}
c_ic_j^*
\Gamma_{ij}(\tau)
|s_i,A_i\rangle\langle s_j,A_j|.
\]

Como \(\Gamma_{ij}\to0\) para \(i\ne j\):

\[
\boxed{
\rho_{SA}(\tau)
\xrightarrow{\tau\to\infty}
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

As probabilidades não foram inseridas no funcional geométrico; elas vêm da
Q22:

\[
\boxed{
P(i)=\operatorname{Tr}(\rho_SP_i)=|c_i|^2
}
\]

no caso puro discreto.

---

## 6. Taxa física

A escala de decoerência no parâmetro de fluxo é:

\[
\boxed{
\tau_{\rm dec}^{-1}
\ge
\Delta_{\rm meas}.
}
\]

Para converter em tempo físico \(t\), usa-se o pullback causal:

\[
\boxed{
\gamma^*\left(\frac{d\tau}{\tau}\right)
=
\kappa\,dt.
}
\]

Assim, localmente:

\[
\boxed{
|\Gamma_{ij}(t)|
\lesssim
C_{ij}
e^{-\Delta_{ij}\tau_0e^{\kappa t}}
}
\]

ou, em janela curta de laboratório:

\[
\boxed{
|\Gamma_{ij}(t)|
\lesssim
C_{ij}e^{-\Gamma_{ij}^{\rm lab}t},
\qquad
\Gamma_{ij}^{\rm lab}\simeq\kappa\tau_*\Delta_{ij}.
}
\]

---

## 7. Resultado da etapa 3 e 4

Fica demonstrado, sob as hipóteses de auto-adjuncidade, gap setorial e
quase-ortogonalidade macroscópica, que:

\[
\boxed{
\text{dominância espectral}
\Longrightarrow
\text{supressão exponencial de coerências}
\Longrightarrow
\text{registro reduzido estável}.
}
\]

Status:

\[
\boxed{
\text{Etapas 3 e 4 fechadas como teorema condicional.}
}
\]

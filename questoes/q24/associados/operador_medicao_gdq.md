# Q24 — Operador de medição GDQ

## 1. Objetivo

Construir o operador de medição que liga o acoplamento sistema--aparelho à
dinâmica assintótica da densidade.

O objeto procurado não é um Hamiltoniano de medição importado da mecânica
quântica padrão. Ele é a Hessiana física da ação oficial da GDQ no background
com aparelho e ambiente:

\[
\boxed{
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_*}
\mathcal S_{\rm GDQ}^{S+A+E}
P^{\rm phys}.
}
\]

Aqui:

- \(\Phi_*=(g_*,f_*,\bar f_*)\) é o background estacionário durante a janela de
  medição;
- \(P^{\rm phys}\) remove difeomorfismos, modos de gauge e variações que
  violam vínculos de normalização/carga;
- \(S+A+E\) indica que a ação oficial é avaliada com fontes e contornos do
  aparelho, não com nova ação fundamental.

---

## 2. Dados de aparelho

O aparelho entra por dados externos clássicos:

\[
\boxed{
J_{\rm app},\qquad
\mathsf R_{\rm app},\qquad
\Omega_{\rm app},\qquad
\partial\Omega_{\rm app}.
}
\]

Eles definem o domínio:

\[
\boxed{
\mathcal D(\mathcal H_{\rm meas})
=
\left\{
\delta\Phi\in H^2_{\rm loc}(\Omega):
(\nabla_n+\mathsf R_{\rm app})\delta\Phi|_{\partial\Omega}
=J_{\rm app}^{(1)}
\right\}
\cap
\operatorname{Im}P^{\rm phys}.
}
\]

Quando \(J_{\rm app}=0\) no setor linearizado homogêneo, a condição reduz-se a
Robin/DtN:

\[
\boxed{
(\nabla_n+\mathsf R_{\rm app})\delta\Phi=0.
}
\]

Essa condição é dado de contorno do experimento. Não altera a ação oficial.

---

## 3. Redução para a equação de densidade

Pela definição constitutiva:

\[
\rho=e^{-(f+\bar f)/2},
\]

uma variação real de densidade é:

\[
\delta\rho
=
-\frac12\rho(\delta f+\delta\bar f).
\]

No setor dissipativo da medida, a parte real da Hessiana projetada induz o
gerador efetivo:

\[
\boxed{
\partial_\tau\delta\rho
=
-\mathcal H_\rho\,\delta\rho,
}
\]

com:

\[
\boxed{
\mathcal H_\rho
=
\Pi_\rho
\mathcal H_{\rm meas}
\Pi_\rho^*.
}
\]

No limite em que apenas a densidade de Perelman é observada, recupera-se o
operador legado do Capítulo 16:

\[
\boxed{
\mathcal H_\rho
\simeq
-\Delta_K+R_{\rm eff}(\boldsymbol r),
}
\]

equivalentemente:

\[
\boxed{
\partial_\tau\rho
=
\Delta_K\rho
-R_{\rm eff}\rho.
}
\]

O sinal é escolhido para que autovalores positivos gerem decaimento:

\[
\rho(\tau)=e^{-\tau\mathcal H_\rho}\rho(0).
\]

---

## 4. Auto-adjuncidade e positividade

O produto interno físico é ponderado pela medida da GDQ:

\[
\boxed{
\langle u,v\rangle_{\mathcal U}
=
\int_{\Omega}
\bar u\,v\,\mathcal U_*\sqrt{\det g_*}\,d^{2n}z.
}
\]

Com \(\mathsf R_{\rm app}\) Hermitiana no bordo e \(P^{\rm phys}\) ortogonal
nesse produto, a integração por partes fornece:

\[
\boxed{
\langle u,\mathcal H_\rho v\rangle_{\mathcal U}
=
\langle \mathcal H_\rho u,v\rangle_{\mathcal U}.
}
\]

O termo de bordo é:

\[
\int_{\partial\Omega}
\bar u
\left(
\nabla_n v+\mathsf R_{\rm app}v
\right)
d\Sigma_{\mathcal U},
\]

e se anula no domínio Robin/DtN.

A forma quadrática é:

\[
\boxed{
Q_\rho[u]
=
\langle u,\mathcal H_\rho u\rangle_{\mathcal U}
\ge0
}
\]

quando o aparelho é estável, isto é, quando sua impedância não injeta modo
negativo no setor de registro.

---

## 5. Resultado da etapa 1

O operador de medição fica definido como:

\[
\boxed{
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_*}
\mathcal S_{\rm GDQ}^{S+A+E}
P^{\rm phys},
\qquad
\mathcal H_\rho
=
\Pi_\rho\mathcal H_{\rm meas}\Pi_\rho^*.
}
\]

Ele é o objeto que substitui o Hamiltoniano de medição importado. A base de
medição e os registros são determinados pelo domínio e pelo contorno do
aparelho.

Status:

\[
\boxed{
\text{Etapa 1 fechada como construção condicional do operador.}
}
\]

A condição é ter um background \(\Phi_*\) admissível e uma impedância
\(\mathsf R_{\rm app}\) especificada para o experimento.

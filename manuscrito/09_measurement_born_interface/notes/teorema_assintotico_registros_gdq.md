---
title: "Teorema assintótico de registros GDQ"
---

# Teorema assintótico de registros GDQ

Esta nota consolida a parte técnica da medição na GDQ. Ela não introduz uma
ação nova. O aparelho entra como fonte, contorno e impedância de interface
aplicados à ação oficial.

## 1. Dados do problema de medição

Uma medição envolve:

$$
S+A+E,
$$

onde $S$ é o sistema, $A$ é o aparelho e $E$ é o ambiente. O aparelho define
dados clássicos externos:

$$
J_{\rm app},
\qquad
\mathsf R_{\rm app},
\qquad
\Omega_{\rm app},
\qquad
\partial\Omega_{\rm app}.
$$

Esses dados selecionam domínio e contorno. Eles não modificam a ação oficial.

Durante a janela de medição, suponha um background admissível:

$$
\Phi_\ast=(g_\ast,f_\ast,\bar f_\ast),
\qquad
\mathcal U_\ast
=
\frac{\rho_\ast}{(4\pi z_\tau)^n}.
$$

## 2. Operador de medição GDQ

O operador efetivo de medição é a Hessiana física projetada:

$$
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_\ast}
\mathcal S_{\rm GDQ}^{S+A+E}
P^{\rm phys}.
$$

Aqui $P^{\rm phys}$ remove difeomorfismos, redundâncias de calibre e variações
que violam vínculos físicos. A notação $S+A+E$ significa que a mesma ação
oficial é avaliada com fontes e contornos de sistema, aparelho e ambiente.

O domínio típico é:

$$
\mathcal D(\mathcal H_{\rm meas})
=
\left\{
\delta\Phi\in H^2_{\rm loc}(\Omega):
(\nabla_n+\mathsf R_{\rm app})\delta\Phi|_{\partial\Omega}
=
J_{\rm app}^{(1)}
\right\}
\cap
\operatorname{Im}P^{\rm phys}.
$$

No setor homogêneo linearizado, $J_{\rm app}^{(1)}=0$ e a condição reduz a:

$$
(\nabla_n+\mathsf R_{\rm app})\delta\Phi=0.
$$

## 3. Redução de densidade

Como

$$
\rho=e^{-(f+\bar f)/2},
$$

uma variação real de densidade é:

$$
\delta\rho
=
-
\frac12\rho(\delta f+\delta\bar f).
$$

No setor dissipativo reduzido da medição, a Hessiana projetada induz:

$$
\partial_\tau\delta\rho
=
-
\mathcal H_\rho\delta\rho,
$$

com:

$$
\mathcal H_\rho
=
\Pi_\rho\mathcal H_{\rm meas}\Pi_\rho^\ast.
$$

No limite em que apenas a densidade efetiva é observada:

$$
\mathcal H_\rho
\simeq
-
\Delta_K+R_{\rm eff}.
$$

O sinal é escolhido de modo que autovalores positivos gerem decaimento:

$$
\rho(\tau)=e^{-\tau\mathcal H_\rho}\rho(0).
$$

## 4. Produto interno, bordo e autoadjunticidade

O produto interno reduzido usa a medida estacionária da GDQ:

$$
\langle u,v\rangle_{\mathcal U}
=
\int_\Omega
\bar u\,v\,
\mathcal U_\ast\sqrt{\det g_\ast}\,d^{2n}z.
$$

Com $\mathsf R_{\rm app}$ Hermitiana no bordo e $P^{\rm phys}$ ortogonal nesse
produto, a integração por partes dá:

$$
\langle u,\mathcal H_\rho v\rangle_{\mathcal U}
=
\langle\mathcal H_\rho u,v\rangle_{\mathcal U}.
$$

O termo de bordo é proporcional a:

$$
\int_{\partial\Omega}
\bar u
\left(
\nabla_n v+\mathsf R_{\rm app}v
\right)
d\Sigma_{\mathcal U}.
$$

Ele se anula para funções no domínio Robin/DtN. Um aparelho estável exige a
forma quadrática:

$$
Q_\rho[u]
=
\langle u,\mathcal H_\rho u\rangle_{\mathcal U}
\ge0
$$

no setor físico de registro.

## 5. Registros como setores espectrais

Um registro macroscópico $R_i$ é representado por um setor:

$$
R_i
\leftrightarrow
\Omega_i
\leftrightarrow
\Pi_i.
$$

Os projetores setoriais satisfazem:

$$
\Pi_i\Pi_j=\delta_{ij}\Pi_i,
\qquad
\sum_i\Pi_i=I_{\rm reg}.
$$

Quando o setor é definido por cluster espectral separado:

$$
\Pi_i
=
\frac1{2\pi i}
\oint_{\Gamma_i}
(z-\mathcal H_\rho)^{-1}\,dz.
$$

## 6. Gap de medição

Em cada setor:

$$
\mathcal H_i
=
\Pi_i\mathcal H_\rho\Pi_i.
$$

Assuma:

$$
0\le\lambda_{i,0}<\lambda_{i,1}\le\lambda_{i,2}\le\cdots.
$$

Defina:

$$
\Delta_i=\lambda_{i,1}-\lambda_{i,0}>0,
$$

e, para setores distintos:

$$
\Delta_{ij}
=
\operatorname{dist}(\sigma_i,\sigma_j)>0.
$$

O gap de medição é:

$$
\Delta_{\rm meas}
=
\min
\left\{
\min_i\Delta_i,
\min_{i\ne j}\Delta_{ij}
\right\}
>0.
$$

## 7. Supressão assintótica das coerências

Após a interação ideal:

$$
|\Psi_{SAE}\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
$$

Os termos fora da diagonal recebem:

$$
\Gamma_{ij}(\tau)
=
\langle A_j(\tau),E_j(\tau)|A_i(\tau),E_i(\tau)\rangle.
$$

Como registros distintos pertencem a setores espectrais separados:

$$
|\Gamma_{ij}(\tau)|
\le
C_{ij}e^{-\Delta_{ij}\tau}
+
O(e^{-S_{\rm sep}/\hbar}),
\qquad
i\ne j.
$$

Logo:

$$
\rho_{SA}(\tau)
\to
\sum_i
\operatorname{Tr}(\rho_SP_i)
|s_i,A_i\rangle\langle s_i,A_i|.
$$

## 8. Repetibilidade

Após observar o registro $i$, o estado condicionado é:

$$
\rho_{S|i}
=
\frac{P_i\rho_SP_i}{\operatorname{Tr}(\rho_SP_i)}.
$$

Então:

$$
\operatorname{Tr}(\rho_{S|i}P_i)=1.
$$

Isso prova a repetibilidade ideal.

## 9. Resultado único por bacias reais

Decoerência e gap provam diagonalização assintótica. Um evento individual exige
uma dinâmica real de bacias no aparelho e ambiente.

Defina:

$$
\mathcal C_{A+E}
=
\{(g,f,\bar f;\xi_{\rm app})
\text{ compatíveis com o contorno do aparelho}\}/\mathcal G.
$$

O funcional efetivo aberto é:

$$
\mathfrak F_{\rm meas}[\Phi]
=
\operatorname{Re}
\mathcal S_{\rm GDQ}^{S+A+E}[\Phi].
$$

Hipóteses suficientes:

1. $\mathcal C_{A+E}$ é regular no setor físico projetado;
2. $\mathfrak F_{\rm meas}$ é $C^2$;
3. existe dinâmica dissipativa com Lyapunov:

$$
\frac{d}{d\tau}\mathfrak F_{\rm meas}[\Phi(\tau)]\le0;
$$

4. cada registro $R_i$ é mínimo hiperbólico:

$$
\nabla\mathfrak F_{\rm meas}(R_i)=0,
\qquad
\operatorname{Hess}_{R_i}^{\rm phys}\mathfrak F_{\rm meas}>0;
$$

5. fronteiras entre bacias são variedades estáveis de selas;
6. a medida inicial é absolutamente contínua em relação à medida induzida por
   $\mathcal U_\ast$.

A bacia é:

$$
\mathcal B_i
=
\left\{
\Phi_0\in\mathcal C_{A+E}:
\lim_{\tau\to\infty}\Phi(\tau;\Phi_0)=R_i
\right\}.
$$

Pelo teorema da variedade estável, as fronteiras de bacia têm medida nula.
Portanto, para quase toda condição inicial real, existe um único $i$ tal que:

$$
\Phi_0\in\mathcal B_i,
\qquad
\Phi(\tau;\Phi_0)\to R_i.
$$

A compatibilidade com Born é:

$$
\mu_{\rm init}(\mathcal B_i)
=
\operatorname{Tr}(\rho_SP_i).
$$

## 10. Status lógico

O teorema assintótico de registros é condicional:

$$
\boxed{
\mathcal H_{\rm meas}\text{ autoadjunto}
+
\Delta_{\rm meas}>0
\Longrightarrow
\text{decoerência exponencial, registros estáveis e repetibilidade}.
}
$$

O resultado único ontológico é condicional adicionalmente à existência de
bacias Morse reais no espaço microgeométrico do aparelho e ambiente. Essa
condição não altera a ação oficial; ela especifica quando um aparelho concreto
realiza uma medição completa.


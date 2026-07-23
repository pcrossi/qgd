# Q58 — Plano do solver cosmológico integrado GDQ

## 1. Objetivo

Construir um solver único para testar a Q58 sem respostas isoladas. O mesmo
background cosmológico deve gerar:

- $H(z)$;
- distâncias de supernovas;
- BAO;
- CMB;
- abundâncias BBN;
- lentes;
- crescimento de estrutura;
- birrefringência.

Classificação:

$$
\boxed{
\text{programa metrológico; não substitui a formulação estrutural já criada.}
}
$$

---

## 2. Entrada única do problema

O solver deve receber uma única classe de dados cosmológicos:

$$
\mathcal P_{\rm cos}
=
\left(
\Phi_*^{\rm cos},
R_H,
\eta_b,
T_0,
\mathcal P_{\rm prim},
\mathcal B_{\rm contorno}
\right).
$$

Onde:

- $\Phi_*^{\rm cos}=(g,J,H,f,\mathcal U)_{\rm cos}$ é a sela cosmológica GDQ;
- $R_H$ é o contorno/horizonte do universo observável;
- $\eta_b$ é a razão bárion-fóton usada na BBN;
- $T_0$ fixa a temperatura atual da CMB;
- $\mathcal P_{\rm prim}$ codifica condições iniciais primordiais;
- $\mathcal B_{\rm contorno}$ codifica contornos globais e de observação.

Esses dados não podem ser mudados separadamente para cada fenômeno.

---

## 3. Bloco de fundo

O fundo efetivo deve ser obtido pela redução macroscópica da equação métrica
ponderada da GDQ:

$$
\operatorname{Eul}_g(\mathcal S_{\rm GDQ})=0
\quad
\Longrightarrow
\quad
\mathcal E_{\rm cos}[a,H,\rho_i,\Theta_H]=0.
$$

Em linguagem operacional, isso fornece:

$$
H(z)=\frac{\dot a}{a}.
$$

Também fornece as distâncias:

$$
D_C(z)=c\int_0^z\frac{dz'}{H(z')},
$$

$$
D_L(z)=(1+z)D_C(z),
\qquad
D_A(z)=\frac{D_C(z)}{1+z}.
$$

Supernovas e BAO devem usar esse mesmo $H(z)$.

---

## 4. Bloco perturbativo comum

As perturbações devem vir da Hessiana física cosmológica:

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm cos}^{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P_{\rm cos}^{\rm phys}.
$$

O sistema linear comum é:

$$
K_{\rm cos}^{\rm phys}\delta\Phi_{\rm cos}
=
J_{\rm bar}
+J_{\gamma}
+J_\nu
+J_H.
$$

O mesmo $\delta\Phi_{\rm cos}$ deve alimentar:

- potenciais de lente;
- crescimento de estrutura;
- transferência CMB;
- correções torsionais em aglomerados;
- birrefringência.

---

## 5. BBN e lítio

A BBN usa o mesmo fundo:

$$
T(z)=T_0(1+z),
\qquad
H(z)=H_{\rm GDQ}(z).
$$

As reações nucleares recebem correção geométrica por barreira Bohm--Cartan:

$$
\Gamma_{ij}^{\rm GDQ}(T)
=
\Gamma_{ij}^{\rm nuc}(T)
+
\Delta\Gamma_{ij}^{\rm Bohm-Cartan}(T,\Phi_*^{\rm cos}).
$$

O lítio só fica resolvido se o mesmo termo que altera $^7{\rm Be}$ e
$^7{\rm Li}$ não estragar deutério, hélio e a razão bárion-fóton.

---

## 6. Bullet Cluster e lentes

O potencial de lente deve vir da métrica efetiva:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp(\Phi+\Psi)\frac{2\,dl}{c^2}.
$$

Na GDQ, a separação tipo Bullet Cluster é atribuída ao setor torsional/elástico
residual:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_{\nu}^{\ \alpha\beta}
-\frac12g_{\mu\nu}|H|^2.
$$

O teste correto não é apenas curva de rotação; é reproduzir simultaneamente:

- pico de lente;
- posição do plasma;
- distribuição bariônica;
- crescimento de estrutura;
- CMB.

---

## 7. Birrefringência

A rotação de polarização deve ser calculada como holonomia do setor fotônico
transportado pela conexão efetiva de Bismut:

$$
\Delta\Psi_{\rm GDQ}
=
\frac12
\int_{\gamma_{\rm CMB}}
\omega_{\rm pol}^{B}.
$$

No limite reduzido legado:

$$
\Delta\Psi
\sim
\frac{\alpha}{\pi}
\left(
1-\frac{3}{4\pi^2}
\right).
$$

Mas para fechamento metrológico esse valor deve sair do mesmo
$\Phi_*^{\rm cos}$ usado para $H(z)$, CMB e lentes.

---

## 8. Critério de fechamento

A Q58 só fica metrologicamente fechada se:

1. um único $\mathcal P_{\rm cos}$ for congelado antes da comparação;
2. $H(z)$, SN, BAO e CMB usarem o mesmo fundo;
3. BBN usar o mesmo $H(z)$ e as mesmas correções geométricas;
4. lentes e crescimento vierem do mesmo $K_{\rm cos}^{\rm phys}$;
5. birrefringência vier da mesma conexão de Bismut cosmológica;
6. nenhuma anomalia receber fator próprio ajustado depois.

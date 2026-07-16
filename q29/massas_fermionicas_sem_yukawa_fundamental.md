# Q29 — Massas fermiônicas e acoplamento ao modo eletrofraco

## 1. Separação conceitual

Na GDQ, o modo eletrofraco não precisa ser a origem de toda massa fermiônica.
Os férmions são modos do operador de Dirac--Bismut:

$$
\slashed D_{B,A}\psi_n=\lambda_n\psi_n,
\qquad
\boxed{m_n^{(0)}c^2=E_0|\lambda_n|.}
$$

A Q39 calcula razões leptônicas por esse problema espectral. Portanto, a massa
não desaparece necessariamente quando $\Phi_{\rm EW}=0$.

## 2. Resposta eletrofraca

O modo de Hopf modifica o operador:

$$
\slashed D_{B,A}(\beta)
=\slashed D_{B,A}^{(0)}
+\beta\mathcal V_{\rm EW}+O(\beta^2).
$$

No subespaço fermiônico,

$$
\boxed{
Y_{ij}^{\rm geom}
=\langle\psi_{L,i},\mathcal V_{\rm EW}\psi_{R,j}\rangle_{\mathcal U_*}.
}
$$

Depois da quebra,

$$
\boxed{
M_{ij}
=M_{ij}^{(0)}
+\frac{v}{\sqrt2}Y_{ij}^{\rm geom}
+O(v^2/\Lambda_C^2).
}
$$

O Modelo Padrão é o limite particular $M^{(0)}=0$.

## 3. Regras de seleção

O modo eletrofraco possui

$$
(j_L,j_R)=\left(\frac12,\frac12\right).
$$

Como

$$
j\otimes\frac12
=\left(j+\frac12\right)\oplus\left(j-\frac12\right),
$$

um overlap não nulo exige

$$
\boxed{
\Delta j_L=\pm\frac12,
\qquad
\Delta j_R=\pm\frac12,
}
$$

além da conservação de hipercarga.

## 4. Mistura

Após diagonalizar $M_f$, os desalinhamentos fornecem

$$
V_{\rm CKM}=U_{u,L}^\dagger U_{d,L},
\qquad
U_{\rm PMNS}=U_{e,L}^\dagger U_{\nu,L}.
$$

Na GDQ, seus elementos são overlaps entre modos distribuídos nos três
estômatos, não constantes fundamentais independentes.

## 5. Resultado

O mecanismo fica estruturalmente definido como

$$
\boxed{
\text{massa primária espectral}
+\text{resposta eletrofraca por overlap}.
}
$$

Valores numéricos de CKM, PMNS e correções de massa exigem as autofunções
normalizadas completas e pertencem ao programa espectral posterior.

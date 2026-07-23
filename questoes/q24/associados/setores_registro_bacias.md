# Q24 — Setores de registro e bacias geométricas

## 1. Objetivo

Definir matematicamente os registros macroscópicos \(R_i\) como setores
estáveis do operador de medição GDQ.

O registro não é introduzido como postulado abstrato. Ele é a região de fase
macroscópica do aparelho que permanece estável após a interação.

\[
\boxed{
R_i
\leftrightarrow
\Omega_i
\leftrightarrow
\Pi_i.
}
\]

---

## 2. Decomposição do domínio de aparelho

Durante a medição, o aparelho possui domínios ou bacias macroscópicas
distinguíveis:

\[
\boxed{
\Omega_{\rm app}
=
\bigcup_i\Omega_i,
\qquad
\Omega_i\cap\Omega_j\simeq\varnothing
\quad(i\ne j).
}
\]

Cada \(\Omega_i\) representa uma configuração estável do ponteiro: marca na
tela, canal de detector, orientação de domínio magnético, estado de avalanche
ou outro registro clássico.

O projetor setorial é:

\[
\boxed{
\Pi_i
=
\chi_{\Omega_i}
\quad
\text{ou, mais geralmente, o projetor de Riesz do cluster }i.
}
\]

Para clusters espectrais:

\[
\boxed{
\Pi_i
=
\frac{1}{2\pi i}
\oint_{\Gamma_i}
(z-\mathcal H_\rho)^{-1}\,dz.
}
\]

Aqui \(\Gamma_i\) envolve apenas o cluster associado ao registro \(R_i\).

---

## 3. Quase-ortogonalidade macroscópica

Os registros são macroscópicos quando seus suportes ou clusters têm overlap
exponencialmente pequeno:

\[
\boxed{
\langle R_i,R_j\rangle_{\mathcal U}
=
\operatorname{Tr}(\Pi_i\Pi_j)
=
O(e^{-S_{\rm sep}/\hbar}),
\qquad
i\ne j.
}
\]

No limite de aparelho clássico:

\[
\boxed{
\Pi_i\Pi_j=\delta_{ij}\Pi_i,
\qquad
\sum_i\Pi_i=I_{\rm reg}.
}
\]

Essa é a versão GDQ da seleção de base de ponteiro: a base é a decomposição
estável imposta pelo contorno do aparelho.

---

## 4. Ligação com o observável do sistema

Se o observável medido é:

\[
O_S=\sum_i o_iP_i,
\]

o acoplamento de medição deve satisfazer:

\[
\boxed{
P_i
\longmapsto
\Pi_i.
}
\]

Em linguagem de fluxo:

\[
\boxed{
\operatorname{supp}(P_i\rho_S)
\xrightarrow{\rm interação}
\Omega_i.
}
\]

Assim, a medição implementa fisicamente os projetores \(P_i\) já usados na
regra operacional de Born da Q22.

---

## 5. Estabilidade dos setores

Um setor \(R_i\) é estável se a Hessiana restrita é positiva no subespaço
ortogonal aos modos internos do registro:

\[
\boxed{
\Pi_i\mathcal H_{\rm meas}\Pi_i
\ge
\lambda_{i,0}\Pi_i,
}
\]

e se pequenas perturbações do aparelho não misturam clusters:

\[
\boxed{
\left\|
\Pi_i(\mathcal H+\delta\mathcal H)\Pi_j
\right\|
<
\frac12
\operatorname{dist}(\sigma_i,\sigma_j),
\qquad
i\ne j.
}
\]

Pelo teorema de estabilidade de projetores de Riesz, isso garante que
\(\Pi_i\) varia continuamente sob perturbações pequenas do contorno.

---

## 6. Resultado da etapa 2

Os registros macroscópicos ficam definidos como setores espectrais/bacias:

\[
\boxed{
R_i
=
(\Omega_i,\Pi_i,\mathcal D_i,\mathsf R_i).
}
\]

Status:

\[
\boxed{
\text{Etapa 2 fechada condicionalmente ao domínio e contorno do aparelho.}
}
\]

Não há base de medição universal e abstrata. A base é selecionada pelo
aparelho.

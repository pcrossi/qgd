# Q29 — Obstrução da normalização eletromagnética no espaço de Einstein suave

A inserção da redução de Hopf é

$$
\Phi_Q(z,y)=e^{2A(z,y)}R_H(z,y)^2\kappa_Q^2,
$$

e sua projeção normalizada é

$$
F_Q(z)=\int_{K_E}\Phi_Q\mathcal U,dV.
$$

O coeficiente cinético possui a mesma estrutura causal da Q38:

$$
K_Q^{(E)}
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\oint_\gamma F_Q(z)dz.
$$

No background smooth e steady,

$$
A=A_0,
\quad R_H=R_0,
\quad \int_{K_E}\mathcal U,dV=1,
$$

logo

$$
F_Q=e^{2A_0}R_0^2\kappa_Q^2=\text{constante}
$$

e

$$
\boxed{K_Q^{(E)}=0.}
$$

O fator $(4\pi z)^{-n}$ não cria polo porque é cancelado pela integração e
normalização folha a folha.

Mais geralmente, toda inserção holomorfa e monovalorada fornece integral nula.
Uma normalização não zero exige

$$
\operatorname{Res}_{z_*}F_Q\ne0
$$

ou monodromia/corte físico, dando

$$
K_Q^{(E)}
=\frac{2\pi\hbar}{\Lambda_C^2}
\operatorname{Re}[i\operatorname{Res}_{z_*}F_Q].
$$

Portanto, o espaço de Einstein fixa a norma espacial do gerador, mas não gera
sozinho o coeficiente físico depois do contorno causal. A rota transfere a
normalização de $e$ para o mesmo resíduo de estômato ainda aberto na Q38.

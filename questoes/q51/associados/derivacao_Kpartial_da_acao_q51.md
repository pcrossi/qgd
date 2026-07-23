# Q51 — Derivação formal de \(K_\partial^{\rm phys}\) a partir da ação oficial

## 1. Objetivo

O fechamento da Q51 exige substituir os diagnósticos:

$$
p_{\rm req},
\qquad
E_\partial^{\rm req},
\qquad
S_\alpha^{\rm eff}
$$

por grandezas calculadas diretamente da GDQ.

O objeto central é:

$$
K_\partial^{\rm phys}.
$$

## 2. Ação de partida

Não se introduz ação nuclear externa. A ação física continua sendo:

$$
\mathcal{S}_{\mathrm{GDQ}}
=
\int_{\gamma}
\left[
\int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
$$

O núcleo pesado é um background admissível:

$$
\Phi_N
=
(g_N,J_N,H_N,f_N,\mathcal U_N).
$$

O canal alfa é uma deformação localizada de superfície:

$$
\delta\Phi
=
\delta\Phi_{\rm bulk}
+\delta\Phi_\partial.
$$

## 3. Domínio com superfície nuclear

Regularizamos o núcleo por um domínio:

$$
\Omega_N^\circ
=
\Omega_N\setminus\mathcal N_{\rm core},
$$

com fronteira efetiva:

$$
\Sigma_N
=
\partial\Omega_N^\circ.
$$

Na vizinhança tubular:

$$
(r,\theta,\varphi),
\qquad
r=R_N+\xi,
$$

a deformação de superfície é escrita como:

$$
\delta\Phi_\partial(\theta,\varphi)
=
\sum_a u_a\,\Psi_a(\theta,\varphi).
$$

Os \(\Psi_a\) são modos físicos de superfície, não funções arbitrárias.

## 4. Ação aumentada e vínculos

Os vínculos relevantes são:

1. conservação de carga;
2. conservação de fluxo;
3. normalização de \(\mathcal U\);
4. remoção de translações e rotações rígidas;
5. compatibilidade com o núcleo filho;
6. seleção do canal alfa \(4N\).

Escrevemos:

$$
\mathcal S_{\rm aug}
=
\mathcal S_{\rm GDQ}
+\sum_A\lambda_A C_A[\Phi].
$$

A Hessiana aumentada é:

$$
K_{\rm aug}
=
\operatorname{Hess}_{\Phi_N}\mathcal S_{\rm aug}.
$$

## 5. Projeção física

O projetor físico remove modos de gauge e vínculos:

$$
P_{\rm red}^2=P_{\rm red},
\qquad
C_A P_{\rm red}=0.
$$

Então:

$$
K^{\rm phys}
=
P_{\rm red}K_{\rm aug}P_{\rm red}.
$$

## 6. Separação bulk/superfície

Decompomos:

$$
\delta\Phi
=
(\delta\Phi_I,\delta\Phi_\partial).
$$

Logo:

$$
K^{\rm phys}
=
\begin{pmatrix}
K_{II} & K_{I\partial}\\
K_{\partial I} & K_{\partial\partial}
\end{pmatrix}.
$$

Eliminando os modos internos relaxáveis:

$$
\delta\Phi_I^*
=
-K_{II}^{-1}K_{I\partial}\delta\Phi_\partial.
$$

Substituindo:

$$
\boxed{
K_\partial^{\rm phys}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
}
$$

Esse é o mesmo mecanismo de Schur/DtN usado em Q40, agora aplicado ao canal
alfa.

## 7. Decomposição física de \(K_\partial^{\rm phys}\)

O operador resultante pode ser organizado como:

$$
K_\partial^{\rm phys}
=
P_{\rm red}
[
K_{\rm geom}
+K_{\rm tors}
+K_{\rm shell}
+K_{\rm canal}
]
P_{\rm red}.
$$

Cada termo tem origem:

| Termo | Origem variacional |
| --- | --- |
| \(K_{\rm geom}\) | segunda variação de \(\mathcal R\sqrt g\) na superfície |
| \(K_{\rm tors}\) | segunda variação da conexão de Bismut/torção \(H\) |
| \(K_{\rm shell}\) | espectro de modos de superfície estabilizados |
| \(K_{\rm canal}\) | vínculos de emissão alfa e ortogonalidade ao filho |

## 8. Projetor alfa

Com \(K_\partial^{\rm phys}\) construído, define-se:

$$
P_\alpha
=
\frac1{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_\partial^{\rm phys})^{-1}\,dz.
$$

O projetor físico de emissão é:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}).
$$

## 9. Energia de preformação

O modo nu de quatro nucleons é:

$$
\Phi_{4N}.
$$

A energia de superfície preditiva é:

$$
\boxed{
E_\partial^{\rm GDQ}
=
\langle
P_\perp\Phi_{4N},
K_\partial^{\rm phys}
P_\perp\Phi_{4N}
\rangle_\partial.
}
$$

Então:

$$
S_\alpha^{\rm GDQ}
=
\exp(-E_\partial^{\rm GDQ}).
$$

## 10. Taxa final

Com a frequência normal interna:

$$
\nu_{\rm GDQ}
=
\frac1{2\pi}
\sqrt{
\lambda_{\alpha,{\rm int}}/M_\alpha^{\rm eff}
},
$$

e ação radial:

$$
W_{\rm rad}^{\rm GDQ}
=
\frac2{\hbar}
\int_{r_1}^{r_2}
\sqrt{
2\mu(V_{\rm eff}^{\rm GDQ}-Q_\alpha)
}\,dr,
$$

a taxa é:

$$
\boxed{
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
\exp(-E_\partial^{\rm GDQ})
\exp(-W_{\rm rad}^{\rm GDQ}).
}
$$

## 11. O que está demonstrado aqui

Está demonstrada a estrutura variacional:

$$
\mathcal S_{\rm GDQ}
\to
K^{\rm phys}
\to
K_\partial^{\rm phys}
\to
P_\alpha
\to
E_\partial^{\rm GDQ}
\to
\Gamma_{\rm GDQ}.
$$

## 12. O que ainda falta numericamente

Falta calcular, para cada núcleo:

1. o background \(\Phi_N\);
2. os blocos \(K_{II},K_{I\partial},K_{\partial\partial}\);
3. o subespaço do núcleo filho \(P_{\rm filho}\);
4. o modo \(\Phi_{4N}\);
5. a janela \(\mathcal C_\alpha\);
6. a frequência normal \(\nu_{\rm GDQ}\).

## 13. Veredito

$$
\boxed{
\text{Q51 possui agora a cadeia variacional formal; falta avaliação do background nuclear.}
}
$$


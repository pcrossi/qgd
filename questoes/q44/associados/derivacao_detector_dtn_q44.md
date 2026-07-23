# Q44 — Derivação do detector por DtN/Schur

## 1. Enunciado

Queremos substituir o fator fenomenológico:

$$
\exp(-\sigma_{\rm det}\rho_{\rm det}L)
$$

por um fator derivado de uma impedância de detector:

$$
\exp(-\Gamma_{\rm det}).
$$

O detector é tratado como aparelho clássico/material acoplado ao contorno. Ele
não altera a ação oficial da GDQ; ele define uma condição externa do problema.

---

## 2. Setor reduzido do detector

No primeiro fechamento condicional, usamos um único canal físico do detector,
representado por uma variável $\varphi(s)$ no interior do material:

$$
s\in[0,L].
$$

O funcional quadrático do detector é:

$$
S_{\rm det}^{(2)}[\varphi]
=
\frac12
\int_0^L
\left[
(\partial_s\varphi)^2+\lambda_{\rm det}^2\varphi^2
\right]ds.
$$

Aqui:

- $L$ é a espessura efetiva do material;
- $\lambda_{\rm det}^{-1}$ é o comprimento de resposta do canal material;
- $\varphi(0)$ é o valor acoplado à interface com a partícula;
- $\varphi(L)=0$ representa detector absorvente/aterrado no lado macroscópico.

Essa é a Hessiana efetiva mínima do detector:

$$
K_{\rm det}
=
-\partial_s^2+\lambda_{\rm det}^2.
$$

---

## 3. Operador DtN

A equação estacionária interna é:

$$
\left(-\partial_s^2+\lambda_{\rm det}^2\right)\varphi=0,
$$

com:

$$
\varphi(0)=\varphi_0,
\qquad
\varphi(L)=0.
$$

A solução é:

$$
\varphi(s)
=
\varphi_0
\frac{\sinh[\lambda_{\rm det}(L-s)]}
{\sinh(\lambda_{\rm det}L)}.
$$

Derivando no bordo:

$$
-\partial_s\varphi(0)
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L)\varphi_0.
$$

Logo, a impedância Dirichlet-to-Neumann é:

$$
\boxed{
\mathsf R_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
}
$$

Ela é positiva para $L>0$ e $\lambda_{\rm det}>0$.

---

## 4. Equivalência por complemento de Schur

Discretizando o interior do detector, a Hessiana fica em blocos:

$$
K=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

Eliminar os graus internos $I$ fornece a impedância efetiva no bordo:

$$
\boxed{
\mathsf R_{\rm det}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
}
$$

No limite contínuo do operador acima, esse complemento de Schur converge para:

$$
\mathsf R_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$

---

## 5. Acoplamento às alternativas de caminho

Se o detector tenta distinguir as duas fendas, o campo de interface associado
ao ramo 1 difere do ramo 2. Escrevemos:

$$
\Delta\Phi_{\partial}
=
\Phi_{\partial}^{(1)}-\Phi_{\partial}^{(2)}
=
\zeta_{\rm det}(w_1-w_2),
$$

onde:

- $w_1$ e $w_2$ são perfis normalizados de acoplamento às fendas;
- $\zeta_{\rm det}$ é a intensidade física do acoplamento detector--fluxo;
- $\int_{\partial\Omega}(w_1-w_2)^2d\Sigma=C_{\rm path}$.

Para marcador primitivo normalizado:

$$
C_{\rm path}=1.
$$

---

## 6. Fator de decoerência derivado

O custo quadrático de distinguir os caminhos é:

$$
\Gamma_{\rm det}
=
\frac12
\int_{\partial\Omega}
\Delta\Phi_\partial
\mathsf R_{\rm det}
\Delta\Phi_\partial
d\Sigma.
$$

Substituindo o canal DtN:

$$
\boxed{
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
}
$$

Esse é o substituto GDQ reduzido para o fator legado
$\sigma_{\rm det}\rho_{\rm det}L$.

---

## 7. Densidade no anteparo com detector

A densidade de duas fendas sem detector é:

$$
\rho_0
=
I_1+I_2+2\sqrt{I_1I_2}\cos\Delta\phi.
$$

Com detector, o termo de coerência é amortecido:

$$
\boxed{
\rho_{\rm det}
=
I_1+I_2
+2e^{-\Gamma_{\rm det}}\sqrt{I_1I_2}\cos\Delta\phi.
}
$$

Essa equação tem os limites corretos:

$$
\Gamma_{\rm det}=0
\Rightarrow
\rho_{\rm det}=\rho_0,
$$

$$
\Gamma_{\rm det}\to\infty
\Rightarrow
\rho_{\rm det}=I_1+I_2.
$$

---

## 8. Status

$$
\boxed{
\text{O fator de decoerência foi derivado para um detector linear reduzido.}
}
$$

Limitação:

$$
\boxed{
\text{ainda não é o detector material completo; } \lambda_{\rm det},L,\zeta_{\rm det}
\text{ são dados do aparelho.}
}
$$

Isso é suficiente para fechar a Q44 condicionalmente no nível de teoria de
interface reduzida. Para previsão metrológica de material real, deve-se calcular
$\lambda_{\rm det}$ e $\zeta_{\rm det}$ a partir do background microscópico do
detector.

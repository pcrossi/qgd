# Q34 — Extensão de $a_6$ à conexão de Bismut

## 1. Dados geométricos

O background oficial é Hermitiano:

$$
(M,g,J,H,\nabla^B),
$$

com

$$
\nabla^Bg=0,
\qquad
\nabla^BJ=0,
\qquad
H=d^c\omega,
$$

e, no setor pluriclosed,

$$
dH=0.
$$

A conexão de Bismut é a conexão Hermitiana com torção totalmente
antissimétrica. A convenção de sinal de $H$ deve ser a mesma usada nas
Questões 2 e 17.

## 2. Conexão total

Para uma flutuação com índice geométrico e índice gauge, a conexão produto é

$$
\boxed{
\mathbb D_\mu
=
\nabla_\mu^B\otimes I_G
+I_{TM}\otimes D_\mu^A.
}
$$

Sua curvatura é

$$
\boxed{
\mathbb\Omega_{\mu\nu}
=
\mathcal R_{\mu\nu}^B\otimes I_G
+I_{TM}\otimes\operatorname{ad}(F_{\mu\nu}).
}
$$

Essa substituição transporta a fórmula universal de Seeley--DeWitt para o
background torsional sem acrescentar um termo fundamental novo à ação.

## 3. Cancelamento dos termos mistos puros de $\Omega$

Para grupos semissimples,

$$
\operatorname{tr}_{\rm ad}F_{\mu\nu}=0.
$$

Como $\nabla^B$ é métrica, sua curvatura toma valores na álgebra ortogonal e

$$
\operatorname{tr}_{TM}\mathcal R_{\mu\nu}^B=0.
$$

Consequentemente, no termo quadrático:

$$
\operatorname{tr}\mathbb\Omega^2
=
\dim G\,\operatorname{tr}_{TM}(\mathcal R^B)^2
+\dim M\,\operatorname{tr}_{\rm ad}F^2,
$$

sem termo misto.

O mesmo mecanismo elimina os termos mistos puros de $\mathbb\Omega$ em
$a_6$: cada monômio cruzado em $\mathbb\Omega^3$ contém um traço linear em
$\mathcal R^B$ ou em $F$, e cada termo cruzado derivativo contém
$\operatorname{tr}D^B\mathcal R^B$ ou
$\operatorname{tr}D_AF$, que também se anula.

Logo,

$$
\boxed{
a_6[\mathbb\Omega]_{\rm puro}
=
\dim G\,a_6[\mathcal R^B]
+\dim M\,a_6[F],
}
$$

antes dos termos do endomorfismo $E$.

## 4. Onde os invariantes mistos sobrevivem

O operador vetorial contém um endomorfismo da forma esquemática

$$
\mathbb E
=
E_B+E_F,
$$

com

$$
E_F{}_\nu{}^\rho
=
2\operatorname{ad}(F^\rho{}_\nu).
$$

Se o operador mínimo torsional tiver

$$
E_B{}_\nu{}^\rho
=
-\operatorname{Ric}^B_\nu{}^\rho
+\mathcal T_\nu{}^\rho(H,\nabla^BH),
$$

então termos lineares em $E_F$ desaparecem pelo traço gauge, mas termos com
dois fatores gauge sobrevivem:

$$
\operatorname{tr}(E_BE_F^2),
\qquad
\operatorname{tr}(E_B\Omega_F^2),
\qquad
\operatorname{tr}(E_F\Omega_B\Omega_F).
$$

Após contração, eles geram invariantes do tipo

$$
\operatorname{Ric}^B_{\mu\nu}
\operatorname{tr}(F^{\mu\rho}F^\nu{}_\rho),
$$

$$
\mathcal R^B_{\mu\nu\rho\sigma}
\operatorname{tr}(F^{\mu\nu}F^{\rho\sigma}),
$$

$$
H^2_{\mu\nu}
\operatorname{tr}(F^{\mu\rho}F^\nu{}_\rho),
$$

e termos com $\nabla^BH$ quando a torção não for paralela.

## 5. Setores especiais

### 5.1 Bismut-flat

Se

$$
\mathcal R^B=0,
\qquad
\nabla^BH=0,
$$

o setor gauge reduz exatamente ao resultado plano já calculado:

$$
a_6^{\rm VJ}
=
\frac1{(4\pi)^2}
\left[
\frac{19}{30}\mathcal B
+\frac1{45}\mathcal C
\right].
$$

### 5.2 Apenas Bismut-Ricci-flat

A condição

$$
\operatorname{Ric}^B=0
$$

não implica automaticamente

$$
\mathcal R^B=0.
$$

Portanto, ela pode eliminar parte dos termos de $E_B$, mas não autoriza
descartar todos os invariantes com a curvatura completa.

O cancelamento steady

$$
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}=0
$$

registrado no background Hopf--Bismut é uma condição de Ricci, não uma prova
de Bismut-flatness.

## 6. Termos de bordo

A fórmula integrada usada no cálculo plano descartou

$$
\int\operatorname{tr}(\Omega_{ij;kk}\Omega_{ij}),
\qquad
\int\operatorname{tr}(EE_{;ii}).
$$

Em um domínio com estômato ou colar, essas integrações geram termos de bordo.
Seu cancelamento ou combinação depende da condição Robin/DtN efetivamente
derivada. Não é permitido reutilizar automaticamente a condição escalar de
Neumann do fóton para todos os componentes vetoriais e torsionais.

## 7. Dado ausente para avaliação

Para produzir coeficientes numéricos mistos é necessário fornecer:

$$
\boxed{
\left(
\mathcal R^B_{\mu\nu\rho\sigma},
\nabla^BH,
E_B,
\mathcal D_{\rm bordo}
\right)
}
$$

no mesmo background estável.

O corpus possui o balanço de Ricci--torção e backgrounds reduzidos, mas não a
curvatura completa de Bismut e o endomorfismo vetorial quadrático desse
background. Assim, não existe ainda uma substituição numérica honesta.

## 8. Resultado

$$
\boxed{
\text{a extensão estrutural de }a_6\text{ à conexão produto Bismut--gauge
está construída.}
}
$$

$$
\boxed{
\text{a avaliação dos invariantes mistos depende da curvatura completa,
do operador torsional e do bordo.}
}
$$

Esse é um fechamento estrutural e uma localização precisa da pendência, não
uma previsão quantitativa.

## 9. Referências

1. J.-M. Bismut, “A local index theorem for non Kähler manifolds”,
   *Mathematische Annalen* **284** (1989), no. 4, 681--699. Fonte original
   para a conexão Hermitiana com torção antissimétrica no contexto do índice
   local.
2. D. V. Vassilevich, “Heat kernel expansion: user's manual”,
   *Physics Reports* **388** (2003) 279--360,
   DOI: 10.1016/j.physrep.2003.09.002,
   arXiv:hep-th/0306138. Fórmulas universais de $a_4$ e $a_6$, inclusive
   termos de curvatura e bordo.

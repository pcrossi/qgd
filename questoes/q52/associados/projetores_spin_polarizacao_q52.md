# Q52 — Projetores físicos de spin e polarização na redução Klein--Nishina

## 1. Objetivo

Este adendo completa o ponto fraco do apêndice legado: a passagem da amplitude
geométrica para a soma não polarizada de spin e fóton.

O objetivo não é substituir a GDQ pela QED. O objetivo é registrar a redução
assintótica que a GDQ deve reproduzir quando:

1. o sóliton eletrônico está isolado e estável;
2. o campo fotônico pertence ao kernel \(U(1)_Q\) massless;
3. o background é assintoticamente plano;
4. os modos de gauge e longitudinais foram removidos por \(P_{\rm phys}\);
5. a circulação/Hopf do elétron foi reduzida ao setor Dirac--Bismut efetivo.

Nessas hipóteses, a soma spin/polarização não é uma regra externa; ela é a
forma de completude dos projetores físicos da redução.

## 2. Projetor fotônico

O fóton GDQ é a flutuação massless protegida no canal \(U(1)_Q\):

$$
\delta\Phi_\gamma
=
P_\gamma\delta\Phi.
$$

No domínio assintótico, \(P_\gamma\) reduz ao projetor transversal. Para um
vetor auxiliar \(n^\mu\) com \(k\cdot n\ne0\),

$$
\Pi_{\mu\nu}^{\perp}(k;n)
=
-\eta_{\mu\nu}
+
\frac{k_\mu n_\nu+n_\mu k_\nu}{k\cdot n}
-
\frac{n^2k_\mu k_\nu}{(k\cdot n)^2}.
$$

Logo,

$$
\sum_{\lambda=1}^{2}
\epsilon_\mu^{(\lambda)}(k)
\epsilon_\nu^{(\lambda)}(k)^*
=
\Pi_{\mu\nu}^{\perp}(k;n).
$$

Os termos dependentes de \(n\) não contribuem quando a corrente de Noether do
canal \(U(1)_Q\) é conservada:

$$
k_\mu\mathcal J_Q^\mu=0.
$$

Assim, para observáveis gauge-invariantes, pode-se usar a contração reduzida

$$
\Pi_{\mu\nu}^{\perp}(k;n)
\sim
-\eta_{\mu\nu},
$$

entendendo que os termos longitudinais foram anulados por Ward/Noether, não
por escolha arbitrária.

## 3. Projetor de spin do sóliton

O spin do elétron na GDQ é circulação/Hopf do estômato, não um índice
postulado. No limite assintótico em que a circulação é representada pela
álgebra de Clifford Dirac--Bismut, o projetor de spin fixo pode ser escrito
como

$$
P_s(p)
=
\frac12
(\slashed p+m_ec)
\left(
1+\gamma^5\slashed S_s
\right),
$$

com

$$
S_s\cdot p=0,
\qquad
S_s^2=-1.
$$

Para feixe não polarizado, a média sobre os dois estados de circulação cancela
o termo axial:

$$
\frac12\sum_{s=\pm}
P_s(p)
=
\frac12(\slashed p+m_ec).
$$

Essa é a forma assintótica da média sobre as duas orientações estáveis do
módulo de Hopf.

## 4. Amplitude reduzida

A amplitude GDQ vem de

$$
\mathcal V_{\gamma e\gamma}^{\rm eff}
=
P_\gamma
\mathcal V_e^{(3)}
G_e^{\rm phys}
\mathcal V_e^{(3)}
P_\gamma
+
\mathcal V_e^{(4)}|_{\gamma\gamma ee}.
$$

No limite assintótico Dirac--Bismut, ela reduz à forma bilinear

$$
\mathcal M
=
-e^2
\bar u(p')
\left[
\slashed\epsilon'^{\,*}
\frac{\slashed p+\slashed k+m_ec}{2p\cdot k}
\slashed\epsilon
+
\slashed\epsilon
\frac{\slashed p-\slashed k'+m_ec}{-2p\cdot k'}
\slashed\epsilon'^{\,*}
\right]
u(p).
$$

Na leitura GDQ:

1. os denominadores são os dois ramos do propagador físico;
2. os numeradores são a representação assintótica dos vértices
   \(\mathcal V_e^{(3)}\);
3. o termo de contato é absorvido pela projeção física/identidade de Noether
   que garante a transversalidade da amplitude.

## 5. Soma não polarizada

A quantidade observável é

$$
\overline{|\mathcal M|^2}
=
\frac12
\sum_{s,s'}
\frac12
\sum_{\lambda,\lambda'}
|\mathcal M|^2.
$$

Usando os projetores acima, essa soma se transforma numa contração de traços:

$$
\overline{|\mathcal M|^2}
=
\frac{e^4}{4}
\operatorname{Tr}
\left[
(\slashed p'+m_ec)
\mathcal A_{\mu\nu}
(\slashed p+m_ec)
\overline{\mathcal A}_{\rho\sigma}
\right]
\Pi_\perp^{\mu\rho}(k')
\Pi_\perp^{\nu\sigma}(k),
$$

onde

$$
\mathcal A_{\mu\nu}
=
\gamma_\mu
\frac{\slashed p+\slashed k+m_ec}{2p\cdot k}
\gamma_\nu
+
\gamma_\nu
\frac{\slashed p-\slashed k'+m_ec}{-2p\cdot k'}
\gamma_\mu.
$$

Após usar:

$$
p+k=p'+k',
\qquad
p^2=p'^2=m_e^2c^2,
\qquad
k^2=k'^2=0,
$$

e a transversalidade dos projetores, a parte angular reduzida é:

$$
\boxed{
\mathcal T_{\rm KN}
=
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta.
}
$$

Esse é exatamente o fator que faltava justificar no apêndice legado.

## 6. Interpretação GDQ

O resultado acima mostra que, no setor assintótico:

$$
\text{média spin/polarização}
=
\text{completude dos projetores físicos}.
$$

Portanto, a média não deve ser apresentada como axioma novo. Ela é uma redução
efetiva da estrutura:

$$
P_{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P_{\rm phys}
$$

quando o canal \(U(1)_Q\) e a circulação Hopf do elétron já foram selecionados.

## 7. Limite do adendo

Este adendo ainda não calcula:

$$
P_\gamma,
\qquad
P_s,
\qquad
\mathcal V_{\gamma e\gamma}^{\rm eff}
$$

diretamente no background 8D do sóliton eletrônico.

Ele fecha a redução assintótica. O fechamento metrológico completo exige
avaliar esses três objetos pela Hessiana oficial.

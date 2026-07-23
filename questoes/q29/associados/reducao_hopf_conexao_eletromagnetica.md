# Q29 — Redução da conexão eletromagnética na fibra de Hopf

## 1. Ansatz geométrico

Considere a fibra de Hopf com conexão $\eta$ e introduza o campo externo como
parte da métrica, não como Yang--Mills fundamental:

$$
ds^2
=g_{\mu\nu}(x)dx^\mu dx^\nu
+R^2g_{S^2}
+R^2\left[\eta+\kappa_QA_Q(x)\right]^2.
$$

A curvatura da conexão total é

$$
d\eta+\kappa_QF_Q,
\qquad
F_Q=dA_Q.
$$

Como $d\eta$ possui pernas internas e $F_Q$ possui pernas externas, o produto
cruzado desaparece na contração escalar:

$$
\langle d\eta,F_Q\rangle=0.
$$

## 2. Fórmula de O'Neill

Para raio de fibra constante, a curvatura escalar reduzida contém

$$
\boxed{
\mathcal R_{8}
=\mathcal R_{\rm base}
-\frac{R^2\kappa_Q^2}{4}|F_Q|^2
+\cdots.
}
$$

Esse é o termo cinético de calibre emergente da própria curvatura da ação
oficial. O sinal converte-se no sinal cinético físico após a reconstrução
lorentziana; sua magnitude euclidiana é positiva na Hessiana física.

Integrando o $S^3$ redondo,

$$
\operatorname{Vol}(S^3_R)=2\pi^2R^3,
$$

obtemos, na convenção

$$
S_{4,Q}=\frac14K_Q\int_{M_4}|F_Q|^2dV_4,
$$

$$
\boxed{
\frac{|K_Q|}{C_{\rm GDQ}\tau}
=2\pi^2R^5\kappa_Q^2.
}
$$

Para $R=1{,}99841118477$ e $\kappa_Q=1$,

$$
\frac{|K_Q|}{C_{\rm GDQ}\tau}
=629{,}14\ldots
$$

antes da normalização do gerador $Q$.

## 3. Papel da integral Chern--Simons

A integral interna

$$
\int_{S^3}\eta\wedge d\eta
$$

classifica a fibração e fixa sua carga de Chern. Contudo, na expansão local da
curvatura escalar ela não multiplica o termo $F_Q^2$. O coeficiente cinético
vem de

$$
\operatorname{Vol}(S^3_R)R^2\kappa_Q^2,
$$

enquanto Chern--Simons permanece um invariante separado.

Em particular, a substituição $\eta\to\eta+\kappa_QA_Q$ não produz localmente

$$
\left(\int_{S^3}\eta\wedge d\eta\right)|F_Q|^2.
$$

## 4. Consequência

A tentativa deriva com sucesso o termo cinético eletromagnético da ação
oficial, mas não deriva o dressing

$$
\alpha\frac{3\pi}{2},|F_Q|^2.
$$

Para esse fator aparecer, é necessário um termo misto genuíno envolvendo o
contorno causal ou uma forma de índice de famílias, por exemplo

$$
\int_{\gamma\times S^3}\widehat\eta_Q
\int_{M_4}F_Q\wedge *_4F_Q.
$$

Tal produto não segue da fórmula local de O'Neill. Ele deve ser obtido da
dependência da medida $\mathcal U$, da monodromia em $z_\tau$ ou do
determinante espectral da família de operadores de Bismut.

## 5. Veredito

$$
\boxed{
\text{a ação oficial gera }F_Q^2\text{ geometricamente,}
\quad
\text{mas o fator }3\pi/2\text{ não aparece na redução local.}
}
$$

Portanto, a rota restante é calcular a $\eta$-forma/determinante da família ao
longo do contorno causal, não reutilizar o valor Chern--Simons como rigidez.

A separação do determinante mostrou posteriormente que a $\eta$-forma pertence
à fase ímpar e não ao módulo que contém $F_Q^2$. A normalização deve vir da
parte real $\zeta'$; ver `questoes/q29/associados/eta_forma_nao_veste_rigidez_par.md`.

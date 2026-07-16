# Q29 — Segunda variação da transgressão Q40

## 1. Valor no background não é rigidez

A expressão usada foi

$$
\mathcal I_\partial
=\alpha\left(\frac{3\pi}{2}+\frac{3}{4\pi^3R^3q}\right).
$$

Para identificá-la com uma compliance eletromagnética, é necessário variar os
campos correspondentes. O valor da ação no background, sozinho, não determina
sua Hessiana.

## 2. Parcela Chern--Simons

O termo

$$
\mathcal I_{\rm CS}=\alpha\frac{3\pi}{2}
$$

é um número de holonomia/topologia no setor considerado. Sua variação em
relação aos módulos métricos $(R,q)$ é

$$
\boxed{\nabla^2_{R,q}\mathcal I_{\rm CS}=0.}
$$

Ele não pode ser contado como rigidez métrica apenas por ser positivo.

Sob variações da **conexão**, um funcional Chern--Simons possui Hessiana de
primeira ordem, esquematicamente $k\star d$. Porém, para calculá-la são
necessários o nível $k$, a conexão de background, o domínio e a fixação de
gauge. O número avaliado $3\pi/2$ não determina esses dados.

## 3. Parcela espectral

Defina

$$
u=\log R,
\qquad
v=\log q.
$$

Então

$$
\mathcal I_{\rm throat}
=s_{\rm th}e^{-3u-v},
\qquad
s_{\rm th}=\alpha\frac{3}{4\pi^3}
=1{,}76513113\times10^{-4}.
$$

No ponto unitário,

$$
\boxed{
H_{\rm throat}
=s_{\rm th}
\begin{pmatrix}
9&3\\
3&1
\end{pmatrix}.
}
$$

Seu espectro é

$$
\{0,10s_{\rm th}\}.
$$

Ela fornece rigidez positiva apenas na combinação de volume $3u+v$ e possui
um modo de cisalhamento nulo. Não fornece a compliance eletromagnética completa.

## 4. Consequência numérica

A parcela total anteriormente usada é

$$
\mathcal S_\partial=0{,}03456447695,
$$

mas $99{,}49\%$ desse número vem da avaliação Chern--Simons sem Hessiana
métrica. Usar somente a parcela cuja segunda variação explícita está conhecida
produziria, na mesma fórmula condicional,

$$
\alpha_{\rm eff}^{-1}=137{,}011814688,
$$

e não $132{,}457669$.

## 5. Operador ainda necessário

Para fechar a normalização eletromagnética, deve-se calcular

$$
H_{\partial,Q}
=\left.
\frac{\delta^2}{\delta a_Q^2}
\left[
\alpha\int_{\partial\Sigma}\operatorname{CS}(\mathcal A_*+a_Q)
+\mathcal I_{\rm throat}(\mathcal A_*+a_Q)
\right]
\right|_{a_Q=0},
$$

com condições de contorno e gauge definidos. Depois se calcula o acoplamento
$J_Q$ ao bulk e o Schur

$$
K_Q^{\rm eff}=K_Q-J_QH_{\partial,Q}^{-1}J_Q^\dagger.
$$

Os documentos atuais não especificam $\mathcal A_*$ e $a_Q$ o suficiente para
avaliar esse operador sem introduzir dados novos.

## 6. Veredito

$$
\boxed{
\text{a identificação }
\mathcal S_\partial=K_0/K_\partial
\text{ não foi derivada pela segunda variação disponível.}
}
$$

O complemento de Schur algébrico permanece correto, mas
$\alpha^{-1}=132{,}457669$ continua condicional. Essa conclusão substitui a
interpretação excessivamente forte do valor de transgressão como rigidez.

A redução explícita da fibra de Hopf foi executada em seguida. Ela deriva o
termo $F_Q^2$ pela fórmula de O'Neill, mas confirma que o invariante
Chern--Simons não o multiplica localmente; ver
`q29/reducao_hopf_conexao_eletromagnetica.md`.

# Q29 — Auditoria dimensional da normalização eletromagnética absoluta

## 1. Convenções simultaneamente presentes

Os documentos Q33 e Q36 tratam $\Lambda_C$ como escala de energia/momento:

$$
E_C=\Lambda_C,
\qquad
\ell_C=\frac{\hbar c}{E_C}.
$$

Em unidades naturais,

$$
[E_C]=L^{-1},
\qquad
[\ell_C]=L.
$$

Entretanto, a ação oficial contém

$$
\frac{\hbar}{\Lambda_C^2}.
$$

## 2. Dimensão do funcional de Perelman

Para uma variedade real de dimensão oito,

$$
[\tau]=L^2,
\qquad
[\mathcal R]=L^{-2},
$$

e

$$
\mathcal U
=
\frac{e^{-f}}{(4\pi\tau)^4}
$$

possui dimensão $L^{-8}$. Portanto,

$$
\int_{M_8}\mathcal U,dV_8=1
$$

é adimensional, assim como

$$
\tau\mathcal R,
\qquad
\tau|\nabla f|^2,
\qquad
f-n,
\qquad
\frac{d\tau}{\tau}.
$$

Logo, todo o funcional entre colchetes e sua projeção causal são
adimensionais.

## 3. Incompatibilidade literal

Se $\Lambda_C=E_C$ é energia, então

$$
\left[
\frac{\hbar}{E_C^2}
\right]
=
[\hbar]L^2,
$$

e a expressão não possui dimensão de ação. Se, ao contrário, $\Lambda_C$ for
comprimento,

$$
\left[
\frac{\hbar}{\Lambda_C^2}
\right]
=
[\hbar]L^{-2},
$$

o problema permanece. A medida normalizada não fornece a potência de área
que falta em nenhum dos dois casos.

Portanto,

$$
\boxed{
\text{a normalização absoluta não pode ser extraída enquanto o mesmo símbolo
$\Lambda_C$ desempenhar esses dois papéis.}
}
$$

## 4. Correção interpretativa mínima

Sem alterar o integrando geométrico nem suas equações variacionais, separe:

$$
E_C:=\text{energia de Cartan},
\qquad
\ell_C:=\frac{\hbar c}{E_C}.
$$

Defina o funcional adimensional

$$
\mathcal W_{\rm GDQ}
:=
\mathfrak P_\gamma
\left[
\int_{M_8}
\left{
\tau(\mathcal R+|\nabla f|^2)+f-n
\right}d\mu
\right].
$$

A ação física deve ter a forma

$$
\boxed{
\mathcal S_{\rm phys}
=
\hbar\,Z_C\,\mathcal W_{\rm GDQ},
}
$$

onde $Z_C$ é adimensional. Tomar $Z_C=1$ é a normalização canônica mínima do
quantum de ação, mas isso constitui uma condição de normalização física; não
é consequência da expressão ambígua $\hbar/\Lambda_C^2$.

Equivalentemente, a expressão antiga pode ser lida como uma densidade de ação
por área e a reconstrução física multiplica pela área de Cartan correspondente.
Essa leitura preserva todas as equações anteriores porque o fator é global.

## 5. Redução de Hopf nessa convenção

Com o projetor causal normalizado e $\kappa_Q=1$, a parcela eletromagnética é

$$
\mathcal S_Q
=
\frac{\hbar Z_C}{4}
\mathcal K_Q
\int_{M_4}|F_Q|^2dV_4,
$$

onde $\mathcal K_Q$ é a norma interna adimensional on-shell. Comparando com

$$
\mathcal S_{\rm Maxwell}
=
\frac{\hbar}{4e^2}
\int_{M_4}|F_Q|^2dV_4,
$$

segue

$$
\boxed{
\frac1{e^2}
=
Z_C\mathcal K_Q.
}
$$

O solver com Bismut $\ell=1$ fornece, na convenção radial usada,

$$
\mathcal K_Q=41{,}594825709.
$$

Se fosse imposto $Z_C=1$, isso daria

$$
\alpha^{-1}
=
4\pi\mathcal K_Q
\simeq522{,}697,
$$

e não o valor físico. Portanto, a normalização canônica mínima não fecha a
constante.

## 6. Origem da diferença

O número $41{,}5948$ é uma norma radial calculada depois de normalizar a medida
interna e usar coordenadas adimensionais. Ele ainda não inclui necessariamente:

1. a normalização do modo externo $F_Q$ em coordenadas físicas;
2. o jacobiano entre $x^\mu$ adimensional e $X^\mu=\ell_Cx^\mu$;
3. a separação precisa entre as quatro direções externas e as quatro internas
   na medida de calor de dimensão oito;
4. o fator de frame de Einstein na redução 4D.

Esses fatores formam exatamente $Z_C$. Logo, $Z_C$ não pode ser determinado
pela integral interna isolada.

## 7. Veredito

O projetor causal e a norma de Hopf foram fixados. A tentativa dimensional
mostrou que a ação oficial, lida literalmente com $\Lambda_C$ como energia,
não possui a dimensão declarada. Isso não invalida as equações variacionais,
os espectros ou os dressings, pois um fator global não os altera. Mas impede a
predição absoluta de $\alpha$.

Para fechar, é obrigatório escrever uma única redução com coordenadas físicas

$$
X^\mu=\ell_Cx^\mu,
\qquad
Y^a=\ell_Cy^a,
$$

e derivar $Z_C$ pelo jacobiano completo, sem normalizar separadamente o bulk
antes da fatoração $4+4$.

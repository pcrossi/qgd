# Q30 — Teste variacional do setor sem elongação

## 1. Objetivo

Testar, numa direção de Cartan do setor efetivo $SU(3)$, se a condição
$S=0$ é preservada pela equação variacional da ação GDQ quando existe
holonomia não trivial.

Esse é um teste necessário, não a redução não abeliana completa.

## 2. Métrica KK mínima

Considere a parte $(r,\theta,y)$ da métrica

$$
ds_3^2
=dr^2+r^2d\theta^2
+e^{2S(r)}\left(dy+a(r)d\theta\right)^2.
$$

$S$ é a elongação do ciclo e $a(r)d\theta$ é a conexão geométrica. Sua
curvatura é

$$
F=a'(r)dr\wedge d\theta,
\qquad
F_{mn}F^{mn}=\frac{2(a')^2}{r^2}.
$$

Pela redução exata da curvatura escalar de uma fibra unidimensional,

$$
\boxed{
R_3
=R_2
-\frac14e^{2S}F_{mn}F^{mn}
-2\Delta S-2|\nabla S|^2.
}
$$

Aqui $R_2=0$ no plano transversal de referência. Esse termo quadrático de
$F$ vem da curvatura da métrica KK; não foi acrescentada uma ação de
Yang--Mills.

## 3. Fase horizontal

Para um modo de carga geométrica $q$,

$$
f=u(r)+i\left[v(r)+n_C\theta\right],
$$

a derivada horizontal é

$$
D_\theta f_I=n_C-q a(r).
$$

No ponto $S=0$, defina

$$
K_f
=(u')^2+(v')^2+\frac{(n_C-qa)^2}{r^2}.
$$

## 4. Funcional radial relevante

O determinante KK dá $\sqrt g=r e^S$. Mantendo os momentos causais
$\mathfrak c_1$ e $\mathfrak c_0$ definidos na redução anterior, a parcela
necessária para variar $S$ é

$$
\mathcal I[S]
=\int_0^\infty dr\,r e^{S-u}
\left\{
\mathfrak c_1
\left[R_3+K_f\right]
+\mathfrak c_0(u-4)
\right\}.
$$

Termos dos outros planos internos constantes multiplicam o funcional por um
fator positivo e não alteram a equação local deste teste.

## 5. Equação de elongação em $S=0$

Variando $S$, integrando por partes o termo $-2\Delta\delta S$ com o peso
$e^{-u}$ e supondo que a variação se anule no bordo, obtém-se

$$
\boxed{
\begin{aligned}
\left.
\frac{e^u}{r}\frac{\delta\mathcal I}{\delta S}
\right|_{S=0}
={}&\mathfrak c_1\Bigg[
-\frac34F_{mn}F^{mn}
+K_f
+2\Delta u-2|\nabla u|^2
\Bigg]\\
&+\mathfrak c_0(u-4).
\end{aligned}
}
$$

No ansatz radial,

$$
\Delta u=u''+\frac{u'}r,
\qquad
|\nabla u|^2=(u')^2,
$$

e portanto

$$
\boxed{
\begin{aligned}
0={}&\mathfrak c_1\left[
-\frac{3}{2}\frac{(a')^2}{r^2}
-(u')^2+(v')^2
+\frac{(n_C-qa)^2}{r^2}
+2u''+\frac{2u'}r
\right]\\
&+\mathfrak c_0(u-4).
\end{aligned}
}
$$

Essa é a condição explícita para que “sem elongação” seja dinamicamente
consistente no teste de Cartan.

## 6. Veredito sobre o chute

$S=0$ não é solução automática quando $a'\ne0$. A curvatura da conexão
sourceia o modo de elongação pelo termo

$$
-\frac32\frac{(a')^2}{r^2}.
$$

Contudo, elongação nula é possível se o perfil fundamental $u=\operatorname{Re}f$
e a circulação horizontal satisfizerem a equação de balanço acima. Assim, o
chute do autor torna-se uma condição dinâmica precisa:

$$
\boxed{
\text{torção permitida e elongação nula}
\iff
u,v,a\text{ resolvem o vínculo de balanço de }S.
}
$$

Não é necessário acrescentar uma rigidez externa para proibir elongações; o
campo $u$ já presente na ação pode atuar como multiplicador geométrico do
balanço. Falta demonstrar existência de solução regular simultânea das
equações de $u,v,a$.

## 7. Cautela sobre energia

Na convenção escalar oficial, a redução de $R$ contém
$-e^{2S}F^2/4$. Portanto, não se pode identificar isoladamente essa parcela
com uma energia positiva $+F^2/4$. A tensão física deve ser extraída da
Hessiana física/continuação causal completa e da subtração do background.
Promover diretamente $-R$ a uma energia seria uma mudança de funcional.

## 8. Próximo sistema

O passo seguinte é variar o mesmo funcional em relação a $a$, $u$ e $v$,
obtendo o sistema acoplado com:

$$
a(0)=0,
\qquad
a(\infty)=n_C/q,
$$

e condições de regularidade para $u,v$. Somente uma solução desse sistema
pode fornecer $\sigma_{\rm GDQ}$.

Esse sistema foi derivado em `q30/sistema_radial_minimo_tubo.md`. A comparação
entre as equações de $u$ e $S$ produz
$(a')^2/r^2=\mathfrak c_0/\mathfrak c_1$, incompatível com holonomia finita
não trivial no domínio infinito. O truncamento de uma direção de Cartan está
excluído; a continuação deve preservar a conexão $SU(3)$ completa.

## 9. Classificação

- fórmula KK para $R_3$: redução geométrica no teste de Cartan;
- equação de $S$: derivação variacional condicional ao ansatz;
- hipótese $S=0$: convertida em vínculo dinâmico verificável;
- existência/estabilidade da solução: aberta;
- tensão e gap: ainda não calculados.

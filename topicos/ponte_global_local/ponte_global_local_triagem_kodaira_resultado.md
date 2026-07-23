# Ponte global--local — triagem numérica do caminho Kodaira--Spencer

## 1. Pergunta

Um único modo não homogêneo mais baixo de $S^3$ já pode fornecer, na ordem
linear, a coluna $B_\mu$ necessária para remover a obstrução do matching
homogêneo?

## 2. Teste mínimo

Na esfera unitária $S^3\subset\mathbb R^4$, o primeiro harmônico escalar real
pode ser escrito como

$$
Y_1(x)=\sqrt{\frac4{\operatorname{Vol}S^3}}\,x_0,
\qquad
\operatorname{Vol}S^3=2\pi^2.
$$

Ele satisfaz exatamente

$$
\int_{S^3}Y_1\,dV=0,
$$

$$
\int_{S^3}Y_1^2\,dV=1,
$$

e

$$
\int_{S^3}|\nabla Y_1|^2dV=3.
$$

O script `ponte_global_local_triagem_kodaira_numerica.py` verifica essas
identidades por quadratura estocástica uniforme em $S^3$. A identidade é
analítica; a quadratura é apenas um teste de implementação.

## 3. Regra de seleção

O tripleto residual $(r_a,r_c,r_u)$ pertence ao setor angular singlet do
background homogêneo. Uma perturbação pura em representação não trivial de
$S^3$ possui sobreposição linear nula com esse setor:

$$
P_{\rm singlet}Y_1=0.
$$

Consequentemente, no background exatamente homogêneo e para um modo de
Beltrami que pertença inteiramente a uma representação não trivial da simetria
preservada,

$$
\boxed{B_{\mu_1}^{\rm linear}=0.}
$$

Derivadas angulares não alteram essa conclusão se o operador e seu domínio de
bordo forem equivariantes: eles preservam as representações e a integração em
$S^3$ elimina o termo linear não singlet. Se o domínio, o estômato ou o
background warped já quebrar essa simetria, o argumento deve ser refeito e um
acoplamento linear pode reaparecer.

Isso corrige a expectativa de que qualquer dependência angular, por si só,
garantisse $B_\mu\neq0$. O harmônico escalar usado aqui é um representante de
triagem da regra de seleção; ele não substitui a construção tensorial do
Beltrami físico.

## 4. Canal quadrático

O quadrado do modo contém um singlet:

$$
Y_1^2
=\frac1{\operatorname{Vol}S^3}
+\left(Y_1^2-\frac1{\operatorname{Vol}S^3}\right).
$$

Portanto a retroação de amplitude finita pode alterar o setor homogêneo:

$$
r_i(A)
=r_i(0)+C_i|A|^2+O(|A|^3),
\qquad i\in\{a,c,u\}.
$$

O teste numérico confirma simultaneamente:

$$
\text{sobreposição linear}=0,
\qquad
\text{singlet quadrático}\neq0.
$$

## 5. Veredito da triagem

$$
\boxed{
\text{o caminho não fecha por uma coluna linear de um único harmônico}
\text{ sobre o background homogêneo.}
}
$$

Ele ainda pode fechar por uma bifurcação não homogênea de amplitude finita.
Para decidir isso, o próximo cálculo mínimo não é ainda o solver completo,
mas os cinco coeficientes de Galerkin obtidos da ação oficial:

$$
\lambda_\mu,
\qquad
g_\mu,
\qquad
C_a,
\qquad C_c,
\qquad C_u,
$$

onde

$$
\mathcal S_{\rm red}(A)
=\mathcal S_0+\lambda_\mu|A|^2+g_\mu|A|^4+\cdots
$$

e os $C_i$ medem a retroação quadrática no matching. Uma bifurcação física
exige uma solução estacionária não nula e estável, por exemplo

$$
\lambda_\mu<0,
\qquad
g_\mu>0,
\qquad
|A_*|^2=-\frac{\lambda_\mu}{2g_\mu},
$$

além de compatibilidade de

$$
r_i(0)+C_i|A_*|^2=0
$$

após permitir a resposta dos demais parâmetros do background.

Classificação: teste de consistência/viabilidade por regra de seleção. Não é
uma sela, um ajuste ou uma prova de estabilidade.

## 6. Limite preciso da conclusão

A triagem estabelece condicionalmente:

$$
\text{modo puro não singlet}
+\text{background e bordo equivariantes}
\Longrightarrow
B_\mu^{\rm linear}=0.
$$

Ela não estabelece que todo modo de Kodaira--Spencer tenha acoplamento linear
nulo. Essa afirmação exige decompor o Beltrami tensorial real nas
representações preservadas pelo background Berger e pelo domínio de bordo.

## 7. Verificações tensorial e global posteriores

A decomposição tensorial em `topicos/ponte_global_local/ponte_global_local_kodaira_harmonicos.md`
confirmou que o background Berger preserva

$$
G_B=SU(2)_L\times U(1)_R.
$$

O primeiro setor não constante, $j=1/2$, não contém vetor invariante. Pelo
lema de Schur, seu acoplamento linear com o residual singlet se anula
exatamente. O primeiro efeito permitido é $b^\dagger b$.

Também foram construídas duas famílias globais integráveis no fator de Hopf
$S^1\times S^3$:

1. deformação anisotrópica diagonal do deck;
2. deformação não linear ressonante.

Ambas satisfazem Maurer--Cartan e possuem representantes globais não triviais
como estruturas complexas marcadas. Contudo, a única extensão simultânea de
$(g,J,f)$ que não acrescenta dados externos é um pullback por difeomorfismo.
Pela naturalidade da ação oficial,

$$
\mathcal S_{\rm GDQ}[F^*(g,J,f)]
=\mathcal S_{\rm GDQ}[g,J,f].
$$

Logo, nas duas famílias,

$$
\lambda_\mu=g_\mu=C_a=C_c=C_u=0.
$$

Esses modos são direções modulares/difeomórficas e devem ser removidos pelo
projetor físico. Eles não constituem a bifurcação procurada.

## 8. Conclusão atualizada

A avaliação simples foi levada até seu limite legítimo:

$$
\boxed{
\begin{aligned}
&\text{primeiro modo não singlet: sem acoplamento linear;}\\
&\text{deformações Hopf explícitas: zeros modulares;}\\
&\text{nenhum fechamento numérico físico foi obtido.}
\end{aligned}
}
$$

O próximo modo não pode ser escolhido apenas no espaço de estruturas
complexas. Ele deve ser um autovetor da Hessiana **conjunta** de $(g,J,f)$,
ortogonal às órbitas de difeomorfismos e sujeito ao domínio DtN da interface.
Isso é precisamente o problema espectral não homogêneo completo; uma triagem
de um único harmônico não o substitui.

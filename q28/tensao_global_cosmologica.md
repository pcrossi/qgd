# Q28 — Tensão global no espaço cosmológico e cálculo de $A$

## 1. Objetivo e dados admitidos

O objetivo é calcular a carga global $A$ sem usar como entrada o número de
gerações observado. O domínio cosmológico considerado é

$$
M_{m cos}=T^5\times S^3.
$$

O cálculo usa somente:

1. a orientação de $M_{\rm cos}$;
2. a isotropia global do background cosmológico estacionário, distinguindo a
   isotropia completa de $T^5$ da decomposição térmica física
   $T^5=T^4_{\rm int}\times S^1_\beta$;
3. a colagem mínima ao longo de $S^1_5\times S^3$, com winding
   $\nu(g)=1$;
4. a conservação das classes características durante o fluxo suave da ação
   oficial.

Não se introduz $N_G=3$, $A=18$ nem um termo de Yang--Mills na ação
fundamental.

## 2. Classe que transporta a tensão orientada

Pela fórmula de Künneth,

$$
H^4(T^5,\mathbb Z)\cong\mathbb Z^5.
$$

Escolha uma base integral $e^1,\ldots,e^5$ de $H^1(T^5,\mathbb Z)$ e a
orientação

$$
\Omega_5=e^1\smile e^2\smile e^3\smile e^4\smile e^5.
$$

Uma classe de grau quatro geral pode ser escrita como

$$
a_4=\sum_{i=1}^5 A_i\,\iota_i\Omega_5,
\qquad
A_i\in\mathbb Z.
$$

Por dualidade de Poincaré, $a_4$ transforma como um vetor integral axial

$$
\mathbf A=(A_1,A_2,A_3,A_4,A_5)\in\mathbb Z^5.
$$

Para a escolha de colagem usada anteriormente,

$$
b_1=e^5,
$$

e somente a componente complementar contribui:

$$
N_{ab}
=\left\langle a_4\smile b_1,[T^5]\right\rangle
=A_5.
$$

Esse $A_5$ é o coeficiente anteriormente abreviado por $A$.

## 3. Tensão escalar não é carga característica

A ação oficial pode determinar uma tensão ou energia global escalar, por
exemplo uma integral ponderada de curvatura e gradientes. Essa quantidade é
invariante sob isotropia e pode ser diferente de zero.

Entretanto, $A$ é uma carga orientada e integral. Ela pertence a uma classe
de cohomologia. Não existe uma igualdade dimensional ou topológica automática
entre a norma da tensão cosmológica e $A$. Converter uma energia contínua em
um inteiro exigiria uma identidade de localização ou uma condição de contorno
quantizada adicional, ainda não presente.

## 4. Teorema de isotropia completa

Considere o grupo de isotropia integral orientado do toro, que contém as
permutações orientadas e as inversões simultâneas de dois ciclos. Em
particular, para quaisquer $i\ne j$, ele contém

$$
R_{ij}
=\operatorname{diag}(1,\ldots,-1_i,\ldots,-1_j,\ldots,1),
\qquad
\det R_{ij}=+1.
$$

Se o background é globalmente isotrópico, sua classe deve satisfazer

$$
R_{ij}^*\mathbf A=\mathbf A
$$

para todos os pares $i\ne j$. A componente $A_i$ muda de sinal sob
$R_{ij}$; portanto,

$$
A_i=-A_i.
$$

Como $A_i$ é inteiro,

$$
A_i=0.
$$

Aplicando o argumento a todas as componentes,

$$
\boxed{
H^4(T^5,\mathbb Z)^{G_{\rm iso}}=0
}
$$

e, consequentemente,

$$
\boxed{
a_4=0,
\qquad
A=0.
}
$$

Com $\nu(g)=1$, o teorema local--global já demonstrado fornece

$$
\boxed{
N_G=\frac{A\nu(g)}6=0.
}
$$

Esse é um resultado negativo exato: o background cosmológico homogêneo,
isotrópico e suave não seleciona três gerações.

## 5. Simetria física do espaço de Einstein térmico

O background efetivamente usado pela GDQ não possui isotropia entre todos os
cinco círculos. Ele contém a decomposição

$$
T^5=T^4_{\rm int}\times S^1_\beta,
$$

na qual $S^1_\beta$ é o ciclo térmico/causal. O grupo admissível preserva
$e^5=[S^1_\beta]$ e atua isotropicamente apenas nas quatro direções internas.

Sob esse subgrupo, o setor invariante deixa de ser nulo e possui posto um:

$$
\boxed{
H^4(T^5,\mathbb Z)^{G_{T^4}}
=\mathbb Z\,\operatorname{PD}(e^5).
}
$$

Assim, a forma cosmológica mais geral compatível com a simetria térmica é

$$
\boxed{
a_4=A\,\operatorname{PD}(e^5),
\qquad
A\in\mathbb Z.
}
$$

Como $b_1=e^5$ e $\nu(g)=1$,

$$
N_{ab}=A,
\qquad
N_G=\frac A6.
$$

Portanto, a condição térmica resolve a **direção** da tensão global, mas não
sua **magnitude**. O cálculo sem dado adicional termina em

$$
\boxed{
A\in\mathbb Z,
}
$$

e não em um inteiro particular.

## 6. Por que o fluxo não altera o resultado

Durante uma evolução suave admissível da ação oficial,

$$
\frac{d}{d\tau}[a_4]=0.
$$

Logo, partindo do setor completamente isotrópico,

$$
[a_4](\tau_0)=0
\quad\Longrightarrow\quad
[a_4](\tau)=0.
$$

A dinâmica local pode criar densidades de tensão não uniformes cuja integral
orientada total se cancela, mas não pode transformar continuamente a classe
nula em $A=18$.

No setor térmico, o mesmo argumento conserva o inteiro inicial:

$$
A(\tau)=A(\tau_0).
$$

Ele não determina $A(\tau_0)$.

## 7. Condição mínima para determinar a magnitude

Uma carga não nula requer uma estrutura que reduza a isotropia e selecione um
ciclo primitivo

$$
\ell\in H^1(T^5,\mathbb Z).
$$

O ciclo térmico já realiza essa seleção. Então é permitido escrever

$$
a_4=A\,\operatorname{PD}(\ell),
\qquad
A\in\mathbb Z.
$$

Para fixar o coeficiente, porém, ainda é necessária uma fonte independente:

1. uma condição inicial que especifique o fluxo integral;
2. uma cirurgia cosmológica orientada com multiplicidade calculável;
3. um defeito global cuja classe de clutching seja explicitamente conhecida;
4. uma identidade de localização da ação oficial que converta dados de bordo
   em número característico.

Mesmo após escolher $\ell$, a topologia apenas quantiza $A$; ela não fixa sua
magnitude. Para calcular um valor não nulo é necessária uma equação global de
seleção, por exemplo uma identidade de localização

$$
A
=\mathscr L[\mathfrak B_{\rm cosmológico}]
\in\mathbb Z,
$$

cujo lado direito seja calculável a partir de dados cosmológicos sem usar
$N_G$.

## 8. Veredito

Com isotropia completa de $T^5$,

$$
\boxed{
A[T^5\times S^3,\ \text{isotropia global}]=0.
}
$$

No espaço de Einstein térmico realmente adotado, o círculo $S^1_\beta$ quebra
essa isotropia e o resultado correto é

$$
\boxed{
a_4=A\,\operatorname{PD}(e^5),
\qquad
A\in\mathbb Z.
}
$$

Portanto, $A=18$ não foi derivado. A geometria fixa a direção e quantiza a
carga, mas não escolhe sua magnitude. Usar a tensão escalar ou a energia
escura diretamente como $A$ misturaria uma quantidade contínua com um número
topológico integral. Falta uma identidade global de localização ou uma
condição inicial/cirúrgica que calcule esse inteiro sem recorrer a $N_G=3$.

## 9. Refinamento aritmético pela colagem $\mathbb Z_6$

A integralidade do índice impõe

$$
\frac A6\in\mathbb Z,
$$

logo

$$
\boxed{
A=6k,
\qquad
N_G=k.
}
$$

O setor positivo primitivo fornece $A=6$ e $N_G=1$. Portanto, $A=18$
requer uma multiplicidade global independente $k=3$, calculada como número de
interseção, soma de resíduos ou índice de zeros de uma seção global derivada
da GDQ. O desenvolvimento completo está em
`q28/selecao_aritmetica_carga_global.md`.

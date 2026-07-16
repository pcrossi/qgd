# Regularidade local da garganta e momentos admissíveis

## 1. Enunciado

Pretendia-se ampliar o ansatz dos colares liberando os momentos iniciais
$p_c$ e $p_u$. Antes disso, deve-se verificar se esses dados são compatíveis
com a regularidade da garganta usada pelo solver.

O cálculo abaixo usa somente as equações canônicas reduzidas já derivadas da
ação oficial.

## 2. Expansão local suave

Numa garganta de reflexão suave em $r=0$, os campos escalares radiais são
pares:

$$
a(r)=a_0+a_2r^2+O(r^4),
$$

$$
c(r)=c_0+c_2r^2+O(r^4),
$$

$$
u(r)=u_0+u_2r^2+O(r^4).
$$

Consequentemente,

$$
\dot a(0)=\dot c(0)=\dot u(0)=0.
$$

As velocidades canônicas do colar são

$$
\dot a
=\frac{2c^2+h_0}{2ac},
$$

$$
\dot c
=-\frac{(cp_c+p_u)e^u}{2a^2\tau},
$$

$$
\dot u
=\frac{4c^2\tau-cp_ce^u+2h_0\tau}
{2a^2c\tau}.
$$

A condição topológica já usada no solver é

$$
h_0=-2c_0^2.
$$

Ela fornece automaticamente

$$
\dot a(0)=0.
$$

Na mesma seção,

$$
\dot u(0)
=-\frac{p_c(0)e^{u_0}}{2a_0^2\tau}.
$$

Como $a_0>0$, $\tau>0$ e $e^{u_0}>0$, a regularidade exige

$$
\boxed{p_c(0)=0.}
$$

Substituindo em $\dot c(0)=0$,

$$
\boxed{p_u(0)=0.}
$$

## 3. Consequência para a ampliação proposta

No domínio atual, vale a equivalência

$$
\boxed{
\text{garganta de reflexão suave}
\quad\Longrightarrow\quad
p_c(0)=p_u(0)=0.
}
$$

Portanto, liberar o plano $(p_c,p_u)$ mantendo simultaneamente a interpretação
de garganta suave é inconsistente. Isso explicava a extrema sensibilidade e o
retorno numérico a $p_c\simeq0$ observado em
`ponte_global_local_extensao_pc.py`.

## 4. Alternativas fisicamente distintas

Há somente três maneiras coerentes de obter momentos iniciais não nulos:

1. substituir a garganta de reflexão por uma fronteira física com condição
   Robin derivada e fonte de interface;
2. deslocar a seção inicial para fora da garganta, mantendo $p_c=p_u=0$ no
   verdadeiro ponto de reflexão;
3. ampliar os campos reduzidos, especialmente $J$, de modo que a relação
   momento--velocidade mude pela própria Hessiana oficial.

A opção 2 já está representada pelo comprimento variável dos colares: os
momentos evoluem a partir da garganta até a interface. A opção 1 requer uma
fonte de bordo que ainda não foi derivada. Assim, a menor ampliação intrínseca
restante é a opção 3, isto é, restaurar ao menos o modo de $\delta J$ indicado
pelo matching anisotrópico.

## 5. Veredito

O solver de onze parâmetros não omitiu momentos regulares livres na
garganta. A obstrução residual não pode ser removida legalmente ajustando
$p_c(0)$ ou $p_u(0)$.

Antes de nova execução é necessário derivar a redução cohomogeneidade-1 com
um modo variável de estrutura Hermitiana $J$ ou uma ação de interface Robin
obtida variacionalmente. Sem uma dessas construções, qualquer continuação que
libere $(p_c,p_u)$ troca o problema físico por uma fonte não especificada.

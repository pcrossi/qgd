# Resultado da primeira busca condicional da sela

## Classificação

$$
\boxed{
\text{teste numérico de existência; nenhuma raiz aceita}
}
$$

Nenhum observável foi usado como alvo.

## 1. Primeira tentativa

A busca com cinco parâmetros não incluiu a compatibilidade da restrição do
lapse na interface. Embora o otimizador tenha parado, obteve

$$
\max|\mathcal C_N^+|=0{,}1208565.
$$

Essa tentativa é inválida como candidata à sela.

## 2. Tentativa corrigida

Foi acrescentado ao resíduo

$$
\mathcal C_N^+(s_-)=0
$$

e o comprimento do colar foi liberado como sexta variável. O resultado foi

$$
\|\mathfrak F\|=0{,}0191852,
$$

$$
\max|\mathcal C_N^-|
=3{,}00\times10^{-6},
$$

$$
\max|\mathcal C_N^+|
=1{,}12\times10^{-2}.
$$

Além disso, vários parâmetros atingiram ou se aproximaram dos limites da
busca. Portanto:

$$
\boxed{
\text{a solução não é aceita como raiz.}
}
$$

## 3. Interpretação

O fracasso não demonstra inexistência da sela da GDQ. Ele exclui apenas a
combinação adicional de hipóteses:

1. dois lados exatamente refletidos;
2. $S^3$ redondo no plano médio;
3. warp toroidal Dirichlet na interface;
4. ausência temporária do vínculo energético.

A reflexão e o arredondamento foram condições auxiliares, não consequências
da ação. O próximo solver deve tratar duas interfaces independentes e deixar
a ação determinar a assimetria e o squashing globais.

## 4. Próxima formulação

Usar dois colares com dados independentes

$$
\mathbf d_-,
\qquad
\mathbf d_+,
$$

e um exterior entre eles. O resíduo deve conter apenas:

1. colagem variacional em $Y_-$ e $Y_+$;
2. restrição do lapse;
3. normalização;
4. vínculos cosmológicos;
5. neutralidade de carga e fluxo;
6. energia de Noether.

Não se deve impor reflexão nem $a=c$ fora do que os vínculos exigirem.

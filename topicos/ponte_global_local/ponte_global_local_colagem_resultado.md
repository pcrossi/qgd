# Resultado do teste de colagem colar--exterior

## Classificação

$$
\boxed{
\text{teste de consistência de interface com fixture sintético}
}
$$

## Resultados

O script `ponte_global_local_colagem.py` forneceu

$$
\max|\mathcal C_N^-|
=1{,}421\times10^{-14},
$$

$$
\max|\mathfrak F_Y|=0,
$$

$$
\max|\mathcal C_N^+|
=2{,}220\times10^{-15}.
$$

Assim, a conversão

$$
p_y=a\Pi_a,
\qquad
p_z=c\Pi_c,
\qquad
p_u=\Pi_u,
\qquad
p_v=\Pi_v
$$

preserva exatamente os traços e momentos na precisão usada.

## Teste de fechamento refletido sem ajuste

Na extremidade do trecho exterior, o resíduo de velocidades foi

$$
(-0{,}02508371,
0{,}29632183,
0{,}24371785,
0{,}77613257,
0),
$$

com norma

$$
\boxed{
\|\mathfrak F_{\rm refl}\|=0{,}8661501.
}
$$

Logo, o fixture histórico não fecha por reflexão e não é uma sela global.
Esse resultado negativo foi preservado; nenhum parâmetro foi ajustado.

## Conclusão

$$
\boxed{
\text{adaptador validado; busca da sela ainda necessária.}
}
$$

A próxima implementação deve variar simultaneamente os dados livres dos dois
colares, $p_x$, $\lambda_N$ e os traços de interface, sob os vínculos
cosmológicos. O componente energético deve ser incluído antes de qualquer
declaração física final.

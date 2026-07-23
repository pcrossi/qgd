# Ponte global--local — zero mode da normalização

## 1. Multiplicador global

A normalização

$$
\int\mathcal U\,dV=1
$$

introduz um multiplicador $\lambda_N$. No funcional reduzido ele aparece por

$$
u-4
\longrightarrow
u-4-\lambda_N.
$$

## 2. Simetria de deslocamento

Considere

$$
u_\lambda=u_0+\lambda_N.
$$

Como os momentos canônicos contêm $e^{-u}$, defina

$$
p_{A,\lambda}=e^{-\lambda_N}p_{A,0}.
$$

Então

$$
p_{A,\lambda}e^{u_\lambda}
=p_{A,0}e^{u_0},
$$

e

$$
p_{A,\lambda}p_{B,\lambda}e^{2u_\lambda}
=p_{A,0}p_{B,0}e^{2u_0}.
$$

Além disso,

$$
u_\lambda-4-\lambda_N=u_0-4.
$$

Logo as equações geométricas, as restrições do lapse e as velocidades são
invariantes sob a transformação conjunta.

## 3. Normalização acumulada

A densidade transforma como

$$
\mathscr V_\lambda
=e^{-\lambda_N}\mathscr V_0.
$$

Se a solução de forma possui normalização não ajustada $Z_0$, a condição
$Z=Z_{\rm cos}$ determina

$$
\boxed{
\lambda_N
=\log\frac{Z_0}{Z_{\rm cos}}.
}
$$

Esse valor não altera a geometria encontrada; apenas normaliza a medida e
reescala os momentos conjugados.

## 4. Consequência computacional

A busca pode ser dividida em duas etapas sem perda:

1. resolver a forma geométrica na gauge $\lambda_N=0$;
2. aplicar o deslocamento acima para impor a normalização física.

Isso não é ajuste fenomenológico: $\lambda_N$ é o multiplicador exato de uma
restrição constitucional.

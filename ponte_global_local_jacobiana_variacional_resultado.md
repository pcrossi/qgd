# Resultado da Jacobiana variacional da colagem

## 1. Validação da Jacobiana

A Jacobiana transportada foi comparada com uma derivada direcional central
independente. O erro relativo foi

$$
1{,}912\times10^{-4}.
$$

Além disso, no candidato final, o resíduo transportado e o resíduo obtido por
reintegração precisa coincidiram nas casas exibidas. Portanto a propagação de
sensibilidades está numericamente consistente para o diagnóstico de posto.

## 2. Busca

Em 120 avaliações, a norma precisa foi reduzida para

$$
\|\mathfrak F\|
=7{,}660526\times10^{-4}.
$$

Ela não satisfaz o critério de raiz e não foi aceita.

## 3. Espectro singular

Os valores singulares da Jacobiana foram

$$
\begin{aligned}
&(1{,}3345\times10^4,
1{,}8409\times10^3,
5{,}8934\times10^2,
5{,}1153,
8{,}5934\times10^{-1},\\
&9{,}5254\times10^{-3},
2{,}1910\times10^{-3},
1{,}1986\times10^{-3},
4{,}8907\times10^{-17},
0).
\end{aligned}
$$

Logo,

$$
\boxed{
\operatorname{rank}D\mathfrak F=8.
}
$$

## 4. Origem dos dois zeros

No setor estacionário usado,

$$
v=\text{constante},
\qquad
p_v=0.
$$

Consequentemente, os resíduos de diferença de fase e de fluxo de fase são
identicamente nulos e não fixam parâmetros geométricos. Depois de removê-los,
restam oito equações independentes para dez parâmetros.

Os dois dados globais que devem substituir essas linhas são precisamente

$$
\mathcal C_R=0
$$

e

$$
\mathcal C_E=0.
$$

O comprimento cosmológico já está fixado pelo domínio exterior. A
normalização atua pelo zero mode de $u$ e é aplicada posteriormente.

## 5. Conclusão

O não fechamento anterior não é evidência de inexistência nem de
instabilidade. O sistema numérico estava subdeterminado por dois módulos:

$$
\boxed{
\text{a busca integral deve substituir os dois resíduos triviais por
raio e energia cosmológicos.}
}
$$

$\mathcal C_R$ já possui primeira e segunda variações explícitas. A etapa
realmente faltante é avaliar $\mathcal C_E=\mathcal H_\xi-E_H$ no ansatz
exterior. Só então a Jacobiana física deve ter posto dez.

## 6. Atualização: inserção efetiva de $\mathcal C_R$

O vínculo de raio Berger foi implementado por

$$
\mathcal C_R=\frac{2y+z}{3}-\log R_{\rm cos}.
$$

O teste registrado em `ponte_global_local_raio_energia_resultado.md` elevou o
posto de oito para nove. O único valor singular exatamente nulo restante
corresponde à linha $p_v=0$, que deve ser substituída por $\mathcal C_E$.

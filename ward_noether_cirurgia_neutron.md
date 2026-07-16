# Ward--Noether no matching da cirurgia do nêutron

## 1. Enunciado

Testar se homogeneidade, isotropia, conservação de energia e conservação das
cargas elétrica e torsional determinam, sem dado adicional, os coeficientes

$$
\mathcal M_0=C_SS+C_TT
$$

e, consequentemente, a taxa do decaimento.

## 2. Consequências das simetrias do espaço-tempo

Homogeneidade espacial e temporal fornecem

$$
\mathcal M_{fi}
=(2\pi)^4\delta^{(4)}(P_f-P_i)\,\widehat{\mathcal M}_{fi}.
$$

Isotropia exige que $\widehat{\mathcal M}_{fi}$ seja escalar. Para quatro
seções de spin $1/2$, o subespaço de escalares possui dimensão dois:

$$
\widehat{\mathcal M}_{fi}=C_SS+C_TT.
$$

Logo, as simetrias do espaço-tempo fixam o delta de conservação e a base
angular, mas deixam dois elementos reduzidos.

## 3. Identidades de Ward das cargas

Se $J_A^\mu$ é a corrente de Noether de uma carga conservada $Q_A$, então

$$
\nabla_\mu J_A^\mu=0
$$

e o vértice amputado satisfaz esquematicamente

$$
q_\mu\Gamma_A^\mu
=\sum_{r\in\mathrm{ext}}\epsilon_rQ_{A,r}K_r,
$$

onde $K_r$ é o operador quadrático inverso da perna externa e
$\epsilon_r=+1$ para saída, $-1$ para entrada. On-shell, $K_r\psi_r=0$, e a
identidade reduz-se a

$$
\boxed{q_\mu\Gamma_A^\mu=0.}
$$

O balanço das cargas fornece separadamente

$$
\sum_r\epsilon_rQ_{{\rm EM},r}=0,
\qquad
\sum_r\epsilon_rQ_{T,r}=0.
$$

Essas equações excluem canais que não conservam carga.

## 4. Parte longitudinal e parte transversal

Decomponha

$$
\Gamma_A^\mu
=\Gamma_{A,L}^\mu+\Gamma_{A,\perp}^\mu,
\qquad
q_\mu\Gamma_{A,\perp}^\mu=0.
$$

A identidade de Ward determina a parte longitudinal. Ela não determina
$\Gamma_{A,\perp}^\mu$. Os dois invariantes $S,T$ pertencem precisamente ao
vértice físico transversal on-shell. Assim,

$$
\boxed{
\text{Ward--Noether não fornece equações algébricas para }C_S,C_T.
}
$$

## 5. Por que a normalização da carga não fixa a transição

Para um estado dentro do mesmo setor, a normalização da corrente pode impor

$$
F_A(0)=Q_A.
$$

Mas o processo em estudo liga estratos diferentes,

$$
\mathscr C_n\longrightarrow\mathscr C_{p+2}.
$$

A carga elétrica conservada é diagonal nos setores assintóticos. Ela fixa
$Q_n=0$, $Q_p=+1$, $Q_e=-1$ e $Q_{\bar\nu}=0$, mas não é um gerador já
construído que transforme $n$ em $p+e+\bar\nu$. A conservação torsional fixa
a classe total, mas não a norma do operador de matching entre os estratos.

Há também uma obstrução dimensional: $Q_A$ é adimensional, enquanto
$C_S,C_T$ têm dimensão $\mathrm{GeV}^{-2}$. A escala
$\hbar/\Lambda_C^2$ vem da ação, mas permanece multiplicada pelos overlaps
adimensionais dos perfis causais.

## 6. Teste de liberdade residual

Para qualquer número complexo $\lambda$, a transformação

$$
C_S\mapsto\lambda C_S,
\qquad
C_T\mapsto\lambda C_T
$$

preserva:

1. o delta de energia--momento;
2. isotropia;
3. todas as cargas externas;
4. as identidades de Ward homogêneas on-shell.

Contudo,

$$
\Gamma_n\mapsto|\lambda|^2\Gamma_n.
$$

Logo, existe ao menos uma liberdade contínua de normalização que Noether não
remove. Além disso, a razão $C_T/C_S$ também é livre enquanto nenhuma
simetria adicional relacionar os dois escalares.

## 7. Papel da ação oficial

Noether não precisa fornecer a magnitude: a própria ação deve fazê-lo. O
vértice efetivo de quatro modos é a quarta variação física, incluindo a
eliminação dos modos transversais:

$$
\boxed{
\mathcal V_{\rm eff}^{(4)}
=\mathcal S_{\rm GDQ}^{(4)}
-\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+\text{permutações}.
}
$$

Sua projeção fornece $F_S(z)$ e $F_T(z)$. O contorno causal então extrai

$$
C_A
=\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}[z^3]F_A,
\qquad A\in\{S,T\}.
$$

## 8. Teorema de suficiência corrigido

> Homogeneidade, isotropia e as cargas de Noether são suficientes para fixar
> a cinemática, as regras de seleção, a base de dois invariantes e a medida de
> fase. Elas são suficientes para fixar a taxa somente quando, adicionalmente,
> a ação oficial e o matching causal determinam os elementos reduzidos
> $C_S,C_T$.

Portanto,

$$
\boxed{
\text{Noether} + \text{ação projetada} + \text{matching}
\Longrightarrow \Gamma_n,
}
$$

mas

$$
\boxed{
\text{Noether isoladamente}\not\Longrightarrow\Gamma_n.
}
$$

## 9. Status

- conservação e seleção: demonstradas;
- completude dos dois invariantes: demonstrada;
- liberdade transversal de normalização: demonstrada;
- quarta variação projetada no background cirúrgico: aberta;
- taxa condicional e histórica: já calculadas;
- taxa causal única: aberta até a projeção da quarta variação.

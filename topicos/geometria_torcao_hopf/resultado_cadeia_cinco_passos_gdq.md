# Cadeia GDQ das duas calotas, colar e modos de saída

## 1. Enunciado e domínio

O objetivo é restringir a ação oficial da GDQ a uma família de cirurgia
formada por duas calotas redondas ligadas por um colar, com fluxo torsional
fixo

$$
Q_T=\int_{\Sigma_r}H=2\tau_T,
$$

e calcular, sem inserir QCD nem calibrar pela vida média do nêutron:

1. a ação radial reduzida;
2. o potencial de cirurgia;
3. o coeficiente cinético causal;
4. os dois modos de saída de Dirac--Bismut;
5. o overlap causal que normaliza a taxa.

O cálculo é feito no bulk local oficial

$$
M=\mathbb R^4\times T^4,
$$

usando localmente uma região de cirurgia em $\mathbb R^4$ e mantendo o
$T^4$ espectador. As calotas não são identificadas com o espaço cosmológico
$T^5\times S^3$.

Neste documento, $\tau_T$ denota a unidade de torção do estômato. Ela não é o
parâmetro de fluxo $\tau$ nem a variável causal $z_\tau$ da ação oficial.

## 2. Restrição da ação oficial

Não se acrescenta termo à ação. Usa-se

$$
\mathcal S_{\rm GDQ}
=\int_\gamma\left[\int_M\frac{\hbar}{\Lambda_C^2}
\left\{\tau\left(\mathcal R+|\partial f|^2\right)
+\frac{f+\bar f}{2}-4\right\}
\mathcal U\sqrt{g}\,d^8x\right]\frac{d\tau}{\tau}.
$$

Considere duas meias $S^4_r$ e um colar produto
$S^3_r\times[0,\ell r]$. Para o benchmark redondo,

$$
\int_{2\,\mathrm{calotas}}\mathcal R\,dV=32\pi^2r^2,
\qquad
\int_{\mathrm{colar}}\mathcal R\,dV=12\pi^2\ell r^2,
$$

e

$$
V_{2\,\mathrm{calotas}}=\frac{8\pi^2}{3}r^4,
\qquad
V_{\mathrm{colar}}=2\pi^2\ell r^4.
$$

A conservação de $Q_T=2\tau_T$ fornece, para
$V(r)=V_0+\nu_3r^3+O(r^4)$,

$$
E_T(r)=\frac{\kappa_TQ_T^2}{2V(r)}
=E_T(0)-\frac{2\kappa_T\tau_T^2\nu_3}{V_0^2}r^3+O(r^4).
$$

Logo, após integrar $T^4$, a medida ponderada e o contorno causal, a
restrição da ação tem a forma

$$
\mathcal A_{\rm red}[r]
=\int ds\left[\frac{M_r}{2}\left(\frac{dr}{ds}\right)^2+U(r)\right]
+O(r^5,\dot r^4).
$$

Esta é uma redução da ação oficial no ansatz declarado, não uma nova ação
fundamental.

## 3. Potencial da cirurgia

O potencial obtido é

$$
\boxed{U(r)=A_2r^2-B_3r^3+C_4r^4+O(r^5),}
$$

com

$$
\boxed{
A_2=\pi^2(32+12\ell)w_R+A_2^{\rm cola},
}
$$

$$
\boxed{
B_3=\frac{2\kappa_T\tau_T^2\nu_3}{V_0^2},
}
$$

$$
\boxed{
C_4=\pi^2\left(\frac83+2\ell\right)w_V+C_4^{\rm cola}.
}
$$

Aqui $w_R$ e $w_V$ são os momentos causais completos da densidade ponderada
dos blocos de curvatura e potencial. Os termos de cola incluem a relaxação de
$f$, a junção suave e o complemento de Schur dos modos transversais. Eles não
podem ser postos iguais a zero sem uma condição adicional de matching.

Existe um ramo bimodal de menor ação quando

$$
B_3^2>4A_2C_4.
$$

Os pontos estacionários não nulos são

$$
r_\pm=\frac{3B_3\pm\sqrt{9B_3^2-32A_2C_4}}{8C_4}.
$$

## 4. Coeficiente cinético e mobilidade causal

Se $F_{rr}^{(2)}(z)$ é o pullback completo da Hessiana física no modo radial,
antes do fator $(4\pi z)^{-4}$, escreva

$$
F_{rr}^{(2)}(z)=\sum_{k\in\mathbb Z}G_{r,k}z^k.
$$

O princípio de Laurent da Q4/Q9 dá, para orientação positiva de $\gamma$,

$$
\boxed{
M_r
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}G_{r,3}
\right].
}
$$

Na convenção já usada no mecanismo, $M_r$ multiplica $\dot r^2/2$ e é,
portanto, a **inércia coletiva causal**. A mobilidade no sentido usual é

$$
\boxed{\mu_r=M_r^{-1},}
$$

quando $M_r>0$. O valor auxiliar $R^2/(6\tau)$ do fluxo de Perelman não pode
substituir este coeficiente físico.

Se a família $(g(z),f(z),\bar f(z))$ for congelada ao longo de $\gamma$, então
$G_{r,3}=0$. Nesse caso não há termo cinético físico extraído pelo contorno:
$M_r=0$ e $\mu_r$ não está definida. Portanto, um valor não nulo exige o
terceiro jato da família causal.

## 5. Dois modos de saída de Dirac--Bismut

Na borda $S^3_r$, com orientação Cartan--Schouten positiva, o operador usado é

$$
D_{m,-3/2}^{(j)}
=\frac1r\left(2\boldsymbol\sigma\!\cdot\!\mathbf L-m\sigma_3\right).
$$

### 5.1 Estômato eletrônico

Para $m=-1$ e $j=1/2$, o bloco tem espectro, em unidades de $r^{-1}$,

$$
\{-1-\sqrt5,\ 0,\ \sqrt5-1,\ 2\}.
$$

O kernel do bloco é unidimensional e tem resíduo numérico nulo. A
multiplicidade espectadora de Peter--Weyl é $2$, de modo que o espaço físico
antes da projeção APS tem dimensão $2$. O representante calculado na base do
script é

$$
\psi_e=(0,0,1,0)^T.
$$

### 5.2 Onda torsional neutra

Para $m=0$ e $j=0$,

$$
D_{0,-3/2}^{(0)}=0_{2\times2}.
$$

O kernel neutro tem dimensão $2$. A condição APS e a orientação da corrente
devem selecionar o subespaço efetivamente **de saída**; a equação tangencial
isolada não escolhe entre as duas bases.

Na ontologia GDQ adotada para o decaimento do nêutron, este é precisamente o
setor do antineutrino: uma onda propagante de torção/fase, eletricamente
neutra e sem estômato localizado. Assim, o modo neutro não é uma saída ainda
ausente da construção; o dado que falta é sua normalização causal completa.

No cobordismo da cirurgia ele deve carregar simultaneamente o fluxo residual
de torção e a parcela contínua de energia:

$$
Q_T^{(\bar\nu)}
=Q_T^{(n)}-Q_T^{(p)}-Q_T^{(e)},
$$

$$
E_{\bar\nu}
=M_nc^2-M_pc^2-E_e-E_{\rm recoil}.
$$

Essas são condições de conservação, não valores ajustáveis. Elas não fixam,
por si sós, a norma do vértice de transição.

Esses resultados são exatos para o operador declarado e foram verificados
por diagonalização independente no script de apoio.

## 6. Overlap causal

O elemento físico envolve quatro modos, conforme a definição já vigente:

$$
\mathcal M_0
=\mathcal V_{\rm GDQ}^{(k)}
[\psi_n,\psi_p,\psi_e,\psi_{\bar\nu}].
$$

O teste apenas entre o modo eletrônico $j=1/2$ e o modo neutro orbital $j=0$
fornece zero para um operador orbital escalar. Esse é somente um overlap
**parcial**. Ele não inclui a transição bariônica $n\to p$ e, portanto, não
determina $\mathcal M_0$.

Como $n$, $p$, $e$ e o modo neutro possuem seções efetivas de spin $1/2$, a
álgebra $SU(2)$ admite dois escalares independentes:

$$
S=(\chi_p^\dagger\chi_n)(\chi_e^\dagger\chi_{\bar\nu}),
$$

$$
T=\sum_{i=1}^3
(\chi_p^\dagger\sigma_i\chi_n)
(\chi_e^\dagger\sigma_i\chi_{\bar\nu}).
$$

Logo, a forma angular mais geral produzida pela ação invariante é

$$
\boxed{\mathcal M_0=C_S S+C_T T.}
$$

Se $F_S(z)$ e $F_T(z)$ são as projeções radiais completas da primeira
variação não nula da ação nos dois canais, o contorno causal fixa

$$
\boxed{
C_A
=\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}[z^3]F_A(z),
\qquad A\in\{S,T\}.
}
$$

Fazendo média no spin inicial do nêutron e somando os spins finais, a álgebra
de Pauli fornece exatamente

$$
\boxed{
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=2|C_S|^2+6|C_T|^2.
}
$$

O termo cruzado é nulo. Portanto, um vértice completo espacialmente homogêneo
**não está excluído** pela seleção angular. A conclusão anterior
$\mathcal M_0^{\rm homog}=0$ foi retirada porque omitia os modos bariônicos.

Para observáveis polarizados, a separação dos canais requer resolver as duas
projeções

$$
F_S(z),
\qquad
F_T(z)
$$

até terceira ordem em $z$, incluindo os perfis espaciais normalizados de
$n$ e $p$. Para a taxa total, porém, a lei GDQ de relaxamento já fixa a
combinação contraída

$$
2|C_S|^2+6|C_T|^2
=\frac{15\pi^3}{16}\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

Logo, a separação individual não é uma pendência da meia-vida.

## 7. Resultado dos cinco passos

| Passo | Resultado | Status |
|---|---|---|
| ação no ansatz | redução radial da ação oficial | derivação efetiva |
| $A_2,B_3,C_4$ | fórmulas geométricas e torsional; matching explícito | paramétrico |
| $M_r$ | resíduo do terceiro jato $G_{r,3}$ | fórmula exata; valor aberto |
| dois modos | kernels carregado e neutro calculados | exato no operador declarado |
| $\mathcal M_0$ | dois invariantes $C_SS+C_TT$; Gram $\operatorname{diag}(2,6)$ | combinação contraída fechada para a taxa; separação aberta para polarização |

O cálculo reduz $M_r$ ao terceiro jato da família causal. No overlap, a lei
de relaxamento fixa a norma contraída dos dois resíduos e fecha a taxa total.
Os resíduos separados permanecem necessários somente para correlações
angulares e polarização. A conservação de torção fixa ainda a carga
$2\tau_T$ do canal.

## 8. Reprodutibilidade

O espectro e as fórmulas radiais são implementados em
`neutron/resolver_cadeia_gdq_neutron.py`. A saída sem parâmetros causais está
registrada em `neutron/saida_cadeia_gdq_neutron.md`. A álgebra do overlap
completo é verificada em `neutron/verificar_overlap_quatro_modos.py`, com
saída em `neutron/saida_overlap_quatro_modos.md`.

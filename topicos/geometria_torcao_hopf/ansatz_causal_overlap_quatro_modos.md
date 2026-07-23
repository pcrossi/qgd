# Ansatz causal mínimo para o overlap de quatro modos

## 1. Correção de domínio

O overlap do decaimento é o funcional de quatro modos

$$
\mathcal M_0
=\mathcal V_{\rm GDQ}^{(k)}
[\psi_n,\psi_p,\psi_e,\psi_{\bar\nu}],
$$

e não o produto interno isolado entre os dois modos emitidos. A
ortogonalidade orbital desse par é verdadeira, mas não decide a amplitude
completa porque a transição $n\to p$ também participa da contração angular.

## 2. Base invariante completa

Para quatro seções efetivas de spin $1/2$, a invariância $SU(2)$ deixa dois
escalares independentes:

$$
S=(\chi_p^\dagger\chi_n)(\chi_e^\dagger\chi_{\bar\nu}),
$$

$$
T=\sum_{i=1}^{3}
(\chi_p^\dagger\sigma_i\chi_n)
(\chi_e^\dagger\sigma_i\chi_{\bar\nu}).
$$

Logo,

$$
\boxed{\mathcal M_0=C_SS+C_TT.}
$$

A identidade de Fierz

$$
\sum_i(\sigma_i)_{ab}(\sigma_i)_{cd}
=2\delta_{ad}\delta_{cb}-\delta_{ab}\delta_{cd}
$$

mostra que essa base é completa. Com média no spin inicial e soma nos spins
finais,

$$
\boxed{
\operatorname{Gram}(S,T)
=\begin{pmatrix}2&0\\0&6\end{pmatrix},
}
$$

e

$$
\boxed{
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=2|C_S|^2+6|C_T|^2.
}
$$

Essa decomposição é representação geométrica dos modos GDQ. Não introduz
uma interação fraca externa.

## 3. Extração causal pela ação oficial

Se $\mathcal Q_A^{(k)}$ é a primeira variação não nula da densidade oficial
projetada no canal $A\in\{S,T\}$, defina

$$
P(z)=\frac{d\tau}{dz}\frac1{\tau(z)},
$$

$$
N_A(z)=\int_M e^{-\sigma(z)}\sqrt{g(z)}\,
\mathcal Q_A^{(k)}(z)\,d^8x.
$$

Então $F_A(z)=P(z)N_A(z)$ e, para orientação positiva de $\gamma$,

$$
\boxed{
C_A
=\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}[z^3]F_A(z).
}
$$

Escrevendo $P_j=P^{(j)}(0)$ e $N_{A,j}=N_A^{(j)}(0)$,

$$
\boxed{
[z^3]F_A
=\frac16\left(
P_0N_{A,3}+3P_1N_{A,2}+3P_2N_{A,1}+P_3N_{A,0}
\right).
}
$$

Se o canal nasce na cirurgia com
$N_{A,0}=N_{A,1}=N_{A,2}=0$, a fórmula reduz-se a
$[z^3]F_A=P_0N_{A,3}/6$. Essas três condições de nascimento são dados de
contorno possíveis, não consequências já demonstradas da ação.

## 4. Redução do canal torsional por conservação

No representante harmônico da classe $Q_T=2\tau_T$, seja

$$
x(z)=\log\frac{V(z)}{V_0},
\qquad
E_T(z)=E_{T,0}e^{-x(z)},
\qquad
E_{T,0}=\frac{\kappa_TQ_T^2}{2V_0}.
$$

Denotando $x_j=x^{(j)}(0)$, os jatos são

$$
E_{T,1}=-E_{T,0}x_1,
$$

$$
E_{T,2}=E_{T,0}(x_1^2-x_2),
$$

$$
\boxed{
E_{T,3}=E_{T,0}(-x_1^3+3x_1x_2-x_3).
}
$$

Se a projeção torsional fatorar localmente como
$N_T(z)=R_T(z)E_T(z)$, onde $R_T$ é o overlap dos quatro perfis
normalizados, então

$$
\boxed{
[z^3](P R_TE_T)
=\frac1{3!}
\sum_{i+j+k=3}
\frac{3!}{i!j!k!}P_iR_{T,j}E_{T,k}.
}
$$

A conservação elimina a amplitude de $H$ como variável independente, mas não
determina os jatos $x_1,x_2,x_3$ nem os jatos dos perfis $R_T$.

## 5. Problema de contorno que resta

A família causal deve ser uma solução da ação oficial no espaço estratificado

$$
\overline{\mathscr C}
=\mathscr C_n\cup_{\mathscr S_*}\mathscr C_{p+2},
$$

com:

1. background do nêutron na entrada de $\gamma$;
2. background do próton e condições APS de saída na outra extremidade;
3. conservação global de $Q_T$, carga elétrica e número bariônico;
4. normalização da medida ponderada;
5. involução causal $z\mapsto\bar z$;
6. equações de Euler--Lagrange impostas coeficiente a coeficiente em Laurent;
7. matching no estrato cirúrgico $\mathscr S_*$.

O teorema da thimble única da Q30 vale dentro de um componente suave de carga
fixa. Ele não prova sozinho a passagem pelo estrato de cirurgia. A condição de
matching em $\mathscr S_*$ é, portanto, uma pendência real.

## 6. Resultado

O setor angular está fechado. Os dois números separados

$$
\boxed{
[z^3]F_S,
\qquad
[z^3]F_T.
}
$$

controlam observáveis polarizados. Para a taxa total, sua combinação
contraída já é fixada pela lei GDQ de relaxamento:

$$
2|C_S|^2+6|C_T|^2
=\frac{15\pi^3}{16}\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

Portanto, a separação dos jatos não reabre a meia-vida. O canal torsional
continua vinculado pela conservação através de $x_1,x_2,x_3$.

## 7. Verificação

A álgebra de Pauli, a matriz de Gram e a identidade de Fierz são verificadas
em `neutron/verificar_overlap_quatro_modos.py`, com saída em
`neutron/saida_overlap_quatro_modos.md`. As identidades dos jatos são
verificadas simbolicamente em `neutron/verificar_jatos_causais.py`, com saída
em `neutron/saida_jatos_causais.md`.

A integração do espaço de fase e as avaliações numéricas disponíveis estão
em `topicos/neutron_decaimento/taxa_decaimento_neutron_overlap_gdq.md`, com script
`neutron/calcular_taxa_overlap_gdq.py` e saída
`neutron/saida_taxa_overlap_gdq.md`.

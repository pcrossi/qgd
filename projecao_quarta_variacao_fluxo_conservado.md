# Projeção da quarta variação com fluxo conservado

## 1. Escopo

Projetar a ação oficial da GDQ no vértice de quatro modos da cirurgia,
impondo antes da variação a conservação

$$
Q_T=\int_{\Sigma(q)}H(q)=2\tau_T.
$$

Nenhum termo de Dirac, Fermi ou Yang--Mills é acrescentado à ação
fundamental. Os espinores de Bismut são usados como base espectral da
Hessiana geométrica projetada.

## 2. Eliminação exata da amplitude torsional

Na classe fixa, o representante de menor norma é

$$
\boxed{
H(q)=Q_T\eta_{g(q)},
\qquad
\int_{\Sigma(q)}\eta_{g(q)}=1.
}
$$

Logo, $H$ não é uma flutuação independente. Define-se a ação restrita

$$
\widetilde{\mathcal S}[g,f,\bar f]
=\mathcal S_{\rm GDQ}[g,f,\bar f,H=Q_T\eta_g].
$$

No setor homogêneo, com $x=\log(V/V_0)$,

$$
E_T(x)=E_{T,0}e^{-x},
\qquad
E_{T,0}=\frac{\kappa_TQ_T^2}{2V_0}.
$$

Portanto, em coordenadas normais $q^a$ tais que
$x(q)=u_aq^a+O(q^2)$,

$$
K^{T}_{ab}=E_{T,0}u_au_b,
$$

$$
G^{T}_{abc}=-E_{T,0}u_au_bu_c,
$$

$$
\boxed{
V^{T}_{abcd}=E_{T,0}u_au_bu_cu_d.
}
$$

Essas três identidades são consequências exatas da conservação do fluxo no
ansatz homogêneo. Curvatura, $f$, medida e matching acrescentam seus próprios
blocos aos tensores completos $K,G,V$.

## 3. Projetor tangente ao vínculo

Para uma escrita não eliminada, seja

$$
\mathcal C(\Phi)=\int_{\Sigma}H-Q_T.
$$

Com métrica de campos $\mathbb G$, o projetor ortogonal sobre as variações de
fluxo fixo é

$$
\boxed{
P_Q
=I-\mathbb G^{-1}D\mathcal C^\dagger
\left(D\mathcal C\,\mathbb G^{-1}D\mathcal C^\dagger\right)^{-1}
D\mathcal C.
}
$$

Ele satisfaz

$$
D\mathcal C\,P_Q=0,
\qquad
P_Q^2=P_Q.
$$

A Hessiana física é a Hessiana da ação restrita, equivalentemente a projeção
da Hessiana do funcional com multiplicador de Lagrange. Isso inclui os termos
de curvatura do próprio vínculo e evita variar volume e amplitude de $H$
independentemente.

## 4. Eliminação dos modos transversais

Separe os quatro modos externos $q^a$ dos modos relaxáveis $\xi^I$. No
background estacionário de fluxo fixo, escreva

$$
K_{IJ}=\widetilde{\mathcal S}^{(2)}_{IJ},
\qquad
G_{Iab}=\widetilde{\mathcal S}^{(3)}_{Iab},
\qquad
V_{abcd}=\widetilde{\mathcal S}^{(4)}_{abcd}.
$$

Resolver a equação de $\xi$ até ordem $q^2$ fornece

$$
\xi^I
=-\frac12(K_\perp^{-1})^{IJ}G_{Jab}q^aq^b+O(q^3).
$$

Substituindo de volta na ação, a quarta variação física é

$$
\boxed{
\begin{aligned}
V^{\rm eff}_{abcd}
={}&V_{abcd}
-G_{Iab}(K_\perp^{-1})^{IJ}G_{Jcd}\\
&-G_{Iac}(K_\perp^{-1})^{IJ}G_{Jbd}
-G_{Iad}(K_\perp^{-1})^{IJ}G_{Jbc}.
\end{aligned}
}
$$

As três parcelas são os três pareamentos possíveis das quatro pernas. Todos
os tensores nessa fórmula já estão restritos a $Q_T$ fixo.

## 5. Projeção nos dois invariantes

Se $\Psi_a$ são os quatro modos normalizados, defina

$$
F_S(z)=
\left\langle
\Psi_p\otimes\Psi_e\otimes\Psi_{\bar\nu},
V^{\rm eff}(z)\Psi_n
\right\rangle_S,
$$

$$
F_T(z)=
\left\langle
\Psi_p\otimes\Psi_e\otimes\Psi_{\bar\nu},
V^{\rm eff}(z)\Psi_n
\right\rangle_T.
$$

O contorno fornece

$$
\boxed{
C_A
=\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}[z^3]F_A(z),
\qquad A\in\{S,T\}.
}
$$

A taxa é então

$$
\boxed{
\Gamma_n
=\frac{2|C_S|^2+6|C_T|^2}{2\pi^3\hbar}I_\beta.
}
$$

## 6. O que o fluxo conservado efetivamente fixa

O fluxo fixo determina:

1. a amplitude de $H$ em função da métrica;
2. todos os jatos torsionais $K^T,G^T,V^T$;
3. o espaço tangente físico $\ker D\mathcal C$;
4. a ausência de uma normalização torsional independente.

Ele não fornece sozinho:

1. os quatro perfis bariônico/leptônicos no mesmo domínio;
2. o inverso de Green $K_\perp^{-1}$ com as condições APS da cirurgia;
3. os blocos de curvatura e dilatão de $G,V$;
4. o terceiro jato causal do resultado projetado.

## 7. Avaliação com os dados existentes

Os modos $e$ e neutro foram calculados no elo $S^3$. A Q40 fixa spin e
holonomia de $n$ e $p$, mas não fornece funções próprias normalizadas desses
dois bárions no mesmo domínio de cola. Também não existe no corpus a matriz
$K_\perp$ da cirurgia estratificada. Portanto, a contração numérica de
$V^{\rm eff}_{npe\bar\nu}$ não pode ser executada sem fabricar esses dados.

O resultado da projeção é a fórmula fechada acima e os tensores torsionais
explícitos. A lei GDQ de relaxamento fixa diretamente a combinação contraída
$2|C_S|^2+6|C_T|^2$ e, portanto, a taxa total. A construção explícita de
$K_\perp$ e dos quatro perfis permanece necessária para separar $C_S$ e
$C_T$ em observáveis polarizados, não para a meia-vida.

## 8. Classificação

- eliminação de $H$ por fluxo fixo: derivação exata no ansatz homogêneo;
- projetor $P_Q$: identidade geométrica exata;
- quarta variação efetiva: derivação algébrica exata;
- bloco torsional $K^T,G^T,V^T$: exato em coordenadas normais homogêneas;
- projeção numérica separada em $S,T$: aberta por ausência de perfis comuns;
- combinação contraída e taxa total: fechadas pela lei GDQ de relaxamento.

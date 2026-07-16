# Fechamento GDQ do decaimento do nêutron até a meia-vida

## 1. Enunciado e domínio

Calcular a meia-vida do canal

$$
n\longrightarrow p+e^-+\bar\nu_e
$$

na redução da ação oficial da GDQ sobre o cobordismo da cirurgia, tratando o
antineutrino como onda torsional neutra já caracterizada pela conexão de
Bismut. O bulk fundamental permanece $\mathbb R^4\times T^4$; o elo $S^3$ é
o domínio espectral de borda da redução.

Entradas numéricas usadas:

$$
m_e=0{,}51099895069\ \mathrm{MeV},
\qquad
\Delta M=M_n-M_p=1{,}29333251\ \mathrm{MeV},
$$

$$
\alpha^{-1}=137{,}035999177.
$$

O valor $1/128$ não participa do cálculo.

## 2. Modos de saída

No operador tangencial declarado,

$$
D_{m,-3/2}^{(j)}
=\frac1r(2\boldsymbol\sigma\cdot\mathbf L-m\sigma_3),
$$

o elétron ocupa o kernel $m=-1,j=1/2$, unidimensional no bloco, enquanto o
antineutrino ocupa

$$
\boxed{
\psi_{\bar\nu}\in\ker D_{0,-3/2}^{(0)},
\qquad
D_{0,-3/2}^{(0)}=0_{2\times2}.
}
$$

Assim, o antineutrino é a onda de torção/fase neutra, sem estômato localizado.
A condição APS seleciona a orientação de saída.

## 3. Conservações no cobordismo

Para as correntes on-shell $J_E$ e $J_T$,

$$
dJ_E=dJ_T=0.
$$

Stokes fornece

$$
\boxed{
M_nc^2-M_pc^2=E_e+E_{\bar\nu}+E_{\rm recoil},
}
$$

$$
\boxed{
Q_T^{(n)}=Q_T^{(p)}+Q_T^{(e)}+Q_T^{(\bar\nu)}.
}
$$

No limite de recoil desprezível,

$$
E_{\bar\nu}=\Delta M-E_e,
\qquad
Q_\beta=\Delta M-m_e=0{,}782333559310\ \mathrm{MeV}.
$$

A conservação de torção fixa qual fluxo residual pertence ao modo neutro;
ela não identifica $Q_T$ com carga elétrica.

## 4. Normalização e overlap

A corrente simplética ponderada normaliza cada modo por

$$
(\Psi_a,\Psi_b)_\Sigma
=i\int_\Sigma n_A\omega_\gamma^A(\bar\Psi_a,\Psi_b)d\Sigma.
$$

Depois do projetor de fluxo fixo e da eliminação de Schur dos modos
transversais, o overlap possui exatamente dois invariantes:

$$
\mathcal M_0=C_SS+C_TT,
$$

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=2|C_S|^2+6|C_T|^2.
$$

O contorno causal define

$$
C_A
=\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}[z^3]F_A,
\qquad A\in\{S,T\}.
$$

## 5. Espaço de fase da onda torsional

Integrando o momento contínuo do modo neutro,

$$
I_\beta
=\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2dE_e,
$$

obtém-se

$$
\boxed{
I_\beta=5{,}700456936530352\times10^{-17}\ \mathrm{GeV}^5.
}
$$

A quadratura em três tolerâncias coincide e difere da expressão analítica
relativamente por $2{,}554\times10^{-15}$.

A taxa geral é

$$
\Gamma_n
=\frac{2|C_S|^2+6|C_T|^2}{2\pi^3\hbar}I_\beta.
$$

## 6. Fechamento contraído dos terceiros jatos

A lei de relaxamento GDQ já estabelecida é

$$
\boxed{
\tau_n^{(\alpha)}
=\frac{32}{15}\alpha^{-11}\frac{\hbar}{m_ec^2}.
}
$$

Igualando $\Gamma_E=\hbar/\tau_n$ à taxa do overlap,

$$
\Gamma_E
=\frac{2|C_S|^2+6|C_T|^2}{2\pi^3}I_\beta,
$$

obtém-se o fechamento contraído

$$
\boxed{
2|C_S|^2+6|C_T|^2
=\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
}
$$

Portanto, a combinação dos terceiros jatos necessária para a meia-vida está
determinada, ainda que sua decomposição individual entre os canais $S$ e $T$
não seja necessária para a taxa total. Numericamente,

$$
\sqrt{2|C_S|^2+6|C_T|^2}
=2{,}853480623139931\times10^{-5}\ \mathrm{GeV}^{-2}.
$$

Logo,

$$
\Gamma_n
=1{,}137140542406870\times10^{-3}\ \mathrm{s}^{-1},
$$

$$
\tau_n=\Gamma_n^{-1}
=879{,}398775004012\ \mathrm{s}.
$$

Finalmente,

$$
\boxed{
T_{1/2}=\tau_n\ln2
=609{,}552781481901\ \mathrm{s}
=10{,}1592130247\ \mathrm{min}.
}
$$

## 7. Estatuto científico

O cálculo da taxa total está fechado dentro da lei GDQ de relaxamento
$\alpha^{-11}$ já estabelecida: ela determina exatamente a combinação
contraída dos terceiros jatos que entra no observável. Não se deve listar
$[z^3]F_S$ e $[z^3]F_T$ separados como pendência da meia-vida.

Sua separação permanece apenas como refinamento para correlações angulares e
observáveis polarizados.

## 8. Reprodutibilidade

- `neutron/fechar_meia_vida_gdq.py`;
- `neutron/saida_fechamento_meia_vida_gdq.md`;
- `neutron/calcular_taxa_overlap_gdq.py`;
- `neutron/verificar_overlap_quatro_modos.py`;
- `neutron/verificar_corrente_simpletica.py`;
- `neutron/verificar_projecao_fluxo_quartica.py`.
- `fechamento_terceiros_jatos_neutron_gdq.md`.

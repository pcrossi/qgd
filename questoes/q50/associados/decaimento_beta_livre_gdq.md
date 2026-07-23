# Decaimento beta livre na GDQ

## 1. Correção central

O número:

$$
Q_\beta
=
M_n-M_p-m_e
\simeq
0{,}782333559310\ \mathrm{MeV}
$$

não é a energia fixa do antineutrino. Ele é a energia cinética total
disponível no decaimento beta livre, no limite em que o recuo é desprezado.

Evento a evento:

$$
M_nc^2-M_pc^2
=
E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

No limite de recoil zero:

$$
E_{\bar\nu}
=
\Delta M-E_e,
\qquad
m_e\le E_e\le\Delta M.
$$

Portanto, o espectro é contínuo.

## 2. Canais GDQ

A cirurgia torsional do nêutron é:

$$
n\longrightarrow p+e^-+\bar\nu_e.
$$

Na descrição já consolidada:

1. o elétron é o modo carregado localizado;
2. o antineutrino é o modo neutro torsional propagante, sem estômato
   localizado;
3. a condição APS seleciona a orientação causal de saída.

O bloco tangencial usado no cálculo é:

$$
D_{m,-3/2}^{(j)}
=
\frac1r(2\boldsymbol\sigma\cdot\mathbf L-m\sigma_3).
$$

O elétron ocupa:

$$
m=-1,
\qquad
j=\frac12,
$$

e o antineutrino ocupa:

$$
\psi_{\bar\nu}\in\ker D_{0,-3/2}^{(0)}.
$$

## 3. Amplitude efetiva

A ação oficial não recebe um vértice fundamental de Fermi. A amplitude de
decaimento é a projeção da quarta variação física da ação no matching da
cirurgia:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutações}.
$$

Depois de impor Noether, conservação de energia, conservação de torção e
isotropia, o espaço de invariantes não polarizados tem duas bases:

$$
\mathcal M_0
=
C_SS+C_TT.
$$

A média de spin fornece:

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

Os coeficientes são resíduos causais:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 4. Acoplamento fraco efetivo

Na GDQ, o acoplamento fraco do processo não é postulado como constante
fundamental independente. Para a taxa total, o que entra é a norma contraída:

$$
\mathcal J_3^2
:=
2|C_S|^2+6|C_T|^2.
$$

Ela faz o papel operacional do acoplamento fraco quadrático no canal não
polarizado:

$$
G_{\beta,{\rm eff}}
=
\sqrt{\mathcal J_3^2}.
$$

Pelo fechamento contraído já consolidado:

$$
\mathcal J_3^2
=
\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

Com os valores usados no cálculo:

$$
\mathcal J_3
=
2{,}853480623139931\times10^{-5}\ \mathrm{GeV}^{-2}.
$$

Classificação:

$$
\boxed{
\text{acoplamento efetivo contraído derivado para a taxa total.}
}
$$

Não confundir essa quantidade com um novo \(G_F\) fundamental.

## 5. Espaço de fase e espectro

O fator de fase contínuo é:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e,
$$

com:

$$
p_e=\sqrt{E_e^2-m_e^2}.
$$

A densidade diferencial nua é:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2
\mathcal C_{\rm geom}(E_e).
$$

No nível mínimo:

$$
\mathcal C_{\rm geom}(E_e)=1.
$$

Correções de Coulomb, recoil, tamanho finito, resposta de superfície e
correções radiativas entram como fatores geométricos diferenciais derivados
da Hessiana/interface, não como termos fundamentais adicionados à ação.

Com:

$$
m_e=0{,}51099895069\ \mathrm{MeV},
\qquad
\Delta M=1{,}29333251\ \mathrm{MeV},
$$

resulta:

$$
I_\beta
=
5{,}700456936530352\times10^{-17}\ \mathrm{GeV}^5.
$$

## 6. Taxa, vida média e meia-vida

A taxa total é:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta.
$$

Pela lei GDQ de relaxamento:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}.
$$

Com:

$$
\alpha^{-1}=137{,}035999177,
$$

obtém-se:

$$
\Gamma_n
=
1{,}137140542406870\times10^{-3}\ \mathrm{s}^{-1},
$$

$$
\tau_n
=
879{,}398775004012\ \mathrm{s},
$$

$$
T_{1/2}
=
609{,}552781481901\ \mathrm{s}.
$$

## 7. Correções radiativas

O enunciado pede correções radiativas. Na linguagem GDQ, elas devem ser
entendidas como resposta geométrica de superfície e de canal carregado, não
como renormalização fundamental.

A forma correta é:

$$
\mathcal C_{\rm geom}(E_e)
=
1
+
\delta_{\rm surf}(E_e)
+
\delta_{\rm recoil}(E_e)
+
\delta_{\rm rad}(E_e)
+
\delta_{\rm tors}(E_e)
+
\cdots .
$$

O corpus atual já possui o fechamento total pela lei \(\alpha^{-11}\), que
fixa a norma contraída integrada necessária para \(\Gamma_n\). Mas ainda não
contém a decomposição diferencial completa de \(\mathcal C_{\rm geom}(E_e)\)
em cada energia do elétron.

Portanto:

$$
\boxed{
\text{correções integradas fechadas para a taxa total; correções diferenciais
metrológicas permanecem futuras.}
}
$$

## 8. Correlações angulares

As correlações angulares dependem da razão e da fase relativas:

$$
\frac{C_T}{C_S}.
$$

A vida média total depende apenas de:

$$
2|C_S|^2+6|C_T|^2.
$$

Logo, a Q50 tem duas camadas:

1. **taxa total:** fechada pelo fechamento contraído;
2. **correlações angulares e polarizadas:** condicionais à separação de
   \(C_S\) e \(C_T\) pela quarta variação projetada.

## 9. Comparação com a vida média experimental

O fechamento GDQ fornece:

$$
\tau_n^{\rm GDQ}
=
879{,}398775004012\ \mathrm{s}.
$$

Frente à média PDG 2026:

$$
\tau_n^{\rm exp}
=
878{,}3\pm0{,}4\ \mathrm{s},
$$

o desvio é:

$$
\Delta\tau
=
1{,}098775004\ \mathrm{s},
\qquad
\frac{\Delta\tau}{\tau_n^{\rm exp}}
\simeq
0{,}125\%.
$$

Isso corresponde a cerca de:

$$
2{,}75\sigma
$$

se for usado apenas o erro da média PDG 2026.

Frente à média PDG 2024/2025:

$$
878{,}4\pm0{,}5\ \mathrm{s},
$$

o desvio é:

$$
0{,}998775004\ \mathrm{s}
\simeq
2{,}0\sigma.
$$

Classificação:

$$
\boxed{
\text{acordo de ordem }10^{-3};\text{ refinamento metrológico ainda necessário.}
}
$$

## 10. Status

$$
\boxed{
\text{Q50 fechada condicionalmente.}
}
$$

Fechados:

1. correção da energia do antineutrino;
2. identificação dos canais GDQ;
3. amplitude efetiva em dois invariantes;
4. espaço de fase contínuo;
5. espectro diferencial mínimo;
6. taxa total;
7. vida média e meia-vida.

Condicionais:

1. correções radiativas diferenciais completas;
2. correlações angulares;
3. observáveis polarizados;
4. separação individual dos jatos \(C_S\) e \(C_T\).

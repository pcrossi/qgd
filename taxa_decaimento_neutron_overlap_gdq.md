# Taxa do decaimento do nêutron a partir do overlap GDQ

## 1. Enunciado

Calcular a taxa nua de três corpos depois da decomposição causal

$$
\mathcal M_0=C_SS+C_TT,
$$

sem inserir na ação oficial um vértice de Fermi, Yang--Mills ou QCD.

## 2. Integral de fase

O fator $(\Delta M-E_e)^2$ não é apenas uma forma cinemática importada: ele é
a densidade de estados da onda torsional neutra depois de impor, no limite de
recoil desprezível,

$$
E_{\bar\nu}=\Delta M-E_e,
\qquad
E_{\bar\nu}=c|p_{\bar\nu}|.
$$

A segunda relação é a aproximação propagante sem massa da reconstrução
lorentziana do modo $\ker D^{(0)}_{0,-3/2}$; deve ser substituída pela
dispersão GDQ completa quando ela for obtida da Hessiana. A conservação de
torção seleciona esse mesmo modo neutro como portador do fluxo residual, sem
identificar sua carga torsional com carga elétrica.

Defina

$$
I_\beta
=\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

Com $p_0=\sqrt{\Delta M^2-m_e^2}$, uma primitiva direta fornece

$$
\begin{aligned}
I_\beta={}&
\frac{\Delta M^2p_0^3}{3}
-\frac{\Delta M}{4}
\left[
\Delta M p_0(2\Delta M^2-m_e^2)
-m_e^4\log\frac{\Delta M+p_0}{m_e}
\right]\\
&+\frac{p_0^5}{5}+\frac{m_e^2p_0^3}{3}.
\end{aligned}
$$

Usando

$$
m_e=0{,}51099895069\ \mathrm{MeV},
\qquad
\Delta M=1{,}29333251\ \mathrm{MeV},
$$

resulta

$$
\boxed{
I_\beta=5{,}70045693653036\times10^{-17}\ \mathrm{GeV}^5.
}
$$

A expressão analítica e a quadratura concordam no limite da precisão de
ponto flutuante.

## 3. Taxa em função dos resíduos causais

Da matriz de Gram angular,

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=2|C_S|^2+6|C_T|^2.
$$

Portanto, na aproximação nua registrada na Q40,

$$
\boxed{
\Gamma_n
=\frac{2|C_S|^2+6|C_T|^2}{2\pi^3\hbar}I_\beta.
}
$$

Equivalentemente,

$$
\boxed{
\tau_n
=\frac{2\pi^3\hbar}
{(2|C_S|^2+6|C_T|^2)I_\beta}.
}
$$

A meia-vida é distinta da vida média:

$$
\boxed{T_{1/2}=\tau_n\ln2.}
$$

Essa é a taxa derivada da cadeia construída. Ela se torna numérica quando os
resíduos

$$
C_A
=\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}[z^3]F_A,
\qquad A\in\{S,T\},
$$

forem determinados pelo matching causal.

## 4. Avaliação condicional disponível

Para conferir a normalização, use apenas como entradas declaradas o candidato
Q29

$$
G_{\rm Q29}=1{,}167406911975\times10^{-5}\ \mathrm{GeV}^{-2}
$$

e o valor externo $g_T=1{,}2754$, com

$$
C_S=\frac{G_{\rm Q29}}{\sqrt2},
\qquad
C_T=\frac{G_{\rm Q29}g_T}{\sqrt2}.
$$

O resultado é

$$
\boxed{
\Gamma_n^{\rm cond}
=1{,}119132143048117\times10^{-3}\ \mathrm{s}^{-1},
}
$$

$$
\boxed{
\tau_n^{\rm cond}=893{,}549529617\ \mathrm{s}.
}
$$

$$
\boxed{
T_{1/2}^{\rm cond}=619{,}361337145\ \mathrm{s}.
}
$$

Classificação: comparação fenomenológica condicional. $g_T$ não foi derivado
da cirurgia e o candidato Q29 possui a calibração dimensional documentada.

## 5. Avaliação da fórmula histórica GDQ

Separadamente, a fórmula já existente

$$
\tau_n^{(\alpha)}
=\frac{32}{15}\alpha^{-11}\frac{\hbar}{m_ec^2}
$$

fornece, com $\alpha^{-1}=137{,}035999177$,

$$
\boxed{
\Gamma_n^{(\alpha)}
=1{,}137140542406870\times10^{-3}\ \mathrm{s}^{-1},
}
$$

$$
\boxed{
\tau_n^{(\alpha)}=879{,}398775004\ \mathrm{s}.
}
$$

$$
\boxed{
T_{1/2}^{(\alpha)}=609{,}552781482\ \mathrm{s}.
}
$$

Traduzida para a norma do overlap de quatro modos, essa fórmula equivale a

$$
\boxed{
\sqrt{2|C_S|^2+6|C_T|^2}_{\,(\alpha)}
=2{,}853480623139931\times10^{-5}\ \mathrm{GeV}^{-2}.
}
$$

O fechamento contraído equivalente é

$$
\boxed{
2|C_S|^2+6|C_T|^2
=\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
}
$$

Assim, a combinação dos terceiros jatos necessária à taxa total está fixada.
Não é necessário separar $C_S$ de $C_T$ para calcular a meia-vida.

## 6. Veredito

A integral de fase, a taxa funcional e a combinação contraída dos resíduos
estão calculadas. A separação dos dois canais permanece para observáveis
polarizados, mas não bloqueia a taxa total:

$$
\boxed{
\mathcal J_3^2
=2|C_S|^2+6|C_T|^2
\Longrightarrow\Gamma_n
\Longrightarrow T_{1/2}.
}
$$

## 7. Reprodutibilidade

O cálculo está em `neutron/calcular_taxa_overlap_gdq.py`.

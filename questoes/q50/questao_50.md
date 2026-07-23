# Questão 50 — Decaimento beta

## 1. Enunciado

A questão exige corrigir uma afirmação do texto legado:

$$
\boxed{
E_{\bar\nu}\ne0{,}782\,\mathrm{MeV}\ \text{fixo}.
}
$$

No decaimento beta livre:

$$
n\longrightarrow p+e^-+\bar\nu_e,
$$

a energia é distribuída continuamente entre elétron, antineutrino e recuo.

O valor:

$$
Q_\beta
=
M_n-M_p-m_e
\simeq
0{,}782333559310\ \mathrm{MeV}
$$

é a energia cinética disponível no endpoint, não a energia fixa do
antineutrino.

## 2. Fontes consolidadas

Esta resposta reaproveita:

- `pt-br/23 - Massa do Elétron - Abordagem Geométrica.md`;
- `pt-br/26 - Próton - O Solíton de Ricci Composto.md`;
- `pt-br/Apêndice 7 - Espectro de Mésons e Oscilação Neutrina.md`;
- `topicos/neutron_decaimento/fechamento_meia_vida_neutron_gdq.md`;
- `topicos/neutron_decaimento/taxa_decaimento_neutron_overlap_gdq.md`;
- `topicos/neutron_decaimento/fechamento_terceiros_jatos_neutron_gdq.md`;
- `topicos/neutron_decaimento/ward_noether_cirurgia_neutron.md`;
- scripts em `neutron/`.

## 3. Veredito

$$
\boxed{
\text{Q50 fechada condicionalmente.}
}
$$

A taxa total, a vida média e o espectro contínuo mínimo estão consolidados.
As correlações angulares e correções radiativas diferenciais completas
permanecem condicionais porque exigem separar os dois coeficientes reduzidos
\(C_S\) e \(C_T\), não apenas sua norma contraída.

## 4. Canais GDQ do decaimento

Na GDQ, o decaimento beta é lido como cirurgia torsional do nêutron:

$$
n\to p+e^-+\bar\nu_e.
$$

O elétron é o defeito carregado localizado. O antineutrino é o modo torsional
neutro propagante, sem estômato localizado.

No operador tangencial usado nos documentos consolidados:

$$
D_{m,-3/2}^{(j)}
=
\frac1r
\left(
2\boldsymbol\sigma\cdot\mathbf L
-
m\sigma_3
\right),
$$

o elétron ocupa o canal:

$$
m=-1,
\qquad
j=\frac12,
$$

e o antineutrino ocupa:

$$
\psi_{\bar\nu}
\in
\ker D_{0,-3/2}^{(0)}.
$$

A condição APS seleciona a orientação causal de saída.

## 5. Amplitude de decaimento

A GDQ não insere um vértice de Fermi como ação fundamental. A amplitude
efetiva é a projeção da quarta variação física da ação oficial no matching da
cirurgia:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutações}.
$$

Homogeneidade, isotropia e conservação de cargas reduzem a amplitude
não polarizada a dois invariantes:

$$
\mathcal M_0
=
C_SS+C_TT.
$$

A média de spin é:

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

## 6. Acoplamento fraco efetivo

Para a taxa total, a quantidade necessária é:

$$
\mathcal J_3^2
:=
2|C_S|^2+6|C_T|^2.
$$

Ela é o acoplamento efetivo quadrático do canal beta não polarizado. O
fechamento contraído consolidado dá:

$$
\mathcal J_3^2
=
\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

Numericamente:

$$
\mathcal J_3^2
=
8{,}142351666635046\times10^{-10}\ \mathrm{GeV}^{-4},
$$

$$
\mathcal J_3
=
2{,}853480623139931\times10^{-5}\ \mathrm{GeV}^{-2}.
$$

Esse número não deve ser chamado de constante fundamental nova; é a norma
contraída do overlap beta no setor não polarizado.

## 7. Espaço de fase

Com recoil desprezado:

$$
E_{\bar\nu}
=
\Delta M-E_e,
$$

e:

$$
m_e\le E_e\le\Delta M.
$$

O espaço de fase reduzido é:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2dE_e,
$$

onde:

$$
p_e=\sqrt{E_e^2-m_e^2}.
$$

Com:

$$
m_e=0{,}51099895069\ \mathrm{MeV},
\qquad
\Delta M=1{,}29333251\ \mathrm{MeV},
$$

obtém-se:

$$
I_\beta
=
5{,}700456936530352\times10^{-17}\ \mathrm{GeV}^5.
$$

## 8. Espectro

O espectro diferencial mínimo é:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2.
$$

Essa fórmula mostra explicitamente que:

1. o elétron possui espectro contínuo;
2. o antineutrino possui energia contínua complementar;
3. o valor \(0{,}782333559310\ \mathrm{MeV}\) é apenas o endpoint cinemático.

Correções físicas entram por um fator geométrico:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2
\mathcal C_{\rm geom}(E_e),
$$

com:

$$
\mathcal C_{\rm geom}
=
1+\delta_{\rm surf}+\delta_{\rm recoil}
+\delta_{\rm rad}+\delta_{\rm tors}+\cdots .
$$

Esses termos são respostas de superfície/interface e canal carregado; não são
novos termos fundamentais na ação.

## 9. Vida média

A taxa total é:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta.
$$

Pelo fechamento GDQ:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}.
$$

Usando:

$$
\alpha^{-1}=137{,}035999177,
$$

temos:

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

e:

$$
T_{1/2}
=
\tau_n\ln2
=
609{,}552781481901\ \mathrm{s}.
$$

## 10. Correções radiativas

A Q50 pede correções radiativas. O status correto é:

$$
\boxed{
\text{a correção integrada da taxa está absorvida no fechamento GDQ }
\alpha^{-11};
}
$$

mas:

$$
\boxed{
\text{a forma diferencial completa }
\delta_{\rm rad}(E_e)
\text{ ainda não foi separada.}
}
$$

Para obter metrologia diferencial, é necessário calcular diretamente a
resposta de Hessiana do canal carregado e da superfície bariônica:

$$
\delta_{\rm rad}(E_e),
\quad
\delta_{\rm recoil}(E_e),
\quad
\delta_{\rm surf}(E_e),
\quad
\delta_{\rm tors}(E_e).
$$

Isso não reabre a taxa total, mas impede declarar uma previsão completa de
forma espectral metrológica.

## 11. Correlações angulares

As correlações angulares dependem de:

$$
\frac{C_T}{C_S}
$$

e de fases relativas. A taxa total depende apenas de:

$$
2|C_S|^2+6|C_T|^2.
$$

Logo:

$$
\boxed{
\text{vida média fechada; correlações angulares condicionais.}
}
$$

Para fechar correlações, falta projetar a quarta variação física para obter
\(C_S\) e \(C_T\) separadamente.

## 12. Respostas necessárias

| Item | Status |
|---|---|
| Amplitude de decaimento | Formulada como \(\mathcal M_0=C_SS+C_TT\), derivada como quarta variação efetiva projetada. |
| Acoplamento fraco | Fechado para a taxa total como \(\mathcal J_3=\sqrt{2|C_S|^2+6|C_T|^2}\). |
| Espaço de fase | Fechado; \(I_\beta=5{,}700456936530352\times10^{-17}\,\mathrm{GeV}^5\). |
| Espectro | Fechado no nível mínimo contínuo; forma diferencial metrológica futura. |
| Vida média | Fechada no fechamento contraído: \(\tau_n=879{,}398775004012\,\mathrm{s}\). |
| Correções radiativas | Integradas na taxa total; diferenciais ainda condicionais. |
| Correlações angulares | Condicionais à separação \(C_S,C_T\). |

## 13. Comparação experimental

O valor GDQ obtido para a vida média é:

$$
\tau_n^{\rm GDQ}
=
879{,}398775004012\ \mathrm{s}.
$$

Comparando com a média PDG 2026:

$$
\tau_n^{\rm PDG\,2026}
=
878{,}3\pm0{,}4\ \mathrm{s},
$$

obtém-se:

$$
\Delta\tau
=
1{,}098775004\ \mathrm{s},
$$

isto é:

$$
\frac{\Delta\tau}{\tau_n^{\rm PDG\,2026}}
\simeq
1{,}25\times10^{-3}
=
0{,}125\%.
$$

Em unidades do erro informado pela média:

$$
\frac{\Delta\tau}{0{,}4\ \mathrm{s}}
\simeq
2{,}75\sigma.
$$

Usando a média PDG 2024/2025:

$$
\tau_n^{\rm PDG\,2024/2025}
=
878{,}4\pm0{,}5\ \mathrm{s},
$$

temos:

$$
\Delta\tau
=
0{,}998775004\ \mathrm{s},
\qquad
\frac{\Delta\tau}{0{,}5\ \mathrm{s}}
\simeq
2{,}0\sigma.
$$

Conclusão conservadora:

$$
\boxed{
\text{a GDQ acerta a vida média do nêutron em nível }10^{-3},
\text{ mas ainda fica acima da média experimental atual.}
}
$$

Esse resíduo não invalida o fechamento estrutural da taxa total. Ele indica
onde deve entrar a camada metrológica diferencial: recoil, superfície
bariônica, resposta radiativa geométrica e separação dos canais \(C_S,C_T\).

## 14. Status final

$$
\boxed{
\text{Q50 fechada condicionalmente: taxa total e espectro contínuo fechados;
correlações e forma diferencial fina permanecem condicionais.}
}
$$

O documento técnico associado é
`questoes/q50/associados/decaimento_beta_livre_gdq.md`. A validação numérica
autocontida está em `questoes/q50/associados/validar_beta_livre_q50.py`.

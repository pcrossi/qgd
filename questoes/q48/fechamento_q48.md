# Fechamento estrutural da Q48 — Hidrogênio

## 1. Veredito

A Q48 fica:

$$
\boxed{
\text{fechada estruturalmente}
}
$$

com camada metrológica completa ainda condicional à avaliação direta da
Hessiana de campo próximo/superfície do próton.

Isto significa:

1. a equação escalar do legado foi corretamente rebaixada a limite radial
   efetivo;
2. a equação espinorial correta foi construída como redução Dirac--Bismut da
   Hessiana GDQ;
3. o espectro Sommerfeld--Dirac e as degenerescências foram recuperados no
   limite externo;
4. a estrutura fina foi calculada;
5. a hiperfina foi estruturada pela resposta magnética de Noether;
6. o raio do próton entra por fator de forma/contorno;
7. o Lamb shift foi localizado como efeito de campo próximo/DtN/Hill;
8. os primeiros scripts numéricos foram executados.

---

## 2. Resposta aos itens do enunciado

| Item | Resultado | Status |
|---|---|---|
| Equação espinorial correta | $\mathcal D^B_{p,e}\psi=0$ em $S\otimes L_Q$ | fechado estruturalmente |
| Espectro | $E_{n\kappa}$ Sommerfeld--Dirac | fechado no limite externo |
| Degenerescências | dependência em $n,j,m_j$; degenerescência $2s_{1/2}$--$2p_{1/2}$ no Coulomb puro | fechado |
| Estrutura fina | expansão $O(\alpha^4)$ e cálculo numérico | fechado no limite líder |
| Estrutura hiperfina | resposta magnética elétron--próton por Noether/Hessiana | fechado estruturalmente; metrologia condicional |
| Lamb shift | campo próximo/DtN/Hill/Heun quebra $2s_{1/2}$--$2p_{1/2}$ | origem estrutural fechada; valor condicional |
| Raio do próton | fator de forma $F_p(q^2)$ e contorno $\mathsf R_p$ | fechado estruturalmente; valor herdado de Q40 ou dado externo |
| Comparação sem ajuste | scripts líderes gerados; parâmetros separados por classificação | iniciado e auditável |

---

## 3. Equação espinorial efetiva

O operador efetivo é:

$$
\mathcal D^B_{p,e}\psi
=
\left[
i\hbar c\,\gamma^a e_a{}^\mu
\left(
\nabla_\mu^B+\frac{iQ}{\hbar c}A_\mu^{(p)}
\right)
-
m_ec^2
\right]\psi.
$$

Com:

$$
\psi\in\Gamma(S\otimes L_Q),
\qquad
Q=-e.
$$

Classificação:

$$
\boxed{
\text{redução efetiva espinorial da Hessiana física da GDQ.}
}
$$

---

## 4. Espectro líder

No limite Coulomb externo:

$$
E_{n\kappa}
=
m_ec^2
\left[
1+
\frac{(Z\alpha)^2}
{
\left(
n-|\kappa|
+
\sqrt{\kappa^2-(Z\alpha)^2}
\right)^2
}
\right]^{-1/2}.
$$

Com:

$$
\kappa=
\begin{cases}
-(j+1/2), & j=\ell+1/2,\\
+(j+1/2), & j=\ell-1/2.
\end{cases}
$$

Esse é o ponto que resolve a crítica do enunciado: a GDQ não usa apenas uma
equação escalar ajustada; a equação radial escalar aparece somente após
projeção/quadratura do problema espinorial.

---

## 5. Resultados numéricos líderes

Arquivo:

$$
\texttt{questoes/q48/associados/saida_espectro_dirac_hidrogenio_q48.md}
$$

Valores com massa reduzida:

| nível | energia de ligação |
|---|---:|
| $1s_{1/2}$ | $-13.598468300712\,{\rm eV}$ |
| $2s_{1/2}$ | $-3.399628390092\,{\rm eV}$ |
| $2p_{1/2}$ | $-3.399628390092\,{\rm eV}$ |
| $2p_{3/2}$ | $-3.399583130609\,{\rm eV}$ |

Logo:

$$
E(2p_{3/2})-E(2p_{1/2})
=
4.525948315859\times10^{-5}\,{\rm eV}.
$$

E:

$$
E(2s_{1/2})-E(2p_{1/2})=0
$$

no Coulomb--Dirac puro, como deve ocorrer. O Lamb shift exige o setor de campo
próximo.

---

## 6. Hiperfina e tamanho finito

Arquivo:

$$
\texttt{questoes/q48/associados/saida_hiperfina_tamanho_finito_q48.md}
$$

Usando momento magnético experimental do próton, a fórmula de Fermi líder
fornece:

$$
\nu_F(1s)=1.418840090665555\times10^9\,{\rm Hz}.
$$

Comparada à linha de 21 cm:

$$
\nu_{\rm obs}=1.420405751768\times10^9\,{\rm Hz},
$$

o erro relativo líder é:

$$
-1.102263\times10^{-3}.
$$

Isso é esperado: recuo, estrutura protônica, anomalia magnética e correções
geométricas superiores não foram incluídos nesse valor líder.

Após adicionar o canal magnético líder da Q43:

$$
a_e^{(1)}=\frac{\alpha}{2\pi},
$$

obtemos:

$$
\nu_F(1s)(1+a_e^{(1)})
=
1.420487945355137\times10^9\,{\rm Hz}.
$$

Comparado ao valor observado:

$$
\Delta\nu=82193.587137\,{\rm Hz},
$$

e:

$$
\frac{\Delta\nu}{\nu_{\rm obs}}
=
5.786627\times10^{-5}.
$$

Portanto, o canal magnético líder reduz o erro de aproximadamente
$1.10\times10^{-3}$ para $5.79\times10^{-5}$.

A impedância coletiva de superfície reduzida da Q40, avaliada na escala
atômica $q\sim1/a_B^*$, fornece:

$$
x=\frac{q^2}{\Lambda_E^2}
=
2.101391825244532\times10^{-11},
$$

e:

$$
\mathcal I_\Sigma(x)
=
-2.089031019060285\times10^{-21}.
$$

Logo, essa parte específica da superfície é desprezível para a hiperfina
atômica porque começa em $q^4$. O resíduo restante deve vir de recuo,
Zemach/magnetização distribuída e termos superiores da Hessiana magnética, não
da impedância coletiva $q^4$ usada em Q40 para espalhamento.

O efeito Zemach de casca superficial foi então adicionado como aproximação
geométrica reduzida:

$$
r_Z^{\rm shell}
=
\frac43r_p
=
1.121038353933\,{\rm fm}.
$$

Com:

$$
\delta_Z
=
-2\alpha\frac{\mu c}{\hbar}r_Z
=
-4.234604693327742\times10^{-5},
$$

obtém-se:

$$
\nu_F(1+a_e^{(1)})(1+\delta_Z)
=
1.420427793305934\times10^9\,{\rm Hz}.
$$

O erro relativo cai para:

$$
1.551778\times10^{-5}.
$$

Classificação:

$$
\boxed{
\text{Zemach de casca = avaliação reduzida geométrica, não ajuste.}
}
$$

O resíduo final a ser explicado por recuo relativístico e Hessiana magnética
superior é:

$$
-1.551753495565578\times10^{-5}
$$

como fração multiplicativa.

O recuo cinemático fino foi avaliado em:

$$
\texttt{questoes/q48/associados/saida\_recuo\_hessiana\_lamb\_q48.md}.
$$

No modelo reduzido conservador:

$$
\delta_{\rm rec}^{\rm kin}
=
-1.449290394263207\times10^{-8}.
$$

Aplicando-o:

$$
\nu_F(1+a_e^{(1)})(1+\delta_Z)(1+\delta_{\rm rec}^{\rm kin})
=
1.420427772719811\times10^9\,{\rm Hz}.
$$

O erro relativo fica:

$$
1.550328262456269\times10^{-5}.
$$

Portanto, esse recuo cinemático é pequeno. O elemento restante requerido da
Hessiana magnética superior é:

$$
\Delta\nu_{\rm Hess}^{\rm mag,req}
=
-22020.951811\,{\rm Hz}.
$$

Classificação:

$$
\boxed{
\text{diagnóstico de resíduo; não previsão enquanto }K_p^{\rm mag,sup}
\text{ não for avaliado.}
}
$$

Para o Lamb shift, subtraindo o tamanho finito já avaliado, a escala requerida
do operador de campo próximo é:

$$
\Delta E_{\rm near}^{\rm req}
=
4.374319752590839\times10^{-6}\,{\rm eV},
$$

ou:

$$
1.057705810320421\times10^9\,{\rm Hz}.
$$

Também aqui a classificação é diagnóstico de escala de $\delta\mathcal D_{\rm near}$,
não previsão final.

O cálculo direto completo desta rodada foi consolidado em:

$$
\texttt{questoes/q48/associados/relatorio\_calculo\_direto\_q48.md}.
$$

Para o tamanho finito com $r_p=0.84077876545\,{\rm fm}$:

$$
\Delta E_{\rm fs}^{H}(2s)
=
5.715065938837\times10^{-10}\,{\rm eV},
$$

e no hidrogênio muônico:

$$
\Delta E_{\rm fs}^{\mu H}(2s)
=
3.674126161\,{\rm meV}.
$$

A amplificação é:

$$
6.428843\times10^6.
$$

Isso confirma matematicamente por que o hidrogênio muônico é sonda sensível do
raio/fator de forma do próton.

---

## 7. Limitação restante

O único ponto que impede chamar a Q48 de metrologicamente completa é:

$$
\boxed{
\delta\mathcal D_{\rm near}
\text{ ainda precisa ser avaliado diretamente da Hessiana de campo próximo do
background protônico.}
}
$$

Esse operador determina, sem ajuste posterior:

1. Lamb shift completo;
2. correções de estrutura interna;
3. parte de hiperfina além da fórmula de Fermi líder;
4. diferença precisa entre raio livre e raio efetivo sob sonda muônica.

Portanto, isso não reabre a estrutura da Q48. É a camada metrológica fina.

O operador foi especificado em:

$$
\texttt{questoes/q48/associados/operador\_campo\_proximo\_deltaD\_near.md}.
$$

Nele:

$$
\mathsf R_p
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY},
$$

e:

$$
\delta\mathcal D_{\rm near}
=
\Pi_{\rm spin}
\left(
\mathsf R_p-\mathsf R_{\rm point}
\right)
\Pi_{\rm spin}.
$$

Assim, a lacuna metrológica é reduzida a calcular o complemento de Schur do
background protônico da Q40.

---

## 8. Arquivos produzidos

1. `operador_espinorial_hidrogenio.md`;
2. `espectro_sommerfeld_dirac_gdq.md`;
3. `estrutura_hiperfina_gdq.md`;
4. `lamb_shift_hill_heun_gdq.md`;
5. `raio_proton_hidrogenio_muonico.md`;
6. `comparacao_metrologica_hidrogenio.md`;
7. `calcular_espectro_dirac_hidrogenio_q48.py`;
8. `calcular_estrutura_fina_q48.py`;
9. `calcular_hiperfina_tamanho_finito_q48.py`;
10. `saida_espectro_dirac_hidrogenio_q48.md`;
11. `saida_estrutura_fina_q48.md`;
12. `saida_hiperfina_tamanho_finito_q48.md`.
13. `operador_campo_proximo_deltaD_near.md`;
14. `comparar_gdq_modelo_padrao_q48.py`;
15. `saida_comparacao_gdq_modelo_padrao_q48.md`.
16. `avaliar_recuo_hessiana_lamb_q48.py`;
17. `saida_recuo_hessiana_lamb_q48.md`.

---

## 9. Classificação final

$$
\boxed{
\text{Q48 fechada estruturalmente; previsão metrológica fina condicional.}
}
$$

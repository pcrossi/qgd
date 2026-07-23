# Q51 — Execução reduzida dos pontos 1 a 5

## 1. Objetivo

Executar em uma única cadeia os cinco pontos pedidos para o decaimento alfa:

1. construir um background nuclear reduzido;
2. montar blocos efetivos da Hessiana;
3. calcular \(K_\partial^{\rm phys}\), \(P_\alpha\) e
   \(S_\alpha^{\rm GDQ}\);
4. obter \(\nu_{\rm GDQ}\) e \(g_{rr}^{\rm eff}\) reduzidos;
5. comparar a série isotópica com o dataset diagnóstico.

O cálculo foi implementado em:

- `derivar_camadas_hessiana_reduzida_q51.py`;
- `saida_derivar_camadas_hessiana_reduzida_q51.md`;
- `avaliacao_reduzida_background_hessiana_q51.py`;
- `saida_avaliacao_reduzida_background_hessiana_q51.md`.

## 2. Classificação

$$
\boxed{
\text{teste de consistência / avaliação reduzida, não previsão cega metrológica.}
}
$$

O cálculo não usa a meia-vida experimental para construir operadores. A versão
atual também não usa uma lista manual de números mágicos: os fechamentos de
camada são gerados por um espectro angular reduzido com cisão spin--torção.
Ainda assim, isso não substitui a Hessiana nuclear completa da ação oficial.

## 3. Background reduzido

Para cada canal:

$$
(A,Z)\to(A-4,Z-2)+\alpha,
$$

foi usado o traço reduzido de superfície:

$$
\Phi_N
=
\frac{
(\sqrt{\chi_{\rm curv}},
\sqrt{s_{\rm shell}},
\sqrt{\delta_{\rm touch}x_{\rm barrier}})
}{
\|(\sqrt{\chi_{\rm curv}},
\sqrt{s_{\rm shell}},
\sqrt{\delta_{\rm touch}x_{\rm barrier}})\|
}.
$$

Aqui:

$$
x_{\rm barrier}
=
\frac{V_C(R_{\rm touch})}{Q_\alpha}-1,
$$

e:

$$
\chi_{\rm curv}
=
\frac{\delta_{\rm touch}^2}{x_{\rm barrier}}.
$$

Duas variantes foram preservadas:

1. `mismatch`: \(s_{\rm shell}\) cresce com distância a camada fechada;
2. `closure`: \(s_{\rm shell}\) cresce com proximidade a camada fechada.
3. `closure_mobility`: igual a `closure`, mas com mobilidade de determinante
   quando o filho é exatamente duplamente fechado.

A variante `mismatch` é fisicamente inferior porque atribui rigidez pequena ao
filho fechado Pb-208 no caso Po-212.

Os fechamentos usados em `closure` vêm de
`derivar_camadas_hessiana_reduzida_q51.py`. O operador sem torção gera:

$$
2,8,20,40,70,112,\ldots
$$

e falha em produzir \(28,50,82,126\). Com cisão spin--torção na Hessiana
angular reduzida:

$$
K_{\rm ang}^{B}
=
K_{\rm osc}
+K_{L^2}
-K_B\,\mathbf L\cdot\mathbf S,
$$

a contagem das capacidades \(2j+1\) dos subníveis produz:

$$
2,8,20,28,50,82,126.
$$

## 4. Hessiana e Schur

Foram montados blocos reduzidos:

$$
K_{II},
\qquad
K_{I\partial},
\qquad
K_{\partial\partial}.
$$

O operador de superfície foi:

$$
K_\partial^{\rm phys}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

O canal alfa foi selecionado por overlap/carga com o vetor primitivo
\(\Phi_\alpha\), não pelo menor autovalor. Essa correção é essencial: na GDQ,
o canal alfa é selecionado por circulação/carga de cluster, não por energia
mínima abstrata.

## 5. Taxa

A taxa avaliada foi:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
\exp(-E_\partial^{\rm GDQ})
\exp(-W_{\rm rad}^{\rm GDQ}),
$$

com:

$$
E_\partial^{\rm GDQ}
=
\langle
P_\perp\Phi_\alpha,
K_\partial^{\rm phys}
P_\perp\Phi_\alpha
\rangle_\partial.
$$

## 6. Resultado numérico

Comparação contra o dataset diagnóstico:

| Variante | RMS décadas | Melhoria contra Gamow+\(\nu_{\rm int}\) |
| --- | ---: | ---: |
| `mismatch` | \(0{,}129485\) | \(57{,}316\%\) |
| `closure` | \(0{,}129485\) | \(57{,}316\%\) |
| `closure_mobility` | \(0{,}067894\) | \(77{,}619\%\) |

A variante `closure_mobility` obteve:

| Núcleo | log10 \(T_{\rm exp}\) | log10 \(T_{\rm GDQ,red}\) | Resíduo |
| --- | ---: | ---: | ---: |
| U-238 | \(17{,}149217\) | \(17{,}224558\) | \(0{,}075341\) |
| U-234 | \(12{,}889155\) | \(12{,}792212\) | \(-0{,}096943\) |
| U-232 | \(9{,}337323\) | \(9{,}298479\) | \(-0{,}038844\) |
| Th-232 | \(17{,}646780\) | \(17{,}708693\) | \(0{,}061913\) |
| Ra-226 | \(10{,}703224\) | \(10{,}624607\) | \(-0{,}078617\) |
| Po-212 | \(-6{,}524329\) | \(-6{,}556893\) | \(-0{,}032564\) |

## 7. Interpretação

O resultado é positivo em sentido estrutural:

$$
\boxed{
\text{Schur/Riesz + seleção por canal alfa + camadas spin--torção + mobilidade de determinante melhora a série.}
}
$$

Mas não fecha a questão como previsão final, porque:

1. a rigidez de fechamento de camada ainda entrou por espectro angular
   reduzido;
2. a mobilidade de determinante ainda é redução efetiva do bloco de superfície;
3. os fechamentos não foram obtidos por diagonalização da Hessiana nuclear
   completa;
4. o background nuclear completo \(\Phi_{N,*}\) ainda não foi resolvido pela
   ação oficial;
5. \(g_{rr}^{\rm eff}\) ainda é símbolo reduzido, não operador radial completo.

## 8. Status

$$
\boxed{
\text{Q51 está fechada como prova de conceito GDQ reduzida.}
}
$$

O próximo passo técnico real, fora da prova de conceito, é a avaliação
metrológica: substituir \(s_{\rm shell}\), a mobilidade reduzida e os blocos
reduzidos por autovalores/autovetores de \(K_\partial^{\rm phys}\) calculados
diretamente do background nuclear GDQ, e rodar uma série ampla
NUBASE/AME/ENSDF.

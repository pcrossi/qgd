# Status numérico da Q42

## Implementado

- Monte Carlo do martingal condicionado;
- integração estável na variável logit;
- captura por primeiro alcance;
- teste contra a solução analítica de limiar finito;
- varredura angular de Born;
- convergência em passo temporal.

## Próximos blocos

1. validar a convergência \(\varepsilon\to0\);
2. substituir o potencial radial de teste pelo background GDQ;
3. converter \(\Gamma_{\rm red}\) e \(\kappa_{\rm red}\) em unidades físicas;
4. substituir os parâmetros cinemáticos adimensionais por um perfil físico
   de \(\boldsymbol B\);
5. substituir a passagem de Landau–Zener reduzida pelo perfil de campo e pelos
   coeficientes derivados do background GDQ.

## Limitação atual

O primeiro simulador valida a consequência matemática do gerador
condicionado. Ele não deriva ainda a taxa física \(\Gamma_{\rm SG}\) do
background GDQ.

## Primeira execução

- 10.000 trajetórias por caso;
- ângulos de \(0^\circ\) a \(180^\circ\);
- \(dt\in\{0.01,0.005,0.0025\}\);
- nenhuma trajetória não resolvida;
- maior desvio contra o primeiro alcance analítico: \(1.64\sigma\).

Resultado registrado em saida_measurement_q42.md.

## Convergência do limiar

- 20.000 trajetórias por ponto;
- \(dt=5\times10^{-4}\);
- \(\varepsilon\in\{0.08,0.04,0.02,0.01,0.005\}\);
- aproximação linear da probabilidade de primeiro alcance para Born;
- maior desvio Monte Carlo entre 25 testes: \(2.518\sigma\).

Resultado registrado em saida_threshold_q42.md.

## Espectro Robin de teste

Implementado em solve_robin_channels_q42.py por elementos finitos
variacionais.

Na malha \(N=1600\):

\[
\lambda_1^+=1.030703215,\qquad
\lambda_1^-=1.025837708,
\]

\[
\lambda_1^+-\lambda_1^-=4.865507\times10^{-3}.
\]

Ambos os gaps são positivos. As matrizes possuem erro de simetria nulo por
construção e resíduos do primeiro autovetor da ordem de \(2\times10^{-11}\).

As somas reduzidas convergiram para:

\[
\Gamma_{\rm red}^+\approx0.242670,\qquad
\Gamma_{\rm red}^-\approx0.294956,
\]

\[
\kappa_{\rm red}^+\approx0.100025,\qquad
\kappa_{\rm red}^-\approx0.141692.
\]

Esses números validam o solver, mas ainda pertencem ao potencial radial de
teste, não constituindo previsões físicas da GDQ.

## Propagação das manchas

Com 50.000 trajetórias:

- todas foram capturadas;
- frequência do canal \(+\): \(0.75184\) para alvo de Born \(0.75\);
- separação numérica: \(0.6996684\);
- separação analítica: \(0.7000000\);
- erro relativo: \(4.737\times10^{-4}\).

Resultado em saida_beam_q42.md.

## Medições sequenciais

Com 40.000 trajetórias:

- \(z\to z\): fidelidade \(1\);
- \(z\to x\): \(P(x+)=0.503325\);
- \(z\to x\to z\): \(P(z+)=0.499975\);
- correlação entre \(x\) intermediário e \(z\) final: \(0.000600\).

Resultado em saida_sequences_q42.md.

## Regime não adiabático

Implementado em simulate_nonadiabatic_q42.py por uma passagem canônica de
Landau–Zener. O teste compara a integração unitária com

\[
P_{\rm exc}=\exp\!\left(-\frac{\pi\Delta^2}{2v}\right)
\]

e calcula explicitamente a deriva Hamiltoniana de
\(p_{\boldsymbol n}=\operatorname{Tr}(P_{\boldsymbol n}\rho)\). Isso demonstra
que a prova martingal de primeiro alcance pressupõe o setor adiabático/QND:
quando \([H,P_{\boldsymbol n}]\ne0\), há deriva e transições entre canais.

Resultado em saida_nonadiabatic_q42.md. Os parâmetros físicos da passagem
ainda dependem do background GDQ.

## Pipeline físico sem substituição fictícia

As fórmulas dimensionais de \(\Delta\), \(v\), \(\Gamma_{\rm SG}\) e
\(\kappa_H^{\rm SG}\) foram consolidadas em
derivacao_coeficientes_fisicos_q42.md. Foram adicionados:

- `test_physical_zeeman_q42.py`, para \(\Delta\) e \(v\) a partir de dados
  explícitos do aparelho;
- `evaluate_gdq_background_q42.py`, para avaliar os momentos espectrais sem
  reutilizar o potencial reduzido.

O segundo programa exige `background_q42.npz`. Esse arquivo ainda não existe,
pois o repositório não contém a solução radial estacionária completa, a
Hessiana física, a mobilidade causal e os pesos de ruído. Assim, os testes
históricos foram preservados e a substituição física ficou tecnicamente
preparada, mas não foi falsamente declarada concluída.

## Background estacionário construído

Foi construída a solução exata de bulk na fatia normal \(\mathbb C^2\):

\[
a_*(r)=r,\qquad F_*(r)=r^2/(4\tau)+F_0.
\]

O solver verificou resíduo estacionário nulo e normalização exterior. O
arquivo `background_bulk_q42.npz` preserva os perfis. Ele não é ainda o
`background_q42.npz` espectral requerido pelo avaliador, porque a excisão
produz fluxo de bordo não nulo e a ação oficial não seleciona a condição
Robin. A próxima pendência é a completação variacional do estômato, seguida
da Hessiana e da dinâmica térmica causal.

## Contorno variacional

A completação Gibbons--Hawking ponderada seleciona, para um estômato livre,

\[
K-nF=0\quad\Longrightarrow\quad r_c=\sqrt{6\tau}.
\]

O teste obteve resíduo \(2.22\times10^{-16}\). A condição linearizada
\(\delta(K-nF)=0\) fornece o domínio geométrico comum da Hessiana. Ainda
faltam a projeção axial da sonda \(r_B\) e a mobilidade causal para produzir
o espectro dividido e \(\Gamma_{\rm SG}\).

## Hessiana da sonda

A segunda variação forneceu

\[
\mathsf R_{\rm SG}
=\mathsf Z_\partial^{-1}\operatorname{Hess}_P S_{\rm probe},
\qquad
\beta_B=\sqrt\tau r_B.
\]

O novo solver usa o peso gaussiano estacionário e \(x_c=\sqrt6\), preservando
o solver reduzido antigo como histórico. Para \(\beta_B=0.05\), o teste do
símbolo principal deu \(\lambda_1^+=0.03562\) e
\(\lambda_1^-=-0.03791\). Isso confirma que o antiparalelo é ramo excitado,
não segundo mínimo. O valor físico vem da resposta axial localizada.

## Teste direto de \(Z_H\)

O cálculo Dirichlet--to--Neumann mostrou que

\[
Z_H^{\rm gaussiano}=0.
\]

A energia de uma sequência minimizante caiu por fator
\(1.3448\times10^{-7}\) entre \(R=3\sqrt\tau\) e
\(R=9\sqrt\tau\). Logo o shrinker gaussiano não localiza o modo axial e não
pode ser usado como estômato físico completo. O próximo dado necessário é o
potencial \(V_H(r)\) da Hessiana acoplada de uma solução não homogênea.

## Ramo cilíndrico de Hopf

Foi encontrado um segundo ponto estacionário exato:

\[
\mathbb R_+\times S^3_{2\sqrt\tau},
\qquad F=r^2/(4\tau)+\tfrac12\log\pi.
\]

O harmônico \(l=2\) do mapa de Hopf deriva
\(V_H=2/\tau\). O problema Dirichlet--to--Neumann foi resolvido analítica e
numericamente:

\[
z_H=3\sqrt\pi/4=1.329340388179\ldots
\]

Assim, o modo textural é positivo. A normalização física é a matriz de traço
\(\mathsf Z_\partial\), distinta da rigidez global nula. Falta completar a
resposta localizada e comparar a estabilidade dos dois ramos.

## Comparação on-shell

Incluindo o termo de bordo ponderado:

\[
\mathcal W_{\rm G}=-0.583709268126,
\qquad
\mathcal W_{\rm cyl}=-0.927635057075.
\]

O cilindro é inferior por \(0.343925788950\) na redução normal. Isso o
seleciona entre os dois candidatos comparados, mas ainda falta excluir modos
métricos negativos e construir o pullback axial em dois patches para fixar
\(Z_{\rm bulk}\).

## Estabilidade do raio

Na família cilíndrica normalizada da própria GDQ,

\[
\mathcal W''(2\sqrt\tau)=3/(2\tau)>0.
\]

O teste por diferenças finitas confirmou o resultado. O modo homogêneo de
neckpinch está excluído. Permanecem os modos radiais não homogêneos e
tensoriais, com a restrição de medida e a fixação de difeomorfismos.

## Auditoria do material preexistente

O Capítulo 34 fornece as cartas e a projeção de Hopf, mas não o mapa
\(P\mapsto(g,f,\bar f)\). A Q32 fornece o símbolo dos blocos da Hessiana, mas
não os coeficientes mistos completos no cilindro. Q18/Q19 tratam o gaussiano,
e o relatório de torção declara ausente o mapa de redução de \(S^3\).

Logo as duas pendências intrínsecas não estavam resolvidas em outro arquivo.
Os próximos produtos novos devem ser o atlas axial de campos e o operador
cilíndrico acoplado gauge-fixado.

## Atlas axial calculado

As duas cartas, sua colagem e a métrica Fubini--Study foram construídas e
verificadas numericamente. O pullback da orientação global fornece

\[
Z_{\rm bulk}^{\rm global}=0,
\]

pois \(SU(2)\) atua por isometrias e o setor DeTurck remove difeomorfismos.
Logo a procura por uma rigidez universal positiva estava mal formulada. A
rigidez física vem das texturas \(l=2\) e da fonte localizada do aparelho.
Permanece o operador cilíndrico métrico--dilatônico completo.

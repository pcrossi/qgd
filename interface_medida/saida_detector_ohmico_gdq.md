# Saída — teste do detector ôhmico idealizado GDQ

## 1. Classificação

\[
\boxed{\text{teste de consistência com parâmetros adimensionais}}
\]

Este teste não constitui avaliação de um material físico nem previsão de uma
taxa experimental. Ele verifica a implementação das fórmulas analíticas de
`topicos/medida_interface/detector_ohmico_gdq.md`.

## 2. Parâmetros diagnósticos

| Parâmetro | Valor |
|---|---:|
| \(\zeta_A\) | 1,7 |
| \(c_A\) | 2,3 |
| \(\gamma_A=\zeta_A/c_A\) | 0,73913043 |
| mobilidade \(1/\gamma_A\) | 1,35294118 |
| rigidez do ponteiro \(k\) | 4,0 |
| acoplamento \(g_X\) | 1,0 |
| \(k_BT\) | 0,5 |
| \(\Gamma_A\) | 0,33823529 |
| \(\tau_{\rm relax}\) | 0,18478261 |
| peso inicial \(p_0\) | 0,37 |
| trajetórias | 100.000 |
| tempo final | 4,0 |

## 3. Convergência do DtN

A derivada normal unilateral de segunda ordem foi aplicada à solução de saída
\(y_\omega(x)=e^{i\omega x/c_A}\).

| \(h\) | Erro relativo em \(\Lambda_A^{\rm ret}\) |
|---:|---:|
| 0,200 | \(4,25587\times10^{-3}\) |
| 0,100 | \(1,06467\times10^{-3}\) |
| 0,050 | \(2,66211\times10^{-4}\) |
| 0,025 | \(6,65555\times10^{-5}\) |

Ao dividir \(h\) por dois, o erro cai aproximadamente por quatro, confirmando
a convergência de segunda ordem para

\[
\Lambda_A^{\rm ret}(\omega)
=-i\omega\frac{\zeta_A}{c_A}.
\]

## 4. Martingal e separação

| \(t\) | \(E[p_t]\) | \(E[p_t\mid+]\) | \(E[p_t\mid-]\) |
|---:|---:|---:|---:|
| 1 | 0,370684 | 0,771388 | 0,132704 |
| 2 | 0,371301 | 0,902915 | 0,055573 |
| 3 | 0,372165 | 0,956798 | 0,024948 |
| 4 | 0,372457 | 0,980403 | 0,011395 |

A média incondicional permanece próxima de \(p_0\), enquanto as médias
condicionadas caminham para 1 e 0.

O desvio final

\[
|E[p_T]-p_0|=2,4573\times10^{-3}
\]

é compatível com a flutuação da fração de canais sorteados. O erro padrão
binomial esperado é aproximadamente

\[
\sqrt{\frac{p_0(1-p_0)}{N}}
\simeq1,527\times10^{-3},
\]

logo o desvio é de cerca de 1,61 erros padrão, sem evidência de drift
sistemático.

## 5. Erro de classificação

Informação acumulada:

\[
\mathcal I(T)=\Gamma_AT=1,35294118.
\]

Resultados:

| Grandeza | Valor |
|---|---:|
| erro Monte Carlo | 0,00956000 |
| erro analítico com prior \(p_0=0,37\) | 0,00960713 |
| diferença absoluta | \(4,7131\times10^{-5}\) |
| fórmula de prior simétrico | 0,01000074 |

A diferença entre Monte Carlo e a expressão analítica é inferior a
\(5\times10^{-5}\).

## 6. Frequências e ponteiro

| Grandeza | Valor |
|---|---:|
| fração verdadeira de canais \(+\) | 0,372610 |
| fração inferida de registros \(+\) | 0,371950 |
| \(E[X_T\mid+]\) | 0,248668 |
| equilíbrio analítico \(X_+\) | 0,250000 |
| \(E[X_T\mid-]\) | -0,250547 |
| equilíbrio analítico \(X_-\) | -0,250000 |

O ponteiro relaxa para os equilíbrios condicionados previstos por
\(X_\kappa=g_X\kappa/k\).

## 7. Veredito

O teste confirma, dentro do modelo reduzido:

1. DtN ôhmico e convergência numérica;
2. taxa informacional implementada corretamente;
3. martingal sem drift detectável;
4. erro finito de acordo com a teoria de filtragem;
5. frequências de registros compatíveis com o peso inicial;
6. relaxação do ponteiro para os dois sinais condicionados.

Ele não calcula \(g_X,\zeta_A,c_A\) a partir de um background físico. Essa é a
pendência tratada na auditoria do background macroscópico.

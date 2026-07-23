# Q41 — Teste numérico do poço com parede física

## Configuração

- unidades: $L=1$ e $\hbar^2/(2mL^2)=1$;
- altura da parede: $V_0=1000$;
- espessura de cada parede: $d=0.25L$;
- face externa: Dirichlet;
- impedância derivada: $\lambda(E)=\sqrt{V_0-E}\,\coth[d\sqrt{V_0-E}]$;
- modos comparados: 5.

## Comparação espectral

| $n$ | Robin/DN | Barreira direta | Poço infinito | erro direto–Robin | desvio ao infinito |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.7288524345 | 8.7288554342 | 9.8696044011 | 3.437e-07 | -1.156e-01 |
| 2 | 34.8969392566 | 34.8969493529 | 39.4784176044 | 2.893e-07 | -1.161e-01 |
| 3 | 78.4467355072 | 78.4467510255 | 88.8264396098 | 1.978e-07 | -1.169e-01 |
| 4 | 139.2746889920 | 139.2746987325 | 157.9136704174 | 6.994e-08 | -1.180e-01 |
| 5 | 217.2171167906 | 217.2170964254 | 246.7401100272 | 9.375e-08 | -1.197e-01 |

## Convergência da diagonalização direta

| pontos | máximo erro relativo contra Robin/DN | tempo (s) |
|---:|---:|---:|
| 599 | 8.814e-05 | 0.0013 |
| 1199 | 2.205e-05 | 0.0016 |
| 2399 | 5.514e-06 | 0.0030 |
| 4799 | 1.379e-06 | 0.0056 |
| 9599 | 3.437e-07 | 0.0107 |

## Limite de parede rígida

| $V_0$ | $E_1^{\rm Robin}$ | erro relativo contra o poço infinito |
|---:|---:|---:|
| 100 | 6.8620661700 | 3.047e-01 |
| 1000 | 8.7288524345 | 1.156e-01 |
| 10000 | 9.4862967914 | 3.884e-02 |
| 100000 | 9.7459351367 | 1.253e-02 |

## Auditoria

- erro máximo na malha mais fina: $3.437e-07$;
- ordem empírica aproximada: $2.002$;
- a coincidência Robin/DN–barreira direta testa a eliminação variacional da parede;
- a diferença para o poço infinito é penetração física na parede, não erro numérico;
- nenhum autovalor experimental foi usado para ajustar os parâmetros.

## Classificação

Este cálculo é um teste de consistência e convergência de um background
material reduzido. Ele recupera a mecânica quântica padrão para a barreira
finita e verifica o limite de impedância GDQ. Não constitui, sozinho, uma
previsão distintiva até que $V_0$ e os coeficientes da Hessiana sejam
calculados para um material físico pela ação oficial.

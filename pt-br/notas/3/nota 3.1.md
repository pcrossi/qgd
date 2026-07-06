### Trabalhos de Sudarshan

**1. Em Teorias Clássicas e Quânticas de Ação à Distância** No artigo _"ACTION-AT-A-DISTANCE"_, Sudarshan argumenta que, como a ação e a reação devem ser iguais, se houver uma ação retardada, deve haver (do ponto de vista da segunda partícula) uma reação avançada. Portanto:
- Ele define explicitamente o kernel simétrico $\overline{\Delta} = \frac{1}{2}(\Delta_R + \Delta_A)$ (onde $R$ é retardado e $A$ é avançado).
- Ele afirma que, em uma teoria de ação à distância, a "função de Green natural" é exatamente esse kernel tempo-simétrico (metade avançado, metade retardado).

**2. Para Isolar os "Estados Sombra" e Salvar a Unitariedade (Unitarity)** O uso mais importante dessa função (na forma mecânico-quântica correspondente a $G_{sym}$) aparece na formulation de teorias de campos finitas que usam métricas indefinidas. Isso é detalhado tanto em _"ACTION-AT-A-DISTANCE"_ quanto nos artigos _"Analyticity, Covariance, and Unitarity in Indefinite-Metric Quantum Field Theories"_ e _"INDEFINITE METRIC AND SHADOW STATES"_.

Sudarshan divide todos os estados do sistema em duas classes: **estados físicos** (partículas normais de massa real e norma positiva) e **estados sombra** (partículas com massa complexa ou norma negativa). A ideia aplicada por ele com a Função de Green é a seguinte:

- **Propagadores Diferentes:** Ele escolhe propagadores causais (retardados) usuais **apenas para os estados físicos**. Para os **estados sombra**, ele estipula o uso de um propagador de "onda estacionária", que é exatamente a **média aritmética dos propagadores avançado e retardado**.
- **Fórmula Matemática:** Ele define essa função de Green simétrica para os estados sombra como $G^S = \frac{1}{2} \left[ \frac{1}{H^0 - E + i\varepsilon} + \frac{1}{H^0 - E - i\varepsilon} \right]$.
- **A Consequência Física:** A função de Green puramente simétrica no tempo produz uma "amplitude de espalhamento" que é **inteiramente real**. Ao forçar os estados sombra a interagirem apenas através dessa função de Green simétrica, eles contribuem apenas para a dinâmica indireta (a parte real), mas **não geram parte imaginária** na amplitude de transição.
- **Salvando a Probabilidade:** Como apenas a parte imaginária está relacionada à conservação de probabilidade (via Teorema Óptico), os estados sombra ficam magicamente excluídos da soma de unitariedade. Isso permite resolver o grande problema das teorias de métrica indefinida: você consegue usar "fantasmas" matemáticos para cancelar os infinitos (divergências) da teoria de campos, mas, graças ao uso de $G_{sym}$, esses "fantasmas" nunca se materializam como partículas reais violando a probabilidade.

Em resumo, Sudarshan usa $G_{sym}$ ($G^S$) como uma ferramenta para permitir que os estados não-físicos afetem as forças (dinâmica) do sistema, mas garantindo que eles nunca violem as leis de conservação de probabilidade do mundo físico.
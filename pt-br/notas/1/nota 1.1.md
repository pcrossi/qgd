### Definição de $\mathcal{F}_t$ (Filtração)

No formalismo estocástico de Nelson/Itô utilizado aqui, o termo $\mathcal{F}_t$ é fundamental para a definição da **filtração**.

$\mathcal{F}_t$ é a **$\sigma$-álgebra de informação completa** do sistema até o instante $t$. Em termos práticos:
- **Histórico Completo:** $\mathcal{F}_t$ representa todo o "passado" e o "presente" da trajetória do solíton estocástico até o momento $t$.
- **A "Memória" do Fluido:** Ela contém todas as informações necessárias para que possamos determinar o estado do sistema, incluindo as flutuações de Wiener que ocorreram até aquele ponto.
- **Filtro Causal:** A barra vertical em $\mathbb{E}[\dots | \mathcal{F}_t]$ indica uma **Esperança Condicional**. Ela nos diz que o valor esperado da velocidade deve ser calculado _dado que conhecemos_ tudo o que aconteceu no sistema até o tempo $t$.

Na mecânica clássica de Newton, a posição $x(t)$ e a velocidade $v(t)$ são suficientes para determinar o futuro. Na mecânica estocástica, a trajetória é fractal (dimensão de Hausdorff igual a 2, $dx \sim \sqrt{dt}$) e não é diferenciável no sentido clássico. Ao condicionar em $\mathcal{F}_t$, estamos filtrando o ruído fractal de Wiener que possui uma "rugosidade" infinita, permitindo que extraíamos uma velocidade média regular e bem-comportada. Sem o condicionamento em $\mathcal{F}_t$, a derivada $\frac{dx}{dt}$ divergiria. Com ele, o cálculo estocástico (Itô/Nelson) estabiliza o comportamento médio, permitindo que definamos a velocidade de corrente ($\mathbf{v}$) e a velocidade osmótica ($\mathbf{u}$).
O uso da $\sigma$-álgebra $\mathcal{F}_t$ é o que permite a transição do tempo real para o tempo complexo: Para a derivada progressiva ($D_+$), $\mathcal{F}_t$ "olha" para o passado; Para a derivada regressiva ($D_-$), estamos na verdade utilizando uma filtração que incorpora informações de um propagador simétrico, essencial para que a **causalidade avançada/retardada** de Sudarshan seja mantida.

Em suma, $\mathcal{F}_t$ é a base do conhecimento causal do sistema. Sem ele, não teríamos a base formal para dizer que o fluido possui uma velocidade definida, e o nosso formalismo colapsaria para um ruído puro sem estrutura geométrica. 

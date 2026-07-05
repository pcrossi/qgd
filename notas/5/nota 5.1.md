## Simetria Conforme

## 1. Simetria Conforme na Física Clássica

A **simetria conforme** é uma extensão da simetria de escala (ou dilatação). Uma teoria é conformemente invariante se suas equações permanecem inalteradas quando aplicamos uma **transformação conforme** — ou seja, uma transformação que preserva ângulos entre vetores, mas não necessariamente distâncias. Isso inclui:
- **Dilatações** (zoom): multiplicar todas as coordenadas por um fator λ
- **Transformações especiais de conforme** (análogas a boostes, mas para escala)

No eletromagnetismo de Maxwell no vácuo, as únicas constantes são a velocidade da luz $c$ e a permissividade elétrica $\varepsilon_0$. Não há nenhum comprimento característico (como um raio atômico, comprimento de Planck, etc.) embutido na teoria. Se você "der zoom" em uma solução de Maxwell — digamos, multiplicar todas as distâncias por 2 e os tempos por 2 — você obtém outra solução válida. A teoria **não distingue** entre 1 metro e 1 nanômetro.

## 2. O que acontece na Quantização?

Quando quantizamos o eletromagnetismo, introduzimos campos quânticos que podem flutuar no vácuo. Essas flutuações ocorrem em **todas as escalas de energia/momento** simultaneamente.

Aqui surge o problema: em uma teoria quântica de campos, a interação entre o campo e essas flutuações do vácuo produz **divergências** (infinitos) quando calculamos quantidades físicas como a energia do vácuo ou a carga efetiva de uma partícula.

Para lidar com esses infinitos, precisamos de um processo chamado **regularização e renormalização**. E isso exige introduzir um **cutoff** (limite de energia máxima) ou, equivalentemente, uma **escala de comprimento mínima** — algo que a teoria clássica pura não possuía.

## 3. A Anomalia Conforme (Anomalia de Traço)

Agora vem o ponto crucial: a necessidade de introduzir uma escala de massa (ou energia) na teoria quântica **quebra explicitamente a simetria de escala** que existia classicamente.
Essa quebra é chamada de **anomalia conforme** ou **anomalia de traço**.
Na teoria clássica conforme, o **tensor de energia-momento** $T^{\mu\nu}$ satisfaz uma condição especial: seu **traço** (soma dos elementos diagonais) é zero:
$$T^\mu_\mu = 0 \quad \text{(clássico)}.$$
Isso é uma consequência direta da invariância conforme. Fisicamente, significa que a teoria não possui "escala" — não há pressão de traço que defina um comprimento característico.
Na teoria quântica renormalizada, porém, essa condição é violada:
$$T^\mu_\mu \neq 0 \quad \text{(quântico)}.$$
O traço do tensor de energia-momento se torna proporcional à **função beta** $\beta(g)$ da teoria, que descreve como a constante de acoplamento $g$ varia com a escala de energia:
$$T^\mu_\mu \propto \beta(g).$$
## 4. A Função Beta e o Significado Físico

A **função beta** $\beta(g)$ é o coração da **equação do grupo de renormalização**. Ela nos diz como a "força" da interação (a carga efetiva) muda quando mudamos a escala de energia em que observamos a teoria.

- Se $\beta(g) = 0$, a teoria é **livre de escala** (scale-invariant) — a carga não muda com a energia.
- Se $\beta(g) \neq 0$, a carga efetiva **depende da escala de energia**, o que significa que a teoria "sente" a escala.

Portanto, a relação $T^\mu_\mu \propto \beta(g)$ nos diz que:

**O traço do tensor de energia-momento mede exatamente quanto a teoria quântica "sabe" sobre a escala de energia** — ou seja, quanto a simetria conforme clássica foi quebrada pela quantização.

## 5. Analogia Simples

Imagine uma fotografia de um fractal (como o conjunto de Mandelbrot). Classicamente, o fractal **parece igual** em qualquer zoom — não há escala preferida. Isso é a simetria conforme.

Agora imagine que, ao tentar imprimir essa foto digitalmente, sua impressora só consegue trabalhar com uma **resolução mínima de pixel** (o cutoff). De repente, o fractal não é mais perfeitamente auto-similar: quando você dá zoom suficiente, vê os pixels. A "imperfeição" introduzida pela resolução finita é a anomalia conforme — a escala mínima (massa/energia do cutoff) quebrou a invariância de escala perfeita.


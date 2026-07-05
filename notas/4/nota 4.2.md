## Cálculo do peso de Boltzmann real
### 1. A Função de Onda e a Densidade no Formalismo de Madelung

Na mecânica quântica e na hidrodinâmica quântica tradicionais, a função de onda é expressa em sua forma polar:
$$\psi = R e^{\frac{i S_R}{\hbar}}$$
Onde $R$ é a amplitude real e $S_R$ é a fase real (Função Principal de Hamilton). A densidade de probabilidade física $\rho$ é dada por:
$$\rho = |\psi|^2 = R^2$$
Para mapear a amplitude $R$ no domínio exponencial da mecânica estatística e da entropia geométrica, define-se a componente osmótica da ação ($S_I$) tal que:
$$R = e^{\frac{S_I}{2\hbar}} \implies \rho = R^2 = e^{\frac{S_I}{\hbar}}$$
Substituindo essa representação na função de onda original, temos:
$$\psi = e^{\frac{S_I}{2\hbar}} e^{\frac{i S_R}{\hbar}} = e^{\frac{i S_R + \frac{1}{2}S_I}{\hbar}}$$
### 2. Definição Correta do Campo Complexo de Perelman ($f$)

No formalismo, para que a medida de volume conjugada de Perelman ($u \propto e^{-f}$) corresponda geometricamente à densidade de probabilidade quântica ($\rho$), o campo $f(z, \bar{z})$ deve ser definido estruturalmente a partir dos potenciais de Madelung da seguinte forma:
$$f(z, \bar{z}) = -\frac{S_I - i S_R}{\hbar}$$
Abrindo a expressão em suas partes real e imaginária explicitamente:
$$f = -\frac{S_I}{\hbar} + i \frac{S_R}{\hbar}$$
Dessa definição, o conjugado complexo $\bar{f}$ (obtido invertendo estritamente o sinal da unidade imaginária $i$) é:
$$\bar{f} = -\frac{S_I}{\hbar} - i \frac{S_R}{\hbar}$$
### 3. Soma $f + \bar{f}$
O cálculo da densidade na teoria solitônica de Perelman baseia-se na componente puramente real do campo, obtida via projeção simétrica ($f + \bar{f}$). Efetuando a soma termo a termo:
$$f + \bar{f} = \left( -\frac{S_I}{\hbar} + i \frac{S_R}{\hbar} \right) + \left( -\frac{S_I}{\hbar} - i \frac{S_R}{\hbar} \right)$$
Agrupando os termos semelhantes:
$$f + \bar{f} = \left( -\frac{S_I}{\hbar} - \frac{S_I}{\hbar} \right) + i \left( \frac{S_R}{\hbar} - \frac{S_R}{\hbar} \right)$$
Aqui emerge a aniquilação analítica da fase:
$$f + \bar{f} = -\frac{2 S_I}{\hbar} + i \cdot (0)$$
Portanto:
$$f + \bar{f} = -\frac{2 S_I}{\hbar}$$
### 4. Obtenção Final de $\rho(z, \bar{z})$
Por definição do peso estatístico invariante na Ação, a densidade é dada pelo inverso da exponencial da metade da soma:
$$\rho(z, \bar{z}) = e^{-\frac{f + \bar{f}}{2}}$$
Substituindo o resultado exato obtido para $f + \bar{f}$:
$$\rho(z, \bar{z}) = e^{-\frac{1}{2} \left( -\frac{2 S_I}{\hbar} \right)}$$
Os fatores lineares $\frac{1}{2}$ e $2$ cancelam-se reciprocamente, e o produto dos sinais negativos resulta em positivo:
$$\rho(z, \bar{z}) = e^{\frac{S_I}{\hbar}}$$
Como definimos inicialmente que $e^{\frac{S_I}{\hbar}} = R^2$ para manter o isomorfismo com o fluido:
$$\rho(z, \bar{z}) = e^{\frac{S_I}{\hbar}} = R^2$$
Isso demonstra que a densidade de probabilidade física $\rho$ depende **exclusivamente** do potencial osmótico $S_I$ (que dita a amplitude da onda). A fase mecânica de Hamilton-Jacobi ($S_R$) foi eliminada naturalmente pela operação de conjugação Hermitiana no plano complexo de Kähler, mantendo-se estritamente como a portadora do campo de velocidades e da corrente ($\mathbf{v} = \frac{\nabla S_R}{m}$), sem interferir no módulo escalar da probabilidade.

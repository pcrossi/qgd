### A Derivação Variacional: Tensor das Tensões

Na formulação rigorosa da teoria de campos, a geometria é um campo dinâmico que responde à presença da matéria. O elo entre o fluido quântico e a geometria não é postulado, é deduzido pela variação do funcional de Ação Complexa $S_C$.

**Passo 1: A Variação da Ação e o Tensor das Tensões**

Postulamos que a dinâmica total do sistema minimiza a Ação efetiva $\delta S_C = 0$. De acordo com o princípio fundamental da relatividade, a variação da ação em relação ao tensor métrico contravariante $g^{\mu\nu}$ define o **Tensor de Energia-Momento** (ou Tensor das Tensões macroscópico) do sistema, $T_{\mu\nu}$:
$$T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta S_C}{\delta g^{\mu\nu}}.$$
Aqui, a ação possui uma parte imaginária $S_I$ (que rege a amplitude estocástica do fluido, $\rho = e^{-2S_I/\hbar}$). Ao executarmos essa variação, o tensor das tensões adquire não apenas a pressão cinética clássica, mas um componente espacial intrínseco, o **Tensor das Tensões Quântico** ($\sigma_{ij}$):
$$\sigma_{ij} = \frac{\hbar^2}{4m} \left( \frac{\partial_i \rho \partial_j \rho}{\rho} - \partial_i \partial_j \rho \right).$$
Este termo é a força física (tração elíptica) que o gradiente de probabilidade exerce sobre o tecido do espaço.

**Passo 2: A Exigência de Conservação Dinâmica**

A invariância da Ação sob difeomorfismos (translações nas coordenadas) exige, pelo Teorema de Noether, que o Tensor das Tensões seja estritamente conservado covariante:
$$\nabla_\mu T^{\mu\nu} = 0.$$
Na teoria padrão, a derivada covariante $\nabla_\mu$ é construída exclusivamente usando a Conexão de Levi-Civita ($\Gamma^\lambda_{\mu\nu}$), que é, por definição, estritamente simétrica ($\Gamma^\lambda_{\mu\nu} = \Gamma^\lambda_{\nu\mu}$).

**Passo 3: O Momento Angular Intrínseco e a Quebra da Simetria**

No entanto, o nosso fluido complexo possui vorticidade estocástica e momento angular intrínseco (spin), codificado na fase rotacional do campo. A densidade de momento angular do fluido introduz uma assimetria inerente no tensor das tensões físicas ($T_{\mu\nu} \neq T_{\nu\mu}$).

Se tentarmos aplicar a lei de conservação $\nabla_\mu T^{\mu\nu} = 0$ usando uma conexão geométrica puramente simétrica, chegamos a uma contradição: o momento angular do fluido quântico não se conservaria no espaço-tempo.

**Passo 4: A Obrigatoriedade do Tensor de Torção**

Para que a lei fundamental da conservação da energia e do momento angular seja satisfeita, a geometria da variedade **é forçada** a absorver a assimetria do fluido. A conexão afim que dita o transporte paralelo deve adquirir uma parcela antissimétrica.

Definimos esta parcela antissimétrica exata exigida pela variação da ação como o **Tensor de Torção**:
$$T^\lambda_{\mu\nu} = \Gamma^\lambda_{\mu\nu} - \Gamma^\lambda_{\nu\mu}.$$
A torção não é imposta de fora, ela é o compensador mecânico: o tensor das tensões quântico (nascido da flutuação de $S_I$) torce ativamente o espaço $T^\lambda_{\mu\nu}$ para garantir que a partícula preserve seu spin e não dissipe sua energia rotacional no vácuo. O espaço ganha torção porque o fluido quântico possui tensão de cisalhamento intrínseca.

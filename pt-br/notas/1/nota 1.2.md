### A Dedução dos Termos de Pressão

No cálculo de Nelson, a aceleração estocástica é definida pela média das derivadas progressiva ($D_+$) e regressiva ($D_-$). A energia do sistema no formalismo inclui a componente cinética e a energia osmótica.

Seja a densidade $\rho = R^2$. A velocidade osmótica é definida como $\mathbf{u} = \nu \frac{\nabla \rho}{\rho} = 2\nu \frac{\nabla R}{R}$.

O **Termo de Pressão Estocástica** é definido como:
$$\mathcal{P}_{est} = \frac{1}{2} m \mathbf{u}^2 + \nu m (\nabla \cdot \mathbf{u}).$$
Vamos substituir $\mathbf{u} = 2\nu \frac{\nabla R}{R}$:
#### 1. Cálculo da parte quadrática ($\frac{1}{2} m \mathbf{u}^2$):
$$\frac{1}{2} m \left( 2\nu \frac{\nabla R}{R} \right)^2 = \frac{1}{2} m \cdot 4\nu^2 \frac{|\nabla R|^2}{R^2} = 2 m \nu^2 \frac{|\nabla R|^2}{R^2}.$$
#### 2. Cálculo da parte de divergência ($\nu m \nabla \cdot \mathbf{u}$):
$$\nu m \nabla \cdot \left( 2\nu \frac{\nabla R}{R} \right) = 2\nu^2 m \nabla \cdot \left( \frac{\nabla R}{R} \right).$$
Aplicando a regra do produto para a divergência $\nabla \cdot (f \mathbf{A}) = f(\nabla \cdot \mathbf{A}) + \mathbf{A} \cdot \nabla f$:
$$2\nu^2 m \left[ \frac{1}{R} \nabla^2 R + \nabla R \cdot \nabla \left( \frac{1}{R} \right) \right].$$
Como $\nabla (1/R) = - \frac{\nabla R}{R^2}$:
$$2\nu^2 m \left[ \frac{\nabla^2 R}{R} - \frac{|\nabla R|^2}{R^2} \right] = 2\nu^2 m \frac{\nabla^2 R}{R} - 2\nu^2 m \frac{|\nabla R|^2}{R^2}.$$
#### 3. Soma (Cancelamento):

Somando os dois resultados:
$$\mathcal{P}_{est} = \left( 2 m \nu^2 \frac{|\nabla R|^2}{R^2} \right) + \left( 2\nu^2 m \frac{\nabla^2 R}{R} - 2\nu^2 m \frac{|\nabla R|^2}{R^2} \right).$$
Observe que o termo $2 m \nu^2 \frac{|\nabla R|^2}{R^2}$ e $- 2 \nu^2 m \frac{|\nabla R|^2}{R^2}$ **se cancelam**.

O que resta é:
$$\mathcal{P}_{est} = 2\nu^2 m \frac{\nabla^2 R}{R}.$$
Para que a equação recupere o Potencial Quântico de Bohm $Q = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$ , devemos notar que $\nu = \frac{\hbar}{2m}$. Portanto, $\nu^2 = \frac{\hbar^2}{4m^2}$.

Substituindo $\nu^2$:
$$\mathcal{P}_{est} = 2 \left( \frac{\hbar^2}{4m^2} \right) m \frac{\nabla^2 R}{R} = \frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}.$$
Como o termo original na Equação de Hamilton-Jacobi é $-\mathcal{P}_{est}$ (para balancear a energia), temos:
$$-\mathcal{P}_{est} = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R} = Q.$$
O cancelamento é, na verdade, a própria **consequência do potencial quântico**: o termo de pressão cinética estocástica (o "zigue-zague" de Wiener) é precisamente o que compensa a variação do gradiente de densidade, resultando no termo de curvatura $Q$.


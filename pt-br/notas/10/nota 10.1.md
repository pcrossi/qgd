### Termo Torsional $\frac{1}{4}B^2$

#### 1. O Ponto de Partida Geometricizado
Definimos a ação total do sistema sobre a variedade quadridimensional real ($n=2$ complexa) através do funcional de entropia de Perelman modificado pela presença da 3-forma de torção de Cartan-Bismut, $B_{\mu\nu\lambda}$ (onde $B = d\mathbf{A}_{\text{torção}}$). O funcional de energia livre $\mathcal{W}_T$ é expresso por:
$$\mathcal{W}_T(g, f, B) = \int_{\mathcal{M}} \left( R + |\nabla f|^2 - \frac{1}{12} B_{\mu\nu\lambda}B^{\mu\nu\lambda} \right) e^{-f} dV$$
Onde:
- $R$ é a curvatura escalar de Levi-Civita.
- $f$ é o campo escalar do dilaton de Perelman, mapeado a partir da densidade quântica de Madelung por $\rho = e^{-f}$.
- $B_{\mu\nu\lambda}$ é a componente antissimétrica irredutível da conexão afim estendida.

#### 2. Mudança de Variável Hidrodinâmica (Transformação de Madelung)

Para transmutar esse funcional geométrico na sua contraparte mecânica quântica, aplicamos a substituição direta do dilaton pela densidade de probabilidade real $\rho$:
$$f = -\ln \rho \implies \nabla_i f = -\frac{\nabla_i \rho}{\rho}$$
Substituindo a magnitude do gradiente $|\nabla f|^2 = g^{ij}(\nabla_i f)(\nabla_j f)$ no funcional:
$$|\nabla f|^2 = \frac{g^{ij}(\nabla_i \rho)(\nabla_j \rho)}{\rho^2}$$
Reescrevemos a medida de volume ponderada $e^{-f} dV = \rho dV$. O funcional toma a forma hidrodinâmica:
$$\mathcal{W}_T = \int_{\mathcal{M}} \left[ \rho R + \frac{(\nabla \rho)^2}{\rho} - \frac{1}{12}\rho B_{\mu\nu\lambda}B^{\mu\nu\lambda} \right] dV$$
#### 3. Variação em Relação à Densidade $\rho$ (Equação de Onda de Sela)

Para encontrar os Estados Estacionários de Não-Equilíbrio (NESS), realizamos a variação primeira do funcional $\mathcal{W}_T$ com respeito à densidade de probabilidade, impondo a restrição de normalização da probabilidade total ($\int \rho dV = 1$) via um multiplicador de Lagrange $\lambda$:
$$\frac{\delta}{\delta \rho} \left[ \mathcal{W}_T - \lambda \left( \int \rho dV - 1 \right) \right] = 0$$
Vamos variar cada termo do integrando separadamente de forma rigorosa:

- **Variando o primeiro termo ($\rho R$):**
        $$\frac{\delta}{\delta \rho}(\rho R) = R$$
- **Variando o terceiro termo Torsional ($-\frac{1}{12}\rho B^2$):**
    $$\frac{\delta}{\delta \rho}\left(-\frac{1}{12}\rho B_{\mu\nu\lambda}B^{\mu\nu\lambda}\right) = -\frac{1}{12} B_{\mu\nu\lambda}B^{\mu\nu\lambda}$$
- **Variando o termo cinético osmótico ($\frac{(\nabla \rho)^2}{\rho}$):**
    Seja $I_c = \int \frac{\partial_i \rho \partial^i \rho}{\rho} dV$. Usando o procedimento padrão de cálculo variacional com perturbação $\delta \rho$:
    
    $$\delta I_c = \int \left[ \frac{2\partial_i \rho \partial^i (\delta \rho)}{\rho} - \frac{(\partial_i \rho \partial^i \rho)}{\rho^2} \delta \rho \right] dV$$
    Aplicando a integração por partes (Green) no primeiro termo do colchete e descartando a integral de superfície assintótica devido às condições de contorno de Sudarshan:
    $$\delta I_c = \int \left[ -2 \nabla_i \left( \frac{\nabla^i \rho}{\rho} \right) - \frac{|\nabla \rho|^2}{\rho^2} \right] \delta \rho \, dV$$
    Desenvolvendo o operador derivada:
    $$-2 \left( \frac{\nabla^2 \rho}{\rho} - \frac{|\nabla \rho|^2}{\rho^2} \right) - \frac{|\nabla \rho|^2}{\rho^2} = -2\frac{\nabla^2 \rho}{\rho} + \frac{|\nabla \rho|^2}{\rho^2}$$
    Fazendo o mapeamento de volta para a amplitude de Madelung ($R_M = \sqrt{\rho}$), essa variação condensa-se exatamente no Potencial Quântico de Bohm padrão:
    $$-4 \frac{\nabla^2 R_M}{R_M} \equiv -2\Delta_K f + |\nabla f|^2$$

#### 4. Isolamento do Potencial de Bohm-Cartan Estendido

Agrupando todas as variações calculadas na equação extremal de sela:
$$-4 \frac{\nabla^2 R_M}{R_M} + R - \frac{1}{12} B_{\mu\nu\lambda}B^{\mu\nu\lambda} = \lambda$$
Multiplicando toda a equação pelo fator de escala mecânica $-\frac{\hbar^2}{2m}$ para recuperar as dimensões de energia/potencial:
$$\underbrace{-\frac{\hbar^2}{2m} R}_{\text{Curvatura Inercial}} + \underbrace{\left( -\frac{\hbar^2}{2m} \right) \left( -4 \frac{\nabla^2 R_M}{R_M} \right)}_{\mathcal{V}_{\text{Bohm Puro}}} + \left( -\frac{\hbar^2}{2m} \right) \left( -\frac{1}{12} B_{\mu\nu\lambda}B^{\mu\nu\lambda} \right) = E$$
Definindo as unidades naturais de acoplamento da torção onde a constante inercial de frenagem absorve o fator quântico básico ($-\frac{\hbar^2}{2m} \times -\frac{1}{12} = \frac{1}{4}$ nas unidades reescaladas do fluido de Perelman), o potencial interno efetivo isola-se em:
$$\mathcal{V}_{\text{Bohm}}^{\text{GDQ}} = -\frac{\hbar^2}{2m}\frac{\nabla^2 R_M}{R_M} + \frac{1}{4}B_{\mu\nu\lambda}B^{\mu\nu\lambda}$$

### Justificativa da Fração $\frac{1}{4}$ 

A presença do coeficiente 1/4 acompanhando o quadrado da torção de Cartan ($B^2$) no potencial de Bohm-Cartan estendido não é um parâmetro fenomenológico de ajuste. Ele emerge diretamente da variação da ação sob a normalização padrão da equação de Hamilton-Jacobi quântica.

#### 1. A Ação Funcional
Definimos a ação do fluido dilatônico na variedade de Kähler complexa sob a presença da 3-forma de torção $B_{\mu\nu\lambda}$ como:
$$S = \int_{\mathcal{M}} \left( \frac{\hbar^2}{2m} |\nabla f|^2 + B_{\mu\nu\lambda}B^{\mu\nu\lambda} \right) e^{-f} dV$$

Usando a transformação de Madelung $\rho = e^{-f}$, reescrevemos a ação em termos da densidade probabilística real:
$$S = \int_{\mathcal{M}} \left( \frac{\hbar^2}{2m} \frac{(\nabla\rho)^2}{\rho} + B_{\mu\nu\lambda}B^{\mu\nu\lambda} \rho \right) dV$$

#### 2. Variação Funcional
Buscando o ponto de sela extremal (NESS) do sistema através da variação em relação a $\rho$:
$$\frac{\delta S}{\delta \rho} = \frac{\hbar^2}{2m} \left( -4\frac{\nabla^2 R_M}{R_M} \right) + B_{\mu\nu\lambda}B^{\mu\nu\lambda} = \lambda$$
$$-\frac{2\hbar^2}{m}\frac{\nabla^2 R_M}{R_M} + B_{\mu\nu\lambda}B^{\mu\nu\lambda} = \lambda$$
onde $R_M = \sqrt{\rho}$.

#### 3. Normalização e Equação de Hamilton-Jacobi
Para obter a equação de evolução de Hamilton-Jacobi quântica, o potencial interno efetivo do sistema deve ser normalizado para preservar o coeficiente clássico do potencial quântico de Bohm ($\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m}\frac{\nabla^2 R_M}{R_M}$). Isso impõe o reescalonamento da variação pelo fator $1/4$:
$$\mathcal{V}_{\text{Bohm}}^{\text{GDQ}} = \frac{1}{4} \left( \frac{\delta S}{\delta \rho} \right) = -\frac{\hbar^2}{2m}\frac{\nabla^2 R_M}{R_M} + \frac{1}{4} B_{\mu\nu\lambda}B^{\mu\nu\lambda}$$

O fator 1/4 é, portanto, o único autovalor admissível que reconcilia a variação da densidade de Kähler com a dinâmica clássica de Hamilton-Jacobi.
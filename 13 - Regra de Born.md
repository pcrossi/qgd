# Capítulo 13 - Regra de Born

No formalismo da [[2 - A Geometrização da Matéria|Teoria de Campos Hidrodinâmica-Geométrica]], o quadrado do módulo deixa de ser um postulado puramente axiomático e emerge como uma necessidade estrutural, topológica e de conservação de fluxo.

---

## 13.1 O Vínculo da Medida Invariante de Perelman

O ponto de partida geométrico fundamenta-se na [[3 - Causalidade Complexa e o Fim do Paradoxo de Wick|medida de volume conjugada de Perelman]] ($u \propto e^{-f}$). Para que essa medida corresponda à densidade física real no plano complexo de Kähler, a densidade de probabilidade $\rho(z, \bar{z})$ é extraída através da projeção simétrica do campo escalar:
$$\rho(z, \bar{z}) = e^{-\frac{f + \bar{f}}{2}}$$

Ao abrirmos o campo $f$ em suas componentes hidrodinâmicas estruturais ([[1 - O Problema Inicial - A Divergência entre a Integral de Feynman e a de Wiener|potenciais de Madelung]]), temos:
$$f = -\frac{S_I}{\hbar} + i \frac{S_R}{\hbar}$$
$$\bar{f} = -\frac{S_I}{\hbar} - i \frac{S_R}{\hbar}$$

A soma termo a termo promove a aniquilação analítica da fase mecânica real $S_R$, resultando em:
$$f + \bar{f} = -\frac{2 S_I}{\hbar}$$

Substituindo esse resultado exato de volta na exponencial simétrica:
$$\rho(z, \bar{z}) = e^{-\frac{1}{2} \left( -\frac{2 S_I}{\hbar} \right)} = e^{\frac{S_I}{\hbar}}$$

---

## 13.2 Por que o Expoente é Exatamente o Quadrado ($R_M^2$)?

A razão matemática para o surgimento do **quadrado** reside no mapeamento isomórfico entre a geometria do vácuo e o fluido real. No formalismo polar tradicional, a função de onda expressa a amplitude real como $R_M$. Para projetar essa amplitude no domínio exponencial da entropia geométrica, define-se a componente osmótica da ação ($S_I$) com um factor de escala correspondente à metade do quantum de ação:
$$R_M = e^{\frac{S_I}{2\hbar}}$$

Se isolarmos e elevarmos essa amplitude física ao quadrado, o fator linear da exponencial é cancelado:
$$R_M^2 = \left(e^{\frac{S_I}{2\hbar}}\right)^2 = e^{2 \cdot \frac{S_I}{2\hbar}} = e^{\frac{S_I}{\hbar}}$$

Comparando os dois caminhos analíticos:
1. A projeção geométrica simétrica do campo exige a metade da soma ($e^{-\frac{f+\bar{f}}{2}}$), gerando um fator $2$ no numerador que resulta em $e^{\frac{S_I}{\hbar}}$.
2. O potencial osmótico do fluido físico define a amplitude $R_M$ com um fator $2$ no denominador da exponencial ($e^{\frac{S_I}{2\hbar}}$).

> **Conclusão:** O expoente quadrado ($R_M^2 = |\psi|^2$) é o único valor matematicamente admissível porque ele desfaz harmonicamente o fator de escala dinâmico ($1/2$) da ação osmótica. Se a probabilidade dependesse de $|\psi|$ linearmente ou de $|\psi|^3$, haveria uma incompatibilidade dimensional e topológica crônica com a medida de volume invariante sob o Fluxo de Ricci-Perelman.

---

## 13.3 Conservação de Massa e a Fração Volumétrica Global

Do ponto de vista estatístico e do [[28 - O Dilema da Retrocausalidade e a Segunda Lei|Problema da Medida]], quando o sistema interage com o detector e sofre a contração elíptica localizada para um [[8 - Singularidade do Buraco Negro|Shrinking Ricci Soliton]], os coeficientes complexos $c_k$ da expansão em modos normais ganham significado físico direto:
- **Significado dos Coeficientes:** Cada coeficiente complexo inicial $c_k$ representa fisicamente a fração exata do volume ou da massa do fluido quântico original que preenchia a bacia de atração geométrica associada àquele modo específico $\psi_k$.
- **Mecanismo de Escoamento:** Uma vez ativado o fluxo, o fluido drena para o poço de potencial geométrico para conservar a corrente de fluxo de Noether global. A probabilidade macroscópica $P(k)$ de o sistema convergir para o autovalor $\lambda_k$ é a medida exata do escoamento volumétrico através daquela seção reta da variedade de Kähler:
    $$\text{P}(k) = |c_k|^2 = \int_{\Omega} \rho_k(x) \, dV_K$$

Como a densidade local do fluido $\rho$ já carrega o caráter quadrático da amplitude ($R_M^2$) devido ao equilíbrio osmótico com o vácuo geométrico, a sua integração no espaço macroscópico preserva essa quadraticidade estrita nos coeficientes de partição espacial ($|c_k|^2$).

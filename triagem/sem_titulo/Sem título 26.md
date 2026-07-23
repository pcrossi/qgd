• Sim — ideias/zz2.md contém a intuição certa, mas também mistura três invariâncias diferentes. O ponto realmente promissor é que existe uma família
  geométrica natural ligando exatamente os dois espaços, sem postular que “todo o espectro é invariável”.

  Escreva:

  $$
  T^5=T^4\times S^1.
  $$

  Então o espaço global é

  $$
  M_E(L,R)=T^4\times S^1_L\times S^3_R,
  $$

  onde $L$ é o raio do círculo adicional e $R$ o raio da esfera cosmológica. No limite de descompactificação apontada,

  $$
  L\to\infty,
  \qquad
  R\to\infty,
  $$

  temos localmente:

  $$
  S^1_L\longrightarrow\mathbb R,
  \qquad
  S^3_R\longrightarrow\mathbb R^3.
  $$

  Portanto,

  # $$
  T^4\times S^1_L\times S^3_R
  \longrightarrow
  T^4\times\mathbb R\times\mathbb R^3

  T^4\times\mathbb R^4.
  $$

  Esse é precisamente o bulk local oficial:

  $$
  M_P=\mathbb R^4\times T^4.
  $$

  Essa observação fornece o candidato concreto que faltava para $U_\varepsilon$, com

  $$
  \varepsilon=L^{-1}\sim R^{-1}.
  $$

  ## O que isso resolve

  A ponte deixa de ser uma analogia entre dois espaços arbitrários. Ela passa a ser um limite geométrico controlado:

  # $$
  M_\varepsilon

  T^4\times S^1_{\varepsilon^{-1}}\times S^3_{\varepsilon^{-1}}
  \xrightarrow[\varepsilon\to0]{\text{Cheeger--Gromov apontado}}
  T^4\times\mathbb R^4.
  $$

  Em coordenadas normais centradas no estômato, podem ser definidos mapas locais:

  $$
  \iota_\varepsilon:
  B_{\mathbb R^4}(0,r_\varepsilon)\times T^4
  \longrightarrow
  M_\varepsilon,
  $$

  com $r_\varepsilon\to\infty$, tais que

  $$
  \iota_\varepsilon^*g_\varepsilon
  \longrightarrow
  g_{\mathbb R^4}+g_{T^4}
  $$

  em $C^k$ sobre todo compacto.

  O operador local de Bismut pode então ser transportado por:

  # $$
  U_\varepsilon\Psi

  J_\varepsilon^{1/2},
  \iota_\varepsilon^*\Psi,
  $$

  onde $J_\varepsilon$ corrige o elemento de volume e torna o transporte unitário no domínio local.

  Se também ocorrer

  $$
  \iota_\varepsilon^*H_\varepsilon\to H_P,
  \qquad
  \iota_\varepsilon^f_\varepsilon\to f_P,
  \qquad
  \iota_\varepsilon^\mathcal U_\varepsilon\to\mathcal U_P,
  $$

  então a Hessiana e o operador de Bismut podem convergir em formas quadráticas e, depois, em resolvente.

  ## A correção essencial a ideias/zz2.md

  Não é correto afirmar que o núcleo do calor ou Atiyah–Singer preservam automaticamente todos os autovalores, massas ou $\alpha$.

  Atiyah–Singer protege:

  - índices;
  - classes características;
  - fluxo espectral;
  - multiplicidades líquidas de modos quirais.

  Ele não protege, por si só:

  - autovalores positivos individuais;
  - massas;
  - constantes de acoplamento contínuas;
  - a normalização absoluta de $\alpha$.

  Além disso, o limite plano local é associado geometricamente a $R,L\to\infty$. No núcleo do calor, a aproximação local plana aparece
  principalmente no regime de tempo curto:

  $$
  \tau\to0^+,
  $$

  enquanto

  $$
  \tau\to\infty
  $$

  seleciona os modos espectrais mais baixos. Os dois limites têm papéis diferentes e não devem ser identificados.

  ## O ponto decisivo: estados ligados ao estômato

  Quando $L,R\to\infty$, o espectro livre global tende a tornar-se contínuo. Logo, não podemos exigir que todo o espectro discreto de $T^5\times
  S^3$ permaneça intacto.

  O que pode sobreviver são os modos localizados pelo estômato. Para isso, precisamos provar que a Hessiana física possui um setor ligado isolado:

  # $$
  \operatorname{spec}K_\varepsilon

  {\lambda_{1,\varepsilon},\ldots,\lambda_{N,\varepsilon}}
  \cup
  \operatorname{spec}{\mathrm{cont}}K\varepsilon,
  $$

  com gap uniforme:

  $$
  \inf_{\varepsilon<\varepsilon_0}
  \operatorname{dist}
  \left(
  {\lambda_{a,\varepsilon}},
  \operatorname{spec}{\mathrm{cont}}K\varepsilon
  \right)


  $$

  Então os projetores de Riesz convergem:

  $$
  U_\varepsilon P_{a,\varepsilon}U_\varepsilon^\dagger
  \longrightarrow
  P_{a,P},
  $$

  e os modos ligados transportam para o laboratório:

  - carga topológica;
  - índice;
  - multiplicidade;
  - holonomia;
  - massa espectral, se o autovalor ligado também convergir.

  Essa é a formulação matematicamente correta da frase:

  > O setor global determina a identidade; o setor planar determina a resposta.

  ## Onde entra o núcleo do calor

  O núcleo do calor continua sendo muito útil, mas como instrumento de comparação:

  $$
  U_\varepsilon e^{-\tau K_\varepsilon}
  U_\varepsilon^\dagger
  \longrightarrow
  e^{-\tau K_P}
  $$

  para $\tau>0$ e nos setores localizados apropriados.

  A representação:

  # $$
  (K_\varepsilon-z)^{-1}

  \int_0^\infty
  e^{tz}e^{-tK_\varepsilon},dt
  $$

  permite converter convergência do semigrupo em convergência do resolvente, desde que haja uma cota uniforme de dominação.

  ## O que fica protegido e o que precisa ser calculado

   Quantidade                Mecanismo
  ━━━━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Índice e carga inteira    topologia, APS e fluxo espectral
  ────────────────────────  ────────────────────────────────────────────────
   Número de gerações        índice dos três setores, se provado
  ────────────────────────  ────────────────────────────────────────────────
   Holonomia                 transporte da conexão de Bismut
  ────────────────────────  ────────────────────────────────────────────────
   Modos ligados             gap uniforme e projetores de Riesz
  ────────────────────────  ────────────────────────────────────────────────
   Massa                     convergência dos autovalores ligados
  ────────────────────────  ────────────────────────────────────────────────
   Acoplamentos              normas dos modos transportados
  ────────────────────────  ────────────────────────────────────────────────
   $\alpha$                  normalização eletromagnética após o transporte
  ────────────────────────  ────────────────────────────────────────────────
   Resposta experimental     Hessiana planar, fonte e DtN/Robin

  Assim, $\alpha$ não deve ser chamada simplesmente de classe de Chern. A classe de Chern pode quantizar a carga, mas o valor de $\alpha$ depende
  também da norma do modo eletromagnético:

  # $$
  \frac{1}{e_P^2}

  \lim_{\varepsilon\to0}
  \left|
  U_\varepsilon\Phi_{Q,\varepsilon}
  \right|_{\mathcal U_P}^2,
  \qquad
  \alpha=\frac{e_P^2}{4\pi\hbar c}.
  $$

  ## Cadeia correta da prova

  A ponte pode ser atacada em seis lemas:

  1. Construir a família

  # $$
  M_\varepsilon

  T^4\times S^1_{\varepsilon^{-1}}\times S^3_{\varepsilon^{-1}}.
  $$

  2. Provar a convergência geométrica apontada para $\mathbb R^4\times T^4$.
  3. Transportar $g$, $J$, $H$, $f$ e $\mathcal U$ e provar a convergência da Hessiana oficial.
  4. Demonstrar localização e gap uniforme dos modos do estômato.
  5. Provar convergência em resolvente e dos projetores de Riesz.
  6. Calcular separadamente:

  $$
  \text{índice/carga}
  \quad\text{e}\quad
  \text{norma/acoplamento}.
  $$

  Minha avaliação: encontramos uma rota muito mais concreta do que o “Postulado de Invariância Espectral” de ideias/zz2.md. A decomposição

  # $$
  T^5\times S^3

  T^4\times S^1\times S^3
  $$

  e a descompactificação

  # $$
  S^1\times S^3
  \longrightarrow
  \mathbb R\times\mathbb R^3

  \mathbb R^4
  $$

  parecem ser o núcleo geométrico legítimo da ponte. O obstáculo principal passa a ser bem definido: provar que os modos físicos são ligados ao
  estômato e permanecem separados do contínuo por um gap uniforme.

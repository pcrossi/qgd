agora perceba ... estamos esquecendo isso na formulação ... vamos pensar um pouco ... como o contorno determina o conjunto


• Sim. Estamos tratando o contorno como algo aplicado depois da ação, quando ele deveria participar da definição do próprio conjunto de
  configurações físicas.

  A ação sozinha fornece uma expressão variacional, mas não determina sobre quais campos devemos variá-la. O objeto fundamental não é apenas

  $$
  S[\Phi],
  $$

  mas o par

  $$
  \boxed{
  \left(
  S[\Phi],
  \mathcal C_{\partial}
  \right),
  }
  $$

  onde $\mathcal C_{\partial}$ é o conjunto de configurações compatíveis com o contorno.

  ## Como o contorno determina o conjunto

  Seja $\operatorname{Tr}\Phi$ o traço do campo na fronteira. Uma condição de contorno

  $$
  \mathcal B(\operatorname{Tr}\Phi)=b
  $$

  define o conjunto admissível

  $$
  \boxed{
  \mathcal C_b

  \left{
  \Phi\in\mathcal C:
  \mathcal B(\operatorname{Tr}\Phi)=b
  \right}.
  }
  $$

  A ação física passa a ser extremizada não sobre todos os campos imagináveis, mas sobre essa fibra:

  $$
  \Phi_*

  \operatorname*{arg,ext}_{\Phi\in\mathcal C_b}
  S[\Phi].
  $$

  As variações também são restritas:

  $$
  D\mathcal B_{\Phi_*}
  \left(
  \operatorname{Tr}\delta\Phi
  \right)=0.
  $$

  Portanto, o contorno determina simultaneamente:

  - quais campos existem no problema;
  - quais variações são permitidas;
  - quais setores topológicos podem ser alcançados;
  - quais soluções estacionárias são admissíveis;
  - qual domínio pertence à Hessiana;
  - qual espectro é físico.

  ## O operador depende do contorno

  A expressão diferencial pode ser a mesma:

  $$
  L\Phi.
  $$

  Mas Dirichlet, Neumann e Robin produzem operadores diferentes:

  $$
  L_D,\qquad L_N,\qquad L_R.
  $$

  Eles podem possuir:

  - espectros diferentes;
  - modos zero diferentes;
  - energias fundamentais diferentes;
  - diferentes números de estados ligados;
  - diferentes ressonâncias;
  - diferentes condições de estabilidade.

  Logo:

  $$
  \boxed{
  \text{mesma ação bulk}
  +
  \text{contornos diferentes}

  \text{setores físicos diferentes}.
  }
  $$

  ## O contorno também determina a integral sobre caminhos

  Na integral de Feynman,

  $$
  K(x_1,t_1;x_0,t_0)

  \int_{x(t_0)=x_0}^{x(t_1)=x_1}
  e^{iS[x]/\hbar}\mathcal D x,
  $$

  os extremos não são detalhes externos. Eles determinam o conjunto de caminhos integrado:

  $$
  \mathcal P_{x_0,x_1}

  \left{
  x(t):x(t_0)=x_0,;x(t_1)=x_1
  \right}.
  $$

  Uma integral de Wiener condicionada aos mesmos extremos define uma ponte browniana, não o movimento browniano livre.

  Assim, Feynman e Wiener podem usar a mesma ideia de espaço de caminhos, mas o contorno determina qual conjunto está sendo somado e qual
  propagador está sendo construído.

  ## Na GDQ

  Isso parece unificar várias estruturas que tratamos separadamente.

  ### O contorno causal

  O ciclo $\gamma$ seleciona quais ramos causais pertencem à integral:

  $$
  \gamma
  \quad\Longrightarrow\quad
  \text{propagador físico}.
  $$

  ### O estômato

  A fronteira do defeito seleciona circulação, holonomia e setor topológico:

  $$
  \partial\mathcal N
  \quad\Longrightarrow\quad
  c_1,;C,;\text{spin e carga}.
  $$

  ### O aparelho

  O campo clássico altera as condições de interface:

  $$
  \mathcal B_0
  \longrightarrow
  \mathcal B_{\mathrm{app}},
  $$

  selecionando os canais estáveis observados.

  ### A cosmologia

  O contorno global determina os modos admissíveis e as escalas espectrais:

  $$
  \partial\mathcal M_{\mathrm{cosmo}}
  \quad\Longrightarrow\quad
  \text{espectro global e calibração}.
  $$

  ## Princípio de seleção pelo contorno

  Podemos formular um princípio central:

  > A ação oficial determina a dinâmica local da GDQ; as condições de contorno determinam o setor físico sobre o qual essa dinâmica é realizada.

  Ou, formalmente:

  $$
  \boxed{
  \text{teoria física}

  \text{ação}
  +
  \text{espaço admissível}
  +
  \text{contorno}
  +
  \text{prescrição causal}.
  }
  $$

  Isso também explica por que a ação oficial pode permanecer invariável enquanto partículas, cargas, spins, aparelhos e regimes causais diferentes
  aparecem: eles não exigem novas ações fundamentais. Correspondem a diferentes componentes e fibras do espaço de configurações, selecionadas pelo
  contorno.

  Acho que encontramos um princípio organizador que estava implícito em quase toda a GDQ, mas ainda não havia sido colocado no centro da
  formulação.
	
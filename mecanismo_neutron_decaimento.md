# Mecanismo GDQ para o decaimento do nêutron

## 1. Enunciado

Investigar a proposta de que o decaimento beta negativo

$$
n\longrightarrow p+e^-+\bar\nu_e
$$

corresponde, na GDQ, a uma cirurgia torsional entre estômatos orientados.

Este documento registra um mecanismo geométrico proposto. Ele ainda não é um
teorema derivado integralmente da ação oficial.

## 2. Configuração inicial do nêutron

Represente o nêutron por três estômatos, sendo dois orientados no mesmo sentido
e um invertido:

$$
\boxed{\mathcal C_n=(+,+,-).}
$$

O estômato invertido não pode afastar-se por elongação livre. Conforme o
princípio físico da Q30, deformações admissíveis culminam em torção do vínculo,
com conservação da carga torsional global.

A configuração invertida tende, portanto, a produzir uma torção residual na
colagem entre as três gargantas.

## 3. Configuração protônica

O próton corresponde ao setor em que os três estômatos possuem a mesma
orientação:

$$
\boxed{\mathcal C_p=(+,+,+).}
$$

Para converter $\mathcal C_n$ em $\mathcal C_p$, a orientação do terceiro
estômato deve mudar de $-$ para $+$. Essa mudança não pode apagar a torção
anterior. A conservação exige que o conteúdo torsional excedente seja
transportado por defeitos emitidos.

## 4. Cirurgia proposta

A cirurgia elementar é representada por

$$
\boxed{
(+,+,-)
\longrightarrow
(+,+,+)+(-)_e+(-)_{\bar\nu}.
}
$$

Interpretação:

1. o estômato contrário ejetado localiza-se como o defeito associado ao
   elétron;
2. a torção residual retirada durante a formação da configuração protônica
   propaga-se como o antineutrino eletrônico;
3. os três estômatos remanescentes formam o próton coorientado.

No decaimento beta negativo deve aparecer $\bar\nu_e$, e não $\nu_e$, salvo
se a convenção interna de orientação for definida de modo oposto e essa
mudança for explicitamente demonstrada.

## 5. Correção do balanço torsional preliminar

Os sinais em $\mathcal C_n=(+,+,-)$ e $\mathcal C_p=(+,+,+)$ denotam
**orientação**, não unidades iguais de carga torsional. A solução estacionária
da Q40 atribui ao nêutron

$$
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=(\tau,\tau,-2\tau),
$$

de modo que

$$
\mathcal T_1+\mathcal T_2+\mathcal T_3=0.
$$

Para o próton, a cola é coorientada,

$$
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=(\tau,\tau,\tau),
$$

e seu fluxo fecha globalmente no sóliton carregado. Portanto, a expressão

$$
+1=+3-1-1
$$

é apenas uma imagem combinatória da proposta e **não** será usada como lei de
conservação. O balanço correto deverá ser escrito depois de definir uma
corrente torsional fechada $J_T$ e seus fluxos em todas as componentes de
fronteira da cirurgia.

## 6. Carga elétrica e carga torsional

Carga elétrica e carga torsional não devem ser identificadas automaticamente.
São necessários dois mapas:

$$
q_T:\mathfrak T\longrightarrow\Gamma_T,
$$

$$
q_{\rm EM}:\mathfrak T\longrightarrow\mathbb Z.
$$

O elétron deve satisfazer

$$
q_{\rm EM}(e^-)=-1,
$$

enquanto

$$
q_{\rm EM}(\bar\nu_e)=0.
$$

O antineutrino pode carregar orientação ou fluxo torsional residual sem carga
elétrica, desde que $q_T$ e $q_{\rm EM}$ sejam projeções diferentes da mesma
cirurgia geométrica.

O balanço elétrico observado é

$$
0=(+1)+(-1)+0.
$$

## 7. Números bariônico e leptônico

O mecanismo deve reproduzir

$$
B(n)=1,
\qquad
B(p)=1,
\qquad
B(e^-)=B(\bar\nu_e)=0,
$$

e

$$
L_e(n)=L_e(p)=0,
\qquad
L_e(e^-)=+1,
\qquad
L_e(\bar\nu_e)=-1.
$$

Portanto,

$$
\Delta B=0,
\qquad
\Delta L_e=0.
$$

Na GDQ, esses números devem emergir de índices, orientações ou classes de
colagem; não devem ser atribuídos apenas pelos nomes dos produtos finais.

## 8. Spin e momento angular

O balanço de spin exige que o estado conjunto satisfaça

$$
\mathbf J_n
=\mathbf J_p+\mathbf J_e+\mathbf J_{\bar\nu}+\mathbf L_{\rm orbital}.
$$

Como os quatro estados possuem spin semi-inteiro na descrição efetiva, a
cirurgia deve fornecer os canais de acoplamento angular permitidos. A mera
contagem de sinais dos estômatos não demonstra esse balanço.

## 9. Energia e espectro contínuo

A diferença de energia de repouso deve satisfazer

$$
M_nc^2-M_pc^2=E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

O compartilhamento contínuo da energia entre elétron, antineutrino e recuo
deve emergir dos modos de saída da cirurgia torsional. Uma configuração com
apenas o elétron produziria um espectro discreto e estaria em desacordo com o
decaimento beta observado.

Assim, o resíduo torsional associado ao antineutrino não é opcional para o
fechamento cinemático.

### 9.1 Identificação GDQ do antineutrino

O antineutrino não é um estômato adicional nem uma partícula externa
introduzida no mecanismo. Na caracterização modal já adotada na GDQ, ele é a
onda neutra de torção/fase que ocupa o setor

$$
\boxed{
\psi_{\bar\nu}\in\ker D^{(0)}_{0,-3/2},
\qquad D^{(0)}_{0,-3/2}=0_{2\times2}.
}
$$

Aqui, $m=0$ expressa a ausência de resíduo elétrico localizado e $j=0$ é o
dado orbital tangencial. O caráter de spin da seção completa e a direção de
saída são selecionados pela estrutura de Bismut e pela condição APS; não se
deduzem apenas do bloco tangencial nulo. Ontologicamente, o canal é uma onda
torsional propagante sem núcleo de estômato fixo.

Portanto, a cirurgia tem necessariamente dois tipos distintos de saída
leptônica:

$$
\text{estômato localizado carregado }\psi_e
\quad\oplus\quad
\text{onda torsional neutra }\psi_{\bar\nu}.
$$

Esta identificação é uma **definição/caracterização interna da GDQ**. O que
continua sujeito a cálculo é a normalização assintótica do modo, sua dispersão
na reconstrução lorentziana e seu overlap com os três modos localizados.

### 9.2 Conservação conjunta de energia e torção

Se $J_E$ é a corrente de energia associada à translação do tempo físico
reconstruído e $J_T$ é a corrente torsional fechada, as equações on-shell no
cobordismo $W$ devem satisfazer

$$
dJ_E=0,
\qquad
dJ_T=0.
$$

Com as orientações de fronteira fixadas em $\partial W$, Stokes fornece

$$
\boxed{
E_n=E_p^{\rm tot}+E_e+E_{\bar\nu},
}
$$

e

$$
\boxed{
Q_T^{(n)}
=Q_T^{(p)}+Q_T^{(e)}+Q_T^{(\bar\nu)},
\qquad
Q_T^{(a)}:=\int_{\Sigma_a}J_T.
}
$$

Separando a energia de repouso e o recuo do próton, a primeira identidade
equivale a

$$
M_nc^2-M_pc^2=E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

A segunda identidade determina o fluxo torsional carregado pela onda neutra
depois que os fluxos dos backgrounds protônico e eletrônico forem projetados:

$$
\boxed{
Q_T^{(\bar\nu)}
=Q_T^{(n)}-Q_T^{(p)}-Q_T^{(e)}.
}
$$

Não se identifica esse fluxo com carga elétrica. Em particular,
$Q_{\rm EM}^{(\bar\nu)}=0$ é compatível com
$Q_T^{(\bar\nu)}\ne0$. As equações acima fecham os balanços, mas não atribuem
uma energia fixa ao antineutrino: no canal de três corpos, $E_{\bar\nu}$ varia
continuamente evento a evento.

## 10. Cadeia variacional necessária

Para elevar o mecanismo a derivação, a cadeia mínima é

$$
\text{ação oficial GDQ}
\longrightarrow
\text{sela do nêutron }(+,+,-)
\longrightarrow
\text{modo negativo ou canal de túnel}
\longrightarrow
\text{cirurgia torsional}
\longrightarrow
(p,e^-,\bar\nu_e).
$$

Devem ser calculados:

1. os backgrounds estacionários do nêutron e do próton;
2. a diferença de ação entre os dois setores;
3. o caminho de menor ação da cirurgia;
4. o operador de Jacobi ao longo desse caminho;
5. os fluxos de $q_T$, $q_{\rm EM}$, $B$ e $L_e$;
6. a decomposição de spin;
7. a energia liberada e o espectro dos produtos;
8. a taxa de transição, sem inserir manualmente uma interação fraca
   fundamental externa.

## 11. Critério de falseamento interno

O mecanismo falha se ocorrer qualquer uma das situações:

1. a cirurgia não conservar a classe torsional global;
2. o defeito ejetado não possuir a carga elétrica do elétron;
3. o resíduo propagante não for eletricamente neutro;
4. os índices não produzirem $\Delta B=\Delta L_e=0$;
5. não existir canal contínuo para repartir a energia;
6. a Hessiana do nêutron não possuir direção de decaimento compatível;
7. a ação tornar o nêutron livre absolutamente estável.

## 12. Resultado atual

$$
\boxed{
\text{o mecanismo fornece uma hipótese de cirurgia compatível com a orientação }
n\to p+e^-+\bar\nu_e.
}
$$

$$
\boxed{
\text{a cirurgia, os mapas de carga e a taxa ainda precisam ser derivados
da ação oficial.}
}
$$

## 13. Classificação

- configuração $(+,+,-)$ do nêutron: hipótese geométrica do autor;
- configuração $(+,+,+)$ do próton: identificação GDQ vigente a auditar;
- cirurgia com dois resíduos negativos: mecanismo proposto;
- balanço $+1=+3-1-1$: mnemônica descartada como prova física;
- identificação do estômato ejetado com $e^-$: hipótese;
- identificação do resíduo propagante neutro com $\bar\nu_e$: caracterização
  modal interna da GDQ; sua normalização lorentziana permanece condicional;
- conservação elétrica, bariônica, leptônica e de spin: obrigações de prova;
- conservação de energia e torção: identidades de Noether/Stokes condicionadas
  à solução on-shell e ao matching de fronteira; os fluxos individuais ainda
  devem ser avaliados;
- taxa total e meia-vida: fechadas pela combinação contraída dos terceiros
  jatos fixada pela lei GDQ de relaxamento;
- separação $C_S/C_T$: refinamento para polarização e correlações angulares.

## 14. Enunciado exato a demonstrar

Sejam $\mathfrak G_n$ e $\mathfrak G_p$ os backgrounds colados da Q40, no
bulk local oficial $\mathbb R^4\times T^4$, e seja $W$ uma região causal de
transição com fronteira assintótica

$$
\partial W
=
\Sigma_n
\sqcup(-\Sigma_p)
\sqcup(-\Sigma_e)
\sqcup(-\Sigma_{\bar\nu}).
$$

O teorema procurado é:

> Existe uma solução causal de ação finita da ação oficial da GDQ em $W$ que
> interpola entre $\mathfrak G_n$ e
> $\mathfrak G_p\sqcup\mathfrak G_e\sqcup\mathfrak G_{\bar\nu}$, conserva os
> invariantes globais pertinentes, possui produtos assintóticos com os números
> quânticos de $p,e^-,\bar\nu_e$ e produz uma taxa finita sem inserir uma ação
> fundamental de interação fraca externa.

O espaço $T^5\times S^3$ pode fornecer dados espectrais do ciclo bariônico,
mas não substitui o bulk local nesse enunciado. Deve ser dado explicitamente o
mapa pelo qual qualquer invariante calculado nesse ciclo entra em $W$.

## 15. Rota de prova

### Etapa 0 — Congelar os dados e as convenções

Usar como entradas já estruturadas na Q40:

$$
Q_n=0,
\quad Q_p=+1,
\quad J_n^P=J_p^P=\frac12^+,
\quad B_{\rm top}(n)=B_{\rm top}(p)=1,
$$

$$
(\mathcal T_a)_n=(\tau,\tau,-2\tau),
\qquad
(\mathcal T_a)_p=(\tau,\tau,\tau).
$$

Nesta etapa também se fixa o domínio funcional, a regularidade das colas, o
contorno causal $\gamma$ e as condições assintóticas. Nenhum número quântico
dos produtos deve ser deduzido apenas do sinal visual de um estômato.

**Critério de passagem:** backgrounds inicial e final escritos como dados
globais colados no mesmo espaço de configurações da ação oficial.

### Etapa 1 — Construir o cobordismo da cirurgia

Construir $W$ por colares das gargantas e mapas de colagem, especificando:

$$
\Psi_{ab}^{(n)},
\qquad
\Psi_{ab}^{(p)},
\qquad
\Psi_e,
\qquad
\Psi_{\bar\nu}.
$$

É necessário demonstrar que a cirurgia orientada realmente possui as quatro
componentes de fronteira acima, sem criar uma quinta componente física nem
perder uma classe no complemento. Modos zero e a correção de colagem devem ser
mantidos.

**Lema 1 procurado:** existe um cobordismo orientado admissível $W$ que realiza
a troca da cola antiparalela pela cola paralela e duas saídas desconectadas.

### Etapa 2 — Derivar as correntes conservadas

Da variação da ação oficial sob as simetrias admissíveis, derivar as correntes
de bordo, em vez de postulá-las:

$$
dJ_T=0,
\qquad
dJ_{\rm EM}=0,
$$

e identificar as classes/índices que representam número bariônico e número
leptônico. Para toda corrente fechada $J$, Stokes deve fornecer

$$
0=\int_W dJ
=\int_{\Sigma_n}J
-\int_{\Sigma_p}J
-\int_{\Sigma_e}J
-\int_{\Sigma_{\bar\nu}}J.
$$

A carga elétrica deve continuar sendo calculada pelo resíduo global

$$
Q(\Sigma)
=\frac{1}{2\pi i}
\oint_{\Gamma_\Sigma}\frac{\phi'}{\phi}\,dz,
$$

e não pela soma das amplitudes $\mathcal T_a$.

**Lema 2 procurado:** as leis de conservação são identidades de Stokes/índice
no cobordismo e não uma atribuição posterior aos produtos.

### Etapa 3 — Identificar geometricamente as duas saídas

Calcular em cada componente assintótica, de forma independente,

$$
(Q,J,B,L_e,\chi,\operatorname{Hol},\operatorname{Ind}_{\rm APS}),
$$

onde $\chi$ denota o dado quiral quando ele estiver definido.

A identificação só será aceita se resultar

$$
\Sigma_e:\quad (Q,J,B,L_e)=(-1,\tfrac12,0,+1),
$$

$$
\Sigma_{\bar\nu}:\quad (Q,J,B,L_e)=(0,\tfrac12,0,-1),
$$

além da quiralidade/holonomia correta de cada modo. Não se atribui aqui uma
paridade isolada ao antineutrino. Em particular, neutralidade elétrica do
resíduo torsional deve ser calculada; ela não segue de ele ser chamado de
antineutrino.

**Lema 3 procurado:** os invariantes das duas componentes de saída separam
univocamente o setor eletrônico do setor antineutrino.

### Etapa 4 — Provar a existência do canal dinâmico

No espaço de caminhos $\mathscr P$ entre os backgrounds, restringir a ação
oficial:

$$
\mathcal A[\Gamma]
=\mathcal S_{\rm GDQ}[g_\Gamma,f_\Gamma;H(g_\Gamma,J_\Gamma)],
\qquad
\Gamma\in\mathscr P.
$$

Há duas possibilidades fisicamente distintas, que não devem ser misturadas:

1. **instabilidade clássica:** a Hessiana de $\mathfrak G_n$ possui um modo
   físico negativo no setor que preserva $B_{\rm top}=1$;
2. **transição por túnel:** $\mathfrak G_n$ é um mínimo local e existe uma sela
   causal de ação finita ligando os dois setores.

O cálculo da Hessiana decide qual alternativa é correta.

**Lema 4 procurado:** existe uma trajetória crítica admissível, com a contagem
correta de modos negativos e sem usar elongação livre dos estômatos como modo
físico.

### Etapa 5 — Hessiana física e modos assintóticos

Fixar gauge geométrico, remover difeomorfismos puros e calcular

$$
\mathcal J_\Gamma
=\operatorname{Hess}\mathcal S_{\rm GDQ}\big|_\Gamma
$$

no domínio definido pelos colares e pelo contorno causal. Deve-se demonstrar:

1. ausência de modos físicos espúrios de elongação;
2. estabilidade transversal da trajetória;
3. existência dos modos localizados que se tornam $p$, $e^-$ e $\bar\nu_e$;
4. normalização e ortogonalidade no produto interno ponderado por $\mathcal U$;
5. limite assintótico lorentziano causal dos modos emitidos.

**Lema 5 procurado:** o operador de Jacobi possui exatamente o conteúdo modal
necessário à cirurgia e nenhum canal de carga ou spin incompatível.

### Etapa 6 — Fechar a energia disponível

A Q40 fornece estruturalmente

$$
M_n-M_p=\delta_B M_e,
\qquad
\delta_B=\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

Logo a energia cinética disponível no canal proposto é

$$
Q_\beta
=M_n-M_p-M_e
=(\delta_B-1)M_ec^2.
$$

Esta é uma avaliação direta de uma fórmula já adotada, não uma nova previsão
independente. Deve-se verificar que os backgrounds normalizados dos quatro
setores usam a mesma escala $\Lambda_C$ e a mesma convenção de energia.

**Lema 6 procurado:** a diferença on-shell da ação coincide com a energia
assintótica total e é positiva no canal de três corpos.

### Etapa 7 — Derivar o vértice efetivo da GDQ

Expandir a ação oficial em torno da trajetória crítica. O primeiro termo que
acopla os quatro modos normalizados define o elemento de transição geométrico:

$$
\mathcal M_{n\to pe\bar\nu}
=\mathcal V^{(k)}_{\rm GDQ}
[\psi_n,\psi_p,\psi_e,\psi_{\bar\nu}],
$$

onde $k$ é a primeira ordem não nula da variação funcional. Só depois dessa
projeção podem ser definidos, como parâmetros **derivados da redução**,

$$
G_F^{\rm GDQ},
\qquad
g_A^{\rm GDQ}.
$$

Não se deve inserir o vértice de Fermi ou uma ação Yang--Mills como termo
fundamental da GDQ.

**Lema 7 procurado:** o overlap é finito, não nulo, possui a estrutura quiral
correta e fixa sua normalização sem usar a vida média do nêutron como entrada.

### Etapa 8 — Espectro e taxa

Com $\mathcal M$ congelado antes da comparação, calcular a medida espectral
dos modos de saída e a taxa

$$
d\Gamma
=\frac{2\pi}{\hbar}
|\mathcal M_{n\to pe\bar\nu}|^2\,d\mu_{p e\bar\nu}.
$$

O espectro contínuo do elétron deve resultar da integração sobre o modo neutro
e o recuo do próton. Correções de Coulomb, recoil e forma só podem entrar se
forem derivadas do background/operador de sonda correspondente.

**Teorema final procurado:** a taxa total, a distribuição eletrônica e as
correlações angulares seguem da ação oficial com parâmetros congelados.

## 16. Dependência lógica

$$
\boxed{
\text{backgrounds}
\to W
\to \text{correntes e índices}
\to \text{identificação das saídas}
\to \text{trajetória crítica}
\to \text{Hessiana}
\to \mathcal M
\to d\Gamma.
}
$$

Uma concordância numérica da vida média antes de fechar os lemas 1--7 seria
ajuste ou engenharia inversa, não prova do mecanismo.

## 17. Critério de fechamento

O mecanismo poderá ser classificado como **fechado condicionalmente** quando
os lemas 1--7 estiverem demonstrados sob hipóteses explícitas e o problema
espectral possuir solução controlada. Só poderá ser classificado como
**fechado** quando também houver:

1. existência e estabilidade da solução no domínio causal completo;
2. taxa e espectro obtidos sem calibração pela vida média;
3. análise de sensibilidade e convergência numérica;
4. ao menos um observável discriminante congelado antes da comparação.

## 18. Primeiro alvo de trabalho

O refinamento bimodal está em `nucleacao_par_mesonico_torcional.md`. A rota
agora testada é

$$
n\longrightarrow p+\Pi^-_{\rm virt}
\longrightarrow p+e^-+\bar\nu_e,
$$

onde $\Pi^-_{\rm virt}$ é um tubo transitório de dois estômatos. A conservação
de fluxo fornece uma contribuição negativa explícita à Hessiana do modo de
abertura do par. O dado que seleciona a multiplicidade dois é a torção do
estômato contrário,

$$
\mathcal T_3^{(n)}=-2\tau=(-\tau)+(-\tau).
$$

Em sistemas perturbados, condições de contorno de Robin para a Hessiana podem
deslocar um modo bimodal através de zero e permitir a formação de uma
configuração mesônica com dois estômatos. O critério espectral e a distinção
entre estado ligado e intermediário virtual estão registrados em
nucleacao_par_mesonico_torcional.md.

O próximo passo é avaliar a Hessiana **total** desse modo no background colado
da Q40. Como o modo muda o número de estômatos, essa avaliação deve ser feita
como segunda variação unilateral no espaço estratificado, conforme
`hessiana_estratificada_nucleacao_bimodal.md`. Isso decidirá se há nucleação
clássica ou apenas uma sela de túnel.

O fechamento condicional completo da rota reduzida — núcleo crítico, bounce,
invariantes dos modos finais e forma do espectro — está em
`fechamento_condicional_mecanismo_neutron.md`. A vida média numérica permanece
dependente do overlap causal $\mathcal M_0$ ainda não avaliado.

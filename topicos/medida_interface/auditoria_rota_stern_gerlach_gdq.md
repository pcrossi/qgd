# Auditoria da rota de Stern--Gerlach e da interface de medida

## Veredito

A rota estrutural é correta, mas o desenvolvimento recente ultrapassou o
problema que se pretendia resolver e começou a circular em torno da mesma
pendência: a ausência de um background macroscópico explícito do aparelho.

O problema deve ser separado em três níveis. Misturá-los faz uma derivação
finita parecer interminável.

## Nível I — problema quântico operacional

Para Stern--Gerlach, basta uma dinâmica efetiva de dois canais com acoplamento

\[
V_{\rm SG}=-\mu_{\rm GDQ}\,\boldsymbol n\cdot\boldsymbol B(\boldsymbol x),
\]

seguida da força

\[
\boldsymbol F_\pm=-\nabla V_\pm
\]

e dos pesos iniciais

\[
p_\pm=\frac{1\pm\boldsymbol a\cdot\boldsymbol n}{2}.
\]

Na GDQ, já foram construídos os ingredientes estruturais desse nível:

1. módulo de Hopf \(\mathbb{CP}^1\);
2. dois canais axiais;
3. sobreposição \(\boldsymbol a\cdot\boldsymbol n\);
4. acoplamento Zeeman emergente por equivariância;
5. gradiente espacial que separa os canais;
6. pesos de Born condicionais pela geometria de projetores/Hopf.

Esse nível está estruturalmente fechado, deixando \(\mu_{\rm GDQ}\) como
coeficiente efetivo mensurável ou como alvo de uma derivação posterior.

## Nível II — teoria de medida reduzida

Para explicar registro, amplificação e irreversibilidade, a ação microscópica
do objeto não basta. É necessário especificar também o estado inicial e a
resposta macroscópica do aparelho. A redução já construída contém:

1. variável de ponteiro com duas bacias;
2. viés condicionado pelo canal do objeto;
3. canal dissipativo causal;
4. filtro estocástico;
5. teorema condicional de captura com probabilidades de Born.

Esse nível está fechado como teorema efetivo condicional. Ele não constitui
ainda uma derivação de um material detector particular diretamente da ação
oficial.

## Nível III — derivação microscópica integral do aparelho

Aqui seria necessário escolher uma solução GDQ macroscópica concreta e obter
de sua Hessiana:

\[
K_A,\quad \Lambda_A^{\rm ret},\quad \gamma_A,\quad T_X,\quad
g_X,\quad w_H,\quad \ell_B.
\]

Esse é um projeto independente de física da matéria/aparelhos. Nem a ação de
Schrödinger nem a ação de Dirac, isoladamente, derivam a constituição de um
ímã, sua temperatura, seus domínios, seu banho e sua tela. Esses dados entram
por Hamiltonianos efetivos, estados e condições de contorno adicionais.

Exigir que a ação oficial da GDQ derive tudo isso antes de aceitar o mecanismo
de Stern--Gerlach impõe à GDQ uma obrigação que não é exigida da mecânica
quântica operacional. Isso pode ser uma ambição futura da teoria, mas não deve
ser critério de fechamento do problema básico.

## Onde surgiu o loop

A sequência repetitiva foi:

\[
\text{coeficiente desconhecido}
\to K_H
\to c_H,i_H
\to Z_H
\to \text{kernel físico do aparelho}
\to \text{background macroscópico}
\to K_H.
\]

Os testes numéricos com kernels diferentes não determinam o kernel físico;
apenas demonstram sua relevância. Continuar variando Robin ou kernels sem um
background novo não acrescentará poder preditivo.

Além disso, a circulação semi-inteira e o momento magnético não devem ser
identificados automaticamente. A primeira é topológica; o segundo pode conter
um fator constitutivo/espectral. Tentar forçar \(Z_H=1\) apenas para recuperar
um valor esperado seria pós-ajuste.

## Correção de rota

Adotam-se dois fechamentos separados:

### Fechamento SG estrutural

Declarar demonstrada, dentro das hipóteses já documentadas, a cadeia

\[
\text{Hopf}
\to\text{dois canais}
\to\text{acoplamento axial}
\to\text{separação espacial}
\to\text{amplificação}
\to\text{frequências de Born}.
\]

O módulo de \(\mu_{\rm GDQ}\), a impedância e a taxa de captura ficam como
parâmetros efetivos do experimento, tal como ocorre numa descrição quântica
operacional.

### Programa microscópico do detector

Manter como trabalho posterior a derivação desses coeficientes para um
background material específico. Esse programa só deve ser retomado quando
forem fornecidos:

1. background estacionário explícito do aparelho;
2. identificação do modo coletivo observado;
3. condições físicas de contorno e estado térmico;
4. bloco físico da Hessiana da ação oficial;
5. mapa geométrico entre o campo clássico aplicado e o setor torsional.

Sem esses cinco dados, novos números serão diagnósticos ou ajustes, não
previsões.

Para o coeficiente giromagnético do objeto, entretanto, não é necessário
resolver o background do aparelho: o campo é fonte externa dada. A rota
intrínseca por multiplicador de circulação está consolidada em
`topicos/medida_interface/auditoria_gamma_magnetica_ZH.md`.

## Critério de parada

Não se deve continuar calculando novos kernels abstratos. O próximo avanço só
é legítimo se ocorrer uma destas duas coisas:

1. consolidar o resultado estrutural de Stern--Gerlach, sem exigir constantes
   materiais de primeiros princípios; ou
2. escolher um aparelho GDQ concreto e resolver seu background.

## Status recomendado

> Stern--Gerlach está fechado como redução geométrica e teoria efetiva
> condicional de medida. A derivação microscópica absoluta de um detector real
> permanece aberta e não é requisito para o fechamento operacional do
> experimento.

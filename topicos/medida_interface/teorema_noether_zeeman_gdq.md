# Teorema de Noether--Zeeman da GDQ

## 1. Enunciado

Considere um sóliton GDQ estacionário cujo módulo interno livre seja isotrópico
e possua um fluxo vetorial conservado \(\boldsymbol C\), normalizado no setor
fermiônico elementar por

\[
|\boldsymbol C|=C_{1/2}=\frac\hbar2.
\]

Se o campo magnético externo \(\boldsymbol B\) é a fonte conjugada a esse
mesmo fluxo de Noether, então:

1. a interação linear é necessariamente Zeeman;
2. as configurações estacionárias são paralela e antiparalela ao campo;
3. a componente mínima do acoplamento ao fluxo é unitária;
4. nenhum kernel radial independente é necessário para o fechamento de
   Stern--Gerlach.

## 2. Origem do fluxo na ação oficial

A ação oficial é invariante sob deslocamento constante da fase,

\[
f\mapsto f+i\varepsilon,
\qquad
\bar f\mapsto\bar f-i\varepsilon,
\]

porque \(f+\bar f\) permanece inalterado e o integrando depende da fase apenas
por suas derivadas. Promovendo \(\varepsilon\) localmente, a primeira variação
define a corrente de Noether de fase. Esquematicamente, omitindo apenas o
fator comum positivo da ação,

\[
J^A_{\rm N}
\propto
i\tau\mathcal U
\left(
g^{A\bar B}\partial_{\bar B}\bar f
-g^{B\bar A}\partial_Bf
\right),
\qquad
\nabla_AJ^A_{\rm N}=0.
\]

No setor do defeito, a projeção rotacional/Hopf desse fluxo define o mapa de
momento vetorial

\[
\boldsymbol{\mathcal C}[\Phi]
=\int_\Sigma \boldsymbol J_{\rm N}\cdot d\boldsymbol\Sigma.
\]

A dupla cobertura seleciona os setores elementares

\[
\boldsymbol C
=\pm\frac\hbar2\boldsymbol n.
\]

## 3. Funcional com vínculo e fonte

O campo do aparelho é dado externo e não é variado. O problema físico é

\[
\boxed{
\mathscr I[\Phi,\boldsymbol\lambda;
\boldsymbol C,\boldsymbol B]
=S_{\rm GDQ}[\Phi]
-\boldsymbol B\cdot\boldsymbol M[\Phi]
-\boldsymbol\lambda\cdot
\left(\boldsymbol{\mathcal C}[\Phi]-\boldsymbol C\right).
}
\]

O observável magnético decompõe-se em

\[
\boldsymbol M[\Phi]
=\gamma_0\boldsymbol{\mathcal C}[\Phi]
+\boldsymbol M_\perp[\Phi].
\]

Aqui \(\gamma_0\) converte o fluxo protegido nas unidades magnéticas e
\(\boldsymbol M_\perp\) representa a deformação interna que não altera a
carga de Noether.

Variando \(\boldsymbol\lambda\):

\[
\boldsymbol{\mathcal C}[\Phi]=\boldsymbol C.
\]

Variando \(\Phi\):

\[
\frac{\delta S_{\rm GDQ}}{\delta\Phi}
-\boldsymbol B\cdot\frac{\delta\boldsymbol M}{\delta\Phi}
-\boldsymbol\lambda\cdot
\frac{\delta\boldsymbol{\mathcal C}}{\delta\Phi}=0.
\]

Se nenhuma deformação interna adicional responder ao campo, ele desloca o
multiplicador conjugado por

\[
\boxed{
\boldsymbol\lambda(\boldsymbol B)
=\boldsymbol\lambda(0)-\gamma_0\boldsymbol B.
}
\]

Portanto,

\[
\boxed{
-\frac{\partial\lambda_i}{\partial B_j}
=\gamma_0\delta_{ij}.
}
\]

## 4. Isotropia e forma única da energia

Antes da aplicação do campo, a isotropia impede a existência de um eixo
preferencial. A energia reduzida só pode depender de \(C^2\). Na presença de
uma fonte vetorial fraca, o único escalar linear permitido é

\[
\boldsymbol C\cdot\boldsymbol B.
\]

Assim,

\[
\boxed{
E(\boldsymbol C,\boldsymbol B)
=E_0(C^2)-\gamma_{\rm eff}\boldsymbol C\cdot\boldsymbol B+O(B^2).
}
\]

Essa é a interação Zeeman, obtida sem introduzir matrizes de Pauli na ação
fundamental.

## 5. Seleção estacionária

Com \(|\boldsymbol C|\) fixo, uma variação angular é

\[
\delta\boldsymbol C
=\delta\boldsymbol\theta\times\boldsymbol C.
\]

Logo,

\[
\delta E
=-\gamma_{\rm eff}\delta\boldsymbol\theta\cdot
(\boldsymbol C\times\boldsymbol B).
\]

A condição estacionária é

\[
\boldsymbol C\times\boldsymbol B=0,
\]

e, no setor elementar,

\[
\boxed{
\boldsymbol C_\pm
=\pm\frac\hbar2\frac{\boldsymbol B}{|\boldsymbol B|}.
}
\]

As energias são

\[
\boxed{
E_\pm
=E_0\mp\gamma_{\rm eff}\frac\hbar2|\boldsymbol B|.
}
\]

Para campo inomogêneo,

\[
\boxed{
\boldsymbol F_\pm
=\pm\gamma_{\rm eff}\frac\hbar2\nabla|\boldsymbol B|.
}
\]

## 6. Parte protegida e vestido geométrico

O fator \(Z_H\) havia sido introduzido ao tratar circulação e resposta
magnética como funcionais independentes. Sob a hipótese física deste teorema
— o campo acopla ao mesmo fluxo de Noether conservado — temos

\[
M_{\boldsymbol n}
=\gamma_0\mathcal C_{\boldsymbol n}.
\]

Consequentemente, para a componente mínima protegida por Noether,

\[
\boxed{Z_{\rm N}=1.}
\]

Isso não obriga o momento magnético total a coincidir com a parte mínima. O
campo pode deformar modos internos do mesmo sóliton sem alterar sua carga de
Noether. Esses modos produzem um vestido geométrico transversal e, portanto,
um momento anômalo compatível com a conservação do fluxo.

Escreva o diferencial magnético como

\[
m=\gamma_0c+m_\perp,
\]

onde \(c=\delta\mathcal C/\delta\Phi\), a primeira parcela é protegida pela
identificação de Noether e \(m_\perp\) contém a resposta interna que não muda
o quantum de fluxo.

No background vinculado, com Hessiana física \(H_C\), a resposta do
multiplicador fornece

\[
\boxed{
\gamma_{\rm eff}
=-\left.\frac{\partial\lambda}{\partial B}\right|_{B=0}
=\frac{\langle c,H_C^{-1}m\rangle}
       {\langle c,H_C^{-1}c\rangle}.
}
\]

Substituindo a decomposição de \(m\):

\[
\boxed{
\gamma_{\rm eff}
=\gamma_0+\Delta\gamma_{\rm geom},
\qquad
\Delta\gamma_{\rm geom}
=\frac{\langle c,H_C^{-1}m_\perp\rangle}
       {\langle c,H_C^{-1}c\rangle}.
}
\]

Portanto, o fator total anteriormente denominado \(Z_H\) é

\[
\boxed{
Z_H=\frac{\gamma_{\rm eff}}{\gamma_0}
=1+\frac{\Delta\gamma_{\rm geom}}{\gamma_0}.
}
\]

Noether fixa o termo \(1\); a ação oficial e o background determinam o excesso.

## 7. Razão giromagnética

Escrevendo

\[
\boldsymbol\mu
=\gamma_{\rm eff}\boldsymbol C
=g\frac{q}{2mc}\boldsymbol C,
\]

segue

\[
g=\frac{2mc}{q}\gamma_{\rm eff}.
\]

A conservação de Noether e a dupla cobertura fixam a contribuição mínima. Na
normalização

\[
\gamma_0=\frac q{mc}.
\]

ela produz \(g_0=2\). A resposta geométrica total é

\[
\boxed{
g_{\rm GDQ}
=2\left(1+a_{\rm geom}\right),
\qquad
a_{\rm geom}
=\frac{\Delta\gamma_{\rm geom}}{\gamma_0}
=-\frac1{\gamma_0}
\left.\frac{\partial\lambda_{\rm geom}}{\partial B}\right|_{0}.
}
\]

Assim, o valor ligeiramente superior a dois é precisamente a parte do
multiplicador gerada pela deformação interna do background, e não uma quebra
da conservação de Noether.

## 7.1 Avaliação numérica na ordem geométrica líder

O Capítulo 19 propõe, na primeira ordem do vestido geométrico,

\[
a_{\rm geom}^{(1)}=\frac{\alpha}{2\pi}.
\]

Usando

\[
\alpha^{-1}=137.035999177,
\]

obtém-se

\[
\boxed{
a_{\rm geom}^{(1)}=0.001161409732098,
}
\]

\[
\boxed{
Z_H^{(1)}=1.001161409732098,
}
\]

e

\[
\boxed{
g_{\rm GDQ}^{(1)}
=2\left(1+\frac{\alpha}{2\pi}\right)
=2.002322819464196.
}
\]

Tomando como referência o módulo do fator eletrônico medido,
\(g_e\simeq2.00231930436092\), a aproximação líder fica acima por

\[
\Delta g\simeq3.51510\times10^{-6},
\]

ou aproximadamente \(1.76\) partes por milhão em \(g\).

Logo, o termo \(\alpha/(2\pi)\) produz corretamente a escala e o sinal do
excesso, mas não é uma previsão metrológica completa. Para isso é necessário
avaliar os termos geométricos superiores contidos na resposta total
\(H_C^{-1}m_\perp\), sem calibrá-los pelo valor experimental de \(g_e\).

## 7.2 Isotropia, carga e densidade de circulação

Seja \(\vartheta\in[0,2\pi)\) a coordenada do ciclo elementar de fase. A
isotropia do background implica invariância sob

\[
\vartheta\mapsto\vartheta+\vartheta_0.
\]

Logo, a densidade de Noether ao longo da órbita é constante. Se
\(\varrho_C(\vartheta)\) é essa densidade e \(C\) a carga/circulação total,

\[
C=\int_0^{2\pi}\varrho_C(\vartheta)d\vartheta,
\]

então

\[
\boxed{
\varrho_C(\vartheta)=\frac{C}{2\pi}.
}
\]

Essa é a conexão precisa entre isotropia e carga: o fluxo conservado é
uniformemente distribuído sobre a órbita de fase.

O vestido geométrico não é uma segunda integração linear da carga. Ele vem da
forma quadrática da ação — equivalentemente, da Hessiana do fluxo. Por isso,
a quantidade relevante é a norma da densidade isotrópica:

\[
\int_0^{2\pi}\varrho_C(\vartheta)^2d\vartheta
=\int_0^{2\pi}\left(\frac{C}{2\pi}\right)^2d\vartheta
=\boxed{\frac{C^2}{2\pi}}.
\]

Essa identidade é precisamente a projeção angular do termo quadrático em
\(|dS_R|^2\) da ação oficial. Para \(C^2\) fixo no setor elementar, a resposta
isotrópica linear ao campo pode ser escrita

\[
\delta E_B^{\rm geom}
=-\alpha\gamma_0
\frac{\boldsymbol C\cdot\boldsymbol B}{C^2}
\int_0^{2\pi}\varrho_C^2d\vartheta.
\]

Logo,

\[
\boxed{
\delta E_B^{\rm geom}
=-\gamma_0\frac{\alpha}{2\pi}
\boldsymbol C\cdot\boldsymbol B,
}
\]

e portanto

\[
\boxed{
a_{\rm geom}^{(1)}=\frac\alpha{2\pi}.
}
\]

Não ocorre dupla contagem: a carga usa a primeira potência,
\(\int\varrho_C=C\), enquanto o vestido elástico usa a segunda,
\(\int\varrho_C^2=C^2/(2\pi)\).

### Correção aritmética identificada no manuscrito

O `Apêndice 1 - A Dedução Espectral do Índice de Compressão Torsional.md`
já tenta efetuar essa projeção, mas registra

\[
\int_0^{2\pi}\left(\frac1{2\pi}\right)^2d\vartheta
=\frac1{4\pi^2}.
\]

Essa igualdade está aritmeticamente incorreta. O resultado correto é

\[
\boxed{
\int_0^{2\pi}\left(\frac1{2\pi}\right)^2d\vartheta
=\frac1{2\pi}.
}
\]

Assim, a própria projeção isotrópica quadrática já presente no manuscrito
fornece o coeficiente angular necessário. O manuscrito-base deve ser corrigido
posteriormente sem propagar a antiga expressão \(1/(4\pi^2)\) para cálculos
bariônicos que usem aquele apêndice.

## 8. Status

A projeção explícita da Hessiana no modo harmônico está em
`topicos/geometria_torcao_hopf/projecao_hessiana_noether_g2.md`. Ela confirma diretamente a norma
\(1/(2\pi)\) e identifica com precisão o numerador eletrogeométrico que deve
ser fornecido pelo setor de conexão de Chern.

\[
\boxed{
\begin{aligned}
&\text{forma Zeeman: derivada por isotropia;}\\
&\text{dois canais: derivados pelo setor }C=\hbar/2;\\
&Z_{\rm N}=1:\text{ parte mínima protegida por Noether;}\\
&g=2(1+a_{\rm geom}):\text{ resposta total do multiplicador.}
\end{aligned}
}
\]

Assim, a microestrutura do detector não pertence à prova. O cálculo de
\(a_{\rm geom}\) pertence exclusivamente ao background do objeto.

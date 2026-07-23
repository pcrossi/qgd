# Auditoria de backgrounds macroscópicos para a interface GDQ

## 1. Pergunta

Existe no manuscrito um background macroscópico já suficientemente definido
para calcular, a partir da ação oficial, a impedância

\[
\gamma_A=\frac{\zeta_A}{c_A}
\]

do detector ôhmico idealizado?

## 2. Veredito

\[
\boxed{
\text{Não existe ainda um background macroscópico completo e diretamente
avaliável.}
}
\]

O manuscrito contém todas as peças conceituais necessárias, mas elas aparecem
em setores diferentes e ainda não foram reunidas numa solução estacionária com:

1. métrica e campo \(f\) explícitos;
2. normalização da medida;
3. Hessiana física gauge-fixada;
4. reconstrução em tempo real;
5. modo coletivo legível;
6. espectro contínuo de saída;
7. sobreposição de bordo calculável.

O melhor caminho não é escolher um número de impedância já usado no
manuscrito. É construir um background composto com lado microscópico e lado
macroscópico claramente separados.

---

## 3. Candidatos encontrados

### 3.1 Capítulo 21 — NESS, Fano e Zwanzig--Mori

O Capítulo 21 contém a arquitetura mais próxima do aparelho:

\[
\partial_\tau\mathcal P\rho
=-i\mathcal P\mathcal L\mathcal P\rho
-\int_0^\tau\mathcal K(s)
\mathcal P\rho(\tau-s)ds
+\mathcal F(\tau),
\]

com

\[
\mathcal K(s)
=\mathcal P\mathcal L
e^{-i\mathcal Q\mathcal Ls}
\mathcal Q\mathcal L\mathcal P.
\]

Contribuições aproveitáveis:

1. separação entre macrovariáveis e modos não observados;
2. núcleo de memória;
3. força flutuante;
4. acoplamento de estado discreto a contínuo;
5. interpretação da irreversibilidade por coarse-graining.

Limitações:

1. \(\mathcal L\) não é calculado da Hessiana oficial;
2. o contínuo \(|\psi_E\rangle\) é postulado em forma de Fano;
3. os elementos \(V_E\) não são avaliados;
4. \(\tau\) aparece como variável da equação de Liouville, sem completar a
   reconstrução para o tempo físico \(t\);
5. a desigualdade de produção de entropia não é derivada para um background
   concreto.

Status:

\[
\boxed{\text{arquitetura correta; background e espectro ausentes}.}
\]

### 3.2 Questão 32 — Hessiana e núcleo de calor

A Q32 organiza o operador quadrático euclidiano:

\[
\mathcal O_{\rm GDQ}
=-\Delta_B+V_{\rm eff},
\]

e o semigrupo

\[
e^{-\tau\mathcal O_{\rm GDQ}}.
\]

Contribuições aproveitáveis:

1. origem da Hessiana na ação;
2. símbolo principal e regularização geométrica;
3. base espectral bem definida;
4. separação entre Hessiana e gerador de calor.

Limitações:

1. o operador é euclidiano/estático;
2. não fornece automaticamente o kernel retardado;
3. o setor vetorial permanece efetivo condicional;
4. não seleciona uma macrovariável nem um domínio aberto.

Status:

\[
\boxed{\text{fornece }\mathbb H_A;\text{ falta OS + domínio aberto}.}
\]

### 3.3 Capítulo 28 — Limite clássico

O Capítulo 28 contém a intenção de recuperar ondas e campos clássicos no
limite macroscópico.

Contribuições aproveitáveis:

1. separação de regimes;
2. propagação de perturbações no tempo físico;
3. interpretação elástica de modos macroscópicos.

Limitações:

1. a passagem \(\tau\to it\) é apresentada de modo mais forte do que a
   reconstrução OS permite;
2. não há background do aparelho;
3. não são fornecidos \(K_t,K_x,T_y\);
4. a impedância não é calculada.

Uso correto:

O capítulo sustenta a existência esperada de um limite ondulatório, mas a
continuação para tempo físico deve ser realizada pela reconstrução OS do setor,
não por uma substituição formal isolada.

### 3.4 Capítulos 23 e 27 — Fano e impedâncias

Esses capítulos usam fatores denominados impedância, admitância de Fano e
Fredholm.

Contribuição:

- sugerem que a razão entre canal localizado e contínuo é fisicamente central.

Limitação decisiva:

Os números \(3\sqrt2/5\), \(0,4791\), fatores de forma e correções posteriores
não são o DtN de um background macroscópico calculado. Eles não podem ser
reutilizados como \(\zeta_A/c_A\) do detector sem derivar a matriz de
transmissão correspondente.

Status:

\[
\boxed{\text{motivação; não usar como impedância do aparelho}.}
\]

### 3.5 Capítulo 37 e Apêndice 9 — detector e dupla fenda

Esses textos introduzem anteparo, seção de absorção e “impedância métrica” do
detector.

Contribuição:

- reconhecem que o detector deve modificar a condição de interface.

Limitações:

1. a impedância é fenomenológica;
2. não há Hessiana do material;
3. propagação avançada/retroativa é afirmada sem problema bem posto;
4. não se calcula registro, ruído ou amplificação.

Status:

\[
\boxed{\text{ideia de interface; não é background calculável}.}
\]

### 3.6 Q42 — shrinker cilíndrico de Hopf

A Q42 fornece o background explícito mais rigoroso:

\[
M_\perp=\mathbb R_+\times S^3_{2\sqrt\tau},
\qquad
F=\frac{r^2}{4\tau}+\frac12\log\pi.
\]

O setor axial possui

\[
V_H=\frac2\tau,
\qquad
z_H=\frac{3\sqrt\pi}{4}.
\]

Contribuições aproveitáveis:

1. solução estacionária exata;
2. medida normalizada;
3. garganta e condição variacional;
4. operador axial;
5. DtN do lado do objeto.

Limitação:

O potencial positivo \(V_H=2/\tau\) produz um setor localizado/gapped. Ele não
é um contínuo macroscópico ôhmico. O peso gaussiano radial também impede
identificá-lo diretamente com uma linha de transmissão homogênea infinita.

Status:

\[
\boxed{\text{usar como }\Lambda_Q;\text{ não usar como }\Lambda_A^{\rm ôhmico}.}
\]

---

## 4. Background composto recomendado

A interface deve combinar dois backgrounds com funções distintas:

\[
\boxed{
\text{garganta de Hopf Q42}
\quad\cup_\Sigma\quad
\text{canal macroscópico NESS aberto}.
}
\]

### 4.1 Lado do objeto

Usar:

\[
\Lambda_Q
=\frac{\mathsf Z_\partial}{\sqrt\tau}
\frac{3\sqrt\pi}{4}
\]

no setor axial localizado, mantendo a matriz de normalização física do traço.

### 4.2 Lado do aparelho

Construir um background macroscópico \(\Phi_{A*}\) que possua um modo físico
de propagação \(T_y\) ao longo de uma coordenada aberta \(x\):

\[
\delta\Phi_A=y(x,t)T_y+\cdots.
\]

A projeção da Hessiana deve fornecer, em baixa energia:

\[
S_A^{(2)}
=\frac12\int dt\,dx
\left[
Z_t(\partial_ty)^2
-Z_x(\partial_xy)^2
-m_y^2y^2
\right].
\]

Para o limite ôhmico do documento anterior:

\[
\boxed{m_y=0,\qquad Z_t>0,\qquad Z_x>0.}
\]

Então:

\[
\zeta_A=Z_x,
\qquad
c_A^2=\frac{Z_x}{Z_t},
\qquad
\gamma_A=\sqrt{Z_tZ_x}.
\]

Essa forma mostra que a impedância pode ser calculada diretamente das duas
normas cinéticas da Hessiana.

---

## 5. Critério espectral para comportamento ôhmico

O resultado do canal semi-infinito não exige que todo aparelho seja ôhmico. Ele
exige as seguintes propriedades de baixa frequência:

1. espectro contínuo próximo de \(\omega=0\);
2. dispersão linear:

   \[
   \omega(k)=c_A|k|+O(k^2);
   \]

3. densidade espectral de bordo não nula;
4. ausência de gap no canal monitorado;
5. condição de radiação retardada;
6. acoplamento de bordo regular quando \(\omega\to0\).

Sob essas condições:

\[
\operatorname{Im}\Lambda_A^{\rm ret}(\omega)
=-\gamma_A\omega+o(\omega).
\]

Se houver gap, banda ou geometria finita:

\[
\Lambda_A^{\rm ret}(\omega)
\]

será colorido e não local no tempo. Essa não é uma falha; é a previsão correta
para o aparelho correspondente.

---

## 6. Pode-se usar fundo plano homogêneo?

Um fundo plano com \(f\) constante é útil como aproximação tangente local, mas
não deve ser declarado solução shrinker compacta global. Em fluxo finito,

\[
\operatorname{Ric}+\nabla^2f
=\frac1{2\tau}g
\]

não é satisfeito por um toro plano compacto com \(f\) constante.

Há duas rotas legítimas:

### Rota local/WKB

Em uma região macroscópica pequena comparada à escala de variação do
background:

\[
L_{\rm aparelho}\ll L_f,
\]

aproximar \(\mathcal U_*\), \(g_*\), \(Z_t\) e \(Z_x\) como constantes. O
canal ôhmico é então o símbolo principal local da Hessiana.

### Rota global NESS

Resolver um background não compacto ou estacionário no tempo físico, com fluxo
líquido e condições de entrada/saída, em vez de exigir um shrinker compacto
com \(f\) constante.

A Rota local já sustenta o teste diagnóstico. Uma previsão material exige a
Rota global ou uma geometria finita explicitamente resolvida.

---

## 7. Cálculo exigido pela ação oficial

Para um candidato \(\Phi_{A*}\), executar:

1. verificar Euler--Lagrange e condições de bordo;
2. normalizar \(\mathcal U_*\);
3. calcular a Hessiana física \(\mathbb H_A\);
4. identificar um modo coletivo \(T_y\);
5. calcular

   \[
   Z_t=\langle T_y,K_tT_y\rangle_{\mathcal U_*},
   \]

   \[
   Z_x=\langle T_y,K_xT_y\rangle_{\mathcal U_*};
   \]

6. verificar \(m_y^2=0\) ou medir o gap;
7. reconstruir o kernel retardado por OS;
8. aplicar condição de radiação;
9. obter

   \[
   \gamma_A=\sqrt{Z_tZ_x};
   \]

10. calcular a sobreposição torsional \(g_X\).

---

## 8. Escolha recomendada para o primeiro background calculável

Usar uma célula macroscópica quase homogênea, aberta em uma direção física:

\[
\Omega_A
=\Sigma_A\times\mathbb R_+,
\]

com:

1. \(\Sigma_A\) compacta e finita, representando a seção do canal;
2. background lentamente variável em \(x\);
3. modo transversal fundamental \(T_y\);
4. condição retardada em \(x\to\infty\);
5. normalização por unidade de seção, não normalização probabilística global
   sobre o domínio infinito.

Essa construção é a tradução geométrica mínima de um canal macroscópico. Ela
é compatível com o NESS do Capítulo 21 e evita a contradição do toro plano
compacto shrinker.

---

## 9. O que pode e não pode ser declarado agora

Pode-se declarar:

\[
\boxed{
\text{o manuscrito contém a arquitetura NESS/coarse-graining e a Q42 contém o
DtN microscópico.}
}
\]

\[
\boxed{
\text{um modo macroscópico gapless com dispersão linear produz impedância
ôhmica }\gamma_A=\sqrt{Z_tZ_x}.
}
\]

Não se pode declarar:

\[
\boxed{
\text{a impedância de um material real já foi calculada no manuscrito.}
}
\]

Também não se deve identificar \(\gamma_A\) com \(\chi_{\rm Fano}\),
\(Z_0=376,73\,\Omega\) ou qualquer outro número sem mapa dimensional e
espectral explícito.

---

## 10. Próximo passo

Construir a redução local da Hessiana oficial numa célula
\(\Sigma_A\times\mathbb R_+\), mantendo \(Z_t\) e \(Z_x\) simbólicos, e depois
escolher um modo geométrico concreto:

1. modo dilatônico;
2. modo torsional transversal;
3. modo métrico-elástico;
4. modo eletromagnético emergente.

O modo torsional transversal é o candidato mais coerente com o acoplamento de
Stern--Gerlach já derivado.

Essa redução foi executada em `topicos/medida_interface/reducao_hessiana_torcional_aparelho.md`. Uma
2-forma harmônica de \(T^4\), propagando ao longo da direção aberta, produz um
canal gapless com
\(c_A^2=Z_x/Z_t\) e \(\gamma_A=\sqrt{Z_tZ_x}\). Permanecem a normalização
causal, a mistura com métrica/dílaton e a avaliação do background material.

## 11. Status

\[
\boxed{
\text{background candidato identificado, mas ainda não resolvido globalmente;}
\quad
\text{aproximação local/WKB suficiente para o detector diagnóstico.}
}
\]

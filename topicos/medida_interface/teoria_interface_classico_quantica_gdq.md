# Teoria da Interface Clássico--Quântica na GDQ

## 1. Função deste documento

Este documento inicia a formulação geral da teoria da medida na
Geometrodinâmica Quântica (GDQ).

Seu objetivo é construir, a partir da ação oficial, a interação entre:

1. uma excitação coerente microscópica;
2. um aparelho macroscópico;
3. a interface física que correlaciona ambos;
4. a amplificação que produz um registro clássico.

A hipótese central é:

> Uma medição GDQ é uma transição de estabilidade na interface entre uma
> excitação coerente e um sistema macroscópico. A resposta causal do aparelho
> quebra uma degenerescência do módulo interno do objeto, amplifica a resposta
> e produz registros geometricamente metastáveis.

Este texto é um documento de fundamentação e programa de derivação. Ele não
declara antecipadamente demonstrados os coeficientes dinâmicos de um detector
real.

---

## 2. Princípio de unidade ontológica

A GDQ não postula dois tipos fundamentais de matéria, um clássico e outro
quântico. O objeto e o aparelho são configurações da mesma geometria e obedecem
à mesma ação oficial.

A distinção clássico--quântico é uma distinção de regime:

\[
\boxed{
\text{quântico e clássico são reduções de escala e estabilidade da mesma GDQ.}
}
\]

No regime quântico, permanecem observáveis a coerência de fase, a topologia do
defeito, a circulação e os modos internos. No regime clássico, o observador
acompanha apenas poucos modos coletivos robustos de um sistema com muitos graus
de liberdade.

Assim, a teoria não deve introduzir uma ação clássica independente para o
aparelho e outra ação fundamental para o objeto.

---

## 3. Ação oficial e decomposição do domínio

A ação física fundamental permanece:

\[
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
\]

Seja o domínio físico relevante decomposto como

\[
\mathcal M=\Omega_Q\cup_{\Sigma}\Omega_A,
\]

onde:

- \(\Omega_Q\) é a região coerente associada ao objeto;
- \(\Omega_A\) contém os graus de liberdade do aparelho;
- \(\Sigma\) é a interface comum;
- \(\varphi=\Phi|_\Sigma\) representa os dados de traço dos campos;
- \(\Phi=(g,f,\bar f,B,\ldots)\) denota os campos relevantes da GDQ.

A escrita

\[
\mathcal S_{\rm GDQ}[\mathcal M]
=\mathcal S_{\rm GDQ}[\Omega_Q]
+\mathcal S_{\rm GDQ}[\Omega_A]
+\mathcal S_{\rm cola}[\Sigma]
\]

é uma decomposição da mesma ação. Não representa três teorias independentes.
O termo de cola deve ser obtido pela completação variacional e pelas condições
de compatibilidade dos dois lados.

Fontes externas controladas pelo experimentalista podem ser representadas por

\[
\mathcal S_{\rm fonte}[\Phi,J_A],
\]

desde que \(J_A\) seja definido por grandezas clássicas do aparelho e não por
projetores quânticos inseridos manualmente.

---

## 4. Definição operacional dos regimes

### 4.1 Regime quântico

Uma região pertence ao regime quântico quando modos internos coerentes,
holonomias e fases possuem tempos de vida comparáveis ou superiores ao tempo
de interação e podem alterar observáveis.

Características esperadas:

- espectro interno discreto;
- baixa dispersão de fase;
- sensibilidade a contornos e holonomias;
- poucos modos internos relevantes;
- circulação e topologia resolvíveis experimentalmente.

### 4.2 Regime clássico

Um aparelho macroscópico é uma configuração GDQ com:

- grande número de graus de liberdade;
- espectro efetivamente denso;
- modos microscópicos não resolvidos;
- forte separação entre escalas rápidas e variáveis coletivas;
- bacias de atração macroscópicas;
- registros metastáveis e redundantes.

Escreve-se:

\[
\Phi_A
=\Phi_A^{\rm macro}(X^a)+\delta\Phi_A^{\rm micro},
\]

onde \(X^a\) pode representar posição do ponteiro, magnetização, corrente,
carga registrada ou outro modo coletivo.

### 4.3 Regime de interface

A interface é o regime em que os modos coerentes do objeto e os modos
coletivos do aparelho possuem acoplamento espectral não desprezível.

Um critério quantitativo deverá ser formulado com a Hessiana e os operadores
de resposta. Não se adotará, antes da análise dimensional, um número arbitrário
baseado apenas em \(|\nabla f|\) ou \(|\nabla\nabla f|\).

---

## 5. Definição de medição

Uma interação constitui medição quando produz simultaneamente:

1. **correlação:** o estado geométrico do objeto modifica uma variável do
   aparelho;
2. **discriminação:** diferentes setores do objeto conduzem a respostas
   distinguíveis;
3. **amplificação:** a diferença microscópica é convertida em separação
   macroscópica;
4. **estabilidade:** os registros pertencem a bacias de atração persistentes;
5. **legibilidade:** existe um observável macroscópico que identifica a bacia;
6. **consistência estatística:** repetições reproduzem as frequências previstas.

Portanto:

\[
\text{interação comum}\not\Rightarrow\text{medição}.
\]

Uma interação que não amplifica nem registra pode produzir espalhamento,
deformação ou emaranhamento sem constituir uma medida completa.

---

## 6. Princípio variacional da interface

Ao variar a ação decomposta, a forma geral deve ser:

\[
\delta\mathcal S
=\int_{\Omega_Q}E_Q(\Phi)\,\delta\Phi
+\int_{\Omega_A}E_A(\Phi)\,\delta\Phi
+\int_\Sigma(\Pi_Q+\Pi_A)\,\delta\varphi.
\]

As equações bulk são:

\[
E_Q(\Phi)=0,
\qquad
E_A(\Phi)=0.
\]

A condição de colagem variacional é:

\[
\boxed{\Pi_Q+\Pi_A=0.}
\]

Depois de resolver os campos internos em função do traço \(\varphi\), definem-se
os operadores Dirichlet--to--Neumann:

\[
\Pi_Q=\Lambda_Q\varphi,
\qquad
\Pi_A=\Lambda_A\varphi-J_A.
\]

Logo, a equação reduzida da interface é:

\[
\boxed{(\Lambda_Q+\Lambda_A)\varphi=J_A.}
\]

Interpretação:

- \(\Lambda_Q\): resposta interna do objeto;
- \(\Lambda_A\): impedância geométrica do aparelho;
- \(J_A\): fonte controlada externamente;
- \(\varphi\): configuração comum selecionada pela colagem.

Uma condição Robin local é uma aproximação de baixa energia para
\(\Lambda_A\), e não deve ser postulada como estrutura fundamental.

---

## 7. Hessiana acoplada e resposta efetiva

Linearizando em torno de um background estacionário conjunto:

\[
\Phi=\Phi_*+\delta\Phi,
\]

a segunda variação possui a forma de blocos:

\[
\delta^2\mathcal S
=\frac12
\begin{pmatrix}q\\a\end{pmatrix}^{T}
\begin{pmatrix}
K_Q & J\\
J^\dagger & K_A
\end{pmatrix}
\begin{pmatrix}q\\a\end{pmatrix}.
\]

Aqui:

- \(q\) são perturbações físicas do objeto;
- \(a\) são perturbações do aparelho;
- \(K_Q\) e \(K_A\) são Hessianas gauge-fixadas;
- \(J\) é o acoplamento da interface.

Eliminando linearmente os modos do aparelho:

\[
a=-K_A^{-1}J^\dagger q,
\]

obtém-se o complemento de Schur:

\[
\boxed{K_{\rm eff}^{Q}=K_Q-JK_A^{-1}J^\dagger.}
\]

Esse operador deve determinar:

- deslocamento dos canais;
- levantamento de degenerescência;
- rigidez localizada;
- susceptibilidade;
- limiar de instabilidade;
- resposta adiabática e não adiabática.

Modos zero de difeomorfismo, calibre e isometrias globais devem ser projetados
antes da inversão de \(K_A\).

---

## 8. Resposta causal, dissipação e ruído

A resposta física do aparelho não é dada por uma inversa elíptica arbitrária,
mas pelo kernel causal apropriado:

\[
G_A^{\rm ret}(\omega)
=\left(K_A(\omega)+i0^+\right)^{-1}.
\]

Em termos gerais:

\[
\operatorname{Re}G_A^{\rm ret}
\longrightarrow\text{deslocamento e rigidez},
\]

\[
\operatorname{Im}G_A^{\rm ret}
\longrightarrow\text{absorção, largura e relaxação}.
\]

Ao eliminar graus microscópicos do aparelho, espera-se uma equação de
Langevin generalizada:

\[
\dot q(t)
=-\int_0^t\mathcal K(t-s)q(s)\,ds+\xi(t).
\]

O Capítulo 21 fornece as rotas de Fano, NESS e Zwanzig--Mori que devem ser
reaproveitadas. Contudo, o kernel \(\mathcal K\) e a força \(\xi\) precisam ser
derivados para o background e o aparelho concretos.

Em equilíbrio térmico, deverá ser verificada uma relação de
flutuação--dissipação. No limite Markoviano:

\[
\dot q=-\Gamma q+\xi.
\]

Assim:

\[
\boxed{
\Gamma_{\rm medida}
=\Gamma_{\rm GDQ}
[\Phi_Q,\Phi_A,\Sigma,T,J_A].
}
\]

\(\Gamma_{\rm medida}\) não é uma constante universal isolada. Ela depende do
objeto, do aparelho, da temperatura, da geometria e do protocolo experimental.

---

## 9. Relaxação e formação de registro

A Hessiana fornece rigidez, mas não fixa sozinha uma escala temporal.
Introduzindo a mobilidade causal \(\mathbb M\):

\[
\partial_t\delta\Phi
=-\mathbb M\mathbb H_{\rm eff}\delta\Phi+\xi.
\]

O tempo de relaxamento é controlado por:

\[
\boxed{
\tau_{\rm relax}^{-1}
=\min\operatorname{Re}
\operatorname{spec}(\mathbb M\mathbb H_{\rm eff}).
}
\]

Um registro clássico corresponde a uma bacia metastável do funcional efetivo,
com tempo de permanência muito maior que o tempo de leitura:

\[
\tau_{\rm registro}\gg\tau_{\rm leitura}\gg\tau_{\rm relax}.
\]

A monotonicidade de Perelman pode contribuir para a estabilidade do fluxo,
mas não substitui a derivação da dissipação e da amplificação macroscópica.

---

## 10. Stern--Gerlach como modelo mínimo

### 10.1 Estrutura intrínseca do objeto

Os Capítulos 9, 11 e 34 e a Questão 42 fornecem, em níveis complementares:

- spin como circulação/torção;
- holonomia semi-inteira;
- representação dupla;
- módulo de orientações de Hopf;
- projetor global:

\[
P=uu^\dagger\in\mathbb{CP}^1.
\]

O aparelho não cria o spin nem os dois ramos.

### 10.2 Papel do eletroímã

O campo clássico fornece o eixo:

\[
\mathbf n=\frac{\mathbf B}{|\mathbf B|}.
\]

Ele quebra a simetria rotacional do módulo de orientações. A forma efetiva de
menor ordem permitida pela simetria axial deve ser derivada, e não postulada,
mas espera-se a estrutura:

\[
\mathcal F_\Sigma(P;\mathbf B)
=F_0(|\mathbf B|)
-\mu_{\rm GDQ}(|\mathbf B|)
\,\mathbf n\cdot\mathbf a(P)+\cdots.
\]

Se essa forma vier da ação, seus pontos estacionários serão:

\[
\mathbf a=+\mathbf n,
\qquad
\mathbf a=-\mathbf n.
\]

Os dois canais resultam então da combinação entre:

1. estrutura semi-inteira intrínseca;
2. módulo de Hopf;
3. anisotropia clássica do aparelho;
4. estabilidade da Hessiana de interface.

### 10.3 Quantidades a derivar

Para um Stern--Gerlach real, a teoria deve calcular:

- \(\Lambda_Q\) do estômato;
- \(\Lambda_A\) do eletroímã/material;
- fonte clássica \(J_A(\mathbf B,\nabla\mathbf B)\);
- momento efetivo \(\mu_{\rm GDQ}\);
- rigidez localizada \(\kappa_H^{\rm SG}\);
- largura/relaxação \(\Gamma_{\rm SG}\);
- tempo de seleção;
- força e separação espacial;
- formato e largura das manchas;
- regime não adiabático.

Os valores de \(\mathbf B\), \(\nabla\mathbf B\), temperatura, comprimento e
velocidade são dados do experimento, não constantes universais que a GDQ deva
prever.

---

## 11. Estatística de resultados e regra de Born

É necessário separar:

\[
\boxed{
\text{decoerência}\neq
\text{amplificação}\neq
\text{seleção individual}.
}
\]

A Questão 42 mostrou a seguinte estrutura condicional. Seja

\[
p_t=\operatorname{Tr}(\rho_tP_+).
\]

Se \(p_t\) for um martingal limitado e a dinâmica produzir absorção quase
certa em \(p_\infty\in\{0,1\}\), então:

\[
\Pr(p_\infty=1)
=\mathbb E[p_\infty]
=\mathbb E[p_0]
=p_0.
\]

Para transformar isso em teorema intrínseco da GDQ, é preciso derivar:

1. o processo condicionado a partir do aparelho;
2. a propriedade de martingal;
3. a ausência de drift que altere as probabilidades;
4. a absorção nos dois registros;
5. a captura quase certa;
6. a relação entre o sinal macroscópico e a inovação estocástica.

Escrever \(p=\operatorname{Tr}(\rho P)\) não é, isoladamente, uma derivação da
regra de Born.

---

## 12. Emaranhamento e condições globais

A teoria local de um objeto e um aparelho deve ser concluída antes de promover
pontes, tubos de fluxo ou condições futuras a fundamentos da medição.

Para sistemas multipartidos, será necessário construir:

\[
\mathcal M_{AB},
\qquad
\mathbb H_{AB},
\qquad
\Lambda_{AB},
\]

e demonstrar:

- correlações de Bell;
- independência das escolhas dos aparelhos;
- no-signalling;
- compatibilidade com causalidade relativística;
- impossibilidade de controle superluminal do resultado.

Um problema de contorno global não é automaticamente uma dinâmica causal.
Condições futuras e escolha retardada permanecem rotas de pesquisa até que
existência, unicidade e estabilidade sejam demonstradas.

---

## 13. Critérios de fechamento da teoria de interface

A teoria será considerada estruturalmente fechada quando demonstrar:

1. decomposição variacional da ação sem alteração do funcional oficial;
2. operador de interface derivado;
3. critério espectral clássico--quântico;
4. complemento de Schur físico com gauges removidos;
5. resposta causal e mobilidade;
6. amplificação e registros metastáveis;
7. processo condicionado e Born;
8. limite Pauli/Dirac/Lindblad;
9. aplicação a pelo menos dois tipos distintos de detector.

Será considerada preditivamente fechada em um experimento quando, além disso:

1. os parâmetros universais forem fixados antes da comparação;
2. os dados do aparelho forem apenas entradas experimentais legítimas;
3. houver convergência numérica;
4. forem previstas curvas e tempos, não apenas um número;
5. existir ao menos uma previsão falseável que não tenha sido usada na
   construção.

---

## 14. Programa de trabalho imediato

### Etapa 1 — Modelo mínimo de Stern--Gerlach

Construir:

\[
\boxed{
\text{objeto Hopf Q42}
+\text{modo coletivo de magnetização}
+\text{banho GDQ do aparelho}.
}
\]

### Etapa 2 — Derivação variacional

1. escolher o background conjunto;
2. definir fontes clássicas do eletroímã;
3. variar a ação nos dois domínios;
4. extrair \(\Pi_Q,\Pi_A,\Lambda_Q,\Lambda_A\);
5. calcular o acoplamento \(J\).

### Etapa 3 — Resposta e redução

1. construir a Hessiana em blocos;
2. remover modos de gauge e isometrias;
3. calcular o complemento de Schur;
4. obter o kernel retardado;
5. derivar rigidez, dissipação e ruído.

### Etapa 4 — Registro e estatística

1. identificar as bacias \(+\) e \(-\);
2. calcular o tempo de captura;
3. derivar o sinal macroscópico;
4. obter o processo condicionado;
5. verificar Born e sequências de medidas.

### Etapa 5 — Validação

1. recuperar o limite operacional de Stern--Gerlach;
2. comparar com os scripts da Q42;
3. substituir parâmetros reduzidos por coeficientes derivados;
4. procurar uma correção experimental específica da GDQ.

---

## 15. Status atual

\[
\boxed{
\text{Arquitetura conceitual consolidada; derivação variacional da interface
é o próximo bloco matemático.}
}
\]

O primeiro alvo técnico é:

\[
\boxed{
J_A^{\rm clássico}
\longrightarrow
\mathsf R_{\rm app}
\quad\text{pela variação da ação oficial, sem inserir Pauli manualmente.}
}
\]

Esse primeiro alvo foi estruturado em
`topicos/medida_interface/derivacao_fonte_classica_interface_sg.md`. O acoplamento fundamental foi
reescrito como contração gauge-invariante entre a torção do objeto e a
curvatura clássica do aparelho. O próximo alvo é a Hessiana dinâmica do
aparelho mínimo e seu kernel retardado.

O aparelho mínimo e o kernel foram estruturados em
`topicos/medida_interface/modelo_aparelho_minimo_gdq.md`. Os coeficientes do potencial do ponteiro, do
acoplamento e do banho foram definidos como projeções das variações da ação
oficial. O próximo passo é derivar condições suficientes para captura e Born
na Rota A e, depois, escolher um detector concreto para avaliação numérica.

A Rota A foi concluída em `topicos/medida_interface/teorema_captura_born_interface_gdq.md`. A equação
estocástica de captura foi derivada por filtragem causal do registro, seu
martingal foi demonstrado e a captura foi identificada como assintótica, com
limiar físico finito. O próximo bloco é a Rota B: calcular a taxa informacional
de um aparelho especificado.

A primeira Rota B foi construída em `topicos/medida_interface/detector_ohmico_gdq.md`. Um canal
geométrico semi-infinito possui DtN retardado exatamente ôhmico e fornece
mobilidade, ruído e a taxa informacional
\(\Gamma_A=g_X^2/(8\gamma_Ak_BT_A)\) no regime clássico ideal. Permanecem a
avaliação geométrica de \(g_X,\zeta_A,c_A\) e a modelagem de um material real.

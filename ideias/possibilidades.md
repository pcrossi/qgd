# Possibilidades futuras da GDQ

Este documento registra ideias que não devem entrar como resultados oficiais
da formulação atual, mas que podem ser revisitadas como rotas técnicas futuras.

---

## 1. Rota Atiyah--Singer para seleção de \(n=4\)

### Ideia

Nada impede, em princípio, que a dimensão complexa quatro da GDQ venha a ser
justificada por um argumento de índice/anomalias baseado no Teorema do Índice
de Atiyah--Singer.

Na formulação oficial atual, a variedade fundamental é:

\[
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}M=8,
\qquad
\dim_{\mathbb C}M=4.
\]

Até que uma prova seja construída, \(n=4\) deve permanecer como axioma
estrutural. A rota Atiyah--Singer deve ser tratada como programa posterior,
não como resultado já demonstrado.

### Formulação possível

O objeto natural a estudar seria um operador de Dirac com torção e acoplamento
de calibre:

\[
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{LC}
+\frac18 B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA^a_\mu
\right).
\]

O problema seria avaliar o índice quiral de um operador do tipo:

\[
\slashed D_{B,A}^+:
\Gamma(S^+\otimes E)
\longrightarrow
\Gamma(S^-\otimes E),
\]

onde:

- \(S^\pm\) são os fibrados espinoriais quirais;
- \(E\) é o fibrado de calibre/matéria;
- \(B\) é a 3-forma torsional;
- \(A\) é a conexão de gauge.

### Obstáculo principal

O bulk oficial:

\[
M=\mathbb R^4\times T^4
\]

não é compacto. Portanto, o índice global usual em variedade compacta não se
aplica automaticamente.

Uma prova futura teria de escolher uma das seguintes rotas:

1. compactificação controlada do setor \(\mathbb R^4\);
2. condições de decaimento no infinito;
3. índice relativo;
4. índice APS com bordo;
5. índice de Callias;
6. aplicação do índice apenas ao setor interno compacto \(T^4\);
7. formulação em célula fundamental com condições periódicas/físicas bem
   definidas.

### Dados que ainda precisam ser fixados

Para a rota se tornar uma prova, é necessário especificar:

1. o operador exato;
2. o domínio funcional;
3. as condições de contorno ou decaimento;
4. o fibrado espinorial;
5. o fibrado \(E\);
6. o grupo de gauge efetivo;
7. as representações dos campos;
8. quais férmions são quirais;
9. o polinômio de anomalia;
10. como a torção de Bismut modifica ou não modifica o índice topológico;
11. por que \(n=4\) cancela as anomalias;
12. por que as demais dimensões candidatas falham.

### Status

\[
\boxed{
\text{Rota aberta, compatível com a GDQ, mas ainda não demonstrada.}
}
\]

Essa possibilidade não deve substituir a resposta oficial atual da Questão 3:

\[
\boxed{
n=4 \text{ é axioma estrutural da GDQ atual.}
}
\]

---

## 2. Observação sobre a versão antiga em \(K3\times(S^1\times S^3)\)

A tentativa antiga baseada em:

\[
K3\times(S^1\times S^3)
\]

não deve ser usada como prova da Questão 3 na formulação atual, porque a
Questão 2 fixou a geometria oficial como:

\[
M=\mathbb R^4\times T^4.
\]

Qualquer aplicação futura de Atiyah--Singer precisa ser reconstruída sobre
\(\mathbb R^4\times T^4\), não sobre a geometria descartada.

---

## 3. Teorema futuro de assintoticidade da medição/decoerência

### Ideia

A Questão 24 fecha estruturalmente o modelo de medição por acoplamento:

\[
S+A+E,
\]

com registros \(R_i\), decoerência, probabilidades e repetibilidade. Porém,
ficou apenas assumida/modelada a assintoticidade forte dos registros:

\[
\langle R_j(t)|R_i(t)\rangle\to0,
\qquad i\ne j,
\]

ou, equivalentemente:

\[
\rho_{SA}(t)
\to
\sum_i P(i)\,|s_i,A_i\rangle\langle s_i,A_i|.
\]

Uma rota futura seria transformar isso em teorema.

### Formulação possível

Definir uma dinâmica reduzida para aparelho+ambiente:

\[
\frac{d\rho_{SA}}{dt}
=
\mathcal L(\rho_{SA}),
\]

onde \(\mathcal L\) pode ser:

1. gerador de Lindblad efetivo;
2. operador de Fokker--Planck geométrico;
3. fluxo de Perelman/Bismut projetado;
4. gerador híbrido de transporte + dissipação.

O objetivo seria provar que os estados de registro \(R_i\) são atratores
assintoticamente estáveis:

\[
\mathcal L(\rho_i)=0,
\qquad
\rho_i=|s_i,A_i\rangle\langle s_i,A_i|,
\]

e que os termos fora da diagonal decaem:

\[
\rho_{ij}(t)
=
\rho_{ij}(0)e^{-\Gamma_{ij}t},
\qquad
\Gamma_{ij}>0,
\qquad
i\ne j.
\]

Então:

\[
\boxed{
\lim_{t\to\infty}\rho_{ij}(t)=0,
\qquad i\ne j.
}
\]

### Formulação geométrica equivalente

Em linguagem GDQ, o teorema poderia ser expresso por bacias geométricas
\(U_i\) do aparelho:

\[
R_i \leftrightarrow U_i.
\]

Para cada bacia, existiria um ponto crítico/atrator:

\[
\mathfrak S_i=(g_i,B_i,f_i),
\]

com:

\[
\nabla \mathcal W_T(\mathfrak S_i)=0
\]

e Hessiana positiva no setor físico:

\[
\operatorname{spec}
\left(
\mathcal J_{\mathfrak S_i}
\big|_{\mathcal H_{\rm phys}}
\right)
\subseteq[0,\infty).
\]

Com gap espectral estritamente positivo fora dos modos de simetria:

\[
\lambda_1^{(i)}>0.
\]

Nesse caso, uma perturbação dentro da bacia \(U_i\) satisfaria:

\[
d(\Phi_t,\mathfrak S_i)
\le
C e^{-\lambda_1^{(i)}t}d(\Phi_0,\mathfrak S_i),
\]

e os diferentes registros ficariam assintoticamente ortogonais:

\[
\langle R_i(t),R_j(t)\rangle
\le
C_{ij}e^{-\Gamma_{ij}t},
\qquad i\ne j.
\]

### Dados necessários para transformar em prova

Para essa rota virar resultado oficial, ainda seria necessário especificar:

1. o gerador efetivo \(\mathcal L\);
2. o domínio funcional;
3. a topologia/norma usada para convergência;
4. os estados de ponteiro \(R_i\);
5. as bacias \(U_i\);
6. o funcional de Lyapunov;
7. o operador de Jacobi/Hessiano em cada bacia;
8. o gap decoerente \(\Gamma_{ij}\);
9. a remoção de modos zero de gauge/simetria;
10. a prova de inexistência de canais de recoerência macroscópica no regime
    considerado.

### Status

\[
\boxed{
\text{Rota aberta para fortalecer a Questão 24; ainda não é resultado oficial.}
}
\]

No estado atual, a Questão 24 estabelece a estrutura de medição e a
assintoticidade como hipótese/modelagem física. O teorema acima seria a versão
matemática forte a demonstrar futuramente.

---

## 4. Q26 — seleção dinâmica do setor spinorial e realização solitônica

### O que foi fechado

A Questão 26 está fechada estruturalmente via fibrado spin, álgebra de
Clifford e representação de:

\[
\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C).
\]

Também foi fechada a formulação complementar por Hopf--Cauchy em
`questoes/q26/associados/spin_hopf_residuo_cauchy.md`.

Em uma carta complexa transversal ao estômato, a seção spinorial local é:

\[
s(z)=z^{1/2}s_0(z),
\]

logo:

\[
\Omega_S=d\log s
=
\frac12\frac{dz}{z}+d\log s_0,
\qquad
\operatorname{Res}_{z=0}\Omega_S=\frac12.
\]

Pelo teorema de Cauchy:

\[
\frac{1}{2\pi i}\oint_\gamma\Omega_S=\frac12.
\]

Na fase física:

\[
\oint_\gamma dS_R=\frac h2=\pi\hbar,
\qquad
\exp\left(
\frac{i}{\hbar}\oint_\gamma dS_R
\right)=-1.
\]

Portanto:

\[
2\pi\mapsto -1,
\qquad
4\pi\mapsto +1.
\]

Isso realiza a mesma estrutura da fibração de Hopf:

\[
S^1\hookrightarrow S^3\to S^2,
\qquad
S^3\simeq SU(2)\to SO(3).
\]

Logo, Hopf/resíduos não é mais falta da Q26.

### Possibilidade futura

O programa posterior não é provar novamente spin \(1/2\). O que ainda pode ser
desenvolvido é a seleção dinâmica do setor spinorial completo:

1. derivar pela ação oficial qual das 16 estruturas spin de \(T^4\) é
   selecionada por um background físico;
2. construir explicitamente o solíton que realiza o setor de Dirac do elétron;
3. verificar estabilidade dos modos espinoriais no operador de Dirac--Bismut
   efetivo;
4. conectar simultaneamente spin, massa, carga e espectro completo no mesmo
   background;
5. entender se integrações toroidais específicas apenas reproduzem a
   meia-monodromia já provada ou se selecionam estruturas spin distintas.

Esse programa pertence a `ideias/possibilidades.md` porque não reabre a Q26.
Ele é uma expansão espectral/solitônica, não uma falta estrutural.

### Status

\[
\boxed{
\text{Q26 fechada; seleção dinâmica do setor spinorial fica como possibilidade
futura.}
}
\]

---

## Compactificação cosmológica \(T^5\times S^3\) para o cálculo de \(\alpha\)

### Ideia

A geometria local oficial da GDQ permanece:

\[
M=\mathbb R^4\times T^4.
\]

Entretanto, para cálculos globais de cosmologia e de invariantes integrados,
pode-se investigar uma representação compactificada:

\[
\mathcal M_{\rm cosmo}
=
T^5\times S^3
\simeq
(S^1_{\rm tempo}\times S^3_{\rm espaço})\times T^4_{\rm interno}.
\]

Essa estrutura deve ser interpretada como compactificação cosmológica do
espaço de Einstein, não como substituição da ação oficial nem da geometria
local de propagação.

### Uso pretendido

A rota pode ser usada futuramente para reavaliar a derivação de \(\alpha\)
por invariantes globais:

\[
\alpha
\stackrel{?}{=}
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
\]

Nessa leitura:

1. \(S^3\) representa o espaço cosmológico fechado de Einstein;
2. o \(S^1\) adicional representa ciclo temporal/euclidiano ou térmico;
3. \(T^4\) preserva o setor interno oficial;
4. \(T^5=S^1\times T^4\) aparece apenas na representação global;
5. a ação GDQ continua independente da escolha de coordenadas.

### O que precisa ser provado

Para essa rota virar resultado oficial, ainda é necessário:

1. mostrar a passagem rigorosa de \(\mathbb R^4\times T^4\) para
   \((S^1\times S^3)\times T^4\) como compactificação cosmológica;
2. provar que os invariantes usados no cálculo de \(\alpha\) são invariantes
   físicos da ação de contorno, e não artefatos de coordenadas;
3. justificar o fator \(1920\) sem usar característica de Euler incorreta;
4. derivar \(\kappa_{\rm Kähler}=9/(8\pi^4)\) da dinâmica ou de uma
   normalização geométrica inevitável;
5. conectar o acoplamento global obtido com a normalização local do setor
   \(U(1)\) em \(\mathbb R^4\times T^4\);
6. separar claramente cosmologia global de dinâmica local.

### Status

\[
\boxed{
\text{Rota futura para }\alpha\text{; compatível como compactificação
cosmológica auxiliar, mas ainda não é prova fechada.}
}
\]

### Atualização — refinamento DtN warped--Bismut

A normalização dos geradores corrigiu a comparação entre a norma radial e o
coeficiente eletromagnético. O teste sem ajuste
`questoes/q37/associados/teste_schur_dtn_global.py` combinou o kernel fotônico canonizado, a
impedância DtN do primeiro harmônico em duas extensões pela 4-bola e o
complemento de Schur de uma interface passiva.

Na aproximação redonda,

\[
K_\partial^{\rm DtN}=\pi^2R^2,
\]

e foi obtido

\[
\alpha_{\rm DtN}^{-1}=137{,}604601779,
\]

com erro de $0{,}414868\%$ em $Z_Q$ diante da fórmula cosmológica e Hessiana
positiva. Nenhum valor de $\alpha$ entrou no cálculo.

O refinamento futuro consiste em substituir o DtN redondo pelo operador DtN
da Hessiana Hermitiano--Bismut na direção normal $r$ do preenchimento

\[
B^4_R\subset\mathbb C^2,
\qquad
\partial B^4_R=S^3_R.
\]

Deve-se derivar

\[
L_r^{\rm phys}
=-\frac1{w_r}\partial_r(p_r\partial_r)+V_r
\]

e calcular

\[
\Lambda_{\rm DtN}^{\rm WB}\phi
=p_r(R)\partial_r\Psi_\phi(R).
\]

O Sturm--Liouville existente em $\chi$ não realiza esse cálculo, pois $\chi$
é tangencial em $S^3$, enquanto $r$ é normal ao elo. O resultado redondo fica
preservado como estimativa geométrica suficiente; o refinamento não deve ser
obtido ajustando a diferença restante.

## Potencial cotangente em \(S^3\) para calibração de massas

### Ideia

A interação local de laboratório aparece com potencial Kepler/Coulomb:

\[
V_{\rm loc}(r)\propto \frac1r.
\]

Mas essa é a aproximação plana do potencial em uma seção espacial global
fechada \(S^3\). No espaço cosmológico de Einstein, o Green esférico natural
tem forma cotangente:

\[
\boxed{
V_{S^3}(r)
\propto
\frac1R\cot\left(\frac rR\right).
}
\]

No limite \(r\ll R\):

\[
\frac1R\cot\left(\frac rR\right)
=
\frac1r-\frac{r}{3R^2}+O(r^3/R^4).
\]

### Consequência

1. \(1/r\) é correto para física local e espectroscopia de laboratório;
2. \(\cot(r/R)/R\) é o candidato correto para calibração global de massas;
3. os volumes e tensões relevantes devem ser avaliados em
   \(T^5\times S^3\), não no plano tangente \(\mathbb R^4\times T^4\);
4. a ação oficial permanece inalterada; muda apenas o background usado para
   avaliar o operador espectral.

## Extensão global da hierarquia leptônica

### Estado atual

A Q39 foi promovida a teorema condicional da hierarquia leptônica no domínio
reduzido intrínseco e no background leptônico 8D estacionário produto/bloco:

\[
g_8=g_B\oplus g_K,
\qquad
A(k)=\mathrm{const},
\qquad
f_K(k)=\mathrm{const},
\qquad
H_{BK}=0,
\qquad
\mathcal C_{BK}=0.
\]

Nesse caso:

\[
a_W=a_f=a_H=\varepsilon=0,
\qquad
\lambda_B^{\rm gap}=\frac12,
\]

e o complemento de Schur é nulo:

\[
\Delta_{\rm Schur}=0.
\]

Logo a hierarquia 8D coincide exatamente com a hierarquia reduzida
intrínseca.

### Possibilidade futura

A extensão global consiste em testar se o mesmo teorema persiste em
backgrounds mais ricos. Um background warped/misto real seria uma solução
estacionária 8D na qual o setor interno deixa de ser apenas espectador e
acopla dinamicamente ao setor de massa. A forma mínima é:

\[
g_8=e^{2A(k)}g_B\oplus g_K+\varepsilon\mathcal C_{BK},
\]

com pelo menos um dos seguintes canais não nulo:

\[
\nabla_KA\ne0,
\qquad
\nabla_Kf_K\ne0,
\qquad
H_{BK}\ne0,
\qquad
\mathcal C_{BK}\ne0.
\]

Isso produziria um bloco misto na Hessiana:

\[
H_8=
\begin{pmatrix}
H_B & J\\
J^\dagger & H_\perp
\end{pmatrix},
\qquad
J\ne0,
\]

e massas efetivas:

\[
H_B^{\rm eff}=H_B-JH_\perp^{-1}J^\dagger.
\]

### Critério de aceitação

Antes de usar qualquer deslocamento de massa, deve-se calcular diretamente no
background estacionário:

\[
a_W=\|\nabla_KA\|_\infty,
\qquad
a_f=\|\nabla_Kf_K\|_\infty,
\qquad
a_H=\|H_{BK}\|_\infty,
\qquad
\varepsilon=\|\mathcal C_{BK}\|.
\]

Então aplicar o critério:

\[
\frac{j_{\rm mix}^2}{m_\perp^2}
<
\lambda_B^{\rm gap}.
\]

Se for subcrítico, a hierarquia de três setores permanece estável. Se for
crítico ou supercrítico, o modo adicional deve ser classificado como
ressonância, estado de contorno, excitação ou composto até prova independente
de carga primitiva e estabilidade assintótica.

### Regra

Esse programa futuro não reabre a Q39 no background produto. Ele serve para
testar a extensão global do teorema condicional da hierarquia leptônica em
soluções 8D mais ricas, backgrounds térmicos, canais massless ou contornos
não homogêneos.

---

## Expansão do teorema condicional da ponte global--local

### Estado atual

A ponte global--local não é axioma da GDQ. Ela está formulada como teorema
condicional de seis lemas:

1. construção da família geométrica apontada;
2. convergência geométrica para o bulk local;
3. transporte de \(g,J,H,f,\mathcal U\) e da Hessiana física projetada;
4. localização e gap uniforme dos modos ligados;
5. convergência de resolventes e projetores de Riesz;
6. separação entre dados herdados e dados que exigem cálculo próprio.

Na classe estacionária gaussiana \(C_3\), as hipóteses foram verificadas e o
teorema está aplicado. O gap físico usado é:

\[
\Delta_0
=
\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0,
\]

com \(\Delta_0=1/2\) na normalização primitiva para \(\tau=1\).

### Expansão possível

A expansão futura consiste em demonstrar a mesma herança para classes mais
gerais de backgrounds:

1. backgrounds warped/mistos reais;
2. estômatos não gaussianos;
3. canais massless ou de espalhamento;
4. contornos de aparelho não homogêneos;
5. backgrounds térmicos do espaço cosmológico de Einstein;
6. defeitos compostos ou multi-centros fora da classe \(C_3\).

Nesses casos, não basta invocar a ponte já aplicada. Deve-se provar novamente
as hipóteses de domínio:

\[
\Phi_\varepsilon\to\Phi_{\rm loc},
\qquad
q_\varepsilon\to q_{\rm loc},
\qquad
\Delta_\varepsilon\ge \Delta_0>0,
\]

e, no caso massless, substituir o argumento de modo ligado por normalização de
fluxo, DtN ou teoria de espalhamento.

### Critério de aceitação

Uma expansão da ponte só deve ser aceita quando fornecer:

1. domínio e contorno explícitos;
2. mapa de transporte dos campos e da medida;
3. projetor físico que remova gauge, normalização e modos de Noether;
4. forma quadrática convergente;
5. gap uniforme ou substituto massless bem posto;
6. convergência de projetores/observáveis;
7. lista dos dados herdados e dos dados não herdados.

### Regra

Esta rota não reabre a ponte global--local já aplicada à classe \(C_3\). Ela
serve para generalizar o teorema condicional a novos backgrounds sem promover
essas generalizações a axiomas.

---

## Q43 — Refinamento metrológico futuro de Zeeman e \(g-2\)

### Estado atual

A Questão 43 está fechada estrutural e operacionalmente:

1. a forma Zeeman foi derivada por Noether, isotropia e fonte externa;
2. o termo mínimo \(g_0=2\) foi identificado;
3. o termo líder foi obtido como:

\[
a^{(1)}=\frac{\alpha}{2\pi};
\]

4. a regra de seleção de Hodge elimina uma fonte superior linear universal;
5. o operador condicional da anomalia foi formulado como resposta da Hessiana
   física:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
\]

Logo, o item futuro não é “resolver Q43” novamente.

### Possibilidade futura

O refinamento metrológico completo deve vir de:

1. construir o background leptônico 8D físico não homogêneo/warped/misto, se
   necessário;
2. calcular \(J_\ell^{(\beta)}\) a partir do contorno térmico escolhido;
3. obter \(\delta_T H_C\) e \(\delta_T m_\perp\);
4. avaliar o canal mediado por densidade \(\operatorname{Re}f\), incluindo
   terceira e quarta variações da ação oficial;
5. reavaliar \(a_\ell(T)\) sem usar \(g-2\) experimental como alvo.

### Regra

Essa possibilidade não reabre Q43. Ela é refinamento metrológico futuro, pois
a estrutura Zeeman, \(g_0=2\), o termo líder \(\alpha/(2\pi)\), a seleção de
canal e o operador de resposta já foram estabelecidos no formalismo GDQ.

---

## Q25 — Refinamentos futuros do benchmark do problema do sinal

### Estado atual

A Questão 25 foi fechada no escopo estrutural e operacional reduzido:

1. a medida GDQ positiva foi preservada;
2. a antissimetria fermiônica foi armazenada como holonomia
   \(\operatorname{Hol}(P_{ij})=-1\);
3. a decomposição em domínios e interfaces foi implementada;
4. o estimador holonômico positivo foi testado;
5. o benchmark físico reduzido foi executado;
6. a comparação com a Fig. 2D de Parsons et al. foi feita;
7. o ensemble térmico foi identificado;
8. a admitância térmica foi aproximada via complemento de Schur;
9. a correção espectral do banho explicou a maior parte da largura residual.

Portanto, essas tarefas não devem reabrir a Q25 como problema estrutural.

### Possibilidades futuras

Os refinamentos que ficam para trabalhos posteriores são:

1. extrair dados adicionais e mais precisos de Cheuk, Mazurenko e Koepsell;
2. redigitalizar a Fig. 2D de Parsons com ferramenta gráfica, incluindo barras
   de erro realistas;
3. derivar o resíduo final

\[
\Delta\Theta_A^{\rm residual}\simeq0.0296
\]

   por mobilidade causal, pesos térmicos reais do aparelho ou canais
   dissipativos omitidos;
4. substituir a Hessiana reduzida pela Hessiana completa do
   background/aparelho GDQ;
5. comparar também \(C_s(r)\), \(C_c(r)\), \(\xi_s\), fator de estrutura e
   perfis de polaron;
6. demonstrar uma cota analítica assintótica de variância/complexidade por
   classe de problema.

### Regra

Essas possibilidades são refinamentos metrológicos e assintóticos. Elas não
invalidam o fechamento estrutural da Q25: o resultado vigente é que a GDQ
possui uma rota positiva por holonomia e benchmark físico reduzido com acordo
fenomenológico parcial, sem reweighting de fase no escopo testado.

---

## Q45 — Comparação metrológica do efeito Hartman

### Estado atual

A Questão 45 foi fechada estruturalmente no setor evanescente unidimensional
reduzido. O efeito Hartman foi interpretado como saturação geométrica de
comprimento próprio:

$$
D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right),
$$

com tempo próprio efetivo:

$$
\tau_{\rm GDQ}(L)
=
\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

A relação $g_{xx}\propto\rho$ foi classificada como solução reduzida do canal
evanescente, não como identidade métrica universal. A velocidade de frente
permanece causal:

$$
v_{\rm front}\le c.
$$

### Possibilidades futuras

Para comparação experimental/metrológica, trabalhar depois:

1. escolher uma barreira física específica;
2. especificar o observável temporal usado: Wigner--Smith, Larmor,
   permanência, Büttiker--Landauer, chegada ou outro;
3. definir banda espectral do pulso e calcular a transmissão completa
   $T(E)A(E)$;
4. incluir reshaping de pico e separar isso da frente causal;
5. modelar o detector como fonte/contorno clássico no protocolo GDQ de
   interface;
6. comparar com dados experimentais sem usar o atraso observado para escolher
   parâmetros internos.

### Regra

Esse programa não reabre a Q45. Ele transforma a resposta estrutural em
previsão metrológica para um aparato concreto.

---

## Q46 — Aharonov--Bohm em aparatos reais

### Estado atual

A Questão 46 foi fechada estruturalmente no setor ideal de holonomia. A fase
Aharonov--Bohm é:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c},
$$

equivalentemente:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left[
\frac{iq\Phi}{\hbar c}
\right].
$$

O campo externo ideal satisfaz:

$$
F=dA=0
$$

no exterior do solenoide, mas a conexão é globalmente não trivial porque o
domínio é perfurado:

$$
\pi_1(M_{\rm ext})\simeq\mathbb Z.
$$

### Possibilidades futuras

Para procurar diferenças metrológicas da GDQ fora do limite ideal:

1. escolher um solenoide/blindagem real;
2. construir o contorno material do solenoide como fonte clássica/interface;
3. calcular a impedância de interface pela Hessiana oficial:

$$
\mathsf R_{\rm sol}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY};
$$

4. obter a correção:

$$
A_{\rm eff}
=
A_{\rm harm}
+\delta A_{\rm surf};
$$

5. avaliar efeitos em visibilidade, envelope, dispersão e atraso de fase;
6. comparar com dados sem usar a diferença observada como ajuste de
   $\mathsf R_{\rm sol}$.

### Regra

Esse programa não reabre a Q46. A fase topológica ideal e a invariância de
calibre já estão fechadas; aparatos reais pertencem ao refinamento
metrológico.

---

## Q47 — Casimir com materiais, temperatura e geometria real

### Estado atual

A Questão 47 foi fechada estruturalmente no limite de placas ideais. O valor
universal recuperado é:

$$
P(a)
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

Na leitura GDQ, esse resultado é o determinante da Hessiana física efetiva em
domínio com contorno ideal, não uma soma de modos livres postulada como
ontologia fundamental.

### Possibilidades futuras

Para transformar o fechamento ideal em previsão metrológica:

1. construir placas reais como fonte/contorno clássico;
2. calcular a impedância de placa:

$$
\mathsf R_{\rm plate}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY};
$$

3. incluir resposta dielétrica/condutiva efetiva
   $\mathsf R_{\rm plate}(\omega,k_\parallel,T)$;
4. incluir temperatura por soma de Matsubara:

$$
\omega_m
=
\frac{2\pi m k_BT}{\hbar};
$$

5. tratar rugosidade e geometria finita no domínio real $\Omega_{\rm real}$;
6. comparar com dados experimentais sem usar a força observada para calibrar
   a impedância.

### Regra

Esses itens não reabrem a Q47. O fechamento vigente é o limite estrutural de
placas ideais; materiais reais são refinamento de aparelho.

---

## Q49 — Metrologia molecular a partir de backgrounds GDQ

### Estado atual

A Questão 49 foi fechada condicionalmente. O rotor rígido ideal e a distorção
centrífuga líder foram derivados no setor reduzido:

$$
E_J
=
B_{\rm GDQ}J(J+1)
-
D_{\rm GDQ}[J(J+1)]^2
+
\cdots,
$$

com:

$$
B_{\rm GDQ}
=
\frac{\hbar^2}{2\mu_{\rm GDQ}R_0^2},
\qquad
D_{\rm GDQ}
=
\frac{\hbar^4}{2\mu_{\rm GDQ}^3\omega_e^2R_0^6}.
$$

Em unidades espectroscópicas:

$$
D_{\rm GDQ}
\simeq
\frac{4B_{\rm GDQ}^3}{\omega_e^2}.
$$

### Possibilidades futuras

Para transformar a Q49 em previsão metrológica molecular:

1. construir o background GDQ estacionário de moléculas diatômicas simples;
2. calcular diretamente:

$$
\Phi_{\rm mol,*}
\mapsto
\mu_{\rm GDQ},
\quad
R_0,
\quad
k_{\rm GDQ},
\quad
\omega_e;
$$

3. incluir anharmonicidades e acoplamentos ro-vibracionais pela Hessiana
   completa;
4. prever \(B\), \(D\) e constantes superiores para uma lista fixa de
   moléculas antes da comparação;
5. comparar com dados espectroscópicos sem usar \(D\) experimental para
   calibrar rigidez.

### Regra

Esse programa não reabre a Q49. A questão está fechada no rotor ideal e na
distorção harmônica líder; a metrologia de moléculas reais é uma aplicação
posterior da teoria de backgrounds moleculares.

---

## Q50 — Correções diferenciais e correlações angulares no decaimento beta

### Estado atual

A Questão 50 foi fechada condicionalmente quanto à taxa total e ao espectro
contínuo mínimo:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2.
$$

A norma contraída:

$$
\mathcal J_3^2
=
2|C_S|^2+6|C_T|^2
$$

foi fixada pelo fechamento GDQ \(\alpha^{-11}\), resultando em:

$$
\tau_n
=
879{,}398775004012\ \mathrm{s}.
$$

Comparação experimental registrada:

$$
\tau_n^{\rm PDG\,2026}
=
878{,}3\pm0{,}4\ \mathrm{s},
$$

logo:

$$
\Delta\tau
=
1{,}098775004\ \mathrm{s}
\simeq
0{,}125\%.
$$

Em relação à média PDG 2024/2025,
\(878{,}4\pm0{,}5\ \mathrm{s}\), o desvio é aproximadamente \(2{,}0\sigma\).
Em relação à média PDG 2026, o desvio é aproximadamente \(2{,}75\sigma\).

### Possibilidades futuras

Para transformar a Q50 em previsão diferencial/polarizada completa:

1. projetar a quarta variação física no background cirúrgico para separar
   \(C_S\) e \(C_T\);
2. calcular a fase relativa \(C_T/C_S\);
3. derivar:

$$
\delta_{\rm rad}(E_e),
\quad
\delta_{\rm recoil}(E_e),
\quad
\delta_{\rm surf}(E_e),
\quad
\delta_{\rm tors}(E_e);
$$

4. incluir recuo do próton e fator de forma bariônico da Q40;
5. prever coeficientes de correlação angular e observáveis polarizados;
6. comparar com dados de espectro beta e correlações sem usar esses dados para
   ajustar \(C_S\) e \(C_T\).

### Regra

Esse programa não reabre a Q50. Ele refina a forma diferencial e observáveis
polarizados; a energia contínua do antineutrino, a integral de fase e a vida
média total já estão consolidadas no fechamento contraído.

---

## Q51 — Fechamento metrológico do decaimento alfa

### Estado atual

A Questão 51 foi iniciada em `questoes/q51/`. O teste reduzido inicial mostrou
que a métrica legada:

$$
g_{rr}^{\rm leg}
=
\exp(-\alpha^2V_C/Q_\alpha)
$$

não melhora Gamow em uma série pequena. A troca não ajustada
\(\nu_0\to\nu_{\rm int}\), com

$$
\nu_{\rm int}
=
\frac{c}{2R_N}
\sqrt{\frac{2Q_\alpha}{\mu}},
$$

produziu pequena melhoria:

| Modelo | RMS décadas |
| --- | ---: |
| Gamow com \(\nu_0\) fixo | \(0{,}309897\) |
| GDQ exponencial legada com \(\nu_0\) fixo | \(0{,}311361\) |
| Gamow com \(\nu_{\rm int}\) | \(0{,}303358\) |
| GDQ exponencial legada com \(\nu_{\rm int}\) | \(0{,}304249\) |

### Programa futuro correto

Para fechar Q51 sem pós-ajuste:

1. construir o background núcleo-filho + cluster alfa;
2. projetar a Hessiana física no canal radial/superficial;
3. obter por Schur/DtN a impedância alfa--núcleo;
4. derivar:

$$
g_{rr}^{\rm eff}(r)
$$

diretamente do operador radial efetivo;

5. calcular a frequência de tentativa como modo normal interno:

$$
\nu_{\rm GDQ}
=
\frac1{2\pi}
\sqrt{
\lambda_{\alpha,{\rm int}}/M_\alpha^{\rm eff}
};
$$

6. congelar os parâmetros e comparar uma série isotópica com dados
   NUBASE/AME/ENSDF;
7. calcular o overlap/pré-formação de superfície:

$$
S_\alpha^{\rm GDQ}
=
\left|
\langle
\Phi_{\rm filho}\oplus\Phi_\alpha,
\Phi_{\rm pai}
\rangle_\partial^{\rm phys}
\right|^2;
$$

8. registrar RMS, resíduos, sensibilidade e comparação contra Gamow puro.

### Regra

A coincidência de um único núcleo, como U-238, não fecha a Q51. O fechamento
exige série isotópica com parâmetros universais e contornos físicos derivados.

### Atualização: pipeline algébrico Schur/Riesz

Foram adicionados em `questoes/q51/associados/`:

- `pipeline_calculo_preditivo_q51.md`;
- `calcular_taxa_alpha_gdq_q51.py`;
- `saida_calcular_taxa_alpha_gdq_q51.md`.

Esses arquivos tornam executável a etapa:

$$
K_{II},K_{I\partial},K_{\partial\partial}
\to
K_\partial^{\rm phys}
\to
P_\alpha
\to
E_\partial^{\rm GDQ}
\to
T_{1/2}^{\rm GDQ}.
$$

O script sem dados reais roda apenas um fixture algébrico. A tarefa futura real
é fornecer os blocos da Hessiana nuclear GDQ obtidos de um background físico,
não ajustar \(p_{\rm req}\) ou \(E_\partial^{\rm req}\).

### Atualização: execução reduzida dos pontos 1 a 5

Foi criado `questoes/q51/associados/avaliacao_reduzida_background_hessiana_q51.py`
e o relatório `questoes/q51/associados/fechamento_reduzido_pontos_1a5_q51.md`.
O cálculo executa uma versão reduzida da cadeia:

$$
\Phi_N
\to
K_{II},K_{I\partial},K_{\partial\partial}
\to
K_\partial^{\rm phys}
\to
P_\alpha
\to
S_\alpha^{\rm GDQ}
\to
T_{1/2}^{\rm GDQ}.
$$

A seleção correta de \(P_\alpha\) deve ser por overlap/carga/circulação do
cluster alfa, não por menor autovalor. Com essa correção, a variante reduzida
`closure` obteve RMS \(0{,}170790\) décadas e melhora de \(43{,}700\%\)
contra Gamow+\(\nu_{\rm int}\) no dataset diagnóstico.

Depois foi criado `derivar_camadas_hessiana_reduzida_q51.py`. O operador sem
torção gera \(2,8,20,40,70,112,\ldots\); a redução com cisão spin--torção gera
\(2,8,20,28,50,82,126\), removendo a lista manual de fechamentos do script.
Depois a frequência foi alinhada ao autovalor do canal alfa selecionado por
\(P_\alpha\), e a variante `closure_mobility` adicionou mobilidade de
determinante para filho exatamente duplamente fechado. Resultado: RMS
\(0{,}067894\) décadas e melhora \(77{,}619\%\) contra Gamow+\(\nu_{\rm int}\).
Status: avanço forte, mas ainda reduzido; o programa futuro é diagonalizar a
Hessiana nuclear completa, substituindo a ordenação angular efetiva e a
mobilidade reduzida por autovalores/autovetores do background GDQ.

### Status de arquivamento da Q51

A Q51 pode ser tratada como:

$$
\boxed{
\text{fechada como prova de conceito GDQ reduzida.}
}
$$

A avaliação metrológica ampla fica como possibilidade/programa posterior:

1. substituir o espectro angular reduzido pela Hessiana nuclear completa;
2. derivar \(g_{rr}^{\rm eff}\) e \(\nu_{\rm GDQ}\) completos;
3. usar NUBASE/AME/ENSDF;
4. comparar contra Royer, Viola--Seaborg, UDL e fórmulas modernas no mesmo
   dataset.

## Q54 — Refinamentos metrológicos da emergência de Einstein

A Q54 foi fechada estruturalmente e condicionalmente em
`questoes/q54/questao_54.md`: a Relatividade Geral emerge da equação métrica
ponderada da ação oficial por média torsional macroscópica e fechamento
hidrodinâmico. O valor absoluto de $G$ e de $\Lambda$ pertence ao problema
global/background já tratado na Q38.

Ficam como possibilidades posteriores, sem reabrir a Q54:

1. calcular os coeficientes PPN finos diretamente da Hessiana física do
   background solar;
2. avaliar correções torsionais em objetos rotantes, polarizados ou com
   anisotropia interna;
3. obter modelos numéricos de campo fraco com $\langle H\rangle_L\neq0$;
4. comparar precessão, lenteamento e atraso Shapiro com dados observacionais;
5. estudar variações aparentes de $G$ como resposta de contorno/aparelho, não
   como mudança da constante global.

## Q53 — Refinamento metrológico da Hessiana neutra

A Q53 está fechada estruturalmente em `questoes/q53/questao_53.md`. O neutrino
é tratado como modo neutro torsional/fase, sem estômato localizado, e a rota
reduzida atual fornece massas neutras próximas aos valores de oscilação.

O refinamento posterior, sem reabrir a questão, é elevar o candidato reduzido:

$$
\lambda
=
\left(
0,
\frac{\chi_\nu^2}{2},
\frac{6\pi}{5}
\right)
$$

a cálculo direto da Hessiana neutra oficial:

$$
K^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm folha},
K_{\rm neutro}^{\rm phys}
\Psi_\beta^{\rm folha}
\right\rangle_{\mathcal U}.
$$

Programa futuro:

1. construir o background neutro $\Phi_*^\nu$;
2. projetar $\operatorname{Hess}\mathcal S_{\rm GDQ}$ no setor neutro;
3. calcular $G^\nu$ e $K^\nu$;
4. diagonalizar $K^\nu c_i=\lambda_iG^\nu c_i$;
5. obter $Z_\nu$ pela ponte global--local;
6. calcular $\delta_{\rm CP}$ como holonomia orientada neutra;
7. calcular $V_{\rm GDQ}(n_e)$ como refração torsional por fonte clássica de
   matéria.

Documento dedicado:

```text
questoes/q53/associados/refinamento_metrologico_hessiana_neutra_q53.md
```

## Q58 — Solver cosmológico integrado

A Q58 está fechada estruturalmente em `questoes/q58/questao_58.md`: Hubble,
lítio, Bullet Cluster, CMB, BAO, supernovas, lentes, crescimento e
birrefringência devem sair de uma única sela cosmológica e de uma única
Hessiana física:

$$
\Phi_*^{\rm cos}
\to
K_{\rm cos}^{\rm phys}
\to
\delta\Phi_{\rm cos}
\to
\text{observáveis cosmológicos}.
$$

Programa metrológico posterior:

1. construir o solver de fundo $H(z)$;
2. acoplar distâncias SN/BAO ao mesmo fundo;
3. acoplar transferências CMB e crescimento ao mesmo $K_{\rm cos}^{\rm phys}$;
4. inserir BBN/lítio com a mesma expansão e correção Bohm--Cartan;
5. simular lentes/Bullet Cluster com o mesmo setor torsional residual;
6. calcular birrefringência como holonomia de Bismut do mesmo background.

Documento dedicado:

```text
questoes/q58/associados/plano_solver_cosmologico_integrado_q58.md
```

## Q55 — Elevação covariante do sóliton com horizonte

A Q55 foi fechada na redução efetiva testada em
`questoes/q55/questao_55.md`. A interpretação consolidada é:

$$
\boxed{
\text{buraco negro regular GDQ}
=
\text{sóliton geométrico de densidade--torção--curvatura com horizonte.}
}
$$

Ficam como programa futuro, sem reabrir o fechamento reduzido:

1. calcular o setor métrico polar completo;
2. construir coordenadas regulares atravessando horizontes;
3. montar a matriz acoplada covariante 8D completa;
4. calcular a Page curve física por canais espectrais reais da GDQ.

## Q56 — Programa cosmológico metrológico da energia escura

A Q56 foi fechada estruturalmente em `questoes/q56/questao_56.md`, mas deixa
um programa natural de extensão observacional.

Tarefas futuras:

1. decidir o contorno cosmológico correto da GDQ entre \(R_H=c/H_0\),
   horizonte de partículas e horizonte de de Sitter;
2. derivar o perfil global \(f(r)\sim\ln(r/r_p)\) como sela da ação oficial no
   setor cosmológico;
3. substituir a equipartição isotrópica dos 28 modos por traço espectral em
   backgrounds anisotrópicos:

   $$
   28
   \to
   \operatorname{Tr}_{\Lambda^2(\mathbb R^8)}P_{\rm cos};
   $$

4. escrever a projeção \(\alpha^2\) como corolário explícito da Q37 e da ponte
   global--local;
5. construir a Hessiana cosmológica física \(K_{\rm cos}^{\rm phys}\);
6. extrair \(m_{\rm gap}^2\), \(c_s^2\), resposta a fontes bariônicas e
   evolução linear de perturbações;
7. comparar posteriormente com supernovas, BAO, \(f\sigma_8\), CMB e lentes.

Essas tarefas não reabrem a resposta estrutural da Q56; elas transformam a
estimativa de escala em cosmologia quantitativa.

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

## 4. Rota Hopf + resíduos para interpretação geométrica do spin \(1/2\)

### Ideia

A Questão 26 foi fechada estruturalmente via fibrado spin, álgebra de Clifford
e representação de:

\[
\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C).
\]

Ainda assim, a GDQ possui uma rota geométrica própria para interpretar o spin:
a fibração de Hopf combinada com uma integral de resíduos/holonomia em torno
do defeito solitônico.

A estrutura topológica relevante é:

\[
\boxed{
S^1\hookrightarrow S^3\xrightarrow{\pi}S^2.
}
\]

Com:

\[
\boxed{
S^3\simeq SU(2),
}
\]

e a projeção:

\[
\boxed{
SU(2)\to SO(3).
}
\]

Essa estrutura implementa naturalmente:

\[
\boxed{
U(2\pi)=-I,
\qquad
U(4\pi)=I.
}
\]

### Papel da integral de resíduos

No texto original, a circulação do defeito é associada a uma 1-forma complexa:

\[
\omega
=
p_\mu dx^\mu
\quad\text{ou}\quad
\omega
=
\nabla_\mu S_C\,dx^\mu,
}
\]

com:

\[
S_C=S_R+iS_I.
\]

Para um contorno fechado \(\gamma\) ao redor do defeito:

\[
\boxed{
\oint_\gamma\omega
=
2\pi i\sum_k\operatorname{Res}(\omega,z_k).
}
\]

A proposta futura é interpretar esse resíduo como invariante de holonomia do
defeito:

\[
\boxed{
\operatorname{Hol}_\gamma
=
\exp\left(\frac{i}{\hbar}\oint_\gamma dS_R\right).
}
\]

No setor spinorial/Hopf, a holonomia de uma volta pode produzir:

\[
\boxed{
\operatorname{Hol}_{2\pi}=-1,
}
\]

enquanto duas voltas produzem:

\[
\boxed{
\operatorname{Hol}_{4\pi}=+1.
}
\]

### Hierarquia correta

Essa rota não substitui a estrutura oficial da Questão 26.

A hierarquia correta é:

1. fibrado spin e representação de \(\mathrm{Spin}(3,1)\): fundamento
   matemático de spin \(1/2\);
2. Hopf/SU(2): realização geométrica da cobertura dupla;
3. integral de resíduos: mecanismo GDQ para computar/quantizar a holonomia do
   defeito;
4. torção/vorticidade: interpretação física local do spin como circulação
   solitônica.

### O que falta para virar prova

Para transformar essa rota em resultado oficial, ainda é necessário:

1. definir a 1-forma exata \(\omega\);
2. especificar o domínio complexo e os polos/resíduos permitidos;
3. mostrar que a integral de resíduos produz exatamente a holonomia spinorial;
4. conectar o contorno \(\gamma\) ao fibrado Hopf \(S^1\hookrightarrow S^3\to S^2\);
5. provar que a monodromia \(2\pi\mapsto-1\) e \(4\pi\mapsto+1\) coincide com
   a representação spinorial usada no operador de Dirac;
6. separar claramente circulação escalar inteira de monodromia spinorial
   meia-inteira;
7. verificar compatibilidade com a torção \(B\) e com o cone causal de \(h\).

### Status

\[
\boxed{
\text{Rota aberta e compatível com a GDQ; útil para fortalecer a interpretação
geométrica do spin, mas ainda não substitui o fechamento estrutural da
Questão 26.}
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
`37p/teste_schur_dtn_global.py` combinou o kernel fotônico canonizado, a
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

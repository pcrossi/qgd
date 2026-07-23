# Questão 24 — Como o problema da medida é resolvido?

## 1. Pergunta

A Questão 24 pergunta:

\[
\boxed{
\text{como a GDQ descreve uma medição completa sem inserir a regra de Born
manualmente?}
}
\]

`24-0.md` exige construir um modelo contendo:

1. sistema;
2. aparelho;
3. ambiente;
4. interação;
5. registros;
6. decoerência;
7. probabilidades;
8. repetibilidade.

E responder:

1. por que uma base é selecionada?
2. um resultado único ocorre ou apenas decoerência?
3. há variáveis adicionais?
4. há colapso real?
5. o modelo permite sinalização?

A resposta não aceitável é:

\[
\boxed{
\text{inserir }|\langle i|\psi\rangle|^2\text{ na função de partição e depois
alegar que Born foi derivada.}
}
\]

---

## 2. Resposta curta

A medição na GDQ deve ser modelada como um processo aberto:

\[
\boxed{
S+A+E
}
\]

onde:

- \(S\) é o sistema medido;
- \(A\) é o aparelho;
- \(E\) é o ambiente;
- \(R_i\) são registros macroscópicos estáveis;
- a interação \(H_{\rm int}\) correlaciona autovalores do observável com
  estados de ponteiro do aparelho.

O acoplamento ideal é:

\[
\boxed{
|s_i\rangle|A_0\rangle|E_0\rangle
\longmapsto
|s_i\rangle|A_i\rangle|E_i\rangle.
}
\]

Para:

\[
\boxed{
|\psi\rangle=\sum_i c_i|s_i\rangle,
}
\]

a evolução unitária total dá:

\[
\boxed{
|\Psi_{SAE}\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
}
\]

Se:

\[
\boxed{
\langle E_j|E_i\rangle\approx\delta_{ij},
\qquad
\langle A_j|A_i\rangle\approx\delta_{ij},
}
\]

então os termos de interferência desaparecem no estado reduzido:

\[
\boxed{
\rho_{SA}
=
\operatorname{Tr}_E|\Psi_{SAE}\rangle\langle\Psi_{SAE}|
\approx
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

Isso resolve:

\[
\boxed{
\text{base de medição, registros estáveis, probabilidades operacionais e
repetibilidade.}
}
\]

Mas há uma distinção essencial:

\[
\boxed{
\text{decoerência sozinha produz mistura imprópria, não escolhe
ontologicamente um único ramo.}
}
\]

Na GDQ, um resultado único só fica resolvido se a teoria assumir que a
microgeometria real do aparelho/ambiente seleciona uma bacia de atração
efetiva. Então o colapso é uma transição geométrica efetiva, contínua e
local, não um postulado não-unitário fundamental.

---

## 3. Modelo mínimo de medição

### 3.1 Sistema

O sistema \(S\) vive em:

\[
\boxed{
\mathcal H_S.
}
\]

O observável medido é:

\[
\boxed{
O_S=\sum_i o_iP_i,
}
\]

com:

\[
\boxed{
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I_S.
}
\]

Os estados próprios são:

\[
\boxed{
P_i|s_j\rangle=\delta_{ij}|s_j\rangle.
}
\]

Um estado inicial geral é:

\[
\boxed{
|\psi\rangle_S=\sum_i c_i|s_i\rangle.
}
\]

Pela Questão 22, as probabilidades operacionais serão calculadas por:

\[
\boxed{
P(i)=\operatorname{Tr}(\rho_SP_i),
}
\]

não inseridas na função de partição.

---

### 3.2 Aparelho

O aparelho \(A\) vive em:

\[
\boxed{
\mathcal H_A.
}
\]

Ele possui um estado pronto:

\[
\boxed{
|A_0\rangle
}
\]

e estados de ponteiro:

\[
\boxed{
|A_i\rangle.
}
\]

Esses estados devem ser macroscopicamente distinguíveis:

\[
\boxed{
\langle A_i|A_j\rangle\approx\delta_{ij}.
}
\]

Na leitura GDQ, cada \(|A_i\rangle\) corresponde a uma bacia geométrica
macroscópica estável do aparelho: uma configuração de métrica/densidade/torção
que pode gravar um registro.

---

### 3.3 Ambiente

O ambiente \(E\) vive em:

\[
\boxed{
\mathcal H_E.
}
\]

Ele inclui:

1. fótons espalhados;
2. fônons;
3. modos térmicos;
4. graus de liberdade internos do detector;
5. microgeometria efetiva do suporte macroscópico;
6. modos do vácuo/Kähler que carregam informação de fase inacessível.

O ambiente começa em:

\[
\boxed{
|E_0\rangle.
}
\]

Depois da interação:

\[
\boxed{
|E_0\rangle\to |E_i\rangle
}
\]

dependendo do resultado registrado.

---

## 4. Interação de medição

A interação ideal de von Neumann tem a forma:

\[
\boxed{
H_{\rm int}(t)
=
g(t)\,O_S\otimes \Pi_A.
}
\]

Aqui:

- \(O_S\) é o observável medido;
- \(\Pi_A\) é o momento conjugado da variável de ponteiro;
- \(g(t)\) é não nulo apenas durante a janela de medição.

O operador unitário total é:

\[
\boxed{
U_{SA}
=
\exp\left[-\frac{i}{\hbar}\int H_{\rm int}(t)\,dt\right].
}
\]

Ele deve satisfazer:

\[
\boxed{
U_{SA}\left(|s_i\rangle|A_0\rangle\right)
=
|s_i\rangle|A_i\rangle.
}
\]

Incluindo o ambiente:

\[
\boxed{
U_{SAE}
\left(
|s_i\rangle|A_0\rangle|E_0\rangle
\right)
=
|s_i\rangle|A_i\rangle|E_i\rangle.
}
\]

Por linearidade:

\[
\boxed{
\sum_i c_i|s_i\rangle|A_0\rangle|E_0\rangle
\longmapsto
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
}
\]

---

## 5. Decoerência

O estado total depois da medição é:

\[
\boxed{
|\Psi\rangle_{SAE}
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
}
\]

A matriz densidade total é:

\[
\boxed{
\rho_{SAE}
=
\sum_{ij}
c_i\bar c_j
|s_i,A_i,E_i\rangle
\langle s_j,A_j,E_j|.
}
\]

O observador macroscópico não acessa todos os graus de liberdade de \(E\).
Logo:

\[
\boxed{
\rho_{SA}
=
\operatorname{Tr}_E\rho_{SAE}.
}
\]

Calculando:

\[
\boxed{
\rho_{SA}
=
\sum_{ij}
c_i\bar c_j
\langle E_j|E_i\rangle
|s_i,A_i\rangle
\langle s_j,A_j|.
}
\]

Se o ambiente registra informação suficiente:

\[
\boxed{
\langle E_j|E_i\rangle\approx0
\quad (i\ne j),
}
\]

então:

\[
\boxed{
\rho_{SA}
\approx
\sum_i
|c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

Essa é a decoerência.

Na linguagem GDQ, a decoerência corresponde à separação dinâmica de bacias de
atração geométricas: os diferentes registros \(A_i\) passam a ocupar setores
macroscópicos quase ortogonais, separados por impedância, dissipação efetiva e
condições de contorno distintas.

---

## 6. Por que uma base é selecionada?

A base não é escolhida pela regra de Born.

Ela é escolhida pela interação:

\[
\boxed{
H_{\rm int}=g(t)\,O_S\otimes\Pi_A.
}
\]

Os estados estáveis são aqueles que não se embaralham rapidamente sob a
interação com o ambiente. Eles satisfazem, aproximadamente:

\[
\boxed{
|s_i\rangle|A_i\rangle|E_0\rangle
\longmapsto
|s_i\rangle|A_i\rangle|E_i(t)\rangle.
}
\]

sem virar superposição macroscópica de vários ponteiros.

Esses são os estados de ponteiro.

Matematicamente, a base selecionada é a que diagonaliza, no setor relevante, o
acoplamento dominante:

\[
\boxed{
[P_i,H_{\rm int}]\approx0
}
\]

ou, na forma de teoria aberta, a base robusta dos operadores de Lindblad
efetivos:

\[
\boxed{
L_\alpha |A_i\rangle\approx \ell_{\alpha i}|A_i\rangle.
}
\]

Na GDQ, essa base corresponde às bacias estáveis/atratores geométricos
impostos pelo aparelho.

---

## 7. Registros

Um registro é um estado macroscópico estável \(R_i\) correlacionado a um
resultado \(i\):

\[
\boxed{
R_i\equiv |A_i\rangle|E_i\rangle.
}
\]

Para ser registro físico, ele deve satisfazer:

1. distinguibilidade:

\[
\boxed{
\langle R_i|R_j\rangle\approx0,\qquad i\ne j;
}
\]

2. estabilidade por tempo macroscópico:

\[
\boxed{
R_i(t+\Delta t)\approx R_i(t);
}
\]

3. redundância ambiental:

\[
\boxed{
E_i=E_i^{(1)}E_i^{(2)}\cdots E_i^{(N)}
}
\]

com muitos fragmentos carregando a mesma informação;

4. legibilidade clássica:

\[
\boxed{
\text{observadores diferentes acessam o mesmo }i\text{ sem medir }S
diretamente.}
}
\]

Na GDQ, o registro é uma configuração geométrica macroscópica presa em uma
bacia de atração do aparelho.

---

## 8. Probabilidades

As probabilidades não devem ser postas na partição.

Elas vêm da Questão 22:

\[
\boxed{
P(i)=\operatorname{Tr}(\rho_SP_i).
}
\]

Para estado puro:

\[
\boxed{
P(i)=\langle\psi|P_i|\psi\rangle.
}
\]

Se:

\[
\boxed{
|\psi\rangle=\sum_i c_i|s_i\rangle,
}
\]

então:

\[
\boxed{
P(i)=|c_i|^2.
}
\]

Na medição completa:

\[
\boxed{
P(R_i)
=
\operatorname{Tr}_{SAE}
\left(
\rho_{SAE}\,
I_S\otimes |A_i,E_i\rangle\langle A_i,E_i|
\right).
}
\]

No setor ideal:

\[
\boxed{
P(R_i)=|c_i|^2.
}
\]

A função de partição geométrica do aparelho pode descrever pesos dinâmicos de
atratores, tempos de relaxação e estabilidade dos registros, mas não deve
introduzir \( |c_i|^2 \) como input escondido.

---

## 9. Repetibilidade

Uma medição ideal é repetível quando, após obter \(i\), medir novamente o
mesmo observável retorna \(i\).

Isso exige:

\[
\boxed{
P_i|s_i\rangle=|s_i\rangle
}
\]

e:

\[
\boxed{
U_{\rm meas}(|s_i\rangle|A_0\rangle)
=
|s_i\rangle|A_i\rangle.
}
\]

Ou seja, o estado próprio não é destruído pela medição ideal:

\[
\boxed{
|s_i\rangle\to |s_i\rangle.
}
\]

Depois do registro:

\[
\boxed{
\rho_{S|i}
=
\frac{P_i\rho_SP_i}{\operatorname{Tr}(\rho_SP_i)}.
}
\]

Então:

\[
\boxed{
\operatorname{Tr}(\rho_{S|i}P_i)=1.
}
\]

Na GDQ, repetibilidade significa que o sistema e o aparelho caíram na mesma
bacia geométrica estável; uma nova interação com o mesmo aparelho não muda o
atrator.

---

## 10. Um resultado único ocorre ou apenas decoerência?

Aqui é preciso ser preciso.

Decoerência por si só produz:

\[
\boxed{
\rho_{SA}
\approx
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

Isso é uma mistura imprópria obtida por traço parcial. Ela explica:

1. por que não vemos interferência entre ponteiros;
2. por que há registros clássicos robustos;
3. por que a base de ponteiro é selecionada;
4. por que a estatística observada obedece Born.

Mas decoerência sozinha não seleciona ontologicamente um único ramo.

Para a GDQ alegar resultado único, deve assumir um ingrediente físico
adicional:

\[
\boxed{
\text{a microgeometria real do aparelho/ambiente seleciona uma bacia de
atração efetiva.}
}
\]

Isto é, o estado global pode ser unitário no nível \(S+A+E\), mas a trajetória
geométrica efetiva de um evento individual cai em uma bacia \(R_i\), determinada
por:

1. condições iniciais microscópicas do aparelho;
2. flutuações ambientais;
3. geometria local de contorno;
4. impedância/decoerência;
5. instabilidade/bifurcação efetiva.

Então:

\[
\boxed{
\text{resultado único na GDQ = seleção ontológica de atrator geométrico.}
}
\]

Sem essa hipótese ontológica, a teoria resolve decoerência e probabilidades,
mas não o problema do resultado único.

---

## 11. Há variáveis adicionais?

Sim, se a GDQ pretende explicar resultado único.

As variáveis adicionais não precisam ser “partículas ocultas” no sentido
bohmiano padrão. Elas podem ser:

1. a geometria real \(g_{\mu\bar\nu}\);
2. a densidade real \(\rho\);
3. a fase \(S_R\);
4. os dados de contorno do aparelho;
5. os modos ambientais inacessíveis;
6. o setor topológico/holonomia;
7. flutuações microscópicas da malha Kähler/Bismut.

Essas variáveis determinam qual bacia de atração é realizada em um evento
individual.

Operacionalmente, observadores que ignoram esses graus de liberdade usam:

\[
\boxed{
\rho_{SA}=\operatorname{Tr}_E\rho_{SAE}
}
\]

e obtêm a estatística de Born.

---

## 12. Há colapso real?

Há três leituras possíveis.

### 12.1 Leitura mínima

Não há colapso fundamental.

Há apenas:

\[
\boxed{
\text{unitariedade global + decoerência + atualização de informação.}
}
\]

Essa leitura é matematicamente segura, mas não resolve resultado único
ontológico.

### 12.2 Leitura GDQ forte

Há colapso físico efetivo:

\[
\boxed{
\text{relaxação/bifurcação geométrica para uma bacia de atração.}
}
\]

Esse colapso não é um salto axiomático não-unitário. Ele é:

1. contínuo;
2. local no aparelho;
3. aberto/dissipativo no setor reduzido;
4. compatível com unitariedade do sistema total;
5. dependente da microgeometria real.

### 12.3 Leitura proibida

Não se deve dizer:

\[
\boxed{
\text{a função de onda colapsa magicamente e escolhe }i\text{ sem mecanismo.}
}
\]

Também não se deve dizer:

\[
\boxed{
\text{decoerência sozinha produz resultado único.}
}
\]

Isso seria tecnicamente falso.

---

## 13. O modelo permite sinalização?

Não, desde que as operações locais obedeçam a estrutura de álgebra local já
fixada na Questão 8.

Se \(O_A\) e \(O_B\) são separados espacialmente:

\[
\boxed{
O_A\perp_h O_B,
}
\]

então:

\[
\boxed{
[\mathcal A(O_A),\mathcal A(O_B)]=0.
}
\]

Uma operação local não seletiva em \(B\), com operadores de Kraus \(M_\alpha\),
satisfaz:

\[
\boxed{
\sum_\alpha M_\alpha^\dagger M_\alpha=I.
}
\]

Para observável \(A\in\mathcal A(O_A)\):

\[
\boxed{
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
(M_\alpha\rho M_\alpha^\dagger A).
}
\]

Como:

\[
\boxed{
[A,M_\alpha]=0,
}
\]

segue:

\[
\boxed{
\langle A\rangle'=\langle A\rangle.
}
\]

Logo:

\[
\boxed{
\text{não há sinalização superluminal nem retrocausal controlável.}
}
\]

A prescrição de Sudarshan pode impor consistência global de contorno, mas não
fornece um canal operacional para enviar bits ao passado.

---

## 14. Relação com o capítulo 16 original

O capítulo `pt-br/16 - Problema da Medida.md` contém uma intuição compatível
com a leitura GDQ forte:

\[
\boxed{
\text{medição como transição/bifurcação geométrica para atratores estáveis.}
}
\]

Isso é aproveitável.

Mas algumas frases precisam ser disciplinadas:

1. não se deve afirmar que a equação de calor conjugada sozinha resolve Born;
2. não se deve inserir \(P(k)=|c_k|^2\) como input da partição;
3. não se deve confundir decoerência com resultado único;
4. não se deve violar a unitariedade fechada da Questão 21;
5. não se deve usar a parte avançada de Sudarshan como canal de sinalização.

A versão auditável é:

\[
\boxed{
\text{Born vem da Questão 22; a medição implementa os projetores e seleciona
a base por interação/decoerência.}
}
\]

E:

\[
\boxed{
\text{o resultado único, se assumido, é seleção de atrator por microgeometria
real do aparelho/ambiente.}
}
\]

---

## 15. Relação com o Apêndice 11

O Apêndice 11 propõe uma razão volumétrica de atratores:

\[
\boxed{
P_n=\frac{\mathcal Z[U_n]}{\mathcal Z_{\rm total}}.
}
\]

Essa ideia é útil para modelar a dinâmica geométrica dos registros.

Mas a forma:

\[
\boxed{
c_1=|\langle 1|\psi\rangle|^2
}
\]

não pode ser usada como derivação de Born, porque já insere Born.

Uso correto:

1. primeiro derivar Born pela Questão 22:

\[
\boxed{
P_i=\operatorname{Tr}(\rho P_i);
}
\]

2. depois usar o ensemble geométrico para modelar estabilidade, relaxação e
   robustez dos registros:

\[
\boxed{
\mathcal Z[U_i]\text{ mede a estabilidade/dinâmica da bacia }i,
\text{ não a origem primária do peso Born.}
}
\]

---

## 15.5 Adendo — prova espectral de dominância no capítulo 16

O capítulo original `pt-br/16 - Problema da Medida.md` contém um ingrediente
matemático que deve ser incorporado à auditoria: o isomorfismo entre a equação
do calor conjugada de Perelman e a equação de difusão de nêutrons em meios
multiplicativos.

Nesse quadro, o operador efetivo satisfaz:

\[
\boxed{
\mathcal H\psi_n(\boldsymbol r)=\lambda_n\psi_n(\boldsymbol r),
\qquad
0<\lambda_0<\lambda_1<\lambda_2<\cdots.
}
\]

A densidade admite expansão espectral:

\[
\boxed{
\rho(\boldsymbol r,\tau)
=
\sum_{n=0}^{\infty}
c_n e^{-\lambda_n\tau}\psi_n(\boldsymbol r).
}
\]

Como:

\[
\boxed{
\frac{e^{-\lambda_n\tau}}{e^{-\lambda_0\tau}}
=
e^{-(\lambda_n-\lambda_0)\tau}
\longrightarrow0,
\qquad n\ge1,
}
\]

segue que:

\[
\boxed{
\rho(\boldsymbol r,\tau)
\xrightarrow{\tau\to\infty}
c_0e^{-\lambda_0\tau}\psi_0(\boldsymbol r).
}
\]

Portanto, não é correto dizer que o manuscrito não possui nenhum mecanismo de
dominância assintótica. Ele possui uma rota espectral clara: o modo fundamental
\(\psi_0\) domina por separação de autovalores.

A ressalva técnica é outra. Essa prova fecha a dominância de um operador
linearizado/efetivo com espectro discreto e gap:

\[
\boxed{
\Delta\lambda=\lambda_1-\lambda_0>0.
}
\]

Ainda resta explicitar, para a medição completa:

1. quais condições de contorno do aparelho definem \(\mathcal H\);
2. como cada registro \(R_i\) corresponde a uma bacia/autofunção efetiva;
3. como o acoplamento \(S+A+E\) reconfigura o espectro;
4. qual taxa real de supressão dos termos fora da diagonal;
5. como a seleção de um atrator único é compatível com a estatística Born da
   Questão 22.

Assim, a pendência não é mais “ausência de prova assintótica”. A pendência
correta é:

\[
\boxed{
\text{formalizar a ponte entre dominância espectral de }\mathcal H
\text{ e registros macroscópicos }R_i.
}
\]

---

## 15.6 Fechamento — teorema assintótico de registros

A ponte acima foi formalizada nos adendos:

1. `associados/operador_medicao_gdq.md`;
2. `associados/setores_registro_bacias.md`;
3. `associados/gap_decoerencia_assintotica.md`;
4. `associados/teorema_assintotico_registros_q24.md`.
5. `associados/resultado_unico_bacias_microgeometria.md`.

O operador de medição da GDQ é a Hessiana física da ação oficial com os
contornos do aparelho:

\[
\boxed{
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_*}
\mathcal S_{\rm GDQ}^{S+A+E}
P^{\rm phys}.
}
\]

No setor de densidade:

\[
\boxed{
\partial_\tau\rho
=
-\mathcal H_\rho\rho,
\qquad
\mathcal H_\rho
=
\Pi_\rho\mathcal H_{\rm meas}\Pi_\rho^*.
}
\]

Os registros são setores/bacias do aparelho:

\[
\boxed{
R_i
\leftrightarrow
\Omega_i
\leftrightarrow
\Pi_i,
\qquad
\Pi_i\Pi_j=\delta_{ij}\Pi_i.
}
\]

Se o aparelho define setores separados por gap:

\[
\boxed{
\Delta_{\rm meas}
=
\min\left\{\min_i(\lambda_{i,1}-\lambda_{i,0}),
\min_{i\ne j}\operatorname{dist}(\sigma_i,\sigma_j)\right\}
>0,
}
\]

então os termos fora da diagonal obedecem:

\[
\boxed{
|\Gamma_{ij}(\tau)|
\le
C_{ij}e^{-\Delta_{ij}\tau},
\qquad
i\ne j.
}
\]

Assim:

\[
\boxed{
\rho_{SA}(\tau)
\xrightarrow{\tau\to\infty}
\sum_i
\operatorname{Tr}(\rho_SP_i)
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

Portanto a dominância espectral do Capítulo 16 fica conectada aos registros
macroscópicos \(R_i\). A regra de Born não foi inserida na partição; ela entra
como regra operacional da Questão 22, enquanto a Q24 mostra como o aparelho
implementa fisicamente os projetores \(P_i\).

O resultado único é tratado no adendo
`associados/resultado_unico_bacias_microgeometria.md`. A ideia é substituir a
hipótese informal de bacia por um teorema condicional.

Se o espaço físico de microgeometrias do aparelho e ambiente satisfaz:

1. regularidade do espaço de configurações;
2. existência de funcional de Lyapunov;
3. registros como mínimos hiperbólicos;
4. fronteiras de bacia dadas por variedades estáveis de selas;
5. medida inicial regular em relação à medida GDQ;

então:

\[
\boxed{
\mathcal C_{A+E}^{\rm reg}
=
\bigcup_i\mathcal B_i
\;\dot\cup\;
\mathcal N,
\qquad
\mu(\mathcal N)=0.
}
\]

Portanto, para quase todo evento real:

\[
\boxed{
\Phi_0\in\mathcal B_i
\text{ para um único }i,
\qquad
\Phi(\tau;\Phi_0)\to R_i.
}
\]

A probabilidade do registro é:

\[
\boxed{
\mathbb P(R_i)
=
\mu_{\rm init}(\mathcal B_i)
=
\operatorname{Tr}(\rho_SP_i).
}
\]

Assim, o colapso é uma transição geométrica efetiva no setor aberto
condicionado. Ele é teorema condicional para aparelhos cujas bacias reais
satisfaçam as hipóteses acima.

Status atualizado:

\[
\boxed{
\text{Questão 24 fechada condicionalmente como teorema assintótico de
registros.}
}
\]

Condição:

\[
\boxed{
\mathcal H_{\rm meas}\text{ auto-adjunto, setores }R_i\text{ bem definidos e }
\Delta_{\rm meas}>0,
\text{ com bacias reais Morse/Lyapunov para resultado único.}
}
\]

---

## 16. Checklist da Questão 24

### 16.1 Sistema

\[
\boxed{
\mathcal H_S,\qquad O_S=\sum_i o_iP_i.
}
\]

### 16.2 Aparelho

\[
\boxed{
\mathcal H_A,\qquad |A_0\rangle\to |A_i\rangle.
}
\]

### 16.3 Ambiente

\[
\boxed{
\mathcal H_E,\qquad |E_0\rangle\to |E_i\rangle.
}
\]

### 16.4 Interação

\[
\boxed{
H_{\rm int}=g(t)O_S\otimes\Pi_A.
}
\]

### 16.5 Registros

\[
\boxed{
R_i=|A_i\rangle|E_i\rangle,
\qquad
\langle R_i|R_j\rangle\approx\delta_{ij}.
}
\]

### 16.6 Decoerência

\[
\boxed{
\rho_{SA}
\approx
\sum_i |c_i|^2|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

### 16.7 Probabilidades

\[
\boxed{
P(i)=\operatorname{Tr}(\rho_SP_i).
}
\]

### 16.8 Repetibilidade

\[
\boxed{
\rho_{S|i}
=
\frac{P_i\rho_SP_i}{\operatorname{Tr}(\rho_SP_i)},
\qquad
\operatorname{Tr}(\rho_{S|i}P_i)=1.
}
\]

---

## 17. Resposta final da Questão 24

A GDQ resolve a medição, em forma auditável, assim:

\[
\boxed{
\text{medição}=
\text{acoplamento }S+A+E
\text{ que correlaciona projetores }P_i
\text{ com registros macroscópicos }R_i.
}
\]

A base é selecionada por:

\[
\boxed{
H_{\rm int}
\text{ e pela estabilidade/decoerência dos estados de ponteiro.}
}
\]

As probabilidades são:

\[
\boxed{
P(i)=\operatorname{Tr}(\rho_SP_i),
}
\]

como derivado na Questão 22.

A decoerência produz:

\[
\boxed{
\rho_{SA}
\approx
\sum_i P(i)\,|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

A repetibilidade segue da estabilidade dos projetores:

\[
\boxed{
P_i\rho_{S|i}P_i=\rho_{S|i}.
}
\]

O teorema assintótico de registros prova que, sob gap setorial:

\[
\boxed{
|\Gamma_{ij}(\tau)|
\le
C_{ij}e^{-\Delta_{ij}\tau},
\qquad
i\ne j.
}
\]

Logo, a dominância espectral gera registros reduzidos estáveis.

O resultado único exige a verificação das hipóteses de bacia real da
microgeometria \(A+E\). Quando elas valem, o adendo de bacias prova:

\[
\boxed{
\Phi_0\in\mathcal B_i
\text{ para um único }i
\quad\Rightarrow\quad
\Phi(\tau)\to R_i
\quad
\text{para quase todo evento.}
}
\]

O “colapso” é:

\[
\boxed{
\text{transição geométrica efetiva, contínua e aberta no setor reduzido,
compatível com unitariedade global.}
}
\]

Não há sinalização:

\[
\boxed{
O_A\perp_hO_B
\Rightarrow
[\mathcal A(O_A),\mathcal A(O_B)]=0.
}
\]

Portanto:

\[
\boxed{
\text{Questão 24 fechada condicionalmente como teorema assintótico de
registros e bacias reais.}
}
\]

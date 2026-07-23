# Questão 52 — Klein–Nishina

## 1. Enunciado

A questão pergunta se a seção de choque de Klein–Nishina é realmente derivada
na GDQ, ou se a fórmula final foi obtida inserindo manualmente estruturas
conhecidas da QED.

As perguntas obrigatórias são:

1. a amplitude vem da ação?
2. como os canais \(s\) e \(u\) aparecem?
3. como polarizações e spin são somados?
4. a normalização da seção de choque é derivada?

O apêndice legado

$$
\texttt{pt-br/Apêndice 6 - Geometrização do Espalhamento de Klein-Nishina.md}
$$

contém a cinemática correta e a fórmula final correta, mas a média de
spin/polarização aparece como identificação externa. Portanto, o apêndice não
deve ser lido como derivação completa da amplitude a partir da ação oficial.

## 2. Dados e domínio

O processo físico é o espalhamento Compton de um fóton por um sóliton
eletrônico:

$$
\gamma(k,\epsilon)+e(p,s)
\longrightarrow
\gamma(k',\epsilon')+e(p',s').
$$

No setor assintótico de laboratório:

$$
p^2=p'^2=m_e^2c^2,
\qquad
k^2=k'^2=0,
$$

e a conservação de Noether fornece

$$
p+k=p'+k'.
$$

No referencial de repouso inicial do sóliton,

$$
p=(m_ec,\mathbf 0).
$$

Define-se

$$
x=\frac{E}{m_ec^2}.
$$

A cinemática Compton segue de conservação de energia-momento:

$$
\boxed{
\frac{E'}{E}
=
\frac{1}
{1+x(1-\cos\theta)}.
}
$$

## 3. A amplitude vem da ação?

Resposta curta:

$$
\boxed{
\text{estruturalmente sim; no apêndice legado, não completamente.}
}
$$

Na GDQ, a amplitude deve vir da expansão da ação oficial ao redor do background
do sóliton eletrônico estacionário:

$$
\Phi_e^*
=
(g_e^*,f_e^*,H_e^*,\mathcal U_e^*).
$$

Escrevendo uma perturbação fotônica física como

$$
\delta\Phi_\gamma
=
(\delta g_\gamma,\delta f_\gamma,\delta H_\gamma),
$$

a expansão funcional tem a forma

$$
\mathcal S_{\rm GDQ}[\Phi_e^*+\delta\Phi]
=
\mathcal S_*
+
\frac12
\langle
\delta\Phi,
K_e^{\rm phys}\delta\Phi
\rangle
+
\frac{1}{3!}
\mathcal V_e^{(3)}[\delta\Phi,\delta\Phi,\delta\Phi]
+
\cdots.
$$

Aqui,

$$
K_e^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_e^*}\mathcal S_{\rm GDQ}
P_{\rm phys}
$$

é a Hessiana física do sóliton eletrônico, e

$$
\mathcal V_e^{(3)}
=
\left.
\frac{\delta^3\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*}
$$

é o vértice geométrico que acopla uma flutuação do sóliton a dois fótons.

O objeto que substitui a amplitude perturbativa usual é a forma bilinear
reduzida

$$
\mathcal M_{\rm GDQ}
=
\langle
\delta\Phi_{\gamma'} ,
\mathcal V_{\gamma e\gamma}^{\rm eff}
\delta\Phi_{\gamma}
\rangle,
$$

onde

$$
\mathcal V_{\gamma e\gamma}^{\rm eff}
=
P_\gamma
\mathcal V_e^{(3)}
G_e^{\rm phys}
\mathcal V_e^{(3)}
P_\gamma
+
\mathcal V_e^{(4)}|_{\gamma\gamma ee}
$$

e

$$
G_e^{\rm phys}
=
(K_e^{\rm phys})^{-1}
$$

no domínio físico com contornos causais da GDQ.

Portanto, a amplitude é derivável da ação por Hessiana, propagador e vértices
variacionais. O apêndice legado, porém, não calculou explicitamente esses
blocos; ele escreveu a estrutura já reduzida. A conclusão correta é:

$$
\boxed{
\text{a amplitude está estruturalmente formulada, mas sua avaliação direta
completa permanece condicional.}
}
$$

## 4. Como os canais \(s\) e \(u\) aparecem?

Os canais \(s\) e \(u\) não precisam ser postulados como diagramas de Feynman.
Eles aparecem como as duas inversões possíveis do propagador físico do sóliton
entre absorção e emissão do fóton.

Na redução assintótica:

$$
G_e^{\rm phys}(p+k)
\sim
\frac{1}{(p+k)^2-m_e^2c^2},
$$

e

$$
G_e^{\rm phys}(p-k')
\sim
\frac{1}{(p-k')^2-m_e^2c^2}.
$$

Como

$$
(p+k)^2-m_e^2c^2
=
2p\cdot k,
$$

e

$$
(p-k')^2-m_e^2c^2
=
-2p\cdot k',
$$

os dois canais reduzidos são:

$$
\boxed{
\mathcal M_s
\propto
\frac{1}{2p\cdot k},
\qquad
\mathcal M_u
\propto
\frac{1}{-2p\cdot k'}.
}
$$

Na linguagem GDQ, eles são os dois ramos causais do mesmo propagador de
interface:

$$
G_{\rm Sud}
=
\frac12(G_{\rm ret}+G_{\rm adv}),
$$

projetado no setor assintótico do sóliton eletrônico. Essa identificação é
compatível com o apêndice legado e não altera a ação oficial.

## 5. Como polarizações e spin são somados?

Este é o ponto mais delicado da Q52.

No apêndice legado, a passagem

$$
(\epsilon\cdot\epsilon')^2
\longrightarrow
\frac{1}{4m^2}
\left[
\frac{E}{E'}
+
\frac{E'}{E}
-
\sin^2\theta
\right]
$$

foi inserida como “média geométrica de spin”. Isso reproduz a estrutura correta,
mas não é uma derivação.

O adendo

$$
\texttt{questoes/q52/associados/projetores\_spin\_polarizacao\_q52.md}
$$

completa esse ponto no nível da redução assintótica: a média de spin e
polarização é a completude dos projetores físicos \(P_\gamma\) e \(P_s\) no
canal Dirac--Bismut/Hopf, não uma regra externa adicionada à seção de choque.

Na GDQ, a soma correta deve vir de projetores físicos:

1. projetor fotônico transversal;
2. projetor de spin do sóliton eletrônico;
3. média sobre estados iniciais não polarizados;
4. soma sobre estados finais não observados.

O projetor fotônico é a restrição da Hessiana ao kernel massless protegido:

$$
P_\gamma
=
P_{\rm phys}^{U(1)}
-
P_{\rm long}
-
P_{\rm gauge}.
$$

Em notação assintótica, ele reduz ao projetor transversal usual:

$$
\sum_{\lambda=1}^{2}
\epsilon_\mu^{(\lambda)}(k)
\epsilon_\nu^{(\lambda)}(k)^*
=
\Pi_{\mu\nu}^{\perp}(k).
$$

O projetor de spin vem da circulação/Hopf do sóliton eletrônico, reconstruída
no limite Dirac–Bismut efetivo:

$$
P_s(p)
=
\text{projetor físico do modo Hopf }s=\pm\frac12.
$$

Na redução assintótica, isso coincide com a completude espinorial efetiva:

$$
\sum_s P_s(p)
\longrightarrow
\slashed p+m_e c.
$$

Assim, a soma não polarizada deve ser escrita como

$$
\overline{|\mathcal M_{\rm GDQ}|^2}
=
\frac12
\sum_{s,s'}
\frac12
\sum_{\lambda,\lambda'}
\left|
\mathcal M_{\rm GDQ}
(s,\lambda\to s',\lambda')
\right|^2.
$$

Depois da projeção física, o resultado reduzido é

$$
\boxed{
\overline{|\mathcal M|^2}
\propto
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta.
}
$$

Mais explicitamente, na redução assintótica:

$$
\frac12
\sum_s P_s(p)
\longrightarrow
\frac12(\slashed p+m_ec),
$$

e

$$
\sum_{\lambda=1}^{2}
\epsilon_\mu^{(\lambda)}(k)
\epsilon_\nu^{(\lambda)}(k)^*
=
\Pi_{\mu\nu}^{\perp}(k).
$$

A contração de traços resultante fornece o fator

$$
\boxed{
\mathcal T_{\rm KN}
=
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta.
}
$$

Portanto:

$$
\boxed{
\text{a soma spin/polarização está fechada na redução assintótica por
projetores físicos; a avaliação 8D direta permanece condicional.}
}
$$

## 6. A normalização da seção de choque é derivada?

Parcialmente.

A seção de choque deve ser a razão entre fluxo de probabilidade espalhado e
fluxo incidente, ambos definidos pela corrente de Noether/Madelung reconstruída:

$$
J^\mu
=
\rho\,v^\mu.
$$

Para um estado assintótico normalizado,

$$
d\sigma
=
\frac{\text{fluxo final em }d\Omega}
{\text{fluxo incidente}}.
$$

A integração da delta de conservação e o Jacobiano cinemático produzem

$$
\left(\frac{E'}{E}\right)^2.
$$

A normalização absoluta exige o acoplamento \(U(1)\) e o raio clássico efetivo:

$$
r_e
=
\frac{e^2}{4\pi\varepsilon_0m_ec^2}
=
\alpha\,\frac{\hbar}{m_ec}.
$$

Na GDQ, \(\alpha\) vem da Q37 e \(m_e\) da hierarquia/escala leptônica vigente.
Então, dentro dessas hipóteses já registradas,

$$
\boxed{
r_e^2
=
\alpha^2
\left(
\frac{\hbar}{m_ec}
\right)^2
}
$$

não é novo parâmetro.

O teste de normalização é o limite de baixa energia:

$$
x=\frac{E}{m_ec^2}\to0,
\qquad
\frac{E'}{E}\to1.
$$

Nesse limite, Klein–Nishina deve reduzir a Thomson:

$$
\boxed{
\frac{d\sigma}{d\Omega}
\to
\frac{r_e^2}{2}
(1+\cos^2\theta).
}
$$

O script

$$
\texttt{questoes/q52/associados/calcular\_klein\_nishina\_q52.py}
$$

verifica esse limite. Para \(\theta=90^\circ\), a diferença relativa decai
linearmente:

$$
x=10^{-3}:\ -1{,}996007\times10^{-3},
$$

$$
x=10^{-4}:\ -1{,}999600\times10^{-4},
$$

$$
x=10^{-5}:\ -1{,}999960\times10^{-5},
$$

$$
x=10^{-6}:\ -1{,}999996\times10^{-6}.
$$

Portanto, a normalização é consistente com o limite clássico. O que ainda não
foi feito é calcular o prefator absoluto diretamente do vértice
\(\mathcal V_{\gamma e\gamma}^{\rm eff}\), sem usar a forma conhecida de
\(r_e\) como atalho.

## 7. Fórmula final na redução assintótica

Com os blocos acima, a redução assintótica fornece:

$$
\boxed{
\frac{d\sigma}{d\Omega}
=
\frac{r_e^2}{2}
\left(
\frac{E'}{E}
\right)^2
\left[
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta
\right].
}
$$

com

$$
\boxed{
\frac{E'}{E}
=
\frac{1}
{1+\frac{E}{m_ec^2}(1-\cos\theta)}.
}
$$

Essa é a fórmula de Klein–Nishina.

## 8. Respostas diretas às quatro perguntas

| Pergunta | Resposta GDQ | Status |
| --- | --- | --- |
| A amplitude vem da ação? | Sim como estrutura: Hessiana física, propagador e vértices variacionais da ação oficial. O apêndice legado não calcula todos os blocos. | Condicional |
| Como canais \(s,u\) aparecem? | Como dois ramos do propagador físico do sóliton, reduzindo a \(1/(2p\cdot k)\) e \(1/(-2p\cdot k')\). | Fechado estruturalmente |
| Como polarizações e spin são somados? | Por projetores físicos \(P_\gamma\) e \(P_s\). O adendo fecha a redução assintótica; falta a avaliação 8D direta. | Fechado estruturalmente; metrologia condicional |
| A normalização é derivada? | A normalização por fluxo e limite Thomson é consistente; o prefator absoluto requer avaliar o vértice GDQ diretamente. | Condicional |

## 9. Status lógico

A Q52 fica classificada como:

$$
\boxed{
\text{fechada estruturalmente e condicionalmente.}
}
$$

Fechada estruturalmente porque:

1. a cinemática Compton é obtida por Noether;
2. os canais \(s/u\) são identificados como ramos do propagador físico;
3. a soma spin/polarização é obtida por projetores na redução assintótica;
4. a fórmula final é recuperada;
5. o limite Thomson é verificado numericamente.

Condicional porque o fechamento forte exige ainda:

1. calcular explicitamente \(\mathcal V_{\gamma e\gamma}^{\rm eff}\) da ação
   oficial;
2. construir \(P_\gamma\) e \(P_s\) diretamente no background 8D da Hessiana
   física do sóliton, não apenas na redução assintótica;
3. obter o prefator \(r_e^2\) como normalização de fluxo derivada, não como
   forma clássica importada.

Essas pendências não invalidam a correspondência Klein–Nishina; elas delimitam
o que ainda falta para transformar a correspondência assintótica em derivação
metrológica completa da GDQ.

## 10. Correção recomendada ao apêndice legado

O apêndice legado deve trocar a linguagem de derivação completa por linguagem
de redução assintótica.

Onde estiver implícito que a média de spin foi deduzida diretamente, substituir
por:

$$
\text{a média spin/polarização abaixo é a forma reduzida obtida após projetar
o setor físico assintótico; sua derivação completa requer os projetores
físicos da Hessiana GDQ.}
$$

E preservar a fórmula final como resultado correto da redução:

$$
\frac{d\sigma}{d\Omega}
=
\frac{r_e^2}{2}
\left(
\frac{E'}{E}
\right)^2
\left[
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta
\right].
$$

## 11. Como deve ser feito o fechamento completo

O fechamento completo da Q52 não exige mudar a ação oficial nem inserir uma
ação de QED. Ele exige executar a cadeia GDQ padrão no background eletrônico.

### 11.1 Construir o background eletrônico estacionário

Primeiro, fixar o sóliton eletrônico como solução estacionária admissível da
ação oficial:

$$
\Phi_e^*
=
(g_e^*,J_e^*,H_e^*,f_e^*,\mathcal U_e^*).
$$

Esse background deve satisfazer:

1. normalização da medida;
2. carga \(U(1)_Q\) unitária;
3. circulação/Hopf correspondente a spin \(1/2\);
4. massa \(m_e\) herdada da hierarquia leptônica vigente;
5. contorno causal compatível com a ponte global--local.

### 11.2 Calcular a Hessiana física

Em seguida, calcular a segunda variação da ação oficial:

$$
K_e
=
\left.
\operatorname{Hess}_{\Phi}\mathcal S_{\rm GDQ}
\right|_{\Phi_e^*}.
$$

Remover modos de gauge, modos longitudinais e modos de contorno redundantes:

$$
K_e^{\rm phys}
=
P_{\rm phys}K_eP_{\rm phys}.
$$

O domínio deve incluir as condições de contorno do estômato eletrônico e o
comportamento assintótico plano.

### 11.3 Identificar o canal fotônico \(P_\gamma\)

O fóton é o modo massless protegido no canal \(U(1)_Q\). Portanto, deve-se
resolver:

$$
K_e^{\rm phys}\psi_\gamma=0
$$

no setor transversal e construir o projetor espectral:

$$
P_\gamma
=
\frac{1}{2\pi i}
\oint_{\Gamma_\gamma}
(z-K_e^{\rm phys})^{-1}\,dz.
$$

No limite assintótico, esse projetor deve reduzir a:

$$
P_\gamma
\longrightarrow
\Pi_{\mu\nu}^{\perp}(k).
$$

Esse passo prova que as polarizações do fóton são herdadas da Hessiana física,
não colocadas à mão.

### 11.4 Identificar o projetor de spin \(P_s\)

O spin deve ser obtido a partir dos dois modos estáveis de circulação/Hopf do
sóliton eletrônico. Formalmente, deve-se diagonalizar o operador de circulação
do contorno:

$$
\mathcal H_{\rm Hopf}\psi_s
=
s\,\psi_s,
\qquad
s=\pm\frac12.
$$

O projetor é:

$$
P_s
=
|\psi_s\rangle\langle\psi_s|.
$$

No limite Dirac--Bismut assintótico,

$$
\frac12\sum_sP_s(p)
\longrightarrow
\frac12(\slashed p+m_ec).
$$

Esse passo transforma a média de spin em completude geométrica de modos de
circulação.

### 11.5 Calcular o vértice fóton--sóliton--fóton

A amplitude deve sair dos termos cúbicos e quárticos da ação oficial:

$$
\mathcal V_e^{(3)}
=
\left.
\frac{\delta^3\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*},
$$

$$
\mathcal V_e^{(4)}
=
\left.
\frac{\delta^4\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*}.
$$

A forma efetiva relevante é:

$$
\mathcal V_{\gamma e\gamma}^{\rm eff}
=
P_\gamma
\mathcal V_e^{(3)}
(K_e^{\rm phys})^{-1}
\mathcal V_e^{(3)}
P_\gamma
+
P_\gamma
\mathcal V_e^{(4)}
P_\gamma.
$$

Os dois termos com \((K_e^{\rm phys})^{-1}\) devem gerar os ramos \(s\) e \(u\).
O termo quártico/contato deve garantir transversalidade e conservação de
Noether.

### 11.6 Obter a amplitude assintótica

Projetando nos estados físicos:

$$
\mathcal M_{\rm GDQ}
(s,\lambda\to s',\lambda')
=
\langle
\psi_{s'}\otimes\epsilon'_{\lambda'},
\mathcal V_{\gamma e\gamma}^{\rm eff}
\psi_s\otimes\epsilon_\lambda
\rangle.
$$

O limite assintótico correto deve produzir:

$$
\mathcal M_{\rm GDQ}
\longrightarrow
\mathcal M_{\rm KN}.
$$

Critério explícito:

$$
\overline{|\mathcal M_{\rm GDQ}|^2}
\propto
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta.
$$

### 11.7 Derivar o prefator \(r_e^2\) por fluxo

Por fim, a normalização da seção de choque deve ser obtida como razão entre
fluxo final e fluxo incidente:

$$
\frac{d\sigma}{d\Omega}
=
\frac{d\Phi_{\rm out}/d\Omega}{\Phi_{\rm in}}.
$$

Os fluxos devem ser calculados com a corrente GDQ reconstruída:

$$
J^\mu_{\rm GDQ}
=
\rho v^\mu.
$$

O prefator deve emergir como:

$$
r_e^2
=
\alpha^2
\left(
\frac{\hbar}{m_ec}
\right)^2,
$$

usando \(\alpha\) da Q37 e \(m_e\) da hierarquia leptônica, não como parâmetro
novo.

### 11.8 Testes finais

O fechamento completo deve verificar:

1. limite Thomson:

   $$
   \frac{d\sigma}{d\Omega}
   \to
   \frac{r_e^2}{2}(1+\cos^2\theta);
   $$

2. deslocamento Compton:

   $$
   \frac{E'}{E}
   =
   \frac{1}
   {1+\frac{E}{m_ec^2}(1-\cos\theta)};
   $$

3. transversalidade:

   $$
   k_\mu\mathcal M^{\mu\nu}=0,
   \qquad
   k'_\nu\mathcal M^{\mu\nu}=0;
   $$

4. independência de gauge auxiliar;
5. comparação angular com dados experimentais de espalhamento Compton.

Se esses passos forem executados, a Q52 poderá ser promovida de
“fechada estruturalmente” para:

$$
\boxed{
\text{Klein--Nishina derivada metrologicamente pela GDQ.}
}
$$

Até lá, o status correto permanece:

$$
\boxed{
\text{redução Klein--Nishina fechada; fechamento 8D completo em refinamento.}
}
$$

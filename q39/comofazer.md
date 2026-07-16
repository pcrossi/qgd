# Como fazer direito a Questão 39

> **Status atualizado:** este arquivo é histórico/metodológico. A rota
> escolhida para fechar a Q39 foi refinada depois: a massa de repouso física
> é definida pelo espectro global regular em \(S^3\), isto é, pelo caso
> Reg-Reg em \([0,\pi]\). O estômato finito Robin-Regularidade é tratado como
> perturbação local de contorno, não como a definição primária da massa.
> A derivação final está em `fechamento_variacional_q39.md` e a consolidação
> em `../questão_39.md`.

## 1. Objetivo

Fechar a hierarquia leptônica significa demonstrar que as massas de
\(e,\mu,\tau\) são autovalores estáveis de um único operador geométrico global:

\[
L_\ell\Phi_n=\hat\lambda_n\Phi_n,
\qquad
M_n c^2=E_{\rm tens}(T^5\times S^3)\sqrt{\hat\lambda_n}.
\]

Com calibração por \(M_e\), o teste físico fica:

\[
\frac{M_\mu}{M_e}
=
\sqrt{\frac{\hat\lambda_\mu}{\hat\lambda_e}},
\qquad
\frac{M_\tau}{M_e}
=
\sqrt{\frac{\hat\lambda_\tau}{\hat\lambda_e}}.
\]

O alvo numérico é:

\[
\sqrt{\hat\lambda_\mu/\hat\lambda_e}\simeq206.768,
\qquad
\sqrt{\hat\lambda_\tau/\hat\lambda_e}\simeq3477.15.
\]

Mas esses números não podem ser usados para escolher os parâmetros do
operador. Eles só podem ser usados no fim, como teste.

---

## 2. O que a simulação atual já tem de aproveitável

O arquivo `solve_hierarchy.py` contém uma rota boa:

1. usa o background global \(T^5\times S^3\);
2. substitui o potencial local \(1/r\) pelo potencial cotangente em \(S^3\);
3. reduz o problema radial a um operador tipo Rosen--Morse trigonométrico;
4. tenta comparar os autovalores com \(M_\mu/M_e\) e \(M_\tau/M_e\);
5. tenta validar numericamente o operador por diferenças finitas.

Isso foi a direção certa no estágio de auditoria. A resolução final separou
duas camadas:

1. espectro global Reg-Reg, que define as massas de repouso;
2. estômato finito, que descreve correções locais de contorno.

---

## 3. Problemas da versão atual

### 3.1 Problema histórico: parâmetros ajustados ao CODATA

O próprio `adendo_q39.md` diz:

\[
\text{“Realizando a otimização dos parâmetros espectrais para reproduzir as razões de massa do CODATA”.}
\]

Isso foi removido da versão final.

Os parâmetros:

\[
\sigma=-0.988409297473,
\qquad
b=0.000121790025
\]

não podem ser escolhidos porque reproduzem:

\[
206.768,\qquad 3477.15.
\]

Eles precisam ser derivados de:

1. geometria do estômato;
2. condição de Robin;
3. monodromia fermiônica;
4. potencial cotangente em \(S^3\);
5. tensão global \(E_{\rm tens}(T^5\times S^3)\);
6. volumes/invariantes de \(T^5\times S^3\);
7. ação oficial GDQ.

### 3.2 Problema histórico: validação numérica inicial falhava

Rodando `solve_hierarchy.py`, a parte analítica dá:

\[
\frac{M_\mu}{M_e}=206.768002,
\qquad
\frac{M_\tau}{M_e}=3477.150041.
\]

Mas a parte de diferenças finitas dá:

\[
\frac{M_\mu}{M_e}=290.311600,
\qquad
\frac{M_\tau}{M_e}=3470.168245.
\]

O erro do múon é aproximadamente:

\[
40.4\%.
\]

Essa versão foi substituída por resolvedores regularizados e comparadores de
domínio. O comparador mostrou que o erro residual vinha do contorno truncado,
não do operador.

### 3.3 Problema histórico: mapeamento antigo \(n=(1,2,18)\)

A versão antiga identificava:

\[
e\leftrightarrow n=1,
\qquad
\mu\leftrightarrow n=2,
\qquad
\tau\leftrightarrow n=18.
\]

Mas ainda falta demonstrar por que o tau deve ser \(n=18\), e não outro modo.

Esse número precisa sair de uma regra topológica ou espectral, por exemplo:

1. saturação das três direções espaciais;
2. degenerescência angular em \(S^3\);
3. representação de \(SU(2)\);
4. restrição de Hopf;
5. produto entre ciclos internos e modos radiais;
6. condição de estabilidade sob o fluxo.

Na versão final, a indexação foi reescrita como:

\[
e\leftrightarrow n=0,\qquad
\mu\leftrightarrow n=1,\qquad
\tau\leftrightarrow n=17.
\]

O valor \(17\) é tratado como mapeamento topológico/radial a ser entendido
junto da degenerescência holonômica do setor global.

### 3.4 A prova de três gerações ainda mistura índice e modo radial

A tese:

\[
N_{\rm ger}=|h^{1,1}-h^{2,1}|=3
\]

pode explicar por que há três famílias.

Mas ela não explica automaticamente por que essas famílias correspondem aos
modos radiais:

\[
n=1,\quad n=2,\quad n=18.
\]

É preciso uma ponte:

\[
\text{classe topológica da geração}
\longrightarrow
\text{condição de contorno}
\longrightarrow
\text{modo espectral selecionado}.
\]

---

## 4. Como fazer corretamente

### Passo 1 — Congelar o operador antes de olhar os dados

Defina o operador completo:

\[
L_\ell
=
-e^{f_*}D_A^\dagger e^{-f_*}D_A
+\frac14\mathcal R_*
+\mathcal V_T
+\mathcal V_B
+\mathcal V_{\partial}
+V_{S^3}(r).
\]

Com:

\[
V_{S^3}(r)
=
-\kappa\frac1R\cot(r/R).
\]

Depois faça a redução radial:

\[
-\phi''(\chi)
+\left(
\frac{C_{\csc}}{\sin^2\chi}
-\kappa\cot\chi
\right)\phi
=
\lambda\phi.
\]

O operador precisa ser fixado antes de comparar com as massas.

### Passo 2 — Derivar \(C_{\csc}\)

O termo:

\[
\frac{C_{\csc}}{\sin^2\chi}
\]

não pode ser escolhido arbitrariamente.

Ele deve sair de uma decomposição angular em \(S^3\). Para uma esfera
tridimensional, o Laplaciano radial contém termos angulares associados a
representações de \(SU(2)\).

O trabalho necessário é mostrar uma relação do tipo:

\[
C_{\csc}=j(j+1)+C_{\rm spin}+C_{\rm torção},
\]

ou outra expressão equivalente derivada da geometria.

Se \(C_{\csc}=1/4\) for mantido, deve haver prova de que esse valor é imposto
pela monodromia fermiônica/spin \(1/2\), e não por conveniência numérica.

### Passo 3 — Derivar \(\kappa\)

O acoplamento cotangente:

\[
\kappa
\]

deve vir da carga geométrica do lépton no fundo global.

Rotas possíveis:

1. integral de fluxo do setor \(U(1)\) em \(T^5\times S^3\);
2. impedância de Fano/Fredholm do estômato;
3. normalização do Green em \(S^3\);
4. tensão do tecido cosmológico;
5. acoplamento da conexão de Bismut ao ciclo fermiônico.

O valor de \(\kappa\) não pode ser obtido minimizando erro contra
\(M_\mu/M_e\) e \(M_\tau/M_e\).

### Passo 4 — Derivar \(\epsilon\)

Na versão atual:

\[
\epsilon=1+\sigma\simeq0.0115907.
\]

Isso equivale a fazer o raio do estômato depender diretamente do parâmetro
que ajusta o espectro.

A forma correta é derivar \(\epsilon\) de uma condição geométrica:

1. raio mínimo do estômato;
2. condição de cirurgia;
3. corte de Cartan;
4. volume excluído no \(S^3\);
5. regularidade da densidade \(\rho=e^{-(f+\bar f)/2}\);
6. condição de normalização do modo fundamental.

Depois disso, \(\sigma\) deve ser consequência de \(\epsilon\), não entrada
livre.

### Passo 5 — Derivar \(\sigma\) da condição de Robin

Para operador de Sturm--Liouville em intervalo:

\[
\chi\in[\epsilon,\pi-\epsilon],
\]

com Robin:

\[
\phi'(\epsilon)+\beta_1\phi(\epsilon)=0,
\qquad
\phi'(\pi-\epsilon)+\beta_2\phi(\pi-\epsilon)=0,
\]

o shift espectral \(\sigma\) deve sair da equação secular:

\[
F(\lambda;\epsilon,\beta_1,\beta_2,C_{\csc},\kappa)=0.
\]

Então:

\[
\sigma=\sigma(\epsilon,\beta_1,\beta_2,C_{\csc},\kappa).
\]

A versão atual faz o inverso: escolhe \(\sigma\) e depois escolhe
\(\beta_1,\beta_2\).

Isso precisa ser invertido.

### Passo 6 — Derivar \(\beta_1,\beta_2\)

As impedâncias Robin:

\[
\beta_1,\qquad\beta_2
\]

devem ser calculadas a partir da ação de contorno.

Rota mínima:

1. variar a ação oficial em um domínio com fronteira;
2. manter os termos de bordo;
3. identificar a condição natural:

   \[
   n^AD_A\Phi+\kappa_\ell\Phi=0;
   \]

4. expressar \(\kappa_\ell\) em termos de \(f_*,g_*,\mathcal T,A\);
5. projetar isso nos dois extremos radiais para obter \(\beta_1,\beta_2\).

Sem isso, \(\beta_1,\beta_2\) são parâmetros livres.

### Passo 7 — Derivar o mapeamento das gerações

Antes de calcular massas, definir a regra:

\[
\text{geração }a
\longmapsto
n_a.
\]

Hoje temos:

\[
n_e=1,\qquad n_\mu=2,\qquad n_\tau=18.
\]

Isso precisa ser provado.

Uma rota possível:

\[
n_a
=
n_{\rm radial}(a)\times d_{\rm angular}(a)\times d_{\rm interno}(a),
\]

onde os fatores vêm de:

1. representação angular em \(S^3\simeq SU(2)\);
2. ciclo fermiônico \(S^1\);
3. degenerescência do setor \(T^4\);
4. condição de Hopf;
5. classe topológica da geração.

Se o valor \(18\) aparecer, ele deve surgir de uma contagem desse tipo.

### Passo 8 — Resolver o espectro sem usar massas

Depois de fixar:

\[
C_{\csc},\quad \kappa,\quad \epsilon,\quad \beta_1,\quad \beta_2,
\quad n_e,\quad n_\mu,\quad n_\tau,
\]

resolver:

\[
L_\ell\Phi_n=\hat\lambda_n\Phi_n.
\]

Só então comparar:

\[
\sqrt{\hat\lambda_\mu/\hat\lambda_e}
\quad\text{e}\quad
\sqrt{\hat\lambda_\tau/\hat\lambda_e}
\]

com os valores experimentais.

### Passo 9 — Validar por dois métodos independentes

Não basta a fórmula analítica.

Precisamos que:

1. solução analítica Rosen--Morse;
2. diferenças finitas;
3. método espectral;
4. variação de malha;
5. teste de convergência;

produzam o mesmo espectro.

Critério mínimo:

\[
\left|
\frac{r_{\rm num}-r_{\rm ana}}{r_{\rm ana}}
\right|
<10^{-3}
\]

para múon e tau.

Hoje isso falha para o múon.

### Passo 10 — Provar estabilidade

A estabilidade não deve ser apenas declarada por:

\[
N_{\rm ger}=3.
\]

É necessário mostrar:

\[
\delta^2S_{\rm GDQ}[\Phi_n]\ge0
\]

para os três modos admitidos e:

\[
\delta^2S_{\rm GDQ}[\Phi_4]<0
\]

ou não normalizabilidade para modos extras.

---

## 5. Como corrigir o script

### 5.1 Separar entrada geométrica de alvo experimental

O script deve ter dois blocos:

1. `derive_parameters_from_geometry()`;
2. `compare_with_experiment()`.

O primeiro não pode receber massas experimentais.

### 5.2 Remover otimização contra CODATA

Não usar:

\[
M_\mu/M_e,\quad M_\tau/M_e
\]

para escolher:

\[
\sigma,\ b,\ \epsilon,\ \beta_1,\ \beta_2,\ C_{\csc},\ \kappa.
\]

### 5.3 Implementar teste de convergência

Rodar para:

\[
N=200,\ 400,\ 800,\ 1600.
\]

Registrar:

\[
\lambda_1(N),\quad\lambda_2(N),\quad\lambda_{18}(N).
\]

Se os valores não convergirem para a fórmula analítica, a discretização ou a
fórmula analítica não estão representando o mesmo problema.

### 5.4 Testar as condições de Robin corretamente

O script atual altera a diagonal da matriz manualmente. Isso pode não
representar a condição de Robin contínua usada na fórmula analítica.

Implementar pelo menos duas discretizações:

1. eliminação por ghost point;
2. matriz de Sturm--Liouville com forma fraca;
3. método espectral Chebyshev.

Os três devem concordar.

### 5.5 Não subtrair \(1\) sem derivação

Hoje:

\[
\hat\lambda_n=\lambda_n-1.
\]

Esse deslocamento precisa ser derivado da curvatura de \(S^3\), da
normalização do Laplaciano, ou do termo \(\frac14\mathcal R_*\). Caso
contrário é mais um parâmetro implícito.

---

## 6. Critério histórico de fechamento da Q39

Este era o critério de fechamento usado durante a fase exploratória. Ele foi
preservado aqui apenas como registro metodológico, pois serviu para separar
quais pontos pertenciam ao espectro global e quais pertenciam a correções
locais de contorno.

Durante a revisão posterior, a Q39 foi fechada no sentido preciso de
**espectro global/topológico de massa de repouso**, usando o domínio completo
\([0,\pi]\) com condições naturais de regularidade nos dois polos
\(\text{Reg-Reg}\). Nesse enquadramento, o estômato finito
Robin-Regularidade não define a massa de repouso: ele descreve uma perturbação
local de tamanho finito.

O critério histórico exigia:

1. operador global fixado pela ação;
2. \(C_{\csc}\) derivado;
3. \(\kappa\) derivado;
4. \(\epsilon\) derivado;
5. \(\beta_1,\beta_2\) derivados;
6. \(\sigma\) derivado da equação secular;
7. mapeamento \(n_e,n_\mu,n_\tau\) derivado;
8. espectro analítico e numérico concordantes;
9. razões leptônicas previstas antes de comparar com CODATA;
10. prova de estabilidade para três gerações;
11. prova de exclusão dos demais modos.

Na formulação final, esses itens foram reorganizados assim:

1. os itens necessários ao espectro global foram documentados em
   `fechamento_variacional_q39.md`;
2. os itens dependentes do estômato finito foram classificados como setor
   local/correção posterior;
3. a massa física de repouso ficou definida pelo espectro Reg-Reg global.

Portanto, a classificação exploratória anterior foi substituída pela
classificação final:

\[
\boxed{
\text{Q39 fechada como espectro global/topológico de massa de repouso.}
}
\]

---

## 7. Próximos trabalhos posteriores

Os trabalhos posteriores, já fora do fechamento principal da Q39, são:

1. derivar diretamente da expansão variacional completa os coeficientes
   efetivos usados no vestimento geométrico;
2. formalizar a correção térmica do ciclo \(S^1_\beta\) como resposta local
   do vácuo cosmológico;
3. aprofundar a exclusão dos demais modos por monodromia, topologia e
   estabilidade espectral.

O arquivo técnico `derivacao_parametros_q39.md` documenta a rota atualmente
usada para \(\epsilon\), \(C_{\csc}\), \(\kappa\), \(\beta_1\), \(\beta_2\) e
\(\sigma\).

Sem usar massas experimentais.

Depois disso, o script pode ser reescrito para testar a previsão real.

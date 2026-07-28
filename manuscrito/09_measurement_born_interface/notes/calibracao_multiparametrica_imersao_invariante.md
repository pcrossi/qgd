---
title: "Calibração multiparamétrica por imersão invariante"
---

# Calibração multiparamétrica por imersão invariante

## 1. Enunciado e estatuto

Pretende-se construir a resposta calibrável de um aparelho sem alterar a ação
fundamental da teoria que descreve o objeto. Na GDQ, a ação oficial fornece a
dinâmica do bulk; fonte, material, geometria e contorno do aparelho são dados
externos do problema.

O resultado desta nota é exato no setor quadrático em torno de um background
admissível e estável. Aplicações não lineares exigem atualizar o background ou
reter ordens superiores.

## 2. Expansão quadrática e gaussiana

Se $\Phi_*(\boldsymbol\lambda)$ é um background conjunto e $\eta$ uma
flutuação física, então:

$$
\mathcal S[\Phi_*+\eta;J]
=
\mathcal S[\Phi_*]
+\frac12\langle\eta,K_{\rm phys}\eta\rangle
-\langle J,\eta\rangle
+O(\eta^3),
$$

com:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\operatorname{Hess}_{\Phi_*}\mathcal S
P_{\rm phys}.
$$

Numa discretização finita:

$$
S^{(2)}
=
\frac12\eta^{\mathsf T}K\eta-J^{\mathsf T}\eta.
$$

Completando o quadrado:

$$
S^{(2)}
=
\frac12
(\eta-K^{-1}J)^{\mathsf T}
K
(\eta-K^{-1}J)
-\frac12J^{\mathsf T}K^{-1}J.
$$

Se $K>0$ no subespaço físico,

$$
\int_{\mathbb R^N}
\exp\!\left[-\frac{S^{(2)}}{\hbar}\right]d^N\eta
=
\frac{(2\pi\hbar)^{N/2}}{\sqrt{\det K}}
\exp\!\left[
\frac{1}{2\hbar}J^{\mathsf T}K^{-1}J
\right].
$$

No contínuo, o determinante só existe depois da definição do domínio e de uma
regularização espectral. A identidade finita não autoriza um determinante
formal sem essas escolhas.

## 3. Eliminação do interior

Separe dados de interface $q$ e modos internos $y$:

$$
S^{(2)}
=
\frac12q^{\mathsf T}K_{qq}q
+q^{\mathsf T}K_{qy}y
+\frac12y^{\mathsf T}K_{yy}y
-J_q^{\mathsf T}q
-J_y^{\mathsf T}y.
$$

A equação interna fornece:

$$
y_*
=
K_{yy}^{-1}(J_y-K_{yq}q).
$$

Substituindo-a na ação, a forma quadrática de interface é governada por:

$$
\boxed{
\mathsf R
=
K_{qq}
-
K_{qy}K_{yy}^{-1}K_{yq}
}.
$$

Esse é o complemento de Schur e, no problema de bordo correspondente, o
operador de Dirichlet-to-Neumann. Se $K$ é positivo e $K_{yy}$ é inversível,
$\mathsf R$ também é positivo.

## 4. Riccati como Schur diferencial

Considere:

$$
u'
=
A_{11}u+A_{12}p,
$$

$$
p'
=
A_{21}u+A_{22}p.
$$

Defina $p=\mathsf Ru$. Então:

$$
p'
=
\mathsf R'u+\mathsf Ru'.
$$

Substituindo o sistema e eliminando $u$:

$$
\boxed{
\mathsf R'
=
A_{21}
+A_{22}\mathsf R
-\mathsf R A_{11}
-\mathsf R A_{12}\mathsf R
}.
$$

A equação de Riccati é, portanto, a versão diferencial da condensação
sucessiva por Schur.

## 5. Exemplo escalar verificável

Para:

$$
S^{(2)}
=
\frac12\int_0^L
\left[
a(u')^2+Vu^2
\right]ds
+\frac12R_0u(0)^2,
$$

temos:

$$
-au''+Vu=0.
$$

Definindo:

$$
R
=
a\frac{u'}{u},
$$

segue:

$$
R'
=
V-\frac{R^2}{a}.
$$

Com $m=\sqrt{V/a}$:

$$
\boxed{
R(L)
=
am
\frac{R_0+am\tanh(mL)}
{am+R_0\tanh(mL)}
}.
$$

Essa solução permite testar, sem dados experimentais, a equivalência entre
solução analítica, integração de Riccati e condensação discreta por Schur.

## 6. Extensão multiparamétrica

Considere:

$$
\frac{\partial\mathsf R}{\partial\lambda_i}
=
\mathcal F_i(\mathsf R,\boldsymbol\lambda).
$$

A condição correta de compatibilidade não é apenas comutar derivadas
explícitas. Como $\mathcal F_i$ depende de $\mathsf R$, a curvatura dos fluxos
é:

$$
\Omega_{ij}
=
\partial_i\mathcal F_j
-\partial_j\mathcal F_i
+D_{\mathsf R}\mathcal F_j[\mathcal F_i]
-D_{\mathsf R}\mathcal F_i[\mathcal F_j].
$$

Se:

$$
\Omega_{ij}=0,
$$

o transporte é localmente independente do caminho no espaço de parâmetros.
Se $\Omega_{ij}\neq0$, a ordem da preparação produz resposta diferente. Isso
pode representar histerese, memória ou controles fisicamente não
comutativos; não deve ser eliminado por ajuste.

## 7. Identificabilidade

Dados $D_a$ e covariâncias $\Sigma_a$, defina:

$$
\chi^2(\boldsymbol\lambda)
=
\sum_a
r_a^{\mathsf T}\Sigma_a^{-1}r_a,
\qquad
r_a
=
D_a-\mathcal O_a(\boldsymbol\lambda).
$$

O estimador é:

$$
\widehat{\boldsymbol\lambda}
=
\operatorname*{arg\,min}_{\boldsymbol\lambda}
\chi^2(\boldsymbol\lambda).
$$

O Jacobiano observacional é:

$$
J_{ai}
=
\frac{\partial\mathcal O_a}{\partial\lambda_i}.
$$

Na aproximação local, a matriz de informação é:

$$
\mathcal I
=
J^{\mathsf T}\Sigma^{-1}J.
$$

Posto completo implica identificabilidade local. Posto deficiente implica uma
família degenerada de aparelhos indistinguíveis pelos dados disponíveis.
Mais casas decimais ou um otimizador diferente não resolvem essa
degenerescência; é necessário um novo observável.

## 8. Protocolo de inferência

1. definir teoria, background, domínio, fonte e contorno;
2. derivar $P_{\rm phys}$ e $K_{\rm phys}$;
3. calcular $\mathsf R_{\rm app}(\boldsymbol\lambda)$;
4. verificar estabilidade e compatibilidade dos fluxos;
5. definir previamente $D_{\rm cal}$ e $D_{\rm test}$;
6. estimar $\widehat{\boldsymbol\lambda}$ apenas em $D_{\rm cal}$;
7. congelar parâmetros;
8. calcular observáveis em $D_{\rm test}$;
9. relatar sensibilidade, convergência e resíduos;
10. classificar o resultado como calibração, comparação ou previsão.

## 9. Aplicação fora da GDQ

O método usa estruturas matemáticas gerais:

$$
\text{operador linearizado}
\to
\text{Schur/DtN}
\to
\text{imersão}
\to
\text{identificabilidade}
\to
\text{teste}.
$$

Logo, pode ser utilizado com elasticidade, Maxwell em meios, acústica,
óptica, transporte, gravidade linearizada ou outra teoria variacional. O
conteúdo físico continua pertencendo à teoria de partida. A estrutura comum
não autoriza importar operadores de uma teoria para outra.

O complemento de Schur, a resposta DtN, o fluxo de Riccati, a imersão
invariante e a análise de informação não são invenções individuais da GDQ.
O conteúdo proposto aqui é o protocolo que os encadeia, preservando a origem
variacional do operador e separando calibração de validação. Sua novidade
comparativa deve ser avaliada contra a literatura antes de qualquer
reivindicação histórica.

## 10. Benchmark com césio

No experimento de Fein et al., a corrente $I$ é a coordenada física do
aparelho no regime linear. A resposta integrada da bobina é:

$$
C(I)
=
(10{,}3\ {\rm G\,m/A})I+L^2G_0,
\qquad
L=0{,}98\ {\rm m}.
$$

Para $^{133}{\rm Cs}$:

$$
\phi_{m_F}(v,I)
=
\frac{2\pi}{d}
\frac{m_Fg_F\mu_B}{m_{\rm Cs}v^2}
C(I),
$$

$$
\frac{V(I)}{V_0}
=
\frac{
\left|
\int_0^\infty
\rho(v)
\sum_{F,m_F}
\cos[\phi_{m_F}(v,I)]\,dv
\right|
}{16}.
$$

Foram usadas as distribuições skew-normal publicadas:

| série nominal | localização | escala | forma |
|---:|---:|---:|---:|
| $270\ {\rm m/s}$ | $228\ {\rm m/s}$ | $118\ {\rm m/s}$ | 4,4 |
| $380\ {\rm m/s}$ | $290\ {\rm m/s}$ | $171\ {\rm m/s}$ | 2,1 |

Os centros dos marcadores foram extraídos do PDF vetorial. Como não são os
dados brutos nem incluem a tabela original de covariâncias, a comparação não
recebe interpretação de qui-quadrado metrológico.

O gradiente de fundo foi calibrado nos índices pares da série rápida:

$$
G_0^{\rm cal}
=
0{,}35035948\ {\rm G/m}.
$$

O artigo informa $0{,}4\ {\rm G/m}$ no ajuste do conjunto completo. Com o
parâmetro congelado:

| conjunto | RMSE | viés |
|---|---:|---:|
| calibração rápida | 0,022693 | -0,010751 |
| teste rápido retido | 0,022753 | -0,003857 |
| série lenta independente | 0,023745 | -0,000433 |

O erro de validação permanece no nível do erro de calibração. Isso constitui
evidência inicial de generalização do método instrumental, não uma validação
exclusiva da ontologia GDQ.

Verificações reproduzíveis:

- [[../scripts/saida_verificar_imersao_calibracao|Consistência entre solução
  analítica, Riccati e Schur]];
- [[../scripts/resultado_benchmark_cs_fein2022|Calibração e validação com
  césio]].

## 11. Limitações

- A Hessiana deve ser avaliada num background físico, não num fixture.
- Modos nulos devem ser projetados antes de inverter $K_{yy}$.
- Perdas exigem resposta causal/retardada, não apenas Hessiana euclidiana.
- Termos não lineares exigem continuação do background.
- Um único registro não identifica vários parâmetros degenerados.
- O benchmark de césio usa o canal magnético operacional publicado.
- Evento individual, Born e irreversibilidade não são derivados apenas por
  calibração.

## 12. Conclusão

O método separa quatro objetos:

$$
\boxed{
\text{constantes da teoria}
\neq
\text{parâmetros do aparelho}
\neq
\text{parâmetros numéricos}
\neq
\text{dados de validação}
}.
$$

Seu resultado central é transformar a calibração num problema geométrico de
resposta, composição e interseção identificável, preservando a teoria física
de partida.

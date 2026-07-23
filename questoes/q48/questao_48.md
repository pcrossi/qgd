# Questão 48 — Hidrogênio

## 1. Enunciado

A questão pede uma resposta GDQ para o átomo de hidrogênio que contenha:

1. equação espinorial correta;
2. espectro;
3. degenerescências;
4. estrutura fina;
5. estrutura hiperfina;
6. Lamb shift;
7. dependência do raio do próton;
8. comparação sem ajuste posterior.

A restrição central do enunciado é:

$$
\boxed{
\text{uma equação escalar ajustada para reproduzir Sommerfeld não substitui a
equação de Dirac.}
}
$$

Portanto, a Q48 não pode ser fechada apenas com a equação radial escalar do
Capítulo 38 legado.

---

## 2. Fontes e dependências já consolidadas

### 2.1 Fonte legada direta

O arquivo principal legado é:

$$
\texttt{pt-br/38 - A Geometria do Atomo de Hidrogenio.md}.
$$

Ele contém três blocos aproveitáveis:

1. limite de campo fraco e fórmula tipo Sommerfeld--Dirac;
2. campo próximo, termos tipo Heun/Hill e interpretação geométrica do Lamb
   shift;
3. acoplamento bidirecional solitônico e raio efetivo no hidrogênio muônico.

### 2.2 Dependências GDQ já disponíveis

1. **Spin e estrutura espinorial** — Q26:

   $$
   \psi\in\Gamma(S\otimes E),
   \qquad
   \{\gamma^a,\gamma^b\}=2\eta^{ab}.
   $$

   O spin não pode ser substituído por circulação escalar inteira. A circulação
   dá interpretação geométrica; a equação correta exige fibrado spin e
   Clifford.

2. **Constante de estrutura fina** — Q37:

   $$
   \alpha_{\rm lab}=\alpha_E^{\rm mean}
   $$

   condicionalmente ao ensemble isotrópico de Einstein e à ponte global--local.
   Em Q48, $\alpha$ deve entrar como dado já derivado/transportado, não como
   parâmetro ajustado ao espectro do hidrogênio.

3. **Próton** — Q40:

   O próton é um background bariônico composto, com carga, spin, raio efetivo e
   fatores de forma de superfície tratados como resultados/reduções do setor
   bariônico. Em Q48, o próton não deve ser substituído por uma carga pontual
   sem declarar a aproximação.

4. **Zeeman e momento magnético mínimo** — Q43:

   A parte mínima $g=2$ é protegida por Noether na normalização magnética
   mínima. A anomalia pertence ao canal interno da Hessiana física. Isso entra
   em estrutura fina, hiperfina e correções magnéticas.

5. **Ponte global--local** — Capítulo 6 e tópicos associados:

   Permite herdar normalizações globais para setores localizados com gap, mas
   não autoriza pós-ajustar parâmetros atômicos.

---

## 3. Auditoria do Capítulo 38 legado

### 3.1 O que é aproveitável

O Capítulo 38 fornece uma equação radial efetiva:

$$
\frac{d^2 \mathcal R}{dr^2}
+
\frac{2}{r}\frac{d\mathcal R}{dr}
+
\left[
\frac{E^2-m_e^2c^4}{\hbar^2c^2}
+
\frac{2E\alpha}{\hbar c r}
-
\frac{\ell(\ell+1)-4\alpha^2}{r^2}
\right]\mathcal R=0.
$$

Ela é útil como:

$$
\boxed{
\text{limite radial efetivo, escalar e spin-projetado.}
}
$$

Também é aproveitável a análise por Frobenius, Kummer/Whittaker, Heun e
determinantes de Hill, desde que reclassificada como estudo do setor radial
após a seleção espinorial correta.

### 3.2 O que não é suficiente

A equação acima depende de $\ell$ e de uma correção torsional escalar. Isso
não resolve, por si só:

1. a estrutura de spin $1/2$;
2. a degenerescência correta em $j$ e $m_j$;
3. a álgebra de Clifford;
4. a separação entre $\ell=j\pm1/2$;
5. a estrutura hiperfina envolvendo o spin do próton;
6. o Lamb shift como efeito espectral de um operador espinorial com domínio e
   contorno definidos;
7. a dependência completa do raio do próton por fator de forma.

Logo:

$$
\boxed{
\text{o Capítulo 38 legado é uma base radial, não a resposta final da Q48.}
}
$$

---

## 4. Rota GDQ correta para a Q48

### 4.1 Cadeia mínima de fechamento

A cadeia exigida é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{p,*}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathcal D^{B}_{p,e}
\to
\text{domínio e contornos}
\to
\text{espectro estável}
\to
\text{observáveis atômicos}.
$$

Onde:

- $\Phi_{p,*}$ é o background bariônico/protônico da Q40;
- $\mathcal D^{B}_{p,e}$ é o operador espinorial efetivo Dirac--Bismut
  herdado da Hessiana física, não um operador de Dirac postulado como ação
  fundamental;
- o campo coulombiano é a projeção efetiva do modo $U(1)$ normalizado pela Q37;
- os contornos de curto alcance carregam raio do próton, fator de forma e
  impedância solitônica.

### 4.2 Equação espinorial efetiva esperada

No setor local reconstruído, a forma correta deve ser uma equação sobre
seções espinoriais:

$$
\psi\in\Gamma(S\otimes L_Q),
$$

com operador do tipo:

$$
\mathcal D_H\psi
=
\left[
i\hbar c\,\gamma^a e_a{}^\mu
\left(
\nabla_\mu^{B}
+
\frac{iQ}{\hbar c}A_\mu^{(p)}
\right)
-
m_ec^2
\right]\psi
=0.
$$

Classificação:

$$
\boxed{
\text{redução efetiva espinorial da Hessiana GDQ, não ação fundamental nova.}
}
$$

Aqui:

- $\nabla^B$ é a conexão espinorial com torção de Bismut;
- $A_\mu^{(p)}$ é o modo $U(1)$ efetivo gerado pelo background protônico;
- $Q=-e$ para o elétron;
- $m_e$ é a escala de repouso herdada do setor leptônico/metrológico;
- correções de curto alcance entram por domínio, contorno e resposta da
  Hessiana, não por potencial arbitrário inserido depois.

### 4.3 Limite de Coulomb e espectro líder

No limite:

1. próton pesado;
2. campo fraco;
3. raio do próton negligenciado;
4. torção residual reduzida ao acoplamento espinorial mínimo;
5. fundo local assintoticamente plano;

o operador deve reduzir ao problema espinorial central:

$$
A_0^{(p)}(r)
\simeq
\frac{e}{4\pi\varepsilon_0 r},
\qquad
\boldsymbol A^{(p)}\simeq0.
$$

O espectro líder esperado é o espectro de Sommerfeld--Dirac:

$$
E_{n\kappa}
=
m_ec^2
\left[
1+
\frac{(Z\alpha)^2}
{\left(
n-|\kappa|
+
\sqrt{\kappa^2-(Z\alpha)^2}
\right)^2}
\right]^{-1/2}.
$$

com:

$$
\kappa=
\begin{cases}
-(j+1/2), & j=\ell+1/2,\\
+(j+1/2), & j=\ell-1/2.
\end{cases}
$$

Esse é o ponto que a equação escalar do legado não entrega de forma suficiente:
a degenerescência correta é organizada por $n$, $j$ e $m_j$, não apenas por
$n$ e $\ell$.

---

## 5. Como cada item do enunciado deve ser tratado

| Item | Rota GDQ correta | Status inicial |
|---|---|---|
| Equação espinorial correta | Derivar $\mathcal D_H$ como redução da Hessiana física no background protônico | aberto |
| Espectro | Mostrar redução ao espectro Sommerfeld--Dirac em campo fraco | parcialmente estruturado |
| Degenerescências | Usar $\kappa,j,m_j$ e simetria central espinorial | aberto |
| Estrutura fina | Expansão do espectro espinorial em potências de $\alpha$ | estruturável |
| Estrutura hiperfina | Acoplamento Noether/circulação elétron--próton e momento magnético protônico da Q40/Q43 | aberto |
| Lamb shift | Determinante/Hessiana de campo próximo, domínio e fator de forma; não apenas termo escalar $1/r^3$ | aberto |
| Raio do próton | Inserir fator de forma/contorno de Q40 e comparar eletrônico vs muônico | parcialmente estruturado |
| Comparação sem ajuste | Congelar $\alpha$, $m_e$, $m_p$, $r_p$ e momentos antes da comparação | pendente |

---

## 6. Plano de execução cuidadoso

### Fase 1 — Auditoria e operador

1. extrair do Capítulo 38 apenas o que é radial/efetivo;
2. escrever a Hessiana linearizada do elétron no background protônico;
3. identificar o operador Dirac--Bismut efetivo;
4. definir domínio, medida, produto interno e contornos;
5. demonstrar a redução para Coulomb no limite fraco.

Produto:

$$
\texttt{questoes/q48/associados/operador_espinorial_hidrogenio.md}.
$$

### Fase 2 — Espectro e degenerescências

1. resolver o operador central por separação espinorial;
2. obter o espectro líder $E_{n\kappa}$;
3. listar degenerescências em $n,j,m_j$;
4. comparar com a fórmula escalar legada e registrar exatamente onde ela é
   insuficiente.

Produto:

$$
\texttt{questoes/q48/associados/espectro_degenerescencias.md}.
$$

### Fase 3 — Correções físicas

1. estrutura fina por expansão do espectro espinorial;
2. hiperfina por acoplamento magnético/circulatório elétron--próton;
3. Lamb shift por campo próximo e determinante/DtN da Hessiana;
4. raio do próton por fator de forma e contorno bariônico;
5. comparação sem pós-ajuste.

Produto:

$$
\texttt{questoes/q48/associados/correcoes_hidrogenio.md}.
$$

Plano detalhado de execução:

$$
\texttt{questoes/q48/associados/plano_solucao_completa_q48.md}.
$$

---

## 7. Fechamento após execução inicial

A execução inicial produziu os documentos e scripts necessários para fechar a
parte estrutural da questão. O veredito consolidado está em:

$$
\texttt{questoes/q48/fechamento_q48.md}.
$$

Status:

$$
\boxed{
\text{Q48 fechada estruturalmente; camada metrológica fina condicional.}
}
$$

O material legado foi aproveitado como limite radial efetivo. A crítica do
enunciado foi resolvida porque a resposta agora passa pela equação espinorial
Dirac--Bismut efetiva antes da redução radial. O ponto remanescente é a
avaliação direta de $\delta\mathcal D_{\rm near}$ da Hessiana de campo próximo
do próton, necessária para uma previsão sem ajuste do Lamb shift completo e
das correções finas de estrutura interna.

O operador de campo próximo foi formalizado como complemento de Schur em:

$$
\texttt{questoes/q48/associados/operador\_campo\_proximo\_deltaD\_near.md}.
$$

A comparação com o Modelo Padrão operacional foi registrada em:

$$
\texttt{questoes/q48/associados/saida\_comparacao\_gdq\_modelo\_padrao\_q48.md}.
$$

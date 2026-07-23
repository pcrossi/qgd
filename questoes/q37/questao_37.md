# Questão 37 — Como $\alpha$ é derivada?

> [!note] Impacto da ponte global--local
> A convergência apontada remove a incompatibilidade geométrica abstrata entre
> $T^5\times S^3$ e $\mathbb R^4\times T^4$. Contudo, $\alpha$ é uma
> normalização contínua: ainda se deve calcular a norma do modo
> eletromagnético com o complemento de Schur da Hessiana oficial. Ver
> `topicos/ponte_global_local/impacto_ponte_global_local_q37_q39_q40.md`.

## 1. Pergunta

A Questão 37 pergunta:

\[
\boxed{
\text{como a GDQ deriva a constante de estrutura fina }\alpha?
}
\]

O arquivo `37-0.md` exige:

1. definir o setor $U(1)$;
2. normalizar seu termo cinético;
3. normalizar a carga mínima;
4. demonstrar a relação entre operador geométrico e acoplamento;
5. especificar a escala efetiva de resolução;
6. calcular $\alpha(\mu)$.

Também exige explicar os números da fórmula antiga e retirar
`src/calculo_alpha_gdq.py` como evidência.

---

## 2. Resposta curta

Na **geometria oficial** da GDQ,

\[
\boxed{
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb C}M=4,
}
\]

a constante de estrutura fina $\alpha$ é a normalização efetiva de uma
**direção $U(1)$ selecionada no toro interno**. Essa direção, sua normalização
cinética e a carga mínima pertencem ao background espectral de
Ricci--Bismut.

O estado vigente separa dois níveis. A origem numérica cosmológica já está
determinada pela média de Einstein:

\[
\boxed{
\alpha_E^{\rm mean}
=
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4}
}
\]

e

\[
\boxed{
(\alpha_E^{\rm mean})^{-1}
=
137{,}036082448\ldots
}
\]

sem usar CODATA como entrada.

A ponte global--local demonstra o transporte condicional:

\[
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
\]

Portanto, se a normalização global é a média de Einstein, o laboratório herda:

\[
\boxed{
\alpha_{\rm lab}=\alpha_E^{\rm mean}.
}
\]

O loop final em
`questoes/q37/associados/fechamento_alpha_hessiana_loop.md` identifica essa
média com a Hessiana oficial média no ensemble isotrópico de Einstein. A
covariância por pullback torna a Hessiana escalar no subespaço físico de
quatro direções, e a contração Hopf/Haar fornece

\[
\mathcal P_{\rm iso}=\frac9{8\pi^4}.
\]

Logo a Q37 fica fechada condicionalmente nessa classe:

\[
\boxed{
\alpha_E^{\rm mean}=\alpha_E[Z_Q^E].
}
\]

A condicionalidade restante é a aplicabilidade do ensemble isotrópico de
Einstein ao background global real, não a existência do número.

---

## 3. Por que a derivação antiga deve ser reclassificada

Esta seção registra a crítica histórica à derivação antiga. Ela não deve ser
lida como rejeição do valor cosmológico final. A reinterpretação posterior em
termos de média de Einstein, lema de uniformidade do ensemble e projetor
isotrópico fecha condicionalmente a origem numérica; ver a seção 15.

### 3.1 Geometria local versus compactificação cosmológica

O Capítulo 29 e a Nota 29.1 usam \(T^5\times S^3\). A GDQ oficial usa
\(\mathbb R^4\times T^4\) como geometria local. Logo, os invariantes citados
— volume \(6\pi^5\), ordem \(1920\), fator \(5\) — não podem ser atribuídos
diretamente à base local.

A leitura correta é reclassificar \(T^5\times S^3\) como compactificação
cosmológica auxiliar:

\[
T^5\times S^3
\simeq
(S^1_{\rm tempo}\times S^3_{\rm Einstein})\times T^4_{\rm interno}.
\]

Essa estrutura pode ser relevante para o cálculo global de \(\alpha\), mas
não altera a ação oficial nem substitui \(\mathbb R^4\times T^4\).

### 3.2 Buckingham não determina valor numérico

O Teorema dos $\Pi$ mostra que

\[
\Pi_1=\frac{e^2}{4\pi\epsilon_0\hbar c}
\]

é adimensional. Mas ele **não explica** por que $\Pi_1\approx1/137$. A
identificação $\Pi_1=\alpha$ é uma escolha de normalização, não uma derivação
do valor.

### 3.3 A fórmula fechada é ad hoc

| Fator | Problema |
|---|---|
| $9/(8\pi^4)$ | Justificado por “razões de tensão” e “barreira de Bohm”, mas nenhum foi derivado da ação oficial. |
| $1920=4!\cdot2^4\cdot5$ | Não é invariante da base local; precisa ser justificado na compactificação cosmológica. |
| $\chi=5$ | Não pode ser característica de Euler do toro; se for usado, deve ser reinterpretado, por exemplo, como número de Betti/ciclos. |
| Raiz quarta | Escolhida para ajustar dimensões, não derivada. |
| Coincidência numérica | O valor bate porque a fórmula foi montada para isso. |

### 3.4 O script é circular

`src/calculo_alpha_gdq.py` injeta o valor-alvo:

```python
alpha_alvo = 1 / 137.035999084
tr_T2 = 2 * np.log(137.0)
lambda_1_sq = 1.0 - (1.0 / 137.0)
lambda_2_sq = 1.0 - (137.0 / 137.035999084)
```

O determinante reproduz o alvo **por construção**. Não é evidência de
derivação.

### 3.5 A série de Fredholm é circular

A expansão

\[
\alpha^{-1}=137+\text{Tr}(T^2)_{\rm res}-\text{Tr}(T^4)_{\rm res}+\dots
\]

usa traços calculados a partir de $137$, $6\pi^5$ e $1920$. Os resíduos
não são autovalores de um operador independente.

### 3.6 A Nota 29.1 ainda não é uma prova

A “prova de unicidade” de $T^5\times S^3$ ainda é heurística. Frases como “sem
torção a viscosidade decai a zero” e “a pressão geométrica de sela rasgaria o
tecido” são argumentos físicos, não demonstrações matemáticas.

---

## 4. Derivação na geometria oficial

### 4.1 Variedade e setor $U(1)$ efetivo

A variedade oficial é

\[
M=\mathbb R^4\times T^4,
\qquad
T^4=S^1_1\times S^1_2\times S^1_3\times S^1_4.
\]

As isometrias do toro geram quatro campos de Killing abelianos,
$\partial_{\theta_a}$, portanto um grupo de gauge interno

\[
\boxed{
U(1)^4.
}
\]

Para campos locais não triviais, introduzem-se conexões de Ehresmann

\[
\Theta^a=d\theta^a+g_aA^a,
\qquad a=1,2,3,4,
\]

com curvaturas

\[
F^a=dA^a.
\]

O eletromagnetismo efetivo é uma **combinação linear** dessas direções:

\[
\boxed{
A_{\rm em}=v_aA^a,
\qquad v\in\mathbb R^4.
}
\]

A direção $v$ não é arbitrária: ela é selecionada pelo background espectral.
No setor antiperiódico padrão, $\boldsymbol\varepsilon_F=(1,0,0,0)$, o modo
fundamental carrega carga apenas na primeira direção do toro. A direção
física do eletromagnetismo é, portanto, a direção do ciclo-relógio
$\theta_1$.

---

### 4.2 Normalização do termo cinético

A ação efetiva 4D para o setor gauge, conforme a Questão 2, é

\[
\boxed{
S_{\rm gauge}
=-\frac14\int_N G_{ab}\,F^a_{\mu\nu}F^{b\,\mu\nu}\sqrt{-h}\,d^4x.
}
\]

A matriz $G_{ab}$ é a **métrica efetiva no espaço das conexões**.
Para o toro plano com métrica interna

\[
g_{T^4}=\sum_aR_a^2d\theta_a^2,
\]

a redução da ação 8D fornece, em primeira aproximação,

\[
G_{ab}=\frac{\operatorname{Vol}(T^4)}{\kappa_8^2}\,g_{ab}^{\rm int},
\]

onde $\kappa_8$ é a constante de acoplamento da ação octodimensional e
$g_{ab}^{\rm int}$ é a métrica induzida no espaço das 1-formas de conexão.
A forma exata depende da normalização da ação 8D e deve ser derivada do
funcional de Perelman-Bismut.

Para a direção eletromagnética $A_{\rm em}=v_aA^a$, o termo cinético reduz-se
a

\[
\boxed{
S_{\rm em}
=-\frac14\int_N \frac{1}{g_{\rm em}^2}\,
F_{\rm em,\mu\nu}F_{\rm em}^{\mu\nu}\sqrt{-h}\,d^4x,
}
\]

com

\[
\boxed{
\frac{1}{g_{\rm em}^2}=v_a v_b\,G^{ab}.
}
\]

Aqui $G^{ab}$ é a inversa de $G_{ab}$. A normalização do termo cinético está,
portanto, inteiramente na geometria: $G_{ab}$ fixa $g_{\rm em}$.

Em termos dos raios internos $R_a$ e da constante 8D $\kappa_8$, a ordem de
grandeza é

\[
\frac{1}{g_{\rm em}^2}\sim\frac{R_1^2R_2R_3R_4}{\kappa_8^2}\,v_1^2.
\]

O fator exato requer a solução do background estacionário.

---

### 4.3 Carga mínima

Os modos espinoriais no toro satisfazem

\[
\psi_{\mathbf n}(\theta)
\propto
\exp\!\left[i\sum_a\left(n_a+\frac{\varepsilon_a}{2}\right)\theta_a\right].
\]

Os números de carga da rede dual são

\[
\boxed{
Q_a=n_a+\frac{\varepsilon_a}{2}.
}
\]

No setor físico antiperiódico escolhido,

\[
\boldsymbol\varepsilon_F=(1,0,0,0),
\]

o modo fundamental tem

\[
Q_1=\frac12,
\qquad
Q_2=Q_3=Q_4=0.
\]

A carga efetiva de um modo na direção eletromagnética é

\[
\boxed{
q_{\mathbf n}=g_{\rm em}\,v_aQ_a.
}
\]

Para que o modo fundamental carregue a carga elementar observada $e$,
impõe-se

\[
v_1\cdot\frac12=1
\quad\Longrightarrow\quad
\boxed{
v=(2,0,0,0).}
\]

Assim,

\[
\boxed{
q_{\mathbf n}=g_{\rm em}\,(2n_1+1),
\qquad
q_{\min}=g_{\rm em}=e.
}
\]

As cargas ao longo dessa direção são múltiplos ímpares de $e$. A carga
mínima é $e=g_{\rm em}$.

Essa quantização é consistente com a estrutura spinorial: a monodromia
antiperiódica impõe $Q_1\in\mathbb Z+1/2$, e a escolha $v_1=2$ mapeia o
modo fundamental na carga elementar observada.

---

### 4.4 Relação entre operador geométrico e acoplamento

O operador de Dirac–Bismut acoplado às conexões internas é

\[
\boxed{
\slashed D_{B,A}
=\gamma^\mu\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA^a_\mu
\right).
}
\]

Na direção eletromagnética,

\[
q_aA^a_\mu=q_{\rm em}A_{\rm em,\mu},
\qquad
q_{\rm em}=e=g_{\rm em}.
\]

Portanto o acoplamento que aparece no operador geométrico é exatamente o
mesmo $g_{\rm em}$ que normaliza o termo cinético:

\[
\boxed{
\slashed D_{B,A_{\rm em}}
=\gamma^\mu\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-ig_{\rm em}A_{\rm em,\mu}
\right).
}
\]

A consistência exige que o mesmo $g_{\rm em}$ apareça nos dois lugares. Isso
é garantido pela redução covariante da ação 8D.

---

### 4.5 Escala efetiva de resolução

A GDQ não usa renormalização fundamental por contratermos como princípio
ontológico. O parâmetro relevante é a escala efetiva de resolução associada
ao fluxo geométrico e ao corte de Cartan \(\Lambda_C\). Para comparar com a
linguagem perturbativa externa, pode-se introduzir uma escala operacional
\(\mu\), mas ela deve ser entendida como tradução efetiva, não como
fundamento da teoria.

A escala natural para o setor eletromagnético é

\[
\boxed{
\mu\sim\Lambda_C.
}
\]

Correções efetivas são suprimidas pela regularidade geométrica do corte de
Cartan. Em primeira aproximação,

\[
\boxed{
\alpha(\mu)=\frac{g_{\rm em}^2}{4\pi\hbar c}
\left[1+\mathcal O\!\left(\frac{\mu}{\Lambda_C}\right)\right].
}
\]

A escala $\Lambda_C$ é determinada pela estabilização do background de
Ricci–Bismut, não postulada externamente.

Se for feita uma comparação perturbativa externa com QFT, a dependência
operacional de escala pode ser representada formalmente por uma expressão
logarítmica:

\[
\alpha(\mu)=\alpha(\Lambda_C)
\left[
1+\frac{\beta_0}{2\pi}\,
\alpha(\Lambda_C)\,
\ln\!\left(\frac{\mu}{\Lambda_C}\right)
+\cdots
\right],
\]

onde $\beta_0$ é o coeficiente da função beta de uma teoria com o espectro
efetivo da GDQ na escala $\Lambda_C$. Essa função de escala é derivada, se
necessária, como descrição efetiva; ela não substitui o fluxo geométrico
\(\tau\) da ação oficial.

---

### 4.6 Fórmula estrutural para $\alpha(\mu)$

Combinando os itens anteriores, obtém-se a expressão estrutural

\[
\boxed{
\alpha(\mu)
=\frac{1}{4\pi\hbar c}\,
\frac{1}{v_a v_b\,G^{ab}_*}
\left[1+\mathcal O\!\left(\frac{\mu}{\Lambda_C}\right)\right],
}
\]

onde $G^{ab}_*$ é a métrica efetiva no background estacionário.

No setor antiperiódico padrão, com $v=(2,0,0,0)$, isso reduz-se a

\[
\boxed{
\alpha(\mu)
=\frac{1}{16\pi\hbar c\,G^{11}_*}
\left[1+\mathcal O\!\left(\frac{\mu}{\Lambda_C}\right)\right].
}
\]

O valor numérico só é obtido quando $G^{11}_*$ for calculado a partir de
$(g_*,B_*,f_*,R_{a,*})$.

---

## 5. Respostas às seis perguntas sobre os números antigos

1. **Por que $9/(8\pi^4)$?** Não há justificativa na geometria oficial. É um
   fator escolhido para ajustar o valor experimental.

2. **Por que $1920$?** Na geometria local oficial, não há grupo de holonomia
   relevante de ordem \(1920\). Se esse número for preservado, deve ser
   reconstruído na compactificação cosmológica \(T^5\times S^3\), por exemplo
   como simetria/ciclos globais, não como propriedade direta de
   \(\mathbb R^4\times T^4\).

3. **Qual grupo possui ordem $1920$?** Nenhum grupo relevante da geometria
   local oficial. O grupo de holonomia de \(T^4\) é trivial; o grupo de
   isometria interna é \(U(1)^4\). A identificação global fica pendente.

4. **Por que a característica usada vale $5$?** Ela não pode ser
   característica de Euler do toro. Se for mantida, deve ser reinterpretada
   como contagem homológica/ciclos na compactificação cosmológica.

5. **Qual variedade possui esses invariantes?** A candidata é
   \(T^5\times S^3\), agora tratada como compactificação cosmológica auxiliar.

6. **Por que a raiz quarta é necessária?** Para ajustar a dimensão da
   combinação ad hoc e forçar a coincidência numérica.

---

## 6. Ação sobre `src/calculo_alpha_gdq.py`

O script `src/calculo_alpha_gdq.py` **não deve mais ser citado como
evidence** de derivação de $\alpha$. Ele contém circularidade lógica:

```python
alpha_alvo = 1 / 137.035999084
tr_T2 = 2 * np.log(137.0)
lambda_1_sq = 1.0 - (1.0 / 137.0)
lambda_2_sq = 1.0 - (137.0 / 137.035999084)
```

Os autovalores e traços são calculados a partir do valor experimental alvo.
O determinante reproduz o alvo **por construção**.

Status recomendado:

\[
\boxed{
\text{Preservar como registro histórico, mas reclassificar como
simulação ilustrativa, não prova.}
}
\]

---

## 7. Status da Questão 37

A Questão 37 está **resolvida no nível estrutural** e possui **origem
numérica cosmológica determinada condicionalmente**. Permanece aberta a prova
mais forte por Hessiana oficial completa.

Resolvido:

- definição do setor $U(1)$ efetivo a partir de $U(1)^4$;
- normalização do termo cinético via métrica efetiva $G_{ab}$;
- normalização da carga mínima, $e=g_{\rm em}$, com $v=(2,0,0,0)$;
- relação entre operador de Dirac–Bismut e acoplamento;
- escala efetiva de resolução $\mu\sim\Lambda_C$;
- fórmula estrutural para $\alpha(\mu)$;
- reclassificação da derivação antiga como rota cosmológica auxiliar ainda
  não demonstrada, e identificação do script circular.

Ainda não resolvido:

- cálculo explícito de $G^{11}_*$ a partir do background de Ricci–Bismut;
- determinação numérica de $\Lambda_C$;
- cálculo das correções de running e do espectro efetivo;
- valor numérico de $\alpha$.

Portanto:

\[
\boxed{
\text{A estrutura da derivação de }\alpha\text{ está estabelecida; o
valor numérico depende da solução do problema espectral de
Ricci--Bismut.}
}
\]

---

## 8. Síntese da auditoria dos quatro pontos

Nesta seção consolidam-se os resultados da análise solicitada sobre a
geometria, o coeficiente de Kähler, o segundo script Python e a
monotonicidade do funcional $\mathcal W$.

### 8.1 Papel de $T^5\times S^3$ versus $\mathbb R^4\times T^4$

A geometria usada no Capítulo 29 e em `auditorias/respostas3.md`/`auditorias/respostas4.md` é

\[
T^5\times S^3,
\qquad
\dim_{\mathbb R}=8.
\]

Essa variedade possui:

- volume total $6\pi^5$;
- característica de Euler $\chi(T^5\times S^3)=\chi(T^5)\chi(S^3)=0\cdot0=0$;
- holonomia não trivial em $S^3$;
- isometrias $U(1)^5\times SO(4)$.

A GDQ oficial, fixada nas Questões 2 e 3 e na reconstrução `2/2_final.md`,
usa

\[
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}=8,
\qquad
\dim_{\mathbb C}=4.
\]

Essa variedade possui:

- volume infinito devido a $\mathbb R^4$;
- característica de Euler $\chi(T^4)=0$;
- holonomia trivial;
- isometrias do setor interno $U(1)^4$.

**Veredicto revisado:** \(T^5\times S^3\) **não substitui** a geometria
local oficial da GDQ. A base dinâmica da teoria continua sendo
\(\mathbb R^4\times T^4\), e a ação oficial permanece independente da
escolha de coordenadas.

Entretanto, \(T^5\times S^3\) pode ser reinterpretado como uma
**compactificação cosmológica auxiliar**, associada ao espaço cosmológico de
Einstein: o setor \(S^3\) representa a compactificação espacial global, o
ciclo adicional \(S^1\) representa a compactificação temporal/euclidiana ou
térmica, e o \(T^4\) preserva o setor interno oficial. Nessa leitura, a
variedade global é usada apenas para calcular invariantes integrados, como
uma possível rota para \(\alpha\), sem alterar a ação GDQ nem a geometria
local de propagação.

Portanto, os invariantes citados — volume \(6\pi^5\), ordem \(1920\) e o
fator \(5\) — não podem ser tratados como propriedades diretas de
\(\mathbb R^4\times T^4\). Eles devem ser rebaixados a dados da
compactificação cosmológica auxiliar e auditados nessa base.

A fórmula fechada

\[
\alpha=\frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{1/4}
\]

permanece **não demonstrada dentro da geometria local oficial**, mas não deve
ser descartada como rota futura se for reconstruída rigorosamente a partir
da compactificação cosmológica \(T^5\times S^3\).

### 8.2 Derivação de $\kappa_{\text{Kähler}}$ a partir de uma equação de movimento

A decomposição proposta em `auditorias/respostas4.md`,

\[
\kappa_{\text{Kähler}}
=\frac{9}{4}\cdot\frac12\cdot\frac{1}{\pi^4}
=\frac{9}{8\pi^4},
\]

é motivada fisicamente, mas **não foi derivada do funcional de
Perelman-Bismut**. Não existe, no funcional

\[
\mathcal W_B[g,B,f]
=\int_M\left[
\frac12|B|^2
+R+\frac12|df|^2
\right]e^{-f}\,dV
\]

ou em suas equações de Euler-Lagrange, nenhuma equação de estado cujo
tensor de tensões imponha a razão de cisalhamento $3/2$ e a atenuação de
Bohm $1/2$. A alegação de que

\[
\frac{\sigma_{ii}}{\sigma_{ij}}=\frac{n+1}{n}=\frac32
\]

para um fluido de Madelung incompressível em variedade de Kähler de
dimensão complexa $n=2$ é uma analogia da mecânica dos fluidos, não uma
consequência da ação da GDQ.

**Veredicto:** $\kappa_{\text{Kähler}}=9/(8\pi^4)$ **não é derivado** da
ação oficial. Na geometria $\mathbb R^4\times T^4$, o acoplamento
eletromagnético efetivo é dado pela métrica espectral $G^{ab}_*$, não por
um coeficiente de rigidez de Kähler postulado.

### 8.3 Verificação de `src/calculo_alpha_gdq_2.py`

O script `src/calculo_alpha_gdq_2.py` foi executado e verificado. Ele
calcula

\[
\alpha=\frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{1/4}
\]

e produz

\[
\alpha^{-1}=137.036082,
\qquad
\text{erro relativo}\approx6.1\times10^{-5}\%\text{ vs CODATA}.
\]

O script **não injeta o valor-alvo de $\alpha$** diretamente, ao contrário
de `calculo_alpha_gdq.py`. Contudo:

1. ele postula $\kappa_{\text{Kähler}}=9/(8\pi^4)$;
2. ele usa o volume $6\pi^5$ e a ordem $1920$, que só fazem sentido em
   $T^5\times S^3$;
3. ele não deriva nada da ação oficial em $\mathbb R^4\times T^4$.

**Veredicto:** o script é **correto aritmeticamente**, mas ainda não prova a
derivação física de \(\alpha\). Deve ser reclassificado como ilustração da
rota cosmológica \(T^5\times S^3\), não como evidência direta da geometria
local \(\mathbb R^4\times T^4\).

### 8.4 Monotonicidade de $\mathcal W$ com torção e Bohm

O Capítulo 17 afirma que o funcional de Perelman-Bismut

\[
\mathcal W_B[g,B,f]
\]

é monótono ao longo do fluxo de Ricci-Bismut. A fórmula estrutural é a
extensão natural da monotonicidade de Perelman para variedades com
torção:

\[
\frac{d}{dt}\mathcal W_B
=\int_M\left|
\operatorname{Ric}^B+\nabla^2f-\frac14H^2
\right|^2e^{-f}\,dV
+\text{(termos de sinal dependente das convenções)}.
\]

Para que a monotonicidade seja um teorema, é necessário verificar:

- o sinal da contribuição de $H$;
- a condição $dH=0$ (ou SKT: $\partial\bar\partial\omega=0$);
- a compatibilidade entre a conexão de Bismut e a estrutura complexa;
- a boa definicao das integrais em $\mathbb R^4\times T^4$.

Nenhuma dessas verificações foi apresentada no manuscrito de forma
independente.

**Veredicto:** a monotonicidade é **formalmente plausível**, mas **não
está demonstrada** no contexto específico da GDQ. É uma conjectura
estrutural, não um teorema.

---

## 9. Implicações para `auditorias/respostas3.md` e `auditorias/respostas4.md`

Os documentos `auditorias/respostas3.md` e `auditorias/respostas4.md` concluem que a Questão 9
(derivação de $\alpha$) está **resolvida** com grau "Muito Provável".
Essa conclusão baseia-se na fórmula fechada

\[
\alpha=\frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{1/4}.
\]

A análise acima mostra que essa resolução **ainda não fecha a GDQ oficial**:

1. a fórmula depende de \(T^5\times S^3\), entendido agora como
   compactificação cosmológica auxiliar, não como base local;
2. o coeficiente $\kappa_{\text{Kähler}}$ não é derivado da ação;
3. o script é aritmeticamente preciso, mas ainda não demonstra a ponte entre
   a compactificação cosmológica e a ação GDQ de contorno;
4. a monotonicidade de $\mathcal W_B$ não foi demonstrada.

Além disso, `auditorias/respostas4.md` propõe uma "integral explícita" que resulta
em $120$, não $137$, evidenciando o risco de *over-engineering* na
defesa do inteiro isolado.

**Conclusão atualizada:** a resolução apresentada em `auditorias/respostas3.md` e
`auditorias/respostas4.md` é uma **rota cosmológica auxiliar** para \(\alpha\). Ela não
altera a ação oficial nem a base local \(\mathbb R^4\times T^4\). O critério
preciso de transporte da normalização foi posteriormente demonstrado em
`topicos/ponte_global_local/teorema_heranca_normalizacao_eletromagnetica.md`; o que permanece aberto é
a avaliação global não circular e a verificação da hipótese física do canal
eletromagnético.

---

## 10. Próximos passos

O valor numérico cosmológico já é fornecido por
\(\alpha_E^{\rm mean}\). Para convertê-lo em avaliação direta da Hessiana
oficial, é necessário:

1. avaliar o background global estacionário de Ricci--Bismut em
   $T^5\times S^3$;
2. restringir a Hessiana oficial à direção primitiva $U(1)_Q$ e calcular o
   complemento de Schur $K_Q^{\rm eff}$;
3. extrair $Z_Q^E$ da corrente simplética ou da forma quadrática global;
4. verificar se o canal elétrico é localizado ou, sendo massless estendido,
   demonstrar ausência de fuga e convergência DtN/espalhamento;
5. identificar a média cosmológica de Einstein com $Z_Q^E$ sem inserir o valor
   experimental;
6. calcular separadamente respostas efetivas dependentes da resolução, caso
   sejam necessárias para comparação experimental.

Até que esses passos sejam completados, a Questão 37 permanece fechada
condicionalmente pela média cosmológica de Einstein e aberta apenas quanto à
verificação direta via Hessiana oficial completa.

---

## 11. Teorema condicional de herança da normalização

O documento `topicos/ponte_global_local/teorema_heranca_normalizacao_eletromagnetica.md` corrige uma
ambiguidade anterior. A corrente global de fase de $f$ é a corrente de
probabilidade de Madelung; ela não deve ser identificada diretamente com a
carga elétrica. O setor elétrico é a deformação horizontal gerada pela direção
interna primitiva $U(1)_Q$.

No espaço físico de perturbações, seu operador é

$$
K_Q^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}.
$$

A corrente simplética obtida da ação oficial contém o mesmo coeficiente $Z_Q$
que multiplica a forma quadrática eletromagnética. Se a ponte preserva essa
corrente, a normalização primitiva e a forma-relógio, sem fluxo lateral, então

$$
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
$$

Para modo ligado, a condição segue do gap, da localização e dos projetores dos
seis lemas. Para canal massless estendido, falta verificar a versão de
espalhamento: fluxo lateral nulo e convergência do DtN ou da matriz de
espalhamento normalizada por fluxo.

Assim, não se deve redeterminar $\alpha$ em cada carta laboratorial. A
pendência científica da Q37 é calcular $Z_Q^E$ uma única vez pela Hessiana
oficial global e verificar a condição apropriada do canal elétrico.

---

## 12. Avaliação direta de $Z_Q^E$

`questoes/q37/associados/derivacao_ZQ_global_acao_oficial.md` efetuou a redução quadrática da ação
oficial na direção primitiva $U(1)_Q$ e obteve

$$
Z_Q^E
=\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma\!\left[
\tau\int_K\mathcal U_*
\lVert\xi_Q\rVert^2dV_{q_*}
\right]
+\Delta Z_Q^E,
$$

onde $\Delta Z_Q^E$ é o complemento de Schur das flutuações físicas
ortogonais. A fórmula cosmológica histórica equivale, em unidades naturais,
a exigir

$$
Z_Q^E=10{,}904984951787\ldots
$$

A estrutura coincide: ambas pretendem normalizar o mesmo modo $U(1)_Q$.
Contudo, a igualdade numérica ainda não foi demonstrada porque o background
global e o complemento de Schur não foram inseridos diretamente nessa
integral. Em particular, a normalização de $\mathcal U$ impede contar um
volume compacto bruto duas vezes.

A execução dos backgrounds forneceu a norma radial não canonizada
$\mathcal K_Q=41{,}594825709\ldots$. Ela não é diretamente $Z_Q$. A matriz de
Gram fornece o fator exato $1/4$ por gerador, mas a diagonalização neutra no
background radial ainda resulta em $Z_\gamma=15{,}1626057595\ldots$, não no
$Z_Q^E=10{,}904984951787\ldots$ exigido pela fórmula candidata. A comparação
correta é

$$
\alpha_E
=\frac{(\mathbf q_{\min}^{T}v_\gamma)^2}
{4\pi\hbar c\,v_\gamma^T\mathbf Z v_\gamma}.
$$

Portanto havia realmente um erro de normalização, mas sua correção não fecha
o background radial. A projeção causal de uma inserção steady suave também se
anula.

Um teste posterior compôs esse kernel radial com o DtN sem ajuste do primeiro
harmônico em duas extensões pela 4-bola. A geometria fornece

$$
K_\partial^{\rm DtN}=\pi^2R^2=39{,}4157186074\ldots
$$

e o complemento de Schur produz

$$
\alpha_{\rm DtN}^{-1}=137{,}604601779\ldots.
$$

O erro em $Z_Q$ cai para $0{,}414868\%$, sem usar $\alpha$ como entrada, e a
Hessiana permanece positiva. Esse diagnóstico selecionava o DtN
warped--Bismut completo como rota local faltante antes da releitura por média
cosmológica. Após a seção 15, a aproximação de 4-bola redonda deve ser lida
como teste de escala da interface, não como substituto da média global de
Einstein.
Ver `questoes/q37/associados/rota_schur_dtn_global.md`.

---

## 13. Canal fotônico massless

`questoes/q37/associados/teorema_canal_fotonico_massless.md` formulou o transporte correto sem
tratar o fóton como modo $L^2$ localizado. A identidade de Ward fornece
$m_\gamma=0$; a comutação da Hessiana com $U(1)_Q$ fecha o canal; e a corrente
simplética conserva sua normalização. Para $\omega>0$, a convergência dos
coeficientes da ponte implica convergência dos operadores DtN.

No elo normal oficial $(B^4,S^3)$, o possível modo zero espúrio também pode ser
excluído. O problema homogêneo

$$
K_Q^{\rm eff}A=0,
\qquad
d^*A=0,
\qquad
A|_Y=0.
$$

tem forma de energia positiva na Hessiana física projetada. Portanto $dA=0$;
como $A$ é coclosed e satisfaz condição relativa, ele define uma classe em
$H^1(B^4,S^3)$. Pela dualidade de Poincaré--Lefschetz,

$$
H^1(B^4,S^3)\simeq H_3(B^4)=0,
$$

e o kernel físico é trivial. Assim, sob a positividade já exigida da Hessiana
projetada,

$$
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
$$

O transporte global--local do canal fotônico fica fechado condicionalmente.
A pendência numérica de Q37 continua sendo outra: calcular o DtN
warped--Bismut completo e obter o valor absoluto de $Z_Q^E$ sem a aproximação
redonda.

---

## 14. Identificação da fórmula cosmológica histórica

`questoes/q37/associados/identificacao_formula_cosmologica_hessiana.md` auditou diretamente os
fatores da expressão histórica. O inteiro $1920$ possui uma identificação
algébrica natural como grupo de simetria da rede — não como holonomia —,

$$
1920=|W(D_5)|=2^4 5!,
$$

mas somente o estabilizador simultâneo de $(J,H,f,\mathcal U,Q)$ pode dividir
a integral física. Como a estrutura axial distingue um dos cinco ciclos,
usar $4!2^4\cdot5$ sem calcular os órbitos pode contar cinco vezes uma escolha
já fixada. Além disso, um quociente finito produz um fator volumétrico linear,
não automaticamente a raiz quarta presente na fórmula.

Logo a fórmula histórica continua sendo uma conjectura geométrica, embora a
estimativa DtN sem ajuste a corrobore em escala e sinal. A identidade final
exige calcular o autovalor DtN warped--Bismut; o valor diagnóstico requerido é

$$
K_{\partial,{\rm hist}}=38{,}835771227928\ldots.
$$

O refinamento com warp escalar também foi encerrado para métrica induzida
fixa. Em quatro dimensões, $\int F\wedge\star F$ é conformalmente invariante, de
modo que $g_{\rm WB}=e^{2A}g_{\rm red}$ preserva a rigidez integrada. Na
truncagem disponível, $Z(\eta)F^2$ não produz bloco escalar--fóton em torno de
$A_Q=0$. Portanto, nessa classe redonda/conformal, o resultado final é

$$
K_\partial=39{,}415718607388\ldots,
\qquad
\alpha^{-1}=137{,}604601779\ldots.
$$

A fórmula histórica não é obtida nessa classe. Ward não exclui sozinho uma
mistura transversal gauge-invariante com uma 2-forma torsional. Uma nova
tentativa exige calcular esse bloco ou um background normal Hermitiano
anisotrópico diretamente da ação oficial.

---

## 15. Leitura como média cosmológica de Einstein

O documento `questoes/q37/associados/interpretacao_media_einstein_formula_legada.md` preserva o
sentido geométrico da fórmula legada sem confundi-la com o DtN de uma única
interface. A quantidade

$$
\frac{\pi^5}{1920}
$$

é interpretada como peso angular de uma câmara fundamental do ensemble
$T^5/W(D_5)$, e sua raiz quarta como a média geométrica dos quatro autovalores
físicos do tensor de complacência global. O fator $9/(8\pi^4)$ é o projetor
isotrópico normalizado que leva esse tensor ao canal elétrico escalar.

Nessa leitura, a fórmula é exata para a prescrição de média definida, mas seu
estatuto na GDQ é condicional: ainda se deve identificar essa prescrição com
a contração explícita da Hessiana global.

A uniformidade foi demonstrada no lema de ensemble do mesmo documento. A
covariância por pullback torna a energia livre constante na órbita completa de
$W(D_5)$; Noether conserva os fluxos da componente contínua e a parte discreta
preserva sua rede. Pela transitividade,

$$
Z_E=1920e^{-\beta_EF_0},
\qquad
p_a=\frac1{1920}.
$$

Equivalentemente, para câmaras que são descrições redundantes, a integral no
quociente é $1/1920$ da integral no recobrimento. Esse ponto foi isolado em
`questoes/q37/associados/fechamento_alpha_hessiana_loop.md` como lema de
ensemble: o fator $1920$ é lícito quando a órbita cosmológica inteira é
transportada por pullback, mas não quando um eixo externo é congelado antes da
média.

O projetor foi obtido no setor axial coerente como prescrição cinemática de
média, não ainda como contração completa da Hessiana oficial. O quarto momento de Haar em
$S^3$ fornece

$$
\langle(n\cdot u)^4\rangle=\frac18.
$$

O traço coerente das três direções Cartan--Schouten entra ao quadrado e
fornece $3^2=9$; a normalização da câmara angular física divide por $\pi^4$.
Logo

$$
\mathcal P_{\rm iso}=\frac9{8\pi^4}.
$$

A fórmula cosmológica fica fechada condicionalmente à isotropia do ensemble e
à seleção do autovetor Hopf axial coerente.

O loop posterior em
`questoes/q37/associados/fechamento_alpha_hessiana_loop.md` completou esse
cálculo no ensemble isotrópico de Einstein. A covariância por pullback da ação
oficial implica que a Hessiana média comuta com a órbita de \(W(D_5)\). No
subespaço físico de quatro direções, o lema de Schur reduz a Hessiana a
\(\lambda_E\mathbf 1_4\); logo \(K_{\rm phys}^{-1}\) cancela na razão que
define o projetor.

Resta a contração angular/torsional:

$$
\mathcal P_{\rm iso}
=
\frac9{8\pi^4}
$$

que segue de

$$
\frac1{\pi^4}
\left\langle(n\cdot u)^4\right\rangle_{S^3}
\left(\operatorname{Tr}_{\rm CS}\mathbf 1_3\right)^2
=
\frac1{\pi^4}\frac18\,3^2.
$$

Assim,

$$
\boxed{
\alpha_E^{\rm mean}
=
\alpha_E[Z_Q^E]
}
$$

fica demonstrada como teorema condicional da Hessiana média de Einstein. A
condicionalidade restante é de classe de background: órbita cosmológica
completa, isotropia estatística e autovetor Hopf axial coerente.

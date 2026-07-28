---
title: "Provas, lemas e definições — Capítulo 9"
---

# Provas, lemas e definições — Capítulo 9

Esta nota reúne a cadeia técnica do Capítulo 9. O ponto central é separar três
camadas:

1. a densidade geométrica positiva da GDQ;
2. a regra operacional de Born no Hilbert físico reconstruído;
3. a dinâmica real de aparelho, interface, decoerência e registro.

Nenhuma dessas camadas altera a ação oficial. O aparelho entra como dado
clássico de fonte, vínculo ou contorno de um problema físico.

## 1. Densidade geométrica e setor local regular

A definição constitutiva vigente é

$$
\rho=e^{-(f+\bar f)/2}.
$$

A fase real é

$$
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

No setor local regular, define-se a representação projetiva

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Logo,

$$
|\Psi|^2=\rho.
$$

Essa identidade é importante, mas seu alcance é limitado: ela identifica a
densidade espacial em uma representação regular. Ela não escolhe a base de um
detector e não prova, sozinha, Born para qualquer observável.

## 2. Born operacional no Hilbert físico reconstruído

Depois da reconstrução do espaço físico, uma medição operacional é uma medida
em uma família de projetores ortogonais

$$
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I.
$$

Uma regra de probabilidade operacional deve satisfazer:

1. positividade, $\mu(P)\ge0$;
2. normalização, $\mu(I)=1$;
3. aditividade em projetores ortogonais;
4. não contextualidade operacional para o mesmo projetor;
5. compatibilidade com composição e marginais.

No espaço de Hilbert físico complexo, essas condições levam à forma

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

Para estado puro $\varrho=|\psi\rangle\langle\psi|$,

$$
\mu(P_i)=\langle\psi|P_i|\psi\rangle.
$$

Se $P_i=|i\rangle\langle i|$,

$$
\mu(P_i)=|\langle i|\psi\rangle|^2.
$$

No caso de posição, para uma região $R$,

$$
P(R)=\int_R\rho\,d\mu_h.
$$

Portanto Born é fechada estruturalmente como regra operacional no Hilbert
físico reconstruído. A GDQ permanece mais profunda que essa camada: ela ainda
precisa dizer como o aparelho define os projetores reais.

### Certificação do setor puro finito

O módulo [FiniteBorn.lean](../../../formal/GDQ/FiniteBorn.lean) prova, para
uma base ortonormal finita $\{\phi_i\}$,

$$
p_i
=
\left|\langle\phi_i,\psi\rangle\right|^2
\ge0,
$$

$$
\sum_i p_i
=
\lVert\psi\rVert^2.
$$

Assim, para $\lVert\psi\rVert=1$, os pesos somam exatamente $1$ e cada peso
de um canal unitário está em $[0,1]$. Isso certifica Born no setor puro
finito. Não substitui Gleason/POVMs gerais nem a derivação dinâmica dos
projetores do aparelho.

### Certificação do setor misto projetivo finito

O módulo [MixedBornTrace.lean](../../../formal/GDQ/MixedBornTrace.lean)
formaliza também

$$
p_i
=
\operatorname{Tr}(\varrho P_i)
$$

para uma matriz densidade finita normalizada e uma família projetiva que
resolve a identidade. O código prova

$$
0\le p_i\le1,
\qquad
\sum_i p_i=1.
$$

A positividade de $\operatorname{Tr}(\varrho P_i)$ aparece como hipótese
espectral explícita, correspondente a $\varrho\ge0$ e $P_i\ge0$. Portanto a
formalização não finge derivar a positividade física apenas da condição de
traço, nem substitui Gleason, POVMs gerais ou a dinâmica de seleção do
aparelho.

### Certificação do teorema assintótico reduzido

O módulo
[MeasurementAsymptotic.lean](../../../formal/GDQ/MeasurementAsymptotic.lean)
prova que, para $\Delta>0$,

$$
C e^{-\Delta\tau}
\longrightarrow
0,
$$

e que qualquer coerência dominada em módulo por esse envelope também converge
a zero. O mesmo módulo certifica a repetibilidade ideal quando a projeção
idempotente preserva o peso condicionado não nulo.

Ele não deriva a autoadjunticidade ou o gap da Hessiana de um aparelho
concreto, nem a existência das bacias Morse responsáveis por um resultado
individual.

## 3. Aparelho como fonte, vínculo ou contorno

Um aparelho clássico não é um operador quântico inserido na teoria. Ele fornece
dados físicos:

$$
J_{\rm app}^{\rm classico},
\qquad
C_{\rm app},
\qquad
\partial M_{\rm app}.
$$

A cadeia correta da GDQ é

$$
J_{\rm app}^{\rm classico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{resposta espectral}
\to
\text{registro}.
$$

O background com aparelho é uma solução estacionária do problema variacional
com esses dados de contorno:

$$
\left.
\frac{\delta}
{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+\mathcal S_{\rm fonte/contorno}
\right)
\right|_{\Phi_*}
=0.
$$

O termo $\mathcal S_{\rm fonte/contorno}$ não é nova ação fundamental. Ele
codifica o fato físico de que o experimentalista construiu um aparelho com
campos, materiais e fronteiras específicas.

## 4. Hessiana física e resposta de interface

No background $\Phi_*$, a Hessiana física projetada é

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_*}
P_{\rm phys}.
$$

O projetor $P_{\rm phys}$ remove vínculos, redundâncias de gauge e modos de
Noether que não correspondem a deformações observáveis do registro.

Separe os graus de liberdade em fronteira $\partial$ e interior $I$:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

O interior estacionário satisfaz

$$
K_{I\partial}\delta\Phi_\partial
+K_{II}\delta\Phi_I=0.
$$

Se $K_{II}$ é inversível no setor físico,

$$
\delta\Phi_I
=-K_{II}^{-1}K_{I\partial}\delta\Phi_\partial.
$$

Substituindo, a resposta efetiva vista na interface é

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Essa é a forma Schur/DtN da impedância do aparelho. Ela contém geometria,
rigidez, perdas e material. Não é parâmetro fundamental novo.

## 5. Decoerência como redução efetiva

Se alternativas macroscópicas $i$ e $j$ induzem respostas de aparelho
distintas, a coerência reduzida tem a forma

$$
\rho_{ij}^{\rm red}(t)
=
\rho_{ij}^{\rm red}(0)\,e^{-\Gamma_{ij}(t)}.
$$

Em um regime com gap de medição $\Delta_{\rm meas}$,

$$
|\rho_{ij}^{\rm red}(t)|
\le
C\,e^{-\Delta_{\rm meas}t}.
$$

Isso explica a supressão operacional das interferências entre registros. Ainda
assim, decoerência não é, por si só, resultado individual único; ela torna
robusta a decomposição macroscópica.

O script `scripts/simular_decoerencia_sae.py` verifica essa queda em um modelo
reduzido $S+A+E$ e explicita que o teste é efetivo.

## 6. Resultado único por bacias reais

Um evento individual exige bacias reais da microgeometria
objeto--aparelho--ambiente. Seja $\mathfrak F_{\rm meas}$ o funcional efetivo
de medição no setor aberto reduzido. Um registro $R_i$ é estável se

$$
\nabla\mathfrak F_{\rm meas}(R_i)=0,
\qquad
\operatorname{Hess}_{R_i}^{\rm phys}\mathfrak F_{\rm meas}>0.
$$

A bacia associada é

$$
\mathcal B_i
=
\left\{
\Phi_0:
\lim_{t\to\infty}\Phi(t;\Phi_0)=R_i
\right\}.
$$

Se as fronteiras entre bacias são variedades estáveis de selas, elas têm
medida nula. Então quase toda condição inicial microscópica cai em uma única
bacia. Para uma dinâmica arbitrária, a compatibilidade com Born exige

$$
\mu_{\rm micro}(\mathcal B_i)
=
\operatorname{Tr}(\varrho P_i).
$$

No setor QND gaussiano, essa igualdade deixa de ser uma hipótese independente.
A Hessiana bloco-diagonal, a integração gaussiana dos modos de saída e a
separação acumulada dos sinais fornecem:

$$
dp_i
=
p_i\sum_a(s_i^a-\bar s^a)d\widetilde W^a,
$$

portanto $p_i$ é martingal. Como a distinguibilidade assintótica força
$p_i(\infty)=\mathbf1_{\{I_\infty=i\}}$, segue:

$$
\mu_{\rm path}(\mathcal B_i)
=
\operatorname{Tr}(\varrho_0P_i).
$$

A prova completa e suas hipóteses estão em
[[teorema_born_bacias_qnd_gaussiano|Teorema Born–bacias para aparelhos QND gaussianos]].

## 7. Emaranhamento e no-signalling no setor reduzido

Emaranhamento é não fatoração do estado físico no espaço de configuração. No
setor de Hilbert reconstruído, para o singlete ideal,

$$
E(\mathbf a,\mathbf b)=-\mathbf a\cdot\mathbf b.
$$

As marginais locais são independentes do eixo remoto:

$$
\sum_{\beta=\pm1}
p(\alpha,\beta|\mathbf a,\mathbf b)
=
p(\alpha|\mathbf a).
$$

O script `scripts/verificar_emaranhamento_no_signalling.py` verifica, no setor
reduzido ideal:

- valores de Schmidt $0.707106781187,0.707106781187$;
- erro máximo em $E+\mathbf a\cdot\mathbf b$ igual a $0$;
- variações marginais locais iguais a $0$;
- valor CHSH ideal $-2.828427124746$.

Esse teste confirma consistência operacional reduzida. Ele não substitui a
Hessiana multipartida de aparelhos reais.

## 8. Extensões não-Hermitianas

Ao eliminar graus de liberdade não observados de um aparelho dissipativo, o
operador efetivo de registro pode ser não-Hermitiano. Isso não significa que a
ação oficial se tornou não-Hermitiana. Significa apenas que o setor observado
é aberto.

Esquematicamente,

$$
K_{\rm eff}(z)
=
K_{QQ}
-K_{QI}(K_{II}-z)^{-1}K_{IQ}.
$$

Se o complemento possui canais dissipativos ou contínuos, $K_{\rm eff}$ pode
ter parte imaginária efetiva. Essa é uma extensão de dinâmica aberta e pertence
à metrologia de aparelhos reais.

## 9. Scripts autocontidos do capítulo

| Script | Papel | Classificação |
|---|---|---|
| `verificar_born_projetores.py` | Positividade, aditividade, mudança de base, composição e marginais. | Teste operacional. |
| `verificar_emaranhamento_no_signalling.py` | Singlete, CHSH e marginais. | Teste reduzido. |
| `simular_decoerencia_sae.py` | Supressão exponencial de coerências. | Redução efetiva. |
| `resposta_detector_schur.py` | Cálculo de $\mathsf R_{\rm app}$ e $\Gamma_{\rm det}$ em detector reduzido. | Toy de interface. |
| `verificar_imersao_calibracao.py` | Solução analítica, Riccati, Schur, convergência e identificabilidade sintética. | Teste matemático. |
| `benchmark_cs_fein2022.py` | Parâmetro instrumental calibrado e congelado antes da série independente. | Comparação fenomenológica real. |

Os scripts reduzidos são verificações pedagógicas. O benchmark de césio usa
dados reais digitizados, mas não substitui o cálculo de uma Hessiana material
completa. A construção e suas hipóteses estão em
[[calibracao_multiparametrica_imersao_invariante|Calibração multiparamétrica
por imersão invariante]].

## 10. Status

| Resultado | Status | Limite |
|---|---|---|
| $\rho=|\Psi|^2$ local | Demonstrado no setor regular | Não escolhe detector. |
| Born operacional | Fechada estruturalmente | Depende do Hilbert físico reconstruído. |
| Aparelho como Schur/DtN | Fechado estruturalmente | Metrologia depende do material. |
| Imersão invariante multiparamétrica | Fechada estruturalmente | Não linearidade e perdas exigem extensões próprias. |
| Benchmark instrumental | Validação inicial fora do ajuste | Canal magnético do césio ainda é entrada operacional. |
| Decoerência | Redução efetiva | Não é sozinha resultado único. |
| Resultado individual | Fechado condicionalmente no setor QND gaussiano | Outros aparelhos exigem nova análise. |
| Não-Hermitiano efetivo | Programa de extensão | Não altera a ação oficial. |

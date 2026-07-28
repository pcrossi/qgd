# Status formal da ponte global--local

## Enunciado correto

A formalização não identifica globalmente o espaço cosmológico com o bulk
local. Ela trata a família apontada

$$
T^4\times S^1_R\times S^3_R
\longrightarrow
T^4\times\mathbb R^4
$$

quando $R\to\infty$. Não existe interface física entre esses dois
backgrounds. Operadores DtN e condições de Robin pertencem somente ao bordo
físico do estômato.

## Checklist dos nove passos

| Passo | Módulo Lean | Resultado |
|---:|---|---|
| 1 | `GDQ.CosmologicalFamily` | `T⁵ × S³` foi decomposto tipadamente como `T⁴ × S¹ × S³`. |
| 2 | `GDQ.CosmologicalFamily` | A família de raios $R$ e a parametrização $R=\varepsilon^{-1}$ foram construídas. |
| 3 | `GDQ.CosmologicalFamily` | A taxa local $O(R^{-2})$ foi codificada por certificado e foi provado que o erro certificado tende a zero. |
| 4 | `GDQ.GlobalLocalTransport` | Foram transportados $g,J,H,f,\rho$ e $\mathcal U$; a convergência de $\rho$ e do kernel segue da de $f$. |
| 5 | `GDQ.C3Application` | O background local e sua Hessiana foram ligados à ação oficial por um certificado de estacionariedade e coercividade. Não foi introduzida sela global--local. |
| 6 | `GDQ.SpectralBridge` | Mosco foi definido por liminf fraco e sequência forte de recuperação. |
| 7 | `GDQ.SpectralBridge` | A margem de gap e a localização de Agmon foram separadas; provou-se $\Delta_0-2\delta>0$. |
| 8 | `GDQ.SpectralBridge` | Convergência forte de resolventes e em norma dos projetores de Riesz foram registradas como certificados verificáveis. |
| 9 | `GDQ.SpectralBridge`, `GDQ.C3Application` | Quantidades herdadas foram separadas de normalizações contínuas; no setor $C_3$, o projetor relativo é idempotente e o gap primitivo é exatamente $1/2$. |

## Refinamento concreto do setor $C_3$

O módulo `GDQ.C3ConcreteHessian` elimina parte do certificado abstrato:

1. constrói o Jacobiano real do vínculo
   $\sum_aT(\cos\theta_a,\sin\theta_a)=0$ no equilíbrio equilátero;
2. prova

$$
(D\mathcal C)^\dagger D\mathcal C
=\frac32T^2P_{\rm rel};
$$

3. prova que o modo comum está no kernel;
4. prova que, no subespaço relativo, a energia é

$$
\frac32\kappa_{\rm rel}T^2\|v\|^2;
$$

5. prova positividade estrita para $\kappa_{\rm rel}>0$ e $T\ne0$;
6. formaliza os níveis OU $m/(2\tau)$ e prova o limite inferior
   $1/(2\tau)$ para $m\ge1$;
7. prova a positividade de $3/(2\tau)$;
8. reduz o complemento de Schur ao bloco angular quando
   $J_{\theta r}=0$;
9. prova a fórmula final do menor gap reduzido.

## Redução gaussiana do integrando oficial

O módulo `GDQ.GaussianOfficialReduction` avança um elo adicional sem trocar
a ação da GDQ por um funcional auxiliar:

1. define o potencial gaussiano

$$
\operatorname{Re}f_\ast(x)
=\frac{|x|^2}{4\tau}+f_0;
$$

2. constrói a densidade constitutiva
   $\rho_\ast=\exp(-\operatorname{Re}f_\ast)$ e prova sua positividade;
3. calcula $|\nabla\operatorname{Re}f_\ast|^2=|x|^2/(4\tau^2)$;
4. expande literalmente o colchete oficial no fundo plano;
5. varia somente a parte imaginária de $f$, mantendo $\rho$ e
   $\operatorname{Re}f$ fixos;
6. prova por quocientes simétricos exatos que a primeira variação se anula em
   zero e que a segunda variação pontual é

$$
2\,\mathrm{prefator}\,\tau\,|\nabla v|^2;
$$

7. prova a positividade desse bloco quando os fatores físicos são positivos;
8. sob integrabilidade explícita dos termos base e quadrático, prova que a
   integral no bulk permanece uma função exatamente quadrática;
9. prova que sua segunda variação integrada é exatamente duas vezes a
   integral do coeficiente quadrático pontual.

Como a família é exatamente quadrática no parâmetro de fase, esses
quocientes não são uma discretização nem uma aproximação de diferenças
finitas.

## Transporte da variação pelo contorno causal

O módulo `GDQ.GaussianContourReduction` remove a pendência algébrica da
segunda integral sem restringir silenciosamente todo contorno à classe
exponencial:

1. permite que $\tau(t)$, o prefator, o termo base e a norma do gradiente
   dependam do parâmetro real do contorno;
2. mantém separadas as hipóteses de integrabilidade dos termos base e
   quadrático, tanto no bulk quanto no contorno;
3. prova que a integral iterada completa permanece exatamente quadrática na
   amplitude da variação de fase;
4. prova que a segunda variação da parte real da ação iterada é duas vezes a
   parte real do coeficiente quadrático integrado;
5. para o relógio homogêneo exponencial, usa o teorema causal já demonstrado
   para obter exatamente

$$
\gamma^\ast\left(\frac{d\tau}{\tau}\right)=\kappa\,dt;
$$

6. prova que o coeficiente integrado fatora por $\kappa$ e preserva
   positividade quando $\kappa>0$ e o coeficiente sem peso é real positivo.

Isso fecha a passagem algébrica pontual $\to$ bulk $\to$ contorno para o
setor puro de fase. As envolventes espaciais do background gaussiano são
construídas no módulo seguinte; o controle causal completo e a identificação
do bloco métrico--dilatônico com o operador OU continuam separados.

## Dominação gaussiana no bulk local

O módulo `GDQ.GaussianBulkDomination` fornece o primeiro certificado
analítico concreto de finitude espacial:

1. infere da compacidade que a medida de Haar de $T^4$ é finita;
2. usa o teorema gaussiano multidimensional para provar integrabilidade em
   $\mathbb R^4$ quando $b>0$;
3. eleva essa função à medida produto
   $\operatorname{Leb}_{\mathbb R^4}\times\operatorname{Haar}_{T^4}$;
4. prova exatamente

$$
\rho_\ast(x)
=e^{-f_0}
\exp\left(-\frac{|x|^2}{4\tau}\right);
$$

5. conclui que $\rho_\ast$, estendida trivialmente no toro, é integrável para
   $\tau>0$;
6. constrói certificados `IntegrableDomination` para $\rho_\ast$ e para um
   múltiplo espacial constante dela;
7. fornece um construtor geral para qualquer densidade mensurável cuja norma
   seja dominada por essa envolvente explícita.

Portanto, a finitude no bulk do bloco gaussiano constante deixou de ser uma
hipótese abstrata. A desigualdade de dominação para coeficientes espaciais
não constantes permanece específica do background; a infraestrutura de
controle causal é construída na seção seguinte.

## Controle gaussiano sem torção e densidade oficial

Os módulos `GDQ.GaussianAdmissibleBackground` e
`GDQ.GaussianOfficialIntegrability` removem duas abstrações que ainda
separavam os cálculos anteriores da ação:

1. constroem uma única `AdmissibleConfiguration` de controle com métrica Hermitiana
   identidade, estrutura complexa padrão em quatro planos reais, torção
   nula, potencial gaussiano, densidade constitutiva e kernel oficial;
2. provam que todo ponto desse background é regular;
3. fornecem curvatura escalar nula, norma de gradiente gaussiana e densidade
   volumétrica unitária como `EuclideanGeometricInvariants`;
4. provam a estimativa exata

$$
(1+r)e^{-br}
\le
\left(1+\frac{2}{b}\right)e^{-(b/2)r},
\qquad b>0,\quad r\ge 0;
$$

5. deduzem a integrabilidade de
   $|x|^2e^{-b|x|^2}$ e $|x|^2\rho_*$ em
   $\mathbb R^4\times T^4$;
6. agrupam literalmente a densidade oficial completa como

$$
\bigl(A(t)|x|^2+B(t)\bigr)\rho_*(x),
$$

   com $A(t)$ e $B(t)$ escritos a partir do prefator oficial, de
   $\gamma(t)$, de $\tau$, de $f_0$ e do denominador do kernel;
7. provam a integrabilidade espacial dessa densidade para cada $t$;
8. constroem `gaussianOfficialBulkControl`.

Esse objeto possui $H=0$ e, portanto, não é um background material da GDQ.
Ele é preservado somente como limite Kähler/plano, teste da ação e controle
de integrabilidade. Em particular, não fundamenta massa, spin, estômato,
três centros ou a Hessiana física material.

O testemunho de Bismut usado nessa construção possui o conteúdo coordenado
disponível na interface abstrata atual. Ele não deve ser confundido com uma
prova futura de atlas suave, completude ou das equações diferenciais globais
$\nabla^B g=0$, $\nabla^B J=0$ e $T^B=H$.

Também foi construída `gaussianFiniteSegmentAction`: a medida externa é
Lebesgue restrita a $[t_0,t_1]$, enquanto a densidade e o pullback oficiais
permanecem intocados. Dado um bound uniforme explícito no segmento, Lean
prova a integrabilidade externa e constrói o valor da ação. Portanto o
segmento finito agora é representado pelo domínio da medida, e não pela
inserção de uma janela no integrando.

## Primeiro ansatz torsional obrigatório

A formalização agora distingue `AdmissibleConfiguration` de
`MaterialAdmissibleConfiguration`. O segundo tipo exige, como campo de
prova, que exista uma componente de torção não nula. Assim, o compilador
impede o uso silencioso do controle $H=0$ no setor material.

O módulo `GDQ.ConformalBismutTorsion` inicia a construção correta:

$$
\omega=e^{2\phi}\omega_0,
\qquad
\phi(x)=a x^0,
\qquad
H=d_J^c\omega.
$$

Lean verifica a antissimetria de $d\omega$ e de $H$ e calcula

$$
H_{451}=2a\,e^{2\phi}.
$$

Logo, para $a\neq0$, esse ansatz possui torção genuinamente não nula. O
mesmo módulo prova a positividade da métrica Hermitiana conformal, preserva
a lei constitutiva de $\rho$ e do kernel e constrói
`conformalMaterialConfiguration`, que habita tipadamente o setor material.

Os módulos subsequentes completaram a construção coordenada local. A conexão

$$
\Gamma^{B\,k}_{ij}
=
\Gamma^{LC\,k}_{ij}
+\frac12 g^{k\ell}H_{ij\ell}
$$

foi construída e Lean verificou diretamente
$\nabla^B g=0$, $\nabla^B J=0$ e $T^B=H$. Para
$\phi=a x^0$, o fator conforme de $H$ cancela contra $g^{-1}$ e os
coeficientes de $\Gamma^B$ são constantes.

O objeto `conformalCoordinateBismutBackground` satisfaz todas as obrigações
de `CoordinateBismutBackground`. As contrações derivadas são

$$
\sqrt{\det g}=e^{8\phi},
\qquad
|\nabla f|_g^2=e^{-2\phi}|\nabla f|_{\rm flat}^2,
\qquad
\mathcal R^B=-60a^2e^{-2\phi}.
$$

O módulo `GDQ.ConformalOfficialDensity` insere exatamente esses invariantes
na ação oficial. Não foi acrescentado um termo fundamental separado
$|H|^2$: a torção entra através da conexão de Bismut e de sua curvatura.
O status é local/coordenado; atlas global, completude e condições no toro
continuam obrigações separadas.

## Controle no parâmetro causal

O módulo `GDQ.GaussianCausalDomination` separa três fatos que não podem ser
confundidos:

1. o relógio homogêneo fornece
   $\gamma^\ast(d\tau/\tau)=\kappa\,dt$, mas esse peso é constante;
2. um integrando temporal constante não nulo não é integrável em toda
   $\mathbb R$;
3. a integral externa torna-se finita se o background integrado possuir
   decaimento suficiente ou se o contorno físico for um segmento finito
   legitimamente parametrizado.

Foram formalizadas duas realizações:

$$
|F(t)|\le C e^{-a t^2},
\qquad a>0,
$$

e a extensão por zero de um segmento $[t_0,t_1]$. A segunda é apenas uma
forma de representar, sobre $\mathbb R$, um contorno fisicamente definido em
intervalo finito; ela não acrescenta termo à ação.

O módulo também introduz `GaussianControlledComplexContourBounds`. Quando o
background fornece as desigualdades espaciais e causal explícitas, Lean
constrói automaticamente `ControlledComplexContourActionData`, incluindo os
dois certificados de integrabilidade exigidos pela ação oficial.

Status rigoroso: a infraestrutura de fechamento integral está demonstrada,
mas a teoria ainda deve selecionar ou derivar, para cada background, se o
contorno é finito ou qual mecanismo produz o decaimento temporal. O relógio
exponencial sozinho não decide essa questão.

## O que é teorema Lean neste estágio

São provas internas do código:

0. os seis lemas possuem enunciados separados em
   `GDQ.GlobalLocalSixLemmas`, e o teorema
   `six_global_local_lemmas_explicit` compõe suas conclusões sem identificar
   globalmente os dois espaços nem herdar normalizações contínuas;

1. a equivalência de tipos $T^5\simeq T^4\times S^1$;
2. a compatibilidade dimensional $4+1+3=8$;
3. a convergência a zero da majorante $C R^{-2}$;
4. a convergência do erro local dado o certificado geométrico;
5. a convergência de $\rho$ e do kernel oficial dada a convergência de $f$;
6. a preservação da distância pelo transporte norm-preservante;
7. a positividade da margem transferida de gap;
8. a positividade eventual dos gaps da família;
9. a composição lógica dos seis certificados;
10. a classificação de invariantes herdados e normalizações não herdadas;
11. a soma nula e a idempotência do projetor relativo de três centros;
12. a positividade do gap $C_3$;
13. o valor exato $\Delta_0=1/2$ na normalização primitiva;
14. gap implica estabilidade da Hessiana física oficial certificada;
15. a identidade de Gram do junction $C_3$;
16. a coercividade angular no complemento de Noether;
17. os limites positivos dos blocos OU e radial;
18. a fórmula conjunta do gap reduzido.
19. a positividade da densidade gaussiana constitutiva;
20. a fórmula da norma do gradiente gaussiano;
21. a expansão do colchete oficial no background plano gaussiano;
22. a primeira e a segunda variações exatas do setor de fase;
23. a positividade do bloco Hessiano de fase;
24. a passagem exata do bloco pontual para a integral no bulk;
25. a preservação quadrática depois da integral no contorno causal;
26. a fórmula exata da segunda variação da parte real da ação iterada;
27. a fatoração pelo gerador $\kappa$ no relógio exponencial e a
    preservação condicional do sinal positivo;
28. a integrabilidade espacial da gaussiana constitutiva no bulk
    $\mathbb R^4\times T^4$;
29. os certificados de dominação da densidade e de seus múltiplos
    espaciais constantes;
30. a integrabilidade de uma envolvente causal gaussiana;
31. a não integrabilidade de constantes não nulas em toda a reta;
32. a integrabilidade de um segmento causal finito estendido por zero;
33. a construção da ação complexa controlada a partir dos bounds espaciais e
    causais.
34. a construção do controle gaussiano plano sem torção;
35. a regularidade e os invariantes explícitos desse background;
36. a dominação de pesos afins por uma gaussiana de taxa reduzida;
37. a integrabilidade dos momentos radiais gaussianos;
38. a redução da densidade oficial completa ao perfil afim-gaussiano;
39. a integrabilidade espacial da densidade oficial completa;
40. a construção da ação oficial gaussiana em segmento causal finito sob
    bound externo explícito.
41. a separação tipada do setor material com `H≠0`;
42. a construção do ansatz conformal `H=d_J^cω`;
43. a antissimetria e a não anulação explícita dessa torção.
44. a positividade Hermitiana e a construção tipada da configuração material
    conformal.
45. a conexão coordenada explícita de Bismut do ansatz conformal;
46. as identidades `∇ᴮg=0`, `∇ᴮJ=0` e `Tᴮ=H`;
47. o background coordenado material completo;
48. a fórmula `sqrt(det g)=e^{8φ}`;
49. a fórmula `|∇f|²_g=e^{-2φ}|∇f|²_flat`;
50. a curvatura escalar `Rᴮ=-60a²e^{-2φ}`;
51. a densidade pontual da ação oficial com os invariantes torsionais
    substituídos literalmente.
52. a derivada exata da ação torsional reduzida normalizada;
53. o valor crítico $q_c=8/5$;
54. a existência de raiz não nula para $q>8/5$;
55. a monotonicidade estrita e a unicidade dessa raiz em
    $0<u<5/42$;
56. a positividade da segunda variação na direção conformal da raiz.
57. a existência construtiva de uma amplitude
    $a_*=\sqrt{u_*/\tau}>0$ estacionária e estável nessa direção.
58. a raiz torsional é um mínimo local da ação reduzida em
    $u=\tau a^2$.
59. a Hessiana reduzida é exatamente
    $q e^{-28u}(2912-18816u)$ e é positiva no intervalo físico.
60. para um modo real adicional, a positividade do bloco acoplado segue
    exatamente da positividade do complemento de Schur
    $K_{XX}-K_{aX}^2/K_{aa}$.

## Obrigações que permanecem explícitas

Lean não declarou como automáticas:

- a expansão em coordenadas normais que produz a constante concreta
  $C_{k,L}$;
- a existência de todo background warped ou misto;
- o atlas global e a completude do ansatz conformal torsional;
- a internalização, em Lean, dos momentos gaussianos usados para passar da
  integral oficial à ação torsional reduzida; essa passagem está deduzida
  analiticamente em `DERIVACAO_SELA_TORSIONAL_CONFORMAL.md`;
- a avaliação dos blocos mistos e não conformais da Hessiana
  métrico--dilatônica--torsional física em torno dessa sela; o bloco
  conformal normalizado e o critério de Schur já estão demonstrados;
- a coercividade da Hessiana de um background arbitrário;
- as estimativas de IMS/Agmon em cada novo operador;
- o teorema funcional-analítico geral “Mosco implica resolvente” dentro da
  biblioteca usada;
- a integral de contorno que constrói cada projetor de Riesz concreto;
- a derivação do bound causal externo em cada background físico quando o
  domínio não for especificado como segmento finito;
- a seleção física entre contorno causal finito e decaimento em toda a reta;
- a demonstração, dentro de Lean, de que a segunda variação
  métrico--dilatônica gauge-fixada no preenchimento gaussiano coincide com o
  bloco OU reduzido;
- massas absolutas, acoplamentos, taxas ou respostas de aparelhos.

Esses itens entram como certificados a serem preenchidos por demonstrações
específicas. Isso preserva o status canônico: a ponte está aplicada à classe
estacionária reduzida $C_3$, enquanto sua extensão a backgrounds gerais
continua condicional.

## Sela torsional conformal

Na folha euclidiana positiva, com Haar normalizada em $T^4$, gaussiana de
largura $\tau>0$, vínculo $\int\mathcal U\,dV_g=1$ e razão de contorno:

$$
q=\frac{z_\tau}{\tau},
$$

a ação oficial reduzida na variável $u=\tau a^2$ é:

$$
\mathcal A_{\rm red}
=
q e^{-28u}(2-24u)+f_{\rm base}-2+128u.
$$

Lean prova que, para:

$$
q>\frac85,
$$

existe uma única raiz:

$$
u_*\in\left(0,\frac5{42}\right),
$$

da primeira variação. Os backgrounds:

$$
a_*=\pm\sqrt{\frac{u_*}{\tau}}
$$

possuem torção não nula e segunda variação positiva na direção conformal.

Classificação: **sela torsional derivada condicionalmente no setor
conformal reduzido**. A Hessiana física acoplada, o atlas global e a
completude permanecem abertos; portanto o resultado ainda não é uma prova de
sóliton material 8D completamente estável.

O documento `HESSIANA_SELA_TORSIONAL_CONFORMAL.md` explicita o vetor
tangente vinculado dessa direção: variar $a$ também varia $g$, $\omega$,
$H=d_J^c\omega$ e a constante de normalização de
$\operatorname{Re}f$. O módulo `GDQ.ConformalTorsionHessian` prova o mínimo
local, identifica a Hessiana em $u$ e formaliza o critério de Schur para os
modos ainda não avaliados. Ele não atribui valores a blocos físicos
desconhecidos.

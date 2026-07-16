# Nucleação torsional de um par mesônico no decaimento do nêutron

## 1. Enunciado exato

Investigar a rota

$$
n\longrightarrow p+\Pi^-_{\operatorname{virt}},
$$

$$
\Pi^-_{\operatorname{virt}}\longrightarrow e^-+\bar\nu_e,
$$

em que $\Pi^-_{\operatorname{virt}}$ é um setor transitório de dois estômatos. A letra
$\Pi$ indica apenas **topologia mesônica bimodal**. A identificação com um
píon físico exige, adicionalmente, massa, spin, paridade, carga e perfil
espectral correspondentes.

O objetivo deste documento é demonstrar o que a conservação de torção já
implica para a nucleação e isolar o único sinal de Hessiana que ainda precisa
ser calculado no background completo.

## 2. Dados usados

Da Q40:

$$
(\mathcal T_a)_n=(\tau,\tau,-2\tau),
\qquad
(\mathcal T_a)_p=(\tau,\tau,\tau),
$$

$$
Q_n=0,
\qquad
Q_p=+1,
\qquad
B_{\text{top}}(n)=B_{\text{top}}(p)=1.
$$

Da Q28, um setor de dois estômatos é colinear na distribuição horizontal de
Hopf. Ele forma um tubo estômato--antiestômato e pode representar propagação,
aniquilação ou um estado mesônico bimodal. Ele não é um junction elementar
tridirecional.

Da conservação local de torção, para uma classe fixa $Q_T$ suportada num
volume efetivo $V$:

$$
E_T(V)=\frac{\kappa_TQ_T^2}{2V}.
$$

Essa última identidade é exata no ansatz homogêneo de fluxo fixo. Seu
levantamento ao background não homogêneo exige substituir $1/V$ pela norma de
Hodge do representante harmônico.

### 2.1 Sistema perturbado e condição de Robin

Em um sistema perturbado, o operador físico da Hessiana pode receber na
interface uma condição de contorno de Robin,

$$
\boxed{
\left(\nabla_n+\eta_R\right)\Psi\big|_{\partial X}=0,
}
$$

com $\eta_R\in\mathbb R$ para a realização auto-adjunta e $\nabla_n$ a
derivada normal covariante. Essa condição mistura o valor do modo com seu
fluxo normal e, portanto, pode deslocar o espectro de borda do setor bimodal.

Se a perturbação e $\eta_R$ conduzirem um autovalor físico do modo de abertura
através de zero, o sistema pode nuclear uma configuração ligada ou
transitória com **dois estômatos**, isto é, uma configuração de topologia
mesônica. A formação não é automática para toda condição de Robin: ela ocorre
quando o autovalor projetado satisfaz

$$
\lambda_{\rm pair}(\eta_R,\delta\Phi)<0
$$

ou, no caso de túnel, quando surge a sela causal correspondente. A massa,
estabilidade e identificação do méson dependem então do polo espectral desse
problema de contorno.

## 3. Por que testar dois estômatos

A criação de um defeito isolado não é a transição genérica num setor de
índice total conservado. Na fatia transversal $X_4$ usada na Q28, a abertura
de um par produz duas vizinhanças removidas

$$
B_+^4,\ B_-^4\subset X_4,
$$

com elos

$$
Y_+=\partial B_+^4\simeq S^3,
\qquad
Y_-=\partial B_-^4\simeq S^3.
$$

O complemento depois da abertura é

$$
X_{4,2}^{\circ}
=X_4\setminus
\left(\operatorname{int}B_+^4\sqcup\operatorname{int}B_-^4\right),
$$

e

$$
\partial X_{4,2}^{\circ}=(-Y_+)\sqcup(-Y_-).
$$

Um colar $S^3\times I$ conecta os dois elos e constitui o tubo bimodal. O
traço da cirurgia é um cobordismo de dimensão cinco sobre $X_4$; no bulk
oficial ele deve ser levantado pelas quatro direções espectadoras de $T^4$.
Assim, esta construção não identifica $T^5\times S^3$ com o bulk local.

## 4. Modelo local da abertura do par

Numa seção complexa normal ao tubo, considere

$$
\varphi_a(z)=\frac{z-a}{z+a},
\qquad a\geq0.
$$

Para $a=0$, zero e polo se cancelam e $\varphi_0=1$ fora do ponto crítico.
Para $a>0$, aparecem duas componentes primitivas:

$$
z_+=a,
\qquad
z_-=-a,
$$

com índices locais

$$
\operatorname{ind}(z_+)=+1,
\qquad
\operatorname{ind}(z_-)=-1.
$$

Portanto,

$$
\operatorname{ind}(z_+)+\operatorname{ind}(z_-)=0.
$$

Esse modelo prova que um par pode nascer sem alterar o índice **local de
nucleação**. Ele não determina sozinho a carga elétrica do tubo. A carga
$Q_{\Pi}=-1$ deve vir do mapa global de transição herdado simultaneamente da
mudança $Q_n=0\to Q_p=+1$.

Pela conservação do resíduo elétrico no cobordismo completo:

$$
Q_n=Q_p+Q_{\Pi},
$$

logo

$$
\boxed{Q_{\Pi}=-1.}
$$

Assim, há dois dados diferentes:

1. o par zero--polo possui índice local líquido zero;
2. o tubo global transporta resíduo elétrico $-1$ transferido pela cirurgia
   bariônica.

Confundir esses dois índices produziria uma contradição aparente.

## 5. A torção dupla do estômato contrário

No nêutron, o terceiro estômato não transporta uma unidade negativa, mas duas:

$$
\boxed{\mathcal T_3^{(n)}=-2\tau.}
$$

Esse fator dois é obrigatório porque ele compensa simultaneamente

$$
\mathcal T_1^{(n)}+\mathcal T_2^{(n)}=2\tau.
$$

Portanto, a carga torsional concentrada que alimenta o modo de nucleação é,
em módulo,

$$
\boxed{Q_{\rm pref}=2\tau.}
$$

A decomposição primitiva mínima dessa concentração é

$$
-2\tau=(-\tau)+(-\tau).
$$

Isso fornece a razão estrutural para testar **dois** estômatos: a torção
preferencial dupla pode bifurcar em dois ramos unitários, enquanto uma
hipótese de apenas um novo estômato deixaria uma unidade torsional sem canal.
Essa decomposição ainda não identifica os dois ramos com partículas; ela
apenas seleciona a multiplicidade bimodal do canal de abertura.

### 5.1 Diferença para a cola protônica

A mudança da cola antiparalela para a paralela é

$$
\Delta\boldsymbol{\mathcal T}
=(\mathcal T_a)_p-(\mathcal T_a)_n
=(0,0,3\tau).
$$

O valor $3\tau$ é a diferença algébrica entre o canal inicial $-2\tau$ e o
canal protônico final $+\tau$. Ele **não** deve ser identificado integralmente
com a torção ejetada. Essa diferença contém dois processos:

1. liberação/bifurcação da concentração inicial de módulo $2\tau$;
2. formação do novo canal protônico coorientado de módulo $\tau$.

Somente a integração da corrente $J_T$ nos colares poderá determinar quanto
do salto $3\tau$ atravessa o tubo e quanto pertence à nova cola protônica. Por
isso, não se impõe mais $\mathcal T_{\Pi}^{\rm out}=-3\tau$ como balanço do
intermediário.

No tubo bimodal, a contrarrotação dos dois estômatos pode ter soma mecânica
nula enquanto o twist longitudinal do colar transporta o fluxo residual.
Portanto, fechamento mecânico horizontal e fluxo torsional longitudinal não
são a mesma quantidade.

## 6. Coordenada coletiva de nucleação

Seja $a$ a amplitude de abertura do par. A involução que troca os dois
estômatos envia $a\mapsto-a$, de modo que o volume efetivo disponível ao fluxo
possui expansão par

$$
V(a)=V_0+\nu a^2+O(a^4),
\qquad
\nu>0.
$$

A condição $\nu>0$ significa apenas que abrir duas calotas aumenta o suporte
disponível ao fluxo torsional concentrado.

Mantendo a torção preferencial $Q_{\rm pref}=2\tau$ conservada durante a
abertura:

$$
E_T(a)
=\frac{\kappa_TQ_{\rm pref}^2}{2V(a)}.
$$

Defina

$$
C_T=\frac{\kappa_TQ_{\rm pref}^2}{2}
=2\kappa_T\tau^2.
$$

Então

$$
E_T(a)
=\frac{C_T}{V_0}
-\frac{C_T\nu}{V_0^2}a^2
+O(a^4),
$$

e, portanto,

$$
\boxed{
\lambda_T
:=\left.\frac{d^2E_T}{da^2}\right|_{a=0}
=-\frac{\kappa_TQ_{\rm pref}^2\nu}{V_0^2}
=-\frac{4\kappa_T\tau^2\nu}{V_0^2}<0.
}
$$

Este é o resultado central: **a conservação de uma torção não nula torna a
parcela torsional da Hessiana negativa na direção que abre um par e aumenta
seu suporte**. Nesse sentido preciso, a torção prefere a nucleação do par.

## 7. A torção prefere, mas a Hessiana total decide

As duas calotas, o colar, a curvatura, o campo $f$ e a medida ponderada possuem
um custo conjunto. Escreva a ação reduzida como

$$
\Delta\mathcal A_2(a)
=\frac12\lambda_{\text{pair}}a^2
+\frac14u_{\text{pair}}a^4
+O(a^6),
$$

com

$$
\boxed{
\lambda_{\text{pair}}
=\lambda_{\rm rest}
-\frac{4\kappa_T\tau^2\nu}{V_0^2}.
}
$$

Aqui $\lambda_{\rm rest}$ é a segunda variação de todos os demais blocos da
ação oficial depois da fixação de gauge e da restrição de normalização.

Se houver modos transversais $\xi$ e acoplamento misto $J_{a\xi}$, o valor
físico é o complemento de Schur

$$
\boxed{
\lambda_{\rm pair}^{\rm phys}
=H_{aa}
-J_{a\xi}K_{\perp}^{-1}J_{a\xi}^{\dagger}.
}
$$

### Nucleação clássica

Se

$$
\lambda_{\rm pair}^{\rm phys}<0,
\qquad
u_{\rm pair}>0,
$$

a configuração sem par é instável e surgem dois mínimos simétricos:

$$
a_*
=\sqrt{-\frac{\lambda_{\rm pair}^{\rm phys}}{u_{\rm pair}}}.
$$

O critério torsional suficiente, antes das correções mistas, é

$$
\boxed{
4\tau^2
>\frac{V_0^2\lambda_{\rm rest}}{\kappa_T\nu}.
}
$$

### Nucleação por túnel

Se $\lambda_{\rm pair}^{\rm phys}>0$, a torção reduz o custo mas não prova
instabilidade clássica. Ainda pode existir uma sela causal de ação finita. A
taxa dependerá da diferença de ação ao longo dessa sela, que deverá ser
calculada no contorno $\gamma$.

## 8. Teorema condicional de nucleação

> **Teorema.** Considere o background neutrônico da Q40 com torção preferencial
> conservada $Q_{\rm pref}=2\tau\neq0$. Suponha que: (i) a família $\Phi(a)$ de abertura do
> par pertença ao domínio da ação oficial; (ii) $V(a)=V_0+\nu a^2+O(a^4)$ com
> $\nu>0$; (iii) o bloco transversal seja invertível após a remoção de gauge;
> e (iv) $u_{\rm pair}>0$. Se
>
> $$
> H_{aa}-J_{a\xi}K_\perp^{-1}J_{a\xi}^{\dagger}<0,
> $$
>
> então o background sem o par é instável na direção bimodal e a ação possui
> uma configuração de menor valor com dois estômatos abertos.

A prova é a expansão par da ação e o teste da segunda derivada. A contribuição
torsional à desigualdade é estritamente negativa e foi derivada acima. O
sinal da Hessiana total ainda depende de $\lambda_{\rm rest}$ e dos blocos
mistos.

## 9. Por que o intermediário deve ser virtual

Da fórmula estrutural vigente da Q40:

$$
Q_\beta
=(\delta_B-1)M_ec^2,
\qquad
\delta_B=\ln(2\pi^2)\frac{3\sqrt2}{5},
$$

resulta

$$
Q_\beta\simeq1{,}530827\,M_ec^2
\simeq0{,}782\ {\rm MeV}.
$$

Essa energia não permite produzir um píon físico on-shell. Logo, mesmo que a
topologia instantânea seja a de um méson de dois estômatos, o objeto deve ser
um modo virtual da trajetória de cirurgia. Chamá-lo diretamente de $\pi^-$
sem calcular seu polo espectral seria incorreto.

## 10. Segunda cirurgia: resolução do tubo

O tubo carregado não pode simplesmente desaparecer no vácuo, pois

$$
Q_{\Pi}=-1.
$$

A resolução admissível deve satisfazer

$$
\Pi^-_{\operatorname{virt}}
\longrightarrow
e^-+\bar\nu_e,
$$

com

$$
-1=(-1)+0,
\qquad
0=(+1)+(-1)
$$

para carga elétrica e número leptônico, respectivamente. Geometricamente, a
proposta é:

1. uma extremidade do tubo localiza o estômato eletrônico carregado;
2. o twist longitudinal restante se desprende como modo quiral neutro;
3. o colar intermediário perde seu suporte e se fecha.

Essa descrição é uma rota de construção. Para virar prova, a Hessiana ao
longo da segunda cirurgia deve possuir um modo carregado localizado e um modo
quiral neutro normalizáveis.

## 11. Resultado obtido e pendência única imediata

Foi demonstrado, no ansatz de fluxo homogêneo fixo, que

$$
\boxed{\lambda_T<0.}
$$

Portanto, a torção conservada realmente favorece a abertura de dois
estômatos. Ainda não foi demonstrado que ela vence o custo total:

$$
\boxed{
\lambda_{\rm pair}^{\rm phys}<0
\quad\text{permanece a condição a avaliar.}
}
$$

O próximo cálculo é inserir a família $\Phi(a)$ no background colado da Q40 e
obter, por segunda variação da ação oficial,

$$
\nu,
\qquad
\lambda_{\rm rest},
\qquad
J_{a\xi},
\qquad
K_\perp.
$$

Como a criação muda $N_{\rm estoma}$, a Hessiana ordinária da Q40 não contém
esse modo. A formulação correta foi refinada em
`hessiana_estratificada_nucleacao_bimodal.md`: usa-se a diferença unilateral
de ação entre os estratos $\mathscr C_3$ e $\mathscr C_{3+2}$. Sem o
coeficiente geométrico das calotas e colares, “a torção cria o par” permanece
um teorema condicional; com $c_2^{\rm eff}<0$, a nucleação clássica estará
provada no setor reduzido.

## 12. Classificação

- topologia mesônica de dois estômatos: estrutura vigente do manuscrito,
  ainda não consolidada como teorema fundamental;
- modelo zero--polo local: construção matemática explícita;
- transferência $Q_{\Pi}=-1$: consequência da conservação elétrica, dado o
  cobordismo proposto;
- torção preferencial $Q_{\rm pref}=2\tau$: consequência da compensação
  estacionária $(\tau,\tau,-2\tau)$;
- decomposição $-2\tau=-\tau-\tau$: seleção primitiva proposta para o canal
  bimodal;
- salto algébrico $3\tau$ até a cola protônica: identidade, ainda sem uma
  partição derivada entre fluxo emitido e nova cola;
- contribuição $\lambda_T<0$: derivação exata no ansatz homogêneo de classe
  torsional fixa;
- nucleação do par: teorema condicional ao sinal da Hessiana completa;
- identificação do tubo com píon físico: não demonstrada e cinematicamente
  excluída como estado on-shell no decaimento livre;
- resolução em $e^-+\bar\nu_e$: mecanismo proposto, ainda a demonstrar.

## 13. Correção radial posterior

A conclusão $\lambda_T<0$ depende da coordenada coletiva satisfazer
$\Delta V\sim a^2$. Para o raio físico $r$ de uma garganta $S^3$, a expansão
natural é $\Delta V\sim r^3$. O documento
`nucleo_critico_par_mesonico.md` mostra que o potencial toma a forma

$$
\Delta\mathcal A(r)=A_2r^2-B_3r^3+C_4r^4+\cdots.
$$

Assim, a torção dupla favorece a formação do par pelo termo $-B_3r^3$, mas a
origem pode permanecer localmente estável. A rota fisicamente preferida passa
por um núcleo crítico finito.

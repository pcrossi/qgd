# Ponte global--local — sela estatística da GDQ

## 1. Enunciado

O objetivo é decidir se a estatística intrínseca da GDQ pode fornecer um
background bulk--interface estacionário mesmo quando a média determinística
do ansatz homogêneo não é um zero exato do mapa de colagem.

Não se permite escolher uma variância a partir do resíduo. A covariância deve
ser determinada pela ação oficial, pelo domínio causal e pelos vínculos.

## 2. Equação estatística correta

Se $X=\bar X+\xi$, com $\mathbb E\xi=0$, a condição de estacionariedade média
é

$$
\mathbb E\left[D\mathcal S_{\rm aug}(\bar X+\xi)\right]=0,
$$

onde $\mathcal S_{\rm aug}$ é a ação oficial acrescida somente dos
multiplicadores dos vínculos já derivados. Expandindo em torno de $\bar X$,

$$
0=D\mathcal S_{\rm aug}(\bar X)
+\frac12D^3\mathcal S_{\rm aug}(\bar X):C
+O(\mathbb E\|\xi\|^3),
$$

com

$$
C=\mathbb E(\xi\otimes\xi)\ge0.
$$

No setor gaussiano, depois da remoção dos vínculos e modos de gauge, a
covariância não é livre. Formalmente,

$$
\boxed{
C^{\rm phys}
=\mathfrak P_\gamma
\left[(K^{\rm phys}-i0_\gamma)^{-1}\right],
}
$$

onde

$$
K^{\rm phys}=P^{\rm phys}
D^2\mathcal S_{\rm aug}[\bar X]
P^{\rm phys}.
$$

Equivalentemente, a equação de campo média é a estacionariedade do funcional
estatístico gaussiano

$$
\Gamma[\bar X]
=\mathcal S_{\rm aug}[\bar X]
+\frac12\operatorname{Tr}_{\rm phys,\gamma}\log K^{\rm phys}[\bar X]
+\cdots.
$$

O determinante acima é a energia livre estatística da própria Hessiana da
GDQ. Não é um novo termo fundamental nem autoriza importar uma ação externa.

## 3. Por que o teste escalar anterior era insuficiente

No candidato da homotopia $h=0{,}18$, a projeção sobre o par singular mole
forneceu

$$
r=4{,}4977387\times10^{-5},
\qquad
b=-3{,}43326\times10^{-5},
$$

e portanto

$$
-\frac rb\simeq1{,}31005>0.
$$

Esse cálculo mostra apenas que a componente esquerda mole pode ser anulada.
Ele não verifica as outras dez equações.

O teste vetorial em `ponte_global_local_teste_sela_estatistica_vetorial.py`
mostrou que a mesma variância deixa

$$
\|F_{\rm médio}\|_2\simeq5{,}42,
$$

embora o resíduo inicial seja apenas

$$
\|F\|_2=1{,}86586\times10^{-4}.
$$

Logo uma única covariância no modo mole não produz uma sela estatística.

## 4. Teste de ruído isotrópico

Também foi testada a aproximação

$$
C=sI
$$

nas coordenadas do mapa de tiro. Em três passos independentes, o mínimo de
$\|F+(s/2)\Delta F\|_2$ exigiu

$$
s\simeq-4{,}8230\times10^{-17}<0.
$$

Uma covariância não pode ser negativa. Além disso, a redução do resíduo foi
somente

$$
\frac{\|F_{\rm corrigido}\|_2}{\|F\|_2}
\simeq0{,}999961.
$$

Portanto o ruído isotrópico no espaço de parâmetros também não fecha a sela.
Esse teste não exclui a estatística da GDQ, pois a identidade nas coordenadas
de tiro não é a métrica física.

## 5. O que deve ser calculado

A prova da sela estatística requer, nesta ordem:

1. construir a forma quadrática completa da segunda variação do funcional
   bulk--interface, incluindo os termos DtN;
2. formar $P^{\rm phys}$ removendo difeomorfismos, normalização e módulos de
   pullback;
3. obter o operador auto-adjunto $K^{\rm phys}$ e seu domínio;
4. calcular $C^{\rm phys}$ pelo resolvente causal, sem usar o resíduo como
   alvo;
5. avaliar a contração vetorial

$$
\frac12D^3\mathcal S_{\rm aug}:C^{\rm phys};
$$

6. resolver simultaneamente

$$
D\mathcal S_{\rm aug}
+\frac12D^3\mathcal S_{\rm aug}:C^{\rm phys}=0;
$$

7. verificar positividade, regularidade, tightness e estabilidade do
   background obtido.

O coeficiente de difusão $\nu_0$ da Questão 16 fixa a escala cinemática da
medida de Wiener, mas não substitui o pullback da métrica física nem determina
sozinho a covariância de cada modo bulk--interface. A projeção sobre os modos
e a geometria local $\Omega$ ainda precisam ser calculadas.

## 6. Veredito

### 6.1 Assinatura da forma cinética oficial

No setor exterior de Berger, na ordem $(x,y,z,u,v)$, o bloco quadrático
$\mathcal K_{B,2}$ possui matriz

$$
M_B=
\begin{pmatrix}
8&8&4&-4&0\\
8&0&2&-2&0\\
4&2&0&-1&0\\
-4&-2&-1&1&0\\
0&0&0&0&1
\end{pmatrix}.
$$

O script `ponte_global_local_assinatura_cinetica.py` encontrou

$$
\operatorname{spec}(M_B)
\simeq
(-5{,}02007,-1{,}43487,-0{,}282293,1,15{,}73723),
$$

portanto sua assinatura é

$$
(n_+,n_-,n_0)=(2,3,0).
$$

Isso confirma que a Hessiana bruta não define uma covariância real positiva.
Primeiro devem ser impostos os vínculos e removidas as direções de gauge; as
direções negativas físicas remanescentes pertencem à escolha causal de
thimble. Inverter diretamente a matriz bruta seria matematicamente incorreto.

### 6.2 Existência de medida estacionária e dado ainda ausente

Uma rota alternativa rigorosa é definir no espaço de configurações físicas
um processo de difusão

$$
dX_t=-\mathbb M(X_t)D\mathcal S_{\rm aug}(X_t)dt
+\sqrt{2\mathbb D(X_t)}\,dW_t.
$$

Se a folha física for compacta, ou se houver tightness uniforme, e o
semigrupo for Feller, Krylov--Bogoliubov fornece ao menos uma medida
invariante. Irredutibilidade e uma condição de Hörmander podem fornecer
unicidade. Isso demonstraria uma sela **estatística**, entendida como medida
estacionária, mesmo sem um ponto crítico determinístico.

Entretanto, a Questão 16 fixa a difusão de coordenadas físicas

$$
D^{ij}=\nu_0\Omega^{-1}h^{ij},
$$

e não fornece automaticamente a mobilidade $\mathbb M$ nem o operador de
ruído $\mathbb D$ no espaço de campos $(g,J,f)$ ou nos parâmetros de colagem.
O pullback entre esses dois espaços é precisamente o dado ainda ausente.
Logo não se pode simular honestamente o processo acima escolhendo ruído em
$\theta\in\mathbb R^{11}$.

## 7. Veredito

$$
\boxed{
\begin{gathered}
\text{a rota estatística permanece matematicamente possível,}\
\text{mas a variância escalar e o ruído isotrópico foram excluídos;}\\
\text{o fechamento exige a covariância física completa da Hessiana oficial.}
\end{gathered}
}
$$

Classificação: derivação formal da equação estatística e testes numéricos de
consistência. Não é prova de existência da sela.

## 8. Resultado do pullback da Questão 16

O cálculo posterior em `topicos/ponte_global_local/ponte_global_local_pullback_estocastico.md` mostrou
que o levantamento tensorial da difusão espacial aos campos é

$$
\mathbb D_X^{\rm coord}=RDR^\dagger,
$$

onde $R$ é o gerador infinitesimal de difeomorfismos. Como

$$
P^{\rm phys}R=0,
$$

segue exatamente

$$
\boxed{
P^{\rm phys}\mathbb D_X^{\rm coord}P^{\rm phys\dagger}=0.
}
$$

Isso vale para difeomorfismos de gauge com traço físico nulo na interface.
Para deslocamentos brownianos com traço não nulo no estômato, resta

$$
B_\partial=P^{\rm phys}RE_\partial,
\qquad
\mathbb D^{\rm phys}=B_\partial D_\partial B_\partial^\dagger.
$$

Logo a estatística da Q16 não fornece ruído físico no interior, mas pode
fornecê-lo pela interface. Esse é o próximo pullback legítimo a calcular.

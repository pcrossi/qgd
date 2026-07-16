# Teorema de herança global--local da normalização eletromagnética

## 1. Enunciado exato

O objetivo deste documento não é calcular novamente a constante de estrutura
fina no laboratório. O objetivo é demonstrar a seguinte implicação:

$$
\text{normalização eletromagnética global}
\quad\Longrightarrow\quad
\text{a mesma normalização na carta laboratorial}.
$$

A demonstração usa somente:

1. a ação oficial da GDQ;
2. a direção interna primitiva $U(1)_Q$;
3. a Hessiana física no background estacionário;
4. a corrente simplética derivada dessa Hessiana;
5. os seis lemas da ponte global--local sem colar artificial, quando o modo
   for localizado, ou sua versão de espalhamento para um canal massless;
6. a compatibilidade das formas-relógio global e local;
7. ausência de fonte, fuga lateral e fechamento do gap no transporte.

Ela não identifica a corrente global de fase de Madelung com a carga elétrica.
Essa corrente conserva probabilidade. A corrente elétrica é a resposta ao
modo interno $U(1)_Q$.

## 2. Gerador geométrico do setor elétrico

No setor toroidal, seja $\xi_Q$ o campo de Killing que gera a direção
primitiva selecionada pela rede de cargas. Escrevendo

$$
T^4=S^1_1\times S^1_2\times S^1_3\times S^1_4,
$$

e usando a normalização primitiva vigente da Q37,

$$
\xi_Q=2\,\partial_{\theta_1}.
$$

O fator dois converte a monodromia antiperiódica fundamental
$Q_1=1/2$ em carga inteira mínima. Ele fixa a rede de cargas, mas não fixa
sozinho a intensidade do acoplamento.

Uma conexão laboratorial $A$ é introduzida como deformação horizontal da
forma interna,

$$
\Theta_Q=d\theta_Q+A.
$$

Denote por $\eta_Q(A)$ a perturbação de $(g,J,f)$ induzida por essa deformação,
incluindo as correções exigidas para permanecer na classe Hermitiana
admissível. Essa definição não acrescenta um termo de Yang--Mills à ação: ela
restringe a segunda variação da ação oficial à direção geométrica $U(1)_Q$.

## 3. Hessiana efetiva do modo $U(1)_Q$

No espaço físico, depois dos vínculos e da remoção de gauge, decomponha as
perturbações como

$$
\mathscr H^{\rm phys}
=\mathscr H_Q\oplus\mathscr H_\perp.
$$

A Hessiana oficial tem a forma em blocos

$$
K^{\rm phys}
=
\begin{pmatrix}
K_{QQ}&K_{Q\perp}\\
K_{\perp Q}&K_{\perp\perp}
\end{pmatrix}.
$$

Como o complemento possui gap no background considerado, sua resposta linear
é

$$
\eta_\perp(A)
=-K_{\perp\perp}^{-1}K_{\perp Q}\eta_Q(A).
$$

Substituindo-a na forma quadrática, obtém-se o operador físico efetivo

$$
K_Q^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}.
$$

Defina

$$
q_Q[A,B]
=\left\langle
\eta_Q(A),K_Q^{\rm eff}\eta_Q(B)
\right\rangle_{\mathcal U_*dV_{g_*}}.
$$

A invariância pela isometria interna implica a identidade de Ward

$$
q_Q[d\lambda,B]=0
$$

para variações admissíveis. Por isso não aparece termo de massa para o modo
não quebrado. Na expansão de duas derivadas, a única forma quadrática local,
real e invariante é

$$
q_Q[A,B]
=\frac{Z_Q}{2}
\int_{N^4}F_A\wedge\star_hF_B
+q_Q^{(>2)}[A,B],
$$

onde $q_Q^{(>2)}$ contém termos de resolução superior. O número $Z_Q>0$ é a
normalização eletromagnética física. Na convenção canônica,

$$
e_Q^2=Z_Q^{-1},
\qquad
\alpha_Q=\frac{e_Q^2}{4\pi\hbar c}.
$$

## 4. Corrente que mede $Z_Q$

Se $\Theta_{\rm GDQ}$ é o potencial pré-simplético obtido da primeira
variação da ação oficial, a corrente bilinear é

$$
\omega_{\rm GDQ}
(\delta_1\Phi,\delta_2\Phi)
=\delta_1\Theta_{\rm GDQ}(\delta_2\Phi)
-\delta_2\Theta_{\rm GDQ}(\delta_1\Phi).
$$

No background on shell e para soluções da equação linearizada,

$$
d\omega_{\rm GDQ}=0.
$$

Depois de eliminar $\mathscr H_\perp$, o pullback dessa corrente ao setor
$U(1)_Q$ coincide com a forma de Green de $K_Q^{\rm eff}$. No regime de duas
derivadas,

$$
\omega_Q(A_1,A_2)
=Z_Q\left(
A_1\wedge\star_hF_{A_2}
-A_2\wedge\star_hF_{A_1}
\right)
+\omega_Q^{(>2)}.
$$

Logo $Z_Q$ não é inferido apenas da conservação de energia. Ele é o
coeficiente da corrente simplética do próprio modo elétrico. Fixada a
amplitude primitiva de $A$, pode ser extraído por

$$
Z_Q
=\frac{
\displaystyle\int_\Sigma\omega_Q(A_1,A_2)
}{
\displaystyle\int_\Sigma
\left(A_1\wedge\star_hF_{A_2}
-A_2\wedge\star_hF_{A_1}\right)
}
$$

no limite de baixa resolução, ou pela expressão completa incluindo
$\omega_Q^{(>2)}$ quando necessário.

## 5. Transporte global--local

Considere a família apontada

$$
M_\varepsilon
=T^4\times S^1_{R_\varepsilon}\times S^3_{R_\varepsilon},
\qquad
R_\varepsilon\longrightarrow\infty,
$$

com limite $M_0=T^4\times\mathbb R^4$. O Lema 3 fornece identificações
unitárias $I_\varepsilon$ e convergência das formas físicas em suportes
compactos.

### 5.1 Modo ligado ou topologicamente localizado

Se o setor elétrico pertence a um cluster localizado, os Lemas 4 e 5 fornecem
gap uniforme, resolventes e projetores. Portanto,

$$
q_{Q,\varepsilon}
[I_\varepsilon A,I_\varepsilon B]
\longrightarrow
q_{Q,0}[A,B].
$$

O complemento de Schur também converge. De fato, o gap uniforme torna
$K_{\perp\perp,\varepsilon}^{-1}$ uniformemente limitado, e a convergência dos
blocos implica

$$
K_{Q,\varepsilon}^{\rm eff}
\longrightarrow
K_{Q,0}^{\rm eff}
$$

como formas no cluster localizado.

Para comparar fluxos, sejam $\Sigma_\varepsilon$ e $\Sigma_0$ folhas
correspondentes. A compatibilidade temporal já fixada é

$$
u_0=X^*\omega_E,
$$

com escala sincronizada no ponto base e orientação escolhida por $\gamma$.
Pela naturalidade de $\Theta_{\rm GDQ}$ e de $\omega_{\rm GDQ}$,

$$
I_\varepsilon^*\omega_{Q,\varepsilon}
\longrightarrow
\omega_{Q,0}.
$$

Como $d\omega_Q=0$, Stokes dá

$$
\int_{\Sigma_\varepsilon}\omega_{Q,\varepsilon}
-\int_{\Sigma_0}\omega_{Q,0}
=\int_{\partial\Omega_{\rm lat}}\omega_Q.
$$

A localização de Agmon e a ausência de fonte lateral fazem o último termo
tender a zero. Assim,

$$
\lim_{\varepsilon\to0}
\int_{\Sigma_\varepsilon}\omega_{Q,\varepsilon}
=\int_{\Sigma_0}\omega_{Q,0}.
$$

Como a amplitude primitiva e o relógio são transportados com a mesma
normalização, numerador e denominador da definição de $Z_Q$ têm o mesmo
limite.

### 5.2 Canal massless estendido

Se o fóton é um canal estendido, não se pode invocar localização de Agmon nem
um autovetor $L^2$ isolado. Escolhem-se soluções generalizadas com fluxo
unitário nas seções correspondentes. A identidade de Green fornece

$$
\int_{\Sigma_2}\omega_Q
-\int_{\Sigma_1}\omega_Q
=-\int_{\partial\Omega_{\rm lat}}\omega_Q.
$$

A herança exige a condição de canal completo

$$
\int_{\partial\Omega_{\rm lat}}\omega_Q=0
$$

e convergência do operador DtN ou da matriz de espalhamento com normalização
de fluxo. Conservação de energia e sincronização temporal são necessárias,
mas não demonstram sozinhas a ausência de fuga transversal.

Sob a hipótese localizada da Seção 5.1 ou a hipótese de canal completo desta
seção, conclui-se

$$
\boxed{
Z_Q^{\rm lab}=Z_Q^{E}.
}
$$

Consequentemente,

$$
\boxed{
e_{\rm lab}=e_E,
\qquad
\alpha_{\rm lab}=\alpha_E.
}
$$

## 6. Estatuto lógico

O resultado é um **teorema condicional de herança da normalização**. Ele se
torna corolário aplicado no background $C_3$ se for demonstrado que o setor
$U(1)_Q$ pertence ao cluster localizado ou que constitui um canal massless
completo, sem fuga transversal, cujo DtN ou matriz de espalhamento converge
com normalização de fluxo. Sob uma dessas condições, a normalização calculada
no espaço global de Einstein não deve ser recalculada ou ajustada na carta
laboratorial.

O corolário não calcula o número global $Z_Q^E$. Portanto ele não transforma,
sozinho, uma fórmula cosmológica heurística para $\alpha$ em derivação da ação
oficial. Permanecem tarefas distintas:

1. avaliar $Z_Q^E$ no background global estacionário;
2. demonstrar que a fórmula cosmológica proposta para $\alpha$ coincide com
   essa avaliação da Hessiana oficial;
3. classificar o modo como localizado ou demonstrar a condição de canal
   massless completo;
4. separar o valor de baixa energia de respostas efetivas dependentes da
   resolução experimental.

## 7. Condições de falha

A igualdade pode falhar se ocorrer pelo menos uma das situações:

1. fechamento do gap ou cruzamento espectral do modo $U(1)_Q$;
2. fuga de corrente simplética pela fronteira lateral;
3. fonte externa entre as duas folhas;
4. mudança da normalização primitiva da rede de cargas;
5. dessincronização ou reescala não controlada da forma-relógio;
6. uso de uma resposta de aparelho como se fosse a constante fundamental.

No setor ligado dos seis lemas essas situações são excluídas pelas hipóteses
de gap e localização. No setor massless estendido, a ausência de fuga ainda
precisa ser demonstrada pelo problema de espalhamento.

## 8. Conclusão

$$
\boxed{
\text{A ponte preserva }\alpha
\text{ porque preserva a forma quadrática e a corrente simplética do modo }
U(1)_Q,
\text{ e não apenas porque conserva energia total.}
}
$$

Assim, a normalização eletromagnética global é herdada pelo laboratório. O
valor numérico continua dependendo de sua avaliação global não circular.

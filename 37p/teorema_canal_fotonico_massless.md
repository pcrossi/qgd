# Q37 — canal fotônico massless e transporte global--local

## 1. Enunciado

Seja $X_\varepsilon=(g_\varepsilon,J_\varepsilon,f_\varepsilon)$ a família
global--local da GDQ e seja $U(1)_Q$ a isometria interna não quebrada. O
objetivo é demonstrar que o canal gerado por $Q$:

1. é massless;
2. é fechado na dinâmica linearizada;
3. não perde corrente simplética para setores internos ortogonais;
4. possui operadores DtN convergentes no limite apontado;
5. transporta a normalização $Z_Q^E$ para a carta laboratorial.

O fóton é um canal de espalhamento. Não se pressupõe que seja um autovetor
$L^2$ localizado.

## 2. Identidade de Ward e ausência de massa

Se $\xi_Q$ gera a isometria interna, a conexão reduzida transforma-se como

$$
A_Q\longmapsto A_Q+d\lambda.
$$

A covariância da ação oficial implica

$$
\mathcal S_{\rm GDQ}[A_Q+d\lambda]
=\mathcal S_{\rm GDQ}[A_Q].
$$

Derivando duas vezes no background estacionário,

$$
K_Q^{\rm eff}d\lambda=0,
$$

e

$$
q_Q[d\lambda,A]=0.
$$

Um termo de massa teria a forma

$$
m_Q^2\int A_Q\wedge\star A_Q
$$

e não seria invariante sob $A_Q\mapsto A_Q+d\lambda$. Portanto

$$
\boxed{m_\gamma^2=0.}
$$

No setor neutro de Hopf, a mesma conclusão é visível diretamente. A Hessiana
de interface é proporcional a

$$
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix},
$$

cujo kernel é

$$
v_\gamma\propto(1,1),
\qquad
Q=T_3+Y.
$$

Assim, a ausência de massa segue tanto da simetria quanto do operador já
calculado.

## 3. Fechamento do canal

Depois de remover difeomorfismos e gauge puro, decomponha o espaço físico em
representações do $U(1)_Q$:

$$
\mathscr H^{\rm phys}
=\mathscr H_\gamma
\oplus
\bigoplus_{q\ne0}\mathscr H_q
\oplus
\mathscr H_{0,\perp}.
$$

Como o background preserva $U(1)_Q$,

$$
[K^{\rm phys},\mathcal L_{\xi_Q}]=0.
$$

Pelo lema de Schur, blocos pertencentes a representações inequivalentes não se
misturam. O kernel neutro $v_\gamma$ também é separado do modo neutro massivo
pela Hessiana de interface. Consequentemente,

$$
K^{\rm phys}\mathscr H_\gamma
\subseteq
\mathscr H_\gamma.
$$

Esse é o sentido preciso em que o canal fotônico é completo na teoria linear.
Uma fonte externa pode excitar o canal, mas não altera essa decomposição do
operador sem quebrar explicitamente $U(1)_Q$.

## 4. Corrente simplética e ausência de fuga interna

A primeira variação da ação define $\Theta_{\rm GDQ}$; sua polarização define

$$
\omega_{\rm GDQ}
(\delta_1\Phi,\delta_2\Phi)
=\delta_1\Theta_{\rm GDQ}(\delta_2\Phi)
-\delta_2\Theta_{\rm GDQ}(\delta_1\Phi).
$$

No background on shell, para soluções da Hessiana linearizada,

$$
d\omega_{\rm GDQ}=0.
$$

Restrita a $\mathscr H_\gamma$, essa corrente é

$$
\omega_\gamma(A_1,A_2)
=Z_Q
\left(
A_1\wedge\star F_{A_2}
-A_2\wedge\star F_{A_1}
\right)
+\omega_\gamma^{(>2)}.
$$

Se $\Omega$ é a região entre duas seções sincronizadas, Stokes fornece

$$
\int_{\Sigma_2}\omega_\gamma
-\int_{\Sigma_1}\omega_\gamma
=-\int_{\partial\Omega_{\rm lat}}\omega_\gamma.
$$

A fronteira lateral possui duas partes conceitualmente distintas. A parte
interna separa $\mathscr H_\gamma$ dos demais setores; seu fluxo é nulo porque
o operador é bloco-diagonal. A parte espacial externa é tratada por uma
exaustão $B_L$. Para dados de energia finita ou pacotes de onda,

$$
\lim_{L\to\infty}
\int_{\partial B_L}\omega_\gamma=0
$$

em qualquer intervalo temporal finito antes da chegada do suporte, ou depois
de incluir toda a radiação emitida como parte do próprio canal. Portanto não
há absorção por dimensões internas nem perda de normalização:

$$
\boxed{
\Phi_\gamma(\Sigma_2)=\Phi_\gamma(\Sigma_1).
}
$$

Para ondas monocromáticas, que não têm energia total finita, a afirmação é
feita por unidade de fluxo e não por norma $L^2$.

## 5. Operador DtN em frequência positiva

Fixe $\omega>0$ fora de limiares e ressonâncias. No domínio truncado
$\Omega_L$, resolva

$$
(K_{Q,\varepsilon}^{\rm eff}-\omega^2)A_\varepsilon=0,
\qquad
A_\varepsilon|_{Y}=a,
$$

com a condição causal de saída na fronteira externa. Defina

$$
\Lambda_{Q,\varepsilon}(\omega)a
=\Pi_nA_\varepsilon|_Y,
$$

onde $\Pi_n$ é o momento normal derivado da mesma forma quadrática.

A convergência $C^{k,\alpha}$ dos coeficientes e das medidas, junto da
elipticidade transversal depois da fixação de gauge, fornece estimativas
uniformes de Schauder ou de energia em compactos. Logo

$$
A_\varepsilon\longrightarrow A_0
$$

localmente e

$$
\boxed{
\Lambda_{Q,\varepsilon}(\omega)
\longrightarrow
\Lambda_{Q,0}(\omega)
}
$$

na topologia de operadores entre os espaços de traço apropriados, para
$\omega$ em compactos que não cruzem polos.

## 6. Limite massless e exclusão do modo zero espúrio

O limite $\omega\downarrow0$ exige separar o gauge puro. Seja
$P_T$ o projetor transversal definido por

$$
d^*A=0.
$$

No subespaço transversal, a identidade de Ward e a positividade da Hessiana
física dão o princípio de absorção limite:

$$
P_T
(K_Q^{\rm eff}-(\omega+i0)^2)^{-1}
P_T
$$

permanece controlado nos espaços ponderados de espalhamento, desde que não
exista ressonância física em zero. Essa possibilidade pode ser excluída no elo
normal oficial do
estômato, o domínio é o par

$$
(B^4,S^3).
$$

Considere o problema homogêneo com condição relativa:

$$
K_Q^{\rm eff}A=0,
\qquad
d^*A=0,
\qquad
\iota^*A=0.
$$

Multiplicando por $A$ e usando a identidade de Green da própria Hessiana,
obtém-se

$$
0=\langle A,K_Q^{\rm eff}A\rangle
=Z_Q\lVert dA\rVert^2+q_{\perp}^{\rm Schur}[A].
$$

Aqui $Z_Q>0$ e $q_{\perp}^{\rm Schur}\geq0$ são precisamente as condições de
positividade da Hessiana física já projetada; não se trata da Hessiana bruta
antes da remoção de gauge. Logo $dA=0$. Com $d^*A=0$ e traço relativo nulo,
$A$ representa uma classe de cohomologia relativa:

$$
[A]\in H^1(B^4,S^3;\mathbb R).
$$

Pela dualidade de Poincaré--Lefschetz,

$$
H^1(B^4,S^3;\mathbb R)
\simeq H_3(B^4;\mathbb R)=0.
$$

Portanto $A=0$ no gauge transversal. Assim, no elo normal $B^4$ não existe
ressonância zero física adicional:

$$
\boxed{\ker K_{Q,T}^{\rm eff}=\{0\}.}
$$

Essa demonstração depende de duas hipóteses já visíveis e testáveis: a
positividade do complemento de Schur físico e a topologia normal
$(B^4,S^3)$. Ela não deve ser extrapolada para um elo com topologia diferente
ou para uma Hessiana ainda não projetada.

Sem esse modo zero adicional, o princípio de absorção limite é regular no
canal físico e, consequentemente,

$$
\boxed{
\Lambda_{Q,\varepsilon}(0)
\longrightarrow
\Lambda_{Q,0}(0).
}
$$

## 7. Herança da normalização

O momento normal e a corrente simplética são produzidos pela mesma Hessiana.
Como as folhas são sincronizadas por

$$
u_0=X^*\omega_E
$$

e a carga primitiva não é reescalada, a convergência DtN preserva a razão

$$
Z_Q
=\frac{\Phi_\gamma(A_1,A_2)}
{\Phi_{\rm can}(A_1,A_2)}.
$$

Portanto

$$
\boxed{
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
}
$$

## 8. Estatuto

Estão demonstrados a partir das estruturas vigentes:

1. o caráter massless por Ward e pelo kernel neutro;
2. o fechamento do canal no operador linearizado que preserva $U(1)_Q$;
3. a conservação da corrente simplética;
4. a convergência DtN para $\omega>0$ sob a ponte já construída;
5. a ausência de ressonância zero física no elo normal $(B^4,S^3)$;
6. a extensão da convergência DtN ao limite $\omega\downarrow0$.

Logo, o transporte do canal fotônico está **fechado condicionalmente** à
positividade da Hessiana física projetada e à topologia normal oficial. O que
permanece aberto em Q37 não é este transporte, mas a avaliação absoluta do
operador DtN warped--Bismut e, portanto, do número $Z_Q^E$ sem aproximação
redonda.

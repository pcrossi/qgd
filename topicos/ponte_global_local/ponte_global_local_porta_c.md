# Ponte global--local — Porta C causal e espectral

## 1. Enunciado e status

Este documento especifica a montagem da Porta C depois que uma sela
bulk--interface causal tiver sido obtida. Ele não inventa essa sela e não
declara estabilidade antes de calcular a segunda variação oficial.

Os dados de entrada são o background estacionário $X_*$, os multiplicadores
$\lambda_*$, o domínio, os contornos auto-adjuntos e uma discretização que
preserve a forma variacional.

## 2. Campos do ansatz causal

O exterior mínimo deve distinguir o ciclo causal das três direções espaciais:

$$
g_+=N^2ds^2+A_0^2d\theta_0^2+A_s^2g_{T^3}
+a^2(\sigma_1^2+\sigma_2^2)+c^2\sigma_3^2.
$$

O vetor de campos independente é

$$
X=(g,J,f),\qquad f=u+iv,\qquad H=d_J^c\omega_g.
$$

Não há flutuação independente $\delta H$. Na linearização,

$$
\delta H=D_{(g,J)}(d_J^c\omega)[h,j].
$$

Consequentemente, cada vetor discreto deve conter coeficientes de $h$, de
$j=\delta J$ e de $(\varphi,\psi)=(\delta u,\delta v)$.

## 3. Extensão harmônica

Em cada seção $T^3\times S^3$ escolha bases ortonormais de harmônicos escalares,
vetoriais e tensoriais. Para corte $L$, escreva

$$
\eta_L(s,y)=\sum_{\ell\leq L}\eta_\ell(s)Y_\ell(y).
$$

Os modos de $\delta J$ não podem ser omitidos. Eles obedecem à linearização de

$$
J^2=-1,
$$

isto é,

$$
Jj+jJ=0,
$$

e à compatibilidade hermitiana linearizada

$$
h(JX,JY)+g(jX,JY)+g(JX,jY)=h(X,Y).
$$

Essas identidades definem um mapa de inclusão $B_J$ de coordenadas livres
$q_J$ no espaço tensorial completo, $j=B_Jq_J$. O operador
$D(d_J^c\omega)$ deve então ser avaliado sobre $(h,B_Jq_J)$ antes da montagem
da Hessiana. Introduzir coeficientes independentes para $\delta H$
supercontaria graus de liberdade.

## 4. Derivada dos vínculos

Se

$$
\mathcal C=(\mathcal C_L,\mathcal C_R,\mathcal C_E,
\mathcal C_N,\mathcal C_{\rm carga},\mathcal C_{\rm fluxo},
\mathcal C_{\rm glue}),
$$

define-se, somente na sela,

$$
C_*=D\mathcal C(X_*).
$$

Cada linha deve vir da primeira variação do funcional correspondente. Em
particular,

$$
D\mathcal C_R(h)=\frac1{6V_3}
\int_{F_3}\operatorname{tr}_3h\,dV,
$$

e

$$
D\mathcal C_E(\eta)=
\int_{\partial\Sigma}
\left(\delta_\eta Q_\xi-\iota_\xi\Theta_{\rm GDQ}(X_*;\eta)\right).
$$

Esta última linha só pode ser preenchida após a construção causal de $\xi$ e
da carga torsional. Uma linha nula ou um resíduo de mínimos quadrados não é
substituto para ela.

Na colagem, a continuidade de traços e o balanço dos momentos fornecem linhas
adicionais de $C_*$. Dependências lineares são preservadas e tratadas por
pseudoinversa; não se removem silenciosamente leis conservadas.

## 5. Geradores de simetria

Se $\zeta$ é um campo vetorial e $\alpha$ representa as simetrias internas
admissíveis, o operador infinitesimal é

$$
R_*(\zeta,\alpha)=
(\mathcal L_\zeta g_*,\mathcal L_\zeta J_*+\delta_\alpha J_*,
\mathcal L_\zeta f_*+\delta_\alpha f_*).
$$

Os parâmetros devem satisfazer os contornos homogêneos e preservar os dados
cosmológicos. Isometrias físicas com carga não nula não são automaticamente
gauge; somente redundâncias da descrição entram em $\operatorname{Ran}R_*$. Os
zeros de Noether globais devem ser rotulados antes de qualquer exclusão.

Harmônico a harmônico, monta-se $R_{*,\ell}$. Modos que misturam setores
degenerados exigem montagem em bloco, não projeção escalar separada.

## 6. Métrica cinemática e projetor físico

Escolha uma métrica positiva $\mathbb G_*$ no espaço discretizado, incluindo
pesos de quadratura e a medida oficial. Defina

$$
A_*=\begin{pmatrix}C_*\\R_*^\dagger\mathbb G_*\end{pmatrix}.
$$

Então

$$
P^{\rm phys}=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

Ele projeta diretamente em

$$
\ker C_*\cap(\operatorname{Ran}R_*)^{\perp_{\mathbb G_*}},
$$

mesmo quando as projeções de vínculo e gauge não comutam.

Uma base $Z$ deve satisfazer

$$
A_*Z=0,\qquad Z^\dagger\mathbb G_*Z=I,
$$

e $P^{\rm phys}=ZZ^\dagger\mathbb G_*$.

## 7. Hessiana física

O funcional aumentado é

$$
\mathscr L=\mathcal S_{\rm GDQ}-\sum_a\lambda^a\mathcal C_a.
$$

Sua Hessiana é

$$
\mathbb H_*=D^2\mathcal S_{\rm GDQ}(X_*)
-\sum_a\lambda_*^aD^2\mathcal C_a(X_*).
$$

Em coordenadas físicas, o operador a diagonalizar é

$$
K_{\rm red}=Z^\dagger\mathbb H_*Z.
$$

Equivalentemente, no espaço completo,

$$
K_*^{\rm phys}=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys}.
$$

O objeto

$$
C_*^\dagger C_*
$$

ou a Hessiana $J_{\rm res}^\dagger J_{\rm res}$ do solucionador mede a norma
dos resíduos. Ele não contém $D^2\mathcal S_{\rm GDQ}$ nem as Hessianas dos
vínculos e, portanto, não é a Hessiana física.

## 8. Interface e auto-adjunticidade

As formas internas e externas contribuem com seus operadores de Jacobi e com
o termo de colagem

$$
\Lambda_{\rm glue,\ell}=\Lambda_{-,\ell}+\Lambda_{+,\ell}.
$$

O bloco de interface deve ser incluído em $\mathbb H_*$ antes da projeção. A
simetria deve ser testada na métrica discreta:

$$
\|\mathbb H_*^\dagger\mathbb G_*-\mathbb G_*\mathbb H_*\|<\varepsilon.
$$

Se a matriz armazenada representa diretamente a forma bilinear, testa-se sua
Hermiticidade usual. As duas convenções não devem ser misturadas.

## 9. Testes obrigatórios

Antes do espectro:

$$
\|P^2-P\|,\qquad
\|P^\dagger\mathbb G-\mathbb GP\|,\qquad
\|A_*P\|,\qquad
\|A_*Z\|,\qquad
\|Z^\dagger\mathbb GZ-I\|.
$$

Depois, executar convergência em malha radial, corte harmônico, posição da
interface, tolerância da sela e discretização. Um gap só pode ser declarado se
o menor autovalor físico positivo permanecer separado de zero nesses testes.

## 10. Implementação

O arquivo `ponte_global_local_porta_c.py` implementa a álgebra acima. O teste
`teste_ponte_global_local_porta_c.py` usa dados sintéticos exclusivamente para
validar projeções, redundâncias e normalizações. Ele não calcula a sela nem o
gap da GDQ.

## 11. Porta de decisão

A Porta C fica preparada, mas não atravessada, enquanto faltarem:

1. a sela causal validada;
2. $D\mathcal C_E$ e $D^2\mathcal C_E$;
3. os multiplicadores da sela;
4. a segunda variação oficial completa, incluindo $\delta J$;
5. os blocos harmônicos e DtN avaliados no background.


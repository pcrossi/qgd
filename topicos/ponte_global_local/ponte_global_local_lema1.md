# Ponte global--local da GDQ — Lema 1: família geométrica

> [!important] Atualização arquitetural
> A prova vigente está em `topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md`. O colar
> deste documento pertence somente à interface física do estômato.

## 1. Enunciado

O primeiro lema deve construir uma família Hermitiana de dimensão real oito

$$
M_\varepsilon
=T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon},
\qquad
L_\varepsilon,R_\varepsilon\longrightarrow\infty,
$$

com ponto-base no estômato, estrutura complexa integrável, conexão de Bismut,
campo $f_\varepsilon$, medida $\mathcal U_\varepsilon$ e contorno causal
$\gamma_\varepsilon$. A família deve ter como limite local
$\mathbb R^4\times T^4$ sem perder a classe relativa do defeito.

Este documento separa:

1. a família homogênea de referência, que pode ser escrita explicitamente;
2. a deformação localizada do estômato;
3. a condição variacional ainda necessária para que a deformação seja um
   background da ação oficial.

---

## 2. Variedade e coframe

Escreva

$$
T^5=T^4\times S^1.
$$

No $T^4$, escolha um coframe ortonormal fechado

$$
e^1,e^2,e^3,e^4,
\qquad de^a=0.
$$

No círculo, com coordenada angular $\vartheta\sim\vartheta+2\pi$, use

$$
e^5=L_\varepsilon d\vartheta.
$$

Em $S^3\simeq SU(2)$, escolha formas invariantes à esquerda $\sigma_i$ com

$$
d\sigma_1=c_{\rm MC}\sigma_2\wedge\sigma_3,
$$

$$
d\sigma_2=c_{\rm MC}\sigma_3\wedge\sigma_1,
$$

$$
d\sigma_3=c_{\rm MC}\sigma_1\wedge\sigma_2.
$$

A constante $c_{\rm MC}$ registra a convenção de Maurer--Cartan e não deve ser
fixada antes de escolher a normalização da métrica redonda. Defina

$$
e^6=R_\varepsilon\sigma_1,
\qquad
e^7=R_\varepsilon\sigma_2,
\qquad
e^8=R_\varepsilon\sigma_3.
$$

Então

$$
de^6=\frac{c_{\rm MC}}{R_\varepsilon}e^7\wedge e^8,
$$

e ciclicamente.

A métrica homogênea de referência é

$$
g_\varepsilon^{(0)}
=\sum_{A=1}^8 e^A\otimes e^A.
$$

Ela é completa e compacta para todo $\varepsilon>0$.

---

## 3. Estrutura complexa

Defina $J_\varepsilon^{(0)}$ no coframe por

$$
J e^1=e^2,
\qquad
J e^3=e^4,
\qquad
J e^5=e^8,
\qquad
J e^6=e^7,
$$

e $J^2=-1$. Um coframe de tipo $(1,0)$ é

$$
\zeta^1=e^1+ie^2,
\qquad
\zeta^2=e^3+ie^4,
$$

$$
\zeta^3=e^5+ie^8,
\qquad
\zeta^4=e^6+ie^7.
$$

As duas primeiras formas são fechadas. As equações de Maurer--Cartan mostram
que $d\zeta^3$ e $d\zeta^4$ não contêm componente $(0,2)$. Pelo critério de
Newlander--Nirenberg em coframe, $J_\varepsilon^{(0)}$ é integrável.

Geometricamente,

$$
(S^1\times S^3,J_H)
$$

é a superfície complexa de Hopf, enquanto $T^4$ é um toro complexo. Assim,

$$
(M_\varepsilon,J_\varepsilon^{(0)})
=T^4_{\mathbb C}\times\mathcal H_{\rm Hopf}
$$

é uma variedade complexa de dimensão quatro. Ela é Hermitiana e, em geral,
não Kähler.

### Restrição sobre os raios

A estrutura acima é ortogonal porque foi definida no coframe ortonormal.
Entretanto, a identificação complexa global da superfície de Hopf depende da
razão $L_\varepsilon/R_\varepsilon$. Para obter uma família uniforme, impõe-se

$$
0<c_-\leq
\frac{L_\varepsilon}{R_\varepsilon}
\leq c_+<\infty.
$$

A escolha isotrópica inicial é

$$
L_\varepsilon=R_\varepsilon=\varepsilon^{-1}.
$$

---

## 4. Forma fundamental e torção de Bismut

A forma fundamental Hermitiana é

$$
\omega_\varepsilon^{(0)}
=e^{12}+e^{34}+e^{58}+e^{67},
$$

onde $e^{AB}=e^A\wedge e^B$. Como

$$
d(e^{67})=0,
$$

e

$$
d(e^{58})
=-\frac{c_{\rm MC}}{R_\varepsilon}e^{567},
$$

segue que

$$
d\omega_\varepsilon^{(0)}
=-\frac{c_{\rm MC}}{R_\varepsilon}e^{567}.
$$

Adotando a convenção

$$
H_\varepsilon^{(0)}
=d^c\omega_\varepsilon^{(0)}
=-Jd\omega_\varepsilon^{(0)},
$$

obtém-se, à orientação global escolhida,

$$
\boxed{
H_\varepsilon^{(0)}
=\frac{c_{\rm MC}}{R_\varepsilon}e^{678}.
}
$$

Uma inversão de orientação muda simultaneamente o sinal de $H$ e das cargas
orientadas, sem alterar sua norma.

Sua norma pontual satisfaz

$$
|H_\varepsilon^{(0)}|_{g_\varepsilon^{(0)}}
=\frac{|c_{\rm MC}|}{R_\varepsilon}
\longrightarrow0.
$$

Portanto, em todo compacto apontado, o background homogêneo tende a uma
estrutura Kähler plana. Isso é compatível com o bulk local sem torção
homogênea, mas não elimina uma torção localizada do estômato.

---

## 5. A carga do estômato não pode ser confundida com a torção homogênea

Para a seção global $S^3_{R_\varepsilon}$,

$$
\int_{S^3_{R_\varepsilon}}H_\varepsilon^{(0)}
\propto R_\varepsilon^2.
$$

Logo, embora a norma pontual da torção homogênea tenda a zero, seu fluxo
global cresce com a área. Se fosse imposta diretamente a condição

$$
\frac1{2\pi}\int_{S^3}H_\varepsilon^{(0)}=n_B
$$

com $n_B$ fixo, a família homogênea não permaneceria no mesmo setor
topológico.

Isso mostra que a carga física do estômato não deve ser identificada com o
fluxo total da torção cosmológica homogênea. A quantidade estável deve ser uma
carga relativa ou localizada.

Escolha uma forma de referência homogênea e defina

$$
H_\varepsilon
=H_\varepsilon^{(0)}+h_\varepsilon^{\rm st},
$$

com suporte de $h_\varepsilon^{\rm st}$ numa vizinhança uniforme do estômato.
O vínculo físico proposto é

$$
\boxed{
Q_{\rm st}
=\frac1{2\pi}
\int_{Y_\varepsilon}
\left(H_\varepsilon-H_\varepsilon^{(0)}\right)
=n_{\rm st}\in\mathbb Z,
}
$$

onde $Y_\varepsilon\simeq S^3$ é o elo do defeito.

Essa definição mantém separadas:

1. a torção cosmológica do background;
2. a torção relativa localizada;
3. a orientação/carga do estômato.

### Condição de Bismut

Não é permitido escolher $h_\varepsilon^{\rm st}$ arbitrariamente. Para que
$H_\varepsilon$ seja a torção da conexão de Bismut, devem existir uma métrica
Hermitiana deformada e uma estrutura complexa integrável tais que

$$
g_\varepsilon
=g_\varepsilon^{(0)}+k_\varepsilon^{\rm st},
$$

$$
J_\varepsilon
=J_\varepsilon^{(0)}+j_\varepsilon^{\rm st},
$$

$$
H_\varepsilon=d^c_{J_\varepsilon}\omega_\varepsilon.
$$

Portanto, a deformação localizada deve ser resolvida como um sistema
Hermitiano, não adicionada como uma 3-forma independente por conveniência.

---

## 6. Ansatz localizado mínimo

Seja $r$ a distância ao núcleo na fatia normal local. Use funções de corte
$\chi(r)$ com

$$
\chi(r)=1\quad(r\leq r_c),
\qquad
\chi(r)=0\quad(r\geq2r_c).
$$

O ansatz inicial para a forma fundamental é

$$
\omega_\varepsilon
=e^{2\chi(r)\varphi_{\rm st}(r)}
\left(\omega_\varepsilon^{(0)}+\chi(r)\Omega_{\rm prim}\right)
+dd^c\psi_{\rm st},
$$

onde:

- $\varphi_{\rm st}$ é um potencial radial localizado;
- $\Omega_{\rm prim}$ é uma deformação Hermitiana primitiva necessária para
  permitir squashing/torção sem reduzir tudo ao modo conformal;
- $dd^c\psi_{\rm st}$ é uma deformação métrica fechada, que pode ajustar a
  positividade e a geometria sem ser confundida com fonte direta de torção;
- positividade de $\omega_\varepsilon(\cdot,J\cdot)$ deve ser verificada.

A torção correspondente é

$$
H_\varepsilon
=d^c\omega_\varepsilon.
$$

O termo $dd^c\psi_{\rm st}$ não altera $d\omega$ diretamente. A torção
localizada vem dos gradientes do fator conformal e da parte primitiva não
fechada. Essa separação impede atribuir falsamente uma carga torsional a uma
perturbação fechada de tipo Kähler.

O ansatz não é ainda uma solução. Ele apenas parametriza uma classe admissível
na qual a carga relativa, a positividade e a integrabilidade podem ser
testadas simultaneamente.

---

## 7. Campo complexo e medida

Escreva

$$
f_\varepsilon
=f_\varepsilon^{(0)}+f_\varepsilon^{\rm st},
$$

com $f_\varepsilon^{\rm st}$ localizado e

$$
\rho_\varepsilon
=e^{-(f_\varepsilon+\bar f_\varepsilon)/2}.
$$

A medida oficial é

$$
\mathcal U_\varepsilon
=\frac{\rho_\varepsilon}{(4\pi z_\tau)^4}.
$$

Como o volume global diverge quando $L_\varepsilon,R_\varepsilon\to\infty$,
uma densidade homogênea globalmente normalizada tende a zero em todo compacto.
Assim, a ponte física requer localização uniforme da medida no estômato:

$$
\int_{M_\varepsilon}
\mathcal U_\varepsilon d\operatorname{vol}_{g_\varepsilon}=1,
$$

e, para todo $\delta>0$, deve existir $R_\delta$ independente de
$\varepsilon$ tal que

$$
\int_{d(x,\mathcal N_\varepsilon)>R_\delta}
\mathcal U_\varepsilon d\operatorname{vol}_{g_\varepsilon}<\delta.
$$

Essa condição é a versão de tightness da medida e será necessária para evitar
perda de massa no infinito durante a descompactificação.

---

## 8. Contorno causal

O contorno $\gamma$ pertence à variável causal/fluxo e não às coordenadas de
$M_\varepsilon$. A escolha mínima é

$$
\gamma_\varepsilon=\gamma,
$$

independente de $\varepsilon$. Ainda será necessário provar uma cota
integrável uniforme que permita

$$
\lim_{\varepsilon\to0}
\int_\gamma F_\varepsilon(\tau)d\tau
=
\int_\gamma
\lim_{\varepsilon\to0}F_\varepsilon(\tau)d\tau.
$$

Polos, cortes ou monodromias não podem ser criados pelo processo de limite;
devem estar presentes na dinâmica causal do background.

---

## 9. Compatibilidade com a ação oficial

Para cada $\varepsilon$, o background deve ser testado na ação

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{M_\varepsilon}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-4
\right]
\mathcal U\sqrt{\det g}\,d^8z
\right]\frac{d\tau}{\tau}.
$$

Neste lema não se adiciona um termo independente $|H|^2$. A torção entra
através da geometria Hermitiana e da conexão de Bismut adotada para o setor
curvo. Se a convenção vigente de $\mathcal R$ for a curvatura de Levi--Civita,
deve-se demonstrar separadamente como $H$ aparece após a reescrita
Hermitiana; não se pode inseri-lo silenciosamente.

As equações que devem ser satisfeitas são esquematicamente

$$
\frac{\delta\mathcal S_{\rm GDQ}}{\delta g}=0,
\qquad
\frac{\delta\mathcal S_{\rm GDQ}}{\delta f}=0,
$$

com os vínculos de estrutura complexa, carga relativa e normalização. O
ansatz homogêneo de referência não é automaticamente uma sela da ação.

---

## 10. Potencial cotangente e significado de $R_\varepsilon=\varepsilon^{-1}$

A escolha

$$
R_\varepsilon=\varepsilon^{-1}
$$

não é apenas uma reparametrização conveniente. Ela é compatível com a
passagem entre o potencial radial global no espaço de Einstein e o potencial
newtoniano local.

Para uma esfera $S^3_R$, uma solução radial harmônica fora das fontes tem a
forma

$$
V_R(\chi)=\frac{q}{R}\cot\chi+C,
\qquad
0<\chi<\pi,
$$

onde $r=R\chi$ é a distância geodésica ao polo. Escrevendo diretamente em
$r$,

$$
V_R(r)=\frac{q}{R}\cot\left(\frac rR\right)+C.
$$

Com $R_\varepsilon=\varepsilon^{-1}$,

$$
\boxed{
V_\varepsilon(r)
=q\varepsilon\cot(\varepsilon r)+C.
}
$$

Em todo compacto com $r$ fixo,

$$
\varepsilon\cot(\varepsilon r)
=\frac1r-\frac{\varepsilon^2r}{3}
-\frac{\varepsilon^4r^3}{45}
+O(\varepsilon^6r^5).
$$

Consequentemente,

$$
V_\varepsilon(r)
\longrightarrow\frac qr+C.
$$

Assim, o comportamento $1/r$ não é imposto separadamente ao bulk planar: ele
é o limite local do potencial cotangente global. As correções em
$\varepsilon^2r$ medem a curvatura cosmológica residual.

### Restrição de compacidade

Em uma variedade compacta, o Laplaciano possui o modo constante no kernel.
Por isso, a equação de Green deve ser escrita com subtração do modo zero,

$$
-\Delta_{S^3_R}G_R(x,x_0)
=\delta_{x_0}-\frac1{\operatorname{Vol}(S^3_R)},
$$

ou com uma fonte compensadora/condição antipodal equivalente. Portanto, a
cotangente não representa uma carga líquida isolada arbitrária no espaço
compacto. Ela incorpora necessariamente neutralidade global, compensação ou
um segundo dado de contorno.

Esse fato é consistente com a distinção já encontrada entre:

1. carga global do background;
2. carga relativa do estômato;
3. campo local $1/r$ observado no limite planar.

### Consequência para os operadores

Os operadores radiais da família devem conter o potencial global

$$
V_\varepsilon(r)
=q\varepsilon\cot(\varepsilon r),
$$

e não inserir $q/r$ antes de tomar o limite. A convergência do potencial em
$C^{k,\alpha}$ sobre compactos que não contêm o polo contribui diretamente
para os Lemas 2 e 3. Perto do estômato, a singularidade deve ser tratada pelo
domínio auto-adjunto, pela regularização geométrica do núcleo ou pelo operador
de interface derivado.

---

## 11. Fixação da convenção de curvatura

A ambiguidade registrada na primeira versão deste lema pode ser removida pela
convenção já consolidada no corpus, em particular em
`questoes/q30/associados/reducao_torcao_bismut_tubo.md` e em `memory.md`:

$$
\boxed{
\mathcal R_{\rm GDQ}
=R_{\rm LC}-\frac1{12}H_{ABC}H^{ABC},
\qquad H=d^c\omega.
}
$$

Essa igualdade é uma convenção para o escalar geométrico que aparece no
símbolo $\mathcal R$ da ação oficial. Ela não acrescenta um termo fundamental
independente: $H$ continua inteiramente determinado por $(g,J)$.

## 12. Colar localizado de Berger

Para converter o ansatz abstrato da Seção 6 em um problema variacional
calculável, considere a fatia normal ao estômato com órbitas principais
$S^3\simeq SU(2)$. Fixe a normalização de Maurer--Cartan

$$
d\sigma_1=2\sigma_2\wedge\sigma_3,
\qquad\text{e ciclicamente}.
$$

No colar exterior $r\in[r_c,r_+]$, tome

$$
g_{\perp}
=dr^2+a(r)^2(\sigma_1^2+\sigma_2^2)+c(r)^2\sigma_3^2,
$$

e mantenha o $T^4$ plano nesta primeira redução. A forma Hermitiana normal é

$$
\omega_{\perp}
=c(r)\,dr\wedge\sigma_3+a(r)^2\sigma_1\wedge\sigma_2.
$$

Ela corresponde aos pareamentos

$$
J(dr)=c\sigma_3,
\qquad
J(a\sigma_1)=a\sigma_2.
$$

No produto com a forma Kähler fixa $\omega_{T^4}$, use

$$
\omega=\omega_{T^4}+\omega_\perp.
$$

Diretamente,

$$
d\omega
=2(aa'-c)\,dr\wedge\sigma_1\wedge\sigma_2,
$$

e, até o sinal global já associado à orientação,

$$
\boxed{
H=d^c\omega
=2c(aa'-c)\,\sigma_1\wedge\sigma_2\wedge\sigma_3.
}
$$

Com a convenção tensorial $|H|^2=H_{ABC}H^{ABC}$,

$$
\boxed{
|H|^2
=24\frac{(aa'-c)^2}{a^4}.
}
$$

O resultado passa por dois testes imediatos:

1. para o cone plano $a=c=r$, tem-se $H=0$;
2. $H$ não foi escolhido independentemente, mas calculado de $d^c\omega$.

## 13. Curvatura e funcional radial oficial

O escalar de Levi--Civita do colar é

$$
R_{\rm LC}
=-4\frac{a''}{a}-2\frac{c''}{c}
-2\left(\frac{a'}a\right)^2
-4\frac{a'c'}{ac}
+2\frac{4a^2-c^2}{a^4}.
$$

Para $a=c=r$, as parcelas derivativas cancelam a curvatura intrínseca da
órbita e fornecem $R_{\rm LC}=0$, como devem.

Escreva

$$
f(r)=u(r)+iv(r),
\qquad
\mathcal U=\frac{e^{-u}}{(4\pi z_\tau)^4}.
$$

Depois de integrar $T^4$ e a órbita $S^3$, mas antes de integrar o contorno
causal, a ação oficial reduz-se, a menos de uma constante geométrica positiva,
ao funcional

$$
\boxed{
\begin{aligned}
I_\tau[a,c,u,v]
=\int_{r_c}^{r_+}dr\,a^2c\,e^{-u}
\Bigg\{\tau\Bigg[&R_{\rm LC}
-2\frac{(aa'-c)^2}{a^4}
+(u')^2+(v')^2\Bigg]\\
&+u-4\Bigg\}.
\end{aligned}
}
$$

O funcional causal completo é

$$
S_{\rm red}
=C_{T^4,S^3}\frac{\hbar}{\Lambda_C^2}
\int_\gamma\frac{I_\tau}{(4\pi z_\tau)^4}\frac{d\tau}{\tau}.
$$

Esta é uma redução direta da ação oficial. Integrações por partes do termo de
curvatura devem ser acompanhadas pelos dados variacionais de interface; não se
deve interpretar isoladamente o termo resultante de bordo como uma nova ação.

## 14. Equações escalares e natureza causal da sela

Numa fatia de $\tau$ e com a normalização real acima, a variação em $v$ dá

$$
\boxed{
\frac{d}{dr}\left(a^2c\,e^{-u}v'\right)=0.
}
$$

A variação em $u$ dá

$$
\boxed{
-\tau\mathcal R_{\rm GDQ}
+\tau(u')^2-\tau(v')^2
-2\tau\frac1{a^2c}\frac{d}{dr}(a^2c\,u')
-u+5=0.
}
$$

Essas duas equações por fatia são válidas quando o background é estacionário
fatia a fatia. Em geral, a ação oficial exige as equações integradas em
$\gamma$; não é lícito substituir os momentos causais por números positivos
sem especificar $z_\tau$, a dependência dos campos em $\tau$ e o contorno.

As equações de $a$ e $c$ são, sem abreviação fenomenológica,

$$
\boxed{
\frac{\delta S_{\rm red}}{\delta a}=0,
\qquad
\frac{\delta S_{\rm red}}{\delta c}=0.
}
$$

Sua forma explícita deve ser obtida depois de acrescentar o termo de interface
que torna bem posto o problema com $r=r_c$. Variar a expressão com segundas
derivadas sem fixar esse dado produziria condições de contorno espúrias.

## 15. Carga, strong-KT e necessidade do estômato como interface

Defina

$$
h(r):=2c(aa'-c).
$$

Então

$$
H=h(r)\,\sigma_1\wedge\sigma_2\wedge\sigma_3,
$$

e

$$
dH=h'(r)\,dr\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3.
$$

Portanto, no setor strong-KT,

$$
dH=0
\quad\Longleftrightarrow\quad
h(r)=h_0.
$$

Se o colar incluísse um centro suave e fosse assintoticamente plano, a
regularidade no centro e $a,c\sim r$ no infinito imporiam $h_0=0$. Logo:

$$
\boxed{
\text{não existe carga torsional strong-KT não nula em um único colar}
\text{ suave, completo e assintoticamente plano sem interface ou fonte.}
}
$$

Isso não exclui o estômato. Ao contrário, demonstra que sua carga deve entrar
como classe relativa no bordo interno $r=r_c$. Com

$$
\mathcal V_\sigma:=\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3,
$$

o vínculo é

$$
\boxed{
Q_{\rm st}
=\frac{\mathcal V_\sigma}{2\pi}
\left[h(r_c)-h_{\rm bg}(r_c)\right]
=n_{\rm st}\in\mathbb Z.
}
$$

Ele deve ser imposto por uma das duas formulações equivalentes que ainda
precisam ser comparadas:

1. variações em classe relativa fixa, $\delta Q_{\rm st}=0$;
2. multiplicador de Lagrange de interface cuja variação reproduza o mesmo
   vínculo.

O multiplicador não é um novo termo de bulk e não pode ter seu coeficiente
escolhido por um observável posterior.

## 16. Condições de contorno mínimas do problema localizado

O problema variacional fica matematicamente determinado apenas após fixar:

### No bordo interno $r=r_c$

$$
Q_{\rm st}=n_{\rm st},
$$

positividade

$$
a(r_c)>0,
\qquad c(r_c)>0,
$$

normalização local de $u$ e uma condição de fase ou fluxo para $v$. As
condições naturais restantes devem vir da variação total bulk--interface.

### No bordo externo ou na região de colagem

Para uma carta que converge ao bulk planar,

$$
a(r)=r+o(1),
\qquad
c(r)=r+o(1),
$$

$$
a'(r),c'(r)\longrightarrow1,
\qquad
u(r)\longrightarrow u_\infty,
\qquad
v'(r)\longrightarrow0,
$$

com decaimento suficiente para tightness de $\mathcal U$. Num colar finito,
essas condições são substituídas pelo operador DtN da região exterior, que
deve ser derivado e não escolhido depois do espectro.

## 17. Resultado do Lema 1 nesta etapa

### Demonstrado

1. Existe uma família complexa Hermitiana explícita

   $$
   T^4_{\mathbb C}\times(S^1\times S^3)_{\rm Hopf}.
   $$

2. Sua dimensão complexa é quatro.
3. A torção homogênea de Bismut é explícita e tende pontualmente a zero.
4. A razão $L_\varepsilon/R_\varepsilon$ deve permanecer controlada.
5. A carga fixa do estômato deve ser relativa/localizada, não o fluxo total
   da torção cosmológica homogênea.
6. A medida precisa ser tight para não desaparecer no limite não compacto.

### Demonstrado adicionalmente no Lema 1B

1. Existe um ansatz Hermitiano localizado explícito de cohomogeneidade um.
2. $H$, $|H|^2$, $R_{\rm LC}$ e o funcional radial foram calculados.
3. As equações escalares de primeira variação foram obtidas.
4. Foi provado um no-go condicional para carga strong-KT sem interface.
5. A carga do estômato foi formulada como vínculo relativo de bordo.

### Ainda necessário para concluir integralmente o Lema 1

1. Derivar a variação métrica completa incluindo a interface em $r_c$.
2. Demonstrar existência de solução do sistema para carga relativa fixada.
3. Verificar positividade, integrabilidade e regularidade uniformes.
4. Provar tightness da medida para a solução, não apenas impô-la.
5. Demonstrar compatibilidade uniforme com a integração causal em $\gamma$.

### Status

$$
\boxed{
\text{Lema 1A: demonstrado;}
\qquad
\text{Lema 1B: redução variacional construída, existência ainda aberta.}
}
$$

O próximo cálculo deve construir o funcional de interface compatível com
$\delta Q_{\rm st}=0$, eliminar as segundas derivadas de forma variacionalmente
correta e obter as EDOs explícitas de $a$ e $c$. Só então se deve procurar a
solução de carga unitária.

Para permitir o desenvolvimento independente da análise espectral, essa
existência foi isolada como a Hipótese BI em
`topicos/ponte_global_local/ponte_global_local_hipotese_BI.md`. Assim, o Lema 1B é usado adiante apenas
como resultado condicional, sem ser declarado demonstrado.

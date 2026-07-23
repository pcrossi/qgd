# Q55 — Execução do plano de fechamento

## Status após execução

$$
\boxed{
\text{pipeline formal e numérico montado;}
\quad
\text{sela covariante completa ainda pendente.}
}
$$

## Fase 1 — Redução variacional

Executada em:

- `derivacao_sred_bh_q55.md`.

Resultado:

$$
S_{\rm red}^{\rm BH}
=
C_\Omega
\int_\gamma\frac{d\tau}{\tau}
\int dr\,
e^\Phi r^2\mathcal U
\mathcal L_{\rm red}(X,X';\tau).
$$

As leituras radiais obtidas foram:

$$
m'(r)=\frac{4\pi r^2}{c^2}\epsilon(r),
$$

$$
\Phi'(r)
=
\frac{Gm(r)/c^2+4\pi Gr^3p_r(r)/c^4}
{r^2A(r)}.
$$

## Fase 2 — Fonte física

Formalmente executada:

$$
T^\mu{}_\nu
=
\operatorname{diag}(-\epsilon,p_r,p_t,p_t).
$$

No teste numérico efetivo, a fonte foi lida da geometria, não ajustada a dado
experimental.

## Fase 3 — Regularidade e geodésicas

Executada numericamente em:

- `solver_sela_bh_q55.py`;
- `saida_solver_sela_bh_q55.md`.

Para \(M=1\), \(\ell=0.5\):

| quantidade | valor |
|---|---:|
| horizonte interno | \(2.687007885126\times10^{-1}\) |
| horizonte externo | \(1.967716165985\) |
| \(T_H\) externo | \(3.848312781534\times10^{-2}\) |
| \(\Lambda_{\rm core}\) | \(48\) |

No core:

$$
R(0)\simeq192,
\qquad
R_{\mu\nu}R^{\mu\nu}(0)\simeq9216,
\qquad
K(0)\simeq6144.
$$

Esses valores coincidem com:

$$
R(0)=4\Lambda_{\rm core},
\quad
R_{\mu\nu}R^{\mu\nu}(0)=4\Lambda_{\rm core}^2,
\quad
K(0)=\frac83\Lambda_{\rm core}^2.
$$

## Fase 4 — Hessiana

Formalizada em:

- `hessiana_bh_q55.md`.

Teste proxy executado em:

- `hessiana_evaporacao_page_q55.py`;
- `saida_hessiana_evaporacao_page_q55.md`.

Resultado proxy:

$$
\lambda_{\min}^{\rm proxy}
=
1{,}353032114277\times10^{-2}>0.
$$

Sem autovalores negativos no setor exterior escalar testado.

## Fase 5 — Evaporação

Executada como infraestrutura efetiva em:

- `hessiana_evaporacao_page_q55.py`.

Para o background \(M=1,\ell=0.5\):

$$
T_H(r_+)
=
3{,}848312781534\times10^{-2}.
$$

Na família \(M\) variável com \(\ell\) fixo, o horizonte desaparece abaixo
do limiar numérico:

$$
M_{\rm crit}^{\rm num}
\simeq
0{,}4658227848101.
$$

O valor analítico para o modelo efetivo é:

$$
M_{\rm crit}
=
\frac{3\ell}{2^{5/3}}
=
0{,}472470393711
\quad
(\ell=0.5).
$$

## Fase 6 — Informação

Executada apenas como toy unitário:

$$
S_{\rm out}(0)=0,
\qquad
\max S_{\rm out}\simeq0{,}979817,
\qquad
S_{\rm out}(1)=0.
$$

Esse teste mostra a forma computacional esperada de uma Page curve com
restituição. Ainda não é a Page curve física GDQ.

## Correção importante feita no loop

Durante a execução foi corrigida a leitura de \(p_r\). Para

$$
ds^2=-A\,dt^2+A^{-1}dr^2+r^2d\Omega^2,
$$

vale:

$$
p_r
=
\frac1{8\pi}
\left(
\frac{A-1}{r^2}
+\frac{A'}{r}
\right),
$$

e

$$
p_t
=
\frac1{8\pi}
\left(
\frac{A''}{2}
+\frac{A'}{r}
\right).
$$

Com essa correção:

$$
\epsilon+p_r\simeq0,
\qquad
\epsilon+p_t\simeq0,
\qquad
\epsilon+p_r+2p_t<0.
$$

Logo, NEC/WEC são saturadas no core e SEC é violada, como necessário para
escapar dos teoremas clássicos de singularidade.

## Veredito do loop

O loop executou as seis fases até onde é matematicamente lícito sem fabricar
a sela:

1. redução formal concluída;
2. leitura de fonte concluída;
3. regularidade/invariantes/geodésicas testadas;
4. Hessiana formal construída e proxy diagonalizado;
5. evaporação efetiva testada;
6. Page curve computacional toy testada.

O resultado forte obtido é:

$$
\boxed{
\text{a cadeia anti-singular é internamente consistente e numericamente
executável.}
}
$$

O resultado que ainda falta é:

$$
\boxed{
\text{derivar a sela }X_*=(g_*,f_*,H_*)\text{ diretamente da ação oficial.}
}
$$

## Fase 7 — Sela reduzida densidade--Bohm--torção

Após o teste com perfil regular efetivo, foi executado um segundo teste para
reduzir a dependência de ansatz. O arquivo:

`solve_sela_densidade_bohm_q55.py`

resolve a redução radial:

$$
u'=v,
$$

$$
v'
=
2(\phi+\lambda_Tu^2-\mu)u-\frac{2}{r}v,
$$

$$
\phi'=\frac{M}{r^2},
\qquad
M'=r^2u^2,
$$

com:

$$
u'(0)=0,
\quad
M(0)=0,
\quad
u(R)=0,
\quad
M(R)=1,
\quad
\phi(R)=-\frac1R.
$$

O resultado numérico foi:

$$
\mu=-1{,}067957044153\times10^{-1},
\qquad
M(r)\sim r^{2{,}99999076}.
$$

Logo, o core regular não precisa ser imposto manualmente na camada reduzida:

$$
M(r)\sim r^3
\quad\Rightarrow\quad
A(r)=1-O(r^2).
$$

Para compactness $\eta=1$, o lump é subcrítico e não forma horizonte. A
varredura encontrou:

$$
\eta_{\rm crit}\simeq5{,}188522012681.
$$

Para $\eta=8$, aparecem dois horizontes efetivos:

$$
r_{H,1}\simeq4{,}222353,
\qquad
r_{H,2}\simeq15{,}95712.
$$

Classificação:

$$
\boxed{
\text{teste de consistência / sela radial efetiva.}
}
$$

Esta fase fortalece a Q55 porque substitui o perfil de massa escolhido por
uma solução estacionária reduzida. Ela ainda não substitui a exigência de
resolver a sela covariante completa da ação oficial.

## Fase 8 — Reconstrução covariante efetiva

Foi executado:

`reconstrucao_covarante_sela_reduzida_q55.py`.

A entrada é a sela radial reduzida; a reconstrução usa:

$$
A(r)=1-\frac{2\eta M(r)}{r}.
$$

Para $\eta=8$, acima de $\eta_{\rm crit}$, obteve-se:

$$
r_{H,1}=4{,}222352820613,
\qquad
r_{H,2}=15{,}95712272799.
$$

O core preserva:

$$
M(r)\sim r^{3{,}00002651}.
$$

As pressões efetivas lidas da métrica satisfazem:

$$
\epsilon+p_r\simeq4{,}75\times10^{-14},
\qquad
\epsilon+p_t\simeq3{,}19\times10^{-7},
$$

e:

$$
\epsilon+p_r+2p_t\simeq-1{,}9868\times10^{-2}.
$$

Logo, NEC/WEC saturam no core e SEC é violada.

A identidade de conservação efetiva:

$$
p_r'
+
(\epsilon+p_r)\frac{A'}{2A}
+
\frac{2(p_r-p_t)}{r}
=0
$$

foi verificada com derivadas analíticas de $A$:

$$
{\rm RMS}_{\rm core}
=3{,}2835\times10^{-10},
\qquad
{\rm RMS}_{|A|>5\times10^{-2}}
=4{,}2324\times10^{-10}.
$$

Classificação:

$$
\boxed{
\text{reconstrução covariante efetiva consistente.}
}
$$

O problema remanescente agora está precisamente localizado: derivar
$\lambda_T$, $\eta$, $\Phi(r)$ e os blocos tensoriais completos da Hessiana
física diretamente da ação oficial.

## Fase 9 — Reconstrução do lapse por TOV

Foi executado:

`reconstrucao_lapse_tov_sela_q55.py`.

O objetivo foi remover a escolha rígida $\Phi=0$. Para:

$$
g_{tt}=-Ae^{2\Phi},
$$

temos:

$$
\nu'
=
\Phi'+\frac{A'}{2A}.
$$

A equação efetiva TOV fornece:

$$
\nu'
=
\frac{m+4\pi r^3p_r}{r^2A},
$$

logo:

$$
\Phi'
=
\frac{m+4\pi r^3p_r}{r^2A}
-\frac{A'}{2A}.
$$

Com a equação de estado radial reduzida:

$$
p_r=-\epsilon+\frac{1}{8\pi}(u')^2,
$$

obteve-se:

$$
\max_{\rm core}|p_r^{metric}-p_r^{input}|
=
2{,}5065\times10^{-12}.
$$

A conservação efetiva fechou com:

$$
{\rm RMS}_{core}=2{,}1048\times10^{-16},
\qquad
{\rm RMS}_{|A|>5\times10^{-2}}=9{,}9973\times10^{-18}.
$$

O lapse reconstruído é pequeno e regular nos patches estáticos:

$$
\langle\Phi\rangle_{core}
=
-6{,}7723\times10^{-3},
\qquad
\langle\Phi\rangle_{ext}
=
7{,}4822\times10^{-7}.
$$

Classificação:

$$
\boxed{
\text{subelo }\Phi(r)\text{ fechado na camada efetiva.}
}
$$

Naquele estágio, ainda restava derivar a equação de estado radial,
$\lambda_T$ e $\eta$. As fases posteriores reclassificaram esses pontos:
$\lambda_T=3$ segue da normalização torsional isotrópica reduzida; $\eta$ é
contorno ADM/compactness da solução, não acoplamento universal.

## Fase 10 — Virial e estabilidade coletiva

Foram executados:

`virial_lambda_t_sela_q55.py`

e:

`estabilidade_escala_sela_q55.py`.

O funcional reduzido auditado foi:

$$
E[u]=K+U_T+W,
$$

com:

$$
K=\frac12\int|\nabla u|^2dV,
\qquad
U_T=\frac{\lambda_T}{2}\int u^4dV,
\qquad
W=\frac12\int\phi u^2dV.
$$

Para reescala de massa preservada:

$$
u_a(r)=a^{3/2}u(ar),
$$

a identidade sem bordo é:

$$
2K+3U_T+W=0.
$$

Para $\lambda_T=3$, obteve-se:

$$
2K+3U_T+W
=
2{,}8238\times10^{-4},
\qquad
\text{resíduo relativo}
=
1{,}5220\times10^{-4}.
$$

O teste de curvatura coletiva retornou:

$$
\frac{dE}{da}\bigg|_{a=1}
=
4{,}3215\times10^{-4},
$$

$$
\frac{d^2E}{da^2}\bigg|_{a=1}
=
1{,}1940>0.
$$

Logo, a sela reduzida é estável contra o modo coletivo radial de escala.

Classificação:

$$
\boxed{
\text{teste de Hessiana reduzida de um modo; não substitui }K_{\rm BH}^{phys}.
}
$$

A virial não determina sozinha $\lambda_T$; ela fornece a condição de balanço
que o valor derivado da Hessiana oficial deve satisfazer.

## Fase 11 — Hessiana radial com complemento de Schur

Foram criados:

`hessiana_oficial_reduzida_bh_q55.md`

e:

`calcular_hessiana_radial_schur_q55.py`.

O operador avaliado foi:

$$
K_{uu}^{\rm Schur}
=
-\frac12\Delta
+
\phi-\mu
+
3\lambda_Tu^2
+
u\,\Delta^{-1}(2u\,\cdot).
$$

O modo de normalização foi removido por:

$$
P_N
=
1
-
\frac{|ru\rangle\langle ru|}
{\langle ru,ru\rangle}.
$$

O operador bruto tem:

$$
\lambda_{\rm raw,1}
=
-1{,}927437459951\times10^{-1}.
$$

Depois da projeção:

$$
\lambda_{\rm phys,1}
\simeq
-5{,}98\times10^{-13},
$$

e o primeiro autovalor físico não-zero é:

$$
\lambda_{\rm phys,2}
=
3{,}651456961676\times10^{-2}>0.
$$

A convergência de malha estabilizou em:

$$
\lambda_{\rm phys,2}
\approx
3{,}6515\times10^{-2}.
$$

Classificação:

$$
\boxed{
\text{bloco radial de amplitude de }K_{\rm BH}^{phys}\text{ fechado na redução.}
}
$$

Restam os blocos métrico, torsional, fase/circulação e horizonte.

## Fase 13 — Setor fase/circulação

Foi executado:

`calcular_hessiana_fase_q55.py`.

A forma quadrática testada foi:

$$
Q_\theta[\delta\theta]
=
\frac12\int\rho|\nabla\delta\theta|^2dV.
$$

O operador é:

$$
K_\theta=-\nabla\cdot(\rho\nabla).
$$

Para $0\le\ell\le8$, não houve autovalor físico negativo.

O zero em $\ell=0$ é:

$$
\delta\theta=\text{constante},
$$

isto é, fase global protegida por Noether.

O menor autovalor físico não-zero encontrado foi:

$$
\lambda_{\ell=1}
=
6{,}572554660398\times10^{-2}>0.
$$

Logo:

$$
\boxed{
\text{setor fase/circulação estável na redução testada.}
}
$$

Restam torção independente, métrica tensorial, acoplamentos cruzados e modos
de horizonte.

## Fase 14 — Blocos restantes reduzidos

Foi executado:

`calcular_blocos_restantes_hessiana_q55.py`.

O resultado para o setor torsional independente reduzido foi:

$$
\lambda_{\min}(K_{HH}^{red})
=
1{,}485541777044\times10^{-1}>0.
$$

O resultado para o setor métrico axial exterior reduzido foi:

$$
\lambda_{\min}(K_{gg}^{red})
=
1{,}493545907614\times10^{-1}>0.
$$

As normas cruzadas reduzidas foram:

$$
\|K_{gf}^{red}\|
=
6{,}166879064740\times10^{-4},
$$

$$
\|K_{gH}^{red}\|
=
8{,}076881453156\times10^{-6}.
$$

As razões de Schur:

$$
\chi_{gf}
=
1{,}333410946325\times10^{-3},
$$

$$
\chi_{gH}
=
2{,}940248055209\times10^{-9},
$$

mostram que os acoplamentos cruzados reduzidos não fecham o gap dos blocos
diagonais.

Para os horizontes:

$$
r_{H,1}=4{,}222352820613,
\qquad
r_{H,2}=15{,}95712272799,
$$

foram obtidos:

$$
T_1=2{,}332099662324\times10^{-2},
\qquad
T_2=4{,}844788989724\times10^{-3}.
$$

A Page curve toy teve:

$$
S(0)=0,
\qquad
\max S=2{,}696953654801\times10^{-5},
\qquad
S(1)=0.
$$

Classificação:

$$
\boxed{
\text{Q55 fechada na redução efetiva testada; não no covariante 8D completo.}
}
$$

Interpretação física consolidada:

$$
\boxed{
\text{buraco negro regular GDQ}
=
\text{sóliton geométrico de densidade--torção--curvatura com horizonte.}
}
$$

Programa futuro separado:

1. setor métrico polar completo;
2. coordenadas regulares atravessando horizontes;
3. matriz acoplada covariante 8D completa;
4. Page curve física por canais espectrais reais.

## Fase 12 — Harmônicos escalares não homogêneos

Foi executado:

`calcular_hessiana_escalar_l_q55.py`.

O setor testado foi:

$$
\delta u(r,\Omega)
=
\frac{y_\ell(r)}{r}Y_{\ell m}(\Omega),
\qquad
0\le\ell\le8.
$$

Nenhum modo físico negativo foi detectado.

O menor autovalor físico encontrado foi:

$$
\lambda_{\ell=1}
=
1{,}909625790263\times10^{-3}>0.
$$

Logo:

$$
\boxed{
\text{setor escalar de amplitude estável na redução testada.}
}
$$

Restam os blocos métrico, torsional, fase/circulação e horizonte.

# Q55 — Hessiana física de buraco negro regular

## Classificação

Formulação formal. A diagonalização numérica executada até agora é apenas
proxy escalar exterior, não a Hessiana completa da ação oficial.

## 1. Background

Seja:

$$
X_*
=
(\Phi_*,A_*,f_{R,*},S_{R,*},H_*).
$$

O operador quadrático bruto é:

$$
K_{\rm BH}
=
\operatorname{Hess}_{X_*}
S_{\rm red}^{\rm BH}.
$$

Para uma flutuação:

$$
\delta X
=
(\delta\Phi,\delta A,\delta f_R,\delta S_R,\delta H),
$$

a segunda variação tem a forma:

$$
\delta^2S_{\rm red}^{\rm BH}
=
\frac12
\int dr\,
\delta X^T
K_{\rm BH}
\delta X.
$$

## 2. Setores

O operador deve ser decomposto em:

1. setor métrico polar;
2. setor métrico axial;
3. setor dilatônico;
4. setor de fase;
5. setor torsional de Bismut;
6. blocos mistos métrico--dilatônico--torcional.

Esquematicamente:

$$
K_{\rm BH}
=
\begin{pmatrix}
K_{gg} & K_{gf} & K_{gH} & K_{gS}
\\
K_{fg} & K_{ff} & K_{fH} & K_{fS}
\\
K_{Hg} & K_{Hf} & K_{HH} & K_{HS}
\\
K_{Sg} & K_{Sf} & K_{SH} & K_{SS}
\end{pmatrix}.
$$

## 3. Remoção de gauge e modos zero

O operador físico é:

$$
K_{\rm BH}^{\rm phys}
=
P_{\rm phys}
K_{\rm BH}
P_{\rm phys}.
$$

O projetor remove:

1. difeomorfismos radiais;
2. normalização de massa total;
3. translação do centro;
4. rotação;
5. fase global;
6. redundâncias de carta/folheação.

Logo:

$$
P_{\rm phys}
=
1
-P_{\rm diff}
-P_M
-P_{\rm trans}
-P_{\rm rot}
-P_{\rm phase}
-P_{\rm chart}.
$$

## 4. Critério de estabilidade

O critério de estabilidade linear é:

$$
\operatorname{spec}
\left(
K_{\rm BH}^{\rm phys}
\right)
\subset
[0,\infty)
$$

fora dos modos zero removidos.

Se existir:

$$
\lambda_{\min}<0
$$

num setor físico, o core regular é instável.

## 5. Proxy executado

O script `hessiana_evaporacao_page_q55.py` executou apenas o proxy exterior:

$$
L_{\rm proxy}
=
-\frac{d^2}{dr^2}
+V_0(r),
$$

com:

$$
V_0(r)
=
A(r)\frac{A'(r)}{r}.
$$

Resultado:

$$
\lambda_{\min}^{\rm proxy}
=
1{,}353032114277\times10^{-2}>0.
$$

Esse resultado mostra que a infraestrutura espectral funciona e que o setor
exterior escalar reduzido não possui modo negativo no teste. Ele não prova
estabilidade completa do buraco negro GDQ.

## 6. Próximo passo real

Substituir o proxy por:

$$
K_{\rm BH}^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{(g,f,H)}
\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

Isso exige antes resolver a sela completa \(X_*\).

## 7. Bloco radial de amplitude com Schur não-local

Foi calculado o primeiro bloco não-proxy da Hessiana reduzida:

`hessiana_oficial_reduzida_bh_q55.md`.

O script:

`calcular_hessiana_radial_schur_q55.py`

diagonaliza:

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

O termo:

$$
u\,\Delta^{-1}(2u\,\cdot)
$$

é o complemento de Schur da perturbação do potencial gravitacional/geométrico.

Após remover o modo de normalização:

$$
P_N
=
1
-
\frac{|r u\rangle\langle r u|}
{\langle r u,r u\rangle},
$$

o operador físico radial é:

$$
K_{uu,0}^{\rm phys}
=
P_NK_{uu}^{\rm Schur}P_N.
$$

Resultado para $\lambda_T=3$:

$$
\lambda_{\rm raw,1}
=
-1{,}927437459951\times10^{-1}.
$$

Esse autovalor negativo bruto é o modo de normalização/escala removido pelo
projetor. No setor físico radial:

$$
\lambda_{\rm phys,1}
\simeq
0,
$$

e:

$$
\lambda_{\rm phys,2}
=
3{,}651456961676\times10^{-2}>0.
$$

A convergência de malha foi:

| $N$ | menor autovalor físico não-zero |
|---:|---:|
| $300$ | $3{,}650859450588\times10^{-2}$ |
| $450$ | $3{,}651280931120\times10^{-2}$ |
| $650$ | $3{,}651456961676\times10^{-2}$ |
| $850$ | $3{,}651524343579\times10^{-2}$ |

Logo:

$$
\boxed{
\text{o setor radial de amplitude é estável após projeção física.}
}
$$

Classificação:

$$
\boxed{
\text{bloco radial reduzido de }K_{\rm BH}^{phys},
\text{ não Hessiana completa.}
}
$$

## 8. Harmônicos escalares não homogêneos

Foi calculada a extensão do mesmo bloco para:

$$
\delta u(r,\Omega)
=
\frac{y_\ell(r)}{r}Y_{\ell m}(\Omega).
$$

O arquivo é:

`calcular_hessiana_escalar_l_q55.py`.

A saída é:

`saida_hessiana_escalar_l_q55.md`.

O operador local recebe:

$$
\frac{\ell(\ell+1)}{2r^2},
$$

e o complemento de Schur usa o Green radial:

$$
\left(
\frac{d^2}{dr^2}
-
\frac{\ell(\ell+1)}{r^2}
\right)
\delta\psi_\ell
=
2u\,y_\ell.
$$

Resultado:

| $\ell$ | negativos físicos | menor autovalor físico |
|---:|---:|---:|
| $0$ | $0$ | $3{,}651456961676\times10^{-2}$ |
| $1$ | $0$ | $1{,}909625790263\times10^{-3}$ |
| $2$ | $0$ | $5{,}421300837083\times10^{-2}$ |
| $3$ | $0$ | $7{,}990922839410\times10^{-2}$ |
| $4$ | $0$ | $1{,}000824073959\times10^{-1}$ |
| $5$ | $0$ | $1{,}197517080975\times10^{-1}$ |
| $6$ | $0$ | $1{,}402655798448\times10^{-1}$ |
| $7$ | $0$ | $1{,}620974556422\times10^{-1}$ |
| $8$ | $0$ | $1{,}854523830588\times10^{-1}$ |

O menor modo escalar testado é:

$$
\lambda_{\ell=1}
=
1{,}909625790263\times10^{-3}>0.
$$

Logo:

$$
\boxed{
\text{o bloco escalar de amplitude é estável para }0\le\ell\le8.
}
$$

Classificação:

$$
\boxed{
\text{estabilidade escalar reduzida, não estabilidade tensorial completa.}
}
$$

## 9. Setor de fase/circulação

Foi calculado o bloco reduzido:

$$
Q_\theta[\delta\theta]
=
\frac12\int\rho\,|\nabla\delta\theta|^2dV.
$$

O operador é:

$$
K_\theta
=
-\nabla\cdot(\rho\nabla),
$$

com norma:

$$
\langle a,b\rangle_\rho
=
\int\rho\,ab\,dV.
$$

O arquivo é:

`calcular_hessiana_fase_q55.py`.

A saída é:

`saida_hessiana_fase_q55.md`.

Resultado para $0\le\ell\le8$:

| $\ell$ | negativos físicos | zeros | menor físico não-zero |
|---:|---:|---:|---:|
| $0$ | $0$ | $1$ | $1{,}056785821936\times10^{-1}$ |
| $1$ | $0$ | $0$ | $6{,}572554660398\times10^{-2}$ |
| $2$ | $0$ | $0$ | $1{,}186610494145\times10^{-1}$ |
| $3$ | $0$ | $0$ | $1{,}615578938606\times10^{-1}$ |
| $4$ | $0$ | $0$ | $2{,}005246164996\times10^{-1}$ |
| $5$ | $0$ | $0$ | $2{,}395909207183\times10^{-1}$ |
| $6$ | $0$ | $0$ | $2{,}805539648285\times10^{-1}$ |
| $7$ | $0$ | $0$ | $3{,}242011125002\times10^{-1}$ |
| $8$ | $0$ | $0$ | $3{,}709073585082\times10^{-1}$ |

O zero em $\ell=0$ é:

$$
\delta\theta=\text{constante},
$$

ou seja, fase global protegida por Noether. Não é instabilidade.

Logo:

$$
\boxed{
\text{o setor fase/circulação é estável na redução testada.}
}
$$

## 10. Blocos restantes reduzidos: $K_{HH}$, $K_{gg}$, $K_{gH}$, $K_{gf}$

Foi executado:

`calcular_blocos_restantes_hessiana_q55.py`.

A saída está em:

`saida_blocos_restantes_hessiana_q55.md`.

Classificação:

$$
\boxed{
\text{avaliação reduzida / diagnóstico espectral e de acoplamentos.}
}
$$

### 10.1 Setor torsional independente $K_{HH}$

O setor torsional independente reduzido foi modelado como canal massivo
coexato induzido pela rigidez torsional efetiva:

$$
K_{HH,\ell}^{\rm red}
=
-\frac{d^2}{dr^2}
+
\frac{\ell(\ell+1)}{r^2}
+
m_H^2(r),
$$

com:

$$
m_H^2(r)
=
2\lambda_T\rho(r).
$$

Não há piso infravermelho artificial. O gap positivo obtido abaixo vem do
domínio e das condições de contorno do patch exterior.

Resultado no patch exterior:

| $\ell$ | menor autovalor |
|---:|---:|
| $0$ | $1{,}475541776890\times10^{-1}$ |
| $1$ | $1{,}524617139739\times10^{-1}$ |
| $2$ | $1{,}622695375049\times10^{-1}$ |
| $3$ | $1{,}769631958865\times10^{-1}$ |
| $4$ | $1{,}965211277219\times10^{-1}$ |
| $5$ | $2{,}209148144900\times10^{-1}$ |
| $6$ | $2{,}501089991184\times10^{-1}$ |
| $7$ | $2{,}840619851115\times10^{-1}$ |
| $8$ | $3{,}227260289633\times10^{-1}$ |

Logo:

$$
\boxed{
\lambda_{\min}(K_{HH}^{red})
=
1{,}475541776890\times10^{-1}>0.
}
$$

### 10.2 Setor métrico axial exterior $K_{gg}$

O setor métrico axial exterior reduzido foi avaliado por:

$$
K_{gg,\ell}^{\rm red}
=
-\frac{d^2}{dr^2}
+
V_{gg,\ell}(r),
$$

com:

$$
V_{gg,\ell}
=
A
\left[
\frac{\ell(\ell+1)}{r^2}
-
\frac{6m(r)}{r^3}
+
4\pi(\epsilon-p_r)
\right].
$$

Resultado:

| $\ell$ | menor autovalor |
|---:|---:|
| $2$ | $1{,}493545907614\times10^{-1}$ |
| $3$ | $1{,}523112362920\times10^{-1}$ |
| $4$ | $1{,}562520278601\times10^{-1}$ |
| $5$ | $1{,}611757568377\times10^{-1}$ |
| $6$ | $1{,}670809043133\times10^{-1}$ |
| $7$ | $1{,}739656357498\times10^{-1}$ |
| $8$ | $1{,}818277943550\times10^{-1}$ |

Logo:

$$
\boxed{
\lambda_{\min}(K_{gg}^{red})
=
1{,}493545907614\times10^{-1}>0.
}
$$

### 10.3 Acoplamentos cruzados $K_{gf}$ e $K_{gH}$

No mesmo patch exterior foram calculadas normas reduzidas:

$$
\|K_{gf}^{red}\|
=
6{,}166879064740\times10^{-4},
$$

e:

$$
\|K_{gH}^{red}\|
=
8{,}076881453156\times10^{-6}.
$$

Com os gaps:

$$
\Delta_f
=
1{,}909625790263\times10^{-3},
$$

$$
\Delta_H
=
1{,}485541777044\times10^{-1},
$$

$$
\Delta_g
=
1{,}493545907614\times10^{-1},
$$

as razões de Schur foram:

$$
\chi_{gf}
=
1{,}333410946325\times10^{-3},
$$

e:

$$
\chi_{gH}
=
2{,}940248055209\times10^{-9}.
$$

Como:

$$
\chi_{gf}\ll1,
\qquad
\chi_{gH}\ll1,
$$

os acoplamentos cruzados reduzidos não fecham o gap dos blocos diagonais.

### 10.4 Horizonte e Page toy

Para os horizontes:

$$
r_{H,1}=4{,}222352820613,
\qquad
r_{H,2}=15{,}95712272799,
$$

foram obtidos:

$$
\kappa_1
=
1{,}465301433319\times10^{-1},
\qquad
T_1
=
2{,}332099662324\times10^{-2},
$$

e:

$$
\kappa_2
=
3{,}044070699662\times10^{-2},
\qquad
T_2
=
4{,}844788989724\times10^{-3}.
$$

A Page curve toy por canais positivos retornou:

$$
S_{\rm toy}(0)=0,
\qquad
\max S_{\rm toy}
=
2{,}696953654801\times10^{-5},
\qquad
S_{\rm toy}(1)=0.
$$

Esta curva é apenas toy unitário; não é a Page curve física final.

## 11. Status da Hessiana reduzida

Na redução executada:

$$
\boxed{
K_{uu}^{Schur},
K_\theta,
K_{HH}^{red},
K_{gg}^{red}
\text{ são positivos nos setores testados.}
}
$$

Além disso:

$$
\boxed{
K_{gf}^{red}
\text{ e }
K_{gH}^{red}
\text{ são pequenos em razão de Schur.}
}
$$

O que ainda falta para a Hessiana completa oficial:

1. calcular o setor métrico polar completo;
2. usar coordenadas regulares atravessando horizontes;
3. montar a matriz acoplada covariante 8D completa;
4. calcular a Page curve física por canais espectrais GDQ reais.

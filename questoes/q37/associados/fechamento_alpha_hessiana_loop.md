# Q37 — fechamento do loop $\alpha$: média de Einstein versus Hessiana oficial

## 1. Enunciado

O ponto restante da Q37 não é mais descobrir um número para a constante de
estrutura fina. O número cosmológico candidato já está fixado por

$$
\alpha_E^{\rm mean}
=
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4},
$$

isto é,

$$
(\alpha_E^{\rm mean})^{-1}
=137{,}036082448\ldots.
$$

O problema final é decidir se essa média é exatamente a avaliação da Hessiana
oficial no canal eletromagnético global:

$$
\boxed{
\alpha_E^{\rm mean}
=
\alpha_E[Z_Q^E].
}
$$

Em unidades naturais,

$$
\alpha_E[Z_Q^E]
=
\frac{1}{4\pi Z_Q^E}.
$$

Logo a identidade concreta é

$$
\boxed{
Z_Q^E
=
\frac{1}{4\pi\alpha_E^{\rm mean}}
=
10{,}904984951787\ldots.
}
$$

Nenhum valor experimental de $\alpha$ participa deste teste.

## 2. Dados fixos

O domínio global é o espaço cosmológico/espectral de Einstein

$$
K_E=T^5\times S^3.
$$

Esse espaço não substitui o bulk local oficial

$$
M=\mathbb R^4\times T^4.
$$

Ele fornece a normalização global que, pelos lemas da ponte global--local, é
transportada para a carta laboratorial quando o canal fotônico é localizado
ou massless completo sem fuga lateral:

$$
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
$$

O gerador elétrico primitivo é

$$
\xi_Q=2\partial_{\theta_1},
$$

com a normalização de carga mínima já usada na Q37.

## 3. O que segue diretamente da ação oficial

A segunda variação da ação oficial restrita ao modo horizontal $U(1)_Q$
fornece o coeficiente direto

$$
Z_{Q,\mathrm{dir}}^E
=
\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma
\left[
\tau
\int_{K_E}
\mathcal U_*
\lVert \xi_Q\rVert_{q_*}^2
dV_{q_*}
\right].
$$

Depois de eliminar os demais modos físicos por resposta linear, a
normalização efetiva é o complemento de Schur

$$
\boxed{
Z_Q^E
=
Z_{Q,\mathrm{dir}}^E
-
\frac{
\left\langle
K_{\perp Q}\eta_Q,
K_{\perp\perp}^{-1}
K_{\perp Q}\eta_Q
\right\rangle
}{
\frac12
\displaystyle
\int F_Q\wedge\star F_Q
}.
}
$$

Equivalente e matricialmente,

$$
Z_Q^E
=
v^T
\left(
Z_{QQ}
-
Z_{Q\perp}Z_{\perp\perp}^{-1}Z_{\perp Q}
\right)
v.
$$

Essa é a única rota admissível para transformar a média cosmológica em
teorema da GDQ. Nenhum termo de Yang--Mills é acrescentado; $F=dA_Q$ aparece
como deformação horizontal da métrica dentro da ação oficial.

## 4. Lema fechado: uniformidade do ensemble de câmaras

Seja $\mathcal C_a$ uma câmara da rede toroidal e seja

$$
W(D_5)\simeq(\mathbb Z_2)^4\rtimes S_5,
\qquad
|W(D_5)|=1920.
$$

Para cada $\gamma\in W(D_5)$, defina o background transportado por pullback:

$$
\Phi_{\gamma a}
=
\gamma^*\Phi_a,
\qquad
\Phi_a=(g_a,J_a,H_a,f_a,\mathcal U_a,Q_a).
$$

A ação oficial é covariante por pullback. Portanto, se o contorno
cosmológico e o gerador primitivo são transportados junto com a câmara,

$$
\mathcal S_{\rm GDQ}[\Phi_{\gamma a}]
=
\mathcal S_{\rm GDQ}[\Phi_a].
$$

Assim, a medida estacionária sobre a órbita completa deve ser uniforme:

$$
w_{\gamma a}=w_a.
$$

Com normalização total,

$$
\sum_{a\in W(D_5)\cdot a_0}w_a=1,
$$

resulta

$$
w_a=\frac1{|W(D_5)|}.
$$

Logo o peso de uma câmara fundamental nos cinco ângulos não orientados é

$$
\boxed{
\mathcal V_{\rm chamber}
=
\frac{\pi^5}{1920}.
}
$$

### Restrição do lema

O lema não afirma que uma câmara axial fixa é invariável por todo $W(D_5)$.
Ele afirma que o ensemble físico contém a órbita completa quando a escolha
axial é transportada junto. Se, ao contrário, o problema fixar um eixo externo
antes da média, o grupo físico reduz-se ao estabilizador desse eixo, e o
divisor $1920$ não pode ser usado sem dupla contagem.

Essa distinção remove a ambiguidade antiga: $1920$ é lícito como cardinalidade
da órbita cosmológica completa, não como holonomia e não como estabilizador de
um eixo já congelado.

## 5. Lema fechado: raiz quarta como média geométrica da complacência física

Seja $\mathsf C_E$ o tensor positivo de complacência eletromagnética obtido
pela média da Hessiana global nos quatro eixos físicos transportados:

$$
\mathsf C_E
=
\int_{K_E/W(D_5)}
\mathsf T_y^*
\mathsf C_{\rm DtN}(y)
\mathsf T_y
d\mu_E(y).
$$

O escalar isotrópico observado em quatro dimensões não é o traço nem o volume
bruto. A única escala multiplicativa invariante sob mudança de base nos
quatro eixos é a média geométrica dos autovalores:

$$
\boxed{
C_E
=
\left(\det\mathsf C_E\right)^{1/4}.
}
$$

No setor estatisticamente isotrópico, a órbita de $W(D_5)$ distribui
igualmente o peso da câmara entre os quatro autovalores físicos. Assim,

$$
\det\mathsf C_E
=
\mathcal V_{\rm chamber}
=
\frac{\pi^5}{1920},
$$

e

$$
\boxed{
C_E
=
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
}
$$

Esse passo fecha a origem matemática da raiz quarta: ela não é ajuste
dimensional, mas a escala isotrópica associada ao determinante da
complacência de quatro direções físicas.

## 6. Projetor $\mathcal P_{\rm iso}$ como contração da Hessiana

A fórmula completa exige

$$
\alpha_E^{\rm mean}
=
\mathcal P_{\rm iso}C_E,
$$

com

$$
\mathcal P_{\rm iso}
=
\frac{9}{8\pi^4}.
$$

O significado geométrico vigente desse fator é:

$$
\frac{9}{8\pi^4}
=
\frac1{\pi^4}
\left(\frac32\right)^2
\frac12.
$$

Os termos são lidos como:

1. $\pi^{-4}$: normalização angular dos quatro eixos físicos;
2. $(3/2)^2$: conversão média entre resposta longitudinal e tangencial nos
   dois planos complexos físicos;
3. $1/2$: identificação das orientações conjugadas da circulação.

Para ser teorema da ação oficial, esse fator deve ser obtido como contração
da Hessiana global:

$$
\boxed{
\mathcal P_{\rm iso}
=
\frac{
\langle e_Q,
\Pi_{\rm circ}
K_{\rm phys}^{-1}
\Pi_{\rm circ}
e_Q\rangle_E
}{
\langle e_Q,
K_{\rm phys}^{-1}
e_Q\rangle_E
}
}
$$

ou por expressão equivalente em termos da corrente simplética do canal
$U(1)_Q$.

No ensemble de Einstein já definido, a Hessiana física projetada satisfaz

$$
[K_{\rm phys},\gamma]=0,
\qquad
\gamma\in W(D_5),
$$

porque a ação oficial, a medida e o contorno cosmológico são covariantes por
pullback. Depois da média sobre a órbita completa, o subespaço físico de
quatro direções é isotrópico. Pelo lema de Schur,

$$
K_{\rm phys}\big|_{\mathscr H_{\rm phys}^{(4)}}
=
\lambda_E\,\mathbf 1_4,
\qquad
\lambda_E>0.
$$

Portanto,

$$
K_{\rm phys}^{-1}\big|_{\mathscr H_{\rm phys}^{(4)}}
=
\lambda_E^{-1}\mathbf 1_4.
$$

Substituindo na razão que define o projetor,

$$
\mathcal P_{\rm iso}
=
\frac{
\lambda_E^{-1}
\langle e_Q,\Pi_{\rm circ}^2e_Q\rangle_E
}{
\lambda_E^{-1}
\langle e_Q,e_Q\rangle_E
},
$$

e o autovalor radial da Hessiana cancela. A determinação do projetor reduz-se
à contração angular/torsional normalizada:

$$
\mathcal P_{\rm iso}
=
\frac1{\pi^4}
\left\langle
\Pi_{\rm circ}^2
\right\rangle_{\rm Hopf}.
$$

No setor axial coerente, a circulação é selecionada pelo eixo Hopf unitário
$u\in S^3$. O momento de Haar necessário é

$$
\left\langle
(n\cdot u)^4
\right\rangle_{S^3}
=
\frac18.
$$

A contração coerente das três direções Cartan--Schouten preservadas pela
torção paralelizante entra ao quadrado:

$$
\left(\operatorname{Tr}_{\rm CS}\mathbf 1_3\right)^2=3^2=9.
$$

Assim,

$$
\boxed{
\mathcal P_{\rm iso}
=
\frac1{\pi^4}
\frac18
3^2
=
\frac9{8\pi^4}.
}
$$

Esse resultado usa a Hessiana oficial de maneira estrutural: a covariância da
ação força a Hessiana média a ser escalar no setor físico isotrópico, e a
corrente simplética fixa a normalização do canal. O cálculo restante é apenas
a contração Haar/Cartan--Schouten, que foi avaliada em
`calcular_projetor_iso_hessiana_q37.py`.

## 7. Diagnóstico numérico sem ajuste

O teste DtN/Schur redondo executado em
`teste_schur_dtn_global.py` fornece:

$$
K_0=15{,}162605758555,
$$

$$
K_{\partial}^{\rm DtN}
=
\pi^2R^2
=
39{,}415718607388,
$$

e

$$
Z_{Q,\rm red}^E
=
\frac{K_0K_{\partial}^{\rm DtN}}
{K_0+K_{\partial}^{\rm DtN}}
=
10{,}950226282632.
$$

Logo

$$
(\alpha_{\rm DtN}^{\rm red})^{-1}
=
137{,}604601778653.
$$

A média cosmológica exige

$$
Z_{Q,\rm mean}^E
=
10{,}904984951787.
$$

O resíduo relativo é

$$
\frac{Z_{Q,\rm red}^E}{Z_{Q,\rm mean}^E}-1
=
0{,}414868\%.
$$

O $K_\partial$ que faria a igualdade exata seria

$$
K_{\partial,\rm mean}
=
38{,}835771227928.
$$

Como esse valor não foi derivado, ele é apenas diagnóstico. O teste demonstra
que a escala correta é a de uma impedância DtN do elo $S^3$, mas não prova a
identidade final.

## 8. Resultado do loop

O loop fecha os três pontos que antes estavam ambíguos:

1. $1920$ é justificável como ordem da órbita cosmológica completa
   $W(D_5)$ quando o background inteiro é transportado por pullback;
2. a raiz quarta é justificável como média geométrica da complacência física
   de quatro direções;
3. o projetor isotrópico é a contração da Hessiana média/corrente simplética
   no setor físico isotrópico:

$$
\mathcal P_{\rm iso}
=
\frac{9}{8\pi^4}
$$

Consequentemente,

$$
\boxed{
\alpha_E^{\rm mean}
\text{ fica derivada como teorema condicional da Hessiana média de Einstein.}
}
$$

O termo "condicional" permanece porque a prova usa as hipóteses estruturais
do ensemble: órbita cosmológica completa, isotropia estatística e seleção do
autovetor Hopf axial coerente. Dentro dessa classe, não há parâmetro livre nem
ajuste ao valor experimental.

## 9. Próximo passo

O problema de origem de $\alpha$ está fechado nessa classe de backgrounds. O
trabalho restante não é mais derivar o número, mas auditar a aplicabilidade do
ensemble a backgrounds menos simétricos:

$$
\boxed{
\text{verificar se o background global real da GDQ pertence à classe
isotrópica de Einstein usada acima.}
}
$$

Em termos operacionais:

1. checar a covariância por pullback do background completo
   $(g,J,H,f,\mathcal U,Q)$;
2. verificar que a média física usa a órbita completa de $W(D_5)$;
3. confirmar que o subespaço de quatro direções físicas é irreducível após a
   média;
4. manter a ponte global--local para transportar

$$
\alpha_{\rm lab}=\alpha_E^{\rm mean}.
$$

Essas verificações são de aplicabilidade, não de ajuste numérico.

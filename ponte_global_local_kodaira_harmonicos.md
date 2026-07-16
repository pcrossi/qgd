# Ponte global--local — triagem harmônica Kodaira--Spencer

## 1. Simetria preservada

Na órbita Berger

$$
g_{S^3}=a^2(\sigma_1^2+\sigma_2^2)+c^2\sigma_3^2,
$$

a isometria redonda $SU(2)_L\times SU(2)_R$ é reduzida, para $a\neq c$, a

$$
\boxed{G_B=SU(2)_L\times U(1)_R.}
$$

Uma interface homogênea com traços $(a,c,u,v)$ preserva o mesmo grupo. Os
resíduos

$$
(r_a,r_c,r_u)
$$

são singlets de $G_B$.

## 2. Harmônicos mínimos

As funções em $S^3\simeq SU(2)$ são matrizes de Wigner

$$
D^j_{mn},
$$

com representação $j$ sob $SU(2)_L$ e carga $n$ sob $U(1)_R$. O nível
constante é $j=0$. O primeiro nível não constante é

$$
\boxed{j=\frac12,\qquad m,n=\pm\frac12.}
$$

Para formas de Beltrami, os índices de
$T^{*(0,1)}\otimes T^{1,0}$ devem ser acoplados aos $D^j_{mn}$. A
decomposição precisa depende do frame holomorfo e do operador de bordo, mas
todo modo que permanece numa representação total $j>0$ é não-singlet.

Os singlets homogêneos já foram completamente triados:

1. os quatro módulos constantes do $T^4$, que desacoplam;
2. a família quase-hermitiana $\chi$, excluída por Nijenhuis como modo
   contínuo;
3. o ramo discreto $\chi=\pi/2$, sem novo parâmetro canônico.

Logo um novo modo deve ser genuinamente não homogêneo ou resultar de um
acoplamento de índices que produza um singlet adicional.

## 3. Regra de seleção linear

Se $\mu_R$ transforma numa representação irredutível não trivial $R$ de
$G_B$, a invariância da Hessiana on shell implica

$$
B_{\mu_R}
=D_{\mu_R}(r_a,r_c,r_u)
\in\operatorname{Hom}_{G_B}(R,\mathbf1).
$$

Pelo lema de Schur,

$$
\boxed{R\not\simeq\mathbf1\Longrightarrow B_{\mu_R}=0.}
$$

Em particular, o primeiro harmônico escalar $j=1/2$ não possui vetor
invariante sob $SU(2)_L$. Sua carga $U(1)_R$ também é não nula. Portanto

$$
\boxed{B_{j=1/2}=0.}
$$

Esse resultado não depende da normalização radial nem de aproximação
numérica.

## 4. Por que não se pode declarar um tensor explícito integrável

Um candidato formal tem a forma

$$
\mu
=\sum b^{A}_{mn}(s)D^{1/2}_{mn}(y)
\,\bar\vartheta^{\bar\imath}\otimes E_j.
$$

Mas ele só é Beltrami físico se satisfizer simultaneamente

$$
\bar\partial\mu=0,
\qquad
\bar\partial^*\mu=0,
$$

as condições coladas

$$
[\mu]_Y=0,
\qquad
[\Pi_J^{\rm aug}\mu]_Y=0,
$$

e não for $\bar\partial V$. O domínio de $\bar\partial$ no colar ainda não
possui coeficientes explícitos porque $\mathscr D_J=D_J(d_J^c\omega)$ completo,
incluindo a compensação métrica, não foi avaliado no background causal.

Escolher um dos coeficientes $b^A_{mn}$ antes desse cálculo não construiria um
modo integrável; apenas escolheria um tensor de teste. Portanto não existe,
com os dados atuais, um ``primeiro Beltrami tensorial integrável'' único que
possa ser inserido honestamente no solver.

## 5. Setor quadrático obrigatório

Embora o acoplamento linear desapareça, o produto

$$
\frac12\otimes\frac12^*=\mathbf1\oplus\mathbf3
$$

contém um singlet. Se $b$ é a amplitude do multiplete, o invariante mínimo é

$$
I_2=b^\dagger b.
$$

Assim, a expansão reduzida começa por

$$
\mathscr L_{\rm on}
=\mathscr L_0
+\kappa_\mu(a,c,u)\,b^\dagger b
+O(|b|^3).
$$

O efeito no matching escalar é quadrático:

$$
\boxed{
\delta r_A
=\partial_{q^A}\kappa_\mu\,b^\dagger b+O(|b|^3),
\qquad q^A=(a,c,u).
}
$$

O coeficiente vem da Hessiana oficial aumentada:

$$
\boxed{
\kappa_\mu
=\langle\mu,
K_{J}^{\rm phys}\mu\rangle,
}
$$

com

$$
K_J^{\rm phys}
=P^{{\rm phys}\dagger}
\left(D^2\mathcal S_{\rm GDQ}
-\sum_a\lambda_aD^2\mathcal C_a\right)
P^{\rm phys}.
$$

Sua parcela torsional contém

$$
-\frac{\hbar}{6\Lambda_C^2}
\int\tau\mathcal U|\mathscr D_J\mu|^2,
$$

além de $\langle H,D_J^2H[\mu,\mu]\rangle$, compensação métrica, medida,
curvatura e DtN. O sinal não pode ser inferido do primeiro termo isolado.

## 6. Consequência para o tripleto residual

O primeiro setor não homogêneo não acrescenta coluna à Jacobiana linear da
sela:

$$
\operatorname{rank}D\mathfrak F
$$

permanece inalterado em $b=0$. Ele só pode gerar uma ramificação com
$b\neq0$ se o coeficiente quadrático atravessar zero ou se existir uma sela
que quebre espontaneamente $G_B$. Isso é um problema de bifurcação da Hessiana,
não uma correção linear do matching.

## 7. Teste simbólico

`ponte_global_local_kodaira_harmonicos.py` constrói as representações de
$SU(2)$ e verifica que $j=1/2$ e $j=1$ não têm vetor invariante, enquanto
$b^\dagger b$ é invariante quadrático. O teste não é um espectro físico.

## 8. Veredito

Sob a simetria preservada pelo background Berger:

1. nenhum primeiro harmônico genuinamente não homogêneo acopla linearmente ao
   tripleto singlet;
2. os únicos singlets homogêneos já foram triados;
3. o primeiro efeito permitido é quadrático;
4. obter um novo ramo requer calcular a Hessiana e procurar bifurcação;
5. inserir uma amplitude não-singlet como parâmetro linear violaria a simetria
   do próprio background.


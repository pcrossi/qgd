# Q30 — Medida sobre selas tubulares e lei de área

## 1. Objetivo

Construir, a partir da ação GDQ, uma medida semiclassicamente controlada sobre
configurações tubulares e determinar se ela produz

$$
\langle\mathcal H(C)\rangle
\sim e^{-\sigma_{\rm eff}A_{\min}(C)}.
$$

$\mathcal H(C)$ denota a inserção de holonomia da conexão geométrica efetiva.
Ela é uma sonda do transporte interno, não um Wilson loop fundamental
postulado na ação.

## 2. Setores com e sem tubo

Para um contorno fechado $C$, defina:

1. $\mathfrak C_0$: configurações no setor do vácuo;
2. $\mathfrak C_C$: configurações com a circulação/holonomia exigida por $C$;
3. $q_C^*$: sela tubular Ricci--Bohm de menor parte real da ação em
   $\mathfrak C_C$.

A diferença de ação possui a decomposição extensiva

$$
\boxed{
\operatorname{Re}\mathcal S[q_C^*]
-\operatorname{Re}\mathcal S[q_0]
=\sigma_{\rm cl}A_{\min}(C)
+\mu_{\rm cl}P(C)+O(1),
}
$$

onde $P(C)$ é o perímetro. O coeficiente $\sigma_{\rm cl}>0$ é o custo por
área da superfície de mundo varrida pelo pescoço estabilizado.

## 3. Contorno complexo e thimble

A ação oficial possui contorno causal complexo $\gamma$. Uma medida positiva
global $e^{-\mathcal S}$ não pode ser presumida. No regime semiclassicamente
estável, deforme o ciclo funcional para a thimble de descida íngreme
$\mathcal J_C$ que passa por $q_C^*$.

Nessa thimble:

1. $\operatorname{Im}\mathcal S$ é constante;
2. $\operatorname{Re}\mathcal S$ cresce para longe da sela;
3. a Hessiana física não possui direções negativas após remover os modos
   coletivos.

Defina o funcional regularizado

$$
Z_C^{(N)}
=\int_{\mathcal J_C^{(N)}}
d\mu_N(q)\,
\exp\left[-\frac{\operatorname{Re}\mathcal S_N[q]}{\hbar}\right],
$$

onde $N$ é um corte espectral da Hessiana GDQ. A fase constante da thimble é
recolocada separadamente e cancela no módulo da razão setorial.

## 4. Observável de holonomia

A resposta normalizada é

$$
\boxed{
\langle\mathcal H(C)\rangle_N
=e^{i\Theta_C}
\frac{Z_C^{(N)}}{Z_0^{(N)}}.
}
$$

No limite de Laplace em torno das selas,

$$
-\hbar\log
\left|\langle\mathcal H(C)\rangle_N\right|
=\Delta S_{\rm cl}(C)
+\frac\hbar2
\log\frac{\det{}'\mathcal H_C^{(N)}}
{\det{}'\mathcal H_0^{(N)}}
+O(\hbar^2).
$$

## 5. Renormalização geométrica da tensão

Por localidade ao longo do bulk tubular e pelo gap transversal, o logaritmo do
determinante admite expansão extensiva:

$$
\frac\hbar2
\log\frac{\det{}'\mathcal H_C}
{\det{}'\mathcal H_0}
=\delta\sigma\,A_{\min}(C)
+\delta\mu\,P(C)+o(A).
$$

Defina

$$
\boxed{
\sigma_{\rm eff}
=\sigma_{\rm cl}+\delta\sigma+O(\hbar^2).
}
$$

O gap impede correlações transversais de alcance infinito, de modo que as
correções não locais entre regiões distantes são exponencialmente suprimidas.

## 6. Subaditividade e existência do limite

Se duas superfícies grandes são coladas ao longo de um bordo de comprimento
$L_\partial$, localidade fornece

$$
F(A_1+A_2)
\le F(A_1)+F(A_2)+cL_\partial,
$$

onde

$$
F(A):=-\hbar\log|Z_C/Z_0|.
$$

Para uma sequência de retângulos com razão de aspecto limitada, o termo de
colagem dividido pela área tende a zero. O argumento subaditivo garante a
existência de

$$
\boxed{
\sigma_{\rm eff}
=\lim_{A\to\infty}\frac{F(A)}{A}.
}
$$

## 7. Lei de área

Se $\sigma_{\rm eff}>0$, então

$$
\boxed{
|\langle\mathcal H(C)\rangle|
=\exp\left[
-\frac{\sigma_{\rm eff}}{\hbar}A_{\min}(C)
-\frac{\mu_{\rm eff}}{\hbar}P(C)
+o(A)
\right].
}
$$

Em particular,

$$
\boxed{
\lim_{A\to\infty}
-\frac{\hbar}{A}
\log|\langle\mathcal H(C)\rangle|
=\sigma_{\rm eff}>0.
}
$$

Para $C_{R,T}$ retangular,

$$
V(R)
=-\lim_{T\to\infty}
\frac\hbar T\log|\langle\mathcal H(C_{R,T})\rangle|
=\sigma_{\rm eff}R+O(1).
$$

## 8. O que foi provado condicionalmente

A lei de área segue da ação GDQ sob quatro hipóteses explícitas:

1. existência da thimble tubular $\mathcal J_C$;
2. sela Ricci--Bohm isolada com $\sigma_{\rm cl}>0$;
3. Hessiana física com gap transversal;
4. existência do limite espectral $N\to\infty$ preservando localidade e
   subaditividade.

As hipóteses 2 e 3 são o conteúdo estrutural já consolidado na Q30. As
hipóteses 1 e 4 ainda não foram demonstradas como construção funcional
infinito-dimensional.

O limite espectral do setor quadrático foi posteriormente construído em
`q30/limite_espectral_medida_gdq.md`: para $\tau>0$, a covariância
$e^{-\tau L}L^{-1}$ é de traço. A extensão interagente e a thimble global
continuam condicionadas a uma cota uniforme de coercividade.

## 9. Limite da tentativa

Não está construída uma medida quântica rigorosa completa em dimensão quatro.
O que foi construído é:

1. medida espectral finita em cada $N$;
2. expansão de sela na thimble;
3. critério subaditivo para o limite de área;
4. identificação exata dos dois elos funcionais ainda ausentes.

Logo, essa etapa fortalece a ponte com Yang--Mills, mas não resolve o problema
Clay.

## 10. Classificação

- medida em corte espectral finito: construção explícita;
- lei de área: teorema condicional por Laplace/subaditividade;
- limite $N\to\infty$: aberto;
- controle global das thimbles: aberto;
- equivalência com Yang--Mills axiomático em $\mathbb R^4$: não demonstrada.

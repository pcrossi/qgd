# Q30 — Obstrução à coercividade global: dados do contorno causal

## 1. Coeficientes causais

Na escrita radial preliminar, os termos com duas derivadas foram formalmente
associados a

$$
\boxed{
\mathfrak c_1
:=\operatorname{Re}\int_\gamma
\frac{d\tau}{(4\pi z_\tau)^4},
}
$$

e os termos restantes por

$$
\boxed{
\mathfrak c_0
:=\operatorname{Re}\int_\gamma
\frac{d\tau}{\tau(4\pi z_\tau)^4}.
}
$$

Essa fatoração só é válida se o restante do integrando puder ser separado do
contorno. A Q4/Q9 impõe, porém, o princípio de Laurent. Se $A(z_\tau)$ é o
coeficiente geométrico completo do termo de gradiente,

$$
A(z_\tau)=\sum_{m\in\mathbb Z}A_mz_\tau^m,
$$

então

$$
\oint_\gamma
\frac{A(z_\tau)}{(4\pi z_\tau)^4}\,dz_\tau
=\frac{2\pi i}{(4\pi)^4}A_3
$$

para orientação positiva e contorno envolvendo a origem. Em particular,

$$
\oint_\gamma z_\tau^{-4}dz_\tau=0.
$$

Logo, a rigidez física não é o momento ingênuo $\mathfrak c_1$, mas o resíduo
do coeficiente de Laurent completo:

$$
\boxed{
\mathfrak c_1^{\rm phys}
=\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}A_3
\right].
}
$$

Escrevendo o pullback da ação quadrática como

$$
F^{(2)}(z)=\frac{d\tau}{dz}\frac1\tau
\int e^{-\sigma}\sqrt g\,\mathcal Q^{(2)}d^8x,
$$

tem-se $A_3=[z^3]F^{(2)}(z)$ ou, no caso holomorfo,
$A_3=F^{(2)(3)}(0)/3!$. Esse coeficiente não é automaticamente o $a_6$ de
Seeley--DeWitt: isso exigiria provar que $F^{(2)}$ é um traço de calor do mesmo
operador. Para orientação positiva, a coercividade exige
$\operatorname{Im}A_3<0$. Um background congelado em $z$ fornece $A_3=0$.
Veja `q30/identificacao_A3_a6_tubo.md`.

## 2. Condição necessária

Para flutuações de frequência crescente e norma fixa,

$$
\operatorname{Re}S^{(2)}[\Phi_N]
\sim\mathfrak c_1^{\rm phys}\lambda_N\|\Phi_N\|^2,
\qquad \lambda_N\to\infty.
$$

Logo:

1. $\mathfrak c_1^{\rm phys}<0$: ação ilimitada inferiormente;
2. $\mathfrak c_1^{\rm phys}=0$: ausência de controle quadrático;
3. apenas $\mathfrak c_1^{\rm phys}>0$: coerção elíptica possível.

Portanto,

$$
\boxed{\mathfrak c_1^{\rm phys}>0\text{ é condição necessária}.}
$$

No bloco torsional, o coeficiente físico projetado $\mathfrak c_C$ também deve
ser positivo.

## 3. Normalização de $u$

Com métrica congelada e

$$
\int_\Sigma e^{-u}d\mu=1,
$$

uma desigualdade log-Sobolev no domínio compacto pode controlar a
concentração. Sem essa normalização, $e^{-u}(u-4)$ é ilimitado inferiormente
quando $u\to-\infty$.

## 4. Dados ausentes

O corpus não fornece para o tubo:

1. parametrização explícita de $\gamma$;
2. orientação;
3. ramo de $z_\tau^{-4}$;
4. terceiro jato causal $A_3$ da Hessiana tubular ponderada;
5. valores/sinais das rigidezes residuais físicas;
6. fases relativas das selas concorrentes.

Assim, não se pode decidir se $\operatorname{Re}S$ cresce nas direções de alta
frequência.

## 5. Stokes

Um salto de Stokes entre $q_i,q_j$ ocorre quando

$$
\operatorname{Im}S[q_i]=\operatorname{Im}S[q_j].
$$

Testá-lo exige os valores complexos das ações no mesmo contorno. Gap e
estabilidade local não determinam essas fases.

## 6. Teorema condicional

Se forem demonstrados

$$
\mathfrak c_1^{\rm phys}>0,
\quad\mathfrak c_C>0,
\quad\int e^{-u}=1,
$$

uma cota log-Sobolev uniforme e separação de fases

$$
|\operatorname{Im}S[q_i]-\operatorname{Im}S[q_*]|\ge\delta>0,
$$

então a medida interagente é normalizável, os cortes convergem, não há Stokes
nesse setor e a lei de área sobrevive ao limite funcional.

## 7. Veredito

$$
\boxed{
\text{coercividade global e ausência de Stokes não podem ser provadas
sem especificar }(\gamma,z_\tau)\text{ no tubo.}
}
$$

Escolher $A_3$ ou $\mathfrak c_1^{\rm phys}>0$ apenas para obter convergência alteraria
silenciosamente a teoria.

## 8. Entrada necessária

É necessária uma prescrição causal que determine

$$
\boxed{
(\mathfrak c_0^{\rm phys},\mathfrak c_1^{\rm phys},\mathfrak c_C^{\rm phys})
\quad\text{e}\quad
\operatorname{Im}S[q_i]-\operatorname{Im}S[q_*].
}
$$

Até isso ser derivado das Q3/Q4/Q9, o nível Clay permanece aberto.

## 9. Classificação

- necessidade de rigidez residual positiva: prova por altas frequências;
- normalização: necessária pelo modo constante;
- critério de Stokes: estrutural;
- valores causais: ausentes;
- construção Clay: aberta.

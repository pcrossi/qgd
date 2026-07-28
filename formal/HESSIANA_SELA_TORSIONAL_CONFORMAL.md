# Hessiana da sela torsional conformal

## 1. O que está sendo calculado

O background reduzido é:

$$
g_*(x)=e^{2a_*x^0}\delta,
$$

$$
\omega_*(x)=e^{2a_*x^0}\omega_0,
$$

$$
H_*=d_{J_0}^c\omega_*,
$$

com:

$$
u_*=\tau a_*^2,
\qquad
q=\frac{z_\tau}{\tau}>\frac85.
$$

O parâmetro $q$ é dado pelo contorno causal. Ele não é uma coordenada
dinâmica da Hessiana. A largura $\tau$ também é mantida fixa nesta variação.

O vínculo:

$$
\int_M\mathcal U\,dV_g=1
$$

determina:

$$
f_0(a)=f_{\rm base}+64\tau a^2.
$$

Assim, variar $a$ mantendo $f_0$ fixo sairia do espaço normalizado de
configurações.

## 2. Vetor tangente físico do setor conformal

Escreva:

$$
a(s)=a_*+s\alpha.
$$

Na origem $s=0$, o vetor tangente induz:

$$
\dot g
=
2x^0\alpha\,g_*,
$$

$$
\dot\omega
=
2x^0\alpha\,\omega_*,
$$

$$
\dot H
=
\left.
\frac{d}{ds}
d_{J_0}^c\omega(a(s))
\right|_{s=0},
$$

e:

$$
\dot f_0
=
128\tau a_*\alpha.
$$

Portanto, a direção $a$ já é uma combinação vinculada de perturbação
métrica, torsional e dilatônica. Ela não é uma variação de torção
independente acrescentada à ação.

## 3. Hessiana restrita exata

Defina:

$$
\mathcal F_q(u)
=
q e^{-28u}(672u-80)+128.
$$

Então:

$$
\frac{d\mathcal A_{\rm red}}{da}
=
2\tau a\,\mathcal F_q(\tau a^2).
$$

Derivando novamente:

$$
\frac{d^2\mathcal A_{\rm red}}{da^2}
=
2\tau\mathcal F_q(u)
+
4\tau u\,\mathcal F_q'(u).
$$

Como:

$$
\mathcal F_q'(u)
=
q e^{-28u}(2912-18816u),
$$

na sela não nula $\mathcal F_q(u_*)=0$:

$$
\boxed{
K_{aa}
=
\left.
\frac{d^2\mathcal A_{\rm red}}{da^2}
\right|_{a_*}
=
4\tau u_*q e^{-28u_*}
\left(2912-18816u_*\right)
>0.
}
$$

Essa é a rigidez da ação reduzida na direção vinculada $\alpha$. O módulo
Lean `GDQ.ConformalTorsionSaddle` prova a existência e unicidade de $u_*$, a
positividade de $\mathcal F_q'(u_*)$ e que $u_*$ é um mínimo local. O módulo
`GDQ.ConformalTorsionHessian` identifica:

$$
\frac{d^2\mathcal A_{\rm red}}{du^2}
=
\mathcal F_q'(u)
$$

e prova sua positividade no intervalo físico.

## 4. Por que isso ainda não é a Hessiana física completa

Uma perturbação geral admissível deve ser escrita, esquematicamente, como:

$$
\delta\Phi
=
(h,\mu,\eta,\sigma).
$$

Aqui:

- $h$ é a variação Hermitiana da métrica;
- $\mu\in\Omega^{0,1}(T^{1,0}M)$ é uma variação de
  Kodaira--Spencer da estrutura complexa;
- $\eta=\delta\operatorname{Re}f$;
- $\sigma=\delta\operatorname{Im}f$.

A torção não é um novo campo fundamental independente:

$$
\delta H
=
\delta\left(d_J^c\omega\right)
$$

é determinada por $(h,\mu)$.

Além disso, os vetores tangentes físicos devem satisfazer:

$$
\delta\int_M\mathcal U\,dV_g=0,
$$

as condições de bordo do estômato e o quociente pelas direções de
difeomorfismo. A fase constante é uma direção de Noether e também deve ser
separada antes de falar em gap.

## 5. Estrutura de blocos

Depois de impor vínculos e gauge, a Hessiana tem a forma:

$$
K_{\rm phys}
=
P_{\rm phys}
\begin{pmatrix}
K_{aa} & K_{aX}\\
K_{Xa} & K_{XX}
\end{pmatrix}
P_{\rm phys},
$$

onde $X$ reúne os modos restantes. A positividade de $K_{aa}$ é necessária,
mas não suficiente. Para um único modo real adicional, a forma quadrática é:

$$
Q(x,y)
=
K_{aa}x^2+2K_{aX}xy+K_{XX}y^2.
$$

Completando o quadrado:

$$
Q(x,y)
=
K_{aa}
\left(
x+\frac{K_{aX}}{K_{aa}}y
\right)^2
+
\left(
K_{XX}-\frac{K_{aX}^2}{K_{aa}}
\right)y^2.
$$

Logo, a condição que falta é:

$$
\boxed{
K_{XX}-\frac{K_{aX}^2}{K_{aa}}>0.
}
$$

Essa identidade e sua implicação de positividade foram formalizadas em Lean.
Nenhum valor foi atribuído artificialmente a $K_{aX}$ ou $K_{XX}$.

## 6. Projetor e cota explícita no setor reduzido

Depois que os vínculos e as direções de gauge já foram eliminados, considere
um setor real de dois modos $(x,y)$. Nesse espaço reduzido, o subespaço
admissível é o espaço inteiro e o subespaço de gauge é nulo. Portanto:

$$
P_{\rm phys}=I.
$$

O módulo Lean `GDQ.ConformalTorsionProjectedHessian` constrói esse projetor
pelo mesmo mecanismo ortogonal geral usado para:

$$
V_{\rm phys}=V_{\rm adm}\cap\mathcal G^\perp,
$$

e prova que ele age como a identidade nesse sistema de coordenadas já
reduzido.

Para:

$$
Q(x,y)
=
K_{aa}x^2+2K_{aX}xy+K_{XX}y^2,
$$

a desigualdade elementar fornece:

$$
2K_{aX}xy
\ge
-|K_{aX}|(x^2+y^2).
$$

Logo:

$$
Q(x,y)
\ge
\mu_{\rm dd}(x^2+y^2),
$$

onde:

$$
\mu_{\rm dd}
=
\min
\left\{
K_{aa}-|K_{aX}|,
K_{XX}-|K_{aX}|
\right\}.
$$

Assim, as condições suficientes:

$$
|K_{aX}|<K_{aa},
$$

$$
|K_{aX}|<K_{XX},
$$

implicam:

$$
\mu_{\rm dd}>0.
$$

Essa dominância diagonal é uma condição suficiente e mais forte que a
condição exata do complemento de Schur. Ela é útil porque fornece uma cota
quantitativa explícita para o gap.

O resultado formal não atribui valores a $K_{aX}$ ou $K_{XX}$. Portanto:

- $K_{aa}>0$ é uma conclusão derivada da ação reduzida;
- a coerção do sistema de dois modos é um teorema condicional;
- a estabilidade da Hessiana física 8D completa continua exigindo o cálculo
  dos blocos mistos e transversais no background concreto.

## 7. Por que $f_{\rm base}$ não fornece o modo $X$

Uma tentativa possível seria promover $f_{\rm base}$ a uma segunda
coordenada da Hessiana. A ação reduzida mostra imediatamente por que isso é
incorreto:

$$
\mathcal A_{\rm red}(u,f_{\rm base})
=
q e^{-28u}(2-24u)+f_{\rm base}-2+128u.
$$

Logo:

$$
\frac{\partial\mathcal A_{\rm red}}{\partial f_{\rm base}}
=1,
$$

$$
\frac{\partial^2\mathcal A_{\rm red}}
{\partial f_{\rm base}^2}
=0,
$$

$$
\frac{\partial^2\mathcal A_{\rm red}}
{\partial f_{\rm base}\partial u}
=0.
$$

Essa matriz Hessiana teria formalmente uma direção nula, mas o ponto não é
crítico nessa direção. Portanto ela não é a Hessiana de uma sela
bidimensional. O parâmetro $f_{\rm base}$ é fixado pelos dados globais:

$$
f_{\rm base}
=
\ln
\left[
\frac{(4\pi\tau)^2}{(4\pi z_\tau)^4}
\right],
$$

eventualmente acrescido do logaritmo do volume de Haar escolhido.

A constante que efetivamente acompanha a variação torsional é:

$$
f_0(a)
=
f_{\rm base}+64\tau a^2.
$$

Sua linearização é:

$$
\boxed{
\delta f_0
=
128\tau a\,\delta a.
}
$$

Portanto cada $\delta a$ determina exatamente uma componente dilatônica
admissível. A família conformal normalizada possui uma única coordenada
física livre. O módulo Lean
`GDQ.ConformalTorsionConstraintTangent` certifica a derivada unitária em
$f_{\rm base}$, os blocos nulos artificiais e a unicidade da componente
$\delta f_0$.

Consequentemente, $K_{aX}$ e $K_{XX}$ não podem ser extraídos escolhendo
$X=f_{\rm base}$. Eles exigem modos 8D independentes que não pertencem ao
ansatz conformal atual.

## 8. Próxima avaliação física

O próximo cálculo deve:

1. escolher uma base completa de perturbações Hermitianas e
   Kodaira--Spencer no domínio físico;
2. derivar $\delta H=\delta(d_J^c\omega)$ nessa base;
3. expandir a ação oficial até segunda ordem;
4. impor a linearização da normalização;
5. construir o projetor que remove difeomorfismos e o modo de fase
   constante;
6. avaliar os blocos $K_{aX}$ e $K_{XX}$;
7. testar a positividade do complemento de Schur e o gap.

Até essa avaliação, o resultado correto é:

> A ação oficial possui um background torsional não nulo, único em
> $u\in(0,5/42)$ para $q>8/5$, que é estável no setor conformal normalizado.
> A estabilidade 8D contra todos os modos permanece condicional à Hessiana
> física projetada.

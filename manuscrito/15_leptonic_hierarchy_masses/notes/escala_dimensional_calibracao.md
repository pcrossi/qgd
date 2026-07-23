---
title: "Escala dimensional e calibração"
---

# Escala dimensional e calibração

## 1. Enunciado

Esta nota fixa a resposta dimensional usada no capítulo. A GDQ calcula
autovalores, rigidezes e razões geométricas. A unidade física em MeV ou GeV
entra por calibração metrológica explícita.

Isso não é uma deficiência específica da GDQ. Nenhuma teoria física determina
o significado operacional de “MeV”, “metro” ou “segundo” sem uma convenção de
medida. O conteúdo preditivo está nas razões adimensionais.

## 2. Operador com dimensão física

Se um operador geométrico é escrito em coordenadas físicas:

$$
L\phi_n=\lambda_n\phi_n,
$$

então:

$$
[\lambda_n]=L^{-2}.
$$

A energia associada é:

$$
M_n c^2
=
\hbar c\sqrt{\lambda_n}.
$$

## 3. Operador normalizado

Na prática geométrica, o domínio interno costuma ser normalizado. Nesse caso:

$$
\widehat L\phi_n=\widehat\lambda_n\phi_n,
$$

com:

$$
[\widehat\lambda_n]=1.
$$

Para restaurar unidades, introduz-se um comprimento de calibração $\ell_0$:

$$
\lambda_n
=
\frac{\widehat\lambda_n}{\ell_0^2}.
$$

Então:

$$
M_n c^2
=
\frac{\hbar c}{\ell_0}
\sqrt{\widehat\lambda_n}.
$$

Definindo:

$$
E_0
:=
\frac{\hbar c}{\ell_0},
$$

temos:

$$
M_n c^2
=
E_0\sqrt{\widehat\lambda_n}.
$$

## 4. Razões são independentes da escala

Para dois modos do mesmo setor:

$$
\frac{M_i}{M_j}
=
\sqrt{
\frac{\widehat\lambda_i}{\widehat\lambda_j}
}.
$$

Esse é o objeto natural da teoria. O número $0{,}511\,\mathrm{MeV}$ depende
de como o laboratório define a unidade de energia. Portanto, o capítulo deve
falar de razões adimensionais.

## 5. Calibração eletrônica

Usar $M_e$ como padrão metrológico é aceitável quando a previsão é:

$$
\frac{M_\mu}{M_e},
\qquad
\frac{M_\tau}{M_e}.
$$

Se o elétron tem autovalor reduzido $\widehat\lambda_e$, então:

$$
M_e c^2
=
E_0\sqrt{\widehat\lambda_e}.
$$

Logo:

$$
E_0
=
\frac{M_ec^2}{\sqrt{\widehat\lambda_e}}.
$$

Substituindo:

$$
M_n
=
M_e
\sqrt{
\frac{\widehat\lambda_n}{\widehat\lambda_e}
}.
$$

Se a normalização do setor eletrônico escolhe:

$$
\widehat\lambda_e=1,
$$

então:

$$
E_0=M_ec^2.
$$

Essa escolha não deriva o MeV do nada. Ela fixa a régua. A previsão permanece
na razão:

$$
R_n
=
\sqrt{
\frac{\widehat\lambda_n}{\widehat\lambda_e}
}.
$$

## 6. Escala de Cartan e escalas setoriais

A ação oficial usa o parâmetro de corte de Cartan na forma normalizada. A
notação segura é:

$$
\ell_C=\frac{\hbar c}{E_C},
\qquad
k_C=\ell_C^{-1},
\qquad
E_C=\hbar c\,k_C.
$$

Não se deve confundir:

$$
\Lambda_C,
\qquad
\widehat\Lambda_\tau=\tau^{-1/2},
\qquad
m_i,
\qquad
E_0^{(s)}.
$$

Em coordenadas normalizadas, $\Lambda_C$ é número de corte da ação. A energia
física correspondente exige uma escolha metrológica de $\ell_C$ ou $E_C$.

Cada setor pode ter uma escala efetiva:

$$
E_0^{(s)}
=
\frac{\hbar c}{\ell_s}.
$$

Se cada $\ell_s$ for medido separadamente, a teoria perde poder preditivo
entre setores. O objetivo forte é derivar as razões entre essas escalas por
colagem, Hessiana e contorno.

## 7. Ponte por decaimento beta

Há também uma ponte metrológica independente no setor bariônico. O endpoint do
decaimento beta livre pode ser escrito como:

$$
Q_\beta
=
\left(
\delta_B-1
\right)
M_ec^2.
$$

Aqui $\delta_B$ é número geométrico adimensional. Na rota legada coerente:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

Logo:

$$
M_ec^2
=
\frac{Q_\beta}{\delta_B-1}.
$$

Essa equação não transforma $Q_\beta$ em axioma da massa do elétron. Ela
mostra que uma escala dimensional pode ser herdada de um contorno metrológico
físico quando a razão geométrica $\delta_B$ é derivada.

## 8. Critério de honestidade

Sempre que uma fórmula tiver a forma:

$$
M_n
=
M_e R_n^{\rm GDQ},
$$

o resultado preditivo é:

$$
R_n^{\rm GDQ}
=
\frac{M_n}{M_e}.
$$

Não se deve escrever “massa absoluta calculada ab initio” se uma escala medida
entrou na normalização. A forma correta é:

$$
\boxed{
\text{massa obtida como razão geométrica após calibração metrológica}
}
$$

## 9. Status

A escala dimensional está fechada em sentido metrológico:

$$
\boxed{
\text{a GDQ prevê razões; a unidade física é fixada por calibração}
}
$$

O fechamento forte ab initio exigiria derivar $E_C$, $\ell_C$ ou cada
$E_0^{(s)}$ diretamente da ação oficial, do background, da Hessiana e das
condições de contorno. Isso é programa posterior, não requisito para usar
razões adimensionais já derivadas.

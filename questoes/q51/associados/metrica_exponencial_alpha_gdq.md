# Auditoria Q51 — Métrica exponencial no decaimento alfa

## 1. Objeto auditado

O capítulo legado `pt-br/36 - Fenomenologia Nuclear - O Decaimento Alfa.md`
usa, no canal radial sob a barreira:

$$
g_{rr}(r)
=
\exp\left(
-\frac{\alpha^2 V(r)}{E_\alpha}
\right).
$$

Consequentemente:

$$
ds_{\rm rad}
=
\sqrt{g_{rr}(r)}\,dr.
$$

## 2. Status correto

Essa expressão ainda não deve ser classificada como teorema completo da GDQ.
Ela é uma redução efetiva plausível, compatível com a leitura de Q45, mas
precisa ser derivada da cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm núcleo+\alpha,*}
\to
P_{\rm phys}
\to
K_{\rm rad}^{\rm phys}
\to
\mathsf R_{\alpha{\rm -core}}
\to
g_{rr}^{\rm eff}(r).
$$

## 3. O que já é consistente

A forma exponencial é consistente com três fatos já usados na GDQ:

1. a densidade geométrica é exponencial em $f+\bar f$;
2. no setor evanescente reduzido da Q45, a métrica longitudinal acompanha a
   densidade do canal;
3. sob uma barreira de Coulomb, o modo radial alfa é evanescente entre o raio
   nuclear interno e o ponto de viragem externo.

Portanto, a estrutura:

$$
g_{rr}^{\rm eff}\sim e^{-\text{ação local adimensional}}
$$

tem boa motivação geométrica.

## 4. O que falta para fechar

Falta demonstrar que o expoente específico:

$$
\frac{\alpha^2 V(r)}{E_\alpha}
$$

é o resultado direto da Hessiana física projetada do sistema
núcleo-filho mais alfa, e não apenas uma escolha efetiva.

O fechamento exige:

1. background admissível do núcleo pesado;
2. modo alfa pré-formado como canal de superfície/torsão;
3. Hessiana radial física;
4. eliminação dos modos internos do núcleo por Schur/DtN;
5. leitura do símbolo radial efetivo;
6. extração do fator métrico $g_{rr}^{\rm eff}(r)$.

## 5. Veredito

$$
\boxed{
g_{rr}(r)=\exp\left(-\alpha^2 V/E_\alpha\right)
\text{ é hipótese reduzida útil, não ainda teorema fechado.}
}
$$


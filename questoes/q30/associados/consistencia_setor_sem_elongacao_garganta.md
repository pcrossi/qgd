# Q30 — Consistência do setor sem elongação na garganta torsional

## 1. Enunciado

Testar se o setor

$$
S=0,
\qquad K\ne0,
$$

é preservado pelas equações da garganta Ricci--Bismut, distinguindo:

1. consistência da truncagem: a equação normal a $S=0$ não possui fonte;
2. estabilidade completa: a Hessiana também é positiva nas direções $S$.

Essas propriedades não são equivalentes.

## 2. Torção conservada como forma de topo

No ciclo tridimensional homogêneo da garganta,

$$
H=h\,\operatorname{vol}_{\Sigma_3},
\qquad
h=\frac{Q_T}{V}.
$$

Em um frame ortonormal,

$$
H_{abc}=h\varepsilon_{abc}.
$$

Logo,

$$
H_{a cd}H_b{}^{cd}=2h^2g_{ab},
\qquad
H_{abc}H^{abc}=6h^2.
$$

Portanto, toda combinação métrica produzida pela variação de $|H|^2$ é
proporcional a $g_{ab}$. Sua parte sem traço anula-se:

$$
\boxed{
\left(H_{a cd}H_b{}^{cd}ight)^{\rm TF}=0.
}
$$

A carga torsional conservada pode sourcear o raio/volume, mas não sourceia um
squashing angular na primeira variação.

## 3. Curvatura e dilatão

No ponto redondo,

$$
\operatorname{Ric}_{ab}=\frac{2}{R^2}g_{ab},
$$

e portanto

$$
\operatorname{Ric}_{ab}^{\rm TF}=0.
$$

Se o background Ricci--Bohm preserva a simetria angular, com
$f=f(r,z)$ e sem gradiente tangencial em $\Sigma_3$, então

$$
\left(\nabla_af\nabla_b\bar f\right)^{\rm TF}=0,
\qquad
\left(\nabla_a\nabla_b\operatorname{Re}f\right)^{\rm TF}=0.
$$

O peso $e^{-\operatorname{Re}f}$ é escalar e não altera essas anulações
algébricas.

## 4. Equação normal ao vínculo

A equação de elongação angular é a projeção sem traço da equação métrica.
Nos backgrounds acima, cada fonte fundamental possui parte sem traço nula:

$$
\boxed{
\mathcal E_{ab}^{\rm TF}ig|_{S=0}=0.
}
$$

Consequentemente,

$$
\boxed{
S=0\text{ é uma truncagem consistente no setor homogêneo e angularmente
invariante da garganta.}
}
$$

Isso implementa precisamente a conexão indicada pelo teorema de conservação:
o puxamento volumétrico modifica $h=Q_T/V$, mas não gera espontaneamente uma
elongação anisotrópica.

## 5. Auditoria não abeliana complementar

Quando a torção de frame é descrita efetivamente por uma curvatura
$\mathcal F_C$ em um ciclo transversal orientado de dimensão quatro, sua
fonte sem traço é

$$
\mathsf T_{ij}^{\rm TF}
=\operatorname{tr}
\left(
\mathcal F_{ik}\mathcal F_j{}^k
-\frac14g_{ij}\mathcal F_{k\ell}\mathcal F^{k\ell}
\right).
$$

Para

$$
\mathcal F_C=\pm *_4\mathcal F_C,
$$

a identidade algébrica de formas auto-duais fornece

$$
\boxed{\mathsf T_{ij}^{\rm TF}=0.}
$$

A Q28 já mostrou que a variação anisotrópica da forma quadrática seleciona
precisamente a igualdade das magnitudes dos dois fluxos, isto é, o setor
auto-dual ou anti-auto-dual. Essa é uma auditoria efetiva compatível com o
resultado fundamental da forma de topo; não substitui $H$ por Yang--Mills.

## 6. Consistência não é estabilidade completa

A auditoria de Berger encontrou

$$
K_q^{V,Q}=-\frac{32\tau}{3R^2}<0.
$$

Não há contradição. No ponto $S=0$:

$$
\left.\frac{\delta\mathcal S}{\delta S}\right|_{S=0}=0
$$

prova consistência, enquanto

$$
\left.\frac{\delta^2\mathcal S}{\delta S^2}\right|_{S=0}<0
$$

mostra instabilidade se $S$ for admitido no espaço físico completo.

Portanto, a Q30 possui duas classificações possíveis:

1. no setor físico postulado “elongações não são graus de liberdade”, a
   truncagem é consistente e o modo negativo não pertence ao domínio;
2. na teoria métrica irrestrita da ação oficial, o modo existe e o background
   homogêneo é uma sela, não um mínimo.

## 7. Veredito

$$
\boxed{
\text{$S=0$ é dinamicamente consistente por isotropia e conservação,
mas sua exclusão do espaço físico continua sendo uma hipótese constitutiva.}
}
$$

Logo, a coercividade de Q30 está fechada condicionalmente no setor torsional
restrito, não provada para todas as variações métricas da ação oficial.

## 8. Classificação

- isotropia do tensor de $H$ top-form: identidade exata;
- anulação da equação sem traço: derivação no background homogêneo;
- auditoria auto-dual não abeliana: redução efetiva compatível;
- exclusão física de $S$: hipótese constitutiva do autor;
- coercividade métrica irrestrita: não demonstrada.


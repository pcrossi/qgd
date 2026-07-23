# Q30 — Auditoria do squashing a volume e carga torsional fixos

## 1. Pergunta

A conservação da carga torsional que estabiliza o raio também estabiliza uma
distorção anisotrópica de Berger?

Considere

$$
ds^2=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2),
$$

com $q=1$ no ciclo redondo. O volume é proporcional a $R^3q$.

## 2. Vínculo de volume e carga

Para testar um squashing puro, imponha

$$
R^3q=R_0^3,
\qquad
R(q)=R_0q^{-1/3}.
$$

Com $Q_T=\int_{S^3}H$ conservada, a norma torsional homogênea depende apenas
do volume total. Portanto, nessa trajetória,

$$
\boxed{\mathcal E_T(Q_T,V_0)=\text{constante}.}
$$

A conservação não produz Hessiana torsional no squashing isovolumétrico.

## 3. Curvatura vinculada

O escalar de Berger é

$$
\mathcal R_B(R,q)=\frac{2(4-q^2)}{R^2}.
$$

Substituindo o vínculo de volume,

$$
\mathcal R_B(q)=\frac{2(4-q^2)q^{2/3}}{R_0^2}.
$$

No ponto redondo,

$$
\left.\frac{d\mathcal R_B}{dq}\right|_{q=1}=0,
\qquad
\boxed{
\left.\frac{d^2\mathcal R_B}{dq^2}\right|_{q=1}
=-\frac{32}{3R_0^2}<0.}
$$

Os termos $3\log R+\log q$ também são constantes quando $R^3q$ é fixado.
Logo, a segunda variação do funcional homogêneo é

$$
\boxed{K_q^{V,Q}=-\frac{32\tau}{3R_0^2}<0.}
$$

Esse resultado é analítico e independe do valor de $Q_T$.

## 4. Compatibilidade com Q29

A Q29 já incorporava o vínculo de Noether
$R^3qT=\mathrm{constante}$ e encontrou um modo comum negativo após o
complemento radial. O cálculo presente é mais restritivo: mesmo congelando o
volume, conservar a carga não estabiliza o squashing.

## 5. Distinção física GDQ

Escreva

$$
\delta e=(S+K)e,
\qquad S^\dagger=S,
\qquad K^\dagger=-K.
$$

O squashing pertence a $S$: é elongação/cisalhamento métrico. A
torção/conexão unitária pertence a $K$: gira o frame preservando a métrica.
Conservar $Q_T$ vincula o módulo de $H$ à geometria, mas não transforma uma
elongação $S$ em rotação $K$.

Portanto:

$$
\boxed{S\text{ físico}\Longrightarrow
\text{o background homogêneo possui modo negativo},}
$$

enquanto

$$
\boxed{S=0\text{ consistente}\Longrightarrow
q\text{ não pertence ao domínio da Hessiana de Q30}.}
$$

## 6. Veredito

A conservação torsional fecha a resposta radial/volumétrica, mas não
estabiliza elongações anisotrópicas. Para manter o setor “torções permitidas,
elongações não”, é necessário demonstrar que $S=0$ é uma truncagem dinâmica
consistente no background Ricci--Bohm completo. O teste de Cartan mínimo
produziu a equação de balanço, mas falhou globalmente; a conservação de carga
sozinha não substitui essa prova.

## 7. Classificação

- vínculo $R^3q=R_0^3$: squashing isovolumétrico;
- Hessiana $K_q^{V,Q}<0$: derivação exata no setor homogêneo;
- exclusão de $q$ quando $S=0$: definição do domínio físico proposto;
- consistência dinâmica global de $S=0$: aberta no background completo.


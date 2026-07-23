# Q43 — derivação reduzida de \(H_1\) por mistura harmônica

## Classificação

Cálculo de regra de seleção e magnitude geométrica reduzida para a
mistura Hessiana \(H_1\). Não usa valores experimentais de \(g_e\) ou
\(g_\mu-2\).

## 1. Mecanismo

A fonte superior direta é nula para campo uniforme. A primeira correção
universal possível vem da Hessiana: o produto quadrático do modo líder
contém uma componente no primeiro harmônico superior.

$$
\cos^2\vartheta
=
\frac12\left(1+\cos2\vartheta\right).
$$

Removendo o modo constante já absorvido na normalização, sobra uma
componente proporcional a \(\cos2\vartheta\).

## 2. Overlaps normalizados

- `beta12 = <u2, u1^2 - mean> = 2.820947917738782e-01`
- `beta11 = <u1, u1^2 - mean> = -2.724897264069244e-17`
- `beta13 = <u3, u1^2 - mean> = -3.814856169696941e-17`

A seleção é específica: o quadrado do modo líder acopla ao modo 2, mas
não ao modo 1 nem ao modo 3 dentro da precisão numérica.

## 3. Bloco \(H_C=H_0+\\alpha H_1\)

Foi usado:

$$
(H_1)_{12}=(H_1)_{21}=\beta_{12}\sqrt{K_1K_2}.
$$

Esse é o termo de mistura permitido pela simetria. O sinal absoluto e
eventuais fatores de terceira variação dependem da Hessiana 8D completa;
aqui foi fixada a magnitude geométrica mínima.

| lépton | papel Q39 | M_l/M_e | K2 | H1_mix | eig_min | a obtido | arquivo |
|---|---|---:|---:|---:|---:|---:|---|
| e | torção primária | 1.000000000000000e+00 | 8.610225765836003e+02 | 2.428899844539588e+02 | 9.988372364602003e-01 | 1.161414653717859e-03 | `background_leptonico_h1mix_e_q43.npz` |
| mu | torção transversal/biespacial | 2.067685934706287e+02 | 1.780324271066477e+05 | 3.492624481279508e+03 | 9.988372364659019e-01 | 1.161414653717858e-03 | `background_leptonico_h1mix_mu_q43.npz` |
| tau | saturação tridimensional | 3.477446405098381e+03 | 2.994159863649186e+06 | 1.432319253188402e+04 | 9.988372364659279e-01 | 1.161414653717859e-03 | `background_leptonico_h1mix_tau_q43.npz` |

## 4. Veredito

A rota de mistura Hessiana existe: \(H_1\) não é proibido pela simetria
e sua primeira magnitude angular é determinada por \(\beta_{12}\).

Porém, no bloco mínimo com \(m_\\perp=(0,1,0)\), essa mistura sozinha
não altera \(a\) de modo metrológico, porque o canal superior ainda
não possui fonte própria e não há correção diagonal/normalização
derivada da terceira variação completa.

Conclusão: o próximo coeficiente universal não é uma nova fonte direta
e também não é fechado apenas pela mistura angular. Falta avaliar a
terceira/quarta variação da ação oficial no background 8D para obter
o fator tensorial que acompanha \(\beta_{12}\) e as correções
diagonais de \(H_1\).

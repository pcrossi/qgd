# Q43 — variações superiores da ação GDQ reduzida

## Classificação

Derivada local de uma truncagem Galerkin reduzida da ação oficial.
Não é previsão metrológica de `g-2`.

## 1. Ponto de expansão

Usou-se o mesmo ponto da auditoria Galerkin:

$$
x_*=(1,0,0,0,0),
$$

com coordenadas:

| índice | modo |
|---:|---|
| 0 | circulação/fase linear |
| 1 | harmônico líder sin(theta) |
| 2 | harmônico superior sin(2theta) |
| 3 | densidade Re(f) cos(theta) |
| 4 | métrica conformal cos(theta) |

## 2. Hessiana local

- passo de diferença central: `2.0e-03`

| autovalor | valor |
|---:|---:|
| 0 | -1.932949747140319e+02 |
| 1 | -4.769504872323265e+01 |
| 2 | 6.280031355700243e+00 |
| 3 | 2.510719663015614e+01 |
| 4 | 1.155477545652323e+03 |

A presença de autovalores negativos confirma o diagnóstico anterior:
esta truncagem simples não é a sela leptônica física.

## 3. Coeficientes cúbicos selecionados

Notação:

$$
T_{ijk}=\frac{\partial^3 S_{\rm red}}{\partial x_i\partial x_j\partial x_k}(x_*).
$$

| termo | índices | valor | leitura |
|---|---|---:|---|
| `T112` | `(1, 1, 2)` | -2.664535259100376e-06 | líder² → superior direto; aqui sai compatível com zero |
| `T113` | `(1, 1, 3)` | 8.881784197001252e-07 | acoplamento superior permitido/proibido pela truncagem |
| `T114` | `(1, 1, 4)` | -2.664535259100376e-06 | acoplamento superior permitido/proibido pela truncagem |
| `T122` | `(1, 2, 2)` | -2.664535259100376e-06 | acoplamento superior permitido/proibido pela truncagem |
| `T123` | `(1, 2, 3)` | -6.283174869281538e+00 | líder-superior mediado pela densidade; canal robusto |
| `T124` | `(1, 2, 4)` | -1.776356839400250e-06 | acoplamento superior permitido/proibido pela truncagem |
| `T011` | `(0, 1, 1)` | 4.440892098500626e-06 | acoplamento envolvendo circulação protegida |
| `T012` | `(0, 1, 2)` | 2.664535259100376e-06 | acoplamento envolvendo circulação protegida |

## 4. Coeficientes quárticos selecionados

Notação:

$$
Q_{ijkl}=\frac{\partial^4 S_{\rm red}}{\partial x_i\partial x_j\partial x_k\partial x_l}(x_*).
$$

| termo | índices | valor |
|---|---|---:|
| `Q1111` | `(1, 1, 1, 1)` | 4.662936703425657e-03 |
| `Q1122` | `(1, 1, 2, 2)` | 3.108624468950438e-03 |
| `Q1133` | `(1, 1, 3, 3)` | 4.714229007163340e+00 |
| `Q1144` | `(1, 1, 4, 4)` | 2.220446049250313e-03 |
| `Q0011` | `(0, 0, 1, 1)` | 2.220446049250313e-03 |
| `Q0022` | `(0, 0, 2, 2)` | 1.554312234475219e-03 |
| `Q0112` | `(0, 1, 1, 2)` | -4.440892098500626e-04 |

## 5. Comparação com a seleção harmônica

A seleção harmônica reduzida calculada anteriormente dá:

$$
\beta_{12}=\langle u_2,u_1^2-\langle u_1^2\rangle\rangle
=
\frac{1}{2\sqrt\pi}.
$$

Numericamente, `1/(2 sqrt(pi)) = 2.820947917738781e-01`.

Na ação reduzida testada, `T112` sai no nível de ruído numérico.
Assim, a seleção puramente harmônica `beta12` não se converte
automaticamente em fonte variacional direta líder² → superior.

O acoplamento cúbico robusto é `T123`, numericamente próximo de
`-2*pi`. A leitura correta é que o modo líder e o modo superior
se comunicam por intermédio da densidade `Re(f)`, não por uma
fonte direta universal em campo uniforme.

## 6. Consequência para Q43

Este cálculo não fornece ainda `mu_2` metrológico. O motivo é estrutural:

1. no ponto simétrico `x_*`, a resposta magnética linear usa apenas a
   Hessiana quadrática;
2. termos cúbicos/quárticos geram resposta não-linear em `B`, salvo se
   o background físico já tiver amplitudes internas estacionárias
   não nulas;
3. a truncagem testada possui modos negativos e, portanto, não pode ser
   usada como background leptônico final.

A rota correta para a previsão metrológica fica então precisa:

1. construir uma sela leptônica 8D estável `Phi_l`;
2. avaliar `T` e `Q` nessa sela, não no ponto simétrico instável;
3. contrair esses tensores com o mapa magnético de contorno
   `M[Phi;B]`;
4. montar `H_C(alpha)` físico e reexecutar o extrator.

Assim, a Q43 ganha uma conclusão adicional: a ação reduzida permite
um canal superior mediado pela densidade, mas não uma fonte direta
universal. A metrologia depende da sela 8D estável e da contração
tensorial completa. Não há justificativa para usar `mu_2_required`
como previsão.

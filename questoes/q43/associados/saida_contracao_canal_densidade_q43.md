# Q43 — contração do canal superior mediado pela densidade

## Classificação

Avaliação condicional de um canal derivado da ação reduzida. Não usa
valores experimentais de `g-2`.

## 1. Entrada

- `eta_density = 0.000000000000000e+00`
- `T123 = -6.283174869281538e+00`
- `alpha/(2*pi) = 1.161409732097664e-03`

O canal aplicado é:

$$
\Delta H_{12}
=
\eta_\ell T_{123}.
$$

Aqui \(\eta_\ell\) deve vir de uma sela admissível. A sela angular
reduzida normalizada foi calculada separadamente e fornece
\(\eta_\ell=0\). Um valor não nulo exigiria o background 8D
não homogêneo, warped ou misto.

## 2. Resultados

| bloco | papel Q39 | M_l/M_e | eig_min | a0 | a_eff | delta_a |
|---|---|---:|---:|---:|---:|---:|
| `background_leptonico_estavel_e_q43.npz` | torção primária | 1.000000000000000e+00 | 9.988372413989819e-01 | 1.161409732097665e-03 | 1.161409732097665e-03 | 0.000000000000000e+00 |
| `background_leptonico_estavel_mu_q43.npz` | torção transversal/biespacial | 2.067685934706287e+02 | 9.988372413989819e-01 | 1.161409732097665e-03 | 1.161409732097665e-03 | 0.000000000000000e+00 |
| `background_leptonico_estavel_tau_q43.npz` | saturação tridimensional | 3.477446405098381e+03 | 9.988372413989819e-01 | 1.161409732097665e-03 | 1.161409732097665e-03 | 0.000000000000000e+00 |

## 3. Leitura

Para o valor informado acima, a tabela mostra diretamente a resposta
do canal mediado pela densidade. A execução canônica usa
\(\eta_\ell=0\), valor da sela angular reduzida normalizada; nesse
caso, a contração não altera a resposta líder.

Logo, o próximo dado físico necessário para a metrologia não é
`mu2_required`; é \(\eta_\ell\) ou, mais geralmente, o perfil
estacionário completo de \(\operatorname{Re}f\) na sela leptônica
8D. Uma vez fornecido esse background, este mesmo operador calcula
a correção sem ajuste experimental.

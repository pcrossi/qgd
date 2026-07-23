# Q72 — Cálculo reduzido de $\mathsf R_{\rm app}(t)$, $\Gamma_{\rm det}$ e kernel de transporte

## 1. Objetivo

Este documento executa a etapa metrológica mínima da Q72 em um aparelho
específico:

$$
\mathsf R_{\rm app}(t),
\qquad
\Gamma_{\rm det},
\qquad
w(t_f,t).
$$

O caso-base é um interferômetro de Mach--Zehnder com chave eletro-óptica,
usado como realização física da escolha retardada.

## 2. Referências usadas como dados externos

O experimento de escolha retardada de Jacques et al. reporta uma realização com
fótons únicos em interferômetro de dois caminhos, onde a configuração aberta ou
fechada é escolhida depois que o fóton entrou no interferômetro, com separação
relativística entre entrada e escolha:

- Vincent Jacques, E. Wu, Frédéric Grosshans, François Treussart, Philippe
  Grangier, Alain Aspect, Jean-François Roch, “Experimental realization of
  Wheeler's delayed-choice gedanken experiment”, *Science* 315, 966--968
  (2007), DOI: `10.1126/science.1136303`.

Para congelar parâmetros materiais de chaveamento, usamos uma chave
Mach--Zehnder eletro-óptica de referência em $\lambda=1550\,\mathrm{nm}$ com
tensão push-pull de $2{,}445\,\mathrm V$, tempo de chaveamento de
$18{,}1\,\mathrm{ps}$ e crosstalk menor que $-30\,\mathrm{dB}$:

- Chuan-Tao Zheng et al., “Design and analysis of a polymer Mach-Zehnder
  interferometer electro-optic switch over a wide spectrum of 110 nm”,
  *Optical Engineering* 48(5), 054601 (2009), DOI: `10.1117/1.3129846`.

Esses dados não são axiomas da GDQ. Eles são dados externos do aparelho.

## 3. Definição da impedância temporal do aparelho

A escolha retardada é representada por uma impedância de interface dependente
do tempo físico:

$$
\mathsf R_{\rm app}(t)
=
\mathsf R_{\rm off}
+
s(t-t_c)
\left(
\mathsf R_{\rm on}-\mathsf R_{\rm off}
\right).
$$

Usamos uma comutação suave:

$$
s(t-t_c)
=
\frac{1}{1+\exp\left[-(t-t_c)/\tau_{\rm sw}\right]}.
$$

No estado coerente/recombinado:

$$
\mathsf R_{\rm off}=0.
$$

No estado de caminho distinguível, a coerência residual é estimada pelo
crosstalk de potência $p_{\rm leak}$. Se a amplitude coerente residual escala
como:

$$
\mathcal C_{\rm on}\simeq\sqrt{p_{\rm leak}},
$$

então:

$$
\Gamma_{\rm on}
=
-\ln\mathcal C_{\rm on}
=
-\ln\sqrt{p_{\rm leak}}.
$$

Pela definição reduzida:

$$
\Gamma_{\rm det}
=
\frac12
\langle
\Delta\Phi_\partial,
\mathsf R_{\rm app}\Delta\Phi_\partial
\rangle,
$$

e tomando a normalização mínima:

$$
\|\Delta\Phi_\partial\|^2=2,
$$

obtemos:

$$
\mathsf R_{\rm on}
=
\Gamma_{\rm on}.
$$

Para crosstalk de $-30\,\mathrm{dB}$:

$$
p_{\rm leak}=10^{-3},
\qquad
\Gamma_{\rm on}=3{,}45387763949.
$$

Portanto:

$$
\boxed{
\mathsf R_{\rm app}(t)
=
3{,}45387763949\,
\frac{1}{1+\exp[-(t-t_c)/18{,}1\,{\rm ps}]}.
}
$$

## 4. Kernel causal de transporte

O kernel reduzido deve ser causal, normalizado e concentrado após o retardo de
propagação entre a região de escolha e o registro:

$$
w(t_f,t)
=
\frac{1}{\tau_{\rm mem}}
\exp\left[
-\frac{t_f-t-t_{\rm prop}}{\tau_{\rm mem}}
\right]
\Theta(t_f-t-t_{\rm prop}).
$$

Após normalização:

$$
\int w(t_f,t)\,dt=1.
$$

Usamos:

$$
\tau_{\rm mem}=\tau_{\rm sw}=18{,}1\,{\rm ps}.
$$

Para um interferômetro compacto de caminho efetivo $L=1\,\mathrm m$ no ar:

$$
t_{\rm prop}=\frac{L}{c}=3{,}33564095198\,{\rm ns}.
$$

## 5. Resultado

A saída numérica está em:

- `questoes/q72/associados/saida_resposta_interferometro_q72.md`.

O limite tardio é:

$$
\Gamma_{\infty}=3{,}45387763949,
\qquad
\mathcal C_{\infty}=3{,}16227766017\times10^{-2}.
$$

Logo, para uma chave com crosstalk de $-30\,\mathrm{dB}$, o termo de
interferência residual fica em cerca de $3{,}16\%$ em amplitude coerente,
correspondente ao limite imposto pela imperfeição do aparelho.

## 6. Interpretação GDQ

O cálculo não altera a ação oficial. Ele calcula a resposta de um contorno
clássico específico:

$$
J_{\rm app}^{\rm clássico}
\to
\mathsf R_{\rm app}(t)
\to
\Gamma_{\rm det}
\to
\mathcal C_{\rm det}.
$$

A escolha retardada é, portanto, uma alteração temporal do contorno. O registro
final depende da impedância realizada pelo aparelho, transportada causalmente
até o detector por $w(t_f,t)$.

Não há sinal físico para o passado. Há solução efetiva de contorno dependente
do aparelho realmente implementado.

## 7. Status

$$
\boxed{
\text{Q72 fica metrologicamente exemplificada para um interferômetro EO-MZI reduzido.}
}
$$

O refinamento completo exigiria medir ou modelar a Hessiana material real do
dispositivo usado no laboratório, substituindo os dados de crosstalk e
chaveamento por blocos diretamente calculados de $K_{\rm app}$.


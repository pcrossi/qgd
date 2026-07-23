# Q76 — toy quase real de estabilidade de qubit GDQ

## 1. Objetivo

Construir uma estimativa semi-realista, mas ainda reduzida, para avaliar a
rota GDQ de estabilidade de qubits.

O objetivo não é prever um hardware específico. O objetivo é transformar a
intuição em uma planilha física clara:

$$
\text{erro total}
=
\text{vazamento}
+
\text{térmico}
+
\text{não adiabático}
+
\text{de fase}
+
\text{readout}.
$$

Na GDQ, cada termo deve ser interpretado como uma redução de:

$$
\Phi_\ast,
\qquad
K_{\rm phys},
\qquad
\mathsf R_{\rm app},
\qquad
\Delta_{\rm gap},
\qquad
J.
$$

## 2. Parâmetros do toy

Usamos os seguintes dados reduzidos:

| Símbolo | Significado |
|---|---|
| $f_{\rm gap}$ | frequência equivalente do gap lógico--complemento |
| $T$ | temperatura do aparelho |
| $J/\Delta$ | mistura residual entre qubit e complemento |
| $t_{\rm gate}$ | tempo de porta |
| $T_2$ | tempo de coerência efetivo |
| $p_{\rm read}$ | erro de leitura reduzido |
| $\delta\theta$ | erro angular de eixo/contorno |

O gap energético é:

$$
\Delta_{\rm gap}
=
hf_{\rm gap}.
$$

## 3. Estimadores

### 3.1 Vazamento Hessiano

O vazamento para modos não lógicos é estimado por:

$$
\epsilon_{\rm leak}
\simeq
\left(
\frac{\|J\|}{\Delta_{\rm gap}}
\right)^2.
$$

### 3.2 Excitação térmica

O fator térmico reduzido é:

$$
\epsilon_{\rm th}
\simeq
\exp
\left(
-
\frac{hf_{\rm gap}}{k_BT}
\right).
$$

Como:

$$
\frac{k_B}{h}
\simeq
20{,}836619\,{\rm GHz/K},
$$

temos:

$$
\frac{hf_{\rm gap}}{k_BT}
=
\frac{f_{\rm gap}/{\rm GHz}}{20{,}836619\,T/{\rm K}}.
$$

### 3.3 Erro não adiabático

Para uma porta de duração $t_{\rm gate}$, a escala adiabática simples é:

$$
\epsilon_{\rm nonad}
\simeq
\left(
\frac{1}{2\pi f_{\rm gap}t_{\rm gate}}
\right)^2.
$$

### 3.4 Erro angular de contorno

Um erro pequeno de eixo $\delta\theta$ produz infidelidade média:

$$
\epsilon_{\rm axis}
\simeq
\frac{\delta\theta^2}{6}.
$$

### 3.5 Decoerência durante a porta

Usamos a aproximação reduzida:

$$
\epsilon_\phi
\simeq
1-\exp
\left(
-
\frac{t_{\rm gate}}{T_2}
\right).
$$

### 3.6 Erro total

Para pequenas probabilidades independentes, usamos:

$$
\epsilon_{\rm total}
\simeq
\epsilon_{\rm leak}
+
\epsilon_{\rm th}
+
\epsilon_{\rm nonad}
+
\epsilon_{\rm axis}
+
\epsilon_\phi
+
p_{\rm read}.
$$

Esse é um estimador de engenharia, não teorema fundamental.

## 4. Interpretação GDQ

O toy mostra que a promessa concreta da GDQ não é “erro zero”. A promessa é:

$$
\boxed{
\text{se a geometria aumenta }\Delta_{\rm gap}\text{ e reduz }J,
\text{ o overhead de correção pode cair.}
}
$$

Para temperatura alta, a condição térmica é severa:

$$
f_{\rm gap}
\gg
20{,}836619\,T\,{\rm GHz}.
$$

Logo, operação em temperatura ambiente só seria plausível se o qubit GDQ real
possuísse um gap geométrico muito alto ou uma proteção topológica que suprima o
acoplamento térmico efetivo. Isso ainda precisa ser derivado de $K_{\rm phys}$
e de $\mathsf R_{\rm app}$.


# Método simbólico

Este diretório concentra as regras formais reaproveitáveis.

## Ordem simbólica

1. Definir $\Phi_*$.
2. Definir vínculos $C_a[\Phi]=0$.
3. Construir a ação aumentada:

$$
\mathcal S_{\rm aug}
=
\mathcal S_{\rm GDQ}
+\sum_a\lambda_aC_a.
$$

4. Calcular:

$$
\delta\mathcal S_{\rm aug},
\qquad
\delta^2\mathcal S_{\rm aug}.
$$

5. Construir:

$$
P_{\rm phys},
\qquad
K_{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}\mathcal S_{\rm aug}
P_{\rm phys}.
$$

6. Inserir fonte:

$$
J_{\rm app}.
$$

7. Resolver:

$$
\delta\Phi
=
K_{\rm phys}^{-1}J_{\rm app}.
$$

8. Extrair observável.

## Regra de classificação

Se $J_{\rm app}$ for dado externo de aparelho, isso deve ser declarado. Não é
alteração da ação oficial.

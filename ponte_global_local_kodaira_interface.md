# Ponte global--local — bordo Kodaira--Spencer derivado da ação oficial

## 1. Escopo

Este documento deriva a forma da condição elíptica e do momento de interface
para deformações integráveis de $J$. Não escolhe uma condição Robin e não
introduz fonte superficial.

Considere uma sela $X_*=(g_*,J_*,f_*)$ e uma deformação de Beltrami

$$
\mu\in\Omega^{0,1}(T^{1,0}M),
\qquad
\bar\partial\mu=0
$$

na ordem linear, com a condição de gauge analítica

$$
\bar\partial^*\mu=0.
$$

O gauge serve para obter um representante elíptico; não acrescenta campo à
ação.

## 2. Operador constitutivo

Como

$$
H=d_J^c\omega,
$$

defina a linearização

$$
\mathscr D_J\mu
=D_J(d_J^c\omega)\mu.
$$

Incluindo a variação métrica $h_\mu$ exigida pela compatibilidade hermitiana,
o vetor real de perturbação é

$$
\eta_\mu=(h_\mu,\mu,0).
$$

A forma bilinear oficial restrita a esse setor é

$$
q_J(\mu,\nu)
=D^2\mathcal S_{\rm GDQ}(X_*)
[\eta_\mu,\eta_\nu].
$$

Sua parcela principal torsional é

$$
q_{H,J}^{\rm prin}(\mu,\nu)
=-\frac{\hbar}{6\Lambda_C^2}
\int_\gamma\!\int_M
\tau\mathcal U_*
\langle\mathscr D_J\mu,\mathscr D_J\nu\rangle
dV\,\frac{d\tau}{\tau}.
$$

O sinal isolado não decide a estabilidade, pois os blocos métrico--$J$, a
medida, a curvatura e os vínculos pertencem à mesma Hessiana.

## 3. Identidade de Green e momento

Para cada lado $M_\pm$ da interface $Y$, a integração por partes define
intrinsecamente

$$
q_{J,\pm}(\mu,\nu)
=\langle K_{J,\pm}\mu,\nu\rangle_{M_\pm}
+\langle\Pi_{J,\pm}\mu,\nu|_Y\rangle_Y.
$$

Na parte principal,

$$
\boxed{
\Pi_{H,J,\pm}\mu
=-\frac{\hbar}{6\Lambda_C^2}
\int_\gamma
\tau\,
\sigma_\nu(\mathscr D_J)^*
(\mathcal U_*\mathscr D_J\mu)
\frac{d\tau}{\tau},
}
$$

onde $\sigma_\nu(\mathscr D_J)$ é o símbolo normal. Os termos de ordem inferior
e os blocos cruzados acrescentam contribuições calculáveis a $\Pi_J$, mas não
mudam sua origem variacional.

Essa fórmula é a impedância fundamental antes da eliminação do bulk.

## 4. Multiplicadores de carga e fluxo

Na folha vinculada,

$$
\mathscr L
=\mathcal S_{\rm GDQ}
-\lambda_Q\mathcal C_Q
-\lambda_F\mathcal C_F
-\sum_b\lambda_b\mathcal C_b.
$$

Portanto o momento correto é o momento **aumentado**

$$
\boxed{
\Pi_{J}^{\rm aug}
=\Pi_{J}^{S}
-\lambda_Q\Pi_J^{Q}
-\lambda_F\Pi_J^{F}
-\sum_b\lambda_b\Pi_J^b.
}
$$

Aqui $\Pi_J^Q$ e $\Pi_J^F$ são obtidos pelas identidades de Green de
$D^2\mathcal C_Q$ e $D^2\mathcal C_F$. Se carga e fluxo forem funcionais
puramente globais/topológicos no setor considerado, essas parcelas podem se
anular; isso deve ser avaliado, não presumido.

## 5. Condição elíptica de bordo

O complexo gauge-fixado possui operador principal de tipo Kodaira--Spencer

$$
\Box_{\bar\partial}
=\bar\partial^*\bar\partial
+\bar\partial\bar\partial^*.
$$

Na interface artificial entre dois bulks, não se impõe condição absoluta ou
relativa independente. O domínio colado é definido por

$$
\boxed{[\mu]_Y=0,}
$$

$$
\boxed{
\Pi_{J,-}^{\rm aug}\mu_-
+\Pi_{J,+}^{\rm aug}\mu_+=0.
}
$$

Os normais são exteriores em cada lado. Essas condições são complementares e
fazem cancelar a forma de Green total. Nos bordos físicos restantes, a
polarização deve ser a já selecionada pela variação global.

## 6. Há salto Robin?

Sem uma ação localizada $S_Y$ ou fonte externa, a primeira variação total não
contém termo independente em $Y$. Portanto o matching fundamental é
homogêneo nos momentos aumentados.

Se os momentos forem escritos sem os multiplicadores, obtém-se apenas a
reescrita

$$
\Pi_{J,-}^{S}+\Pi_{J,+}^{S}
=\lambda_Q(\Pi_{J,-}^{Q}+\Pi_{J,+}^{Q})
+\lambda_F(\Pi_{J,-}^{F}+\Pi_{J,+}^{F})+\cdots.
$$

Isso não é uma Robin externa: é a Hessiana dos vínculos existentes. Depois de
resolver o bulk com traço $\mu_Y$, os mapas DtN produzem

$$
\boxed{
(\Lambda_{J,-}^{\rm aug}+\Lambda_{J,+}^{\rm aug})\mu_Y=0.
}
$$

Essa expressão tem aparência de impedância/Robin, mas foi derivada e seu lado
direito continua zero.

## 7. Acoplamento ao tripleto residual

Se

$$
r=(r_a,r_c,r_u)
$$

é o residual de matching anterior, a nova coluna é o bloco cruzado da Hessiana
on shell:

$$
\boxed{
B_\mu
=D_{\mu_Y}r
=\left.
\frac{\partial^2\mathscr L_{\rm on}}
{\partial(a_Y,c_Y,u_Y)\,\partial\mu_Y}
\right|_{X_*}.
}
$$

Em termos da impedância total, $B_\mu$ é o bloco

$$
B_\mu
=P_{acu}\Lambda_{\rm glue}^{\rm aug}P_\mu.
$$

Para o modo toroidal constante já calculado,

$$
\mathscr D_J\mu_0=0,
\qquad
\Pi_J^{\rm aug}\mu_0=0,
\qquad
\boxed{B_{\mu_0}=0.}
$$

Para um modo interno não homogêneo, o valor de $B_\mu$ requer o background e o
autovetor do problema elíptico. A fórmula acima é implementável, mas nenhum
número ou posto adicional pode ser declarado antes dessa avaliação.

## 8. Critério de decisão

Um modo Beltrami ajuda a Porta B somente se:

1. satisfaz Maurer--Cartan e os contornos colados;
2. não pertence a $\operatorname{Ran}R_*$;
3. possui norma finita;
4. $B_\mu\neq0$;
5. a Hessiana física aumentada permanece auto-adjunta;
6. o novo modo não é um zero modular cosmológico.

O matching correto foi derivado como homogêneo. Não há salto material nem
coeficiente Robin livre.

## 9. Implementação

`ponte_global_local_kodaira_interface.py` implementa a montagem da Hessiana
aumentada, a soma orientada dos momentos, o complemento de Schur/DtN e a
extração do bloco $B_\mu$. O teste associado verifica simetria e recusa fonte
externa.


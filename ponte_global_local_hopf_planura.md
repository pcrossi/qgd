# Ponte global--local — planura exata do modo Hopf compatível

## 1. Pergunta anterior ao ajuste

Considere o ramo sem traço

$$
Q_\epsilon
=\operatorname{diag}(qe^\epsilon,qe^{-\epsilon}),
\qquad
\det Q_\epsilon=q^2.
$$

Ele foi construído pela conjugação diferenciável $F_\epsilon$ entre os
quocientes de Hopf. Para permanecer no domínio da ação oficial, não se pode
variar somente $J$. A família compatível é

$$
X_\epsilon
=(g_\epsilon,J_\epsilon,f_\epsilon)
=F_\epsilon^*(g_0,J_0,f_0).
$$

## 2. Naturalidade da ação

Sob pullback,

$$
\omega_\epsilon=F_\epsilon^*\omega_0,
$$

$$
H_\epsilon
=d_{J_\epsilon}^c\omega_\epsilon
=F_\epsilon^*(d_{J_0}^c\omega_0),
$$

e

$$
\mathcal R_B[g_\epsilon,J_\epsilon]
=F_\epsilon^*\mathcal R_B[g_0,J_0].
$$

A medida também é natural:

$$
\mathcal U_\epsilon dV_{g_\epsilon}
=F_\epsilon^*(\mathcal U_0dV_{g_0}),
$$

pois $f_\epsilon=F_\epsilon^*f_0$ e $z_\tau$ não é alterado pela
reparametrização espacial.

Logo toda a densidade oficial satisfaz

$$
\mathbf L_{\rm GDQ}[X_\epsilon]
=F_\epsilon^*\mathbf L_{\rm GDQ}[X_0].
$$

## 3. Domínio fundamental e identificação

No recobrimento, $F_\epsilon$ conjuga

$$
z\mapsto qz
$$

em

$$
z\mapsto Q_\epsilon z.
$$

Portanto ele envia um domínio fundamental no outro, incluindo suas faces
identificadas. A mudança de variáveis dá

$$
\boxed{
\mathcal S_{\rm GDQ}[X_\epsilon;D_\epsilon]
=\mathcal S_{\rm GDQ}[X_0;D_0].
}
$$

Se o quociente for representado por um colar cortado, os termos das duas faces
se cancelam pela identificação torcida. Não existe bordo físico adicional e,
sem ação localizada, não sobra termo Robin.

## 4. Dados globais

Para $\epsilon_1=-\epsilon_2$,

$$
\det Q_\epsilon=q^2
$$

exatamente. Assim o modo não altera o módulo comum do ciclo, o volume de
contração nem a normalização global associada ao determinante. Sob o pullback
completo, os funcionais geométricos de raio, carga e fluxo também mantêm seus
valores.

Se algum dado externo distinguir separadamente os dois autovalores de $Q$,
essa marcação quebrará a equivalência. Nenhum dado desse tipo pertence ao
problema atual.

## 5. Coeficientes efetivos

Escreva uma expansão estática

$$
\mathcal S_{\rm on}(\epsilon)
=\mathcal S_0
+\frac12\lambda_\mu|\epsilon|^2
+\frac14g_\mu|\epsilon|^4+\cdots.
$$

Como a igualdade da ação vale para toda a família,

$$
\boxed{
\lambda_\mu=0,
\qquad
g_\mu=0.
}
$$

Do mesmo modo, para os resíduos singlets,

$$
\boxed{
C_a=\partial_a\lambda_\mu=0,
\qquad
C_c=\partial_c\lambda_\mu=0,
\qquad
C_u=\partial_u\lambda_\mu=0.
}
$$

Na realidade, todas as derivadas estáticas ao longo dessa família compatível
se anulam.

## 6. Interpretação correta

O representante de Kodaira--Spencer é não trivial quando se fixa a estrutura
complexa e se classifica superfícies de Hopf por biholomorfismos. Contudo a
GDQ varia conjuntamente $(g,J,f)$ e é invariante por difeomorfismos. A família
conjugada completa é, portanto, uma direção nula da ação, a menos que uma
marcação global adicional torne os autovalores individuais observáveis.

Isso resolve a aparente tensão:

1. $\mu_{\rm Hopf}$ é não-gauge no problema puramente complexo marcado;
2. $(\mathcal L_Vg,\mathcal L_VJ,\mathcal L_Vf)$ é localmente uma direção de
   difeomorfismo da ação;
3. sem marcação anisotrópica externa, a ação integrada no quociente não a
   distingue globalmente;
4. o modo deve ser tratado como zero modular/direção redundante na Hessiana
   física atual.

## 7. O que não pode ser feito

Manter $g$ fixo enquanto se varia $J$ por $\mu_{\rm Hopf}$ viola em geral a
compatibilidade hermitiana. Escolher depois uma compensação métrica diferente
do pullback define outra família física, que teria de ser derivada por um novo
problema variacional. Ela não pode ser usada para fabricar $\lambda_\mu$.

Também não é lícito interpretar a norma positiva de $\mu$ como massa:

$$
\|\mu\|_{L^2}>0
$$

é uma norma cinemática, enquanto

$$
D^2\mathcal S[\Phi_H,\Phi_H]=0.
$$

## 8. Consequência para o Galerkin

O modo não deve ser acrescentado como amplitude estabilizadora. Se for mantido
para auditoria, deve aparecer entre os zeros a remover por $P^{\rm phys}$ ou
entre os módulos fixados pelos dados globais. Ele não alimenta o tripleto
residual em nenhuma ordem estática.

## 9. Teste

`ponte_global_local_hopf_planura.py` verifica $\det Q_\epsilon=q^2$ e codifica
os coeficientes nulos. O teste associado confirma a planura polinomial; a prova
física é a naturalidade exata acima, não o ajuste numérico.


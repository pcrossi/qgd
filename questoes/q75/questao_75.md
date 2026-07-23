# Questão 75 — Efeito Sagnac via GDQ

## 1. Enunciado

A Q75 pergunta como a GDQ descreve o efeito Sagnac.

O efeito Sagnac ocorre quando dois feixes percorrem um interferômetro em sentidos
opostos enquanto o aparelho está em rotação. Ao recombinar os feixes, aparece
um deslocamento temporal ou de fase proporcional à área encerrada e à velocidade
angular do aparelho.

## 2. Status curto

$$
\boxed{
\text{Q75 fechada estruturalmente como holonomia de relógio/contorno rotativo.}
}
$$

O que está fechado:

1. a fórmula temporal padrão;
2. a fórmula de fase para luz;
3. a fórmula de fase para matéria;
4. a interpretação GDQ como holonomia da conexão de simultaneidade;
5. a distinção com Aharonov--Bohm;
6. a classificação de refinamentos materiais como resposta de aparelho.

O que fica para aplicação metrológica:

1. fibra óptica real;
2. dispersão;
3. índice de refração dependente de frequência;
4. deformação mecânica do anel;
5. ruído térmico;
6. Hessiana material $\mathsf R_{\rm rot}$ do aparelho.

## 3. Fórmula temporal

Em um referencial rotativo com velocidade angular $\boldsymbol\Omega$, a
velocidade local do contorno é:

$$
\mathbf v_{\rm rot}
=
\boldsymbol\Omega\times\mathbf r.
$$

A diferença de tempo entre os dois sentidos é:

$$
\Delta t_{\rm Sag}
=
\frac{2}{c^2}
\oint_\gamma
(\boldsymbol\Omega\times\mathbf r)\cdot d\mathbf r.
$$

Pelo teorema de Stokes:

$$
\oint_\gamma
(\boldsymbol\Omega\times\mathbf r)\cdot d\mathbf r
=
2\boldsymbol\Omega\cdot\mathbf A.
$$

Logo:

$$
\boxed{
\Delta t_{\rm Sag}
=
\frac{4\boldsymbol\Omega\cdot\mathbf A}{c^2}.
}
$$

Aqui $\mathbf A$ é a área vetorial orientada do circuito.

## 4. Fase para luz

Para luz de frequência angular $\omega$:

$$
\Delta\varphi_\gamma
=
\omega\Delta t_{\rm Sag}.
$$

Como:

$$
\omega
=
\frac{2\pi c}{\lambda},
$$

obtemos:

$$
\boxed{
\Delta\varphi_{\rm Sag}^{\gamma}
=
\frac{8\pi}{\lambda c}
\boldsymbol\Omega\cdot\mathbf A.
}
$$

Essa é a expressão usual do Sagnac óptico no vácuo.

## 5. Fase para matéria

Para uma onda de matéria, a fase associada ao tempo próprio/ação reduzida é:

$$
\Delta\varphi_m
=
\frac{mc^2}{\hbar}
\Delta t_{\rm Sag}.
$$

Portanto:

$$
\boxed{
\Delta\varphi_{\rm Sag}^{m}
=
\frac{4m}{\hbar}
\boldsymbol\Omega\cdot\mathbf A.
}
$$

Essa expressão é a forma reduzida para interferometria de matéria em rotação.

## 6. Interpretação GDQ

Na GDQ, o Sagnac não é força local sobre o feixe. Ele é holonomia da conexão de
relógio/simultaneidade induzida pelo contorno rotativo do aparelho.

A forma efetiva de relógio pode ser escrita, no limite reduzido, como:

$$
\Theta_t
=
dt
-
\frac{1}{c^2}
(\boldsymbol\Omega\times\mathbf r)\cdot d\mathbf r.
$$

Ao integrar em circuito fechado:

$$
\oint_\gamma \Theta_t
=
-
\frac{1}{c^2}
\oint_\gamma
(\boldsymbol\Omega\times\mathbf r)\cdot d\mathbf r.
$$

A diferença entre os dois sentidos dobra o efeito:

$$
\Delta t
=
-2\oint_\gamma(\Theta_t-dt)
=
\frac{2}{c^2}
\oint_\gamma
(\boldsymbol\Omega\times\mathbf r)\cdot d\mathbf r.
$$

Portanto:

$$
\boxed{
\text{Sagnac = holonomia da 1-forma de simultaneidade.}
}
$$

## 7. Relação com Aharonov--Bohm

Aharonov--Bohm mede holonomia de calibre:

$$
\Delta\varphi_{\rm AB}
=
\frac{q}{\hbar c}
\oint A\cdot dx.
$$

Sagnac mede holonomia de relógio/rotação:

$$
\Delta t_{\rm Sag}
=
\frac{2}{c^2}
\oint
(\boldsymbol\Omega\times\mathbf r)\cdot d\mathbf r.
$$

Assim:

$$
\boxed{
\text{AB é holonomia de calibre; Sagnac é holonomia de simultaneidade.}
}
$$

Ambos são efeitos de contorno e colagem, mas pertencem a conexões diferentes.

## 8. Por que não é rotação global do background

A GDQ deve evitar confundir:

1. rotação global isométrica do background;
2. resposta localizada de um aparelho em rotação.

Uma rotação global de todo o universo/laboratório seria mudança de descrição.
O Sagnac ocorre porque o aparelho define um contorno físico rotativo enquanto a
folha de laboratório fornece uma simultaneidade comparativa.

Logo:

$$
\boxed{
\boldsymbol\Omega
\text{ é dado do aparelho/contorno, não novo termo da ação.}
}
$$

## 9. Aparelho real e impedância rotativa

Em um giroscópio real, o anel/fibra possui:

1. índice de refração;
2. dispersão;
3. elasticidade;
4. acoplamento térmico;
5. ruído de fase;
6. perdas.

Na GDQ, isso entra como resposta material:

$$
\mathsf R_{\rm rot}
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

A fase real pode ser escrita como:

$$
\Delta\varphi_{\rm real}
=
\Delta\varphi_{\rm Sag}
+
\delta\varphi_{\rm mat},
$$

com:

$$
\delta\varphi_{\rm mat}
\sim
\oint_\gamma
\delta\Theta_t^{\rm surf}.
$$

No aparelho ideal:

$$
\delta\varphi_{\rm mat}=0.
$$

## 10. Conclusão

A GDQ descreve o efeito Sagnac como uma holonomia de contorno rotativo:

$$
\boxed{
\Delta t_{\rm Sag}
=
\frac{4\boldsymbol\Omega\cdot\mathbf A}{c^2}.
}
$$

Para luz:

$$
\boxed{
\Delta\varphi_{\rm Sag}^{\gamma}
=
\frac{8\pi\boldsymbol\Omega\cdot\mathbf A}{\lambda c}.
}
$$

Para matéria:

$$
\boxed{
\Delta\varphi_{\rm Sag}^{m}
=
\frac{4m\boldsymbol\Omega\cdot\mathbf A}{\hbar}.
}
$$

Classificação final:

$$
\boxed{
\text{Q75 fechada estruturalmente; aparelhos reais ficam como metrologia de } \mathsf R_{\rm rot}.
}
$$


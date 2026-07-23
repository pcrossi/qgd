# Questão 45 — Efeito Hartman

## 1. Enunciado

A questão pergunta:

1. por que $g_{xx}\propto\rho$;
2. se essa relação resulta da ação;
3. qual definição de tempo de tunelamento é usada;
4. como a deformação de pulsos é tratada;
5. se a velocidade de frente permanece causal.

O capítulo legado associado é:

- `pt-br/12 -  O Tempo de Tunelamento Quântico (Efeito Hartman).md`.

Documento técnico associado:

- `questoes/q45/associados/derivacao_reduzida_hartman_gdq.md`.

## 2. Status curto

$$
\boxed{
\text{Q45 fechada estruturalmente no setor evanescente unidimensional reduzido.}
}
$$

O que está fechado:

1. a leitura GDQ do efeito Hartman como saturação de comprimento próprio;
2. a separação entre tempo de pico/grupo e velocidade de frente;
3. a causalidade local;
4. a classificação correta de $g_{xx}\propto\rho$ como solução reduzida,
   não axioma universal.

O que não está fechado metrologicamente:

1. comparação com experimento específico;
2. deformação completa de pacotes largos;
3. detector real;
4. contorno material da barreira.

Esses itens são dados de aplicação experimental. Eles foram movidos para
`ideias/possibilidades.md` como refinamento futuro e não reabrem a resolução
estrutural da questão.

## 3. Dados e domínio

O domínio efetivo é uma barreira unidimensional:

$$
\Omega_L=[0,L].
$$

No interior da barreira:

$$
V_0>E.
$$

O modo estacionário reduzido é evanescente:

$$
\psi(x)=\psi_0e^{-\kappa x},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

Assim:

$$
\rho(x)=\rho_0e^{-2\kappa x}.
$$

Na GDQ, $\rho$ é a densidade geométrica:

$$
\rho=e^{-(f+\bar f)/2}.
$$

## 4. Por que $g_{xx}\propto\rho$?

A relação não é uma identidade tensorial universal. Ela vale no setor:

$$
\begin{aligned}
&\text{barreira estacionária}
+\text{modo evanescente}
+\text{transversais congeladas}
+\text{canal longitudinal reduzido}.
\end{aligned}
$$

Nesse setor, a densidade decrescente define a impedância geométrica do canal.
Com normalização na interface $x=0$, a solução longitudinal admissível é:

$$
g_{xx}(x)=g_0\frac{\rho(x)}{\rho_0}.
$$

Como $\rho(x)=\rho_0e^{-2\kappa x}$:

$$
g_{xx}(x)=g_0e^{-2\kappa x}.
$$

Então:

$$
\sqrt{g_{xx}(x)}=\sqrt{g_0}e^{-\kappa x}.
$$

Fisicamente: onde a densidade evanescente cai, o canal próprio acessível ao
sóliton também se contrai. A coordenada $x$ continua podendo ser grande, mas o
comprimento próprio efetivo não cresce indefinidamente.

## 5. Essa relação resulta da ação?

Sim, condicionalmente.

Ela não deve ser derivada por uma ação auxiliar tipo Einstein--Hilbert, como
aparece no capítulo legado. A derivação correta deve ser lida como redução da
ação oficial:

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

No setor evanescente, impõem-se:

1. fase transportadora estacionária ou suprimida;
2. corrente real nula dentro da barreira;
3. modos transversais congelados;
4. normalização de entrada $\rho_0$;
5. calibre longitudinal de medida;
6. minimização da energia geométrica do canal reduzido.

Sob essas hipóteses:

$$
\delta\mathcal S_{\rm GDQ}=0
\quad
\Longrightarrow
\quad
g_{xx}=g_0\rho/\rho_0
$$

no domínio reduzido.

Classificação:

$$
\boxed{
g_{xx}\propto\rho
\text{ é teorema reduzido condicional, não postulado fundamental.}
}
$$

## 6. Distância própria

A distância própria no canal é:

$$
D_{\rm prop}(L)
=\int_0^L\sqrt{g_{xx}(x)}\,dx.
$$

Substituindo:

$$
D_{\rm prop}(L)
=\sqrt{g_0}\int_0^L e^{-\kappa x}\,dx.
$$

Logo:

$$
D_{\rm prop}(L)
=\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right).
$$

No limite opaco:

$$
\lim_{L\to\infty}D_{\rm prop}(L)
=\frac{\sqrt{g_0}}{\kappa}.
$$

Essa é a saturação geométrica que substitui a leitura paradoxal de velocidade
de coordenada infinita.

## 7. Qual tempo de tunelamento é usado?

Há duas leituras distintas.

Para comparação com a literatura de Hartman, usa-se o tempo de fase ou
Wigner--Smith:

$$
\tau_{\rm W}(E)=\hbar\frac{\partial}{\partial E}\arg T(E).
$$

Na interpretação GDQ, usa-se o tempo próprio efetivo do canal evanescente:

$$
\tau_{\rm GDQ}(L)
=\int_0^L\frac{ds}{v_{\rm prop}}.
$$

Com velocidade física local efetiva $v_0\le c$:

$$
\tau_{\rm GDQ}(L)
=\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

Portanto:

$$
\lim_{L\to\infty}\tau_{\rm GDQ}(L)
=\frac{\sqrt{g_0}}{v_0\kappa}.
$$

O tempo saturado não é tempo de frente. É tempo de pico/grupo ou tempo próprio
efetivo do canal reduzido.

## 8. Como a deformação de pulsos é tratada?

Um pacote transmitido é:

$$
\Psi_T(x,t)=\int T(E)A(E)e^{i(kx-\omega t)}\,dE.
$$

Se $A(E)$ é estreito e $T(E)$ é regular na banda, o pico obedece ao atraso de
grupo:

$$
\tau_{\rm W}=\hbar\partial_E\arg T(E).
$$

Se a barreira é opaca ou o pacote é largo, $T(E)$ filtra o espectro. O pico
transmitido pode ser remodelado. Nesse caso, o avanço do pico não mede
velocidade de sinal.

Na GDQ, a regra é:

$$
\text{deformação de pico}
\ne
\text{propagação de frente}.
$$

Pacotes largos exigem cálculo espectral completo do detector e da barreira.
Esse é refinamento experimental, não lacuna conceitual da Q45.

## 9. A velocidade de frente permanece causal?

Sim.

A velocidade de coordenada aparente:

$$
v_{\rm coord}(L)=\frac{L}{\tau_{\rm GDQ}(L)}
$$

pode crescer quando $L$ cresce, porque $\tau_{\rm GDQ}$ satura. Mas essa razão
não é velocidade local.

A velocidade local é:

$$
v_{\rm prop}=\frac{ds}{dt}\le c.
$$

A frente causal obedece:

$$
v_{\rm front}\le c.
$$

Logo:

$$
\boxed{
\text{Hartman em GDQ não viola causalidade; ele expressa contração do canal próprio.}
}
$$

## 10. Respostas diretas às perguntas obrigatórias

1. $g_{xx}\propto\rho$ porque, no setor evanescente reduzido, a densidade
   geométrica fixa a impedância longitudinal do canal sob normalização de
   interface.
2. A relação resulta da ação oficial apenas após redução unidimensional,
   congelamento transversal, contorno evanescente e calibre de medida. Não é
   lei universal.
3. O tempo comparável à literatura é Wigner--Smith; a interpretação GDQ usa o
   tempo próprio efetivo do canal.
4. Pulsos deformados são tratados por transmissão espectral $T(E)A(E)$; o pico
   pode sofrer reshaping e não define frente causal.
5. A velocidade de frente permanece causal porque a reconstrução física local
   mantém $v_{\rm front}\le c$.

## 11. Veredito

$$
\boxed{
\text{Q45 fechada estruturalmente.}
}
$$

A questão não fornece ainda uma previsão metrológica universal para qualquer
barreira, porque isso depende do contorno material e do detector. Mas o
paradoxo conceitual de Hartman fica resolvido dentro da GDQ reduzida:

$$
\text{tempo saturado}
=
\text{comprimento próprio saturado}/v_{\rm prop},
$$

não velocidade superluminal.

A comparação com barreiras e detectores reais fica registrada em
`ideias/possibilidades.md` como programa metrológico futuro.

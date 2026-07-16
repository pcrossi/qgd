# Ponte global--local — raio cosmológico e obstrução energética

> **Documento histórico parcialmente superado.** O pullback causal reduzido
> foi posteriormente construído em `ponte_global_local_exterior_causal.md`.
> O estado numérico vigente está em
> `ponte_global_local_solver_final_resultado.md`.

## 1. Enunciado

O sistema de tiro com dois colares possuía dez parâmetros, mas sua Jacobiana
tinha posto oito porque, no setor estacionário,

$$
v=\text{constante},
\qquad
p_v=0.
$$

Era necessário substituir as duas linhas identicamente nulas pelos vínculos
cosmológicos de raio e energia:

$$
\mathcal C_R=0,
\qquad
\mathcal C_E=0.
$$

## 2. Raio da órbita Berger

No exterior completo,

$$
g_{S^3}
=a^2(\sigma_1^2+\sigma_2^2)+c^2\sigma_3^2.
$$

Com a normalização usada na redução,

$$
\operatorname{Vol}(S^3_{a,c})=2\pi^2a^2c.
$$

Logo o raio volumétrico é

$$
\mathcal R_3=(a^2c)^{1/3},
$$

e, em variáveis logarítmicas $y=\log a$ e $z=\log c$,

$$
\boxed{
\mathcal C_R
=\frac{2y+z}{3}-\log R_{\rm cos}=0.
}
$$

Sua variação reduzida é

$$
D\mathcal C_R
=\frac23Dy+\frac13Dz.
$$

O vínculo foi avaliado na seção cosmológica distinguida, isto é, no extremo
direito do exterior. Essa escolha pertence ao dado de contorno global; não é
uma média radial ajustada depois do cálculo.

## 3. Teste de posto

O script `ponte_global_local_teste_raio_jacobiana.py` inseriu essa linha na
Jacobiana variacional transportada. No fixture histórico, os valores
singulares foram

$$
\begin{aligned}
(&7{,}9078\times10^3,
1{,}2415\times10^3,
4{,}0583\times10^2,
7{,}6952,
4{,}0491,
7{,}4001\times10^{-1},\\
&3{,}5923\times10^{-3},
2{,}5153\times10^{-3},
5{,}2179\times10^{-4},
0).
\end{aligned}
$$

Portanto,

$$
\boxed{
\operatorname{rank}D\mathfrak F=9.
}
$$

Esse é um teste de consistência do sistema reduzido, não uma solução da sela.
O valor provisório $R_{\rm cos}=1$ foi apenas a unidade geométrica usada para
avaliar o posto; ele não foi otimizado nem comparado com observações.

## 4. Por que a energia ainda não pode ser avaliada

O vínculo correto já está definido covariantemente:

$$
\mathcal C_E[X]=\mathcal H_\xi[X]-E_H,
$$

com

$$
\delta\mathcal H_\xi
=\int_{\partial\Sigma}
\left(
\delta\mathbf Q_\xi
-\iota_\xi\boldsymbol\Theta_{\rm GDQ}
\right).
$$

Entretanto, o ansatz radial Berger usa a coordenada espacial de
cohomogeneidade um $s$. Ela não é o parâmetro de fluxo $\tau$ e tampouco o
tempo físico reconstruído $t$. O material canônico da Q38 fornece $R_H$ e
$E_H$ como dados de contorno, mas não fornece:

1. a imersão da folha lorentziana física no exterior Berger;
2. o campo vetorial $\xi$ nessa imersão;
3. o pullback de $\mathbf Q_\xi$ para a seção cosmológica;
4. a constante aditiva de referência de $\mathcal H_\xi$.

Sem esses dados, identificar o Hamiltoniano radial ou a restrição do lapse
com $E_H$ confundiria translação em $s$ com translação no tempo físico. Essa
identificação é proibida pelas convenções vigentes da GDQ.

## 5. Dado mínimo que fecha a última linha

É suficiente construir uma aplicação causal

$$
\iota_t:N^4\longrightarrow M^8
$$

compatível com a reconstrução vigente e definir

$$
\xi=\iota_{t*}(\partial_t)
$$

na fronteira cosmológica. Então deve-se:

1. avaliar $\delta\mathcal H_\xi$ com o potencial simplético já derivado;
2. verificar a integrabilidade na polarização DtN/Robin;
3. integrar no espaço de soluções a partir de um background de referência;
4. substituir a linha $p_v=0$ por $\mathcal H_\xi-E_H=0$;
5. recalcular o posto e somente depois procurar a sela.

## 6. Veredito

$$
\boxed{
\mathcal C_R\text{ está implementado e recupera um grau de posto;}
\quad
\mathcal C_E\text{ permanece aberto por falta do pullback causal explícito.}
}
$$

Não há justificativa para continuar a otimização da sela antes dessa
construção: o sistema atual tem uma nulidade física conhecida e, portanto,
não pode determinar isoladamente os dez parâmetros.

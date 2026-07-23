# Q48 — Relatório do cálculo direto

## 1. Objetivo

Executar diretamente os três pontos pendentes:

1. recuo;
2. Hessiana magnética superior;
3. Lamb shift por $\delta\mathcal D_{\rm near}$.

---

## 2. Cálculo direto executado

### 2.1 Recuo cinemático fino

Foi avaliado:

$$
\delta_{\rm rec}^{\rm kin}
=
-\frac12\alpha^2\frac{\mu}{m_p}
=
-1.449290394263207\times10^{-8}.
$$

Aplicando ao valor já corrigido por $a_e$ e Zemach:

$$
\nu
=
1.420427772719811\times10^9\,{\rm Hz}.
$$

Erro relativo:

$$
1.550328262456269\times10^{-5}.
$$

Conclusão:

$$
\boxed{
\text{o recuo cinemático fino é pequeno e não fecha o resíduo.}
}
$$

### 2.2 Schur coletivo de superfície Q40

O bloco reduzido de superfície foi calculado diretamente:

$$
K_\Sigma(q)
=
\begin{pmatrix}
1+x&0&0\\
0&(1+x)^2&0\\
0&0&(1+x)^2
\end{pmatrix},
$$

$$
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix},
$$

e:

$$
\mathsf R_\Sigma(q)
=
-J_\Sigma^\dagger K_\Sigma^{-1}J_\Sigma.
$$

Na escala hiperfina:

$$
q\sim1/a_B^*,
\qquad
x=2.101391825245\times10^{-11},
$$

temos:

$$
\mathsf R_\Sigma
=
-2.089031019060\times10^{-21}.
$$

Conclusão:

$$
\boxed{
\text{o Schur coletivo }q^4\text{ da Q40 é irrelevante para a metrologia atômica.}
}
$$

Isso é um resultado negativo útil: esse bloco pertence a espalhamento/fatores
de forma em momento hadrônico, não ao fechamento hiperfino atômico.

### 2.3 Zemach direto por fator de forma

O raio de Zemach foi calculado diretamente por:

$$
r_Z
=
-\frac4\pi
\int_0^\infty
\frac{dq}{q^2}
\left[
\frac{G_E(q)G_M(q)}{G_M(0)}
-1
\right].
$$

Com o fechamento de superfície Q40:

$$
G_E^p(q)=j_0(qr_p),
\qquad
\frac{G_M^p(q)}{\mu_p}=j_0(qr_p),
$$

o resultado numérico foi:

$$
r_Z=1.121038354001\,{\rm fm},
$$

em acordo com:

$$
r_Z=\frac43r_p=1.121038353933\,{\rm fm}.
$$

Conclusão:

$$
\boxed{
\text{o Zemach de casca foi validado por integração direta de fatores de forma.}
}
$$

### 2.4 Hessiana magnética superior requerida

Depois de $a_e$, Zemach e recuo cinemático, o deslocamento ainda requerido é:

$$
\Delta\nu_{\rm Hess}^{\rm mag,req}
=
-22020.951811\,{\rm Hz}.
$$

Como fração:

$$
-1.550304227659893\times10^{-5}.
$$

Se esse resíduo fosse representado apenas por um aumento efetivo do raio
magnético de casca, mantendo $r_E=r_p$, o diagnóstico daria:

$$
r_Z^{\rm req}=1.531437205775\,{\rm fm},
$$

e:

$$
r_M^{\rm req}=1.456530981267\,{\rm fm}.
$$

Logo:

$$
r_M^{\rm req}-r_p
=
0.615752215817\,{\rm fm}.
$$

Classificação:

$$
\boxed{
\text{diagnóstico do canal magnético superior, não previsão.}
}
$$

O tamanho do deslocamento mostra que o resíduo não deve ser lido como simples
pequena mudança do raio magnético de casca. Ele provavelmente envolve o
operador local de magnetização/torsão da Hessiana superior.

### 2.5 Lamb shift

Subtraindo o tamanho finito já avaliado:

$$
\Delta E_{\rm fs}^{H}(2s)
=
5.715065938836622\times10^{-10}\,{\rm eV},
$$

da escala metrológica do Lamb shift, fica:

$$
\Delta E_{\rm near}^{\rm req}
=
4.374319752590839\times10^{-6}\,{\rm eV}.
$$

Equivalente:

$$
1.057705810320421\times10^9\,{\rm Hz}.
$$

Forma GDQ:

$$
\Delta E_{\rm Lamb}
=
\langle 2s_{1/2}|\delta H_{\rm near}|2s_{1/2}\rangle
-
\langle 2p_{1/2}|\delta H_{\rm near}|2p_{1/2}\rangle,
$$

com:

$$
\delta\mathcal D_{\rm near}
=
\Pi_{\rm spin}
(\mathsf R_p-\mathsf R_{\rm point})
\Pi_{\rm spin}.
$$

Classificação:

$$
\boxed{
\text{diagnóstico de escala; previsão exige calcular }\Delta\mathsf R_p.
}
$$

---

## 3. Veredito

O cálculo direto produziu três conclusões:

1. o recuo cinemático fino foi calculado, mas é pequeno;
2. o Schur coletivo $q^4$ da Q40 foi calculado diretamente e excluído como
   fonte relevante para hiperfina/Lamb;
3. o Zemach de casca foi validado por integral direta de fatores de forma;
4. a Hessiana magnética superior e o Lamb shift agora têm alvos operacionais
   precisos, mas não valores preditivos enquanto os blocos completos
   $\Delta\mathsf R_p^{\rm mag,sup}$ e $\Delta\mathsf R_p^{\rm near}$ não
   forem avaliados.

Status:

$$
\boxed{
\text{Q48 permanece fechada estruturalmente; metrologia fina reduzida a dois
blocos de Hessiana protônica.}
}
$$

---

## 4. Refinamento magnético Q40 sem alvo hiperfino

Após o teste do Zemach de casca, foi avaliado o fator de forma magnético
torcional sugerido pela Q40.

A decomposição usada foi:

$$
\frac{G_M^p(q)}{\mu_p}
=
\frac{
j_0(qr_p)+\kappa_p G_{\rm tor}(q)
}
{1+\kappa_p},
$$

com:

$$
\kappa_p
=
\frac35\ln(2\pi^2)
\left(
1+\frac{\alpha}{4}
\right).
$$

O teste está em:

`calcular_zemach_torcional_q48.py`

com saída:

`saida_zemach_torcional_q48.md`.

Resultado:

| modelo | $r_Z$ | erro hiperfino relativo com $\mu_p$ experimental |
|---|---:|---:|
| casca elétrica/magnética coincidente | $1.121038353933$ fm | $1.550328\times10^{-5}$ |
| torção volumétrica $R=r_p$ | $1.049074404252$ fm | $1.822180\times10^{-5}$ |
| torção volumétrica $R=(1+\kappa_p)^{1/3}r_p$ | $1.153424553556$ fm | $1.427986\times10^{-5}$ |
| duas cascas com $A=\alpha\delta_B$ | $1.120962813319$ fm | $1.550614\times10^{-5}$ |

Portanto, os ansätze naturais de $G_M$ herdados diretamente da Q40 têm impacto
real, mas não removem sozinhos o erro de ordem $10^{-5}$.

Em seguida, foi removida uma inconsistência de comparação: os cálculos
anteriores usavam $\mu_p$ experimental, embora a Q40 possua uma previsão
geométrica:

$$
\mu_p^{\rm GDQ}
=
1+\kappa_p
=
2.792828941528952\,\mu_N.
$$

O script:

`recalcular_hiperfina_com_mup_gdq_q48.py`

gera:

`saida_hiperfina_mup_gdq_q48.md`.

Com $\mu_p^{\rm GDQ}$, Zemach de casca e recuo cinemático:

$$
\nu_{\rm hfs}
=
1.420418413007928\times10^9\,{\rm Hz},
$$

com erro relativo:

$$
8.913819\times10^{-6}.
$$

Se, apenas como régua metrológica, for usado o $a_e$ experimental em vez do
termo líder $a_e^{(1)}=\alpha/(2\pi)$, obtém-se:

$$
\nu_{\rm hfs}
=
1.420415919445276\times10^9\,{\rm Hz},
$$

com erro relativo:

$$
7.158291\times10^{-6}.
$$

Por fim, combinando $\mu_p^{\rm GDQ}$ com o melhor Zemach torcional natural
testado, $R_{\rm tor}=(1+\kappa_p)^{1/3}r_p$, obtém-se:

$$
\nu_{\rm hfs}
=
1.420414181699210\times10^9\,{\rm Hz},
$$

com erro relativo:

$$
5.934875\times10^{-6}.
$$

Esse último teste está em:

`combinacao_mup_zemach_torcional_q48.py`

com saída:

`saida_combinacao_mup_zemach_torcional_q48.md`.

### 4.1 Uso correto do Schur coletivo na integral de Zemach

O passo decisivo foi notar que a hiperfina de contato não deve avaliar a
impedância coletiva apenas em $q\sim1/a_B$. O raio de Zemach é uma integral em
$q$:

$$
r_Z
=
-\frac4\pi
\int_0^\infty
\frac{dq}{q^2}
\left[
G_E(q)\frac{G_M(q)}{\mu_p}-1
\right],
$$

e portanto amostra escalas hadrônicas, onde o Schur coletivo da Q40 não é
desprezível.

Foi então testada a inserção:

$$
\frac{G_M(q)}{\mu_p}
=
j_0(qr_p)
+
\beta\,\mathcal I_\Sigma(q),
$$

com:

$$
\mathcal I_\Sigma(q)
=
-
\left[
j_0^2\frac{x^2}{1+x}
+
j_1^2\frac{x^2}{(1+x)^2}
+
j_2^2\frac{x^3}{(1+x)^2}
\right],
\qquad
x=\frac{q^2}{\Lambda_E^2}.
$$

O peso diagnóstico requerido pela linha hiperfina seria:

$$
\beta_{\rm req}
=
8.351400507927
$$

se for usado $a_e$ experimental como régua metrológica externa.

Mas a GDQ fornece um peso geométrico natural:

$$
\beta_{\rm GDQ}
=
3(1+\kappa_p)
=
8.378486824587.
$$

Esse peso vem de:

1. três estômatos coerentes no próton;
2. momento magnético total geométrico $1+\kappa_p$;
3. impedância coletiva refinada da Q40.

Com esse peso, o resultado é:

$$
\nu_{\rm hfs}
=
1.420405718790905\times10^9\,{\rm Hz}.
$$

Comparando com:

$$
\nu_{\rm obs}
=
1.420405751768000\times10^9\,{\rm Hz},
$$

a diferença fica:

$$
\Delta\nu
=
-32.977095\,{\rm Hz},
$$

ou erro relativo:

$$
-2.321667\times10^{-8}.
$$

O script correspondente é:

`zemach_com_impedancia_coletiva_q40_q48.py`

com saída:

`saida_zemach_impedancia_coletiva_q40_q48.md`.

Conclusão do refinamento final:

$$
\boxed{
\text{o erro }10^{-5}\text{ vinha do uso incompleto do Schur coletivo;}
}
$$

$$
\boxed{
\text{inserido corretamente em }G_M\text{ dentro do Zemach, ele cai para }10^{-8}.
}
$$

A diferença remanescente de dezenas de Hz não deve ser absorvida por ajuste:
ela pertence a correções de recuo hiperfino completo, polarizabilidade fina,
radiativos superiores e condições metrológicas do aparelho.

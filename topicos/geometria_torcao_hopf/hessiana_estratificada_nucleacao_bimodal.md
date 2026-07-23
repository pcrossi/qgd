# Hessiana estratificada do modo de nucleação bimodal

## 1. Diagnóstico da Hessiana existente

A Hessiana bariônica da Q40 foi construída no domínio

$$
\delta B_{\text{top}}=0,
\qquad
\delta N_{\text{estoma}}=0,
\qquad
\delta Q_B=0,
\qquad
\delta J_B=0.
$$

Ela demonstra estabilidade dentro do setor de três estômatos. A nucleação
proposta, porém, muda

$$
N_{\text{estoma}}:3\longrightarrow3+2.
$$

Portanto, o modo bimodal não pertence ao espaço tangente usado na Q40. Não é
correto inseri-lo diretamente em
$\mathcal O_B=\operatorname{Hess}\mathcal S_{\rm GDQ}|_{\mathfrak G_n}$.

## 2. Espaço de configurações estratificado

Defina

$$
\mathscr C_3
=\{\text{configurações regulares com três estômatos}\},
$$

$$
\mathscr C_{3+2}
=\{\text{configurações regulares com três estômatos e um par bimodal}\}.
$$

Os dois setores encontram-se numa configuração singular em que o raio do novo
par tende a zero. Denote esse estrato por $\mathscr S_*$ e forme

$$
\boxed{
\overline{\mathscr C}
=\mathscr C_3\cup_{\mathscr S_*}\mathscr C_{3+2}.
}
$$

A coordenada de nucleação é unilateral:

$$
a\in[0,a_0),
$$

com $a=0$ no estrato de três estômatos e $a>0$ no estrato bimodal. O objeto
correto é a expansão assintótica da ação ao aproximar o estrato singular pelo
lado $a>0$, não uma Hessiana bilateral em $a=0$.

## 3. Família regularizada

Na fatia transversal $X_4$, escolha dois centros $x_\pm(a)$ relacionados pela
involução do par e remova

$$
B^4_\pm(a)=\{x:d(x,x_\pm(a))<r(a)\}.
$$

O domínio regularizado é

$$
X_{4,a}^{\circ}
=X_4\setminus\left(B^4_+(a)\sqcup B^4_-(a)\right),
\qquad a>0.
$$

Nos dois elos $Y_\pm(a)\simeq S^3$, imponha colares de forma produto e mapas
de transição complementares. Os campos são

$$
\Phi_a=(g_a,f_a,H_a,\Psi_a),
$$

com

$$
\Phi_a\longrightarrow\mathfrak G_n
\quad\text{fora de uma vizinhança que encolhe quando }a\downarrow0,
$$

$$
\int_{\Sigma_a}H_a=Q_{\text{pref}}=2\tau,
$$

e $\Psi_a|_{Y_+\sqcup Y_-}$ realizando o fator local zero--polo. No bulk
oficial, essa família deve ser levantada pelo fator espectador $T^4$.

## 4. Diferença unilateral de ação

Defina, no mesmo contorno causal $\gamma$,

$$
\Delta\mathcal A(a)
=\mathcal S_{\rm GDQ}[\Phi_a;\gamma]
-\mathcal S_{\rm GDQ}[\mathfrak G_n;\gamma].
$$

A família é admissível somente se a diferença for finita após a mesma
regularização de bordo nos dois termos. A expansão procurada é

$$
\boxed{
\Delta\mathcal A(a)=c_2a^2+c_4a^4+o(a^4).
}
$$

O coeficiente físico de nucleação é

$$
\boxed{
c_2
=\liminf_{a\downarrow0}
\frac{\Delta\mathcal A(a)}{a^2}.
}
$$

Quando a extensão é duas vezes diferenciável pela direita,

$$
\lambda_{2,+}=2c_2.
$$

## 5. Parcela torsional determinada

Para

$$
V(a)=V_0+\nu a^2+O(a^4),
\qquad \nu>0,
$$

e $Q_{\text{pref}}=2\tau$ conservado,

$$
E_T(a)
=\frac{\kappa_T(2\tau)^2}{2V(a)}
=\frac{2\kappa_T\tau^2}{V(a)}.
$$

Logo,

$$
E_T(a)-E_T(0)
=-\frac{2\kappa_T\tau^2\nu}{V_0^2}a^2+O(a^4).
$$

Portanto,

$$
\boxed{
c_T=-\frac{2\kappa_T\tau^2\nu}{V_0^2}<0,
}
$$

e

$$
\boxed{
\lambda_{T,+}=2c_T
=-\frac{4\kappa_T\tau^2\nu}{V_0^2}<0.
}
$$

A torção dupla reduz a ação na direção unilateral que abre o par.

## 6. Parcela ainda não determinada

Defina

$$
c_{\text{geom}+f+\text{cola}}
=\liminf_{a\downarrow0}
\frac{\Delta\mathcal A_{\text{geom}+f+\text{cola}}(a)}{a^2}.
$$

Esse coeficiente contém curvatura das duas calotas, gradiente de $f$, medida
$\mathcal U$, transgressão de Bismut, impedância dos colares e contorno causal.
O valor $1/(4\pi^3)$ da Q40 é a impedância de uma garganta já formada; ele não
fornece automaticamente a lei de escala de uma garganta com raio tendendo a
zero.

## 7. Relaxação dos modos transversais

Para perturbações regulares $\xi$, escreva

$$
\begin{aligned}
\Delta\mathcal A(a,\xi)
=&\left(c_{\text{geom}+f+\text{cola}}+c_T\right)a^2
+a\,\operatorname{Re}\langle j,\xi\rangle\\
&+\frac12\langle\xi,K_\perp\xi\rangle
+o(a^2+\|\xi\|^2).
\end{aligned}
$$

Se $K_\perp>0$ após remover os modos zero,

$$
\xi_*(a)=-aK_\perp^{-1}j+o(a),
$$

e

$$
\boxed{
c_2^{\text{eff}}
=c_{\text{geom}+f+\text{cola}}
-\frac{2\kappa_T\tau^2\nu}{V_0^2}
-\frac12\langle j,K_\perp^{-1}j\rangle.
}
$$

## 8. Teorema de bifurcação estratificada

> **Teorema condicional.** Suponha que a família $\Phi_a$ exista, que a ação
> relativa admita a expansão acima, que $K_\perp$ seja positivo depois da
> remoção dos modos zero e que $c_4>0$. Se
>
> $$
> c_2^{\text{eff}}<0,
> $$
>
> então existem configurações bimodais com $a>0$ arbitrariamente pequeno e
> ação menor que a do limite sem par. O estrato neutrônico é unilateralmente
> instável e a torção nucleia dois estômatos.

Se $c_2^{\text{eff}}>0$, não há nucleação clássica local, mas ainda pode haver
uma sela causal de ação finita em $a>0$.

## 9. Relação com a estabilidade da Q40

A positividade da Hessiana da Q40 controla $K_\perp$ no setor que preserva
$N_{\text{estoma}}=3$, mas não determina
$c_{\text{geom}+f+\text{cola}}$, que compara estratos diferentes. Portanto,
não há contradição entre estabilidade do nêutron em $\mathscr C_3$ e possível
instabilidade unilateral em direção a $\mathscr C_{3+2}$.

## 10. Próximo cálculo bem posto

Para uma sequência $a_k\downarrow0$, resolver

$$
(g_{a_k},f_{a_k},H_{a_k})
=\operatorname*{Crit}\mathcal S_{\rm GDQ}
$$

em $X_{4,a_k}^{\circ}\times T^4$, com:

1. fluxo $Q_{\text{pref}}=2\tau$ fixo;
2. colagens complementares em $Y_\pm(a_k)$;
3. mesma normalização de $\mathcal U$;
4. mesmo contorno causal $\gamma$;
5. matching com $\mathfrak G_n$ fora da nucleação.

Então avaliar

$$
c_2^{\text{eff}}
=\liminf_{k\to\infty}
\frac{
\mathcal S_{\rm GDQ}[\Phi_{a_k}]
-\mathcal S_{\rm GDQ}[\mathfrak G_n]
}{a_k^2}.
$$

Esse limite, e não a Hessiana fixa da Q40, decide se a torção dupla cria o par.

## 11. Status

- exclusão do modo pela Hessiana original da Q40: verificação documental;
- espaço estratificado e família perfurada: construção matemática;
- coeficiente torsional $c_T<0$: derivação setorial exata;
- fórmula de relaxação por Schur: derivação funcional condicional;
- sinal de $c_2^{\text{eff}}$: aberto até resolver calotas e colares;
- nucleação clássica: condicional a $c_2^{\text{eff}}<0$.

## 12. Auditoria pela coordenada radial física

O ansatz $V(a)=V_0+\nu a^2+\cdots$ não deve ser identificado automaticamente
com o raio da garganta. Para o raio físico $r$ de um elo $S^3$, a lei natural
é $\Delta V\sim r^3$. Nesse caso, a parcela torsional começa em ordem cúbica,
enquanto as calotas custam ordem $r^2$. O tratamento radial corrigido está em
`topicos/geometria_torcao_hopf/nucleo_critico_par_mesonico.md` e conduz a uma nucleação por núcleo crítico
finito, não necessariamente a $c_2^{\rm eff}<0$.

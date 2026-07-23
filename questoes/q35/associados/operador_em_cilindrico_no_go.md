# Q35 — Operador eletromagnético no colar cilíndrico e no-go local

## 1. Enunciado

O objetivo é construir o operador $L_{\rm EM}^{(2)}$ usando somente o
background e a interface já derivados, sem acrescentar massa fotônica,
coeficiente Robin ou potencial de confinamento.

O background disponível é o colar homogêneo

$$
ds^2=dr^2+g_{S^3},
\qquad
f=f_0,
\qquad
r\in[r_c,r_\infty).
$$

No canal eletromagnético, a Hessiana da interface possui autovalor zero.

## 2. Forma quadrática

A redução de O'Neill da curvatura oficial fornece a forma de Maxwell

$$
\mathfrak q_{\rm EM}[A]
=
\frac14
\int Z_{\rm EM}(r)
|dA|^2\,dV,
$$

com $Z_{\rm EM}>0$ no setor admissível. Depois da projeção transversal

$$
\delta_f A=0,
$$

o operador físico é o operador de Hodge ponderado

$$
\boxed{
L_{\rm EM}^{(2)}
=
P_T\,\delta_f
\left(
Z_{\rm EM}\,d
\right)P_T.
}
$$

No ramo cilíndrico homogêneo, $Z_{\rm EM}$ é constante. Para o modo interno
fotônico fundamental, a parte radial reduz a

$$
\boxed{
L_{\gamma,r}
=
-\frac{d^2}{dr^2}.
}
$$

## 3. Domínio e interface

A condição Robin geral derivada na Q29 é

$$
\left(
\nabla_n+\mathsf R_a^{\rm Robin}
\right)\Psi_a=0.
$$

No canal do fóton,

$$
\mathsf R_\gamma^{\rm Robin}=0.
$$

Logo, sem inserir uma impedância adicional,

$$
\boxed{
\partial_n\Psi_\gamma=0.
}
$$

O domínio local disponível é, portanto, $H^2$ com condição de Neumann.

## 4. Colar compacto

Para um intervalo de comprimento

$$
L=r_\infty-r_c<\infty
$$

com Neumann nas duas extremidades,

$$
\Psi_n(r)
=
\cos\left(\frac{n\pi(r-r_c)}{L}\right),
\qquad
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
n=0,1,\ldots
$$

O kernel $n=0$ é o fóton constante. Depois de removê-lo,

$$
\boxed{
\lambda_{1,\rm EM}^+
=
\frac{\pi^2}{L^2},
\qquad
\Lambda_{\rm EM}
=
\frac{\pi}{L}
}
$$

na normalização radial unitária. Assim, a escala depende do comprimento
global do colar. A geometria infinitesimal local não determina $L$.

## 5. Colar infinito

Quando $L\to\infty$,

$$
\lambda_{1,\rm EM}^+\to0.
$$

No semieixo, o espectro de $-d^2/dr^2$ com Neumann é contínuo:

$$
\operatorname{spec}(L_{\gamma,r})=[0,\infty).
$$

Portanto não existe primeiro autovalor positivo isolado:

$$
\boxed{
\inf\left(
\operatorname{spec}L_{\gamma,r}\setminus\{0\}
\right)=0.
}
$$

Isso coincide com a divergência da norma do modo constante já encontrada na
Fase 2 do colar dinâmico.

## 6. Consequência

O background local atualmente derivado produz uma alternativa exata:

1. colar infinito: não há gap espectral e não se determina
   $\Lambda_{\rm EM}>0$;
2. colar compacto: $\Lambda_{\rm EM}=\pi/L$, mas $L$ é dado global da
   colagem.

Logo,

$$
\boxed{
\text{a escala eletromagnética não pode ser extraída do colar local;}
\quad
\text{ela exige o comprimento ou o operador global de colagem.}
}
$$

Esse resultado não é falha da Q35. Ele identifica $\Lambda_{\rm EM}$ como
escala global/setorial, de modo análogo à impossibilidade de reconstruir uma
propriedade global usando apenas um infinitésimo de fibra.

## 7. O que poderia alterar o resultado

Um gap positivo independente de $L$ exigiria derivar da ação ou da colagem:

1. um potencial ponderado $V_{\rm EM}(r)$;
2. uma impedância Robin eletromagnética não nula;
3. localização por warp/dilatão em background estável;
4. uma seção compacta global com espectro transversal positivo.

Nenhum desses elementos pode ser escolhido por ajuste.

## 8. Classificação

- operador e condição de Neumann: **derivação no background disponível**;
- espectro compacto: **resultado analítico exato**;
- limite infinito sem gap: **no-go local**;
- valor físico de $\Lambda_{\rm EM}$: **dado global ainda não calculado**.

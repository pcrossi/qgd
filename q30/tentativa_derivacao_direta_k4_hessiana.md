# Q30 — Tentativa de derivar $k^{-4}$ diretamente da Hessiana GDQ

## 1. Pergunta

Pretende-se demonstrar

$$
\operatorname{Hess}\mathcal S_{\rm GDQ}
\longrightarrow
\widetilde{\mathsf R}_{\rm est}(k)\sim k^{-4},
$$

sem usar previamente $V(r)=\sigma r$.

## 2. Ordem diferencial

A ação contém curvatura escalar e primeiros gradientes de $f$. Depois de
fixar gauge e tratar bordos, sua Hessiana local tem genericamente símbolo
principal de segunda ordem:

$$
\boxed{
\mathcal H^{(2)}(k)=k^2\mathsf M_2+\mathsf M_0+\cdots.
}
$$

Se $\mathsf M_2$ é invertível no subespaço físico,

$$
\boxed{
(\mathcal H^{(2)})^{-1}(k)\sim k^{-2}\mathsf M_2^{-1}.
}
$$

Uma Hessiana local não degenerada de segunda ordem não produz $k^{-4}$ no
infravermelho.

## 3. Teste em dois blocos

Considere

$$
\mathcal H(k)
=k^2\begin{pmatrix}a&b\\b&c\end{pmatrix}
+k^4\begin{pmatrix}\alpha&\beta\\\beta&\gamma\end{pmatrix}+\cdots.
$$

Se $ac-b^2\ne0$, todos os elementos do inverso começam em $k^{-2}$. Um modo
$k^{-4}$ somente pode aparecer se

$$
\boxed{ac-b^2=0}
$$

e a matriz de quarta ordem tiver projeção positiva na direção nula física.
Logo, o critério direto é

$$
\boxed{
\det\mathsf M_2=0\text{ numa direção física não gauge},
\qquad
\langle v_0,\mathsf M_4v_0\rangle>0.
}
$$

## 4. O heat-kernel no infravermelho

O propagador suavizado é

$$
G_\tau(k)=\frac{e^{-\tau k^2}}{k^2+m^2}.
$$

Para $m=0$ e $k\to0$,

$$
G_\tau(k)=\frac1{k^2}-\tau+O(k^2).
$$

Logo, a suavização modifica o ultravioleta, mas não gera $k^{-4}$ no
infravermelho. O operador inverso é

$$
G_\tau^{-1}(k)
=k^2e^{\tau k^2}
=k^2+\tau k^4+O(k^6).
$$

O termo quartico domina somente se o coeficiente físico de $k^2$ for
cancelado.

## 5. Equilíbrio não é degeneração da Hessiana

O equilíbrio Ricci--Bohm anula a primeira variação. Isso não implica
automaticamente $\det\mathsf M_2=0$ na segunda variação. Um tubo estável
normalmente possui rigidez quadrática positiva.

Portanto, usar o equilíbrio transversal como prova imediata do cancelamento
de $k^2$ seria um salto lógico.

## 6. Resultado da tentativa local

$$
\boxed{
\text{a Hessiana local GDQ em torno do vácuo homogêneo não deriva
automaticamente uma resposta }k^{-4}.
}
$$

O cálculo operacional anterior permanece correto como transformada da lei
linear, mas não é derivação perturbativa do polo a partir do vácuo.

## 7. Rota correta

A lei linear é resposta não perturbativa do tubo:

$$
\boxed{
\text{ação GDQ}
\to\text{sela tubular}
\to\text{integração dos modos transversais}
\to\Gamma_{\rm tubo}[X]
\to V(r)=\sigma r.
}
$$

Ao representar essa resposta coletiva em três dimensões surge $k^{-4}$; ele
não precisa ser polo elementar da Hessiana local.

Uma rota alternativa seria provar uma direção crítica física com
$\det\mathsf M_2=0$ e termo $\tau k^4>0$, mas essa segunda variação ainda não
foi calculada.

## 8. Consequência para Clay

Seria necessário provar uma das teses:

1. a medida sobre selas tubulares produz lei de área e kernel estático
   $k^{-4}$;
2. a Hessiana física possui direção não gauge com símbolo líder
   $+\tau k^4$.

A primeira é mais compatível com a GDQ atual.

A rota coletiva foi formulada em `q30/medida_selas_tubulares_lei_area.md`.
Ela constrói a medida em corte espectral finito e deriva condicionalmente a
lei de área por Laplace e subaditividade. Permanecem o limite $N\to\infty$ e o
controle global das thimbles.

## 9. Status

$$
\boxed{
\text{tentativa direta local: resultado negativo;
rota coletiva tubular: programa correto ainda a executar.}
}
$$

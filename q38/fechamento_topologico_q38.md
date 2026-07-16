# Q38 — fechamento topológico pela ação oficial da GDQ

## 1. Equação crítica

No setor métrico ordinário do funcional normalizado, a sela *shrinking*
satisfaz

\[
\operatorname{Ric}(g)+\nabla^2\sigma=\lambda g,
\qquad \lambda=\frac1{2\tau}>0.
\]

Pretendia-se avaliá-la numa compactificação interna de topologia
\(K=T^5\times S^3\), eventualmente com uma métrica *warped*.

## 2. Obstrução local ao produto plano

No produto direto, com toro plano e \(\sigma\) constante nas direções
toroidais, a projeção \(AB\) dá \(0=\lambda g_{AB}\), impossível para
\(\lambda>0\). Mesmo permitindo \(\sigma\) não constante e mantendo o fator
toroidal plano, o traço integrado produziria

\[
\int_{T^5}\Delta\sigma\,dV
=5\lambda\operatorname{Vol}(T^5)>0,
\]

em contradição com o teorema de Stokes.

## 3. Obstrução global: o warp não resolve

Um sóliton gradiente *shrinking* completo e compacto possui grupo
fundamental finito. O mecanismo geométrico é que, no recobrimento universal,

\[
\operatorname{Ric}_{\sigma}
:=\operatorname{Ric}+\nabla^2\sigma=\lambda g>0.
\]

Como a base é compacta, a oscilação de \(\sigma\) é limitada. A estimativa de
diâmetro de Bakry--Émery aplicada ao recobrimento torna-o compacto; portanto,
o recobrimento tem um número finito de folhas e \(\pi_1(K)\) é finito.

Mas

\[
\pi_1(T^5\times S^3)=\mathbb Z^5,
\]

que é infinito. Logo,

\[
\boxed{T^5\times S^3\text{ não admite uma sela gradiente shrinking
compacta da equação oficial ordinária.}}
\]

A conclusão independe das coordenadas e não é removida por um warp suave que
preserve a topologia.

## 4. Normalização e redução gravitacional

No modo interno normalizado,

\[
\int_K\mathcal U_*\,dV_K=1.
\]

Assim, um fator constante \(e^{-\sigma_*}\) é absorvido pela normalização.
Um warp produziria a média ponderada \(\langle e^{2A}\rangle_{\mathcal U}\),
mas não pode criar a sela shrinking proibida acima.

Permanece válida a redução formal

\[
C_R^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\int_\gamma d\tau
\int_K\eta_R e^{2A}\mathcal U_*\,dV_K,
\qquad
G=\frac{c^4}{16\pi C_R^{\rm GDQ}}.
\]

Ela identifica o coeficiente a calcular, mas não determina seu valor sem uma
sela admissível.

## 5. Setor steady de Bismut

O background de Hopf com torção pode permanecer candidato *steady*
(\(\lambda=0\)) ou background constitutivo. Isso não equivale à equação
shrinking. Para ele determinar \(G\), deve-se definir explicitamente
\(\mathcal R\) como escalar da conexão de Bismut e exibir sua dependência em
\((g,J)\); só então sua variação e sua Hessiana são unívocas. Não se acrescenta
Yang--Mills nem se promove a torção a campo independente se a ação oficial não
o faz.

## 6. Veredito

\[
\boxed{\text{Q38 fechada como diagnóstico estrutural e aberta como
previsão numérica de }G.}
\]

Precisamente:

1. \(G=c^4/(16\pi C_R^{\rm GDQ})\) está formalmente derivada;
2. a compactificação shrinking \(T^5\times S^3\) está excluída;
3. o fator isolado \(e^{-1/(2\alpha)}\) não foi derivado;
4. o valor numérico requer outra sela admissível ou a definição variacional
   completa do setor steady de Bismut.

Não resta uma EDP de warp a resolver dentro do ansatz shrinking
\(T^5\times S^3\): esse caminho está encerrado pela topologia.

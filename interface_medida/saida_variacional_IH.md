# Saída — teste variacional do perfil torsional \(I_H\)

## 1. Classificação

\[
\boxed{\text{diagnóstico de sensibilidade espectral}}
\]

O teste usa o operador axial da Q42 como candidato diagnóstico:

\[
K_H
=-\frac1{e^{-x^2/4}}
\frac d{dx}
\left(e^{-x^2/4}\frac d{dx}\right)+2.
\]

Os kernels \(c_H\) e \(i_H\) são exemplos normalizados. Eles não são ainda
os kernels físicos derivados da colagem.

## 2. Casos

Foram considerados:

1. \(i_H=c_H\), ambos gaussianos de largura 0,4;
2. circulação localizada com largura 0,4 e acoplamento de largura 1,0;
3. circulação localizada e acoplamento uniforme;
4. condições Robin \(R=0,1,5\);
5. malhas \(N=400,800,1600,3200\).

O valor do quantum foi normalizado como \(C_{1/2}=1\). Para outro valor, todos
os resultados de \(I_H\) escalam linearmente.

## 3. Limites convergidos

Valores em \(N=3200\):

| Robin | Kernel magnético | \(I_H/C_{1/2}\) | Susceptibilidade | \(E_{\min}\) |
|---:|---|---:|---:|---:|
| 0 | \(i=c\) | 1,0000000 | 0,4711719 | 1,0611838 |
| 0 | largura 1,0 | 0,7978652 | 0,4711719 | 1,0611838 |
| 0 | uniforme | 0,5987088 | 0,4711719 | 1,0611838 |
| 1 | \(i=c\) | 1,0000000 | 0,3120327 | 1,6023961 |
| 1 | largura 1,0 | 0,8284768 | 0,3120327 | 1,6023961 |
| 1 | uniforme | 0,6316061 | 0,3120327 | 1,6023961 |
| 5 | \(i=c\) | 1,0000000 | 0,1783376 | 2,8036710 |
| 5 | largura 1,0 | 0,8964224 | 0,1783376 | 2,8036710 |
| 5 | uniforme | 0,7046250 | 0,1783376 | 2,8036710 |

## 4. Convergência

Entre \(N=1600\) e \(N=3200\):

- mudança máxima da razão: aproximadamente \(2,15\times10^{-6}\);
- mudança máxima da susceptibilidade: aproximadamente
  \(1,80\times10^{-6}\);
- resíduos lineares ficaram entre \(10^{-13}\) e \(10^{-11}\);
- todas as susceptibilidades e energias foram positivas.

No caso \(i_H=c_H\):

\[
\boxed{
I_H/C_{1/2}=1
}
\]

com erro numérico zero na precisão apresentada, independentemente da condição
Robin.

## 5. Interpretação

O teste confirma:

\[
I_H
=C_{1/2}
\frac{\mathcal I_H[K_H^{-1}c_H]}
{\mathcal C_H[K_H^{-1}c_H]}.
\]

Assim:

1. a circulação quantizada fixa a escala global do perfil;
2. a condição Robin altera a susceptibilidade e a energia do setor;
3. o acoplamento magnético pode medir uma combinação diferente da circulação;
4. quando os funcionais diferem, aparece um fator de forma geométrico;
5. a igualdade \(I_H=C_{1/2}\) é exata somente quando
   \(\mathcal I_H=\mathcal C_H\).

Se uma integral topológica anterior fornece \(C_{1/2}=1/2\), então:

\[
I_H=\frac12
\]

somente no caso de identidade dos dois funcionais. Nos exemplos diferentes,
o resultado seria \(I_H=(1/2)\times\text{razão espectral}\).

## 6. Veredito

O problema numérico está bem posto e convergente. A pendência física não é o
solver, mas derivar:

- \(c_H(r)\) da holonomia/circulação;
- \(i_H(r)\) do acoplamento magnético;
- a condição Robin física;
- a identidade, ou não, entre esses dois funcionais.


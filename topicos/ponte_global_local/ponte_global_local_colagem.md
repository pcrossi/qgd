# Ponte global--local — colagem do colar ao exterior Berger

## 1. Traços comuns

O colar interno fornece

$$
X_Y^-=(a,c,u,v)
$$

e

$$
\Pi_Y^-=(\Pi_a,\Pi_c,\Pi_u,\Pi_v).
$$

O exterior usa

$$
X_+^{\rm ext}=(x,y,z,u,v),
$$

com

$$
a=e^y,
\qquad
c=e^z.
$$

## 2. Conversão canônica

Pela invariância da forma de Liouville,

$$
\Pi_a\,\delta a+
\Pi_c\,\delta c
=p_y\,\delta y+p_z\,\delta z.
$$

Logo,

$$
\boxed{
p_y=a\Pi_a,
\qquad
p_z=c\Pi_c,
\qquad
p_u=\Pi_u,
\qquad
p_v=\Pi_v.
}
$$

Essa identidade fixa o adaptador sem coeficientes livres.

## 3. Warp toroidal

O traço $x=\log A$ não existe no colar normal porque o $T^4$ foi fatorado e
mantido fixo nessa redução. Portanto há duas opções matematicamente distintas:

1. impor $x|_Y=x_{T^4}$ como dado de Dirichlet da compactificação;
2. ampliar o colar interno para incluir a resposta de $T^4$ e então colar
   também seu momento.

A construção mínima vigente usa a primeira opção. Assim, $p_x$ é uma reação
exterior determinada pela solução, não um momento ajustado ao DtN interno.

## 4. Orientações

Se a coordenada exterior cresce da interface esquerda para a direita, a
colagem esquerda pode ser escrita como

$$
p_A(s_-)=p_A^-(Y_-)
$$

na convenção canônica orientada. Na interface direita,

$$
p_A(s_+)=-p_A^-(Y_+)
$$

para dois colares geometricamente refletidos. A forma invariante permanece

$$
\Pi_A^-+\Pi_A^+=0.
$$

## 5. Resíduo conjunto

O problema completo deve zerar

$$
\mathfrak F
=\begin{pmatrix}
\mathfrak F_{Y_-}\\
\mathfrak F_{Y_+}\\
\mathcal C_N\\
\mathcal C_L\\
\mathcal C_R\\
\mathcal C_E\\
\mathcal C_{\rm norm}\\
\mathcal C_{\rm Noether}
\end{pmatrix}.
$$

Os resíduos de interface contêm continuidade dos quatro traços e dos quatro
momentos. Não se deve impor simultaneamente um dado de Dirichlet e outro de
Neumann independente para o mesmo campo; os dados livres são distribuídos
entre as duas pontas pelo problema de tiro/colocação.

## 6. Teste do adaptador

O script `ponte_global_local_colagem.py`:

1. integra o fixture histórico do colar interno;
2. converte exatamente seu estado final em dados exteriores;
3. verifica o resíduo da interface;
4. integra um trecho exterior sem otimização;
5. mede o resíduo de uma condição refletida simples.

O teste não procura uma sela e preserva o resíduo ruim. Sua finalidade é
validar a conversão e impedir que uma falha de orientação seja confundida com
física.

## 7. Dado ainda ausente do resíduo numérico físico

O componente

$$
\mathcal C_E=\mathcal H_\xi-E_H
$$

está definido variacionalmente, mas sua avaliação reduzida ainda depende da
integração da carga de Noether no contorno causal $\gamma$. Enquanto esse
componente não for implementado, qualquer raiz do restante será apenas uma
sela geométrica condicional a energia não fixada.

## 8. Busca sem simetria imposta

O script `ponte_global_local_busca_duas_interfaces.py` implementa dois colares
independentes e um exterior Berger, com dez variáveis e dez resíduos. Ele não
impõe reflexão nem arredondamento. O resultado atual está documentado em
`topicos/ponte_global_local/ponte_global_local_busca_duas_interfaces_resultado.md`: foi encontrado um
candidato com resíduo preciso de ordem $10^{-3}$, ainda não aceito como raiz.

# Q30 — Auditoria auxiliar: holonomia plana não fixa a tensão GDQ

## 1. Pergunta

A conexão clock--shift das três câmaras é plana no interior,

$$
\mathcal F_{\mathcal A_\rho}=0,
$$

mas possui holonomia global irreducível. Pretende-se saber se isso basta para
calcular uma tensão de tubo $\sigma>0$ pela ação oficial.

## 2. Separação entre gap e tensão

A holonomia irreducível modifica o domínio do laplaciano covariante e elimina
seções adjuntas paralelas. Por isso pode produzir
$\lambda_{1,\rm cor}>0$ mesmo com $\mathcal F=0$ localmente.

Entretanto, uma densidade local quadrática em $\mathcal F$, proveniente da
redução da curvatura, satisfaz

$$
\mathcal E_{\mathcal F}[\mathcal A_\rho]=0.
$$

Logo,

$$
\boxed{
\text{gap por holonomia não implica tensão local positiva.}
}
$$

## 3. Avaliação da ação GDQ

A tensão correta é

$$
\sigma_{\rm GDQ}
=\frac{\mathcal S[q_*]-\mathcal S[q_{\rm vac}]}{L_tL_z}
$$

na continuação estacionária apropriada. Para a conexão plana com módulos
congelados, sua contribuição local à curvatura KK é nula. Restam:

1. o setor de circulação de $f$;
2. a curvatura e a torção das transições de patch;
3. termos de bordo exigidos pela variação;
4. a diferença da medida ponderada em relação ao vácuo.

Nenhum desses termos foi avaliado na construção clock--shift.

## 4. Circulação isolada

No modelo radial, a contribuição angular contém

$$
2\pi\mathfrak c_1
\int_0^\infty\frac{dr}{r}
e^{-u}(n_C-qa)^2.
$$

Sem um perfil $u(r)$ derivado ou cancelamento horizontal completo, ela é
logarítmica. Se $a$ cancela a circulação fora do núcleo, o valor depende do
perfil e do tamanho do núcleo. Portanto, não há número universal extraível
somente de $n_C$.

## 5. No-go de determinação atual

Os dados $(P,Q)$, $\mathbb Z_3$ e $\lambda_{1,\rm cor}>0$ não determinam
$\sigma$. Métricas transversais e perfis de $u$ diferentes podem ter as mesmas
holonomias, mas ações por unidade de comprimento diferentes.

Assim,

$$
\boxed{
\sigma\text{ não pode ser calculada da holonomia clock--shift sem o
background métrico--dilatônico e os termos de colagem.}
}
$$

## 6. Dado mínimo ausente

Para determinar $\sigma$ sem ajuste, é necessário obter da ação

$$
\boxed{
\left(
g_\Sigma,\ u_*,\ v_*,\ H_*,\
\mathcal D_{\partial\Sigma}
\right).
}
$$

Equivalentemente, deve-se resolver as equações variacionais na seção de três
câmaras com as holonomias $P,Q,(PQ)^{-1}$ e condições de bordo derivadas.

## 7. Exclusões

Não serão usados para preencher a lacuna:

1. tensão fenomenológica de QCD;
2. ação de plaqueta de Wilson;
3. raio hadrônico experimental;
4. $\alpha_s$ inserido como parâmetro;
5. termo de transgressão não derivado da variação oficial.

## 8. Resultado

$$
\boxed{
\text{Q30: gap de cor condicionalmente demonstrado;
tensão }\sigma\text{ indeterminada pelo background ausente.}
}
$$

Este resultado impede que a prova espectral do gap seja usada indevidamente
como cálculo da lei de área.

## 9. Correção posterior do background

O background fundamental não é $\Sigma_{0,3}$. A correção está em
`q30/correcao_background_transversal_gdq.md`: a seção é o pescoço
Ricci--Bohm estabilizado do tubo. O presente no-go permanece válido somente
contra a tentativa de obter $\sigma$ de uma conexão plana auxiliar.

## 10. Classificação

- distinção gap/tensão: derivação exata;
- contribuição de curvatura da conexão plana: zero;
- indeterminação de $\sigma$: no-go com os dados atuais;
- aplicação como background fundamental: rejeitada pela correção GDQ.

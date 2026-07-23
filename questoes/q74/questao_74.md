# Questão 74 — Emaranhamento via GDQ

## 1. Enunciado

A Q74 pergunta como a GDQ deve tratar o emaranhamento quântico sem introduzir
ação fantasmagórica à distância.

A proposta inicial do enunciado contém a ideia correta:

$$
\boxed{
\text{emaranhamento deve ser geometria multipartida + holonomia + contorno.}
}
$$

Mas também contém três pontos que precisam ser corrigidos:

1. não devemos chamar uma coordenada de configuração de “5ª dimensão física”
   sem construção própria;
2. não devemos afirmar que a distância métrica real entre laboratórios é zero;
3. não devemos afirmar imunidade absoluta contra ruído sem calcular Hessiana,
   gap e acoplamento do aparelho.

## 2. Status curto

$$
\boxed{
\text{Q74 fechada estruturalmente como formulação geométrica condicional do emaranhamento.}
}
$$

O que está fechado:

1. a interpretação GDQ do emaranhamento como estado global no espaço de
   configuração;
2. a leitura por holonomia/colagem, não por sinal superluminal;
3. a decomposição por Mayer--Vietoris como linguagem natural de costura;
4. a compatibilidade conceitual com no-signalling;
5. a rota para Bell/correlações por medida condicionada de dois aparelhos.

O que permanece condicional:

1. prova operacional completa de Bell/no-signalling para aparelhos reais;
2. cálculo da Hessiana multipartida;
3. estimativa do gap de proteção e da taxa de decoerência;
4. simulação de detector duplo com escolhas independentes.

Esses pontos não invalidam a formulação estrutural. Eles definem a etapa
metrológica/operacional.

## 3. O erro da separação espacial ingênua

Na mecânica operacional, dois registros podem estar separados por distância
macroscópica no espaço físico reconstruído:

$$
x_A,x_B\in\mathbb R^3,
\qquad
|x_A-x_B|\gg1.
$$

Na GDQ, entretanto, o estado de duas partículas não vive em duas cópias
independentes de $\mathbb R^3$. Ele vive no espaço de configuração:

$$
Q_2
=
M_{\rm loc}\times M_{\rm loc}
$$

ou, no setor reduzido espacial:

$$
Q_2^{\rm red}
\simeq
\mathbb R^3_A\times\mathbb R^3_B.
$$

Portanto, a correlação não exige que um sinal atravesse o espaço físico de
$A$ até $B$. O objeto geométrico é uma seção global:

$$
\Psi_{\rm geom}
\sim
(\rho,S_R)
\quad
\text{em } Q_2.
$$

O que parece “não local” em $\mathbb R^3$ é local no espaço de configuração.

Correção importante:

$$
\boxed{
\mathcal D_{\rm GDQ}(A,B)=0
\text{ não deve ser lido como distância métrica física nula.}
}
$$

A leitura correta é:

$$
\boxed{
\text{há conectividade de seção/colagem no espaço de configuração.}
}
$$

## 4. Mayer--Vietoris e colagem de fase

Dividimos o domínio global em dois abertos:

$$
Q_2
=
U_A\cup U_B.
$$

A sequência de Mayer--Vietoris fornece:

$$
\cdots
\to
H^1(Q_2)
\to
H^1(U_A)\oplus H^1(U_B)
\to
H^1(U_A\cap U_B)
\xrightarrow{\delta}
H^2(Q_2)
\to
\cdots.
$$

As fases locais são representadas por 1-formas:

$$
\theta_A=dS_A,
\qquad
\theta_B=dS_B.
$$

Na interseção, a condição de colagem é:

$$
\theta_A|_{U_A\cap U_B}
-
\theta_B|_{U_A\cap U_B}
=
d\chi.
$$

Assim, o emaranhamento não é uma força entre dois pontos. É uma restrição de
compatibilidade de uma seção global.

Quando a classe global é não trivial:

$$
[\omega]\neq0
\quad
\text{ou}
\quad
\operatorname{Hol}_\Gamma\neq1,
$$

a seção não fatora:

$$
(\rho,S_R)_{AB}
\ne
(\rho_A,S_A)\otimes(\rho_B,S_B).
$$

Esse é o conteúdo geométrico do emaranhamento.

## 5. Estado emaranhado como não fatoração geométrica

No setor reduzido, separabilidade significa:

$$
\rho_{AB}(x_A,x_B)
=
\rho_A(x_A)\rho_B(x_B),
$$

e:

$$
S_{AB}(x_A,x_B)
=
S_A(x_A)+S_B(x_B).
$$

Emaranhamento significa que pelo menos uma dessas fatorações falha:

$$
\rho_{AB}\ne\rho_A\rho_B
\quad
\text{ou}
\quad
S_{AB}\ne S_A+S_B.
$$

Na GDQ, essa falha não é mística. Ela indica que a solução estacionária da
ação/redução no espaço de configuração possui classe global ou contorno
compartilhado.

## 6. No-signalling

Para preservar causalidade operacional, a GDQ precisa satisfazer:

$$
P(a|x,y)=P(a|x),
$$

e:

$$
P(b|x,y)=P(b|y),
$$

onde:

- $x$ é a escolha de aparelho em $A$;
- $y$ é a escolha de aparelho em $B$;
- $a,b$ são registros.

Na linguagem de densidade conjunta:

$$
P(a|x,y)
=
\sum_b P(a,b|x,y).
$$

O requisito é que a marginalização elimine a dependência da escolha distante.

Portanto:

$$
\boxed{
\text{correlação global não é comunicação operacional.}
}
$$

Q74 fecha a formulação geométrica; a prova completa de no-signalling para
aparelhos reais permanece teorema operacional a demonstrar, já registrado em:

- `brain/open-problems/operational-microcausality-no-signalling/index.md`.

## 7. Bell como próximo teste

O alvo operacional é recuperar uma correlação do tipo singlete:

$$
E(\boldsymbol a,\boldsymbol b)
=
-\boldsymbol a\cdot\boldsymbol b.
$$

Na GDQ, isso deve vir de:

1. estado global não fatorável no espaço de configuração;
2. dois aparelhos clássicos impondo eixos $\boldsymbol a$ e $\boldsymbol b$;
3. respostas de interface $\mathsf R_A$ e $\mathsf R_B$;
4. medida condicionada conjunta;
5. marginalização que preserva no-signalling.

A cadeia correta é:

$$
\mathcal S_{\rm GDQ}
\to
(\rho,S_R)_{AB}
\to
\mathsf R_A(\boldsymbol a)
\oplus
\mathsf R_B(\boldsymbol b)
\to
P(a,b|\boldsymbol a,\boldsymbol b)
\to
E(\boldsymbol a,\boldsymbol b).
$$

Isso ainda não foi executado aqui numericamente.

## 8. Robustez e decoerência

O enunciado inicial afirma robustez forte contra ruído. A versão correta é
condicional:

$$
\boxed{
\text{a coerência é protegida se houver gap físico e contorno compatível.}
}
$$

O critério é espectral:

$$
\lambda_1(K_{AB}^{\rm phys})
-
\lambda_0(K_{AB}^{\rm phys})
>
0.
$$

Perturbações locais são suprimidas se:

$$
\|\delta K_{\rm env}\|
\ll
\Delta_{\rm gap}.
$$

Sem esse cálculo, não se deve dizer “imunidade local absoluta”. Deve-se dizer:

$$
\boxed{
\text{proteção topológica/espectral condicional.}
}
$$

## 9. Conclusão

A GDQ resolve conceitualmente o emaranhamento ao remover a imagem errada de
duas partículas pontuais isoladas trocando sinais.

O objeto correto é:

$$
\boxed{
\text{uma seção geométrica global no espaço de configuração multipartido.}
}
$$

A correlação vem de não fatoração, holonomia e colagem de contorno. A
causalidade operacional é preservada quando as marginais locais não dependem da
escolha distante.

Classificação final:

$$
\boxed{
\text{Q74 fechada estruturalmente; Bell/no-signalling metrológico ficam condicionais.}
}
$$


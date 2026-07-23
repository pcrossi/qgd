# Questão 49 — Rotor molecular

## 1. Enunciado

A questão pede avaliar se o tratamento GDQ do rotor molecular responde:

1. se o espectro \(J(J+1)\) é derivado;
2. se o parâmetro elástico é previsto;
3. se a constante de distorção centrífuga \(D\) é calculada para várias
   moléculas;
4. se o mesmo parâmetro funciona sem reajuste.

O arquivo legado associado é:

$$
\texttt{pt-br/41 - O Rotor Rigido Molecular.md}.
$$

## 2. Veredito

$$
\boxed{
\text{Q49 fechada condicionalmente.}
}
$$

O rotor rígido ideal fica fechado estruturalmente: o fator \(J(J+1)\) é a
assinatura espectral do Laplace--Beltrami angular na esfera de orientações
\(S^2\), herdado da Hessiana física projetada no modo coletivo de rotação da
molécula.

A distorção centrífuga líder também é derivada no setor radial harmônico:

$$
E_J
=
B_{\rm GDQ}J(J+1)
-
D_{\rm GDQ}[J(J+1)]^2
+
\cdots .
$$

Porém, a previsão metrológica de \(D\) para muitas moléculas só é cega quando
\(\mu_{\rm GDQ}\), \(R_0\) e \(\omega_e\) forem calculados da Hessiana do
background molecular GDQ. Se esses dados forem importados de espectroscopia,
o cálculo é uma comparação fenomenológica sem reajuste extra, não uma previsão
absoluta da ação.

## 3. Releitura GDQ do capítulo legado

O capítulo legado contém uma ideia correta:

$$
\text{molécula diatômica}
\sim
\text{dois nós geométricos ligados por uma ponte de fluxo}.
$$

No regime de baixa energia, os graus internos rápidos são integrados ou
projetados, restando coordenadas coletivas:

$$
R(t)\in\mathbb R_+,
\qquad
\Omega(t)\in S^2.
$$

A cadeia correta não é importar o rotor quântico como postulado. A cadeia GDQ
é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm mol,*}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
K_{\rm ang}\oplus K_r
\to
\text{espectro molecular reduzido}.
$$

Assim, a mecânica quântica molecular aparece como descrição efetiva do setor
coletivo estável, não como ontologia fundamental.

## 4. Derivação do espectro \(J(J+1)\)

No fundo molecular estacionário, a orientação da ligação pertence à esfera:

$$
\Omega\in S^2.
$$

O setor angular efetivo da Hessiana reduzida é:

$$
K_{\rm ang}
=
-
\frac{\hbar^2}{2I_0}\Delta_{S^2},
\qquad
I_0=\mu_{\rm GDQ}R_0^2.
$$

Como:

$$
-
\Delta_{S^2}Y_{Jm}
=
J(J+1)Y_{Jm},
$$

segue:

$$
E_J^{(0)}
=
\frac{\hbar^2}{2I_0}J(J+1)
=
B_{\rm GDQ}J(J+1).
$$

Logo:

$$
\boxed{
J(J+1)\text{ é derivado no domínio angular reduzido.}
}
$$

A circulação/holonomia discutida no capítulo legado fornece a condição
topológica de fechamento dos estados; a forma precisa \(J(J+1)\) vem da
autoadjunticidade do operador angular em \(S^2\).

## 5. Distorção centrífuga

A coordenada radial da ponte tem expansão:

$$
V_{\rm GDQ}(R)
=
V_0
+
\frac{1}{2}\mu_{\rm GDQ}\omega_e^2(R-R_0)^2
+
\cdots .
$$

Para momento angular fixo:

$$
L^2=\hbar^2J(J+1),
$$

a energia efetiva é:

$$
E(R;J)
=
\frac{L^2}{2\mu_{\rm GDQ}R^2}
+
\frac{1}{2}\mu_{\rm GDQ}\omega_e^2(R-R_0)^2.
$$

Minimizando em \(R\) e expandindo em baixa rotação:

$$
E_J
=
B_{\rm GDQ}J(J+1)
-
D_{\rm GDQ}[J(J+1)]^2
+
\cdots ,
$$

com:

$$
B_{\rm GDQ}
=
\frac{\hbar^2}{2\mu_{\rm GDQ}R_0^2},
$$

e:

$$
D_{\rm GDQ}
=
\frac{\hbar^4}{2\mu_{\rm GDQ}^3\omega_e^2R_0^6}
=
\frac{4B_{\rm GDQ}^3}{\hbar^2\omega_e^2}.
$$

Em unidades espectroscópicas, quando \(B\) e \(\omega_e\) são expressos em
\({\rm cm}^{-1}\):

$$
D_{\rm GDQ}
\simeq
\frac{4B_{\rm GDQ}^3}{\omega_e^2}.
$$

Isso recupera a forma líder da distorção centrífuga sem introduzir um
parâmetro elástico novo no rotor ideal.

## 6. O parâmetro elástico do texto legado

O texto legado escreveu:

$$
D
=
\gamma_{\rm elastic}
\frac{\hbar^4}{4I_0^3\omega_e^2}.
$$

Essa forma é útil historicamente, mas deve ser reclassificada.

Como \(I_0=\mu R_0^2\), a derivação harmônica reduzida fornece:

$$
D_{\rm red}
=
\frac{\hbar^4}{2I_0^3\omega_e^2}.
$$

Portanto, na normalização do capítulo legado:

$$
\gamma_{\rm elastic}^{\rm red}=2.
$$

Conclusão:

$$
\boxed{
\gamma_{\rm elastic}\text{ não deve ser tratado como constante fundamental.}
}
$$

Ele representa uma parametrização efetiva de rigidez radial, anisotropia,
anharmonicidade e resposta de contorno. Na versão limpa da GDQ, esses efeitos
devem vir da Hessiana física do background molecular.

## 7. Respostas às perguntas obrigatórias

| Pergunta | Resposta |
|---|---|
| O espectro \(J(J+1)\) é derivado? | Sim. Ele vem de \(-\Delta_{S^2}\) no domínio angular reduzido da ligação molecular. |
| O parâmetro elástico é previsto? | No rotor harmônico ideal, sim: ele é a rigidez radial \(k_{\rm GDQ}=\mu_{\rm GDQ}\omega_e^2\). Em moléculas reais, precisa ser extraído da Hessiana do background molecular. |
| A constante \(D\) é calculada para várias moléculas? | Ainda não como previsão cega. A fórmula está derivada; faltam backgrounds moleculares específicos ou uso explícito de dados espectroscópicos externos. |
| O mesmo parâmetro funciona sem reajuste? | Não deve haver parâmetro universal único. Cada molécula tem \(R_0\), \(\mu\) e \(\omega_e\) próprios. A ausência de reajuste significa usar esses dados derivados uma vez por molécula e prever a torre rotacional. |

## 8. Limitação que permanece

Para fechar metrologicamente a Q49 seria necessário resolver, para cada
molécula:

$$
\Phi_{\rm mol,*}
\mapsto
\mu_{\rm GDQ},
\quad
R_0,
\quad
\omega_e,
\quad
\text{anharmonicidades}.
$$

Essa etapa pertence a uma teoria GDQ de ligação molecular e química efetiva.
Ela não reabre o rotor ideal, mas impede declarar que a Q49 já calcula \(D\)
cegamente para várias moléculas.

## 9. Status final

$$
\boxed{
\text{Q49 fechada condicionalmente: rotor ideal fechado; metrologia molecular em programa futuro.}
}
$$

O documento associado
`questoes/q49/associados/derivacao_rotor_molecular_gdq.md` contém a derivação
passo a passo do termo de distorção.

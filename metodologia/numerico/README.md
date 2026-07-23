# Método numérico

Scripts numéricos devem ser autocontidos, auditáveis e reproduzíveis.

## Cada script deve informar

1. equação;
2. domínio;
3. operador;
4. contorno;
5. fonte;
6. parâmetros universais;
7. parâmetros de aparelho;
8. observável;
9. classificação;
10. limites testados.

## Saídas obrigatórias

Para cada script, salvar:

1. `.md` com explicação e tabela;
2. `.csv` ou `.npz` com dados;
3. estudo de convergência;
4. veredito conservador.

## Nomes recomendados

Scripts:

$$
\texttt{calcular\_<objeto>\_<questao>.py}
$$

Saídas:

$$
\texttt{saida\_<objeto>\_<questao>.md}
$$

Dados:

$$
\texttt{dados\_<objeto>\_<questao>.npz}
$$

## Biblioteca reduzida comum

O arquivo [gdq_reduced.py](gdq_reduced.py) reúne blocos numéricos reutilizáveis
para aplicações reduzidas já classificadas:

1. DtN de canal massivo unidimensional;
2. complemento de Schur;
3. forma quadrática de resposta;
4. custo de detector linear reduzido;
5. coeficiente de coerência;
6. densidade de duas alternativas com amortecimento do termo cruzado.

Essas funções não substituem a ação oficial. Elas implementam blocos efetivos
usados depois que o domínio, o contorno e a redução física foram declarados.

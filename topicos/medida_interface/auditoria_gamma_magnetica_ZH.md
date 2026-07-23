# Auditoria da razão giromagnética e do fator \(Z_H\)

> **Atualização:** a rota mínima por isotropia e pelo fluxo de Noether comum
> foi consolidada em `topicos/medida_interface/teorema_noether_zeeman_gdq.md`. A fórmula hessiana deste
> documento só é necessária se o campo e a circulação forem funcionais
> físicos distintos. Quando são o mesmo fluxo conservado, a componente mínima
> satisfaz \(Z_{\rm N}=1\), mas o momento total pode conter o vestido geométrico
> transversal derivado em `topicos/medida_interface/teorema_noether_zeeman_gdq.md`.

## 1. Pergunta

O campo magnético é um dado externo. A circulação de spin é imposta como setor
topológico. Pergunta-se se a ação oficial, aumentada pelo vínculo, determina o
momento magnético e o fator anteriormente chamado \(Z_H\).

## 2. Três objetos distintos

Não devem ser identificados sem um mapa demonstrado:

\[
c_1=\frac1{2\pi}\int_{S^2}\mathcal F_H,
\qquad
C_S=\oint p\cdot dx,
\qquad
\mu_i=-\frac{\partial E_{\rm on}}{\partial B_i}.
\]

O primeiro classifica o fibrado de Hopf; o segundo fixa o setor de spin; o
terceiro é a resposta conjugada ao campo externo.

## 3. O que o manuscrito já demonstra

O Capítulo 19 parte de

\[
j^\mu=\nabla_\alpha\mathcal T^{\alpha\mu}
\]

e, por integração por partes, obtém

\[
\frac qc\int A_\mu j^\mu dV
=\frac q{2c}\int\mathcal T^{\mu\nu}F_{\mu\nu}dV
+S_{\partial}.
\]

Isso demonstra a forma gauge-invariante do acoplamento e, após a redução
axial, a forma Zeeman

\[
V_Z=-\boldsymbol\mu\cdot\boldsymbol B.
\]

Também está estabelecido o setor

\[
S_{\boldsymbol n}=\pm\frac\hbar2.
\]

## 4. O que ainda não é derivado no texto original

A passagem

\[
\mathcal T^{\mu\nu}
=g_{\rm geom}\frac{e}{2m}S^{\mu\nu}
\]

é apresentada no Capítulo 19 depois da afirmação de que a dupla cobertura
impõe uma razão de períodos igual a dois. Não há ali uma avaliação da ação
on-shell ou das correntes de carga e massa que demonstre essa igualdade.

Além disso, a Q10 usa \(\mu_B\) dentro do potencial de interface antes de
derivá-lo. Logo:

\[
\boxed{
\text{a forma Zeeman está derivada; o coeficiente giromagnético absoluto não.}
}
\]

A dupla cobertura demonstra a representação de spin \(1/2\), mas não basta,
isoladamente, para demonstrar \(g=2\). Para uma única distribuição clássica
com correntes de carga e massa proporcionais, obtém-se \(g=1\); um valor
diferente exige calcular a relação geométrica entre essas duas correntes.

## 5. Formulação correta por multiplicador de vínculo

Escolha o eixo \(\boldsymbol n\) definido pelo campo do aparelho e denote por
\(C\) a circulação física normalizada de modo que seus setores elementares
sejam \(C=\pm\hbar/2\). Considere o funcional aumentado

\[
\mathscr I[\Phi,\lambda;C,B]
=S_{\rm GDQ}[\Phi]
-B\,M_{\boldsymbol n}[\Phi]
-\lambda\bigl(\mathcal C_{\boldsymbol n}[\Phi]-C\bigr),
\]

com \(B\) mantido fixo durante a variação. Aqui

\[
M_{\boldsymbol n}[\Phi]
=\frac q c\int t_{\boldsymbol n}[\Phi]d\mu_{\rm GDQ}
\]

é o observável conjugado ao campo, conforme a integração por partes do
Capítulo 19.

As equações são

\[
\frac{\delta S_{\rm GDQ}}{\delta\Phi}
-B\frac{\delta M_{\boldsymbol n}}{\delta\Phi}
-\lambda\frac{\delta\mathcal C_{\boldsymbol n}}{\delta\Phi}=0,
\]

\[
\mathcal C_{\boldsymbol n}[\Phi]=C.
\]

Seja \(E(C,B)\) o funcional on-shell correspondente. Pelo teorema do
envelope,

\[
\boxed{
\frac{\partial E}{\partial C}=\lambda(C,B),
\qquad
-\frac{\partial E}{\partial B}=\mu_{\boldsymbol n}(C,B).
}
\]

Consequentemente, a igualdade das derivadas mistas fornece a identidade
variacional

\[
\boxed{
\frac{\partial\mu_{\boldsymbol n}}{\partial C}
=-\frac{\partial\lambda}{\partial B}.
}
\]

No regime linear e isotrópico,

\[
\mu_{\boldsymbol n}=\gamma_{\rm GDQ}C+O(B,C^3),
\]

de modo que

\[
\boxed{
\gamma_{\rm GDQ}
=-\left.\frac{\partial\lambda}{\partial B}\right|_{B=0,C=C_{1/2}}.
}
\]

Essa é a forma direta de determinar a razão giromagnética usando o vínculo na
ação oficial. O multiplicador não é um parâmetro ajustável: ele é resolvido
junto com o background estacionário.

## 6. Relação com \(Z_H\)

O fator \(Z_H\) não deve ser tratado como nova constante fundamental. Ele é
apenas uma parametrização da razão entre o momento conjugado e a circulação.
Escolhida uma referência \(\gamma_0\), define-se

\[
\boxed{
Z_H=\frac{\gamma_{\rm GDQ}}{\gamma_0}.
}
\]

Portanto,

\[
\boxed{
Z_H
=-\frac1{\gamma_0}
\left.\frac{\partial\lambda}{\partial B}\right|_{0,C_{1/2}}.
}
\]

Se a ação reduzida demonstrar que \(B\) desloca o multiplicador por

\[
\lambda(C,B)=\lambda_0(C)-\gamma_0B,
\]

então \(Z_H=1\). Se o coeficiente for diferente, o resultado é um fator
constitutivo/espectral calculado, não uma violação da quantização do spin.

## 7. Expansão pela Hessiana, sem kernels arbitrários

No background vinculado \(\Phi_C\), defina

\[
H_C=\frac{\delta^2}{\delta\Phi^2}
\left(S_{\rm GDQ}-\lambda_0\mathcal C\right),
\quad
m=\frac{\delta M}{\delta\Phi},
\quad
c=\frac{\delta\mathcal C}{\delta\Phi}.
\]

Derivando as equações em relação a \(B\), obtém-se

\[
H_C\Phi_B-m-\lambda_Bc=0,
\qquad
\langle c,\Phi_B\rangle=0.
\]

Assumindo a inversibilidade de \(H_C\) no setor físico,

\[
\boxed{
\lambda_B
=-\frac{\langle c,H_C^{-1}m\rangle}
        {\langle c,H_C^{-1}c\rangle}
}
\]

na convenção de sinais adotada acima. Assim,

\[
\boxed{
\gamma_{\rm GDQ}
=\frac{\langle c,H_C^{-1}m\rangle}
       {\langle c,H_C^{-1}c\rangle}.
}

Essa expressão é a versão intrínseca da razão anteriormente escrita com
\(c_H\), \(i_H\) e \(K_H\), mas agora os objetos são definidos como
diferenciais dos funcionais físicos. Não há liberdade para escolher kernels
gaussianos ou uniformes por conveniência.

## 8. Critério de fechamento

O problema de Stern--Gerlach fica fechado operacionalmente com
\(\gamma_{\rm GDQ}\) mantido como coeficiente mensurável. Uma previsão absoluta
de \(g\) exige avaliar a última razão no background eletrônico estacionário.

Não é necessário modelar o ímã: \(B\) é fonte dada. É necessário apenas o
background do objeto, o vínculo de circulação e os dois diferenciais físicos
\(c\) e \(m\).

Status final:

\[
\boxed{
\begin{aligned}
&\text{forma Zeeman e dois canais: fechados;}\\
&\text{fórmula variacional de }\gamma_{\rm GDQ}\text{ e }Z_H:\text{ fechada;}\\
&\text{valor numérico absoluto de }g:\text{ ainda não avaliado da ação.}
\end{aligned}
}
\]

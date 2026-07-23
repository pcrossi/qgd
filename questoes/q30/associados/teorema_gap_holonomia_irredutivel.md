# Q30 — Gap espectral por holonomia $SU(3)$ irreducível

## 1. Enunciado

Seja $\Sigma$ a seção transversal compacta do tubo GDQ, sem bordo ou com
condições auto-adjuntas derivadas da colagem. Seja $E_C\to\Sigma$ o subfibrado
Hermitiano de posto três da Q28 e

$$
\mathcal A_C\in\Omega^1(\Sigma,\mathfrak{su}(3))
$$

uma conexão geométrica suave.

## 2. Operador e kernel

No espaço de seções adjuntas, considere

$$
\boxed{\Delta_{\mathcal A}=D_{\mathcal A}^{\dagger}D_{\mathcal A}.}
$$

Sua forma quadrática satisfaz

$$
\langle\phi,\Delta_{\mathcal A}\phi\rangle
=\|D_{\mathcal A}\phi\|^2\ge0.
$$

Logo,

$$
\phi\in\ker\Delta_{\mathcal A}
\iff D_{\mathcal A}\phi=0.
$$

O kernel é a álgebra das seções adjuntas paralelas, isto é, a álgebra de Lie
do estabilizador da holonomia.

## 3. Irredutibilidade

Suponha que a holonomia seja irreducível no setor $E_C$. Seu estabilizador
contínuo reduz-se ao centro da álgebra. Como

$$
\mathfrak z(\mathfrak{su}(3))=\{0\},
$$

segue

$$
\boxed{\ker\Delta_{\mathcal A}=\{0\}.}
$$

O centro do grupo $SU(3)$ é discreto, $\mathbb Z_3$, e não produz modo
infinitesimal adjunto.

## 4. Gap no domínio compacto

Em $\Sigma$ compacta, $\Delta_{\mathcal A}$ é elíptico auto-adjunto e possui
resolvente compacto. Seu espectro é discreto e tende ao infinito. Como o
kernel é trivial,

$$
\boxed{\lambda_{1,\mathcal A}>0.}
$$

Equivalentemente, existe $C_{\mathcal A}>0$ tal que

$$
\boxed{
\|D_{\mathcal A}\phi\|^2
\ge C_{\mathcal A}\|\phi\|^2.
}
$$

## 5. Relação com o no-go abeliano

Uma conexão reduzida a um único gerador de Cartan é redutível. Seu
estabilizador contém uma subálgebra de Cartan, permitindo seções adjuntas
paralelas. O no-go radial e este teorema se complementam:

$$
\boxed{
\text{a redução abeliana falha dinamicamente e não remove o kernel;
a holonomia }SU(3)\text{ irreducível remove o kernel adjunto.}
}
$$

## 6. Resultado provado

Sob compacidade, auto-adjunticidade e holonomia irreducível,

$$
\boxed{
D_{\mathcal A}^{\dagger}D_{\mathcal A}
\text{ possui gap positivo.}
}
$$

Essa conclusão é geométrica. Não usa glúons fundamentais, ação de
Yang--Mills postulada, rede de Wilson ou valor experimental de
$\Lambda_{\rm QCD}$.

## 7. Limite do resultado

A Hessiana física completa tem a forma esquemática

$$
\mathcal H_{\rm GDQ}^{\rm phys}
=\Delta_{\mathcal A}
+\mathcal V_{\rm Ricci-Bismut}+\mathcal M_{gf}.
$$

O gap do primeiro bloco implica gap completo somente se

$$
\inf\operatorname{spec}
(\mathcal V_{\rm Ricci-Bismut}+\mathcal M_{gf})
>-\lambda_{1,\mathcal A}.
$$

Também falta demonstrar desde a ação que o minimizador tubular possui
holonomia irreducível e calcular $\lambda_{1,\mathcal A}$.

O controle dos demais blocos foi reduzido em
`questoes/q30/associados/controle_hessiana_fisica_torcional.md` ao critério de Schur
$b^2<m_{\mathcal A}^2m_f^2$.

## 8. Status

$$
\boxed{
\text{mass gap provado condicionalmente para o bloco de conexão GDQ;
gap quantitativo da Hessiana completa ainda pendente.}
}
$$

import GDQ.SternGerlachProjectors

namespace GDQ

/-!
# Stern--Gerlach sequencial

Este módulo formaliza a composição probabilística dos canais angulares já
derivados. Ele não insere operadores do aparelho na ação oficial: pressupõe
que a Hessiana de interface selecionou os dois projetores físicos e calcula a
estatística sequencial resultante.
-/

/-- Probabilidade de retornar ao canal inicial após seleção e reanálise. -/
noncomputable def sternGerlachReturnWeight (θ : ℝ) : ℝ :=
  sternGerlachPlusWeight θ ^ 2 + sternGerlachMinusWeight θ ^ 2

/-- Em eixos ortogonais, cada canal intermediário possui peso `1/2`. -/
theorem sternGerlach_orthogonal_plus :
    sternGerlachPlusWeight (Real.pi / 2) = 1 / 2 := by
  simp [sternGerlachPlusWeight]

/-- Em eixos ortogonais, o canal complementar também possui peso `1/2`. -/
theorem sternGerlach_orthogonal_minus :
    sternGerlachMinusWeight (Real.pi / 2) = 1 / 2 := by
  simp [sternGerlachMinusWeight]

/--
Na sequência `z → x → z`, a soma dos dois caminhos que retornam a `z+` é
`1/2`.
-/
theorem sternGerlach_z_x_z_return :
    sternGerlachReturnWeight (Real.pi / 2) = 1 / 2 := by
  rw [sternGerlachReturnWeight, sternGerlach_orthogonal_plus,
    sternGerlach_orthogonal_minus]
  norm_num

/-- A probabilidade final do canal `z-` na mesma sequência também é `1/2`. -/
theorem sternGerlach_z_x_z_complement :
    1 - sternGerlachReturnWeight (Real.pi / 2) = 1 / 2 := by
  rw [sternGerlach_z_x_z_return]
  norm_num

end GDQ

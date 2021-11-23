#4a
diagnosis_HCC(x) & (~exam_ps_less_equal_2(x)) ==> diagnosis_cnlc_4a(x)
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & (~ exam_child_pugh_AB(x)) ==> diagnosis_cnlc_4a(x)

# 3b
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & exam_extrahepatic_transfer(x) ==> diagnosis_cnlc_3b(x)

# 3a
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & (~ exam_extrahepatic_transfer(x)) & exam_vascular_invasion(x) ==> diagnosis_cnlc_3a(x)

# 2b
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & (~ exam_extrahepatic_transfer(x)) & (~ exam_vascular_invasion(x)) & exam_tumor_number_larger_equal_4(x) ==> diagnosis_cnlc_2b(x)

# 2a
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & (~ exam_extrahepatic_transfer(x)) & (~ exam_vascular_invasion(x)) & exam_tumor_number_2or3(x) & (~ exam_tumor_size_less_equal_3cm(x)) ==> diagnosis_cnlc_2a(x)

# 1b
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & (~ exam_extrahepatic_transfer(x)) & (~ exam_vascular_invasion(x)) & exam_tumor_number_2or3(x) & exam_tumor_size_less_equal_3cm(x) ==> diagnosis_cnlc_1b(x)
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & (~ exam_extrahepatic_transfer(x)) & (~ exam_vascular_invasion(x)) & exam_tumor_number_1(x) & (~ exam_tumor_size_less_equal_5cm(x)) ==> diagnosis_cnlc_1b(x)

# 1a
diagnosis_HCC(x) & exam_ps_less_equal_2(x) & exam_child_pugh_AB(x) & (~ exam_extrahepatic_transfer(x)) & (~ exam_vascular_invasion(x)) & exam_tumor_number_1(x) & exam_tumor_size_less_equal_5cm(x) ==> diagnosis_cnlc_1a(x)


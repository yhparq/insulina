# utils/calculations.py
def calculate_insulin_dose(glucose_level, carb_intake, target_glucose, sensitivity_factor, carb_ratio):
    # Cálculo de la insulina de corrección
    correction_dose = (glucose_level - target_glucose) / sensitivity_factor

    # Cálculo de la insulina para cubrir carbohidratos
    carb_dose = carb_intake / carb_ratio

    # Dosis total recomendada
    total_dose = correction_dose + carb_dose
    return max(total_dose, 0)  # Asegurarse de no tener dosis negativas

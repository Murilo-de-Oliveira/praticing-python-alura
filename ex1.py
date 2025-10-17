def validate_positive_number(value: float, field_name: str) -> bool:
    if value <= 0:
        raise ValueError(f"{field_name} não pode ser menor ou igual a zero.")
    return True


def calculate_tip_value(value: float, tip: float) -> float:
    return value * (tip / 100)


try:
    value = float(input("Digite o valor da conta: "))
    validate_positive_number(value, "Valor da conta")

    tip = float(input("Digite a porcentagem de gorjeta: "))
    validate_positive_number(tip, "Gorjeta")

    tip_value = calculate_tip_value(value, tip)
    total = value + tip_value

    print(f"Valor da gorjeta: R$ {tip_value:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

except ValueError as e:
    print("Erro:", e)
except Exception:
    print("Ocorreu um erro inesperado.")

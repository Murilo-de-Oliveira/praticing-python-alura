def validate_cpf(text: str) -> str:
    if not text.isalnum():
        raise ValueError("O CPF deve conter apenas números.")
    
    if len(text) != 11:
        raise ValueError("O CPF deve ter exatamente 11 dígitos.")
        
    return "CPF válido."
    
cpf = input("Digite seu CPF: ")
try:
    result = validate_cpf(cpf)
    print(result)
except ValueError as e:
    print(f"Erro: {e}")
except Exception:
    print("Erro inesperado no processamento")

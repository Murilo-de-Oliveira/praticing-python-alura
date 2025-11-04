import secrets
import string

# Definição das regras da atividade
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"

# Garante que tenha pelo menos um de cada tipo
password = [
    secrets.choice(uppercase),
    secrets.choice(lowercase),
    secrets.choice(digits),
    secrets.choice(special)
]

# Gera o restante da senha
all_chars = uppercase + lowercase + digits + special
password += [secrets.choice(all_chars) for _ in range(12 - len(password))]

# Embaralha a senha
secrets.SystemRandom().shuffle(password)

# Mostra a senha
print(''.join(password))

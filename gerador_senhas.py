import random 
import string

# Definindo os conjuntos de caracteres
letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

# Mistura tudo em uma única base 
caracteres = letras + numeros + simbolos

# Cabeçalho
print("-" * 40)
print("     🔐  Gerador de Senhas Seguras")
print("-" * 40)

try:
    # Tamanho
    tamanho_senha = int(input("\nQuantos caracteres a senha deve ter? "))

    # Gerando a senha
    senha = ""
    for _ in range(tamanho_senha):
        senha += random.choice(caracteres)

    # Resultado
    print("\n" + "-" * 40)
    print(f"Sua nova senha é:\n{senha}")
    print("-" * 40)
    print("Senha gerada com sucesso!")

except ValueError:
    print("\nErro: Por favor, digite apenas números inteiros.")
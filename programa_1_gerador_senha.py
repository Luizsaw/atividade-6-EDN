import random
import string

tamanho = int(input("Digite a quantidade de caracteres da senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
print(f"Senha gerada: {senha}")

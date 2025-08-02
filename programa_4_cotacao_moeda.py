import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    chave = f"{moeda}BRL"
    if chave in dados:
        info = dados[chave]
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Valor máximo: R$ {info['high']}")
        print(f"Valor mínimo: R$ {info['low']}")
        print(f"Data e hora da última atualização: {info['create_date']}")
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar a cotação.")

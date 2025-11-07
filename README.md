# 🔐 Simulador de Brute Force - Projeto Educacional

## 📋 Descrição

Este projeto demonstra como funciona um ataque de **brute force** contra um sistema de login. É um projeto para entender conceitos de segurança cibernética.

## 🗂️ Estrutura do Projeto

```
p2/
├── servidor_local.py    # Servidor web Flask com página de login
├── bruteforce.py        # Script que simula o ataque de brute force
├── wordlist.txt         # Lista de senhas comuns para testar
└── README.md            # Este arquivo
```

## 🚀 Como Usar

### Pré-requisitos

Certifique-se de ter Python 3 instalado e as bibliotecas necessárias:

```powershell
pip install flask requests
```

### Passo 1: Iniciar o Servidor

Abra um terminal e execute:

```powershell
python servidor_local.py
```

Você verá algo como:

```
==================================================
  SERVIDOR DE TESTE - APENAS PARA FINS EDUCACIONAIS
==================================================
Servidor de login rodando em http://127.0.0.1:5000
A senha correta é: segredo123
==================================================
```

O servidor ficará rodando e você pode acessar `http://127.0.0.1:5000` no navegador para ver a página de login.

### Passo 2: Executar o Ataque de Brute Force

Abra **outro terminal** (deixe o servidor rodando no primeiro) e execute:

```powershell
python bruteforce.py
```

O script tentará cada senha da `wordlist.txt` até encontrar a correta.

## 🔍 Como Funciona

### servidor_local.py
- Cria um servidor web Flask na porta 5000
- Apresenta uma página de login simples
- Verifica se a senha enviada corresponde à senha correta (`segredo123`)
- Retorna mensagens diferentes para sucesso e falha

### bruteforce.py
- Lê senhas de um arquivo de wordlist
- Faz requisições POST para o servidor, tentando cada senha
- Analisa a resposta do servidor procurando por "Acesso Concedido"
- Para quando encontra a senha correta

### wordlist.txt
- Contém uma lista de senhas comuns
- Uma senha por linha
- Usada pelo script de brute force

## 🎓 Conceitos de Segurança Demonstrados

1. **Brute Force Attack**: Tentativa sistemática de adivinhar credenciais testando múltiplas combinações
2. **Wordlist**: Lista de senhas comuns frequentemente usadas em ataques
3. **HTTP POST**: Método usado para enviar dados de formulários
4. **Response Analysis**: Análise das respostas do servidor para determinar sucesso/falha
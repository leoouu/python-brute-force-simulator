from flask import Flask, request, render_template_string

app = Flask(__name__)

SENHA_CORRETA = "segredo123"

LOGIN_PAGE_HTML = """
<html>
    <head><title>Página de Login</title></head>
    <body>
        <h2>Login (Servidor Local de Teste)</h2>
        <p>Usuário: admin</p>
        <p>Tente adivinhar a senha!</p>
        <form method="post">
            Senha: <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
        <p><i>{mensagem}</i></p>
    </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem_erro = ""
    
    if request.method == 'POST':
        senha_tentada = request.form.get('password', '')
        
        if senha_tentada and senha_tentada == SENHA_CORRETA:            
            return "<h1>Acesso Concedido!</h1><p>A senha era 'segredo123'.</p>"
        else:
            mensagem_erro = "Senha incorreta. Tente novamente."

    return render_template_string(LOGIN_PAGE_HTML, mensagem=mensagem_erro)

if __name__ == '__main__':
    print("=" * 50)
    print("  SERVIDOR DE TESTE - APENAS PARA FINS EDUCACIONAIS")
    print("=" * 50)
    print(f"Servidor de login rodando em http://127.0.0.1:5000")
    print(f"A senha correta é: {SENHA_CORRETA}")
    print("=" * 50)
    app.run(port=5000, debug=False)
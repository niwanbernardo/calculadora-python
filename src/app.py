from flask import Flask, render_template_string, request
from .calculadora import Calculadora

app = Flask(__name__)
calc = Calculadora()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora Python Web</title>
    <style>
        body {
            background: #f4f6f8;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 400px;
            margin: 40px auto;
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            padding: 32px 24px 24px 24px;
        }
        h2 {
            text-align: center;
            color: #2d3e50;
            margin-bottom: 24px;
        }
        form {
            display: flex;
            gap: 8px;
            margin-bottom: 18px;
            justify-content: center;
        }
        input[type="text"] {
            flex: 1;
            padding: 10px;
            border: 1px solid #cfd8dc;
            border-radius: 6px;
            font-size: 1rem;
        }
        button {
            background: #1976d2;
            color: #fff;
            border: none;
            padding: 10px 18px;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover {
            background: #1565c0;
        }
        .result, .error {
            text-align: center;
            font-size: 1.2rem;
            margin: 12px 0;
            padding: 8px;
            border-radius: 6px;
        }
        .result {
            background: #e3f2fd;
            color: #1976d2;
            border: 1px solid #90caf9;
        }
        .error {
            background: #ffebee;
            color: #c62828;
            border: 1px solid #ef9a9a;
        }
        h4 {
            margin-top: 24px;
            color: #37474f;
        }
        ul {
            background: #f5f5f5;
            border-radius: 6px;
            padding: 12px;
            list-style: none;
            margin: 8px 0 16px 0;
        }
        ul li {
            padding: 4px 0;
            border-bottom: 1px solid #e0e0e0;
        }
        ul li:last-child {
            border-bottom: none;
        }
        .footer {
            text-align: center;
            color: #90a4ae;
            font-size: 0.95rem;
            margin-top: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Calculadora Python Web</h2>
        <form method="post">
            <input type="text" name="operacao" placeholder="Ex: 14 - 8" required>
            <button type="submit">Calcular</button>
        </form>
        {% if resultado %}
            {% if "Erro:" in resultado %}
                <div class="error">{{ resultado }}</div>
            {% else %}
                <div class="result">Resultado: {{ resultado }}</div>
            {% endif %}
        {% endif %}
        <h4>Histórico de Operações:</h4>
        <ul>
            {% for op in historico %}
                <li>{{ op }}</li>
            {% endfor %}
            {% if not historico %}
                <li><em>Nenhuma operação realizada ainda.</em></li>
            {% endif %}
        </ul>
        <h4>Pilha de Resultados:</h4>
        <ul>
            {% for res in pilha %}
                <li>{{ res }}</li>
            {% endfor %}
            {% if not pilha %}
                <li><em>Pilha vazia.</em></li>
            {% endif %}
        </ul>
        <div class="footer">
            &copy; 2025 Calculadora Python | Desenvolvido por Niwan - Case Engenharia de TI JR
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        operacao = request.form["operacao"]
        try:
            calc.adicionar_operacao(operacao)
            resultado = calc.processar_operacoes()[-1]
            resultado = str(resultado)
        except Exception as e:
            resultado = f"Erro: {e}"
    historico = [str(op) for op in calc.operacoes]
    pilha = calc.pilha_resultados.items
    return render_template_string(HTML, resultado=resultado, historico=historico, pilha=pilha)

if __name__ == "__main__":
    app.run(debug=True)
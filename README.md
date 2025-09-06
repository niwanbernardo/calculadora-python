<!-- Início da seção de introdução -->
<h1>🧮 Calculadora Python 🚀</h1>
<p>
Este repositório contém uma calculadora desenvolvida em Python, capaz de realizar operações aritméticas básicas (adição, subtração, multiplicação e divisão), mantendo histórico e pilha de resultados. O projeto possui interface de linha de comando (CLI) e interface web (Flask), além de testes automatizados.
</p>
<!-- Fim da seção de introdução -->

---

<!-- Início da seção de demonstração -->
<h2>🎥 Demonstração:</h2>
<p>Confira abaixo uma prévia do código em ação:</p>
<img src="https://i.postimg.cc/vZTG8x7r/Captura-de-tela-2025-09-06-163748.png" width="500" height="300" alt="Demonstração da calculadora">
<!-- Fim da seção de demonstração -->

---

<!-- Início da seção de tecnologias -->
<h2>💻 Tecnologias utilizadas:</h2>
<p>
  <img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img align="center" alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img align="center" alt="Pytest" src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white"/>
</p>
<!-- Fim da seção de tecnologias -->

---

<!-- Início da seção de como utilizar -->
<h2>🎮 Como utilizar:</h2>
<ol>
  <li>Clone o repositório:
    <pre><code>git clone https://github.com/niwanbernardo/calculadora-python.git
cd calculadora-python</code></pre>
  </li>
  <li>Instale as dependências:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><b>Para executar via linha de comando (CLI):</b>
    <pre><code>python -m src.main</code></pre>
    <b>Exemplo de uso:</b>
    <ul>
      <li>Digite uma operação no formato: <code>&lt;número&gt; &lt;operador&gt; &lt;número&gt;</code></li>
      <li>Exemplo: <code>14 - 8</code></li>
      <li>Operadores suportados: <code>+</code> <code>-</code> <code>*</code> <code>/</code></li>
      <li>Digite <code>sair</code> para encerrar.</li>
    </ul>
  </li>
  <li><b>Para executar a interface web (Flask):</b>
    <pre><code>python -m src.app</code></pre>
    <ul>
      <li>Acesse <a href="http://localhost:5000" target="_blank">http://localhost:5000</a> no navegador.</li>
    </ul>
  </li>
  <li><b>Para rodar os testes:</b>
    <pre><code>python -m pytest</code></pre>
  </li>
</ol>
<!-- Fim da seção de como utilizar -->

---

<!-- Início da seção de funcionalidades -->
<h2>⚙️ Funcionalidades:</h2>
<ul>
  <li><b>Operações:</b> Adição, subtração, multiplicação e divisão.</li>
  <li><b>Histórico:</b> Exibe todas as operações realizadas.</li>
  <li><b>Pilha de resultados:</b> Armazena e exibe os resultados de cada cálculo.</li>
  <li><b>Interface Web:</b> Use a calculadora pelo navegador com Flask.</li>
  <li><b>Testes automatizados:</b> Cobertura de testes com Pytest.</li>
  <li><b>Tratamento de erros:</b> Mensagens claras para entradas inválidas e divisão por zero.</li>
</ul>
<!-- Fim da seção de funcionalidades -->

---

<!-- Início da seção de estrutura do projeto -->
<h2>📁 Estrutura do Projeto:</h2>

<pre>
calculadora-python
├── src
│   ├── main.py              # Ponto de entrada da aplicação CLI
│   ├── app.py               # Interface web com Flask
│   ├── calculadora.py       # Classe principal Calculadora
│   ├── operacoes.py         # Funções das operações aritméticas
│   └── stack.py             # Implementação da classe Stack para resultados
├── tests
│   ├── test_calculadora.py  # Testes unitários da classe Calculadora
│   └── test_operacoes.py    # Testes unitários das operações aritméticas
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
</pre>
<!-- Fim da seção de estrutura do projeto -->

---

<!-- Início da seção "Contato" -->
<h2>🌐 Contato:</h2>
<p>
<a href="https://www.linkedin.com/in/niwanbatista/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" target="_blank" height=25> </a>
<a href="https://api.whatsapp.com/send?phone=5511991359164" target="_blank"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" target="_blank" height=25></a>
<a href="https://www.instagram.com/niwanbatista/"><img src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white" target="_blank" height=25></a> 
<a href="https://github.com/niwanbernardo" target="_blank"><img alt="Github" src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white" target="_blank" height=25 /></a>
</p>
<!-- Fim da seção "Contato" -->

---

<!-- Início da seção de licença -->
<h2>⚖️ Licença (MIT):</h2>
<p> Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo, modificá-lo e compartilhá-lo.</p>
<!-- Fim da seção de licença -->

---

<!-- Início da seção "Finalização" -->
<div align="center">
  <p>Feito com ❤️ por <b>Niwan Bernardo</b>.</p>
  <p>Deixe uma ⭐ no projeto se foi útil para você.</p>
</div>
<!-- Fim da seção "Finalização" -->
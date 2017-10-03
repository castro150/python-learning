# Boa prática no python: não usar o python local para rodar, porque tem dependências de outros
# projetos instaladas. Para isso, baixar a dependência virtualenv para virtualizar o python e
# usar no Heroku por exemplo, para isso é criada a pasta 'virtual' no projeto, com o comando
# 'virtualenv virtual', uma instalação isolada do python em 'virtual/bin/python'.
# IMPORTANTE: para instalar, usar o 'conda install venv'

# Para criar o requirements.txt: ../virtual/bin/pip freeze > requirements.txt
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_endpoint():
    return render_template('home.html')


@app.route('/about')
def about_endpoint():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

import requests
import json
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)


class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario

    def request_api(self):
        # Fazendo requisição usando a API Rest pública do GITHUB.
        self.resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos?per_page=1000')
        if self.resposta.status_code == 200:
            return self.resposta.json()
        else:
            return False

    def get_repo(self):
        # Selecionando informações a serem trabalhadas e organizando em JSON.

        dados_api = self.request_api()
        if dados_api == False:
            print(f'API falhou ou chegou ao limite. Usando arquivo JSON agora. {self.resposta.status_code}')
            with open("data.json", encoding='utf-8') as meu_json:
                dados_api = json.load(meu_json)
        else:
            save(dados_api)

        dados = []
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                name = dados_api[i]['name']
                url = dados_api[i]['svn_url']
                description = dados_api[i]['description']
                archived = dados_api[i]['archived']
                language = dados_api[i]['language']
                fork = dados_api[i]['fork']
                created_at = datetime.strptime(
                    dados_api[i]['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                updated_at = datetime.strptime(
                    dados_api[i]['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
                pushed_at = datetime.strptime(
                    dados_api[i]['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")
                edit = {'name': name, 'url': url, 'description': description, 'archived': archived,
                        'language': language, 'fork': fork, 'created_at': created_at, 'updated_at': updated_at, 'pushed_at': pushed_at}
                dados.append(edit)
            return {'dados': dados}
        else:
            print(dados_api)

    def print_repo(self):
        dados_api = self.request_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                repo = dados_api[i]['name']
                url = dados_api[i]['svn_url']
                archived = dados_api[i]['archived']
                language = dados_api[i]['language']
                fork = dados_api[i]['fork']
                print(
                    f"{repo} - {url} - {archived} - {language} - {fork}")
        else:
            print(dados_api)


def save(data, name='data.json'):
    # Salvando dados em JSON apenas para visualisar a resposta do resquest de forma organizada.
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_language(requisicao, language):
    # Retornando repositorios que usam a linguagem escolhida.
    if language == "None" or language == None:
        return requisicao
    else:
        return [x for x in requisicao if str(x['language']).lower() == str(language).lower()]


def get_fork(self, requisicao, fork):
    # Retornando repositorios que são forks.
    if fork == "None" or fork == None:
        return requisicao
    else:
        return [x for x in requisicao if x['fork'] is True]


def get_archived(self, requisicao, archived):
    # Retornando repositorios que são archived.
    if archived == "None" or archived == None:
        return requisicao
    else:
        return [x for x in archived if x['archived'] is True]


def get_type(requisicao, type):
    if type == 'archived':
        return [x for x in requisicao if x['archived'] == True]
    elif type == 'fork':
        return [x for x in requisicao if x['fork'] == True]
    else:
        return requisicao


def sort_by(requisicao, sort):
    if sort == 'last_update':
        requisicao.sort(key=lambda date: date['pushed_at'], reverse=True)
        return requisicao
    else:
        requisicao.sort(key=lambda name: str(name['name']).lower())
        return requisicao


def find_text_repositori(requisicao, text):
    if text == "None" or text == None:
        return requisicao
    else:
        return [x for x in requisicao if str(text).lower() in str(x['name']).lower()]


repositorios = ListaDeRepositorios('BenitoMarculanoRibeiro')


@app.route('/')
def index():
    data = repositorios.get_repo()['dados']
    name_repositori = request.args.get('name_repositori')
    type = request.args.get('type')
    language = request.args.get('language')
    sort = request.args.get('sort')
    posts = sort_by(find_text_repositori(
        get_type(get_language(data, language), type), name_repositori), sort)
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

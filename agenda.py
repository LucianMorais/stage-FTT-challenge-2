class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

    def exibir_informacoes(self):
        print("\nInformações do Personagem:")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Link da Imagem: {self.link_imagem}")
        print(f"Programa: {self.programa}")
        print(f"Animador: {self.animador}")


def main():
    personagem1 = Personagem("Athur", "Personagem engraçado", "link_imagem_arthur.jpg", "ToonBoom", "Maria")
    personagem2 = Personagem("Maria", "Personagem aventureira", "link_imagem_maria.jpg", "Maya", "Arthur")

    personagem1.exibir_informacoes()
    personagem2.exibir_informacoes()

if __name__ == "__main__":
    main()


from flask import Flask, request, jsonify
from personagem import Personagem

app = Flask(__name__)
animacao_empresa = Animacao()

@app.route('/characters/', methods=['POST'])
def criar_personagem():
    data = request.json

    nome = data.get('nome')
    descricao = data.get('descricao')
    link_imagem = data.get('link_imagem')
    programa = data.get('programa')
    animador = data.get('animador')

    animacao_empresa.criar_personagem(nome, descricao, link_imagem, programa, animador)

    return jsonify({"mensagem": "Personagem criado com sucesso!"}), 201

@app.route('/characters/', methods=['GET'])
def listar_personagens():
    personagens = animacao_empresa.personagens
    return jsonify({"personagens": personagens})

if __name__ == '__main__':
    app.run(debug=True)

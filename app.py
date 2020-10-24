from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Pessoa(db.Model):
    tablename = 'cliente'
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    cpf = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf 
        self.email = email

db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")

        if nome and telefone and cpf and email:
            p = Pessoa(nome, telefone, cpf, email)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("index"))

@app.route("/lista")
def listar():
    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas=pessoas)

@app.route("/apagar/<int:id>")
def apagar_id(id):
    pessoa = Pessoa.query.filter_by(id=id).first()
    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas=pessoas)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    pessoa = Pessoa.query.filter_by(id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")

        if nome and telefone and cpf and email:
            pessoa.nome = nome
            pessoa.telefone = telefone
            pessoa.cpf = cpf
            pessoa.email = email

            db.session.commit()

            return redirect(url_for("listar"))

    return render_template("atualizar.html", pessoa=pessoa)


if __name__ == '__main__':
    app.run(debug = True)
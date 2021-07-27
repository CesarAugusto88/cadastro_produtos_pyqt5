from PyQt5 import uic, QtWidgets
import mysql.connector
# import re
from decouple import config


banco = mysql.connector.connect(
    host= config("HOST"),
    user=  config("DB_USER"),
    passwd=  config("DB_KEY"),
    database= config("DB")
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""
    if formulario.radioButton.isChecked():
        categoria = "Informatica"
    elif formulario.radioButton_2.isChecked():
        categoria = "Alimentos"
    else:
        categoria = "Eletronicos"

    print("Código: ", linha1)
    print("Descrição: ", linha2)
    print("Preço: ", linha3)

    linha3 = linha3.replace(",",".")
    # linha3 = re.sub(r"^\s+|\s+$", "", desc)

    cursor = banco.cursor()
    comando_SQL = """INSERT INTO produtos (codigo,descricao,preco,
                    categoria) VALUES (%s,%s,%s,%s)"""
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def chama_segunda_tela():
    segunda_tela.show()


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")  # Declarada antes

formulario.pushButton.clicked.connect(funcao_principal)
# Chamado função que mostra a segunda tela a partir do botão do primeiro formulário
formulario.pushButton_2.clicked.connect(chama_segunda_tela)

formulario.show()
app.exec()

""" Shift + Alt + A
create table produtos (
    -> id INT NOT NULL AUTO_INCREMENT,
    -> codigo INT,
    -> descricao VARCHAR(50),
    -> preco DOUBLE,
    -> categoria VARCHAR(20),
    -> PRIMARY KEY (id)
    -> );
    
INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"""
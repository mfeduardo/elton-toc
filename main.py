#####################################
# Elton TOC (versão 1.0)
# Desenvolvido por Eduardo Filgueiras
#####################################

from PyQt6 import QtWidgets, uic
import clipboard

def split():
    texto = main.input_texto.toPlainText()
    resultado = ' '.join(texto.split())
    main.input_texto.setText(resultado)
  

def reset():
    main.input_texto.setText('')


def copiar():
    clipboard.copy(main.input_texto.toPlainText())


app = QtWidgets.QApplication([])

# main
main = uic.loadUi('ui/main.ui')

main.bt_split.clicked.connect(split)
main.bt_copiar.clicked.connect(copiar)
main.bt_reset.clicked.connect(reset)

main.show()

app.exec()

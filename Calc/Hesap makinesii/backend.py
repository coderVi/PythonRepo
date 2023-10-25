import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class CalculatorApp(QMainWindow):
    try:
        def __init__(self):
            super().__init__()
            loadUi('calc.ui', self)

            self.txt_giris.setText("")
            self.operand1 = 0 
            self.operator = None
            self.pending_operand = False

            # Sayı tuşlarına tıklama olayları
            self.bir.clicked.connect(lambda: self.append_number(1))
            self.iki.clicked.connect(lambda: self.append_number(2))
            self.uc.clicked.connect(lambda: self.append_number(3))
            self.dort.clicked.connect(lambda: self.append_number(4))
            self.bes.clicked.connect(lambda: self.append_number(5))
            self.alti.clicked.connect(lambda: self.append_number(6))
            self.yedi.clicked.connect(lambda: self.append_number(7))
            self.sekiz.clicked.connect(lambda: self.append_number(8))
            self.dokuz.clicked.connect(lambda: self.append_number(9))
            self.sifir.clicked.connect(lambda: self.append_number(0))

            # İşlem tuşlarına tıklama olayları
            self.topla.clicked.connect(lambda: self.set_operator("+"))
            self.cikarma.clicked.connect(lambda: self.set_operator("-"))
            self.carpma.clicked.connect(lambda: self.set_operator("*"))
            self.bolme.clicked.connect(lambda: self.set_operator("/"))

            # Eşittir tuşuna tıklama olayı
            self.esittir.clicked.connect(self.calculate)

            # Temizle ve nokta tuşlarına tıklama olayları
            self.temizle.clicked.connect(self.clear)
            self.virgul.clicked.connect(self.append_decimal)

        def append_number(self, number):
            current_text = self.txt_giris.text()
            
            new_text = current_text + str(number)
            self.txt_giris.setText(new_text)

        def set_operator(self, operator):
            if not self.pending_operand:
                self.operand1 = float(self.txt_giris.text())
                self.operator = operator
                self.txt_giris.setText("")
                self.pending_operand = True

        def calculate(self):
            if self.pending_operand:
                operand2 = float(self.txt_giris.text())
                if self.operator == "+":
                    result = self.operand1 + operand2
                elif self.operator == "-":
                    result = self.operand1 - operand2
                elif self.operator == "*":
                    result = self.operand1 * operand2
                elif self.operator == "/":
                    if operand2 == 0:
                        result = "Hata"
                    else:
                        result = self.operand1 / operand2

                self.txt_giris.setText(str(result))
                self.pending_operand = False

        def clear(self):
            self.txt_giris.setText("")
            self.operand1 = 0
            self.operator = None
            self.pending_operand = False

        def append_decimal(self):
            current_text = self.txt_giris.text()
            if "." not in current_text:
                new_text = current_text + "."
                self.txt_giris.setText(new_text)
    
    except:
        print("Hatalı Giriş!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())

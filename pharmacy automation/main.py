from PyQt6.QtWidgets import QApplication
# Programın ilk açılış formunu tanımladık
from giris import Form_Giris

app = QApplication([])
acilisPenceresi = Form_Giris()
acilisPenceresi.show()
app.exec()
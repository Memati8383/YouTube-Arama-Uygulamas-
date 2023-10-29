import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class YouTubeAramaUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YouTube Arama Uygulaması')
        self.setGeometry(100, 100, 400, 250)
        self.setWindowIcon(QIcon('youtube_icon.png'))

        main_layout = QVBoxLayout()

        header_layout = QVBoxLayout()
        header_layout.setAlignment(Qt.AlignCenter)

        header_label = QLabel(self)
        header_label.setText("YouTube Arama")
        header_label.setFont(QFont("Arial", 18, QFont.Bold))
        header_layout.addWidget(header_label)

        main_layout.addLayout(header_layout)

        input_layout = QVBoxLayout()

        input_label = QLabel(self)
        input_label.setText("Arama sorgusu:")
        input_label.setFont(QFont("Arial", 14))

        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("Arama sorgusu")
        self.entry.setFont(QFont("Arial", 12))
        self.entry.setStyleSheet("padding: 5px; border: 2px solid #FF0000; border-radius: 5px;")

        input_layout.addWidget(input_label)
        input_layout.addWidget(self.entry)

        main_layout.addLayout(input_layout)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        self.arama_dugmesi = QPushButton('🔍 Ara', self)
        self.arama_dugmesi.clicked.connect(self.youtube_arama_yap)
        self.arama_dugmesi.setStyleSheet("background-color: #FF0000; color: white; border: none; padding: 10px 20px; font-weight: bold;")

        kilavuz_dugmesi = QPushButton('📚 Kılavuz', self)
        kilavuz_dugmesi.clicked.connect(self.kilavuz_goster)
        kilavuz_dugmesi.setStyleSheet("background-color: orange; color: white; border: none; padding: 10px 20px; font-weight: bold;")

        discord_dugmesi = QPushButton('🎮 Discord', self)
        discord_dugmesi.clicked.connect(self.discord_ac)
        discord_dugmesi.setStyleSheet("background-color: #7289da; color: white; border: none; padding: 10px 20px; font-weight: bold;")

        cikis_dugmesi = QPushButton('🚪 Çık', self)
        cikis_dugmesi.clicked.connect(self.cikis_yap)
        cikis_dugmesi.setStyleSheet("background-color: red; color: white; border: none; padding: 10px 20px; font-weight: bold;")

        button_layout.addWidget(self.arama_dugmesi)
        button_layout.addWidget(kilavuz_dugmesi)
        button_layout.addWidget(discord_dugmesi)
        button_layout.addWidget(cikis_dugmesi)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def youtube_arama_yap(self):
        arama_sorgusu = self.entry.text()

        if arama_sorgusu:
            try:
                webbrowser.open(f"https://www.youtube.com/results?search_query={arama_sorgusu}")
            except Exception as e:
                print("Bir hata oluştu.")
        else:
            print("Lütfen bir arama sorgusu girin.")

    def kilavuz_goster(self):
        kilavuz_mesaji = (
            "<html><body>"
            "<p style='font-size: 14px; font-family: Arial;'>"
            "<strong>YouTube Arama Uygulaması Kılavuzu</strong><br><br>"
            "Arama yapmak için şu adımları izleyin:<br><br>"
            "1. 'Arama sorgusu' alanına aramak istediğiniz kelime veya terimi yazın.<br>"
            "   Örnek: 'Python programlama', 'Python tutorial' vb.<br><br>"
            "2. '🔍 Ara' düğmesine tıklayın. Bu, tarayıcınızda YouTube arama sonuçlarını açacaktır.<br><br>"
            "Daha fazla yardım veya geri bildirim için lütfen aşağıdaki websitem ile iletişime geçin:<br>"
            "<a href='http://akdemirferit.rf.gd' style='color: #FF0000; text-decoration: none;'>akdemirferit.rf.gd</a>"
            "</p></body></html>"
        )

        kilavuz_mesaji_penceresi = QMessageBox(self)
        kilavuz_mesaji_penceresi.setWindowTitle("Kılavuz")
        kilavuz_mesaji_penceresi.setIcon(QMessageBox.Information)
        kilavuz_mesaji_penceresi.setTextFormat(Qt.RichText)  # HTML etiketlerini desteklemek için Qt.RichText kullanın
        kilavuz_mesaji_penceresi.setText(kilavuz_mesaji)

        kilavuz_mesaji_penceresi.exec_()

    def discord_ac(self):
        webbrowser.open("https://discord.com")

    def cikis_yap(self):
        print('Çıkış butonuna tıklandı.')
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uygulama = YouTubeAramaUygulamasi()
    uygulama.show()
    sys.exit(app.exec_())

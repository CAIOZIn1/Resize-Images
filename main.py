import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from ProjetoUi.design import *


class Resize_images(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.btn_choice_file.clicked.connect(self.open_image)
        self.btn_resize.clicked.connect(self.resize_image)
        self.btn_save.clicked.connect(self.save_image)

    def open_image(self) -> None:
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r''
        )

        self.input_file.setText(image)
        self.original_image = QPixmap(image)
        self.label_image.setPixmap(self.original_image)

        self.input_width.setText(str(self.original_image.width()))
        self.input_heigth.setText(str(self.original_image.height()))

    def resize_image(self) -> None:
        largura = int(self.input_width.text())
        self.new_image = self.original_image.scaledToWidth(largura)
        self.label_image.setPixmap(self.new_image)

        self.input_width.setText(str(self.new_image.width()))
        self.input_heigth.setText(str(self.new_image.height()))

    def save_image(self) -> None:
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Abrir imagem',
            r'',
        )
        self.new_image.save(image, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resize_images = Resize_images()
    resize_images.show()
    qt.exec_()

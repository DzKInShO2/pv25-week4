import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QFormLayout,
    QWidget,
    QComboBox,
    QPushButton,
    QLineEdit,
    QListWidget,
    QLabel,
)


class MynApp(QWidget):
    def __init__(self):
        super().__init__()

        self.products = {
            "": 0,
            "Bimoli (Rp. 20,000)": 20_000,
            "Beras 5 Kg (Rp. 75,000)": 75_000,
            "Kecap ABC (Rp. 7,000)": 7_000,
            "Saos Saset (Rp. 2,500)": 2_500
        }

        self.discounts = {
            "0%":  0.00,
            "5%":  0.05,
            "10%": 0.10,
            "15%": 0.15
        }

        self.__init_components()

    def __init_components(self):
        self.setWindowTitle("POS Application")
        self.setFixedSize(480, 360)

        root_layout = QVBoxLayout()

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.product_selection = QComboBox()
        self.product_selection.addItems(self.products.keys())
        self.product_selection.setFixedWidth(164)

        self.product_quantity = QLineEdit()
        self.product_quantity.setFixedWidth(148)

        self.discount_selection = QComboBox()
        self.discount_selection.addItems(self.discounts.keys())
        self.discount_selection.setFixedWidth(56)

        self.add_button = QPushButton("Add to Cart")
        self.add_button.clicked.connect(self.__add_item_to_list)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.__clear_item_list)
        self.clear_button.setFixedWidth(64)

        form_layout.addRow(QLabel("Product"), self.product_selection)
        form_layout.addRow(QLabel("Quantity"), self.product_quantity)
        form_layout.addRow(QLabel("Discount"), self.discount_selection)
        form_layout.addRow(self.add_button, self.clear_button)

        self.item_list = QListWidget()
        self.total_number = 0
        self.total_label = QLabel(f"Total: Rp. {self.total_number}")

        root_layout.addLayout(form_layout, 3)
        root_layout.addWidget(self.item_list, 6)
        root_layout.addWidget(self.total_label, 1)

        self.setLayout(root_layout)

    def __add_item_to_list(self):
        selected = self.product_selection.currentText()
        quantity = int(self.product_quantity.text())
        discount = self.discount_selection.currentText()

        text = f"{selected} - {quantity} "
        text += f"x Rp. {self.products[selected]:,} (disc {discount})"
        self.item_list.addItem(text)

        price = self.products[selected] * quantity
        price -= price * self.discounts[discount]

        self.total_number += int(price)
        self.total_label.setText(f"Total: Rp. {self.total_number:,}")

    def __clear_item_list(self):
        self.item_list.clear()
        self.total_number = 0
        self.total_label.setText(f"Total: Rp. {self.total_number:,}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MynApp()
    win.show()

    sys.exit(app.exec())

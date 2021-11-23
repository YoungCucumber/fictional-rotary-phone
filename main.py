import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Table(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        QApplication.setStyle('Fusion')
        self.run()
        self.create_table()

    def create_table(self):
        self.tbl_wdt.setHorizontalHeaderLabels(['Название сорта', 'Степень обжарки', 'Молотый/В Зернах',
                                                'Описание вкуса', 'Цена в рублях', 'Объем в граммах'])
        self.tbl_wdt.resizeColumnsToContents()

    def run(self):
        self.fill_table(self.load_db())

    def load_db(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute("""SELECT name, roast, type, description, price, volume FROM data""").fetchall()
        return data

    def fill_table(self, data):
        self.tbl_wdt.setColumnCount(6)
        self.tbl_wdt.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(6):
                self.tbl_wdt.setItem(i, j, QTableWidgetItem(str(data[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())

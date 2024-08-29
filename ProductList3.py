import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# 데이터베이스 처리 클래스
class ProductDatabase:
    def __init__(self, db_name="ProductList.db"):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.initialize_database()

    def initialize_database(self):
        # 테이블이 없을 경우 생성
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )
        self.con.commit()

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id = ?;", (prod_id,))
        self.con.commit()

    def get_all_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# UI 클래스
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.db = db  # 데이터베이스 인스턴스
        self.init_ui()

    def init_ui(self):
        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        
        # 이벤트 연결
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 초기 데이터 로드
        self.getProduct()

    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.add_product(name, price)
        self.getProduct()

    def updateProduct(self):
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.update_product(prod_id, name, price)
        self.getProduct()

    def removeProduct(self):
        prod_id = self.prodID.text()
        self.db.remove_product(prod_id)
        self.getProduct()

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.db.get_all_products()
        
        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


# 인스턴스를 생성한다.
app = QApplication(sys.argv)
db = ProductDatabase()  # 데이터베이스 객체 생성
myWindow = Window(db)
myWindow.show()
app.exec_()

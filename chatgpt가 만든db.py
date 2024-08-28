import sqlite3
import random
import string

class ElectronicsDatabase:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id TEXT PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            ''')

    def insert_product(self, product_id, product_name, price):
        with self.conn:
            self.conn.execute('''
                INSERT INTO products (product_id, product_name, price)
                VALUES (?, ?, ?)
            ''', (product_id, product_name, price))

    def update_product(self, product_id, new_name=None, new_price=None):
        with self.conn:
            if new_name and new_price:
                self.conn.execute('''
                    UPDATE products
                    SET product_name = ?, price = ?
                    WHERE product_id = ?
                ''', (new_name, new_price, product_id))
            elif new_name:
                self.conn.execute('''
                    UPDATE products
                    SET product_name = ?
                    WHERE product_id = ?
                ''', (new_name, product_id))
            elif new_price:
                self.conn.execute('''
                    UPDATE products
                    SET price = ?
                    WHERE product_id = ?
                ''', (new_price, product_id))

    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute('''
                DELETE FROM products
                WHERE product_id = ?
            ''', (product_id,))

    def select_product(self, product_id=None):
        with self.conn:
            if product_id:
                cursor = self.conn.execute('''
                    SELECT * FROM products
                    WHERE product_id = ?
                ''', (product_id,))
            else:
                cursor = self.conn.execute('''
                    SELECT * FROM products
                ''')

            return cursor.fetchall()

    def generate_sample_data(self, num_samples=100):
        for _ in range(num_samples):
            product_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            product_name = 'Product ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            price = round(random.uniform(50, 1000), 2)
            self.insert_product(product_id, product_name, price)

    def close(self):
        self.conn.close()

# 사용 예시
db = ElectronicsDatabase()
db.generate_sample_data(100)  # 샘플 데이터 100개 생성

# 데이터 삽입
db.insert_product('P12345', 'Example Product', 299.99)

# 데이터 조회
products = db.select_product()
for product in products:
    print(product)

# 데이터 업데이트
db.update_product('P12345', new_name='Updated Product', new_price=349.99)

# 데이터 삭제
db.delete_product('P12345')

# DB 연결 종료
db.close()

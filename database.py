import mysql.connector
from os import system

system("clear")


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1029"
        )
        self.cursor = self.db.cursor()
        self.__setup()
    
    def __setup(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS AIRPORT;")
        self.cursor.execute("USE AIRPORT;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS TICKETS (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                FULLNAME VARCHAR(64) NOT NULL,
                PRICE FLOAT DEFAULT 0,
                STATUS BOOL DEFAULT FALSE,
                SEAT_NUMBER INT NOT NULL
            );
        """)


    def insert(self, FIO: str, price: float, status: bool, seat_number: int):
        self.cursor.execute(
            "INSERT INTO TICKETS VALUES (NULL, %s, %s, %s, %s);",
            (FIO, price, status, seat_number)
        )
        self.db.commit()


    def update (self, id: str, FIO: str = None, price: float = None, status: bool = None, seat_number: int = None):
        self.cursor.execute(
            """
                UPDATE TICKETS
                SET
                    FULLNAME = CASE 
                        WHEN %s IS NOT NULL THEN %s
                        ELSE FULLNAME
                    END,
                    PRICE = CASE
                        WHEN %s IS NOT NULL THEN %s
                        ELSE PRICE
                    END,
                    STATUS = CASE
                        WHEN %s IS NOT NULL THEN %s
                        ELSE STATUS
                    END,
                    SEAT_NUMBER = CASE
                        WHEN %s IS NOT NULL THEN %s
                        ELSE SEAT_NUMBER
                    END
                WHERE
                    ID = %s;
            """,
            (FIO, FIO, price, price, status, status, seat_number, seat_number, id)
        )
        self.db.commit()
        

    def select(self):
        self.cursor.execute("SELECT * FROM TICKETS;")
        tickets = self.cursor.fetchall()

        return tickets



database = Database()
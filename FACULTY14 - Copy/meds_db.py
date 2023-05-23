#meds database
import sqlite3


class Meds_Database:
    def __init__(self, meds_db):
        self.con = sqlite3.connect(meds_db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS meds(
            id Integer Primary Key,
            description text,
            name text,
            quantity integer
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insertMeds(self, description, name, quantity):
        self.cur.execute("INSERT into meds values (NULL,?,?,?)",
                         (description, name, quantity))
        self.con.commit()

    # Fetch All Data from DB
    def fetchMeds(self):
        self.cur.execute("SELECT * from meds")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE from meds where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def updateMeds(self, id, description, name, quantity):
        self.cur.execute(
            "UPDATE meds set description=?, name=?, quantity=? where id=?",
            (description, name, quantity, id))
        self.con.commit()


    def get_data(self):

        self.cur.execute("SELECT * from meds")
        self.cur.commit()
        totalMeds = self.cur.rowcount

        return totalMeds
          

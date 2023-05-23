#patient database
import sqlite3

class Patient_Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS patient(
            id Integer Primary Key,
            name text,
            address text,
            prevCheckup date,
            age text,
            contact text,
            martial text,
            height text, 
            weight text,
            pulse text,
            bodytemp text,
            home text,
            work text,
            fever text,
            cough text,
            colds text,
            diarrhea text, 
            sore_throat text,
            body_pain text,
            breathing text,
            high_hr text,
            stress text,
            alcohol text,
            fatigue text,
            palpitate text   
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, address, prevCheckup, age, contact, martial, height, weight, pulse, bodytemp, home, work, 
               fever,cough ,colds,diarrhea ,sore_throat,body_pain ,breathing,high_hr, stress, alcohol,
                fatigue, palpitate ):
        self.cur.execute("INSERT into patient values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (name, address , prevCheckup , age, contact, martial, height, weight, pulse, bodytemp,
                          home,work,fever,cough ,colds,diarrhea ,sore_throat, body_pain,breathing, 
                          high_hr, stress, alcohol, fatigue, palpitate))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from patient")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from patient where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, address , prevCheckup , age, contact, martial, height, weight, pulse, bodytemp):
        self.cur.execute(
            "update patient set name=?, address=?, prevCheckup=?, age=?, contact=?, martial=?, height=?, weight=?, pulse=?, bodytemp=? where id=?",
            (name,address, prevCheckup, age, contact, martial, height, weight, pulse, bodytemp, id))
        self.con.commit()

    # Update Meds Record in DB
    def updateMeds(self, id, home, work, fever,cough ,colds,diarrhea ,sore_throat, body_pain, breathing, high_hr, stress, alcohol, fatigue, palpitate  ):
        self.cur.execute( 
            "update patient set home=?, work=?,fever=?,cough=? ,colds=?,diarrhea=? ,sore_throat=?, body_pain=?,breathing=?, high_hr=?, stress=?, alcohol=?, fatigue=?, palpitate=? where id=?",
            (home, work, fever,cough ,colds,diarrhea ,sore_throat, body_pain,breathing, high_hr, stress, alcohol, fatigue, palpitate, id))
        self.con.commit()


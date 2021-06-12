from src.config.db import DB
from datetime import datetime, date, time, timedelta

class Semestres():
    def Listado(self):
        cursor = DB.cursor()
        sql = """select * from semestres """
        cursor.execute(sql)
        semestres = cursor.fetchall()
        return semestres

    def insertSemestre(self,nombre):
        cursor = DB.cursor()
        cursor.execute("""insert into semestres(
                nom_se
            )values (?)
        """, (nombre,))
        DB.commit()
        cursor.close()

    def semestre(self,id):
        cursor = DB.cursor()
        cursor.execute(""" select semestre from  sesion
        where id_se = ? """,(id,))
        semestre = cursor.fetchone()
     
        return semestre
  
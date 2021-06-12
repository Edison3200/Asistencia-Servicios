from src.config.db import DB
from datetime import datetime, date, time, timedelta

class RegistroUsu():
    def insertarUsu(self,iden,nombre,apellidos,celular,email,semestre):
        cursor = DB.cursor()
        cursor.execute("""insert into estudiantes(
                iden,
                nom_es,
                apellidos,
                celular,
                email,
                semestre
            )values (?,?,?,?,?,?)
        """, (iden,nombre,apellidos,celular, email,semestre))
        DB.commit()
        cursor.close()
    
    def Listado(self):
        cursor = DB.cursor()
        sql = """select * from estudiantes """
        cursor.execute(sql)
        estudiantes = cursor.fetchall()
        return estudiantes

    def EliminarEstu(self,id):
        cursor = DB.cursor()
        cursor.execute(""" Delete FROM estudiantes Where id_es = ? """, (id,))
        DB.commit()
        cursor.close()

    def ActualizarEstu(self,iden,nombre,apellidos,celular,email,semestre,id):
        cursor = DB.cursor()
        cursor.execute(""" update estudiantes set iden = ? , nom_es = ? , apellidos = ? , celular = ? , email = ?, semestre = ? where id_es = ? """,(iden,nombre,apellidos,celular, email,semestre,id,))
        DB.commit()
        cursor.close()

    def Estudiante(self,id):
        cursor = DB.cursor()
        cursor.execute(""" select * from estudiantes 
        where id_es = ? """,(id,))
        usuario = cursor.fetchone()
     
        return usuario





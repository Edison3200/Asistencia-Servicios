from src.config.db import DB
from datetime import datetime, date, time, timedelta

class Sesiones():
    
    def Listado(self):
        cursor = DB.cursor()
        sql = """select * from sesion , semestres where  semestres.id_se = sesion.semestre  """
        cursor.execute(sql)
        sesiones = cursor.fetchall()
        return sesiones

    def insertSesion(self,nombre,descripcion,semestre,fecha,horai,horaf):
        cursor = DB.cursor()
        cursor.execute("""insert into sesion(
                nom,
                descripcion,
                semestre,
                fecha_ini,
                hora_ini,
                hora_fin
            )values (?,?,?,?,?,?)
        """, (nombre,descripcion,semestre,fecha,horai,horaf))
        DB.commit()
        cursor.close()

    def EliminarSesion(self,id):
        cursor = DB.cursor()
        cursor.execute(""" Delete FROM sesion  where sesion.id_se = ?""", (id,))
        DB.commit()
        cursor.close()
    
    def ListadoSesion(self,id):
        cursor = DB.cursor()
        cursor.execute(""" select * from estudiantes 
        where semestre = ? """,(id,))
        estudiantes = cursor.fetchall()
        return estudiantes
    def SesionIni(self,id):
        cursor = DB.cursor()
        cursor.execute(""" select * from sesion , semestres
         where  semestres.id_se = sesion.semestre and sesion.id_se = ? """,(id,))
        sesion = cursor.fetchone()
     
        return sesion
    def SesionActiva(self,id):#estudiantes que iniciaron sesion
        cursor = DB.cursor()
        cursor.execute(""" select id_es from sesion_es
        where id_se = ? """,(id,))
        estudiantes = cursor.fetchall()
        return estudiantes
    def AgregarEstSesion(self,sesion,estu):
        cursor = DB.cursor()
        cursor.execute("""insert into sesion_es(
                id_se,
                id_es
            )values (?,?)
        """, (sesion,estu,))
        DB.commit()
        cursor.close()
    def EliminarEstSesion(self,sesion,estu):
        cursor = DB.cursor()
        cursor.execute(""" Delete FROM sesion_es Where id_se = ? and id_es = ? """, (sesion,estu,))
        DB.commit()
        cursor.close()

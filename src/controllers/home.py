from flask import json, render_template, request, redirect, url_for, flash,jsonify
from src import app
from src.models.sesiones import Sesiones
from src.models.estudiantes import RegistroUsu
from src.models.semestres import Semestres


app.secret_key ='spbYO0JJ0PUFLUikKYbKrpS5w3KUEnab5KcYDdYb'

@app.route('/', methods =['GET'])
def index():
   return jsonify({"response":"Bienvenido"})

#RUTAS DE SESIONES
@app.route('/sesion', methods =['GET','POST'])
def sesion():
   if request.method == 'GET': #Listado de sesiones
       sesiones = Sesiones()
       sesiones = sesiones.Listado()
       
       for i in range(0,len(sesiones)):
         sesiones[i]=list(sesiones[i])
         sesiones[i][4]=json.dumps(sesiones[i][4], indent=4, sort_keys=True, default=str)
         sesiones[i][5]=json.dumps(sesiones[i][5], indent=4, sort_keys=True, default=str)
         sesiones[i][6]=json.dumps(sesiones[i][6], indent=4, sort_keys=True, default=str)
       
       return jsonify({"sesiones":sesiones,"message":"Listado de sesiones"})

   if request.method == 'POST':#Agregar una sesion
      data = request.get_json()
      nombre = data['nombre']
      descripcion = data['descripcion']
      semestre = data['semestres']
      fecha = data['fecha']
      horai = data['horai']
      horaf = data['horaf']
      
      new_ses = Sesiones()
      new_ses =new_ses.insertSesion(nombre,descripcion,semestre,fecha,horai,horaf)
      
      if new_ses is None:
         result={
            "sesion":nombre,
            "fecha:":fecha,
            "message":"La sesion se creo con exito"
         }
         return jsonify(result)

      return jsonify(new_ses)
 
@app.route('/sesion/<int:id>', methods =['GET','PUT','DELETE'])   
def guardar_sesion(id):#id de sesion
    
    if request.method == 'GET':

       semestre = Semestres()
       semestre = semestre.semestre(id) #id de semestre
       
       sesion = Sesiones()
       datos = sesion.SesionIni(id)  
       
       datos=list(datos)
       datos[4]=json.dumps(datos[4], indent=4, sort_keys=True, default=str)
       datos[5]=json.dumps(datos[5], indent=4, sort_keys=True, default=str)
       datos[6]=json.dumps(datos[6], indent=4, sort_keys=True, default=str)


       aux =[]#se almacena los activos
       activos = sesion.SesionActiva(id) #lista de estudiantes en tabla sesion_es(estudiantes activos)
       for i in range(0,len(activos)):
            aux.append(activos[i][0])
       estudiantes = Sesiones()
       estudiantes = estudiantes.ListadoSesion(semestre[0])#Listado de estudiante de un semestre
      
       result={
            "sesion":datos,
            "activos":aux,
            "message":"informacion de sesion y listado de estudiantes activos"
         }
       return jsonify(result)


    if request.method == 'PUT':#Guardar estudiantes activos en sesion
       data = request.get_json()

       semestre = Semestres()
       semestre = semestre.semestre(id) #id de semestre -se envia id de sesion

       estudiantes = Sesiones()
       estudiantes = estudiantes.ListadoSesion(semestre[0])#Listado de estudiantes de un semestre

       lista_activos = Sesiones()#lista de estudiantes ya activos en base de datos
       lista_activos = lista_activos.SesionActiva(id)

       ssesion = Sesiones()

       lista_estudiantes_activos = []
       lista_estudiantes_desac=[]

       result = False

       for i in range(0,len(estudiantes)):
         if str(estudiantes[i][0]) in data:
      
            lista_estudiantes_activos.append(estudiantes[i][0])
         else:
            lista_estudiantes_desac.append(estudiantes[i][0])
       for i in range(0,len(estudiantes)):
          ssesion.EliminarEstSesion(id,estudiantes[i][0])
       for i in range (0,len(lista_estudiantes_activos)):
          ssesion.AgregarEstSesion(id,lista_estudiantes_activos[i])
          result = True
       
       if result is True:
            result={
               "Estudiantes":lista_estudiantes_activos,
               "message":"Los estudiantes fueron guardados en asistencia"
            }
            return jsonify(result)
         
       return jsonify({"menssage":"No se logro actualizar la lista"})
       

    if request.method == 'DELETE':
         
         session = Sesiones()
         session = session.EliminarSesion(id)
         if session is None:
            result={
               "sesion":id,
               "message":"La sesion fue eliminada"
            }
            return jsonify(result)
        
         return jsonify(session)
     
        

#RUTAS DE ESTUDIANTE
@app.route('/estudiante', methods=['GET', 'POST'])  
def estudiante():
   if request.method == 'GET':#Listado de estudiantes

      estudiantes = RegistroUsu()
      estudiantes = estudiantes.Listado()

      return jsonify({"estudiantes":estudiantes,"message":"Listado de estudiantes"})
   
   if request.method == 'POST':#Agregar un nuevo estudiante

      data = request.get_json()

      iden = data['identificacion']
      nombre = data['nombres']
      apellidos = data['apellidos']
      celular = data['celular']
      email = data['email']
      semestre = data['semestres']

      new_es = RegistroUsu()
      new_es =new_es.insertarUsu(iden,nombre,apellidos,celular,email,semestre)
      
      if new_es is None:
         result={
            "estudiante":nombre+" "+apellidos,
            "message":"El estudiante fue agregado"
         }
         return jsonify(result)
      
      return jsonify(new_es)

@app.route('/estudiante/<int:id>', methods=['GET','PUT', 'DELETE'])  
def admin_estudiante(id):
   if request.method == 'GET':#Encontrar 1 estudiante por su id
      estudiante = RegistroUsu()
      estudiante = estudiante.Estudiante(id)

      return jsonify({"estudiante":estudiante,"message":"Estudiante Encontrado"})

   if request.method == 'PUT':#Actualizar un estudiante
        
      data = request.get_json()

      iden = data['identificacion']
      nombre = data['nombres']
      apellidos = data['apellidos']
      celular = data['celular']
      email = data['email']
      semestre = data['semestres']

      edit_es = RegistroUsu()
      edit_es =edit_es.ActualizarEstu(iden,nombre,apellidos,celular,email,semestre,id)
      
      if edit_es is None:
         result={
            "estudiante":nombre+" "+apellidos,
            "message":"La informacion del estudiante fue actualizada"
         }
         return jsonify(result)

      return jsonify(edit_es)

   if request.method == 'DELETE':#Eliminar un estudiante
     
      estudiante = RegistroUsu()
      estudiante = estudiante.EliminarEstu(id)
      if estudiante is None:
            result={
               "message":"El estudiante fue eliminado"
            }
            return jsonify(result)
      return jsonify(estudiante)

#RUTA DE SEMESTRE
@app.route('/semestre', methods=['GET', 'POST'])  
def semestre():
   if request.method == 'GET':#listado de semestres
      semestres = Semestres()
      semestres = semestres.Listado()
      return jsonify({"semestres":semestres,"message":"Listado de Semestre"})

   if request.method == 'POST':#Agregar un semestre
      data = request.get_json()
      nombre = data['nombre']

      new_semes = Semestres()
      new_semes = new_semes.insertSemestre(nombre)
    
      if new_semes is None:
         result={
            "semestre":nombre,
            "message":"El semestre fue agregado"
         }
         return jsonify(result)
     
      return jsonify(new_semes)
      
     
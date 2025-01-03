from django.shortcuts import render,redirect

# Create your views here.
from.models import Usuario, Habito, Progreso, Notificacion, Meta

from django.contrib import messages

from datetime import datetime, timedelta

from django.utils.timezone import now



def inicio(request):
    return render(request,'inicio.html')

def nuevousuario(request):
    return render(request,'nuevousuario.html')

#Presentando en pantalla el listado de Estudiantes
def listadousuario(request):
    estudiantesBdd=Usuario.objects.all()
    return render(request,'listadousuario.html',{'usuarios':estudiantesBdd})


#Capturando datos del formulario e insertando en la Bdd
def guardarusuario(request):
    nombre=request.POST['txt_nombre']
    correo=request.POST['txt_correo']
    nuevousu=Usuario.objects.create(nombre=nombre,correo=correo)
    messages.success(request,"usuario guardado")#mensajes temporales
    return redirect('/listadousuario')


def eliminarusuario(request,id):
    estudiantesBdd=Usuario.objects.get(id=id)
    estudiantesBdd.delete()
    messages.success(request,"eliminar usuario")#mensajes temporales
    return redirect('/listadousuario')


def editarusuario(request,id):
    estudiantesBdd=Usuario.objects.get(id=id)
    return render(request,'editarusuario.html',{'usuarios':estudiantesBdd})





def procesareditarusuario(request):
    cam=Usuario.objects.get(id=request.POST['id'])
    cam.nombre=request.POST['txt_nombre']
    cam.correo=request.POST['txt_correo']
    cam.save()
    messages.success(request,"Usuario editado exitosamente")#mensajes temporales
    return redirect('/listadousuario')




#-------------------------------------habito

def nuevohabito(request):
    usuarios = Usuario.objects.all()
    return render(request, 'nuevohabito.html', {'usuarios': usuarios})


def listadohabito(request):
    habitosBdd = Habito.objects.all()
    return render(request, 'listadohabito.html', {'habitos': habitosBdd})



def guardarhabito(request):
    nombre_habito = request.POST['txt_nombre_habito']
    descripcion = request.POST['txt_descripcion']
    meta_diaria = request.POST['txt_meta_diaria']
    usuario_id = request.POST['usuario_id']
    usuario = Usuario.objects.get(id=usuario_id)
    nuevo_habito = Habito.objects.create(
        nombre_habito=nombre_habito,
        descripcion=descripcion,
        meta_diaria=meta_diaria,
        usuario=usuario
    )
    messages.success(request,"habito guardado")#mensajes temporales
    return redirect('/listadohabito')





def eliminarhabito(request, id):
    habitoBdd = Habito.objects.get(idhabito=id)
    habitoBdd.delete()
    messages.success(request,"habito eliminado")#mensajes temporales
    return redirect('/listadohabito')


def editarhabito(request, id):
    habitoBdd = Habito.objects.get(idhabito=id)
    usuarios = Usuario.objects.all()
    return render(request, 'editarhabito.html', {'habito': habitoBdd, 'usuarios': usuarios})


def procesareditarhabito(request):
    habito = Habito.objects.get(idhabito=request.POST['id'])
    habito.nombre_habito = request.POST['txt_nombre_habito']
    habito.descripcion = request.POST['txt_descripcion']
    habito.meta_diaria = request.POST['txt_meta_diaria']
    habito.usuario = Usuario.objects.get(id=request.POST['usuario_id'])
    habito.save()
    messages.success(request,"habito editado exitosamente")#mensajes temporales
    return redirect('/listadohabito')


#---------------------------------------progreso


def actualizar_progresos():
    # Obtén todas las notificaciones cuya fecha y hora límite han pasado
    notificaciones_expiradas = Notificacion.objects.filter(
        fecha_programada__lte=now()
    )

    for notificacion in notificaciones_expiradas:
        # Crear un progreso automáticamente basado en la notificación
        Progreso.objects.create(
            fecha=notificacion.fecha_programada,
            tiempo_realizado=notificacion.tiempo_realizado,  # Asigna tiempo realizado por defecto (puedes modificarlo)
            notas="Progreso creado automáticamente desde notificación.",
            idhabito=notificacion.idhabito
        )
        
        # Eliminar la notificación o marcarla como completada
        notificacion.delete()

    return redirect('/listadoprogreso')




def listadoprogreso(request):
    # Llama a la función que actualiza progresos antes de mostrar el listado
    actualizar_progresos()
    
    progresos = Progreso.objects.all()
    return render(request, 'listadoprogreso.html', {'progresos': progresos})



def guardarprogreso(request):
    fecha = request.POST['txt_fecha']
    tiempo_realizado = request.POST['txt_tiempo_realizado']
    notas = request.POST.get('txt_notas', '')
    habito_id = request.POST['habito_id']
    habito = Habito.objects.get(idhabito=habito_id)
    
    nuevo_progreso = Progreso.objects.create(
        fecha=fecha,
        tiempo_realizado=tiempo_realizado,
        notas=notas,
        idhabito=habito
    )
    messages.success(request,"progreso guardado")#mensajes temporales
    return redirect('/listadoprogreso')


def eliminarprogreso(request, id):
    progresoBdd = Progreso.objects.get(idprogreso=id)
    progresoBdd.delete()
    messages.success(request,"progreso eliminado")#mensajes temporales
    return redirect('/listadoprogreso')


def editarprogreso(request, id):
    progresoBdd = Progreso.objects.get(idprogreso=id)
    habitos = Habito.objects.all()
    return render(request, 'editarprogreso.html', {'progreso': progresoBdd, 'habitos': habitos})



def procesareditarprogreso(request):
    progreso = Progreso.objects.get(idprogreso=request.POST['id'])
    progreso.fecha = request.POST['txt_fecha']
    progreso.tiempo_realizado = request.POST['txt_tiempo_realizado']
    progreso.notas = request.POST.get('txt_notas', '')
    progreso.idhabito = Habito.objects.get(idhabito=request.POST['habito_id'])
    progreso.save()
    messages.success(request,"progreso editado exitosamente")#mensajes temporales
    return redirect('/listadoprogreso')





















#---------------------------------------notificacion



def nuevanotificacion(request):
    usuarios = Usuario.objects.all()
    habitos = Habito.objects.all()
    return render(request, 'nuevanotificacion.html', {'usuarios': usuarios, 'habitos': habitos})


def listadonotificacion(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'listadonotificacion.html', {'notificaciones': notificaciones})





def guardarnotificacion(request):
    if request.method == "POST":
        usuario_id = request.POST['usuario_id']
        habito_id = request.POST['habito_id']
        hora = request.POST['txt_hora']
        fecha_programada = request.POST['txt_fecha_programada']
        frecuencia = request.POST['txt_frecuencia']
        tiempo_realizado = request.POST['txt_tiempo_realizado']  # Obtener minutos
       
        
        usuario = Usuario.objects.get(id=usuario_id)
        habito = Habito.objects.get(idhabito=habito_id)

        nueva_notificacion = Notificacion.objects.create(
            usuario=usuario,
            idhabito=habito,
            hora=hora,
            fecha_programada=fecha_programada,
            frecuencia=frecuencia,
            tiempo_realizado=tiempo_realizado  # Asignar tiempo realizado
            
        )
        
        # Pasar los datos al contexto del mensaje
        messages.success(
            request,
            f'{habito.nombre_habito}|{hora}|{fecha_programada}'  # Enviar el nombre del hábito, la hora y la fecha
        )
        
        return redirect('/listadonotificacion')  # Ajusta según la ruta que necesites






def eliminarnotificacion(request, id):
    notificacionBdd = Notificacion.objects.get(id=id)
    notificacionBdd.delete()
    messages.success(request,"notificacion eliminado")#mensajes temporales
    return redirect('/listadonotificacion')



def editarnotificacion(request, id):
    notificacionBdd = Notificacion.objects.get(id=id)
    usuarios = Usuario.objects.all()
    habitos = Habito.objects.all()
    return render(request, 'editarnotificacion.html', {'notificacion': notificacionBdd, 'usuarios': usuarios, 'habitos': habitos})



def procesareditarnotificacion(request):
    notificacion = Notificacion.objects.get(id=request.POST['id'])
    notificacion.usuario = Usuario.objects.get(id=request.POST['usuario_id'])
    notificacion.idhabito = Habito.objects.get(idhabito=request.POST['habito_id'])
    notificacion.hora = request.POST['txt_hora']
    notificacion.fecha_programada = request.POST['txt_fecha_programada']
    notificacion.frecuencia = request.POST['txt_frecuencia']
    notificacion.tiempo_realizado = request.POST['txt_tiempo_realizado']  # Actualizar minutos real
    notificacion.save()
    messages.success(request,"notificacion editado exitosamente")#mensajes temporales
    return redirect('/listadonotificacion')






































#---------------------------------------metas

def nuevaficha(request):
    habitos = Habito.objects.all()
    return render(request, 'nuevaficha.html', {'habitos': habitos})



def listadometa(request):
    metas = Meta.objects.all()
    return render(request, 'listadometa.html', {'metas': metas})



def guardarmeta(request):
    habito_id = request.POST['habito_id']
    nombre = request.POST['txt_nombre']
    descripcion = request.POST['txt_descripcion']
    valor_meta = request.POST['txt_valor_meta']
    fecha_limite = request.POST['txt_fecha_limite']

    habito = Habito.objects.get(idhabito=habito_id)

    nueva_meta = Meta.objects.create(
        idhabito=habito,
        nombre=nombre,
        descripcion=descripcion,
        valor_meta=valor_meta,
        fecha_limite=fecha_limite
    )
    messages.success(request,"metas guardado")#mensajes temporales
    return redirect('/listadometa')


def eliminarmeta(request, id):
    metaBdd = Meta.objects.get(id=id)
    metaBdd.delete()
    messages.success(request,"metas eliminado")#mensajes temporales
    return redirect('/listadometa')



def editarmeta(request, id):
    metaBdd = Meta.objects.get(id=id)
    habitos = Habito.objects.all()
    return render(request, 'editarmeta.html', {'meta': metaBdd, 'habitos': habitos})




def procesareditarmeta(request):
    meta = Meta.objects.get(id=request.POST['id'])
    meta.idhabito = Habito.objects.get(idhabito=request.POST['habito_id'])
    meta.nombre = request.POST['txt_nombre']
    meta.descripcion = request.POST['txt_descripcion']
    meta.valor_meta = request.POST['txt_valor_meta']
    meta.fecha_limite = request.POST['txt_fecha_limite']
    meta.save()
    messages.success(request,"metas editado exitosamente")#mensajes temporales
    return redirect('/listadometa')





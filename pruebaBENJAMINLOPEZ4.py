
tareas=[]
def desplegar_menu():
 print("========= MENÚ PRINCIPAL ==========")
 print("1. Agregar tarea")
 print("2. Buscar tarea")
 print("3. Eliminar tarea")
 print("4. Actualizar estado")
 print("5. Mostrar tareas")
 print("6. Salir")
 print("==================================")

def seleccionar_opcion():
    try:
        opcion = int(input("seleccione una opcion(1-6): "))
        if 0 <= opcion <=6: 
             return opcion
        else:
            print("error: Ingrese un numero entre 1 y 6 ")
    except ValueError:
        print("error: debe ingresar un numero entero.")


def validar_descripcion(desc):
    return desc.strip() != ""

def validar_prioridad(prio):
    try:
        prioridad=int(prio)
        return 0 <= prioridad <= 10
    except ValueError:
        return False
    
def validar_tiempo(tiempo):
    try:
        tiempo = float(tiempo)
        return tiempo > 0
    except ValueError:
        return False
    

def agregar_tarea(Tareas):
    print("**************Agregar Tareas***************")
    desc = input("ingrese la descripcion de la tarea: ")
    if not validar_descripcion(desc):
        print("error: la descripcion no puede estar vacia")
        return
    prio = input("ingrese la prioridad (1-10): ")
    if not validar_prioridad(prio):
        print("error: prioridad invalida. Debe ser un entero entre 1 y 10")
        return
    tiempo = input("ingrese el tiempo estimado en horas: ")
    if not validar_tiempo(tiempo):
           print("error: tiempo invalido. Debe ser un numero mayor a 0.")
           return

    nueva_tarea = {

        "descripcion": desc,
        "prioridad":int(prio),
         "tiempo_estimado":float(tiempo),
        "completada": False 
    }

    tarea.append(nueva_tarea)
    print("registro exitoso: tarea agregada")


def buscar_tarea(tareas, descripcion_buscada):
    for i in range(tareas):
        if tarea[i]["desc"].lower() == descripcion_buscada.lower():
            return i

    return -1


def actualizar_estado(tareas):
    for tarea in tareas:
        if tarea["prio"] >=5:
            tarea["completada"]=True
    else:
        tarea["estado"]=False

while True:
    desplegar_menu()
    seleccion=seleccionar_opcion()
    if seleccion==1:
        agregar_tarea(tareas)
    elif seleccion==2:
        descripcion = input("ingrese la descripcion de la tarea a buscar: ").strip()
        if buscar_tarea(tareas,descripcion) !=-1:
            tarea=tareas[buscar_tarea(tareas,descripcion)]
            print(f"tarea N°{buscar_tarea(tareas,descripcion)+1}: ")
            print(f"descripcion: {tarea["desc"]}")
            print(f"prioridad: {area["prio"]}")
            print(f"tiempo estimado: {tarea["tiempo"]}")
            if tarea["estado"]== True:
               print("estado: COMPLETADO")
            else:
                print("estado: PENDIENTE")

        else:
            print("tarea no encontrada")

    elif seleccion == 3:
        descripcion=input("ingrese la descripcion de la tarea a eliminar: ").strip()
        if buscar_tarea(tareas,descripcion) !=-1:
            tareas.pop(buscar_tarea(tareas,descripcion))
            print("tarea eliminada con exito")
        else:
            print(f"la tarea {descripcion} no se encuentra registrada.")
   
    elif seleccion == 4:
        actualizar_estado(tareas)
        print("se han actualizado los estados de las tareas.")
    
    elif seleccion == 5:
        actualizar_estado(tareas)
        print("==== Lista de tareas ====\n")
        for tarea in tareas:
            print(f"descripcion: {tarea["desc"]}")
            print(f"prioridad: {tarea["prio"]}")
            print(f"tiempo_estimado: {tarea["tiempo"]}")
            if tarea["estado"]==True:
                print("estado: COMPLETADA")
            else:
                print("estado PENDIENTE")

            print("********************************")

    elif seleccion == 6: 
        print("Gracias por usar el sistema")
        break






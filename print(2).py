carreras=[]



seguir = True
while seguir:
    print("1. crear carrera")
    print("2. leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. adicionar clases")
    print("6. Salir")
    opcion =int(input("Ingrese su opcion: "))
    
    print("---------------------------------------------------------------------")
    if opcion==1:
        print("Ingrese carrera")
        nombre=input("Nombre : ")
        dicCarrera={}
        dicCarrera["carrera"]=nombre
        carreras.append(dicCarrera)
    elif opcion==2:
        print("Leer carrera")
        for carrera in carreras:
            print("- Nombre : "+carrera["carrera"])
    elif opcion==3:
        print("Actualizar carrera")
    elif opcion==4:
        print("Borrar carrera")
        name=input("Ingrese nombre de la carrera :")
        indice =0
        encontrado=False
        for carrera in carreras:
            if carrera["carrera"]==name:
                encontrado=True
                break
            else:
                indice+=1
    
    elif opcion==5:
        print("adicionar clases")
        i=1
        for carrera in carreras:
            print(str(i)+"- Nombre : "+carrera["carrera"])
            i+=1
        seleccionar
    elif opcion==6:
        print("Hasta la proxima")
        seguir=False
    print("---------------------------------------------------------------------")
    
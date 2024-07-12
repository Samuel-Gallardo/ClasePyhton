import random,csv,time
from math import prod
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
menor_a_800k=[]
entre_800k=[]
mayor_a_2000k=[]
sueldos=[]
def menu():
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opc=int(input("Ingrese una opcion: "))
    print("")
    if opc==1:
        asignar_sueldos()
    elif opc==2:
        clasificar_sueldos()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_sueldos()
    elif opc==5:
        despedida()
    
def asignar_sueldos():
    sueldo1=random.randint(300000,2500000)
    sueldos.append(sueldo1)
    if sueldo1<800000:
        menor_a_800k.append(sueldo1)
    elif sueldo1>=800000 and sueldo1<=2000000:
        entre_800k.append(sueldo1)
    elif sueldo1>2000000:
        mayor_a_2000k.append(sueldo1)
        
    sueldo2=random.randint(300000,2500000)
    sueldos.append(sueldo2)
    if sueldo2<800000:
        menor_a_800k.append(sueldo2)
    elif sueldo2>=800000 and sueldo1<=2000000:
        entre_800k.append(sueldo2)
    elif sueldo2>2000000:
        mayor_a_2000k.append(sueldo2)
    
    sueldo3=random.randint(300000,2500000)
    sueldos.append(sueldo3)
    if sueldo3<800000:
        menor_a_800k.append(sueldo3)
    elif sueldo3>=800000 and sueldo3<=2000000:
        entre_800k.append(sueldo3)
    elif sueldo3>2000000:
        mayor_a_2000k.append(sueldo3)
    
    sueldo4=random.randint(300000,2500000)
    sueldos.append(sueldo4)
    if sueldo4<800000:
        menor_a_800k.append(sueldo4)
    elif sueldo4>=800000 and sueldo4<=2000000:
        entre_800k.append(sueldo4)
    elif sueldo4>2000000:
        mayor_a_2000k.append(sueldo4)
        
    sueldo5=random.randint(300000,2500000)
    sueldos.append(sueldo5)
    if sueldo5<800000:
        menor_a_800k.append(sueldo5)
    elif sueldo5>=800000 and sueldo5<=2000000:
        entre_800k.append(sueldo5)
    elif sueldo5>2000000:
        mayor_a_2000k.append(sueldo5)
        
    sueldo6=random.randint(300000,2500000)
    sueldos.append(sueldo6)
    if sueldo6<800000:
        menor_a_800k.append(sueldo6)
    elif sueldo6>=800000 and sueldo6<=2000000:
        entre_800k.append(sueldo6)
    elif sueldo6>2000000:
        mayor_a_2000k.append(sueldo6)
        
    sueldo7=random.randint(300000,2500000)
    sueldos.append(sueldo7)
    if sueldo7<800000:
        menor_a_800k.append(sueldo7)
    elif sueldo7>=800000 and sueldo7<=2000000:
        entre_800k.append(sueldo7)
    elif sueldo7>2000000:
        mayor_a_2000k.append(sueldo7)
        
    sueldo8=random.randint(300000,2500000)
    sueldos.append(sueldo8)
    if sueldo8<800000:
        menor_a_800k.append(sueldo8)
    elif sueldo8>=800000 and sueldo8<=2000000:
        entre_800k.append(sueldo8)
    elif sueldo8>2000000:
        mayor_a_2000k.append(sueldo8)
        
    sueldo9=random.randint(300000,2500000)
    sueldos.append(sueldo9)
    if sueldo9<800000:
        menor_a_800k.append(sueldo9)
    elif sueldo9>=800000 and sueldo9<=2000000:
        entre_800k.append(sueldo9)
    elif sueldo9>2000000:
        mayor_a_2000k.append(sueldo9)
        
    sueldo10=random.randint(300000,2500000)
    sueldos.append(sueldo10)
    if sueldo10<800000:
        menor_a_800k.append(sueldo10)
    elif sueldo10>=800000 and sueldo10<=2000000:
        entre_800k.append(sueldo10)
    elif sueldo10>2000000:
        mayor_a_2000k.append(sueldo10)
    print("Sueldos Asignados Aleatoriamente")
    print("")
    menu()
    
            
def clasificar_sueldos():
    for i in range(len(menor_a_800k)):
        total=i+1
    print(f"Sueldos Menores a $800.000 | Total:{total}")
    print(f"Nombre Trabajador   |   Sueldo")
    for x in range(len(menor_a_800k)):
        trabajador=trabajadores[x]
        if trabajador in trabajadores:
            print(f"{trabajador}    |   {menor_a_800k[x]}")
        
    for i in range(len(entre_800k)):
        total=i+1
    print(f"Sueldos Entre $800.000 y $2.000.000| Total:{total}")
    print(f"Nombre Trabajador   |   Sueldo")
    for x in range(len(entre_800k)):
        trabajador=trabajadores[x]
        if trabajador in trabajadores:
            print(f"{trabajador}    |   {entre_800k[x]}")
    
    for i in range(len(mayor_a_2000k)):
        total=i+1
    print(f"Sueldos Mayor a $2.000.000 | Total:{total}")
    print(f"Nombre Trabajador   |   Sueldo")
    for x in range(len(mayor_a_2000k)):
        trabajador=trabajadores[x]
        print(f"{trabajador}    |   {mayor_a_2000k[x]}")
  
    menu()

def ver_estadisticas():
    sueldosmax=max(sueldos)
    sueldomin=min(sueldos)
    promediosueldo=sum(sueldos)/10
    producto=prod(sueldos)
    mediaG=producto**(1/10)
    
    print(f"Sueldo Maximo: {sueldosmax}")
    print(f"Sueldo Minimo: {sueldomin}")
    print(f"Promedio de Sueldos: {promediosueldo}")
    print(f"Media Geometrica: {mediaG:.2f}")
    print("")
    menu()
def reporte_sueldos():
    with open('reporte_sueldo.csv','w',newline='') as archivo:
        archivo.write("Nombre empleado  |   Sueldo\n")
        for x in range(len(sueldos)):
            trabajador=trabajadores[x]
            archivo.write(f"{trabajador}    |   {sueldos[x]}\n")
        
    
    menu()
    
def despedida():
    print("Finalizando Programa...")
    print("Desarrollado por : Samuel Gallardo\nRut: 22.080.828-9")
    time.sleep(1)
    exit()
menu()
    
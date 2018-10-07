import time,Funciones
import prueba #Libreria del teclado
Te=prueba._Getch()
Q=Te.__init__()

Mov=Funciones.Movimientos()
Mov.Recoger(3000,9000,7320,0) ## M1,M2,Desfasamiento entre motores
motor=0
sentido=0
cont1=0
Cm2=0
Cm3=0
Cm4=0
tt=0
while 1:
    teclaPulsada=Te.__call__()
    Sel=(teclaPulsada)
    print "Sel: "+ Sel
    if Sel=='r':
	print "oprimiendo R"
        Mov.Elongar(6000,9000,7320,0) #p1,p2,p3,Velocidad
    if Sel=='d':
        motor=0
        cont1=cont1+1
        Mov.MoverBrazo(1,0,cont1,motor)# Direccion, Velocidad,Movimiento,ServoMotor
    if Sel=='a':
        motor=0
        cont1=cont1-1
        Mov.MoverBrazo(0,0,cont1,motor)# Direccion, Velocidad,Movimiento,ServoMotor

    if Sel=='x':
        motor=1
        Cm2=Cm2+1
        Mov.MoverBrazo(0,0,Cm2,motor)# Direccion, Velocidad,Movimiento,ServoMotor
    if Sel=='w':
        motor=1
        Cm2=Cm2-1
        Mov.MoverBrazo(1,0,Cm2,motor)# Direccion, Velocidad,Movimiento,ServoMotor

    if Sel=='z':
        motor=2
        Cm3=Cm3+1
        Mov.MoverBrazo(0,0,Cm3,motor)# Direccion, Velocidad,Movimiento,ServoMotor
    if Sel=='q':
        motor=2
        Cm3=Cm3-1
        Mov.MoverBrazo(1,0,Cm3,motor)# Direccion, Velocidad,Movimiento,ServoMotor
    if Sel=='e':
        motor=3
        Cm4=Cm4+1
        Mov.MoverBrazo(0,0,Cm4,motor)# Direccion, Velocidad,Movimiento,ServoMotor
    if Sel=='c':
        motor=3
        Cm4=Cm4+1
        Mov.MoverBrazo(1,0,Cm4,motor)# Direccion, Velocidad,Movimiento,ServoMotor
    if Sel=='g':
        break







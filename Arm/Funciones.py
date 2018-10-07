import maestro,time

servo = maestro.Controller()
servo.setRange(0,0,9000)
servo.setRange(1,0,9000)
servo.setRange(2,0,9000)
servo.setRange(3,0,9000)
servo.setRange(4,0,9000)
servo.setRange(5,0,9000)
servo.setRange(6,0,9000)
servo.setRange(7,0,9000)
servo.setRange(8,0,9000)

class Movimientos:
    def Elongar(self,p1,p2,p3,VeAC):
        posiciones=[p1,p2,p3]
        for i in range(len(posiciones)):
            pos_ideal=posiciones[i]
            pos_actual=servo.getPosition(i)
            pos_actual2=0
            inc=0
            VelM=VeAC
            Error=pos_ideal-pos_actual
            while 1:
                if Error>-100 and Error<100:
                    break
                if Error>0:
                    inc=pos_actual
                    while(1):
                        inc=inc+1
                        servo.setAccel(i,VelM)
                        servo.setSpeed(i,VelM)
                        servo.setTarget(i,inc)

                        if inc>0.99*pos_ideal:
                            pos_actual=servo.getPosition(i)
                            break
                    break

                if Error<0:
                    inc=pos_actual
                    while(1):
                        inc=inc-1
                        servo.setAccel(i,VelM)
                        servo.setSpeed(i,VelM)
                        servo.setTarget(i,inc)

                        if pos_ideal>0.99*inc:
                            pos_actual=servo.getPosition(i)
                            break
                    break
    def Recoger(self,p1,p2,p3,VeAC):
        pos_ideal=0
        pos_actual=0
        inc=0
        posiciones=[p1,p2,p3]
        for i in range(len(posiciones)):
            k=len(posiciones)-1-i
            pos_ideal=posiciones[k]
            pos_actual=servo.getPosition(k)
            pos_actual2=0
            inc=pos_actual
            VelM=VeAC
            Error=pos_ideal-pos_actual

            while 1:
                if Error>-100 and Error<100:
                    break
                if Error>0:
                    inc=pos_actual
                    while(1):
                        inc=inc+1
                        servo.setAccel(k,VelM)
                        servo.setSpeed(k,VelM)
                        servo.setTarget(k,inc)

                        if inc>0.99*pos_ideal:
                            pos_actual=servo.getPosition(k)
                            break
                    break

                if Error<0:
                    inc=pos_actual
                    while(1):
                        inc=inc-1
                        servo.setAccel(k,VelM)
                        servo.setSpeed(k,VelM)
                        servo.setTarget(k,inc)

                        if inc<pos_ideal:
                            pos_actual=servo.getPosition(k)
                            break

                    break

    def MoverBrazo(self,Dir,VV,Gir,M):

        if Dir==0:
            if M==0:
                GM=Gir
                pos=servo.getPosition(M)-GM
            if M==1:
                GM1=Gir
                pos=servo.getPosition(M)-GM1
            if M==2:
                GM2=Gir
                pos=servo.getPosition(M)-GM2
            if M==3:
                GM3=Gir
                pos=servo.getPosition(M)-GM3
            if M==4:
                GM4=Gir
                pos=servo.getPosition(M)-GM4
            if M==5:
                GM5=Gir
                pos=servo.getPosition(M)-GM5

        elif Dir==1:
            if M==0:
                GM=Gir
                pos=servo.getPosition(M)+GM
            if M==1:
                GM1=Gir
                pos=servo.getPosition(M)+GM1
            if M==2:
                GM2=Gir
                pos=servo.getPosition(M)+GM2
            if M==3:
                GM3=Gir
                pos=servo.getPosition(M)+GM3
            if M==4:
                GM4=Gir
                pos=servo.getPosition(M)+GM4
            if M==5:
                GM5=Gir
                pos=servo.getPosition(M)+GM5

        servo.setAccel(M,VV)

        servo.setTarget(M,pos)

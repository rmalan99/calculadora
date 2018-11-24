import os,time
from math import sqrt,pow
import colorama
from colorama import Fore,Style,Back,init
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>color
init()
colorama.init(convert=True)
l_m=Fore.MAGENTA+Style.BRIGHT#....|morado brilloso
s_=Style.RESET_ALL#...............|reset color
l_b=Fore.BLUE+Style.BRIGHT#.......|azul brillate
l_r=Fore.RED#.....................|ROJO INTENZO
l_B=Fore.BLUE#....................|azul opaco
l=Fore.YELLOW
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def y():            
        print(l+"                                ///////////////////",s_)
        print(l+"                             ////  //////////////////          ////",s_)
        print(l+"                            ///////////////////           ////////",s_)
        print(l+"                            ///////",l_r+'///',s_,l+"////////        ////////////",s_)
        print(l+"                               //////////////////        /////",s_)
        print(l+"                                 /////////////////    ////////",s_)
        print(l+"                                //////////////////    ////",s_)
        print(l+"                              // //////////////////////",s_)
        print(l+"                             / //////////////////////",s_)
        print(l+"                              /////////////////",s_)
        print(l+"                              //////////////",s_)
def relay():
    print ("volviendo");
    time.sleep(1);
    print ("volviendo.");
    time.sleep(3)
    print ("volviendo..");
    time.sleep(2);
    print ("volviendo...");
    time.sleep(5);
    ini();
def clear():#LIMPIANDO EL PROMT
    c=os.system("cls" if os.name=="nt" else "clear" )#|\(O_ O) SE DISTIGUE FACILMENTE QUE PASO AHI
    print(c)
def volver(intem):
    lit=["<////////////////////////>","1=volver a menu principal","2=reinicio"]
    for x in lit:
        print(x)
    r=True
    while r==True:
        try:
            resp=int(input("=>"));
            break
        except ValueError:
            print("debe ser un numero");

    if (resp==2):
        if(intem==1):
            pro_arit();
            relay();
        elif(intem==2):
            pro_geo();
            relay();
        elif(intem==3):
            variaciones();
            relay();
        elif(intem==4):
            permutaciones();
            relay();
        elif(intem==5):
            int_sim();
            relay();
        elif(intem==6):
            int_comp();
            relay();
        elif(intem==7):
            ecua_2();
            relay();
    else:
        ini();
        relay();
def pro_arit():
    clear();
    intem=1;
    print("progreciones aritmeticas\n");
    while True:
        try:
            a1=int(input("digite la primera constante {a1} "));
            a2=int(input("digite la segunda costante {a2} "));
            d=a2-a1;
            n=int(input("cual es la costante e-nesima que dea ver "))
            break
        except ValueError:
            print("debe ser un numero ");
            y();

    an=(a1+(n-1)*d);
    print("=>", an)
    volver(intem);
def pro_geo():
    clear();
    intem=2;
    print("progreciones geometricas")
    while True:
        try:
            a1=int(input("dijite el primer termino "));
            a2=int(input("dijiste el segundo termino "));
            n=int(input("cual es la e-enesima position ue desea ver "));
            break
        except ValueError:
            print("debe digitar un numero ");
    r=a2/a1;
    an=(a1*(r**(n-1)));
    print("=> ",an);
    volver(intem);
def variaciones():
    clear();
    intem=3;
    print("variaciones ")
    y=1;
    while True:
        try:
            m=int(input("cantidad de conjuntos ue desea"));
            n=int(input("cuantos elementos tendra estos conjuntos "))
            break
        except ValueError:
            print("debe ser un digito");
            y();
    for x in range(n):
        p=m-x;
        y=y*p;
    print("se pueden crear ",y," variaciones distintas ")
    volver(intem);
def permutaciones():
    intem=4;
    print("permutaciones ")
    clear();
    p=1;
    
    while True:
        try:
            per=int(input("dijite cantida de permutaciones "));
        except ValueError:
            print("debe ser un numero");
            y();
    per=per+1;
    while per>1:
        per=per-1
        p=per*p;
    print("=> ",p);
    volver(intem)
#.............................................................
def intereses():
    clear();
    titulos=["intereses simples","interes compuesto"]
    y=0;
    print("<---selecione--->")
    for x in titulos:
        y=y+1;
        print(y,"=",x);
    while True:
        try:
            resp=int(input("=>"));
            break
        except ValueError:
            print("debe ser un numero");
            y();
    if (1==resp):
        int_sim();
    if (2==resp):
        int_comp();
def int_sim():
    clear();
    intem=5;
    print("interes simples")
    while True:
        try:
            va=int(input("digite el valor actual "));
            n=int(input("digite el periodo o plazo "));
            i=float(input("digite el interes{valor solo en desimal flotante } "));
            break
        except ValueError:
            print("debeser un numero");
            y();
    vf=va*(1+n*i)
    print("el total a pagar en un periodo de ",n," es ",vf,);
    volver(intem);
def int_comp():
    clear();
    intem=6;
    print("interes compuesto")
    p=0;
    while True:
        try:
            c=int(input("digite el valor capital "));
            n=int(input("digite el periodo o plazo "));
            i=float(input("digite el interes{valor solo en desimal flotante} "));
            break
        except ValueError:
            print("bebe ser un digito");
            y();
    
    for x in range(n+1):
        if (x>0):
            p=c*i;
            c=p+c;
        print("<....................................>")
        print (x,">==",c,">==",i,">==",p);
    volver(intem);
def ecua_2():
    clear();
    intem=7;
    y=False;
    while y==False:
        print("ecuaciones cuadratricas\ndigite los terminos segun correspodacorrectamente")
        a=int(input("digite el numerador del primer termino\n=>"));
        b=int(input("digite e numerador del segundo termino\n=>"));
        c=int(input("digite el numerador del segundo termino\n=>"));
        if (b<0 and c<0):
            print("su ecuacion es \n",a,"X^2",b,"X",c);
            cont=str(input("esta correcta (si o no?)"));
            if (cont=="si"):
                y=True;
        elif ( b>0 and c>0):
            print("su ecuacion es \n",a,"X^2+",b,"X+",c);
            cont=str(input("esta correcta (si o no?)"));
            if (cont=="si"):
                y=True;
        elif(b<0 and c>0):
            print("su ecuacion es \n",a,"X^2",b,"X+",c);
            cont=str(input("esta correcta (si o no?)"));
            if (cont=="si"):
                y=True;
        elif(b>0 and c<0):
            print("su ecuacion es \n",a,"X^2+",b,"X",c);
            cont=str(input("esta correcta (si o no?)"));
            if (cont=="si"):
                y=True;
        else:
            print("desea salir");
            salir()
        clear();
        bloque_1=pow(b,2);
        bloque_2=(4*a)*c;
        bloque_3=bloque_1-bloque_2;
        bloque_3_5=sqrt(bloque_3);
        bloque_4=-1*b;
        bloque_5=2*a;
        x_1=(bloque_4+bloque_3_5)/bloque_5;
        x_2=(bloque_4-bloque_3_5)/bloque_5;
        print("x=-(",b," )<+->RAIZ(",b,"^2-4*(",a,")*(",c,")");
        print("-----------------------------")
        print("          2(",a,")");
        print("\n")
        time.sleep(2);
        print("x=",bloque_4,"<+->raiz(",bloque_1,"-",bloque_2);
        print("-----------------------------")
        print("          ",bloque_5);
        print("\n")
        time.sleep(2);
        print("x=",bloque_4,"<+->",bloque_3_5);
        print("-----------------------------")
        print("          ",bloque_5);
        print("\n")
        time.sleep(2);
        print("x1=",x_1,"                    x2=",x_2);
        volver(intem);

def ini():
    clear();
    y()
    titulos=["progrecion aritmetica","progreciones geometricas","ecuaciones cuadraticas","variaciones","permutaciones","intereses" ];
    p=0
    for x in titulos:
        p=1+p;
        print(p,"= ",x)
    option=int(input("=>"))    
    if (option==1):
        pro_arit();
    elif(option==2):
        pro_geo();
    elif(option==3):
        ecua_2();
    elif(option==4):
        variaciones();
    elif(option==5):
        permutaciones();
    elif(option==6):
        intereses();
ini();
import colores_modo_oscuro as c
#import colores as c
import random
import sys
import time
import os
import tkinter as tk
import webbrowser
import sqlite3

empezar=False

def inicio():
    global user
    global empezar
    empezar=False
    user = {}
    cargar()

def delscr():
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

def grdusr():
    global us
    global con
    cadena = '\n' + str(us) + ',' + str(con) + '\n'
    with open('usuarios.txt', 'a') as file:
        file.write(cadena)
    
def salir():
    sys.exit()


def mayus(input):
    mayus = 0
    listamayus = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    for i in input:
        if i in listamayus:
            mayus += 1
    if mayus > 0:
        return True
    else:
        return False

def minus(input):
    minus = 0
    listaminus = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    for i in input:
        if i in listaminus:
            minus += 1
    if minus > 0:
        return True
    else:
        return False

def nums(input):
    nums = 0
    listanums = "1 2 3 4 5 6 7 8 9 0".split()
    for i in input:
        if i in listanums:
            nums += 1
    if nums > 0:
        return True
    else:
        return False

def validcontr(input):
    dicc1 = {
        'mayus': mayus(input),
        'minus': minus(input),
        'nums': nums(input)
    }
    if mayus(input) & minus(input) & nums(input):
        delscr()
        return True
    else:
        print ("Contraseña inválida")
        time.sleep(1)
        delscr()
        print
        if dicc1['mayus'] == False:
            print ("La contraseña necesita al menos una mayúscula.")
            time.sleep(1.5)
            delscr()
        if dicc1['minus'] == False:
            print ("La contraseña necesita al menos una minúscula.")
            time.sleep(1.5)
            delscr()
        if dicc1['nums'] == False:
            print ("La contraseña necesita al menos un número.")
            time.sleep(1.5)
            delscr()

def repetido():
    with open("usuarios.txt", "r") as f:
        for line in f:
            loginInfo = line.strip().split(",")
            if us == loginInfo[0]:
                return True
    return False

def registr():
    False
    global con
    global us
    logo1()
    us=input("Ingrese su usuario ")
    if len(us)<=2:
        print("El usuario debe contener más de dos caracteres")
        time.sleep(1)
        delscr()
        registr()
    else:
        while True:
            con=input("Ingrese una contraseña ")
            if validcontr(con):
                if repetido():
                    print("El usuario ya se ha registrado")
                    time.sleep(1)
                    print("Regresando al menú principal...")
                    time.sleep(1.5)
                    cargar()
                else:
                    user[us] = con
                    grdusr()
                    print("Usuario registrado con éxito")
                    time.sleep(1)
                    cargar()
                    return False

def nuevoinic():
    if autorizado():
        print("""
Bienvenido, ha iniciado sesión con éxito,
Cuando pierda o gane, cierre la pestaña del
juego y mantenga abierta la terminal de comandos.

El juego iniciará en unos segundos...
""")
        time.sleep(4.5)
        pass        
    else:
        print("Usuario o contraseña incorrectos")
        print("Volviendo al menú principal....")
        time.sleep(2)
        delscr()
        cargar()

def autorizado():
  global usuarioin
  logo2()  
  usuarioin = input("Ingrese su usuario: ").strip()
  con = input("Ingrese su contraseña: ").strip()

  with open("usuarios.txt", "r") as f:
    for line in f:
      loginInfo = line.strip().split(",")
      if usuarioin == loginInfo[0] and con == loginInfo[1]:
        return True
    return False

def logo():
    print('''
                                                                                    
                                                                                
                                     .%@%.                                      
                              *%/#&    /&    #%/&(                              
                  ****.     ,#,%,(*% ,.   * */*/%/%(     .****                  
                #,     .(  .%*&/%(.*@@@@@@@@(.&#/(*(,  /*      /                
                .(.*@* ,.# ,*,**.#.%./,*/** (,&,/,*,* ( . *@/.(*                
                   *,  / & &%#/#.&.% ,,,(*. (*@*@/%*# / , ..%                   
          /,     ,( *. ( @ (%./*((*#,(##/%*.&/%/*,.(( ( * ., (,     ,(          
          (  #  */ /. / *,, &.@/@/@.*(&,,&%,,%,&.@.#,.** &  % ./ .%  (.         
         &  ,./.@ #, % .(****%.@.&,%.*( .*/./*&/@/&#***,/ (../ / ( (  (         
   *.  *%(..,*,/,/&,( (  #%#./%*@,( .&    /..(,#,(( (/% .#.#*%./ (,*, ##/.  %   
    %   /. #,*#. .@@#(*./   @*.(    , .((, ,    #,.@,  ,/,#(@@   /,*( ,(   &    
 */(.,#,./(%@& *#*#,  /(*,%/(//(#*,*&*/#(#,@/**((/(((#/.#(  .#*(*.%@&(/..%*.(// 
@  . .%, ((    (     (#.   (&&(,  .#@.((((.&&,  ,(&&(   .#%     @.   *( ,&, ,  (
 ((,*#/.(*.%               ....      .# .%,      ....               %.*#./#/,(#.
      (*#(/ #.                         ,(                          (.,%/#%      
     /,#.@.# #      ,&&%#@@##&&(       ,(          .(@/..*&&      & %.# / (     
     # (.#.,/.#     .(#      /#*       ,(       ,,,,,,,,,. #%    /,**./ / /.    
     *,.*,.,( &    .*,,%    ,,#,,      ,(        ,@@@@@(  (@     /.**., * #     
      # .  % **    * ,, /  .( # *,     ,(         .*%,#/,        ,* #  , @      
      ,(  #  %      ,**,    .*/*.....*%(/&/....  .&&(*.           &  (, (,      
 *((#  @/ *,./                  %.    .*( ,    /  /#/%#.*         /*.# /@  ##(/ 
@ ,&/ .,#/&, ,/%.               **  ,.*/%,*,  .(               .%(,.,@(%*. *%* (
@ *    .&./    .@,,,,,,,,,,,,,,,&,.../#&#%,.,..(,,,,,,,,,,,,,,,#     %,@*    , #
 #*     ((  ,%*                 @.((%.,(%,.&*# (                 *##  /(.    *%.
        (@@,,/                   # *@,%./&*&( // .@@,             */.@@#        
     #*//((/.(        ,////////*  ,#/ *./*.*#*   .@,,#/%/%(@.     &.(//*(,#.    
   /, ( /,** #.     *@. %*  ((         /#        %...// *@%      .% *(,( &..%   
  /* # /.,#  .&         &,  #/         ,(        @...//.@,       (.  /* / *.,/  
  & *  .#  /@*,(       #%   ##         ,(        *&,.(%/        ,(.@(  %,. , (  
  /* .# *((,&/ *%                      ,(         .@&@,        (* &/,&(* @. ,/  
   *#/.% @  (,&  #,                    ,(         .(*        .&. (./  ( (.*#/   
     ./ / ,* / #,  (/                  ,(                  *%  ,@ # /, @ #,     
     ,* , (.(#//#(    *#/              ,(              /#/    /#//#(.#. .,/     
      (  @..   /%*. .,#%*. .(%/,       ,(       ,*%#. .*#%*.  ,#/.  ../  @.     
       *%,(@/#       .,/%&(,*#%*  .*/%.,( (&/.  ,##**/%&/,.       &,@#,&/       
             #@&  ,#(*.  .,*(#*   ,*///((///*,.  ,#(*,.  .*(#*  &@%             
               .**         /@#.   ,/,%/*(,%,*/   .(@(         **.               
         %*.,/#*  ,(.((/. ,*/.,/%/*/,/./. ,,*/ ./,**.(../((.,/  ,((,.,#         
        ,(%(,,*(&/   (/*/ &*/ .,#&(,        ,/&%*. *(/,%/*    *&(*,,/&#,        
        ,/ /#*#(.# ,(,,..##*.    (,   .&#.   ,%    .*(#. ,  //%/(*//# /*        
         &. ,./,. .*##.           #%*./  #,*%(            (#/.  ,/*, .#         
            ....                       ..                        ...            
                                                                                

''')

def logo1():
    print('''


                                                                                                                           
8 888888888o.   8 8888888888       ,o888888o.     8 8888    d888888o. 8888888 8888888888 8 888888888o.      ,o888888o.     
8 8888    `88.  8 8888            8888     `88.   8 8888  .`8888:' `88.     8 8888       8 8888    `88.  . 8888     `88.   
8 8888     `88  8 8888         ,8 8888       `8.  8 8888  8.`8888.   Y8     8 8888       8 8888     `88 ,8 8888       `8b  
8 8888     ,88  8 8888         88 8888            8 8888  `8.`8888.         8 8888       8 8888     ,88 88 8888        `8b 
8 8888.   ,88'  8 888888888888 88 8888            8 8888   `8.`8888.        8 8888       8 8888.   ,88' 88 8888         88 
8 888888888P'   8 8888         88 8888            8 8888    `8.`8888.       8 8888       8 888888888P'  88 8888         88 
8 8888`8b       8 8888         88 8888   8888888  8 8888     `8.`8888.      8 8888       8 8888`8b      88 8888        ,8P 
8 8888 `8b.     8 8888         `8 8888       .8'  8 8888 8b   `8.`8888.     8 8888       8 8888 `8b.    `8 8888       ,8P  
8 8888   `8b.   8 8888            8888     ,88'   8 8888 `8b.  ;8.`8888     8 8888       8 8888   `8b.   ` 8888     ,88'   
8 8888     `88. 8 888888888888     `8888888P'     8 8888  `Y8888P ,88P'     8 8888       8 8888     `88.    `8888888P'     


''')

def logo2():
    print('''


                                                                                                 
 8 8888 b.             8  8 8888     ,o888888o.     8 8888          .8.          8 888888888o.   
 8 8888 888o.          8  8 8888    8888     `88.   8 8888         .888.         8 8888    `88.  
 8 8888 Y88888o.       8  8 8888 ,8 8888       `8.  8 8888        :88888.        8 8888     `88  
 8 8888 .`Y888888o.    8  8 8888 88 8888            8 8888       . `88888.       8 8888     ,88  
 8 8888 8o. `Y888888o. 8  8 8888 88 8888            8 8888      .8. `88888.      8 8888.   ,88'  
 8 8888 8`Y8o. `Y88888o8  8 8888 88 8888            8 8888     .8`8. `88888.     8 888888888P'   
 8 8888 8   `Y8o. `Y8888  8 8888 88 8888            8 8888    .8' `8. `88888.    8 8888`8b       
 8 8888 8      `Y8o. `Y8  8 8888 `8 8888       .8'  8 8888   .8'   `8. `88888.   8 8888 `8b.     
 8 8888 8         `Y8o.`  8 8888    8888     ,88'   8 8888  .888888888. `88888.  8 8888   `8b.   
 8 8888 8            `Yo  8 8888     `8888888P'     8 8888 .8'       `8. `88888. 8 8888     `88. 
                                                                                                 
   d888888o.   8 8888888888     d888888o.    8 8888     ,o888888o.     b.             8          
 .`8888:' `88. 8 8888         .`8888:' `88.  8 8888  . 8888     `88.   888o.          8          
 8.`8888.   Y8 8 8888         8.`8888.   Y8  8 8888 ,8 8888       `8b  Y88888o.       8          
 `8.`8888.     8 8888         `8.`8888.      8 8888 88 8888        `8b .`Y888888o.    8          
  `8.`8888.    8 888888888888  `8.`8888.     8 8888 88 8888         88 8o. `Y888888o. 8          
   `8.`8888.   8 8888           `8.`8888.    8 8888 88 8888         88 8`Y8o. `Y88888o8          
    `8.`8888.  8 8888            `8.`8888.   8 8888 88 8888        ,8P 8   `Y8o. `Y8888          
8b   `8.`8888. 8 8888        8b   `8.`8888.  8 8888 `8 8888       ,8P  8      `Y8o. `Y8          
`8b.  ;8.`8888 8 8888        `8b.  ;8.`8888  8 8888  ` 8888     ,88'   8         `Y8o.`          
 `Y8888P ,88P' 8 888888888888 `Y8888P ,88P'  8 8888     `8888888P'     8            `Yo          

                                                                                                                                                                                                      
''')

def cargar():
    delscr()
    logo()
    print("""
Bienvenido al menú de inicio del juego 2048,
¿qué le gustaría hacer?
""")
    print("•Registrarse (1)")
    time.sleep(0.4)
    print("•Iniciar Sesión (2)")
    time.sleep(0.4)
    print("•Salir (3)")
    time.sleep(0.4)
    print("•Instrucciones y estrategia del juego (4)")
    time.sleep(0.3)
    print("•Cambiar paleta de colores (5)")
    a=input("Escriba un número: ")

    if a=="3":
        salir()

    if a=="1":
        delscr()
        registr()

    if a=="2":
        delscr()
        nuevoinic()
    
    if a=="4":
        webbrowser.open('http://www.manualpc.com/guia-y-estrategia-de-2048/')
        print("Se ha abierto una pestaña con las instrucciones y estrategias del juego")
        b=input("¿Desea regresar al menú principal? (s/n) ")
        if b=="s":
            cargar()
        else:
            print("saliendo...")
            time.sleep(1)
            sys.exit

    if a=="5":
        delscr()
        paleta()

def paleta():
    print("Ha cambiado a colores oscuros")
    import colores_modo_oscuro as c
    print("Regresando al menú principal...")
    time.sleep(2)
    cargar()






class Game(tk.Frame):
        def __init__(self):
            tk.Frame.__init__(self)
            self.grid()
            self.master.title("Bienvenido a 2048")

            self.main_grid = tk.Frame(
            self, bg=c.COLOR_CUADRIC, bd=3, width=600, height=600
            )
            self.main_grid.grid(pady=(100, 0))
            self.interfaz()
            self.empzr_jg()

            self.master.bind("<Left>", self.left)
            self.master.bind("<Right>", self.right)
            self.master.bind("<Up>", self.up)
            self.master.bind("<Down>", self.down)

            self.mainloop()
        
        
        def interfaz(self):
            self.cells = []
            for i in range(4):
                row = []
                for j in range(4):
                    cell_frame = tk.Frame(
                        self.main_grid,
                        bg=c.COLOR_CELDA_VACIA,
                        width=150,
                        height=150
                    )
                    cell_frame.grid(row=i, column=j, padx=5, pady=5)
                    cell_number = tk.Label(self.main_grid, bg=c.COLOR_CELDA_VACIA)
                    cell_number.grid(row=i, column=j)
                    datos_celda = {"frame": cell_frame, "number": cell_number}
                    row.append(datos_celda)
                self.cells.append(row)
                
            score_frame = tk.Frame(self)
            score_frame.place(relx=0.5, y=45, anchor="center")
            tk.Label(
                score_frame,
                text="Puntaje",
                font=c.FUENTE_ETIQUETA_PUNTAJE
            ).grid(row=0)
            self.score_label = tk.Label(score_frame, text="0", font=c.FUENTE_PUNTAJE)
            self.score_label.grid(row=1)

        def empzr_jg(self):
            self.matriz = [[0] * 4 for _ in range(4)]

            row = random.randint(0, 3)
            col = random.randint(0, 3)
            self.matriz[row][col] = 2
            self.cells[row][col]["frame"].configure(bg=c.COLORES_CELDA[2])
            self.cells[row][col]["number"].configure(
                bg=c.COLORES_CELDA[2],
                fg=c.COLORES_NUMERO_CELDA[2],
                font=c.FUENTES_NUMERO_CELDA[2],
                text="2"
            )
            while(self.matriz[row][col] != 0):
                row = random.randint(0, 3)
                col = random.randint(0,3)
            self.matriz[row][col] = 2
            self.cells[row][col]["frame"].configure(bg=c.COLORES_CELDA[2])
            self.cells[row][col]["number"].configure(
                bg=c.COLORES_CELDA[2],
                fg=c.COLORES_NUMERO_CELDA[2],
                font=c.FUENTES_NUMERO_CELDA[2],
                text="2"
            )

            self.score = 0

        def apilar(self):
            nueva_matriz = [[0] * 4 for _ in range(4)]
            for i in range(4):
                pos_llena = 0
                for j in range(4):
                    if self.matriz[i][j] !=0:
                        nueva_matriz[i][pos_llena] = self.matriz[i][j]
                        pos_llena += 1
            self.matriz = nueva_matriz

        def combinar(self):
            for i in range(4):
                for j in range(3):
                    if self.matriz[i][j] != 0 and self.matriz[i][j] == self.matriz[i][j + 1]:
                        self.matriz[i][j] *= 2
                        self.matriz[i][j + 1] = 0
                        self.score += self.matriz[i][j]
        
        def reversa(self):
            nueva_matriz = []
            for i in range(4):
                nueva_matriz.append([])
                for j in range(4):
                    nueva_matriz[i].append(self.matriz[i][3 - j])
            self.matriz = nueva_matriz        

        def transponer(self):
            nueva_matriz = [[0] * 4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    nueva_matriz[i][j] = self.matriz[j][i]
            self.matriz = nueva_matriz

        def agrgr_loza(self):
            if any(0 in row for row in self.matriz):
                row = random.randint(0, 3)
                col = random.randint(0, 3)
                while(self.matriz[row][col] != 0):
                    row = random.randint(0, 3)
                    col = random.randint(0,3)
                self.matriz[row][col] = random.choice([2, 4])
        
        def act_intrfz(self):
            global puntaje 
            for i in range(4):
                for j in range(4):
                    cell_value = self.matriz[i][j]
                    if cell_value == 0:
                        self.cells[i][j]["frame"].configure(bg=c.COLOR_CELDA_VACIA)
                        self.cells[i][j]["number"].configure(bg=c.COLOR_CELDA_VACIA, text="")
                    else:
                        self.cells[i][j]["frame"].configure(bg=c.COLORES_CELDA[cell_value])
                        self.cells[i][j]["number"].configure(
                            bg=c.COLORES_CELDA[cell_value],
                            fg=c.COLORES_NUMERO_CELDA[cell_value],
                            font=c.FUENTES_NUMERO_CELDA[cell_value],
                            text=str(cell_value)
                        )
            self.score_label.configure(text=self.score)
            self.update_idletasks()
            puntaje=self.score


        def left(self, event):
            self.apilar()
            self.combinar()
            self.apilar()
            self.agrgr_loza()
            self.act_intrfz()
            self.fin_juego()

        
        def right(self, event):
            self.reversa()
            self.apilar()
            self.combinar()
            self.apilar()
            self.reversa()
            self.agrgr_loza()
            self.act_intrfz()
            self.fin_juego()

        
        def up(self, event):
            self.transponer()
            self.apilar()
            self.combinar()
            self.apilar()
            self.transponer()
            self.agrgr_loza()
            self.act_intrfz()
            self.fin_juego()


        def down(self, event):
            self.transponer()
            self.reversa()
            self.apilar()
            self.combinar()
            self.apilar()
            self.reversa()
            self.transponer()
            self.agrgr_loza()
            self.act_intrfz()
            self.fin_juego()

        def movs_hor(self):
            for i in range(4):
                for j in range(3):
                    if self.matriz[i][j] == self.matriz[i][j + 1]:
                        return True
            return False

        def movs_vert(self):
            for i in range(3):
                for j in range(4):
                    if self.matriz[i][j] == self.matriz[i + 1][j]:
                        return True
            return False

        def fin_juego(self):
            global empezar
            if any(2048 in row for row in self.matriz):
                casilla_fin_juego = tk.Frame(self.main_grid, borderwidth=2)
                casilla_fin_juego.place(relx=0.5, rely=0.5, anchor="center")
                tk.Label(
                    casilla_fin_juego,
                    text="¡Felicitaciones, ganaste!",
                    bg=c.FONDO_GANAR,
                    fg=c.COLOR_FUENTE_FIN_JUEGO,
                    font=c.FUENTE_FIN_JUEGO
                ).pack()

            elif not any(0 in row for row in self.matriz) and not self.movs_hor() and not self.movs_vert():
                global empezar
                casilla_fin_juego = tk.Frame(self.main_grid, borderwidth=2)
                casilla_fin_juego.place(relx=0.5, rely=0.5, anchor="center")
                tk.Label(
                    casilla_fin_juego,
                    text="Fin del juego...",
                    bg=c.FONDO_PERDER,
                    fg=c.COLOR_FUENTE_FIN_JUEGO,
                    font=c.FUENTE_FIN_JUEGO
                ).pack()

def juego():
    inicio()

    def main():
        Game()

    if __name__ == "__main__":
        main()

    def puntuacion():
        guarda_puntaje()

    def conectar():
        global cur
        global conn
        conn = sqlite3.connect('puntajes.db')
        cur=conn.cursor()
        create_table()

    def create_table():
        cur.execute('CREATE TABLE IF NOT EXISTS puntuación (Usuario TEXT, Puntaje REAL)')

    def guarda_puntaje():
        conectar()
        global cur
        global puntaje
        global usuarioin
        global conn
        cur.execute("INSERT INTO puntuación (Usuario, Puntaje) VALUES (?, ?)",
        (usuarioin, puntaje))
        conn.commit()
        print(f"Felicidades {usuarioin} ha obtenido {puntaje} puntos!")
        time.sleep(3)
        delscr()
        mostrar_puntajes()

    def mostrar_puntajes():
        conectar()
        global cur
        sqlite_select_query = """SELECT * from puntuación"""
        cur.execute(sqlite_select_query)
        registros = cur.fetchall()
        print("Los puntajes registrados hasta el momento son:")
        print("\n")
        for row in registros:
            print("Usuario: ", row[0]) 
            print(f"Puntaje: {row[1]} Puntos")
            print("\n")
        time.sleep(3)
        z=input("¿Desea volver al menú? (s/n) ")
        if z=="s":
            cur.close()
            conn.close()
            juego()
        else:
            print("Saliendo del programa...")
            time.sleep(3)
            delscr()
            cur.close()
            conn.close()
            sys.exit
    
    puntuacion()

juego()

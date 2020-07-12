import tkinter as tk
import colores as c
import random


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
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matriz[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0,3)
        self.matriz[row][col] = random.choice([2, 4])
    
    def act_intrfz(self):
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
            casilla_fin_juego = tk.Frame(self.main_grid, borderwidth=2)
            casilla_fin_juego.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                casilla_fin_juego,
                text="Fin del juego...",
                bg=c.FONDO_PERDER,
                fg=c.COLOR_FUENTE_FIN_JUEGO,
                font=c.FUENTE_FIN_JUEGO
            ).pack()

def main():
    Game()

if __name__ == "__main__":
    main()
from graphics import *
from plot_proj import *


def home(window):
    home.txt = Text(Point(400,50),"Input Plot")
    home.txt.setSize(20)
    home.txt.draw(window)
    home.escolha = Text(Point(400,100),"Escolha qual função você quer fazer um gráfico:")
    home.escolha.draw(window)
    home.rect = Rectangle(Point(100,200),Point(300,300))
    home.center = home.rect.getCenter()
    home.rect.draw(window)
    home.calc_2d = Text(home.center, "Calculadora 2D")
    home.calc_2d.setSize(15)
    home.calc_2d.draw(window)
    home.rect2 = Rectangle(Point(500,200),Point(700,300))
    home.center2 = home.rect2.getCenter()
    home.rect2.draw(window)
    home.calc_3d = Text(home.center2, "Calculadora 3D")
    home.calc_3d.setSize(15)
    home.calc_3d.draw(window)

def undraw_home():
    home.txt.undraw()
    home.escolha.undraw()
    home.rect.undraw()
    home.calc_2d.undraw()
    home.rect2.undraw()
    home.calc_3d.undraw()

def entrada_2d(window):
    undraw_home()
    input_box = Entry(Point(400,300),20)
    input_box.draw(window)

def entrada_3d(window):
    undraw_home()
    input_box = Entry(Point(400,300),20)
    input_box.draw(window)
    txt = Text(Point(600,300),"texto teste")
    txt.draw(window)


def main():
    win = GraphWin("Input Plot", 800, 600,autoflush = False)
    #img = Image(Point(50,50),'function2d.png')
    #img.draw(win)
    #entrada_2d(win)
    home(win)
    while True:
        mouse = win.checkMouse()
        if mouse is not None:
            x = mouse.getX()
            y = mouse.getY()
            if x >= 100 and x <= 300 and y >= 200 and y <= 300:
                entrada_2d(win)
                break
            elif x >= 500 and x <= 700 and y >= 200 and y <= 300:
                entrada_3d(win)
                break
            update(15)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
    
if __name__ == "__main__":
    main()

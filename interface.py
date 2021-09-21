from graphics import *
from plot_proj import *
#Aluno : Gabriel Viana da Silva
#Matrícula: 149350
#Data : 21/09/2021
##### Interface ainda em desenvolvimento ####
def home(window):
    txt = Text(Point(400,50),"Input Plot")
    txt.setSize(20)
    txt.draw(window)
    escolha = Text(Point(400,100),"Escolha qual função você quer fazer um gráfico:")
    escolha.draw(window)
    rect = Rectangle(Point(100,200),Point(300,300))
    center = rect.getCenter()
    rect.draw(window)
    calc_2d = Text(center,"Calculadora 2D")
    calc_2d.setSize(15)
    calc_2d.draw(window)
    rect2 = Rectangle(Point(500,200),Point(700,300))
    center2 = rect2.getCenter()
    rect2.draw(window)
    calc_3d = Text(center2, "Calculadora 3D")
    calc_3d.setSize(15)
    calc_3d.draw(window)

def clear(window):
    for item in window.items[:]:
        item.undraw()
    window.update()

def entrada_2d(window):
    clear(window)
    input_box = Entry(Point(400,500),20)
    input_box.draw(window)
    go = Rectangle(Point(500,485),Point(530,510))
    go.draw(window)
    txt_go = Text(go.getCenter(),'Go')
    txt_go.draw(window)
    dx = Rectangle(Point(460,520),Point(530,540))
    dx.draw(window)
    txt_dx = Text(dx.getCenter(),"Derivada")
    txt_dx.draw(window)
    home_bt = Rectangle(Point(700,580),Point(795,595))
    home_bt.draw(window)
    txt_home = Text(home_bt.getCenter(),"Tela inicial")
    txt_home.draw(window)
    while True:
        input_mouse = window.checkMouse()
        if input_mouse is not None:
            in_x = input_mouse.getX()
            in_y = input_mouse.getY()
            if in_x >= 500 and in_x <= 530 and in_y >= 485 and in_y <= 510:
                expr = input_box.getText()
                plot_2dim(to_expression(expr))
                img = Image(Point(400,240),"function2d.png")
                img.draw(window)
            elif in_x >= 460 and in_x <= 530 and in_y >= 520 and in_y <= 530:
                expr = input_box.getText()
                derivada(to_expression(expr))
                dx_graph = Image(Point(400,240),"deriv.png")
                dx_graph.draw(window)

            if in_x >= 700 and in_x <= 795 and in_y >= 580 and in_y <= 595:
                clear(window)
                home(window)
                begin(window)
    
def entrada_3d(window):
    clear(window)
    input_box = Entry(Point(400,300),20)
    input_box.draw(window)
    txt = Text(Point(600,300),"texto teste")
    txt.draw(window)

def begin(window):
    while True:
        mouse = window.checkMouse()
        print(mouse)
        if mouse is not None:
            x = mouse.getX()
            y = mouse.getY()
            if x >= 100 and x <= 300 and y >= 200 and y <= 300:
                entrada_2d(window)
            elif x >= 500 and x <= 700 and y >= 200 and y <= 300:
                entrada_3d(window)
            update(15)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def main():
    win = GraphWin("Input Plot", 800, 600,autoflush = False)
    #img = Image(Point(50,50),'function2d.png')
    #img.draw(win)
    #entrada_2d(win)
    home(win)
    begin(win)
    
if __name__ == "__main__":
    main()

from graphics import *
from plot_proj import *
#Aluno : Gabriel Viana da Silva
#Matrícula: 149350
#Data : 21/09/2021
##### Interface ainda em desenvolvimento ####
def ajuda(window):
    clear(window)
    home_bt = Rectangle(Point(700,580),Point(795,595))
    home_bt.draw(window)
    txt_home = Text(home_bt.getCenter(),"Tela inicial")
    txt_home.draw(window)
    calc2_hlp = Text(Point(80,80),"Calculadora 2D\n\nExemplos:\n\n1/x\nx**2\nsin(x)\nsqrt(x)")
    calc2_hlp.draw(window)
    calc3_hlp = Text(Point(720,80),"Calculadora 3D\n\nExemplos:\n\nx*y\nx*y**2\nsin(x)/cos(y)\nexp(y)*log(x)\nsin(x)**cos(y)")
    calc3_hlp.draw(window)
    while True:
        mouse = window.checkMouse()
        if mouse is not None:
            in_x = mouse.getX()
            in_y = mouse.getY()
            if in_x >= 700 and in_x <= 795 and in_y >= 580 and in_y <= 595:
                    clear(window)
                    home(window)
                    begin(window)

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
    help_bt = Rectangle(Point(700,580),Point(795,595))
    help_bt.draw(window)
    txt_help = Text(help_bt.getCenter(),"Ajuda")
    txt_help.draw(window)

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
        try:
            input_mouse = window.checkMouse()
            if input_mouse is not None:
                in_x = input_mouse.getX()
                in_y = input_mouse.getY()
                if in_x >= 500 and in_x <= 530 and in_y >= 485 and in_y <= 510:
                    try:
                        expr = input_box.getText()
                        plot_2dim(to_expression(expr))
                        img = Image(Point(400,240),"function2d.png")
                        img.draw(window)
                    except:
                        pass
                elif in_x >= 460 and in_x <= 530 and in_y >= 520 and in_y <= 530:
                    try:
                        expr = input_box.getText()
                        derivada(expr)
                        dx_graph = Image(Point(400,240),"deriv.png")
                        dx_graph.draw(window)
                    except:
                        pass
                if in_x >= 700 and in_x <= 795 and in_y >= 580 and in_y <= 595:
                    clear(window)
                    home(window)
                    begin(window)
        except:
            img.undraw()
            dx_graph.undraw()
            err = Text(Point(400,240),"Função não valida")
            err.draw(window)

            
    
def entrada_3d(window):
    clear(window)
    input_box = Entry(Point(400,500),20)
    input_box.draw(window)
    go = Rectangle(Point(500,485),Point(530,510))
    go.draw(window)
    txt_go = Text(go.getCenter(),'Go')
    txt_go.draw(window)
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
                try:
                    expr = input_box.getText()
                    plot_3dim(to_expression(expr))
                    img = Image(Point(400,240),"function3d.png")
                    img.draw(window)
                except:
                    err = Text(Point(400,240),"Função não valida")
                    err.draw(window)
            
            if in_x >= 700 and in_x <= 795 and in_y >= 580 and in_y <= 595:
                clear(window)
                home(window)
                begin(window)


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
            elif x >= 700 and x <= 795 and y >= 580 and y <= 595:
                ajuda(window)
            update(15)

def main():
    win = GraphWin("Input Plot", 800, 600,autoflush = False)
    #img = Image(Point(50,50),'function2d.png')
    #img.draw(win)
    #entrada_2d(win)
    home(win)
    begin(win)
    
if __name__ == "__main__":
    main()

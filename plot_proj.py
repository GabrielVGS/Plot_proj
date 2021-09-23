import sympy as sy
from sympy.plotting import plot,plot3d
from sympy import Derivative


def to_expression(expr):
    assert isinstance(expr,str), "Uma string não foi inserida na função"
    return sy.parse_expr(expr,evaluate=False)
    
def plot_2dim(express):
    '''Plota uma função em 2d e salva ela no computador,
    Exemplo: x**2'''
    graph2d = plot(express,show = False,xlim=[-10,10],ylim=[-10,10])
    graph2d.save("function2d.png")
        #return "Expressão inválida"

def plot_3dim(express):
    '''Plota uma função em 3d e salva ela no computador,
    Exemplo: x**2 + y*x
    Exemplo2: (x*y)**2'''
    try:
        graph3d = plot3d(express,show = False)
        graph3d.save('function3d.png')
    except:
        return "Expressão inválida"


def derivada(express):
    try:
        d = Derivative(express)
        deriv = d.doit()
        func = plot(express,show = False,xlim=[-10,10],ylim=[-10,10])
        derivada_img = plot(deriv,show = False,line_color='red',xlim=[-10,10],ylim=[-10,10])
        func.extend(derivada_img)
        func.save("deriv.png")
    except:
        return "Expressão inválida"

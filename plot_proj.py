import matplotlib.pyplot as plt
import sympy as sy
from sympy.plotting import plot,plot3d
from sympy import Derivative


def to_expression(expr):
    assert isinstance(expr,str), "Uma string não foi inserida na função"
    return sy.parse_expr(expr,evaluate=False)
    
def plot_2dim(express):
    '''Plota uma função em 2d e salva ela no computador,
    Exemplo: x**2'''
    graph2d = plot(express)
    graph2d.save("function2d.png")

def plot_3dim(express):
    '''Plota uma função em 3d e salva ela no computador,
    Exemplo: x**2 + y*x
    Exemplo2: x*y'''
    ### Função ainda em desenvolvimento  ###
    graph3d = plot3d(express)
    graph3d.save('function3d.png')
    ### Função ainda em desenvolvimento ###


def derivada(express):
    d = Derivative(express)
    deriv = d.doit()
    derivada_img = plot(deriv)
    derivada_img.save("deriv.png")
    ###Função em desenvolvimento###
    
derivada("g**2")

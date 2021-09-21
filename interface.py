from graphics import *
from plot_proj import *



def main():
    win = GraphWin("My Circle", 100, 100)
    img = Image(Point(50,50),'function2d.png')
    img.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
    
if __name__ == "__main__":
    main()

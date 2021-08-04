import numpy as np
import matplotlib.pyplot as plt


def velocity(v0, a, t):
    return (v0 + a*t)


def plot_dis(x,y, title, xlabel, ylabel, plot_name):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(plot_name)


def main():
    v0 = 10
    t = np.arange(0,2,0.1)
    a = -10
    vel = velocity(v0, a, t)

    plt.plot(t, vel)
    plt.title('Good/Nice/Perfect/Beautifool Plot')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.savefig('GoodPlot.pdf')


if __name__ == "__main__":
    main()
    

import numpy as np
import matplotlib.pyplot as plt


def velocity(v0, a, t):
    return (v0 + a*t)

def displacement(s0, v0, a, t):
    return (s0 + v0*t + 0.5*a*t**2)

def plot_fig(x,y, title, xlabel, ylabel, plot_name):
    plt.grid(alpha = 0.3)
    plt.plot(x, y, 'go', ls='-', label= ylabel[:3])
    plt.legend()    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(plot_name)
    plt.close()


def main():
    v0 = 10
    t = np.arange(0,2,0.1)
    a = -10
    vel = velocity(v0, a, t)
    s0 = 0
    dis = displacement(s0, v0, a, t)

    plot_fig(t, dis, "Displacement Vs Time plot", 'Time (sec)', "Displacement (m)", "Dis_plot.pdf")
    plot_fig(t, vel, "Velocity Vs Time plot", 'Time (sec)', "Velocity (m/s)", "Vel_plot.pdf")


if __name__ == "__main__":
    main()
    

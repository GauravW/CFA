import numpy as np
import matplotlib.pyplot as plt

def velocity(v0, a, t):
    return (v0 + a*t)


def main():
    v0 = 0
    t = np.arange(0,100,1)
    a = -10
    vel = velocity(v0, a, t)

    plt.plot(t, vel)
    plt.title('Good/Nice/Perfect/Beautifool Plot')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.savefig('GoodPlot.pdf')


if __name__ == "__main__":
    main()
    

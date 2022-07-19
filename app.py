import numpy as np
import matplotlib.pyplot as plt

delta_t = 0.01
steps = 1000
k = 1
m = 1
x0 = 1
v0 = 2


def a(x):
    return - (k * x / m)


def leap_fiog_method(steps, delta_t, v0, x0, a):
    v = [v0]
    x = [x0]
    t_interval = [0]

    vt_2 = v0 + a(x0) * (delta_t/2)

    for i in range(1, steps):
        x_next = x[i - 1] + vt_2 * delta_t
        v_next_2 = vt_2 + a(x_next) * (delta_t)

        v.append((v_next_2 + vt_2) / 2)
        x.append(x_next)
        t_interval.append((i-1)*delta_t)

        vt_2 = v_next_2

    return {"v": v, "x": x, 't': t_interval}


leap_fiog = leap_fiog_method(steps, delta_t, v0, x0, a)


plt.plot(leap_fiog["t"], leap_fiog["v"])
plt.plot(leap_fiog["t"], leap_fiog["x"])
plt.show()

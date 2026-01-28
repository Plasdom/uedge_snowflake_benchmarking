import numpy as np
import freeqdsk
import matplotlib.pyplot as plt


def psi_analytic(x, y, x0, y0, a0=0.1):

    dist_sq = (x - x0) ** 2 + (y - y0) ** 2
    dist = np.sqrt(dist_sq)
    a0_sq = a0**2
    res = np.zeros(x.shape)
    res = np.log(dist)
    res[np.where(dist_sq < a0_sq)] = 0.5 * (
        dist_sq[np.where(dist_sq < a0_sq)] / a0_sq - 1.0
    ) + np.log(a0)
    return res


def psi_analytic3(x, y, p1, p2, p3, i1, i2, i3):
    psi = i1 * psi_analytic(x, y, p1[0], p1[1])
    psi += i2 * psi_analytic(x, y, p2[0], p2[1])
    psi += i3 * psi_analytic(x, y, p3[0], p3[1])

    return psi


def generate_analytic_snowflake(
    template: str,
    savepath: str,
    R0_offset: float = 0.0,
    i1: float = 0.05,
    i2: float = 0.015,
    i3: float = 0.02,
    p1: tuple = None,
    p2: tuple = None,
    p3: tuple = None,
    plot: bool = False,
):
    """Modify an existing geqdsk file and replace the magnetic equilbrium with an analytic solution to the vacuum poloidal field around three current filaments with currents i1, i2, i3.

    :param template: Filepath to an existing geqdsk file which will be used as a template
    :param savepath: Filepath where the modified geqdsk file will be saved
    :param R0_offset: Major radius offset [m]. Set to very large value to minimise toroidal geometry effects in the resultant equilibrium, defaults to 10000.0
    :param i1: Current through filament 1, defaults to 0.05
    :param i2: Current through filament 1, defaults to 0.015
    :param i3: Current through filament 1, defaults to 0.02
    :param plot: whether to plot the resultant flux contours, defaults to False
    """
    with open(template, "r") as f:
        gf = freeqdsk.geqdsk.read(f)

    # Create a SF
    X = gf.r_grid + R0_offset
    Y = gf.z_grid
    if p1 is None:
        p1 = (1.0 + R0_offset, gf.zmagx)
    if p2 is None:
        p2 = (0.6 + R0_offset, gf.zmagx - 1.5)
    if p3 is None:
        p3 = (1.4 + R0_offset, gf.zmagx - 1.5)
    psi = psi_analytic3(X, Y, p1, p2, p3, i1, i2, i3)

    gf.psi = psi * (R0_offset + gf.rmagx) / gf.rmagx
    gf.rbdry += R0_offset
    gf.rlim += R0_offset
    gf.rmagx = 1.0 + R0_offset
    gf.rleft += R0_offset
    gf.rcentr += R0_offset
    with open(savepath, "w") as f:
        freeqdsk.geqdsk.write(gf, f)

    if plot:
        fig, ax = plt.subplots(1)
        ax.contour(X, Y, psi, levels=50)
        ax.set_aspect("equal")
        ax.set_xlabel("R")
        ax.set_ylabel("Z")
        ax.set_title("Flux surfaces")
        plt.show()

import casadi


def robertson_ode(ngroups: int) -> dict:
    x = casadi.MX.sym("x", ngroups)
    y = casadi.MX.sym("y", ngroups)
    z = casadi.MX.sym("z", ngroups)
    k1 = 0.04
    k2 = 30000000
    k3 = 10000

    # Expression for ODE right-hand side
    f0 = -k1 * x + k3 * y * z
    f1 = k1 * x - k2 * y**2 - k3 * y * z
    f2 = k2 * y**2

    ode = {}  # ODE declaration
    ode["x"] = casadi.vertcat(x, y, z)  # states
    ode["ode"] = casadi.vertcat(f0, f1, f2)  # right-hand side

    return ode


def robertson() -> dict:
    x = casadi.MX.sym("x", 1)
    y = casadi.MX.sym("y", 1)
    z = casadi.MX.sym("z", 1)
    k1 = 0.04
    k2 = 30000000
    k3 = 10000

    # Expression for ODE right-hand side
    f0 = -k1 * x + k3 * y * z
    f1 = (k1 * x - k3 * y * z - k2 * y * y,)

    # algebraic equation
    f2 = 1.0 - x - y - z

    ode = {}  # ODE declaration
    ode["xy"] = casadi.vertcat(x, y)  # states
    ode["z"] = z  # algebraic
    ode["ode"] = casadi.vertcat(f0, f1)  # right-hand side
    ode["alg"] = f2  # algebraic equation

    return ode

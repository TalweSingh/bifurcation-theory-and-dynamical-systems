import scipy

def model(t, y, beta, alpha, gamma, N):
    S, E, I, R, C = y
    dSdt = -beta * S * (I/N)
    dEdt = beta * S * (I/N) - alpha * E
    dIdt = alpha * E - gamma * I
    dRdt = gamma * I
    dCdt = alpha * E  # -dSdt    # check if correct
    return dSdt, dEdt, dIdt, dRdt, dCdt

def solve(y, x, N, t_eval):
    '''
    Solves seir model.

    t : [t_start, t_end]
    x : [beta, alpha, gamma, I_0]
    y : [S, E, I, R, C]

    #TODO: add timespan/evaluation points
    '''
    sol = scipy.integrate.solve_ivp(model, [t_eval[0], t_eval[-1]], y, args=(x[0], x[1], x[2], N), t_eval=t_eval)
    return sol
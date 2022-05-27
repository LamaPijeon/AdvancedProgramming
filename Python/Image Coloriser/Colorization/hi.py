import numpy as np

def stochastic_sample(xs, ys):
    perm = np.random.permutation(len(xs))
    x = xs[perm[0]]
    y = ys[perm[0]]

    return x, y

def adam(model, xs, ys, learning_rate = 0.1, b1 = 0.9, b2 = 0.999, epsilon = 0.00000001, max_iteration = 1000):
    """
        Adam: This is the adam optimizer that build upon adadelta and RMSProp
        model: The model we want to optimize the parameter on
        xs: the feature of my dataset
        ys: the continous value (target)
        learning_rate: the amount of learning we want to happen at each time step (default is 0.1 and will be updated by the optimizer)
        b1: this is the first decaying average with proposed default value of 0.9 (deep learning purposes)
        b2: this is the second decaying average with proposed default value of 0.999 (deep learning purposes)
        epsilon: a variable for numerical stability during the division
        max_iteration: the number of sgd round we want to do before stopping the optimization
    """
    # Variable Initialization
    num_param = len(model.weights)
    m = [0 for _ in range(num_param)] # two m for each parameter
    v = [0 for _ in range(num_param)] # two v for each parameter
    g = [0 for _ in range(num_param)] # two gradient
    
    for t in range(1,max_iteration):
        
        # Calculate the gradients 
        x, y = stochastic_sample(xs, ys)
        
        # Get the partial derivatives
        g = model.derivate(x, y)

        # Update the m and v parameter
        m = [b1*m_i + (1 - b1)*g_i for m_i, g_i in zip(m, g)]
        v = [b2*v_i + (1 - b2)*(g_i**2) for v_i, g_i in zip(v, g)]

        # Bias correction for m and v
        m_cor = [m_i / (1 - (b1**t)) for m_i in m]
        v_cor = [v_i / (1 - (b2**t)) for v_i in v]

        # Update the parameter
        model.weights = [weight - (learning_rate / (np.sqrt(v_cor_i) + epsilon))*m_cor_i for weight, v_cor_i, m_cor_i in zip(model.weights, v_cor, m_cor)]
        
        if t % 100 == 0:
            print(f"Iteration {t}")
            print(model)
import numpy as np
from Kroup_func import kroupa01_norm

def generate_star_mass_data(mass_min, mass_max, N_p):
    """
    Generates simulated stellar mass data using the Kroupa (2001) Initial Mass Function (IMF).

    Parameters:
    ----------
    mass_min : float
        Minimum stellar mass to generate (in units of Msun).
    mass_max : float
        Maximum stellar mass to generate (in units of Msun).
    N_p : int
        Total number of stars to simulate.

    Returns:
    -------
    tuple
        - M_in : array-like
            Array containing the stellar masses selected according to the IMF.
        - prob_val : array-like
            Probability values associated with the generated stellar masses.
    """
    random_p = np.random.uniform(0, 1, N_p)
    
    random_mass = np.random.uniform(mass_min, mass_max, N_p)

    M_in = random_mass[random_p < kroupa01_norm(random_mass)]
    prob_val = random_p[random_p < kroupa01_norm(random_mass)]

    return M_in, prob_val


def generate_times(masses):
    """
    Generates times related to stellar evolution based on stellar masses.

    Parameters:
    ----------
    masses : array-like
        Array or list of generated stellar masses (in units of Msun).

    Returns:
    -------
    tuple
        - born_time : array-like
            Formation times of the stars (in Myr).
        - t_alive : array-like
            Total time the star has lived up to the present (in Myr).
        - t_out_ms : array-like
            Difference between the main-sequence time and the lived time (in Myr).
            if t_out_ms<0, the star is out of the MS, i.e. t_alive > t_ms.
    """
    
    born_time = np.random.uniform(0, 13600, len(masses))
    
    t_ms = ((10**10) / (masses**2.5)) * 1e-6  # in MYr
    
    t_alive = 13600 - born_time
    
    t_out_ms = t_alive - t_ms
    
    return born_time, t_alive, t_out_ms

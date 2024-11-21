import numpy as np

def kroupa01_normal(m):
    """
    Computes the Kroupa (2001) Initial Mass Function (IMF) for stellar masses.

    This function defines the IMF as a piecewise power law:
    -  m^{-0.3}  for  m < 0.08 
    -  m^{-1.3}  for  0.08 <= m < 0.5 
    -  m^{-2.3}  for  m >= 0.5 

    Parameters:
    ----------
    m : array-like or float
        Stellar mass or array of stellar masses (in units of Msun).

    Returns:
    -------
    array-like or float
        The value of the IMF for the given stellar mass(es).
    """
    return np.where(m < 0.08, m**-0.3, 
                    np.where(m < 0.5, 0.08**-0.3 * (m / 0.08)**-1.3, 
                            0.08**-0.3 * (0.5 / 0.08)**-1.3 * (m / 0.5)**-2.3))

# Definir la función de probabilidad normalizada
def kroupa01_norm(m):
    """
    Computes the normalized Kroupa (2001) IMF.

    This function normalizes the Kroupa IMF by dividing the values of `kroupa01_normal` 
    by the value at m = 0.08, ensuring that the IMF is properly scaled.

    Parameters:
    ----------
    m : array-like or float
        Stellar mass or array of stellar masses (in units of Msun).

    Returns:
    -------
    array-like or float
        The normalized IMF value for the given stellar mass(es).
    """
    return kroupa01_normal(m) / kroupa01_normal(0.08)
import numpy as np

def remanent_classifier(masses, t_out_ms):
    """
    Classifies initial masses into WD, NS, or BH, according the initial mass.

    Parameters:
        masses (array-like): Array or list of initial stellar masses.
        indicators (array-like): Array or list of compact object indicators.
        
    Returns:
        np.ndarray: Array with indicators for each remanent;
         - 0: Main Sequence
         - 1: White Dwarf
         - 2: Neutro Star
         - 3: Black Hole
    """
    # Inicializar un array de ceros con el mismo tamaño que masses
    # Este array almacenará las clasificaciones de los objetos compactos
    indicators = np.zeros_like(masses, dtype=int)

    # Máscara que identifica estrellas fuera de la secuencia principal (t_out_ms < 0)
    stars_out_ms = t_out_ms < 0

    # Clasificar en enanas blancas: 0 < mass < 8 y fuera de la secuencia principal
    indicators[stars_out_ms & (masses > 0) & (masses < 8)] = 1

    # Clasificar en estrellas de neutrones: 8 < mass < 20 y fuera de la secuencia principal
    indicators[stars_out_ms & (masses > 8) & (masses < 20)] = 2

    # Clasificar en agujeros negros: 20 < mass < 100 y fuera de la secuencia principal
    indicators[stars_out_ms & (masses > 20) & (masses < 100)] = 3

    # Retornar el array de indicadores con las clasificaciones
    return indicators



def remanent_mass(masses,indicators):
    """
    Caluclate de final mass of the remanent based in the initial mass, using 
    the studys of:
    - Kalirai (2008) - https://arxiv.org/abs/0706.3894
    - Raithel (2018) - https://iopscience.iop.org/article/10.3847/1538-4357/aab09b

    Parameters:
        masses (array-like): Array or list with initial masses
        indicators (array-like): Array or list with remanent indicator;
        - 0: Main Sequence
        - 1: White Dwarf
        - 2: Neutro Star
        - 3: Black Hole
        
    Returns:
        np.ndarray: Array with final masses. Stars that are not yet remanent (indicator = 0) are assigned a value of -1.
    """
    masses = np.asarray(masses)
    final_masses = np.full_like(masses, None, dtype=object)  # Inicializar array con None

    # White Dwarf (WD)
    cond_WD = (masses < 9) & (indicators==1)
    final_masses[cond_WD] = 0.109 * masses[cond_WD] + 0.394

    # Neutron Star (NS)
    NS_type = (indicators==2) 
    cond_NS1 = (9 <= masses) & (masses <= 13) & NS_type
    final_masses[cond_NS1] = (
        2.24 + 0.508 * (masses[cond_NS1] - 14.75)
        + 0.125 * (masses[cond_NS1] - 14.75) ** 2
        + 0.011 * (masses[cond_NS1] - 14.75) ** 3
    )

    cond_NS2 = (13 < masses) & (masses < 15)& NS_type
    final_masses[cond_NS2] = 0.123 + 0.112 * masses[cond_NS2]

    cond_NS3 = (15 <= masses) & (masses < 17.8)& NS_type
    final_masses[cond_NS3] = 0.996 + 0.0384 * masses[cond_NS3]

    cond_NS4 = (17.8 <= masses) & (masses < 18.5)& NS_type
    final_masses[cond_NS4] = -0.020 + 0.10 * masses[cond_NS4]

    cond_NS5 = (18.5 <= masses) & (masses < 21.7)& NS_type
    final_masses[cond_NS5] = np.random.normal(1.6, 0.158, size=np.sum(cond_NS5))

    cond_NS6 = (25.2 <= masses) & (masses < 27.5)& NS_type
    final_masses[cond_NS6] = ( 3232.29 - 409.429*(masses[cond_NS6] - 2.619) + 17.2867*(masses[cond_NS6] - 2.619)**2 - 0.24315*(masses[cond_NS6] - 2.619)**3 )

    cond_NS7 = (60 <= masses) & (masses <= 120) & NS_type
    final_masses[cond_NS7] = np.random.normal(1.78, 0.02, size=np.sum(cond_NS7))

    # Black Hole (BH)
    BH_type = (indicators==3) 
    cond_BH1 = (15 <= masses) & (masses <= 40) & BH_type
    M_BH_core_low = -2.049 + 0.4140*masses[cond_BH1]
    M_BH_all = (15.52 - 0.3294*(masses[cond_BH1] - 25.97) - 0.02121*(masses[cond_BH1] - 25.97)**2 + 0.003120*(masses[cond_BH1] - 25.97)**3 )
    final_masses[cond_BH1] = 0.9*M_BH_core_low + (1 - 0.9)*M_BH_all

    cond_BH2 = (45 <= masses) & (masses <= 120) & BH_type
    final_masses[cond_BH2] = 5.697 + 7.8598 * 10**8 * (masses[cond_BH2])**-4.858

    final_masses[indicators==0] = -1

    return final_masses
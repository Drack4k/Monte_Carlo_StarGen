from Kroup_func import kroupa01_norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_mass(masses, prob_val, mass_min, mass_max):
    """
    Generates a plot comparing the normalized Kroupa initial mass function (IMF)
    to the generated masses.

    Parameters:
    ----------
    masses : array-like
        Array or list of generated stellar masses.
    prob_val : array-like
        Probability values associated with the generated masses.
    mass_min : float
        Minimum mass for generating the IMF.
    mass_max : float
        Maximum mass for generating the IMF.

    Returns:
    -------
    int
        Returns 0 upon completion.
    """
    mass_model = np.logspace(np.log10(mass_min), np.log10(mass_max), 400)
    pdf_kroupa = kroupa01_norm(mass_model)

    plt.plot(mass_model, pdf_kroupa, label='Normalized Kroupa01 IMF')
    plt.scatter(masses, prob_val, label='Generated Stars', s=2, c="black")
    plt.yscale('log')
    plt.xscale('log')
    plt.legend(loc='best', prop=dict(size=8))
    plt.xlabel('Mass [$M_\odot$]')
    plt.ylabel(r'Norm. Mass Function $\xi(m)\Delta m$')
    return 0


def plot_mass_histogram(masses):
    """
    Generates a histogram of stellar masses in logarithmic scale.

    Parameters:
    ----------
    masses : array-like
        Array or list of generated stellar masses.

    Returns:
    -------
    int
        Returns 0 upon completion.
    """
    sns.histplot(np.log10(masses), color="blue", bins=150, kde=False, alpha=0.5)
    plt.title("Generated Mass Distribution")
    plt.xlabel("Log. Mass [$M_\odot$]")
    return 0


def plot_born_times_histogram(born_time):
    """
    Generates a histogram of stellar birth times.

    Parameters:
    ----------
    born_time : array-like
        Array or list of stellar birth times.

    Returns:
    -------
    int
        Returns 0 upon completion.
    """
    sns.histplot(born_time, color="green", bins=150, kde=False, alpha=0.5)
    plt.title("Generated Born Time Distribution")
    plt.xlabel("Born Time [Myr]")
    return 0


def plot_mass_histogram_per_remanent(masses,ind):
    """
    Plots histograms of initial masses for different stellar remnant types
    with logarithmic scales on both axes.

    Parameters
    ----------
    masses : array-like
        Array containing the masses of stars.
    ind : array-like
        Array of indices indicating the remnant type for each star:
        - 0: Main Sequence
        - 1: White Dwarf
        - 2: Neutron Star
        - 3: Black Hole

    Returns
    -------
    int
        Returns 0 upon completion.
    """
    
    plt.hist(masses[ind==0], bins=100, histtype='step',density=True, color='blue', alpha=0.5, label='Main Sequence')
    plt.hist(masses[ind==1], bins=25,histtype='step', density=True, color='red', alpha=0.5, label='White Dwarf')
    plt.hist(masses[ind==2], bins=25,histtype='step', density=True, color='green', alpha=0.5, label='Neutron Star')
    plt.hist(masses[ind==3], bins=10, histtype='step',density=True, color='purple', alpha=0.5, label='Black Hole')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Initial Mass [$M_\odot$]')
    plt.ylabel('Counts')
    plt.legend(loc='best', prop={'size': 6.5})
    plt.title("Mass distribution per remanent")
    return 0


def plot_mass_vs_age(masses,ages,ind):
    """
    Plots the mass versus age of stars, categorized by remnant type, with special markers 
    highlighting the oldest and youngest stars in each category.

    Parameters
    ----------
    masses : array-like
        Array containing the masses of stars.
    ages : array-like
        Array containing the ages of stars (in Myr).
    ind : array-like
        Array of indices indicating the remnant type for each star:
        - 0: Main Sequence
        - 1: White Dwarf
        - 2: Neutron Star
        - 3: Black Hole

    Returns
    -------
    Returns 0 upon completion.


    """

    
    color_map = {
    'Main Sequence': 'grey',
    'White Dwarf': 'blue',
    'Neutron Star': 'green',
    'Black Hole': 'purple'
    }

    
    colors = [color_map[category] for category in ['Main Sequence', 'White Dwarf', 'Neutron Star', 'Black Hole']]

    categories = ['Main Sequence', 'White Dwarf', 'Neutron Star', 'Black Hole']

    for i, category in enumerate(categories):
        plt.scatter(ages[ind == i], masses[ind == i], alpha=0.6, label=category, color=colors[i], s=10)

    
    for i in range(4):
        cat_ages = ages[ind == i]
        cat_masses = masses[ind == i]
        if len(cat_ages) > 0:  
            oldest_idx = np.argmax(cat_ages)
            youngest_idx = np.argmin(cat_ages)

            if i==1:
                plt.scatter(cat_ages[oldest_idx], cat_masses[oldest_idx], color=colors[i],edgecolor="black",marker="*", s=80, label=f'Oldest {categories[i]}')
                plt.scatter(cat_ages[youngest_idx], cat_masses[youngest_idx], color=colors[i],edgecolor="black",marker="D", s=30, label=f'Youngest {categories[i]}')

            else:
                plt.scatter(cat_ages[oldest_idx], cat_masses[oldest_idx], color=colors[i],edgecolor="black",marker="*", s=80)
                plt.scatter(cat_ages[youngest_idx], cat_masses[youngest_idx], color=colors[i],edgecolor="black",marker="D", s=30)

    
    plt.xscale('linear')  
    plt.xlabel('Age [Myr]')
    plt.ylabel('Mass [$M_\odot$]')
    plt.yscale("log")
    plt.legend(loc='upper center')
    plt.title('Age vs Mass for Stellar Categories')
    return 0


def pie_plot(ind):
    """
    Plots a pie chart showing the distribution of different stellar categories in the input array 'ind'.

    Parameters
    ----------
    ind : array-like
        Array of indices indicating the remnant type for each star:
        - 0: Main Sequence
        - 1: White Dwarf
        - 2: Neutron Star
        - 3: Black Hole

    Returns
    -------
    Returns 0 upon completion.

    """
    color_map = {
        'Main Sequence': 'grey',
        'White Dwarf': 'blue',
        'Neutron Star': 'green',
        'Black Hole': 'purple'
    }
    colors = [color_map[category] for category in ['Main Sequence', 'White Dwarf', 'Neutron Star', 'Black Hole']]
    categories = ['Main Sequence', 'White Dwarf', 'Neutron Star', 'Black Hole']
    counts = [(ind == 0).sum(), (ind == 1).sum(), (ind == 2).sum(), (ind == 3).sum()]
    fractions = np.array(counts) / sum(counts)
    
    
    wedges, texts, autotexts = plt.pie(fractions, labels=categories, autopct='%1.1f%%', colors=colors)
    
    
    for i, category in enumerate(categories):
        if category == 'Black Hole':
            autotexts[i].set_position((1.1, 0)) 
            texts[i].set_position((1.25,0))

        if category == 'Neutron Star':
            autotexts[i].set_position((1.1, -0.08))  
            texts[i].set_position((1.25, -0.08))

    plt.title('Fraction of Stellar Categories in the Simulation')
    return 0

def pie_plot_remanets(ind):
    """
    Plots a pie chart showing the distribution of stellar remnant categories (excluding Main Sequence) in the input array 'ind'.

    Parameters
    ----------
    ind : array-like
        Array of indices indicating the remnant type for each star:
        - 1: White Dwarf
        - 2: Neutron Star
        - 3: Black Hole
    
    Returns
    -------
    Returns 0 upon completion.


    """
    color_map = {
        'White Dwarf': 'blue',
        'Neutron Star': 'green',
        'Black Hole': 'purple'
    }
    colors = [color_map[category] for category in ['White Dwarf', 'Neutron Star', 'Black Hole']]
    categories = ['White Dwarf', 'Neutron Star', 'Black Hole']
    counts = [(ind == 1).sum(), (ind == 2).sum(), (ind == 3).sum()]
    fractions = np.array(counts) / sum(counts) 

    plt.pie(fractions, labels=categories, autopct='%1.1f%%', colors=colors)
    plt.title('Fraction of Stellar Categories (Excluding Main Sequence)')
    return 0
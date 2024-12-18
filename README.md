# Monte_Carlo_StarGen
Monte Carlo code for generating artificial stellar populations, based on the IMF of Kroupa 2001. This code facilitates the simulation of synthetic stellar populations, making it possible to analyse galaxies in a controlled environment, especially in the Milky Way.
![dia](https://github.com/user-attachments/assets/1a3a7a7f-b547-46ff-a9fa-4598c77a1204)

## Overview

### Initial Mass (generate_star_mass_data)
In this first stage, the code randomly generates the initial masses of the stars using the Monte Carlo method, in combination with the Initial Mass Function of Kroupa (2001). The user must specify the number of stars to simulate, and the code will select and store only those masses that meet the distribution defined by the IMF.

### Born time, age, and time on MS (generate_times)
Each star is assigned a randomly generated birth time, following a uniform distribution based on a constant star formation rate over time. A galaxy age of 13600 Myr is assumed to calculate the age and time out of the main sequence. The latter is calculated taking into account that the lifetime in the MS is given by $t_{MS} = 10^{10} / M^{2.5} ~[yr]$.

### End point (remnant_classifier) 
The code identifies those stars that are already stellar remnants at nowadays, evaluating the time they have been out of the MS (t_out) and classifies them assigning a numerical value depending on the intial mass of the object. If t_out is negative, it means that the stars are still in the MS, and they are assigned an index 0. If t_out is positive, the type of stellar remnant is classified depending on the initial mass of the star, assigning an index 1 for white dwarfs, 2 for neutron stars and 3 for black holes. The time out the MS will be $t_{out} = age - t_{MS}$.

### remnant mass (remnant_mass) 
The final mass of each remnant is calculated, following the relations established by   
    - Kalirai (2008) - https://arxiv.org/abs/0706.3894   
    - Raithel (2018) - https://iopscience.iop.org/article/10.3847/1538-4357/aab09b   

For the stars that still in the MS, the code assigns the initial mass as "final mass"

## Usage
### prerequisites
1- python 3.7 or a higher version installed   
2- python libraries: matplotlib, seaborn, numpy. If you download the full repository, just use the following command:   
```python
pip install -r requirements.txt
```
3- run the code   
```python
python main.py
```
The code will ask you to enter the number of stars to generate, a seed for those steps that make use of random and define the variable ‘plots’. The latter activates the generation of pre-made plots.   

Note: The code will probably take a little longer the first time you run it.

## Output
The output of the code consists in the catalog of the generated stars, including initial mass, age, object type and final mass, this latter could be interpreted as "mass at nowadays". The catalog will be generated in the same folder where the code is being executed. If the user has entered ‘y’ in the ‘plots’ request, then pre-set plots will also be generated in the ‘Plots’ folder.


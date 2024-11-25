import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from data_generator import generate_star_mass_data, generate_times
from utils import remnant_classifier, remnant_mass
from plots import plot_mass, plot_born_times_histogram, plot_mass_histogram, plot_mass_histogram_per_remnant,plot_mass_vs_age,pie_plot,pie_plot_remnant
def main(N_p,Xseed,plots):
    """
    Main function to generate a stellar catalog based on the Kroupa IMF and produce optional plots.

    Steps:
    1. Generate stellar masses with their associated probabilities using the Kroupa IMF.
    2. Simulate stellar formation times and calculate their lifetimes (ages).
    3. Classify stars based on their masses and lifetimes.
    4. Compute the final mass for each star that is a remnant at nowadays, considering stellar evolution.
    5. Optionally create and save 7 plots:
      - Ini. mass vs probability
      - Ini. mass histogram
      - born times histogram
      - Ini. mass histogram with remnant labels.
      - Ini. mass vs age
      - Pie plot
      - Pie plot for remnant
    6. Save the generated catalog as a CSV file.

    Parameters:
    ----------
    N_p : int
        Number of stars to simulate before applying the Kroupa IMF filter.
    Xseed: int
        Custom seed to the randoms numbers
    plots : bool
        Whether to generate and save additional plots (True/False).

    Returns:
    -------
    pd.DataFrame
        A DataFrame containing the generated stellar catalog with the following columns:
        - 'Mass_i': Initial stellar mass.
        - 'Age': Stellar age (Myr).
        - 'Object': Type of stellar remnant (e.g., white dwarf, neutron star, black hole).
        - 'Mass_f': Final stellar mass after evolution.
    """
    start_time = time.time()
    # Define the seed
    np.random.seed(Xseed)
    # Define minimum and maximum stellar mass limits
    mass_min, mass_max = 0.08, 100

    # Generate stellar masses and associated probabilities
    masses, prob_val = generate_star_mass_data(mass_min, mass_max, N_p)
    print(f"Out of {N_p} initial stars, {len(masses)} satisfy the Kroupa (2001) IMF distribution.")

    # Simulate stellar formation times and calculate lifetimes
    born_times, t_alive, t_out_ms = generate_times(masses)

    # Classify stars based on masses and remaining main-sequence lifetimes
    indicators = remnant_classifier(masses, t_out_ms)

    # Compute the final mass of each star after evolution
    final_mass = remnant_mass(masses, indicators)

    

    # Generate and save plots if requested
    if plots:
        plt.figure(figsize=(10, 6))
        plot_mass(masses, prob_val, mass_min, mass_max)
        plt.savefig("Plots/mass_distribution_scatter.pdf", format="pdf", dpi=300)
        plt.close()

        plt.figure(figsize=(10, 6))
        plot_mass_histogram(masses)
        plt.savefig("Plots/mass_distribution_histogram.pdf", format="pdf", dpi=300)
        plt.close()

        plt.figure(figsize=(10, 6))
        plot_mass_histogram_per_remnant(masses,indicators)
        plt.savefig("Plots/plot_mass_hist_per_remnant.pdf", format="pdf", dpi=300)
        plt.close()

        plt.figure(figsize=(10, 6))
        plot_mass_vs_age(final_mass,t_alive,indicators)
        plt.savefig("Plots/plot_mass_age.pdf", format="pdf", dpi=300)
        plt.close()

        plt.figure(figsize=(10, 6))
        plot_born_times_histogram(born_times)
        plt.savefig("Plots/Born_time_histogram.pdf", format="pdf", dpi=300)
        plt.close()

        plt.figure(figsize=(10, 6))
        pie_plot(indicators)
        plt.savefig("Plots/Pie_plot.pdf", format="pdf", dpi=300)
        plt.close()

        plt.figure(figsize=(10, 6))
        pie_plot_remnant(indicators)
        plt.savefig("Plots/Pie_plot_remnant.pdf", format="pdf", dpi=300)
        plt.close()

    # Create a DataFrame for the stellar catalog
    df = pd.DataFrame({
        "Mass_i": masses,
        "Age": t_alive,
        "Object": indicators,
        "Mass_f": final_mass
    })

    # Save the DataFrame to a CSV file
    df.to_csv("MC_Catalog.csv", index=False)

    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Execution time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")

    print("Execution completed successfully...")

    return df


if __name__ == "__main__":
    # Prompt the user for the number of stars to simulate
    N_p = int(input("Enter the number of stars to simulate: "))
    Xseed = int(input("Custom Seed: "))
    # Prompt the user to decide whether to generate additional plots
    plots = input("Generate additional plots? (y/n): ")
    plots = True if plots.lower() == "y" else False

    # Execute the main function
    main(N_p, Xseed, plots)

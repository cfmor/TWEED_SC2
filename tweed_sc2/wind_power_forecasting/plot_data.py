import matplotlib.pyplot as plt

def plot_location_power(df, save_path='power_comparison.png'):
    """
    Loads dataframe and plots Time vs Power for each.
    """

    locations = df['Location'].unique()
    fig, axes = plt.subplots(len(locations), 1, figsize=(12, 4 * len(locations)), sharex=True) 

    for i, loc in enumerate(locations):
        loc_data = df[df['Location'] == loc]
        ax = axes[i]
        ax.plot(loc_data['Time'], loc_data['Power'], color='tab:blue', lw=0.5)
        ax.set_title(f'{loc}', fontsize=14)
        ax.set_ylabel('Power Output')
        ax.grid(True, linestyle='--', alpha=0.6)

    axes[-1].set_xlabel('Timestamp')
    plt.tight_layout()

    plt.savefig(save_path, dpi=300)
    plt.show()
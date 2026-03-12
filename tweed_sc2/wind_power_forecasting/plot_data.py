import matplotlib.pyplot as plt

    
def plot_location_data(df, col, loc):
    """
    Loads dataframe and plots Time vs datastream for one location.
    """
    
    loc_data = df[df['Location'] == loc]
    plt.plot(loc_data.index, loc_data[col], color='tab:blue', lw=0.5)
    plt.title(f'{loc}', fontsize=14)
    if col == 'Power':
        plt.ylabel(col + ' (%)')
    elif col == 'windspeed_10m' or col == 'windspeed_100m' or col == 'windgusts_10m':
        plt.ylabel(col + ' (m/s)')
    elif col == 'winddirection_10m' or col == 'winddirection_100m':
        plt.ylabel(col + ' (deg)')
    elif col == 'wdcos_10' or col == 'wdsin_10' or col == 'wdcos_100' or col == 'wdsin_100':
        plt.ylabel(col + ' (-)')
    elif col == 'relativehumidity_2m':
        plt.ylabel(col + ' (%)')
    elif col == 'temperature_2m' or col == 'dewpoint_2m':
        plt.ylabel(col+' (K)')
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.xlabel('Timestamp')
    plt.tight_layout()

    save_path = col + '.png'
    plt.savefig(save_path, dpi=300)
    plt.show()
    
def plot_all_location_data(df, col):
    """
    Loads dataframe and plots Time vs datastream for each location.
    """
    
    locations = df['Location'].unique()
    fig, axes = plt.subplots(len(locations), 1, figsize=(12, 4 * len(locations)), sharex=True) 

    for i, loc in enumerate(locations):
        loc_data = df[df['Location'] == loc]
        ax = axes[i]
        # ax.plot(loc_data.index, loc_data[col], color='tab:blue', lw=0.5)
        ax.plot(loc_data.Time, loc_data[col], color='tab:blue', lw=0.5)

        ax.set_title(f'{loc}', fontsize=14)
        if col == 'Power':
            ax.set_ylabel(col + ' (%)')
        elif col == 'windspeed_10m' or col == 'windspeed_100m' or col == 'windgusts_10m':
            ax.set_ylabel(col + ' (m/s)')
        elif col == col == 'winddirection_10m' or col == 'winddirection_100m':
            ax.set_ylabel(col + ' (deg)')
        elif col == 'relativehumidity_2m':
            ax.set_ylabel(col + ' (%)')
        elif col == 'temperature_2m' or col == 'dewpoint_2m':
            ax.set_ylabel(col+' (K)')
        ax.grid(True, linestyle='--', alpha=0.6)

    axes[-1].set_xlabel('Timestamp')
    plt.tight_layout()

    save_path = col + '.png'
    plt.savefig(save_path, dpi=300)
    plt.show()
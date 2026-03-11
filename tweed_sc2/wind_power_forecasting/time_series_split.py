import pandas as pd

# File paths
file1 = r".\inputs\Location1_train.csv"
file2 = r".\inputs\Location2_train.csv"
file3 = r".\inputs\Location3_train.csv"
file4 = r".\inputs\Location4_train.csv"  # change if needed

# Reading the CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)

# Optional: display the first rows to verify
print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())



import pandas as pd
from typing import Tuple, Optional

def time_series_split(
    df: pd.DataFrame,
    time_col: str = "Time",
    train_ratio: float = 0.70,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
) -> Tuple[pd.DataFrame, Optional[pd.DataFrame], pd.DataFrame]:
    """
    BEST-PRACTICE time-based split for chronological data (e.g. weather + Power forecasting).
    
    Why this is the best way:
    - Time series data MUST respect temporal order → never random shuffle (no future leakage).
    - Train = past, Validation = recent past, Test = future (real-world forecasting simulation).
    - Automatically sorts by Time and converts to datetime.
    - Flexible ratios (they must sum to 1.0).
    - Optional validation set (set val_ratio=0 to skip it).
    - Returns full DataFrames (including all columns: Time, temperature_2m, ..., Power) so you can
      easily create X_train / y_train = train.drop(columns=['Power']), etc.
    
    Example usage:
        train, val, test = time_series_split(your_df)
        # or without validation:
        train, test = time_series_split(your_df, val_ratio=0.0)
        
        # Then for modeling:
        X_train = train.drop(columns=['Power'])
        y_train = train['Power']
        # same for val / test
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    if time_col not in df.columns:
        raise ValueError(f"Column '{time_col}' not found. Available columns: {list(df.columns)}")

    # Work on a copy so we don't modify the original
    data = df.copy()

    # Convert Time to datetime (handles strings, Unix timestamps, etc.)
    if not pd.api.types.is_datetime64_any_dtype(data[time_col]):
        data[time_col] = pd.to_datetime(data[time_col], errors="coerce")

    # Sort chronologically (critical!)
    data = data.sort_values(by=time_col).reset_index(drop=True)

    # Validate ratios
    if not abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6:
        raise ValueError(f"Ratios must sum to 1.0 (got {train_ratio + val_ratio + test_ratio})")

    n = len(data)
    if n < 10:
        raise ValueError("Dataset too small for meaningful split")

    # Calculate exact indices (integer splits)
    train_end = int(n * train_ratio)
    val_end = int(n * (train_ratio + val_ratio))

    # Prevent empty sets
    if train_end == 0:
        train_end = max(1, int(n * 0.1))
    if val_end <= train_end and val_ratio > 0:
        val_end = train_end + max(1, int(n * 0.1))

    train_df = data.iloc[:train_end].copy()
    val_df = data.iloc[train_end:val_end].copy() if val_ratio > 0 else None
    test_df = data.iloc[val_end:].copy()

    print(f" Time-series split completed:")
    print(f"   Train:     {len(train_df):,} rows ({train_ratio:.0%}) → {train_df[time_col].min()} to {train_df[time_col].max()}")
    if val_df is not None:
        print(f"   Validation: {len(val_df):,} rows ({val_ratio:.0%}) → {val_df[time_col].min()} to {val_df[time_col].max()}")
    print(f"   Test:      {len(test_df):,} rows ({test_ratio:.0%})  → {test_df[time_col].min()} to {test_df[time_col].max()}")

    if val_df is not None:
        return train_df, val_df, test_df
    else:
        return train_df, test_df

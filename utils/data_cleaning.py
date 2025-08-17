import pandas as pd

def clean_financial_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generic cleaning pipeline for raw user-provided financial data.
    """
    # Drop completely empty rows/cols
    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert date columns (use your actual column name)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Force numeric columns
    for col in ('amount', 'balance', 'debit', 'credit'):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Sort (optional)
    if 'date' in df.columns:
        df = df.sort_values('date')

    return df

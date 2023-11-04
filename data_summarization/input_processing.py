import pandas as pd


def pd_dataframe(csv_file):
    try:
        df = pd.read_csv(csv_file)
        return df
    except:
        raise TypeError("Invalid Format")


# Replaces the string in each coloumn with integer.
# Changed the function such that it takes a df as input and returns encoded df and a dictionary pertaining to the encoding
# TODO make sure the coloumn contains  repeating strings instead of some random data


def assign_values(coloumn_name):
    df = pd_dataframe
    coloumn = coloumn_name
    values = df[coloumn].unique()

    int_val = {value: index for index, value in enumerate(values)}

    df[coloumn] = df[coloumn].map(int_val)

    dict_actual_vals = {index: value for value, index in int_val.items()}

    return df, dict_actual_vals


def sort_long_boi(compared: list, df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort and return a DataFrame based on a specified numeric column or columns.

    Parameters:
    -----------
    compared : list
        A list of column names to be compared or returned.

    df : pd.DataFrame
        The input DataFrame that will be sorted and filtered.

    Returns:
    --------
    pd.DataFrame
        If a numeric column specified in 'compared' is found in the DataFrame, the DataFrame will be sorted
        by that column, and a subset of the DataFrame containing only the specified 'compared' columns will be returned.
        If no valid numeric columns are found, the original DataFrame will be returned with the specified 'compared' columns.
    """
    for column in compared:
        if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
            sorted_df = df.sort_values(by=column)
            return sorted_df[compared]
    return df[compared]


def longest_element_length_in_columns(df):
    column_lengths = []

    for column in df.columns:
        max_length = (
            df[column].apply(lambda x: len(str(x)) if not pd.isnull(x) else 0).max()
        )
        column_lengths.append(max_length)

    return column_lengths


def shorten_long_boi(df, len_of_longest_element_in_column: list) -> pd.DataFrame:
    x = 0
    for i in len_of_longest_element_in_column:
        x = x + i
    k = 3500 // x  # Use integer division

    total_rows = df.shape[0]
    z = total_rows // k

    selected_rows = df.iloc[::z].reset_index(drop=True)  # Reset index
    return selected_rows


def final_long_boi(df, columns: list) -> pd.DataFrame:
    x = sort_long_boi(columns, df)
    y = longest_element_length_in_columns(x)
    z = shorten_long_boi(x, y)
    return z

import google.generativeai as palm

palm.configure(api_key="AIzaSyBATda5w9AEGCb0PPvMQ02n1xo7-uAWtV0")


def auto_select_coloumn(coloumns: list) -> str:
    """
    Automatically select viable comparisons from the given list of columns.

    Parameters:
    -----------
    columns : list
        A list of column names to consider for generating viable comparisons.

    Returns:
    --------
    list
        A list of sets of column names that can be compared within the given context.

    Example:
    --------
    # Given a list of columns, automatically select and return sets of columns for comparison.
    columns = ['Education', 'Joining Year', 'City', 'Paymenteir', 'Age', 'Gender', 'EverBenched']
    result = auto_select_coloumn(columns)

    # The function may return a list like this:
    [['Education', 'Joining Year'], ['City', 'Paymenteir'], ['Age', 'Gender'], ['EverBenched', 'Education']]

    """

    coloum_str = ",".join(coloumns)
    prompt = f"""
    Given a CSV file with the following column names:
    {coloum_str}

    Please return a list of sets of columns that can be compared while considering the context, and nothing else."

    With this prompt, the response generated should be a list of sets of columns for comparison, and it should not include any other information or text.
   
    """
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0,
        max_output_tokens=100,
    )
    coloumns_list = eval(completion.result)

    return coloumns_list


def create_input_str(columns: list, df) -> str:
    """
    Create a descriptive input string for summarizing data and comparing specified columns.

    Parameters:
    -----------
    columns : list
        A list of column names from the DataFrame to be compared or summarized.

    df : DataFrame
        The input DataFrame containing the data to be summarized and compared.

    Returns:
    --------
    str
        A descriptive input string that can be used as a prompt for summarizing the data and comparing the specified columns.

    """
    string = f"Summarize this data, and compare the columns.\n{df[columns]}"

    return string


def llm(input_str: str) -> str:
    """
    Generate a data summary based on the input string using a language model.

    Parameters:
    -----------
    input_str : str
        An input string that serves as a prompt for generating a data summary.

    Returns:
    --------
    str
        A data summary generated by the language model.
    """
    prompt = input_str
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0,
        max_output_tokens=2000,
    )
    data_summary = completion.result
    return data_summary

import google.generativeai as palm

from data_summarization.processing import auto_select_coloumn, create_input_str, llm

from data_summarization.input_processing import *

from graph_plot import plot_graph

palm.configure(api_key="AIzaSyBATda5w9AEGCb0PPvMQ02n1xo7-uAWtV0")


def get_summarised_txt(file, columns: list = [], autodetect: bool = True) -> list:
    """
    Function to return summarized text

    Params
    ------
    df: Pandas DataFrame
        Contains data from input csv file

    columns: list
        (Default is an empty list: case where user asks the LLM to choose columns)
        List whose elements are lists. Each of the elements contain columns that will be comapred to each other in the data analysis.

    autodetect: bool
        (Default is True: case where user expects LLM to autodetect which columns should be compared)
        If True: LLM autodetects
        If False: User inputs the columns that require a comparision"""

    df = pd_dataframe(file)
    if autodetect:
        columns = auto_select_coloumn(df.columns.to_list())

    for i in columns:
        plot_graph(df, i[0], i[1])

    outputs = list()
    for i in columns:
        ip = create_input_str(i, df)
        op = llm(ip)
        print(op)
        outputs.append(op)

    return outputs

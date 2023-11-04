from data_summarization.input_processing import *
from data_summarization.summarised_txt import *
from data_summarization.processing import *

file = open("sample_data.csv")
op = get_summarised_txt(
    file, [["Education", "JoiningYear"], ["PaymentTier", "Age"]], False
)
print(op)

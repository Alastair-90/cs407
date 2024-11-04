from matplotlib import pyplot as plt
from pandas.core.interchange.dataframe_protocol import DataFrame
import pandas as pd
from verispy import VERIS
data_dir="" #replace with your own address for data
v = VERIS(json_dir=data_dir)
print (v.schema_url)
veris_df = v.json_to_df(verbose=True)
date_ = veris_df['timeline.month'].value_counts()
date_ = date_[date_ == 6]
print(date_)



print( v.enum_summary(veris_df,'variety'))

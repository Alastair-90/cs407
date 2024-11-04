from matplotlib import pyplot as plt
from pandas.core.interchange.dataframe_protocol import DataFrame
import pandas as pd
from verispy import VERIS
data_dir="" #replace with your own address for data
v = VERIS(json_dir=data_dir)
print (v.schema_url)
veris_df = v.json_to_df(verbose=True)

industryCounts=veris_df['victim.industry'].value_counts()

industryCounts = industryCounts[industryCounts > 20]

plt.figure(figsize=(15, 6))
industryCounts.plot(kind='bar')



plt.title('Number of Incidents by Industry')
plt.xlabel('Industry')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=90)
plt.show()




print( v.enum_summary(veris_df,'variety'))

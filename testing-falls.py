import os
import pandas as pd
import numpy as np

## update to proper path (this part is manual right now... need to automate)
root_data_directory = 'trouble_shooting/summer2024'

#path_participation = f'{root_data_directory}/participation'
#path_registration = f'{root_data_directory}/registration'
 
propper_formated_df = pd.read_csv('trouble_shooting/summer2024/Participation_summer.csv', header = 0,sep=',')
propper_formated_df.head()

propper_formated_df.to_excel(f'{root_data_directory}/Master_Participation_Data_Set.xlsx', index=False)
import os
import pandas as pd
import numpy as np

## update to proper path (this part is manual right now... need to automate)
root_data_directory_part = 'trouble_shooting/summer2024'
root_data_directory_reg = 'trouble_shooting/summer2024_registration'
#path_participation = f'{root_data_directory}/participation'
#path_registration = f'{root_data_directory}/registration'
errors = []

files = os.listdir(root_data_directory_part)
all_files = []   
for file in files:
    if file.endswith('.csv'):
        all_files.append(root_data_directory_part + "/" + file)


all_dfs = []
for one_filename in  all_files:
    try:
        print('Processing:', one_filename)
        temp_df = pd.read_csv(one_filename,header = 0,sep=',')  
        all_dfs.append(temp_df)                                           
    except Exception as e:
        print(f"Error processing {one_filename}: {e}")
        error = {
            "code_sequence": 'error loading participation data',
            "filename": one_filename,
            "code_error": e,
        }
        errors.append(error)
        continue                                     
master_partipation_df = pd.concat(all_dfs)
master_partipation_df.columns
master_partipation_df.to_excel(f'{root_data_directory_part}/Master_Participation_Data_Set.xlsx', index=False)
 
#propper_formated_df = pd.read_csv('trouble_shooting/summer2024/Participation_summer.csv', header = 0,sep=',')
#propper_formated_df.head()

#propper_formated_df.to_excel(f'{root_data_directory}/Master_Participation_Data_Set.xlsx', index=False)

files = os.listdir(root_data_directory_reg)
all_files = []   
for file in files:
    if file.endswith('.csv'):
        all_files.append(root_data_directory_reg + '/' + file)  

df_total = pd.DataFrame()

for file in all_files:
    df_temp = pd.read_csv(file)
    df_temp["Meeting ID"] =  file.split("/")[-1].split("_")[0]     ## get the meeting id by keeping the characters after the last / and before the _ in the file name
    df_temp.rename(columns={'Email':'User Email'}, inplace=True)
    print("Unique Rows: ", df_temp["User Email"].nunique())
    print("Total Rows: ", df_temp["User Email"].count())
    df_total = df_total._append(df_temp)                                         

df_total.to_excel(f'{root_data_directory_reg}/Master_Registration_data.xlsx', index=False)

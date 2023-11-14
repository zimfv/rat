import numpy as np
import pandas as pd


# test pandas
print('Getting test tables:\n')
df_employment = pd.read_csv('tables/employment.csv').head(2)
print('\nEmploytment table:')
print(df_employment.head())

df_environment = pd.read_csv('tables/environment.csv').head(2)
print('\nEnviroment table:')
print(df_environment.head())

# test rat.ratrestore.restore_table()
print('\ntest rat.ratrestore.restore_table()\n')
from rat.ratrestore import restore_table
df_restored = restore_table(df_employment, df_environment, name_a='Employment', name_b='Environment', name_res='Count', print_status=True)
print('\nRestored table:')
print(df_restored)

print('\nrat.ratrestore.restore_table() completed.\nFloat restoring is possible.\n')
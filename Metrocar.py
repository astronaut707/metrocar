import pandas as pd

# Importing dataFrames
step1 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step1.csv', index_col=False)
step2 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step2.csv', index_col=False)
step3 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step3.csv', index_col=False)
step4 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step4.csv', index_col=False)
step5 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step5.csv', index_col=False)
step6 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step6.csv', index_col=False)
step7 = pd.read_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/step7.csv', index_col=False)

steps = [step1, step2, step3, step4, step5, step6, step7]
funnel = pd.concat(steps)
funnel = funnel.reset_index(drop=True)

print(funnel)
funnel.to_csv('C:/Users/infin/Documents/[00] Data Analysis Projects/project_6/data/funnel.csv')

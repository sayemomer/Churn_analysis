import pandas as pd

telco = pd.read_csv('Churn.csv')

# ? how many Churn and non churn 
print(telco['Churn'].value_counts())

# ? how many Churner and non churner in states

print(telco.groupby('State')['Churn'].value_counts())

#Store the Churn by state in csv formet

# newfile = open('ChurnBYstate.csv','a')

# ChurnByState = telco.groupby('State')['Churn'].value_counts();

# for State in ChurnByState:
#     print(State)

# newfile.write(x);

# ? who calls customer service the most Churners or non_churners




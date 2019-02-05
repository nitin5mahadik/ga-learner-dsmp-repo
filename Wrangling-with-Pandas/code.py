# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 


# code starts here
bank=pd.read_csv("/opt/greyatom/kernel-gateway/data/executor/attachments/account/b1/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b69/a340d73b-3d57-4e25-9cfd-074cea5af958/file.csv")

categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var)





# code ends here


# --------------
# code starts here
import pandas as pd 
import pandas as pd
from scipy.stats import mode 


#code ends here
banks=bank.drop(['Loan_ID'], inplace=False , axis=1)
 
banks.isnull().sum
 
bank_mode = banks.mode().iloc[0]
print(bank_mode)
banks=banks.fillna(bank_mode, inplace=False)


# --------------
# Code starts here
import pandas as pd 
import numpy as np 
from scipy.stats import mode 

# code ends here
avg_loan_amount=pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc=np.mean)

print(avg_loan_amount)


# --------------
# code starts here
import pandas as pd 
import numpy as np 
from scipy.stats import mode 

# code ends here
loan_approved_se= len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
print(loan_approved_se)

loan_approved_nse=len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
print(loan_approved_nse)

percentage_se=(loan_approved_se*100/614)
percentage_nse=(loan_approved_nse*100/614)

print(percentage_se)
print(percentage_nse)


# --------------
# code starts here

import pandas as pd 
import numpy as np 
from scipy.stats import mode 
# code ends here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )
 
big_loan_term=len(loan_term[loan_term>=25])
 
print(big_loan_term)


# --------------
# code starts here
import pandas as pd 
import numpy as np 

loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
 
#loan_groupby=loan_groupby1.groupby(['ApplicantIncome','Credit_History'])
print(loan_groupby)
mean_values=loan_groupby.mean()


# code ends here



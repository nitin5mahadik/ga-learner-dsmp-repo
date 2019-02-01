# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here
data=pd.read_csv(path)
#print(data)
loan_status=data['Loan_Status'].value_counts()
#loan_status=data['Loan_status'].value_counts()

loan_status.plot(kind='Bar')
plt.show()


# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
#print(property_and_loan)
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')

plt.xticks(rotation=45)



# --------------
#Code starts here


education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
print(education_and_loan)


# --------------
#Code starts here


graduate=data[data['Education']=='Graduate']

not_graduate=data[data['Education']=='Not Graduate']

graduate.plot(kind='density' , label='Graduate')

not_graduate.plot(kind='density',label='Not Graduate')





#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows=3, ncols=1 ,figsize=(20,10))

data.plot.scatter(x='ApplicantIncome', y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome'] + data['CoapplicantIncome']

data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')




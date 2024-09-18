import pandas as pd

df = pd.read_csv('employee_data.csv')

print("Original Data:")
print(df.head())

df = df.drop(columns=['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber'])

df = df.rename(columns={
    'Age': 'Employee_Age',
    'Attrition': 'Employee_Attrition',
    'BusinessTravel': 'Travel_Frequency',
    'DailyRate': 'Daily_Rate',
    'Department': 'Dept',
    'DistanceFromHome': 'Distance_From_Home',
    'Education': 'Education_Level',
    'EducationField': 'Education_Field',
    'EnvironmentSatisfaction': 'Env_Satisfaction',
    'Gender': 'Gender',
    'HourlyRate': 'Hourly_Rate',
    'JobInvolvement': 'Job_Involvement',
    'JobLevel': 'Job_Level',
    'JobRole': 'Job_Role',
    'JobSatisfaction': 'Job_Satisfaction',
    'MaritalStatus': 'Marital_Status',
    'MonthlyIncome': 'Monthly_Income',
    'MonthlyRate': 'Monthly_Rate',
    'NumCompaniesWorked': 'Num_Companies_Worked',
    'OverTime': 'Overtime_Status',
    'PercentSalaryHike': 'Salary_Hike_Percent',
    'PerformanceRating': 'Performance_Rating',
    'RelationshipSatisfaction': 'Relationship_Satisfaction',
    'StockOptionLevel': 'Stock_Option_Level',
    'TotalWorkingYears': 'Total_Working_Years',
    'TrainingTimesLastYear': 'Training_Times_Last_Year',
    'WorkLifeBalance': 'Work_Life_Balance',
    'YearsAtCompany': 'Years_At_Company',
    'YearsInCurrentRole': 'Years_In_Current_Role',
    'YearsSinceLastPromotion': 'Years_Since_Last_Promotion',
    'YearsWithCurrManager': 'Years_With_Current_Manager'
})

df = df.drop_duplicates()

df['Gender'] = df['Gender'].str.capitalize()
df['Marital_Status'] = df['Marital_Status'].str.capitalize()

df = df.dropna()

df = df[(df['Years_At_Company'] <= df['Total_Working_Years']) & (df['Years_At_Company'] >= 0)]

print("\nCleaned Data:")
print(df.head())

df.to_csv('cleaned_employee_data.csv', index=False)


# Create new dataframe - which will be used for classification model



# In[186]:





model_data = pd.DataFrame()

model_students = ML_model_students.id.unique()

'''Add unique students'''

model_data['id'] = model_students



'''Add all other required fields'''

mother_education = []

father_education = []

curr_cum_GPA = []

ELM_score = []

EPT_score = []

Num_UDIs = []

Num_CIs = []

SCH_region = []

city = []

cohort_year = []

gender = []

Third_term_persistence = []

Fifth_term_persistence = []

Seventh_term_persistence = []

Last_Institution_Persistence_Status = []





for student in model_students:

    df = ML_model_students[ML_model_students.id == student]

    mother_education.append(df['mother_education'].iloc[0])

    father_education.append(df['father_education'].iloc[0])

    curr_cum_GPA.append(df['curr_cum_GPA'].iloc[0])

    ELM_score.append(df['ELM_score'].iloc[0])

    EPT_score.append(df['EPT_score'].iloc[0])

    Num_UDIs.append(df['Num_UDIs'].iloc[0])

    Num_CIs.append(df['Num_CIs'].iloc[0])

    SCH_region.append(df['SCH_region'].iloc[0])

    city.append(df['city'].iloc[0])

    cohort_year.append(df['cohort_year'].iloc[0])

    gender.append(df['gender'].iloc[0])

    Third_term_persistence.append(df['Third_term_persistence'].iloc[0])

    Fifth_term_persistence.append(df['Fifth_term_persistence'].iloc[0])

    Seventh_term_persistence.append(df['Seventh_term_persistence'].iloc[0])

    Last_Institution_Persistence_Status.append(df['Last_Institution_Persistence_Status'].iloc[0])



    

model_data['mother_education'] = mother_education

model_data['father_education'] = father_education

model_data['curr_cum_GPA'] = curr_cum_GPA

model_data['ELM_score'] = ELM_score

model_data['EPT_score'] = EPT_score

model_data['Num_UDIs'] = Num_UDIs

model_data['Num_CIs'] = Num_CIs

model_data['SCH_region'] = SCH_region

model_data['city'] = city

model_data['cohort_year'] = cohort_year

model_data['gender'] = gender

model_data['Third_term_persistence'] = Third_term_persistence

model_data['Fifth_term_persistence'] = Fifth_term_persistence

model_data['Seventh_term_persistence'] = Seventh_term_persistence

model_data['Last_Institution_Persistence_Status'] = Last_Institution_Persistence_Status









# In[187]:





model_data.head(3)





# Data preprocessing: Replace missing values



# In[188]:





model_data.SCH_region.fillna('Bay Area', inplace=True)

model_data.curr_cum_GPA.fillna(0, inplace=True)





# In[189]:





model_data.isna().any()





# In[190]:





'''Students to consider to calculate 3rd term persistence: '''

for_3rdTerm_pers = ['2014', '2015', '2016', '2017', '2018']

'''Students to consider to calculate 5th term persistence: '''

for_5thTerm_pers = ['2014', '2015', '2016', '2017']

'''Students to consider to calculate 7th term persistence: '''

for_7thTerm_pers = ['2014', '2015', '2016']

'''Students to consider to calculate 4 Year Graduation: '''

for_4Year_graduation = ['2014', '2015']


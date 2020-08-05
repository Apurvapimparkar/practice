#!/usr/bin/env python

# coding: utf-8



# In[179]:





import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from scipy.stats import chi2_contingency

from scipy.stats import chi2





# In[180]:





# Read the CI CSV file

original_CI_dataset = pd.read_csv(filepath_or_buffer = "CI_students_with_terms_28thMarch.csv",  encoding="utf-8")



# make a copy of it

data = original_CI_dataset



# Chnage the names of the columns:

data.columns = ['id', 'first_name', 'last_name', 'date', 'state', 

                'gender', 'batch', 'race', 'mother_education',

                'father_education','CI_num', 'gpa', 'metro_cohort', 

              'Country', 'direction', 'method','metro_start_term', 

                'coordinator', 'support_staff', 'topic', 

                'notes', 'persistence_status', 'cohort_name', 'newTermNameAdded',

                   'TermNum', 'Cumulative_gpa', 'Termwise_Metro_persistence', 'Term_gpa',

                  'third_term_persistence','fifth_term_persistence', 'seventh_term_persistence', 

                   'institution_persistence_status', 'institution_persistence','change_in_TermGPA','Week_Number']

CI_all_students = data





# In[181]:





original_Metro_Dataset = pd.read_csv(filepath_or_buffer = "All_Metro_students_final_31stMar.csv", low_memory=False)

metro_all = original_Metro_Dataset

# Chnage the names of the columns:

metro_all.columns = ['id', 'TermNum', 'change_in_TermGPA','mother_education','father_education', 

                     'Last_Institution_Persistence_Status', 'Termwise_Institution_Persistence',

                 'Fifth_term_persistence', 'Third_term_persistence','Last_Metro_Persistence_Status',

                 'Seventh_term_persistence',

                 'race','metro_start_term', 'metro_cohort', 

                'cohort', 'metro_persistence', 'first_name',

                'last_name','gender', 'term', 'term_gpa', 

              'cumulative_gpa', 'street', 'city','state', 'zip', 

                'country', 'email', 'accName', 'enrollment_num']

metro_all_students = metro_all





# In[182]:





original_Comparison_Dataset = pd.read_csv(filepath_or_buffer = "Comparison_students_7thApril.csv", low_memory=False)

comparison_all = original_Comparison_Dataset

# Chnage the names of the columns:

comparison_all.columns = ['id', 'TermNum', 'change_in_TermGPA','mother_education','father_education', 

                     'Last_Institution_Persistence_Status', 'Termwise_Institution_Persistence',

                 'Fifth_term_persistence', 'Third_term_persistence','Last_Metro_Persistence_Status',

                 'Seventh_term_persistence',

                 'race','metro_start_term', 'metro_cohort', 

                'cohort', 'metro_persistence', 'first_name',

                'last_name','gender', 'term', 'term_gpa', 

              'cumulative_gpa', 'street', 'city','state', 'zip', 

                'country', 'email', 'accName', 'enrollment_num']

comparison_all_students = comparison_all





# In[183]:





original_classication_model_Dataset = pd.read_csv(filepath_or_buffer = "For_Classification_Model.csv", low_memory=False)

classification_all = original_classication_model_Dataset

# Chnage the names of the columns:

classification_all.columns = ['id', 'TermNum','ELM_score','EPT_score','curr_cum_GPA',

                     'Num_UDIs', 'Num_CIs', 'change_in_TermGPA','SCH_region', 'SCH_zip',

                     'mother_education','father_education', 

                     'Last_Institution_Persistence_Status', 'Termwise_Institution_Persistence',

                 'Fifth_term_persistence', 'Third_term_persistence','Last_Metro_Persistence_Status',

                 'Seventh_term_persistence',

                 'race','metro_start_term', 'metro_cohort', 

                'cohort', 'metro_persistence', 'first_name',

                'last_name','gender', 'term', 'term_gpa', 

              'cumulative_gpa', 'street', 'city','state', 'zip', 

                'country', 'email', 'accName', 'enrollment_num']

ML_model_students = classification_all





# In[184]:





ML_model_students['mother_education'].replace('No High School', 'HighSchool/lower',inplace=True)

ML_model_students['mother_education'].replace('Some High School', 'HighSchool/lower',inplace=True)

ML_model_students['mother_education'].replace('Some College', 'Some_college',inplace=True)

ML_model_students['mother_education'].replace('High School Grad', 'HighSchool/lower',inplace=True)

ML_model_students['mother_education'].replace('2-Yr College Grad', 'Some_college',inplace=True)

ML_model_students['mother_education'].replace('4-Yr College Grad', 'College/post_grad',inplace=True)

ML_model_students['mother_education'].replace('Postgraduate', 'College/post_grad',inplace=True)



ML_model_students['father_education'].replace('No High School', 'HighSchool/lower',inplace=True)

ML_model_students['father_education'].replace('Some High School', 'HighSchool/lower',inplace=True)

ML_model_students['father_education'].replace('Some College', 'Some_college',inplace=True)

ML_model_students['father_education'].replace('High School Grad', 'HighSchool/lower',inplace=True)

ML_model_students['father_education'].replace('2-Yr College Grad', 'Some_college',inplace=True)

ML_model_students['father_education'].replace('4-Yr College Grad', 'College/post_grad',inplace=True)

ML_model_students['father_education'].replace('Postgraduate', 'College/post_grad',inplace=True)





# Add cohort year to the metro students dataframe



# In[185]:





list_of_cohorts = ML_model_students['cohort'].tolist()

new_list_ofcohortYear = []

for cohort in list_of_cohorts:

    new_list_ofcohortYear.append(cohort[-4:])

ML_model_students['cohort_year'] = new_list_ofcohortYear

"""Changing file-1"""

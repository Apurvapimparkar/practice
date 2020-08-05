# In[192]:





all_students = model_data.id.unique()

term1_freq = []

term2_freq = []

term3_freq = []

term4_freq = []

firstYear_freq = []

secondYear_freq = []

bothYear_freq = []



for student in all_students:

    df = CI_all_students[CI_all_students.id == student]

    df1 = df[df.TermNum == 1]

    term1_freq.append(len(df1))

    df2 = df[df.TermNum == 2]

    term2_freq.append(len(df2))

    df3 = df[df.TermNum == 3]

    term3_freq.append(len(df3))

    df4 = df[df.TermNum == 4]

    term4_freq.append(len(df4))

    firstYear_freq.append(len(df1)+len(df2))

    secondYear_freq.append(len(df3)+len(df4))

    bothYear_freq.append(len(df1)+len(df2)+len(df3)+len(df4))

    

model_data['term1_CI_freq'] = term1_freq  

model_data['term2_CI_freq'] = term2_freq   

model_data['term3_CI_freq'] = term3_freq   

model_data['term4_CI_freq'] = term4_freq

model_data['firstYear_CI_freq'] = firstYear_freq

model_data['secondYear_CI_freq'] = secondYear_freq

model_data['bothYear_CI_freq'] = bothYear_freq

    

    





# In[193]:





all_students = model_data.id.unique()

term1_only_freq = []

term2_only_freq  = []

both_term1and2_freq = []

firstYear_only_freq = []

secondYear_only_freq = []

bothYear_freq = []



for student in all_students:

    df = CI_all_students[CI_all_students.id == student]

    df1 = df[df.TermNum == 1]

    df2 = df[df.TermNum == 2]

    df3 = df[df.TermNum == 3]

    df4 = df[df.TermNum == 4]

    

    '''Term-1 only'''

    if len(df2) == 0:

        term1_only_freq.append(len(df1))

    else:

        term1_only_freq.append(0)

    

    '''Term-2 only'''

    if len(df1) == 0:

        term2_only_freq.append(len(df2))

    else:

        term2_only_freq.append(0) 



    '''Both term 1 and 2 both'''

    if (len(df1) != 0) & (len(df2) != 0):

        both_term1and2_freq.append(len(df1) + len(df2))

    else:

        both_term1and2_freq.append(0) 



    '''First Year only'''

    if ((len(df1)+len(df2) != 0) & (len(df3)+len(df4) == 0)):

        firstYear_only_freq.append(len(df1) + len(df2))

    else:

        firstYear_only_freq.append(0) 

        

    '''Second Year only'''

    if ((len(df1)+len(df2) == 0) & (len(df3)+len(df4) != 0)):

        secondYear_only_freq.append(len(df3) + len(df4))

    else:

        secondYear_only_freq.append(0)       

        

    '''Both years'''

    if ((len(df1)+len(df2) != 0) & (len(df3)+len(df4) != 0)):

        bothYear_freq.append(len(df1)+len(df2)+len(df3)+len(df4))

    else:

        bothYear_freq.append(0)

        

    

model_data['term1_only_freq'] = term1_only_freq  

model_data['term2_only_freq'] = term2_only_freq   

model_data['both_term1and2_freq'] = both_term1and2_freq   

model_data['firstYear_only_freq'] = firstYear_only_freq

model_data['secondYear_only_freq'] = secondYear_only_freq

model_data['bothYear_freq'] = bothYear_freq

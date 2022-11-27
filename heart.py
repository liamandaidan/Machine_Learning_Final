def cleanData():
    """The purpose of this module is clean the data for the spread sheet heart.csv
    """
    import pandas as pd

    df = pd.read_csv("./heart.csv")

    age = df.age.values.tolist()
    sex = [] #[Male/female] [1/0]
    cp_type = [] #chest pain type [Typical anigina, atypical anigina, non-anginal, asymptomatic] [0-3]
    rbp = df.resting_blood_pressure.values.tolist()
    cho = df.cholestoral.values.tolist()
    fbs_type = [] #fasting blood sugar type [greater/lower] [true/false] [1/0]
    rest_ecg = [] #rest ecg [nornaml/ST-T wave/ left vent..] [1/2/3]
    mh = df.Max_heart_rate.values.tolist()
    eia_type = [] #excersiced induced agnia [true/false] [1/0]
    oldPeak = df.oldpeak.values.tolist()
    slope = [] #slope [upsloping/flat/downslope] [1/2/3]
    vcf_type = [] #vessels colored by flourposopy [zero, one, two, three] [1,2,3,4]
    thalassemia = [] #thalassemia [no test/fixed/normal flow/reversible defect] [0,1,2,3]
    target = df.target.values.tolist()
    for item in df['sex']:
        if item == 'Male':
            sex.append(1)
        else:
            sex.append(0)

    for item in df['chest_pain_type']:
        if item == 'Typical angina':
            cp_type.append(0)
        elif item == 'Atypical angina':
            cp_type.append(1)
        elif item == 'Non-anginal pain':
            cp_type.append(2)
        else: #asymptomatic
            cp_type.append(3)

    for item in df['fasting_blood_sugar']:
        if item == 'Lower than 120 mg/ml':
            fbs_type.append(0)
        else:
            fbs_type.append(1)

    for item in df['rest_ecg']:
        if item == 'Normal':
            rest_ecg.append(1)
        elif item == 'ST-T wave abnormality':
            rest_ecg.append(2)
        else: #Left ventricular hypertrophy
            rest_ecg.append(3)

    for item in df['exercise_induced_angina']:
        if item == 'Yes':
            eia_type.append(1)
        else: #no
            eia_type.append(0)

    for item in df['slope']:
        if item == 'Upsloping':
            slope.append(1)
        elif item == 'Flat':
            slope.append(2)
        else: #downsloping
            slope.append(3)

    for item in df['vessels_colored_by_flourosopy']:
        if item == 'Zero':
            vcf_type.append(1)
        elif item == 'One':
            vcf_type.append(2)
        elif item == 'Two':
            vcf_type.append(3)
        else:
            vcf_type.append(4)

    for item in df['thalassemia']:
        if item == 'No':
            thalassemia.append(0)
        elif item == 'Fixed Defect':
            thalassemia.append(1)
        elif item == 'Normal':
            thalassemia.append(2)
        else: 
            thalassemia.append(3)

    # final_arr = [age, sex, cp_type, rbp, cho, fbs_type, rest_ecg, mh, eia_type, oldPeak, slope, vcf_type, thalassemia, target]
    # final_arr_columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholestoral', 'fasting_blood_sugar', 'rest_ecg', 'Max_heart_rate', 'exercise_induced_angina',
    #                     'oldpeak', 'slope', 'vessels_colored_by_flourosopy', 'thalassemia', 'target']
    d = {'age': age, 'sex': sex, 'chest_pain_type': cp_type, 'resting_blood_pressure': rbp, 'cholestoral': cho, 'fasting_blood_sugar': fbs_type, 'rest_ecg': rest_ecg, 
        'Max_heart_rate': mh, 'exercise_induced_angina': eia_type, 'oldpeak': oldPeak, 'slope': slope, 'vessels_colored_by_flourosopy': vcf_type, 'thalassemia': thalassemia, 'target': target}
    df2 = pd.DataFrame(data=d)

    df2.to_csv('./cleanedDataHeart.csv', index = False)

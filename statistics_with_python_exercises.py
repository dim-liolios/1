import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns


# >>>> TEST 1 <<<<

df = pd.read_csv('Cartwheeldata.csv')
print(df.query('Age > 30'))
x = df.Age > 30
print(x.mean())
print(np.mean(df['Age'] > 30))


#-----------------------------------------------------------------------------------------------------------------------

# >>>> TEST 2 <<<<

data = {'Country': ('Belgium',  'India',  'Brazil'),
        'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Country', 'Capital',  'Population'], index = [1,22,3])


#-----------------------------------------------------------------------------------------------------------------------

# >>>> TEST 3 <<<<

tips_data = sns.load_dataset('tips')
sns.boxplot(tips_data["total_bill"]).set_title('Total bill')
sns.histplot(tips_data["tip"]).set_title('Tip')
sns.boxplot(x = tips_data["tip"], y = tips_data["day"], hue = tips_data.sex)
g = sns.FacetGrid(tips_data, row = "sex")
g = g.map(plt.hist, "tip")
plt.show()

#=======================================================================================================================

# >>>> TEST 5 <<<<

da = pd.read_csv("nhanes_2015_2016.csv")
pd.set_option('display.max_columns', 30)

da["Smoking"] = da.SMQ020.replace({1: "Yes", 2: "No", 7: np.nan, 9: np.nan})
da["Age"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
da['Marital_Status'] = da.DMDMARTL.replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "Never married",
                                            6: 'Living with partner', 77: "Refused", 99: "Don't know"})
da['Marital_Status'] = da.Marital_Status.fillna("Missing values")
da["Education"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College",
                                       7: "Refused", 9: "Don't know"})
da["Gender"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
db = da.loc[(da.Education != "Don't know") & (da.Marital_Status != "Refused"), :]


print(pd.crosstab(db.Education, db.Marital_Status).apply(lambda x: x/x.sum(),axis=1))
print(db.groupby(["Gender", "Education", "Marital_Status"]).size().unstack().fillna(0).apply(lambda x: x/x.sum(), axis=1))
print(db.groupby(["Age", "Marital_Status"]).size().unstack().fillna(0).apply(lambda x: x/x.sum(), axis=1))

# ----------------------------------------------------------------------------------------------------------------------
# Construct a 95% confidence interval for the proportion of smokers who are female. Construct a 95% confidence interval
# for the proportion of smokers who are male. Construct a 95% confidence interval for the difference between those two
# gender proportions.

# 1os tropos:
print(pd.crosstab(da.Smoking, da.Gender).unstack())
print('Women: ', sm.stats.proportion_confint(906, 2972))
print('Men: ', sm.stats.proportion_confint(1413, 2753))

# 2os tropos:
print(pd.crosstab(da.Smoking, da.Gender).apply(lambda x: x/x.sum(), axis = 0 ))
print('WOMEN')
p_women = 0.3048
error_women = np.sqrt(p_women*(1-p_women)/2972)
uci = p_women + 1.96*error_women
lci = p_women - 1.96*error_women
print(lci, uci)
print('MEN')
p_men = 0.5132
error_men = np.sqrt(p_men*(1-p_men)/2753)
uci = p_men + 1.96*error_men
lci = p_men - 1.96*error_men
print(lci, uci)
print('DIFFERENCE')
p_diff = p_women - p_men
error_diff = np.sqrt(error_women**2 + error_men**2)
uci = p_diff + 1.96*error_diff
lci = p_diff - 1.96*error_diff
print(lci, uci)

#=======================================================================================================================

# >>>> TEST 6 <<<<

mean_univ = 155
sd_univ = 5
mean_gym = 185
sd_gym = 5
gymperc = 0.3
total_pop_size = 40000

univ_stud = np.random.normal(mean_univ, sd_univ, int(total_pop_size*(1-gymperc)))
gym_stud = np.random.normal(mean_gym, sd_gym, int(total_pop_size*gymperc))

population = np.append(univ_stud, gym_stud)

number_samp = 5000
sample_size = 50

mean_distr = np.empty(number_samp)
for x in range(number_samp):
    random_students = np.random.choice(total_pop_size, sample_size)
    mean_distr[x] = np.mean(random_students)

print(mean_distr)
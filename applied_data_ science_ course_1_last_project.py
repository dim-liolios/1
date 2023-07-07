import numpy as np
import math
import re
from PIL import Image

# =========
# COURSE 1|
# =========

# Week 1 - Practice
# -----------------

text = 'Overview[edit]\nFERPA gives parents access to their child\'s education records, an opportunity to seek to have the records amended, and some control over the disclosure of information from the records. With several exceptions, schools must have a student\'s consent prior to the disclosure of education records after that student is 18 years old. The law applies only to educational agencies and institutions that receive funds under a program administered by the U.S. Department of Education.\n\nOther regulations under this act, effective starting January 3, 2012, allow for greater disclosures of personal and directory student identifying information and regulate student IDs and e-mail addresses.[2] For example, schools may provide external companies with a student\'s personally identifiable information without the student\'s consent.[2]\n\nExamples of situations affected by FERPA include school employees divulging information to anyone other than the student about the student\'s grades or behavior, and school work posted on a bulletin board with a grade. Generally, schools must have written permission from the parent or eligible student in order to release any information from a student\'s education record.\n\nThis privacy policy also governs how state agencies transmit testing data to federal agencies, such as the Education Data Exchange Network.\n\nThis U.S. federal law also gave students 18 years of age or older, or students of any age if enrolled in any post-secondary educational institution, the right of privacy regarding grades, enrollment, and even billing information unless the school has specific permission from the student to share that specific type of information.\n\nFERPA also permits a school to disclose personally identifiable information from education records of an "eligible student" (a student age 18 or older or enrolled in a postsecondary institution at any age) to his or her parents if the student is a "dependent student" as that term is defined in Section 152 of the Internal Revenue Code. Generally, if either parent has claimed the student as a dependent on the parent\'s most recent income tax statement, the school may non-consensually disclose the student\'s education records to both parents.[3]\n\nThe law allowed students who apply to an educational institution such as graduate school permission to view recommendations submitted by others as part of the application. However, on standard application forms, students are given the option to waive this right.\n\nFERPA specifically excludes employees of an educational institution if they are not students.\n\nThe act is also referred to as the Buckley Amendment, for one of its proponents, Senator James L. Buckley of New York.\n\nAccess to public records[edit]\nThe citing of FERPA to conceal public records that are not "educational" in nature has been widely criticized, including by the act\'s primary Senate sponsor.[4] For example, in the Owasso Independent School District v. Falvo case, an important part of the debate was determining the relationship between peer-grading and "education records" as defined in FERPA. In the Court of Appeals, it was ruled that students placing grades on the work of other students made such work into an "education record." Thus, peer-grading was determined as a violation of FERPA privacy policies because students had access to other students\' academic performance without full consent.[5] However, when the case went to the Supreme Court, it was officially ruled that peer-grading was not a violation of FERPA. This is because a grade written on a student\'s work does not become an "education record" until the teacher writes the final grade into a grade book.[6]\n\nStudent medical records[edit]\nLegal experts have debated the issue of whether student medical records (for example records of therapy sessions with a therapist at an on-campus counseling center) might be released to the school administration under certain triggering events, such as when a student sued his college or university.[7][8]\n\nUsually, student medical treatment records will remain under the protection of FERPA, not the Health Insurance Portability and Accountability Act (HIPAA). This is due to the "FERPA Exception" written within HIPAA.[9]'
print(text)

x = re.findall('[\w ]*\[edit\]', text)
for title in re.findall("[\w ]*\[edit\]",text):
    print(re.split("\[",title)[0])

x = re.findall('([\w ]*)(\[edit\])', text)
for y in x:
    print(y[0])

for x in re.finditer("(?P<name>[\w ]*)(?P<name1>\[edit\])", text):
    print(x.groupdict())

for x in re.finditer("([\w ]*)(\[edit\])", text):
    print(x.group(1))
    print(x.groups()[0])


# Week 1 - LAST Assignment
# -------------------------

# Part A
simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
    Ruth and Peter, their parents, have 3 kids."""
print(re.findall('[A-Z]\w+', simple_string))

# Part B
return [x for x in re.findall('([\w ]+): B', grades)]

# Part C
with open('Applied Data Science Course 1 - Week 1 Assignment.txt') as f:
    logdata = f.read()

print(logdata)

host = re.findall('([\d.]+) - ', logdata)
user_name = re.findall('([-\w\d]+) \[', logdata)
time = re.findall('([\w:/ -]+)\]', logdata)
request = re.findall('"([\S ]+)"', logdata)

lista = []
for x in re.finditer('(?P<host>[\d.]+) - (?P<user_name>[-\w\d]+) \[(?P<time>[\w:/ -]+)\] "(?P<request>[\S ]+)"', logdata):
        print(x.groupdict())
        lista.append(x.groupdict())

# ======================================================================================================================

# Week 2 - Practice
-----------------

df = pd.read_csv('Admission_Predict.csv', index_col=0)
pd.set_option('display.max_columns', 8)


# RENAME DataFrame

# 1.
df = df.rename(mapper=str.strip, axis = 1)
df = df.rename(columns={'SOP': 'Statement of Purpose','LOR':'Letter of Recommendation'})

# 2.
df.columns = ['GRE Score', 'TOEFL Score', 'University Rating', 'Statement of Purpose', 'Letter of Recommendation',
              'CGPA', 'Research', 'Chance of Admit']

# 3.
df.columns = df.columns.str.lower().str.strip()
print(df.columns)

# QUERYING

print(df.loc[(df['chance of admit'] > 0.7)][["gre score","toefl score"]])
print(df.loc[(df['chance of admit'] > 0.7) & (df['gre score'] < 320)]["toefl score"])
print(df.loc[(df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9)])
print(df[df['chance of admit'].gt(0.85) & df['chance of admit'].lt(0.9)])


# Week 2 - LAST Assignment
-------------------------

df = pd.read_csv('Applied Data Science Course 1 - Week 2 Assignment (Immunization data).csv', index_col = 0)
pd.set_option('display.max_columns')

# Question 1
----------

dz = df['EDUC1']
def proportion_of_education():
    dict_edu = {}
    list_names = ["college", "more than high school but not college", "high school", "less than high school", ]
    perc = dz.value_counts(normalize=True)
    for x in range(4):
        dict_edu[list_names[x]] = perc.iloc[x]
    return dict_edu

# Question 2
----------

def average_influenza_doses():
    #kai prin kai meta i stili pou theloyme einai sosto:
    dz1 = df[df['CBF_01'] == 1]['P_NUMFLU']
    dz2 = df['P_NUMFLU'][df['CBF_01'] == 2]
    return (dz1.mean(), dz2.mean())

# Question 3
----------

def chickenpox_by_sex():
    dz = df[df["P_NUMVRC"] > 0][["SEX", "HAD_CPOX"]].dropna()

    male_dz = dz[dz["SEX"] == 1]
    female_dz = dz[dz["SEX"] == 2]

    male1 = male_dz.value_counts(normalize=True).iloc[1]
    male2 = male_dz.value_counts(normalize=True).iloc[0]
    female1 = female_dz.value_counts(normalize=True).iloc[1]
    female2 = female_dz.value_counts(normalize=True).iloc[0]

    return {'male': male1 / male2, 'female': female1 / female2}

# Question 4
----------

df = df[df["HAD_CPOX"] <= 2]
df = df[~df["P_NUMVRC"].isna() & ~df["HAD_CPOX"].isna()] #xreiazetai mono gia to corr2 meso scipy

def corr_chickenpox():
    import scipy.stats as stats

    corr1 = (df[["HAD_CPOX", "P_NUMVRC"]].corr())
    corr2, pval = stats.pearsonr(df["HAD_CPOX"], df["P_NUMVRC"])

    return corr1.iloc[0,1], corr2

# ======================================================================================================================

# Week 3 - Practice
# -----------------

df = pd.read_csv("Applied Data Science Course 1 - World University Rating.csv")
pd.set_option('display.max_rows', 100, 'display.max_columns', 50)

print(df.loc[df.country == 'Greece', ['institution', 'score']])
print(df[df.country == 'Greece'].loc[:,'score'].mean())
print(df.groupby('country')['score'].agg('mean'))

def create_cat(rank):
    if rank <= 100:
        return 'First Tier Top University'
    elif 100 < rank <= 200:
        return 'Second Tier Top University'
    elif 200 < rank <= 300:
        return 'Third Tier Top University'
    return "Other Top University"


df['Rank_Level'] = df['world_rank'].agg(create_cat)

print(df.pivot_table(values='score', index='country', columns='Rank_Level', margins = True, aggfunc=[np.mean]).head())
print(df.pivot_table(values='world_rank', index='country', margins=True, aggfunc=[np.min, np.max, np.mean]).head())


# Week 3 - LAST Assignment
# -------------------------

import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt


def data():
    # 1st file
    energy = pd.read_excel("Applied Data Science Course 1 - Week 3 Assignment (Energy Indicators).xls", usecols='C:F',
                           skiprows=18, header=None, skipfooter=38)
    pd.set_option('display.max_rows', 250, 'display.max_columns', 15)

    energy = energy.rename(columns={2: 'Country', 3: 'Energy Supply', 4: 'Energy Supply per Capita', 5: '% Renewable'})
    energy['Energy Supply'] = energy['Energy Supply'].replace('...', np.NaN).apply(lambda x: x * 1000000)
    energy['Country'] = energy['Country'].apply(lambda x: re.sub(pattern="(\s\(.+\))|[0-9]+", repl='', string=x))
    energy = energy.replace({"Republic of Korea": "South Korea", 'United States of America': "United States",
                             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                             "China, Hong Kong Special Administrative Region": 'Hong Kong'})

    # 2nd file
    GDP = pd.read_csv("Applied Data Science Course 1 - Week 3 Assignment (World Bank).csv", header=4)
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP = GDP.replace({"Korea, Rep.": "South Korea",
                       "Iran, Islamic Rep.": "Iran",
                       "Hong Kong SAR, China": "Hong Kong"})
    GDP_merge = GDP.loc[:, ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]

    # 3rd file
    ScimEn = pd.read_excel("Applied Data Science Course 1 - Week 3 Assignment (Energy Engineering and Power Technology).xlsx")
    ScimEn_merge = ScimEn.iloc[:15]

    return energy, GDP_merge, ScimEn_merge

def answer_one():
    # Merge
    (Energy, GDP, ScimEn) = data()

    df = pd.merge(ScimEn, Energy, how='inner')
    df = pd.merge(df, GDP, how='inner')
    df.set_index('Country', inplace=True)

    return df

def answer_two():
    # (Energy, GDP, ScimEn) = data()
    #
    # df = pd.merge(ScimEn, Energy, how='outer')
    # df = pd.merge(df, GDP, how='outer')
    # df.set_index('Country', inplace=True)
    #
    # return len(df)

    #gia na perasei to test:
    Energy = pd.read_excel("Applied Data Science Course 1 - Week 3 Assignment (Energy Indicators).xls", na_values=["..."], header=None, skiprows=18, skipfooter=38,
                           usecols=[2, 3, 4, 5],
                           names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x * 1000000)

    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)", "")
    Energy['Country'] = Energy['Country'].str.replace(r"\d*", "")
    Energy['Country'] = Energy['Country'].replace({'Republic of Korea': 'South Korea',
                                                   'United States of America': 'United States',
                                                   'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                                   'China, Hong Kong Special Administrative Region': 'Hong Kong'})

    GDP = pd.read_csv("Applied Data Science Course 1 - Week 3 Assignment (World Bank).csv", skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.': 'South Korea',
                                                       'Iran, Islamic Rep.': 'Iran',
                                                       'Hong Kong SAR, China': 'Hong Kong'})

    ScimEn = pd.read_excel("Applied Data Science Course 1 - Week 3 Assignment (Energy Engineering and Power Technology).xlsx")

    inner1 = pd.merge(ScimEn, Energy, how="inner", left_on="Country", right_on="Country")

    GDP.rename(columns={"Country Name": "Country"}, inplace=True)
    GDP = GDP.loc[:, ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', "Country"]]
    inner2 = pd.merge(inner1, GDP, how="inner", left_on="Country", right_on="Country").set_index("Country")

    outer1 = pd.merge(ScimEn, Energy, how="outer", left_on="Country", right_on="Country")
    outer2 = pd.merge(outer1, GDP, how="outer", left_on="Country", right_on="Country").set_index("Country")

    return len(outer2)-len(inner2)

print(answer_two())

def answer_three():
    df = answer_one()
    df["avgGDP"] = df.iloc[:, -10:].apply(lambda x: np.nanmean(x), axis=1)
    df = df.sort_values("avgGDP", ascending=False)

    return df["avgGDP"]

def answer_four():
    df = answer_one()
    df["avgGDP"] = df.iloc[:, -10:].apply(lambda x: np.nanmean(x), axis=1)
    df = df.sort_values("avgGDP", ascending=False)

    # episis swsto:
    # return df["2015"][5] - df["2006"][5]
    return abs(df.iloc[5,-11] - df.iloc[5, -2])

def answer_five():
    df = answer_one()

    df['Energy Supply per Capita'] = df['Energy Supply per Capita'].replace('...', np.NaN)

    return df['Energy Supply per Capita'].dropna().mean()

def answer_six():
    df = answer_one()

    max_ren = df['% Renewable']

    return (max_ren.idxmax(axis = 0), max_ren.max())
    # episis swsto:
    # df = answer_one()
    # df = df.reset_index()
    # max_ren = df[df["% Renewable"] == df["% Renewable"].max()].iloc[0]
    # return (max_ren["Country"], max_ren["% Renewable"])

def answer_seven():
    df = answer_one()
    df['ratio'] = df['Self-citations'] / df['Citations']
    max_ratio = df['ratio']

    return (max_ratio.idxmax(axis = 0), max_ratio.max())
    # episis swsto:
    # return (df[df['ratio'] == df['ratio'].max()].index[0], df['ratio'].max())

def answer_eight():
    df = answer_one()
    df['population'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df = df.sort_values('population', ascending=False)

    return df['population'].index[2]

def answer_nine():
    (energy, _, ScimEn ) = data()

    df = pd.merge(energy, ScimEn, how = 'inner', on = 'Country')
    df['population'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['docs_per_person'] = df['Citable documents'] / df['population']

    return df[['docs_per_person', 'Energy Supply per Capita']].corr().iloc[0,1]

def plot9():
    (energy, _, ScimEn) = data()
    df = pd.merge(energy, ScimEn, how = 'inner', on = 'Country')
    df['population'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['docs_per_person'] = df['Citable documents'] / df['population']

    plt.scatter(df['docs_per_person'], df['Energy Supply per Capita'])
    plt.show()

def answer_ten():
    df = answer_one()

    median = df['% Renewable'].median()
    df['HighRenew'] = df['% Renewable'].apply(lambda x: 1 if x >= median else 0)
    # df = df.sort_values('Rank')

    return df['HighRenew']

def answer_eleven():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    df = answer_one()
    df = df.reset_index()
    df['population'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['Continent'] = df['Country'].apply(lambda x: ContinentDict[x])
    df = df.groupby('Continent')['population'].agg([len, np.sum, np.mean, np.std]).rename(columns={"len": "size"})

    return df

def answer_twelve():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    df = answer_one()
    df = df.reset_index()

    df['Continent'] = df['Country'].apply(lambda x: ContinentDict[x])
    df['% Renewable'] = pd.cut(df['% Renewable'], 5)
    df = df.groupby(['Continent', '% Renewable']).apply(len)
    # df = df.groupby(['Continent', '% Renewable']).size()
    return df

def answer_thirteen():
    df = answer_one()

    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['PopEst'] = df['PopEst'].apply(lambda x: f"{x:,}")

    return df['PopEst']

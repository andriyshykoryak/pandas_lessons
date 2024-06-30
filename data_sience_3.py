import pandas as pd
df = pd.read_csv('pandas_lessons\\GoogleApps.csv')

# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?
print((df['Category']=='BUSINESS').value_counts())
# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих.
res=df['Content Rating'].value_counts()
print(round(res['Teen']/res['Everyone 10+'],3))

# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.

print(round(round(df[df['Type']=='Paid']['Rating'].mean(),2)-round(df[df['Type']=='Free']['Rating'].mean(),2),2))

# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Paid')?
# Відповідь запиши з точністю до сотих.

# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.

print(round(df[df['Category']=='COMICS']['Size'].max(),2))
print(round(df[df['Category']=='COMICS']['Size'].min(),2))

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?

print(df[(df['Category']=='FINANCE')&(df['Rating']>4.5)]['Installs'].value_counts().sum())

# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?

free=df[(df['Type']=='Free') & (df['Rating']>4.9)&(df['Category']=='GAME')].value_counts().sum()
paid=df[(df['Type']=='Paid') & (df['Rating']>4.9)&(df['Category']=='GAME')].value_counts().sum()
print(free/paid)
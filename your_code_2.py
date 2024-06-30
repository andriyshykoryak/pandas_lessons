import pandas as pd
df = pd.read_csv('pandas_lessons\\GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?


# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?


# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?


# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?


# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
# art_and = df[df['Category']=='ART_AND_DESIGN']
# print(art_and['Installs'].median())


free=df[df['Type']=='Free']['Reviews'].max()
paid=df[df['Type']=='Paid']['Reviews'].max()

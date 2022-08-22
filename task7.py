#List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
#değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
import pandas as pd
import seaborn as sns
df = sns.load_dataset("car_crashes")
df = df.drop('abbrev', axis=1)
df = df.drop('no_previous', axis=1)

columns = ["total", "speeding", "alcohol", "not_distracted", "ins_premium", "ins_losses"]
df2 = pd.DataFrame(df.head(5).values, range(5), columns = columns)
print(df2)
print(df.head(5))

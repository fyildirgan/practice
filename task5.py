# List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.
import numpy
import seaborn as sns

df = sns.load_dataset("car_crashes")

a = []
# print(df)
for col in df.columns:
    if (df[col].dtype.type == numpy.float64):
        a.append("NUM_"+ col.upper())
    else:
        a.append(col.upper())
print(a)












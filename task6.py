#: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
#değişkenlerin isimlerinin sonuna "FLAG" yazınız.
import seaborn as sns
df = sns.load_dataset("car_crashes")

a = []
for col in df.columns:
    if ("no" in col):
        a.append(col)
    else:
        a.append(col + "FLAG")
print(a)




















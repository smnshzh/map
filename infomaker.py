import pandas as pd


df = pd.read_excel("map.xlsx")
data_list = df.values.tolist()
entery = input("Give a name for your file")
with open(f"{entery}.js",'w',encoding = 'utf-8') as f:
   f.write("const info = ")
   f.write(str(data_list))

f.close()

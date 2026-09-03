import pandas as pd
data=pd.read_csv("scholar_data.csv")
print("Scholar Data:")
print(data)
data["Average"]=data[["Maths","Python","Statistics"]].mean(axis=1)
print("Scholar Average:")
print(data[["Scholar","Average"]])

highest=data["Average"].max()
lowest=data["Average"].min()
print("\nHighest Average:",highest)
print("Lowest Average:",lowest)

top_student=data.loc[data["Average"].idxmax(),"Scholar"]
print("\nTop Scholar:",top_student)

import matplotlib.pyplot as plt
plt.bar(data["Scholar"],data["Average"])
plt.xlabel("Scholar Name")
plt.ylabel("Average Marks")
plt.title("Scholar Average Marks")
plt.savefig("Scholar_Average_Marks.png")
plt.show()

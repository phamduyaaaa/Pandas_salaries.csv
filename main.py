import pandas as pd
df = pd.read_csv("ds_salaries.csv",sep=",")
#Task_1
print("\n||_______________TASK 1_______________||")
df_job = df[["job_title","salary_in_usd"]]
# people = df["job_title"].value_counts()
df_job = df_job.groupby("job_title").mean()
df_job = df_job.sort_values(by = "salary_in_usd",ascending = False)
print("-----JOB CÓ MỨC LƯƠNG TRUNG BÌNH THEO USD CAO NHẤT LÀ:-----\n",df_job.head(1))
print("\n")
print("\n")
#Task_2
print("\n||_______________TASK 2_______________||")
df_ds = df[["job_title","salary_in_usd","employee_residence"]]
df_ds = df_ds.loc[df["job_title"] == "Data Scientist"]
df_ds = df_ds.groupby("employee_residence").agg({"salary_in_usd": "mean"}).sort_values("salary_in_usd",ascending = False)
print("-----DS CÓ MỨC LƯƠNG TB CAO NHẤT MANG QUỐC TỊCH:----- \n",df_ds.head(1))
print("\n")
print("\n")
#Task_3
print("\n||_______________TASK 3_______________||")
df_usa = df.loc[df["company_location"] == "US"]
df_usa = df_usa.loc[df["employee_residence"] == "US"]
df_usa = df_usa[["salary_in_usd","employee_residence","company_location"]]

df_foreign_usa = df.loc[df["company_location"] == "US"]
df_foreign_usa = df_foreign_usa.loc[df["employee_residence"] != "US"]
df_foreign_usa = df_foreign_usa[["salary_in_usd","employee_residence","company_location"]]

print("-----MỨC LƯƠNG TRUNG BÌNH NHÂN SỰ TRONG NƯỚC LÀM VIỆC TẠI USA:-->",df_usa["salary_in_usd"].mean())
print("-----MỨC LƯƠNG TRUNG BÌNH NHÂN SỰ NGOẠI QUỐC LÀM VIỆC TẠI USA:-->",df_foreign_usa["salary_in_usd"].mean())
print("\n")
print("\n")
#Task_4
print("\n||_______________TASK 4_______________||")
df_DE_levelSE_SM = df[["experience_level","job_title","company_size","salary_in_usd","company_location"]]
df_DE_levelSE_SM = df_DE_levelSE_SM.loc[(df_DE_levelSE_SM["experience_level"] == "SE") & (df_DE_levelSE_SM["job_title"] == "Data Engineer") &(df_DE_levelSE_SM["company_location"] == "US")]
df_DE_levelSE_SM = df_DE_levelSE_SM.loc[(df_DE_levelSE_SM["company_size"] =="S") | (df_DE_levelSE_SM["company_size"] =="L")]
print("-----MỨC LƯƠNG TRUNG BÌNH CỦA DA(SE level) Ở CÔNG TY VỪA VÀ NHỎ Ở USA LÀ:-->",df_DE_levelSE_SM["salary_in_usd"].mean())
print("\n")
print("\n")
#Task_5
print("\n||_______________TASK 5_______________||")
df_DS_USA = df[["job_title","experience_level","salary_in_usd","company_location"]]
df_DS_USA = df_DS_USA.loc[(df_DS_USA["job_title"] == "Data Scientist")&(df_DS_USA["company_location"] == "US")]
df_DS_USA = df_DS_USA.groupby("experience_level").agg({"salary_in_usd": "mean"})
print("-----MỨC LƯƠNG DS Ở USA LÀ:-----\n",df_DS_USA)
print("\n")
print("\n")
#Task_6
print("\n||_______________TASK 6_______________||")
df_foreign_largecompany = df[["employee_residence","company_location","company_size"]]
df_foreign_largecompany = df_foreign_largecompany.loc[(df_foreign_largecompany["company_size"] == "L") & (df_foreign_largecompany["company_location"] == "US")]
print(df_foreign_largecompany.shape)
# ---> tổng nhân sự là 106
df_foreign_largecompany = df_foreign_largecompany.loc[df["employee_residence"] != "US"]
print(df_foreign_largecompany.shape)
# --> tổng nhân sự nước ngoài là 8
print("-----TỈ LỆ NHÂN SỰ NƯỚC NGOÀI Ở CÔNG TY LỚN TẠI USA CHIẾM:-->",8*100/106,"%")
print("\n")
print("\n")
#Task_7
print("\n||_______________TASK 7_______________||")
df_top3_MI = df[["job_title","employee_residence","salary_in_usd"]]
df_top3_MI = df_top3_MI.loc[df_top3_MI["employee_residence"] == "US"]
df_top3_MI = df_top3_MI.groupby("job_title").agg({"salary_in_usd": "mean"}).sort_values("salary_in_usd",ascending = False)
print("-----TOP 3 JOB (XẾP THEO TIÊU CHÍ LƯƠNG) CHO LEVEL MI:-----\n",df_top3_MI.head(3))
print("\n")
print("\n")
#Task_8
print("\n||_______________TASK 8_______________||")
df_germany_job = df[["job_title","salary_in_usd","employee_residence"]]
df_germany_job = df_germany_job.loc[df_germany_job["employee_residence"] == "DE"]
print(df_germany_job)
df_germany_job = df_germany_job.groupby("job_title").agg({"salary_in_usd" : "mean"}).sort_values("salary_in_usd")
print("-----JOB Ở ĐỨC CÓ MỨC LƯƠNG TRUNG BÌNH THẤP NHẤT LÀ:------\n",df_germany_job.head(1))
print("\n")
print("\n")
#Task_9
print("\n||_______________TASK 9_______________||")
# ml_deve = df.loc[df.job_title == "Machine Learning Developer"]
# print(ml_deve.salary_in_usd)
df_SE = df[["job_title","experience_level","salary_in_usd"]]
df_SE = df_SE.loc[df_SE["experience_level"]=="SE"]
df_SE = df_SE.groupby("job_title").agg({"salary_in_usd":"mean"})
df_SE["salary_in_usd"].rename(level = 0, index = "SE", inplace = True)

df_MI = df[["job_title","experience_level","salary_in_usd"]]
df_MI = df_MI.loc[df_MI["experience_level"]=="MI"]
df_MI = df_MI.groupby("job_title").agg({"salary_in_usd":"mean"})
df_MI["salary_in_usd"].rename(level = 0, index = "MI", inplace = True)

df_distance_salary = pd.merge(df_SE,df_MI,on = "job_title")
print(df_distance_salary)
df_distance_salary["distance"] = abs(df_distance_salary["salary_in_usd_y"] - df_distance_salary["salary_in_usd_x"])
print("-----JOB CÓ KHOẢNG CÁCH THU NHẬP GIỮA SE VÀ MI ÍT NHẤT LÀ:-----")
print(df_distance_salary["distance"].sort_values().head(1))
print("\n")
print("\n")
#Task_10
print("\n||_______________TASK 10_______________||")
df_10 = df[["experience_level","job_title","salary_in_usd"]]
df_top5_EN = df_10.loc[df["experience_level"] == "EN"]
df_top5_EN = df_top5_EN.groupby("job_title").agg({"salary_in_usd":"mean"}).sort_values("salary_in_usd",ascending = False).head(5)

df_top5_MI = df_10.loc[df["experience_level"] == "MI"]
df_top5_MI = df_top5_MI.groupby("job_title").agg({"salary_in_usd":"mean"}).sort_values("salary_in_usd",ascending = False).head(5)

df_top5_SE = df_10.loc[df["experience_level"] == "SE"]
df_top5_SE = df_top5_SE.groupby("job_title").agg({"salary_in_usd":"mean"}).sort_values("salary_in_usd",ascending = False).head(5)

df_top5_EX = df_10.loc[df["experience_level"] == "EX"]
df_top5_EX = df_top5_EX.groupby("job_title").agg({"salary_in_usd":"mean"}).sort_values("salary_in_usd",ascending = False).head(5)

# df_top5 = pd.merge(df_top5_EX,df_top5_EN,on="job_title")
print(df_top5_EX)
print(df_top5_SE)
print(df_top5_MI)
print(df_top5_EN)
print("\n")
print("\n")
#Task_11
print("\n||_______________TASK 11_______________||")
print("\n")
print("\n")
#Task_12
print("\n||_______________TASK 12_______________||")
df_foreign = df[["company_location","employee_residence","salary_in_usd"]]
df_foreign = df_foreign.loc[df_foreign["employee_residence"] != df_foreign["company_location"]]
df_foreign = df_foreign.groupby("company_location").agg({"salary_in_usd":"mean"}).sort_values("salary_in_usd",ascending=False).head(1)
print("---->BA LAN LÀ NƯỚC TRẢ LƯƠNG CHO NHÂN SỰ NƯỚC NGOÀI CAO NHÁT:-----")
print(df_foreign)
print("\n")
print("\n")
#Task_13
print("\n||_______________TASK 13_______________||")
df_ex_level = df[["experience_level","salary_in_usd","company_size"]]
df_ex_level = df_ex_level.groupby(["experience_level","company_size"])
print(df_ex_level)
print("---->Cùng experience_level, công ty quy mô càng lớn trả lương càng cao!!!")
print("\n")
print("\n")
#Task_14
# print("\n||_______________TASK 14_______________||")
# print("-----SẮP XẾP JOB THEO THỨ TỰ TĂNG DẦN THEO THU NHẬP TRUNG BÌNH LÀ:-----\n",df_job.sort_values("salary_in_usd"))
# print("\n")
# print("\n")
# #Task_15
# print("\n||_______________TASK 15_______________||")
# df_country = df[["job_title","company_location","salary_in_usd"]]
# df_country = df_country.groupby(["company_location","job_title"]).agg({"salary_in_usd":"mean"}).sort_values("salary_in_usd",ascending=False)
# top1 = df_country.groupby("company_location").head(1)
# print(df_country)
# down3 = df_country.groupby("company_location").tail(3)
# top1_target = top1.groupby("job_title").mean()
# down3_target = down3.groupby("job_title").mean()
# print(top1_target)
# print(down3_target)
# print(pd.merge(top1_target,down3_target,on="job_title"))
# print("\n")
# print("\n")



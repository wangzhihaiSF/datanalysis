f = open("data_project1.csv", "r", encoding="utf8")
data_p1 = f.readlines()[1:] # 从 1 开始过滤列名
for i in data_p1:
    print(i.split(","))



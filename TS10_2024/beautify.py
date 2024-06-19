import pandas as pd

info = pd.read_csv("crawl_results.csv").set_index("ID").sort_index()
info["Chuyên"] = info["Chuyên"].map(lambda a: max(0, a))
info["Toán"] = info["Toán"].map(lambda a: max(0, a))
info["Văn"] = info["Văn"].map(lambda a: max(0, a))
info["Ngoại Ngữ"] = info["Ngoại Ngữ"].map(lambda a: max(0, a))

# def cal_point(row):
#     row["Điểm tổng (không chuyên)"] = int(row["Toán"]) + int(row["Văn"]) + int(row["Ngoại Ngữ"])
#     row["Điểm tổng (chuyên)"] = int(row["Toán"]) + int(row["Văn"]) + int(row["Ngoại Ngữ"]) + int(row["Chuyên"])*2

#     # if row["Toán"] < 1 or row["Văn"] < 1 or row["Ngoại Ngữ"] < 1:
#     #     row["Điểm tổng (không chuyên)"] = -1
#     #     row["Điểm tổng (chuyên)"] = -1
#     # else:
#     #     if row["Chuyên"] < 1:
#     #         row["Điểm tổng (chuyên)"] = -1

info["Điểm tổng (không chuyên)"] = info["Toán"] + info["Văn"] + info["Ngoại Ngữ"]
info["Điểm tổng (chuyên)"] = info["Toán"] + info["Văn"] + info["Ngoại Ngữ"] + info["Chuyên"]*2
# info = info.apply(cal_point, axis='columns')

print(info)
info.to_csv("real_results.csv", sep=',', encoding='utf-8')
info.to_excel("real_results.xlsx")
# print(info)
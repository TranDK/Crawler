import json
import requests
from multiprocessing import Process, cpu_count

def crawl(ID):
  link = f'https://s6.tuoitre.vn/api/diem-thi-lop-10.htm?keywords={str(ID)}&year=2024&sitename=tuoitre.vn'
  response = requests.get(link, headers = {'Origin': 'https://tuoitre.vn'})
  return response.json()["data"][0]

with open('crawl_results.csv', "w", encoding='utf-8') as output:
  output.write('"ID","Tên","Ngày sinh","Họ Tên","Tỉnh","Toán","Văn","Ngoại Ngữ","Chuyên"\n')

def loop(start, end):
  with open('crawl_results.csv', "a", encoding='utf-8') as output:
    for i in range(start, end+1):
      try:
        ans = crawl(i)
      except:
        pass
      else:
        output.write(f'"{ans["Id"]}","{ans["HO_TEN"]}","{ans["NGAY_SINH"]}","{ans["TINH"]}","{ans["TOAN"]}","{ans["VAN"]}","{ans["NGOAI_NGU"]}","{ans["CHUYEN"]}"\n')


if __name__ == "__main__":
  range = [[9901, 9438], [90000, 100200], [100201, 110400], [110401, 120600], [120601, 130800], [130801, 141000], [141001, 151200], [151201, 161400], [161401, 171600], [171601, 181800], [181801, 192007]]
  pros = []

  for i in range:
    pros.append(Process(target=loop, args=(i[0], i[1])))

  for p in pros:
    p.start()

  for p in pros:
    p.join()
  
  print("ggez")
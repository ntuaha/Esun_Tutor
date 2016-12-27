import xlrd
import csv
banks = []
data_count = 0
book = xlrd.open_workbook("./22010.xls")
#每個sheet都要讀
for sh_num in range(book.nsheets): 
    sh = book.sheet_by_index(sh_num)
    num_rows = sh.nrows
    num_cols = sh.ncols
    for count_rows in range(num_rows):
        line_data=sh.cell_value(rowx=count_rows,colx =1 )
        banks_name=sh.cell_value(rowx=count_rows,colx =0 ).replace("\u3000","")
        #只抓開始有金額的部分
        #排除銀行名稱為“總計”資料
        if  isinstance(line_data, float) & (banks_name != '總計'):
            banks.append(extract_bank(count_rows))

#輸出檔案 csv
with open("output_CSV.csv","w",newline="") as datacsv:
     csvwriter = csv.writer(datacsv,dialect = ("excel"))
     #寫標題
     #csvwriter.writerow(banks[0])
     csvwriter.writerow(["報表編號",
                         "時間",
                         "報表代號",
                         "報表名稱",
                         "銀行中文名稱",
                         "銀行英文名稱",
                         "銀行類別",
                         "金控註記",
                         "活期性存款",
                         "定期性存款",
                         "外匯存款",
                         "公庫存款及其他"
                        ])
    #寫資料
     for data_count in range(len(banks)):
         #csvwriter.writerow(banks[n].values())            
         csvwriter.writerow([banks[n]["報表編號"],
                             banks[n]["時間"],
                             banks[n]["報表代號"],
                             banks[n]["報表名稱"],
                             banks[n]["銀行中文名稱"],
                             banks[n]["銀行英文名稱"],
                             banks[n]["銀行類別"],
                             banks[n]["金控註記"],
                             banks[n]["活期性存款"],
                             banks[n]["定期性存款"],
                             banks[n]["外匯存款"],
                             banks[n]["公庫存款及其他"]
                            ])            

print('資料筆數：',data_count)
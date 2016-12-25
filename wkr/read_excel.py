def extract_bank(count_rows):
    bank = {"銀行類別":"本國銀行","報表編號":"22010","時間":"010509"}
    
    title=sh.cell_value(rowx=0,colx = 0).replace("\u3000","")
    
    name_zh = sh.cell_value(rowx=count_rows,colx = 0).replace("\u3000","")
    if "#" in name_zh:
        fhc_flag = "T"
    else:
        fhc_flag = "F"
    
    name_zh = name_zh.replace("#","")    
    name_en = sh.cell_value(rowx=count_rows+1,colx = 0).replace("\u3000","")   
    
    md = sh.cell_value(rowx=count_rows,colx = 1) * 1e6
    fd = sh.cell_value(rowx=count_rows,colx = 2) * 1e6
    fy = sh.cell_value(rowx=count_rows,colx = 3) * 1e6
    dc = sh.cell_value(rowx=count_rows,colx = 4) * 1e6 
    
    #bank["時間"] =
    #bank["報表編號"] =
    bank["報表代號"] = title[:3]
    bank["報表名稱"] = title[3:19]
    bank["活期性存款"] = md
    bank["定期性存款"] = fd
    bank["外匯存款"] = fy
    bank["公庫存款及其他"] = dc
    bank["銀行中文名稱"] = name_zh
    bank["銀行英文名稱"] = name_en
    bank["金控註記"] = fhc_flag
    
    return bank
    
import xlrd
banks = []
data_count = 0
book = xlrd.open_workbook("./22010.xls")
for sh_num in range(book.nsheets): 
    sh = book.sheet_by_index(sh_num)
    num_rows = sh.nrows
    num_cols = sh.ncols
    for count_rows in range(num_rows):
        line_data=sh.cell_value(rowx=count_rows,colx =1 )
        if  isinstance(line_data, float):
            data_count=data_count+1
            banks.append(extract_bank(count_rows))
print(data_count)
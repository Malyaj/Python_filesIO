import pandas as pd
import codecs

path = r"D:\Users\703143501\Documents\GE Confidential\WIP\2019\weekly_reports\Metric report FW 03\data\cdsi.xls"

fp= codecs.open(path, "r", "utf-16")
lines= fp.readlines()

#rows_to_ignore = [0,2]
header_row_location = 2
tab = '\t'

for line_number in range(len(lines)):
    if line_number < 2:
        continue
    elif line_number == 2:
        headers = lines[line_number].split(tab)[:-2]
        df = pd.DataFrame(columns = headers)
    else:
        # insert row
        row = lines[line_number].split(tab)[:-2]
        df = df.append(pd.Series(row, index=df.columns ), ignore_index=True)
        #df.append(pd.Series(row, index=df.columns ), ignore_index=True)

# export this df to an excel file
path_to_save = r"D:\Users\703143501\Documents\GE Confidential\WIP\2019\weekly_reports\Metric report FW 03\data\cdsi.csv"
df.to_csv(path_to_save, index = False)

# this could be more flexible

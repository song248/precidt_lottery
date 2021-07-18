import pandas as pd

def load_data():
    excel = pd.read_excel('C:/Users/songtg/Desktop/lotto/excel.xlsx', header=None)
    excel = excel.drop(index=0)
    excel = excel.drop(index=1)
    excel = excel.drop(index=2)
    excel = excel.drop(columns=[0,2,3,4,5,6,7,8,9,10,11,12])
    excel = excel.rename(columns={1: 'round'})
    for i in range(0, 6):
        excel = excel.rename(columns={i+13: i+1})
    excel = excel.rename(columns={19: 'bonus'})
    excel = excel.assign(number = [i for i in range(1, len(excel)+1)])
    excel = excel.set_index("number")
    excel = excel[::-1]

    return excel
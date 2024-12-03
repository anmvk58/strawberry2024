import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    file_shipper = pd.read_excel("C:\\Users\\anmv\\Desktop\\Dâu Tây\\Shipper.xlsx")

    list_shipper = file_shipper.shipper.unique()
    print(list_shipper)
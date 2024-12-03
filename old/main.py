import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    filename = datetime.today().strftime('%Y%m%d')
    # print(filename)
    # filename = '20230219'
    df = pd.read_excel(f"C:\\Users\\gameb\\OneDrive\\Desktop\\Dâu Tây\\{filename}.xlsx")
    # print(df)
    df_details = pd.read_excel(f"C:\\Users\\gameb\\OneDrive\\Desktop\\Dâu Tây\\{filename}d.xlsx")
    df_filter = df_details[['Mã hóa đơn', 'Tên hàng', 'Giá bán']]
    df_filter_only_ship = df_filter.loc[df_filter['Tên hàng'] == 'Phí Ship']
    # df_filter_only_ship['Đơn giá'] = df_filter_only_ship['Đơn giá'].astype(int)
    result = df.merge(df_filter_only_ship, how='left', on='Mã hóa đơn')

    file_shipper = pd.read_excel("C:\\Users\\gameb\\OneDrive\\Desktop\\Dâu Tây\\Shipper.xlsx")
    df_ship = file_shipper[['Mã hóa đơn', 'shipper']]
    list_shipper = df_ship.shipper.unique()

    final_result = result.merge(df_ship, how='left', on='Mã hóa đơn')

    writer = pd.ExcelWriter(f"C:\\Users\\gameb\\OneDrive\\Desktop\\Dâu Tây\\{filename}result.xlsx", engine='xlsxwriter')
    final_result.to_excel(writer, sheet_name=filename, index=False)

    for shipper in list_shipper:
        df = final_result.loc[final_result['shipper'] == shipper]
        df.to_excel(writer, sheet_name=shipper, index=False)

    writer.close()
    # print(final_result)
    # result.to_excel(f"C:\\Users\\gameb\\OneDrive\\Desktop\\Dâu Tây\\{filename}result.xlsx", engine='xlsxwriter', index=False)
    print("Finished")
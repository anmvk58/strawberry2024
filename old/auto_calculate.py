import pandas as pd
from datetime import datetime
def calculate_for_one_ship(df, shipper_name):
    df_notchuyenkhoan = df.loc[df['chuyển khoản'] != 1]
    tong_tien = sum(df_notchuyenkhoan['tổng tiền'])
    tong_don = df.shape[0]
    tien_ship = tong_don*25
    phai_thu = tong_tien - tien_ship

    data = [['Tổng tiền', tong_tien], ['Tiền ship', tien_ship], ['Cắt ship', 0], ['Phải thu', phai_thu]]
    df_result = pd.DataFrame(data, columns=['Shipper', shipper_name])
    return df_result


if __name__ == '__main__':
    filename = datetime.today().strftime('%Y%m%d')
    df = pd.read_excel(f"C:\\Users\\gameb\\OneDrive\\Desktop\\filenhap.xlsx")
    list_order = []
    for order in df['mã đơn']:
        # list_order.append("HD00" + str(order))
        list_order.append("" + str(order))

    df['OrderCode'] = list_order
    new_cols = ['OrderCode', 'tổng tiền', 'chuyển khoản', 'ship', 'địa chỉ']
    final_df = df[new_cols]

    writer = pd.ExcelWriter(f"C:\\Users\\gameb\\OneDrive\\Desktop\\{filename}_result.xlsx", engine='xlsxwriter')
    final_df.to_excel(writer, sheet_name='Result', index=False)

    list_shipper = final_df.ship.unique()

    total_shipper_df = pd.DataFrame()

    for ship in list_shipper:
      df_ship = final_df.loc[final_df['ship'] == ship]
      df_cal = calculate_for_one_ship(df_ship, ship)

      total_shipper_df =  pd.concat([total_shipper_df, df_cal], axis=1)

      df_cal.to_excel(writer, sheet_name=ship, index=False, startrow=0, startcol=0)
      df_ship.to_excel(writer, sheet_name=ship, index=False ,startrow=df_cal.shape[0]+2 , startcol=0)

      print(df_cal)
      print("---")

    total_shipper_df.to_excel(writer, sheet_name="Total", index=False ,startrow=df_cal.shape[0]+2 , startcol=0)
    writer.close()
import re
import pandas as pd
from unidecode import unidecode

DICT_KIOT = {
    'svip': 'DAU_SVIP',
    'vip': 'DAU_VIP',
    'nhỡ': 'DAU_NHO',
    'bi': 'DAU_BI',
    've': 'DAU_VE',
    'hộp quà svip': 'HOP_QUA_SVIP',
    'hộp quà vip': 'HOP_QUA_VIP',
    'hộp quà nhỡ': 'HOP_QUA_NHO',
    'hộp quà bi': 'HOP_QUA_BI',
    'cb ve': 'COMBO_VE',
    'cb bi': 'COMBO_BI',
    'cb nhỡ': 'COMBO_NHO',
    'cb vip': 'COMBO_VIP',
    'mận': 'MANHAU',
}


def convert_order(raw_order):
    list_order = raw_order.split("\n")
    result = []
    for item in list_order:
        item_normalized = re.sub(r'\s+', ' ', item)
        index = item_normalized.strip().find(' ')
        quantity = float(item_normalized[0:index])
        product = item_normalized[index+1:]
        # if unidecode(product).lower()[:2] == "cb":
        #     quantity = quantity*2
        #     product = product[3:]
        result.append({
            'product': product.strip(),
            'quantity': quantity
        })
    return result


if __name__ == '__main__':
    df = pd.read_excel("input_auto.xlsx", dtype=str)
    for item in df.itertuples():
        note = item.note if not pd.isna(item.note) else ''
        print(note)

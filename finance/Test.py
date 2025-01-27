# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
#
# # Data
# quarters = [
#     "Q2 2023", "Q3 2023", "Q4 2023",
#     "Q1 2024", "Q2 2024", "Q3 2024"
# ]
#
# banks = {
#     "VPBank (VPB)": [5.6, 5.7, 5.75, 5.8, 5.9, 5.98],
#     "HDBank (HDB)": [5.2, 5.25, 5.3, 5.35, 5.4, 5.49],
#     "Techcombank (TCB)": [4.3, 4.25, 4.2, 4.15, 4.1, 4.01],
#     "MBBank (MBB)": [4.3, 4.32, 4.33, 4.35, 4.4, 4.23],
#     "TPBank (TPB)": [4.1, 4.15, 4.2, 4.22, 4.25, 4.23],
#     "VIB": [4.1, 4.12, 4.15, 4.18, 4.22, 4.25],
#     "Vietcombank (VCB)": [2.98, 3.0, 3.02, 3.01, 3.01, 2.98],
#     "Nam A Bank (NAB)": [3.62, 3.65, 3.7, 3.75, 3.76, 3.78]
# }
#
# # Create plot
# plt.figure(figsize=(14, 8))
# for bank, values in banks.items():
#     plt.plot(quarters, values, marker='o', label=bank)
#
# # Customization
# plt.title("Sự thay đổi NIM của các ngân hàng từ Q2 2023 đến Q3 2024", fontsize=16)
# plt.xlabel("Quý", fontsize=14)
# plt.ylabel("NIM (%)", fontsize=14)
# plt.xticks(rotation=45)
# plt.grid(alpha=0.4)
# plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), title="Ngân hàng", fontsize=12)
# plt.tight_layout()
#
# # Show plot
# plt.show()

if __name__ == '__main__':
    for i in range(14):
        char_i = chr(66 + i * 2)
        print(f'{char_i} - {66 + i * 2} - {i}')
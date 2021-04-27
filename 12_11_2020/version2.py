# for j in range(1,SoKhungTinHieu+1):
#     nL = SoMauTrenKhung*j-SoMauTrenKhung+1
#     nR = SoMauTrenKhung*j + 2
#     # tinhieu = data[33281:33602]
#     tinhieu = data[nL:nR]
#     for k in range(1,SoMauTrenKhung+1):
#         tong = 0
#         for i in range(1,SoMauTrenKhung+1):
#             Rt = 0
#             if k+i <= SoMauTrenKhung:
#                 Rt = tinhieu[i+k]
#             #ttq[k] = ttq[k] + tinhieu[i]*Rt
#             tong = tong + tinhieu[i] * Rt
#         ttq[j] = tong


# tinhieu = data[33281:33602]
# for k in range(1,SoMauTrenKhung+1):
#     for i in range(1,SoMauTrenKhung+1):
#         Rt = 0
#         if k+i <= SoMauTrenKhung:
#             Rt = tinhieu[i+k]
#         ttq[k] = ttq[k] + tinhieu[i]*Rt
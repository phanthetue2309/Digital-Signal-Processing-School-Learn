from scipy.io import wavfile
import matplotlib.pyplot as plt 
import numpy as np

samplerate, data = wavfile.read('Audio/trai_Heo.wav')
times = len(data)/float(samplerate) # độ dài tín hiệu 
dt = 1/samplerate 

data = data / max(data) 
SoKhungTinHieu = (int)(times // 0.02) 
SoMauTrenKhung = (int)(0.02*16000 )
print(len(data),SoKhungTinHieu)

fig, ax = plt.subplots(2)
fig, ax1 = plt.subplots(2)
ax[0].plot(data)
ax[0].set_title("Tín hiệu đầu vào")
ax[0].set_ylabel("Amplitidue")
ax[0].set_xlabel("Index of sample")
Rt = np.zeros(SoMauTrenKhung+1)
# tính độ trễ trên khung  
# khung 105 cuả file studio_male

def draw(i):
    nL = SoMauTrenKhung*i
    nR = SoMauTrenKhung*(i+1)
    x = np.arange(SoMauTrenKhung)
    ax1[0].plot(x,data[nL:nR])
    ax1[0].set_xlabel("Frames")
    ax1[0].set_ylabel("Amplitidue")
    ax1[0].set_title("Khung tín hiệu thứ " +str(i+1))

def hamcucdai(i):
    ttq1 = hamtutuongquan(i) # gọi hàm tự tương quan
    maxP = nguong_y = 0.5 * ttq1[0] # ngưỡng xác định (giá trị cực đại là giá trị đầu tiên)
    P = check  = 0
    vitri = -1   
    for m in range(0,SoMauTrenKhung):
        if (ttq1[m] > nguong_y) : # nếu giá trị tự tương quan > ngưỡng thì xét điểm bắt đầu trên ngưỡng
            if check == 0  :
                check = 1 # đánh dấu để thông báo là đang trên ngưỡng 
            else :
                if (maxP < ttq1[m] and P != 0 and 45 < m < 213): 
                    maxP = ttq1[m]
                    vitri = m                
        elif (ttq1[m] < nguong_y and check == 1 ):  
            if P == 0 : 
                P = m
            check = 0 # đánh dấu để thông báo là đã xuống dưới ngưỡng
    new_F0 = 0
    T0 = vitri*0.02/SoMauTrenKhung  
    if T0 < 1/75 and T0 > 1/350 : # điều kiện để tần số nằm trong khoảng 75 < Fs < 350 
        new_F0 = 1 / T0 
    F0[i] = new_F0
    x = np.arange(SoMauTrenKhung)
    if (new_F0 == 0) :
        ax1[1].set_title("Khung tín hiệu "+ str(i+1)+ " là vô thanh có tần số " + str(new_F0))
    else : 
        ax1[1].set_title("Khung tín hiệu "+ str(i+1)+ " là hữu thanh có tần số " + str(new_F0))
    ax1[1].plot(x,ttq1)
    ax1[1].plot(x[vitri],ttq1[vitri],'*') # vẽ tại điểm cực đại cục bộ
    ax1[1].set_xlabel("Index of sample")
    ax1[1].set_ylabel("Herts")
    ax1[1].axhline(y=nguong_y, color='r', linestyle='--')  
    return new_F0 # giá trị trả về là F0 tại điểm đó

def hamtutuongquan(i): 
    nL = SoMauTrenKhung*i 
    nR = SoMauTrenKhung*(i+1) 
    ttq1 = np.zeros(SoMauTrenKhung) # khởi tạo vector lưu các giá trị tự tương quan
    tinhieu = data[nL:nR] # khung tín hiệu xét từ vị trí nL -> nR
    for x in range(0,SoMauTrenKhung):
        for y in range(0,SoMauTrenKhung):
            giatri = 0
            if x+y < SoMauTrenKhung:
                giatri = tinhieu[x+y]
            ttq1[x] = ttq1[x] + tinhieu[y]*giatri
    return ttq1


F0 = np.zeros(SoKhungTinHieu+1)

for i in range(0,SoKhungTinHieu) :
    ttq1 = hamtutuongquan(i)
    maxP = nguong_y = 0.5 * ttq1[0] # ngưỡng xác định    
    P = check  = 0
    vitri = -1   
    for m in range(0,SoMauTrenKhung):
        if (ttq1[m] > nguong_y) :
            if check == 0  :
                check = 1
            else :
                if (maxP < ttq1[m] and P != 0 and 45 < m < 213):
                    maxP = ttq1[m]
                    vitri = m                
        elif (ttq1[m] < nguong_y and check == 1 ): 
            if P == 0 : 
                P = m
                check = 0
   # new_F0 = 1/(vitri*(len(data)-1)*dt/len(data))
   # vitri*i/L (i = L *dt-dt) L = somautoanfile   
    new_F0 = 0
    T0 = vitri*(len(data)-1)*dt/len(data)  
    if T0 < 1/75 and T0 > 1/350 : 
        new_F0 = 1 / T0 
    F0[i] = new_F0


for i in range(1,len(F0)-1):
    if F0[i] == 0:
        continue
    elif (F0[i+1] == 0 and F0[i-1] == 0):
        F0[i] = 0
        continue
    elif abs(F0[i+1] - F0[i]) > 20 and abs(F0[i-1] - F0[i]) > 20 : 
        F0[i] = 0

x = np.arange(len(F0))
for i in range(len(F0)):
    if (F0[i] == 0) :
        ax[1].plot(x[i],F0[i],'.',color='white')
    else : 
        ax[1].plot(x[i],F0[i],'.',color='blue')
ax[1].set_title("Dải tần số F0")
ax[1].set_ylabel("Hertz")
ax[1].set_xlabel("Index of frames")


draw(37) # 
hamcucdai(37) # khung 37 của file lab female

plt.show()
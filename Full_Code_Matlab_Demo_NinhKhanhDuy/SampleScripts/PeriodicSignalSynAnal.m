% CT nay lam 2 viec:
% - tong hop x[n] tu N tin hieu sin thuc co tan so cach deu nhau trong dai [0,2pi) va phat ra loa
% - phan tich pho cua tin hieu vua moi tong hop duoc
n = 0:16000; % vecto thoi gian roi rac
Fs = 16000;  % tan so lay mau
N = 20; % so luong TH sin (chinh la chu ky cua x[n])
s = zeros(1,length(n)); % tin hieu tong cua N TH sin
for k = 0:N-1
    A = randi(N); % sinh bien do ngau nhien
    s = s + A*cos((2*pi*k/N)*n); % w(k) = 2*pi*k/N
end
%s = s + 3*randn(1, length(s)); % them nhieu trang (white noise) vao tin hieu
% ve do thi tin hieu
subplot(3,1,1);
plot(n(1:100),s(1:100)); % chi ve 100 mau dau tien
title(['So tin hieu sin N=', num2str(N)])
sound(s,Fs); % khoi phuc TH voi ts lay mau Fs
pause(3);

% phan tich pho bien do cua tin hieu vua tong hop s[n]
% ve do thi |X(e^jw)| va |X(F)|
x = s;
N = 1024; % so diem tren truc tan so w
w = -pi:pi/N:pi;
X = freqz(x,1,w); % X(e^jw) la vecto phuc theo w
% ve do thi pho bien do |X(e^jw)| cua tin hieu
subplot(3,1,2);
plot(w,abs(X)); 
grid; 
axis([min(w), max(w), 0, max(abs(X))]);
title ('Pho bien do tin hieu tren tan so w va thang tuyen tinh');
xlabel('w(radians)');
% ve do thi pho bien do |X(F)| cua tin hieu
F = Fs * w / (2*pi); % chuyen tu t/s ly thuyet w (radian) sang t/s thuc F (Hz)
modX = abs(X)/Fs;
logXF = 20*log10(modX); % lay log10 cua |X(F)| de nen dai bien thien
subplot(3,1,3);
plot(F,logXF); 
grid; 
axis([0, Fs/2 , min(logXF), max(logXF)]);
title ('Pho bien do tin hieu tren tan so F va thang logarit');
xlabel('F(Hz)');
ylabel('Magnitude (dB)');


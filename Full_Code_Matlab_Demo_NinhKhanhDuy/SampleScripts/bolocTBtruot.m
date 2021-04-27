% a. Tim DUXDV cua bo loc trung binh truot M diem
% b. Sinh tin hieu sin s[n] lan voi nhieu trang w[n] theo x = s + w
% c. Loc tin hieu x (thu duoc y) va tim M de RMSE(s,y) la nho nhat
clc; clf;
% cau a
M = 9;              % bac cua bo loc
N = 200;           % do dai cua tin hieu
b = 1/M*ones(1,M);  % vecto he so b = [1/M, 1/M, ..., 1/M]
a = 1;              % vecto he so a = [1]
h = impz(b,a,100);   % tim h[n]
figure(1);
stem((0:length(h)-1),h,'fill');
title('h[n]');
xlabel('n');
% cau b
n = 0:N-1;              % vecto thoi gian roi rac 
s = 5*sin(2*pi*1/10*n); % s[n]
noise = randn(1,N);     % nhieu trang
x = s + noise;          % x[n]
figure(2); % ve 3 do thi s[n], w[n] & y[n]
subplot(3,1,1);
plot(s);
title('s[n]');
subplot(3,1,2);
plot(noise);
title('noise[n]');
subplot(3,1,3);
plot(x);
title('x[n]');
% cau c
v = [1 3 5 7 9];        % cac gia tri bac cua bo loc
figure(3);
for i = 1:length(v)
   M = v(i);            % bac cua bo loc
   b = 1/M*ones(1,M);   % vecto hs b thay doi theo M
   y = filter(b,a,x);   % tim y[n]
   y = [y(1+(M-1)/2:end), zeros(1,(M-1)/2)];  % tien y[n] (M-1)/2 mau de bu tre pha
   hieu = y-s;          % vector loi cua y va s
   hieu2 = hieu.*hieu;  % vector loi binh phuong
   sse = sum(hieu2);    % tong loi binh phuong
   rmse = sqrt(1/N*sse);  % RMSE(y,s)
   % ve do thi va xuat ket qua
   subplot(length(v),1,i); % do thi thu i
   plot(s); hold on; plot(y); % xep chong 2 do thi s[n] & y[n]
   legend('s[n]','y[n]');
   title('M = ' + string(M) + ', RMSE = ' + string(rmse));
   fprintf('M = %d, RMSE = %.2f\n', M, rmse);
end
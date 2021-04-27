% CT ve pho cua tin hieu bat ky cho truoc x[n].
N = 1024; % so diem tren truc tan so w
w = -pi:pi/N:pi;
n = 0:100; % vecto thoi gian roi rac

x = cos(pi/10*n); % TH sin co tan so w=pi/10
%x = [1/3, 1/3, 1/3, zeros(1,1998)];
% x = (1/2).^n; % sinh va ve do thi x[n] = (1/2)^n  %x[n] = (1/2)^n*u[n]
% x = [1, zeros(1,length(n)-1)]; % x = delta[n]
% x = randn(1, length(n)); % x[n] = white noise

clf;
figure(1);
subplot(3,1,1);
stem(n,x,'fill');
title('x[n]');

% sinh va ve do thi X(e^jw)
X = freqz(x,1,w); % nhan duoc X(e^jw) la vecto phuc theo w
modX = abs(X);
subplot(3,1,2);
plot(w,modX);grid;
axis([min(w), max(w) , 0, max(modX)+1]);
title ('Pho bien do tin hieu');
xlabel('Tan so w (radians)');
phaseX = angle(X);
subplot(3,1,3);
plot(w,phaseX);grid;
axis([min(w), max(w) , min(phaseX), max(phaseX)]);
title ('Pho pha tin hieu');
xlabel('Tan so w (radians)');
sound(x,8000);
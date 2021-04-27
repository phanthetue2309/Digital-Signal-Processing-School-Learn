% plot signal's spectrum, given its expression
w = -pi:pi/100:pi;          % vecto tan so (truc t/s)
X = 1/3*(1 + exp(-j*w) + exp(j*w));   % ham pho
Xabs = abs(X);              % pho bien do
Xphase = angle(X);          % pho pha

figure(1)
subplot(2,1,1);
plot(w,Xabs);
grid;
title('Pho bien do');

subplot(2,1,2);
plot(w,Xphase);
grid;
title('Pho pha');


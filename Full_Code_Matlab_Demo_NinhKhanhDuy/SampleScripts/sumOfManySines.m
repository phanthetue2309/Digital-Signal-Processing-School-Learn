% CT tong hop x[n] tu nhieu TH sin phuc va phat tin hieu vua moi tong hop duoc
n = -100:100; % vecto thoi gian roi rac
n0 = 20;
clf;
for i = 1:2
        N = 10.^(i+1); % so luong TH sin
        sum = 0;
        for k = 0:N-1
            A = 1; % bien do TH sin
            sum = sum + A*exp(j*((-pi + 2*pi*k/N)*(n-n0))); %w(k) = -pi + 2*pi*k/N (k=0:N-1)
        end
        s = 1/N*sum; % tin hieu TB cong cua N TH sin
        subplot(4,1,2*(i-1)+1);
        stem(n,real(s),'fill');
        title(['Phan thuc cua TH voi N=', num2str(N)])
        
        subplot(4,1,2*i);
        stem(n,imag(s),'fill');
        title(['Phan ao cua TH voi N=', num2str(N)])
        sound(real(s),8000); % khoi phuc TH voi ts lay mau 8000Hz
        pause(3);
end

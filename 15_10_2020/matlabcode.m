[y,Fs] = audioread('lab_female.wav');
info = audioinfo('lab_female.wav');
t = 0:(1/Fs):(info.Duration);
D=1/Fs;
t = t(1:end-1);

subplot(3,1,1);
plot(t,y);
title('Tin hieu Lab Female');
xlabel('Time');
ylabel('Amplitude');

% cau 3
bien_chuan = [0.7, 1.073, 1.96, 2.45, 3.434, 3.825, 4.66, 5.118, 6.075, 6.447, 7.183, 7.812];

for m=1:length(bien_chuan)
    xline(bien_chuan(m),'-.r','LineWidth',1.25);
end

E=zeros(ceil(info.Duration/0.01),1);

n=1;
for m=1:length(E)
  count=D;
  while (count<0.01 && n<length(t))
    E(m)=E(m)+(y(n)^2);    
    count=count+D;
    n=n+1;
  end
end

% t_new=0:0.01:info.Duration;
subplot(3,1,2);
% cau1,2
plot(log10(E));
title('Nang luong E');
xlabel('Index of frames');
ylabel('Amplitude');

normA=zeros(ceil(info.Duration/0.01),1);
min = log(min(E));
max = log(max(E));
for m=1:length(E)
    normA(m)=(log(E(m))-min)/(max-min);
end

subplot(3,1,3);
plot(normA);

nguong_y=0.58;
yline(nguong_y,'-.m','LineWidth',1.25);
title('Nang luong chuan hoa');
xlabel('Index of frames');
ylabel('Amplitude');
% cau4
nguong_y=0.58;
bien_tinh_toan=zeros(1,length(bien_chuan));
check=0;m=1; k=1;
while (m<length(normA))
    if(normA(m)>nguong_y && check==0) 
        xline(m,'-.r','LineWidth',1.25); 
        bien_tinh_toan(k) =m*0.01; k=k+1;
        check=1;
    end
    if(normA(m)<nguong_y && check==1) 
        a=true;
        for i=m:(m+20)
            if (normA(i)>0.6)
                a=false;
                break;
            end
        end
        if(a==true)
            xline(m,'-.r','LineWidth',1.25); 
            bien_tinh_toan(k) =m*0.01; k=k+1;
            check=0;
        end
        
    end
    m=m+1;
end

sai_so=zeros(1,length(bien_chuan));
for m=1:length(sai_so)
    sai_so(m)=abs(bien_chuan(m)-bien_tinh_toan(m));
end
    sai_so_trung_binh=sum(sai_so)/length(sai_so);

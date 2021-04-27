[y,Fs] = audioread('studio_female.wav');
info = audioinfo('studio_female.wav');

t = 0:(1/Fs):(info.Duration);
t = t(1:end-1);
%subplot(3,1,1);
%plot(t,y);

soKhung=ceil(info.Duration/0.02);
E=zeros(soKhung,1);



%chia khung tin hieu
khung=zeros(soKhung,320);
n=1;
for m=1:soKhung
   i=1;
    while (i*(1/Fs)<=0.02 && n<length(y))
        khung(m,i)=y(n);
        i=i+1;
        n=n+1;
    end
end

%ham tu tuong quan
HamTTQ=zeros(soKhung,320);
ttq=zeros(1,320);
for m=1:soKhung

    tinhieu=khung(m,:);
    ttq=zeros(1,320);
    %tinhieu=x(33281: 33600);
    
    for k=1:320   
        for i=1:320
            Rt=0;       
            if((k+i)<=320) %neu lon hon so mau thi rt=0
            Rt = tinhieu(i+k); 
            end
            ttq(k)=ttq(k)+(tinhieu(i)*Rt);
        end
    end
    
    HamTTQ(m,:)=ttq(1:320);
end
subplot(3,1,2);
plot(t,y);
%plot(khung(104,:));
subplot(3,1,3);
plot(HamTTQ(104,:));

%nguong xac dinh T0

yline(nguong_y);

%subplot(3,1,1);
mangY=[];mangX=[];
for k=1:soKhung
    nguong_y=0.3*HamTTQ(k,1);
    check=0;i=0;maxP=0;P=0;
    maxP=nguong_y;
    A=HamTTQ(k,:);m=1;vitri=0;
    while (m<320)
        if(A(m)>nguong_y)
            if(check==0) 
            %xline(m,'-.r','LineWidth',1.25); %bien tam thoi
            check=1;
            else
                if(maxP<A(m) && m>1 && P~=0)
                    maxP=A(m);vitri=m;
                end
            end
        end
        if(A(m)<nguong_y && check==1)         
            if (P==0)
                P=m;
            end
                %xline(m,'-.r','LineWidth',1.25); 
                check=0;        
        end
        m=m+1;   
    end
 %   F0=(1/(vitri*0.02/320));
    F0 = 1/(vitri/320*0.02);
    if (F0 > 350 || F0 < 75 )
        F0 = 0;
    end
    mangY=[mangY,F0];
    mangX=[mangX,vitri];

end
subplot(311);
X = 1:length(mangY);
plot(X,mangY,'*');


%CucDai=0;
%for m=1:length(Index)
    %if (arrPeaks(m)>CucDai&&m~=1)
        %CucDai=arrPeaks(m);
        %ViTri=Index(m);
    %end
%end

%subplot(3,1,1);
%plot(ViTri,CucDai,'*');




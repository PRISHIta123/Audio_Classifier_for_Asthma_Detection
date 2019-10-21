
[y,fs]=audioread("106_2b1_Pl_mc_LittC2SE.wav");
left=y(:,1);
%spectrogram(y,256,250,256,1E3,15,'yaxis');

T=1/fs; 
L=1000; 
t=(0:L-1)*T; 
NFFT =1024; 
M = round(0.02*fs);
w = 0.54 - 0.46 * cos(2*pi*[0:M-1]/(M-1));
spectrogram(y,w,100,1024,1E3,'yaxis')
axis([0 15 0 30])
xlabel('Time')

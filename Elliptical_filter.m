ws = [0.3*pi 0.75*pi] %Stopband edge frequency
wp = [0.4*pi 0.6*pi] %Passband edge frequency
Rp = 0.5; %Passband ripple in dB
As = 20; %Stopband attenuation in dB
[N,wn] = ellipord(wp/pi,ws/pi,Rp,As);
[b,a] = ellip(N,Rp,As,wn);
[db,mag,pha,grd,w] = freqz_m(b,a);
plot(w*8000/2/pi,db);
axis([500 3500 -22 1]);
xlabel('frequency (Hz)'); ylabel('decibels'); title('Magnitude
Response of Elliptic Filter');

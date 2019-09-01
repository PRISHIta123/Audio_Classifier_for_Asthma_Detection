% Highpass Chebyshev Digital Filter
ws = 0.125*2*pi; % digital stopband frequency in rad/s
wp = 0.1375*2*pi; % digital passband frequency in rad/s
Rp = 0.5; % passband ripple in dB
As = 20;
[N,wn] = cheb1ord(wp/pi,ws/pi,Rp,As);
[b,a] = cheby1(N, Rp, wn, 'high');
[db,mag,pha,grd,w] = freqz_m(b,a);
plot(w*8000/2/pi,db);
axis([800 1200 -22 1]);

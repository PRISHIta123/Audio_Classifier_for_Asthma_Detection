Fs = 44100;                                             % Sampling Frequency (Change If Different)
Fn = Fs/2;                                              % Nyquist Frequency
Wp = [150  5800]/Fn;                                    % Normalised Passband
Ws = [ 50  6100]/Fn;                                    % Normalised Stopband
Rp =  1;                                                % Passband Ripple (dB)
Rs = 30;                                                % Stopband Ripple (dB)
[n,Ws] = cheb2ord(Wp,Ws,Rp,Rs);                         % Chebyshev Type II Order
[b,a] = cheby2(n,Rs,Ws);                                % IIR Filter Coefficients
[SOS,G] = tf2sos(b,a);                                  % Convert To Second-Order-Section For Stability
figure(1)
freqz(SOS, 4096, Fs)                                    % Check Filter Performance
filt_sig = filtfilt(SOS,G, Your_Signal);

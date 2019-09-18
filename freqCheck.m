[audioIn,fs] = audioread('F:\Respiratory_Sound_Database\Respiratory_Sound_Database\audio_and_txt_files\107_2b5_Ar_mc_AKGC417L.wav');
fs
spectrum=pwelch(audioIn); %pitch function not working in Matlab 2017
%sampling frequency for training audio file is 44100 Hz
N= length(audioIn);
slength=N/fs;
t=linspace(0,N/fs,N);
plot(t,audioIn);

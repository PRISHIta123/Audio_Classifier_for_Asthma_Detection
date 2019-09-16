[audioIn,fs] = audioread('G:\respiratory-sound-database\Respiratory_Sound_Database\Respiratory_Sound_Database\audio_and_txt_files\107_2b5_Ar_mc_AKGC417L.wav');
fs
spectrum=pwelch(audioIn); %pitch function not working in Matlab 2017
plot(10*log10(spectrum))
drawnow;
sound(audioIn,fs);
%highest recorded frequency for test audio file is 44100 Hz

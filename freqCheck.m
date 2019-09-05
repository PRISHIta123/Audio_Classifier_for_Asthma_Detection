function freqCheck()
  [audioIn,fs] = audioread('Name of File saved in Desktop/Folder');
  [f0,idx] = pitch(audioIn,fs);
  figure
  plot(idx,f0)
  ylabel('Pitch (Hz)')
  xlabel('Sample Number')
  a=max(f0);
  b=min(f0);
  disp(a);disp(b)

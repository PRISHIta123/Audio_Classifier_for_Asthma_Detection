import chebyshev_and_elliptic_filters
import wave
import numpy as np
import pandas as pd

fs=44100
order=20
cutoff=0.25*fs
chebylowf=chebyshev_and_elliptic_filters.IIR2Filter(self,order,cutoff,'lowpass','cheby2',1,1,fs)
chebyhighf=chebyshev_and_elliptic_filters.IIR2Filter(self,order,cutoff,'highpass','cheby2',1,1,fs)
ellipf=chebyshev_and_elliptic_filters.IIR2Filter(self,order,cutoff,'lowpass','elliptic',1,1,fs)

audio_filepaths=pd.read_csv("F://audio_paths.csv",header=None)

ar=audio_filepaths.values
paths=ar[0,:]

for x in paths:
  file=wave.read(x,'r')
  
  
  

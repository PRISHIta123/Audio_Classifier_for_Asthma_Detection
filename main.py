import chebyshev_and_elliptic_filters as cef
import wavio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fs=44100
order=20
cutoff=[11025]#0.25*fs
chebylowf=cef.IIR2Filter(order,cutoff,'lowpass','cheby2',1,1,fs)
chebyhighf=cef.IIR2Filter(order,cutoff,'highpass','cheby2',1,1,fs)
ellipf=cef.IIR2Filter(order,cutoff,'lowpass','elliptic',1,1,fs)

audio_filepaths=pd.read_csv("F://audio_paths.csv",header=None)

#Read audio files from csv
ar=audio_filepaths.values
paths=ar[0,:]

for x in paths:
  file=wavio.read(x)
  impulse=file.data
  impulseRespcl=np.zeros(len(impulse))# Stores chebyshev low pass filter impulse responses
  impulseRespch=np.zeros(len(impulse))# Stores chebyshev high pass filter impulse responses
  impulseRespel=np.zeros(len(impulse))# Stores elliptic low pass filter impulse responses
  
  #Calculate impulse responses
  for i in range(len(impulse)):
	  impulseRespcl[i]=chebylowf.filter(impulse[i])
    impulseRespch[i]=chebyhighf.filter(impulse[i])
    impulseRespel[i]=ellipf.filter(impulse[i])
  
  #Cheby Low Pass Plot
  chebylfr=np.fft.fft(impulseRespcl)
  chebylfr = abs(chebylfr[0:int(len(chebylfr)/2)])
  FT1 = np.linspace(0,fs/2,len(chebylfr))# Fourier Transform of Frequency Response
  
  plt.figure("Frequency Response")
  plt.plot(FT1,np.real(chebylfr))
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Amplitude")
  plt.title("Chebyshev Low Pass")
  plt.show()
  
  #Cheby High Pass Plot
  chebyhfr=np.fft.fft(impulseRespch)
  chebyhfr = abs(chebyhfr[0:int(len(chebyhfr)/2)])
  FT2 = np.linspace(0,fs/2,len(chebyhfr))# Fourier Transform of Frequency Response
  
  plt.figure("Frequency Response")
  plt.plot(FT2,np.real(chebyhfr))
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Amplitude")
  plt.title("Chebyshev High Pass")
  plt.show()
  
  #Elliptic Low Pass Plot
  ellipfr=np.fft.fft(impulseRespel)
  ellipfr = abs(ellipfr[0:int(len(ellipfr)/2)])
  FT3 = np.linspace(0,fs/2,len(ellipfr))# Fourier Transform of Frequency Response
  
  plt.figure("Frequency Response")
  plt.plot(FT3,np.real(ellipfr))
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Amplitude")
  plt.title("Elliptic Low Pass")
  plt.show()
  
  break
  
  
  
  
  

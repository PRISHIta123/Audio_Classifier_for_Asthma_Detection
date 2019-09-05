import chebyshev_and_elliptic_filters
from mlabwrap import mlab

mlab.path(mlab.path(),path_to_directory)
fs=mlab.freqcheck()
chebylowf=chebyshev_and_elliptic_filters.IIR2Filter(self,order,cutoff,'lowpass','cheby2',1,1,fs)
chebyhighf=chebyshev_and_elliptic_filters.IIR2Filter(self,order,cutoff,'highpass','cheby2',1,1,fs)
ellipf=chebyshev_and_elliptic_filters.IIR2Filter(self,order,cutoff,'lowpass','elliptic',1,1,fs)


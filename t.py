# 波形图
# wave=thinkdsp.read_wave("D:\CloudMusic\ss/000000.wav")
# wave.plot()
# plt.savefig('D:\CloudMusic\ss/test1')
# plt.show()
# 频谱
import thinkdsp
from 频谱 import thinkplot

wave= thinkdsp.read_wave("D:\CloudMusic\ss/000000.wav")
spectrum=wave.make_spectrum()
spectrum.plot()
thinkplot.show()

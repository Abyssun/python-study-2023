import matplotlib.pyplot as plt
fig = plt.figure()   # 生成画布
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.set(xlim=[0.5,4.5],ylim=[-2,8],title='An Example Axes1',ylabel='Y-Axis',xlabel='X-Axis')
ax2.set(xlim=[0.5,4.5],ylim=[-2,8],title='An Example Axes2',ylabel='Y-Axis',xlabel='X-Axis')
ax3.set(xlim=[0.5,4.5],ylim=[-2,8],title='An Example Axes3',ylabel='Y-Axis',xlabel='X-Axis')
ax4.set(xlim=[0.5,4.5],ylim=[-2,8],title='An Example Axes4',ylabel='Y-Axis',xlabel='X-Axis')
plt.show()
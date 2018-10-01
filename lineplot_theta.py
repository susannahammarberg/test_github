import h5py
import numpy as np
import matplotlib.pyplot as plt

#scan_number = range(191458,191486+1)
#scan_number = range(192613,192643+1)
scan_number = range(192861,192891+1)

'''
file_in = '/dls/i13-1/data/2018/mt20167-1/raw/merlin-' + str(scan_number) + '.hdf'
key = 'entry/data/data'
'''

rock_curve = []
#theta = []
for ii in scan_number:
	file_in = '/dls/i13-1/data/2018/mt20167-1/raw/' + str(ii) + '.nxs'
	key_data = 'entry1/instrument/excalibur/data'
	key_theta = 'entry1/instrument/t1_theta/t1_theta'

	with h5py.File(file_in) as f:
		dat = f[key_data][:, 750:1000,950:1100]
		#theta_temp = f[key_theta]
		#print theta_temp
		print ii

	line = dat.sum()
	rock_curve.append(line)
	# theta not saved in nexus
#	theta.append(theta_temp)


kk=np.arange(len(scan_number))
plt.figure()
plt.plot(kk,(rock_curve))
plt.title('Rocking curve ' + str(scan_number[0]) + ' to ' + str(scan_number[-1]) )
plt.show()


#module load python/ana

import h5py
import numpy as np
import matplotlib.pyplot as plt
import sys

scan_number = sys.argv[1]
motor_name = sys.argv[2]
detector_name = sys.argv[3]


file_motor = '/dls/i13-1/data/2018/mt17325-1/raw/' + str(scan_number) + '.nxs'
if detector_name == 'merlin':
    file_data = '/dls/i13-1/data/2018/mt17325-1/raw/' + str(scan_number) + '.nxs'
    key_data = 'entry1/instrument/merlin_sw_hdf/data'
elif detector_name == 'excalibur':
    file_data = '/dls/i13-1/data/2018/mt17325-1/raw/excalibur-vds-' + str(scan_number) + '.hdf'
    key_data = 'entry/instrument/detector/data'

if motor_name == 'theta':
    key_motor = 'entry1/instrument/t1_theta/t1_theta'
elif motor_name == 'sample_lab_y':
    key_motor = 'entry1/instrument/sample_lab_y/sample_lab_y'
elif motor_name == 'sample_lab_x':
    key_motor = 'entry1/instrument/sample_lab_x/sample_lab_x'


f_data = h5py.File(file_data)
dat = f_data[key_data]

if motor_name == 'repscan':
    motor = np.arange(np.size(dat,0))
else:
    f_motor = h5py.File(file_motor)
    motor = f_motor[key_motor]

print np.shape(dat)
line = np.sum(np.sum(dat[:,600:1100,1500:1800],1),1)
#line = np.sum(np.sum(dat,1),1)

max_pos = np.argmax(line)
max_val = line[max_pos]
max_motor = motor[max_pos]
print 'Maximum point =', max_val, 'at', max_motor

plt.figure()
plt.title('Scan: ' + str(scan_number) + ' (maximum at ' + str(max_motor) + ')')
plt.xlabel(motor_name)
plt.ylabel(detector_name)
plt.plot(motor,line)
plt.yscale('log')
plt.show()

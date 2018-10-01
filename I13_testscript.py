# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:23:20 2018

@author: Sanna

Copy from ptypy3d.py


3d reconstructions using ptypy.



"""
import ptypy
from ptypy.core import Ptycho
from ptypy import utils as u
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from ptypy.experiment.nanomax3d import NanomaxBraggJune2017 # after update need to update spec ptyScan class
from ptypy.experiment.I13_Bragg3d import I13Bragg3d # after update need to update spec ptyScan class

p = u.Param()
p.run = 'I13Bragg3d'  

# nice thursday night ptycho: 191526 - 191587

# 0 voltage friday night scan 191767-191827
sample = 'name'; scans = range(191767, 191768+1) #range(191767, 191827)
#sample = 'JWX29A_NW1' #; scans =[458,459]

p.data_type = "single"   #or "double"
# for verbose output
#p.verbose_level = 5

# use special plot layout for 3d data  (but the io.home part tells ptypy where to save recons and dumps)
p.io = u.Param()
p.io.home = './'
p.io.autosave = u.Param()
p.io.autosave.interval = 1 # does not work
p.io.autoplot = u.Param()
p.io.autoplot.layout = 'bragg3d'
p.io.autoplot.dump = True
p.io.autoplot.interval = 1
 
p.scans = u.Param()
p.scans.scan01 = u.Param()
p.scans.scan01.name = 'Bragg3dModel'
#p.scans.scan01.illumination = illumination
p.scans.scan01.data= u.Param()
p.scans.scan01.data.name = 'I13Bragg3d'


p.scans.scan01.data.datapath = '/dls/i13-1/data/2018/mt20167-1/raw/'
#[750,950,950,1150]
p.scans.scan01.data.detector_roi_indices = [450,950,550,1150]
p.scans.scan01.data.scans = scans
p.scans.scan01.data.center = None
p.scans.scan01.data.theta_bragg = 11.0
p.scans.scan01.data.rocking_step = .02
p.scans.scan01.data.shape = 500

#512#150#60#290#128
# ptypy says: Setting center for ROI from None to [ 75.60081158  86.26238307].   bu that must be in the images that iI cut out from the detector
#p.scans.scan01.data.center = (200,270) #(512-170,245)     #(512-170,245) for 192_   #Seems like its y than x
#p.scans.scan01.data.load_parallel = 'all'
#p.scans.scan01.data.psize = 55e-6

p.scans.scan01.data.energy = 9.7
p.scans.scan01.data.distance = 3.5


p.scans.scan01.illumination = u.Param()
p.scans.scan01.illumination.aperture = u.Param() 
p.scans.scan01.illumination.aperture.form = 'circ'
p.scans.scan01.illumination.aperture.size = 100e-9 
p.scans.scan01.sample = u.Param()
p.scans.scan01.sample.fill = 1e-3

# to use a probe from an old reconstruction:
#p.scans.scan01.illumination.model = 'recon'
#p.scans.scan01.illumination.recon = u.Param()

p.engines = u.Param()
p.engines.engine00 = u.Param()
p.engines.engine00.name = 'DM'    #Not 'DM_3dBragg' ? 
p.engines.engine00.numiter = 2
p.engines.engine00.probe_update_start = 100000
p.engines.engine00.probe_support = None

# prepare and run
P = Ptycho(p,level=2)

shape = p.scans.scan01.data.shape
dd= P.diff.storages.values()[0].data * P.mask.storages.values()[0].data[0][0]

dd[:,:,76,74] = 0 

plt.figure()
plt.imshow(sum(sum(dd)))
plt.show()

from xrd import XRD_fun

XRD_fun(P,scans,shape)

for k, v in P.obj.S.items():
    print k, v
    
for l, m in P.model.scans.items():
    print l, m
    
for o,n in P.diff.S.items():
    print o, n
    
    
for o,n in P.exit.S.items():
    print o, n
    
P.model.scans['scan01'].ptyscan.info

########## INFO ##########
# Averages the data to show the trends better

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import glio
s = glio.GadgetSnapshot('snapshot_010')						### Change snapshot here ###
s.load()


#################### POSITION ####################
########## Produces data for the x, y, and z position values for the disk ##########
f = open('data_disk_xyz', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s %s\n" % (s.pos[2][i][0], s.pos[2][i][1], s.pos[2][i][2]))

f.close()


########## Produces data for the mass of the gas particles ##########
f = open('data_disk_mass', 'w')
for i in range(0, len(s.mass[2][:])):
	f.write("%s\n" % s.mass[2][i])

f.close()


########## Sets up the  x, y, and z postion arrays ##########
f2 = open('data_disk_xyz')
lines = f2.readlines()

f2.close()

disk_x = []
disk_y = []
disk_z = []

for line in lines:
	p = line.split()
	disk_x.append(float(p[0]))
	disk_y.append(float(p[1]))
	disk_z.append(float(p[2]))

disk_px = np.array(disk_x)
disk_py = np.array(disk_y)
disk_pz = np.array(disk_z)

disk_xm = np.array(disk_x)
disk_ym = np.array(disk_y)
disk_zm = np.array(disk_z)


########## Sets up the mass array ##########
f2 = open('data_disk_mass')
lines = f2.readlines()
f2.close()

disk_mass = []

for line in lines:
	p = line.split()
	disk_mass.append(float(p[0]))

disk_m = np.array(disk_mass)


########## Find the center of mass in all directions ##########
disk_xm[:] = [x * (8.76209*(10**-6)) for x in disk_xm]
disk_xm_sum = sum(disk_xm)

disk_ym[:] = [y * (8.76209*(10**-6)) for y in disk_ym]
disk_ym_sum = sum(disk_ym)

disk_zm[:] = [z * (8.76209*(10**-6)) for z in disk_zm]
disk_zm_sum = sum(disk_zm)

disk_mass_sum = sum(disk_m)

com_x = disk_xm_sum / disk_mass_sum
#print com_x

com_y = disk_ym_sum / disk_mass_sum
#print com_y

com_z = disk_zm_sum / disk_mass_sum
#print com_z


########## Centers the values by subtracting the center of mass ##########
disk_centered_x = np.array(disk_x)
disk_centered_y = np.array(disk_y)
disk_centered_z = np.array(disk_z)

disk_centered_x[:] = [x - com_x for x in disk_centered_x]
a = disk_centered_x[0::6]
disk_centered_y[:] = [y - com_y for y in disk_centered_y]
b = disk_centered_y[0::6]
disk_centered_z[:] = [z - com_z for z in disk_centered_z]


#################### VELOCITY ####################
########## Produces data for the vx, vy, and vz velocity values for the disk ##########
f = open('data_disk_vxyz', 'w')
for i in range(0, len(s.vel[2][:])):
	f.write("%s %s %s\n" % (s.vel[2][i][0], s.vel[2][i][1], s.vel[2][i][2]))

f.close()


########## Produces data for the mass of the disk particles ##########
f = open('data_disk_mass', 'w')
for i in range(0, len(s.mass[2][:])):
	f.write("%s\n" % s.mass[2][i])

f.close()


########## Sets up the  vx, vy, and vz velocity arrays ##########
f2 = open('data_disk_vxyz')
lines = f2.readlines()

f2.close()

disk_vx = []
disk_vy = []
disk_vz = []

for line in lines:
	p = line.split()
	disk_vx.append(float(p[0]))
	disk_vy.append(float(p[1]))
	disk_vz.append(float(p[2]))

disk_pvx = np.array(disk_vx)
disk_pvy = np.array(disk_vy)
disk_pvz = np.array(disk_vz)

disk_vxm = np.array(disk_vx)
disk_vym = np.array(disk_vy)
disk_vzm = np.array(disk_vz)


########## Find the momentum in all directions ##########
disk_vxm[:] = [vx * (8.76209*(10**-6)) for vx in disk_vxm]
disk_vxm_sum = sum(disk_vxm)

disk_vym[:] = [vy * (8.76209*(10**-6)) for vy in disk_vym]
disk_vym_sum = sum(disk_vym)

disk_vzm[:] = [vz * (8.76209*(10**-6)) for vz in disk_vzm]
disk_vzm_sum = sum(disk_vzm)

disk_mass_sum = sum(disk_m)

mom_vx = disk_vxm_sum / disk_mass_sum
#print mom_vx

mom_vy = disk_vym_sum / disk_mass_sum
#print mom_vy

mom_vz = disk_vzm_sum / disk_mass_sum
#print mom_vz


########## Centers the values by subtracting the momentum ##########
disk_centered_vx = np.array(disk_vx)
disk_centered_vy = np.array(disk_vy)
disk_centered_vz = np.array(disk_vz)

disk_centered_vx[:] = [vx - mom_vx for vx in disk_centered_vx]
disk_centered_vy[:] = [vy - mom_vy for vy in disk_centered_vy]
disk_centered_vz[:] = [vz - mom_vz for vz in disk_centered_vz]


########## Makes the transformations to cylindrical coordinates ##########
r_disk = np.sqrt(disk_centered_x**2 + disk_centered_y**2)
theta_disk = np.arctan2(disk_centered_y, disk_centered_x)
	
vr_disk = disk_centered_vx*np.cos(theta_disk) + disk_centered_vy*np.sin(theta_disk)
vtheta_disk = disk_centered_vy*np.cos(theta_disk) - disk_centered_vx*np.sin(theta_disk)


disk_centered_vr = np.array(vr_disk)
disk_centered_vtheta = np.array(vtheta_disk)


########## For loop that takes a slice of the data ##########
x_slice = []
y_slice = []
vr_slice = []
vtheta_slice = []
vz_slice = []

for i in range(len(disk_centered_y)):
	if 1.0 >= disk_centered_y[i] >= 0.0:
		x_slice.append(disk_centered_x[i])
		y_slice.append(disk_centered_y[i])
		vr_slice.append(disk_centered_vr[i])
		vtheta_slice.append(disk_centered_vtheta[i])
		vz_slice.append(disk_centered_vz[i])


########## Plots ##########
plt.subplot(411)
plt.plot(x_slice, vz_slice, '.', markersize=3, alpha=0.3)
plt.title('Disk Density and Velocity Slices', fontsize=30)
plt.ylabel('vz (km/sec)', fontsize=28)
plt.yticks(fontsize=15)
plt.text(25, 200, 't = 35', fontsize=25)										### Make sure to change time label ###
plt.axis([-30, 30, -300, 300])
plt.tick_params(axis='x', labelbottom='off')
plt.grid()

plt.subplot(412)
plt.plot(x_slice, vtheta_slice, '.', markersize=3, alpha=0.3)
plt.ylabel('vtheta (km/sec)', fontsize=28)
plt.yticks(fontsize=15)
plt.axis([-30, 30, -300, 300])
plt.tick_params(axis='x', labelbottom='off')
plt.grid()

plt.subplot(413)
plt.plot(x_slice, vr_slice, '.', markersize=3, alpha=0.3)
plt.ylabel('vr (km/sec)', fontsize=28)
plt.yticks(fontsize=15)
plt.axis([-30, 30, -300, 300])
plt.tick_params(axis='x', labelbottom='off')
plt.grid()

plt.subplot(414)
plt.plot(x_slice, y_slice, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=28)
plt.ylabel('y (kpc)', fontsize=28)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.axis([-30, 30, -5, 5])
plt.grid()

plt.subplots_adjust(hspace=0.1)
plt.show()

########## Binned and averaged velocity plots and density histogram ##########

########## Creates arrays to be plotted ##########
wn_vz, bins, patches = plt.hist(x_slice, bins=300, weights=vz_slice)
n_vz, bins, patches = plt.hist(x_slice, bins=300)
bins_mean_vz = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(wn_vz))])
averages_vz = wn_vz / n_vz
mask_vz = np.logical_not( np.isnan(averages_vz))

wn_vtheta, bins, patches = plt.hist(x_slice, bins=300, weights=vtheta_slice)
n_vtheta, bins, patches = plt.hist(x_slice, bins=300)
bins_mean_vtheta = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(wn_vtheta))])
averages_vtheta = wn_vtheta / n_vtheta
mask_vtheta = np.logical_not( np.isnan(averages_vtheta))

wn_vr, bins, patches = plt.hist(x_slice, bins=300, weights=vr_slice)
n_vr, bins, patches = plt.hist(x_slice, bins=300)
bins_mean_vr = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(wn_vr))])
averages_vr = wn_vr / n_vr
mask_vr = np.logical_not( np.isnan(averages_vr))


########## Plots ##########
plt.subplot(411)
plt.plot(bins_mean_vz[mask_vz], averages_vz[mask_vz], linewidth=3)
plt.title('Disk Averaged Density and Velocity Slices', fontsize=30)
plt.ylabel('vz (km/sec)', fontsize=28)
plt.yticks(fontsize=22)
plt.text(25, 15, 't = 10', fontsize=25)										### Make sure to change time label ###
plt.axis([-30, 30, -25, 25])
plt.tick_params(axis='x', labelbottom='off')
plt.grid()

plt.subplot(412)
plt.plot(bins_mean_vtheta[mask_vtheta], averages_vtheta[mask_vtheta], linewidth=3)
plt.ylabel('vtheta (km/sec)', fontsize=28)
plt.yticks(fontsize=22)
plt.axis([-30, 30, 0, 250])
plt.tick_params(axis='x', labelbottom='off')
plt.grid()

plt.subplot(413)
plt.plot(bins_mean_vr[mask_vr], averages_vr[mask_vr], linewidth=3)
plt.ylabel('vr (km/sec)', fontsize=28)
plt.yticks(fontsize=22)
plt.axis([-30, 30, -50, 50])
plt.tick_params(axis='x', labelbottom='off')
plt.grid()

plt.subplot(414)
plt.hist(x_slice, bins=300, weights=y_slice)
plt.xlabel('x (kpc)', fontsize=28)
plt.ylabel('Number of Particles', fontsize=28)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.axis([-30, 30, 0, 600])			### Need to change 1200 to 2000 for t=35 ###
plt.grid()

plt.subplots_adjust(hspace=0.15)
plt.show()




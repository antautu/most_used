import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import glio
s = glio.GadgetSnapshot('snapshot_013')						### Change snapshot here ###
s.load()

#################### POSITION ####################
########## Produces data for the x, y, and z position values for the disk ##########
f = open('data_disk_xyz', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s %s\n" % (s.pos[2][i][0], s.pos[2][i][1], s.pos[2][i][2]))

f.close()


########## Produces data for the mass of the disk particles ##########
f = open('data_disk_mass', 'w')
for i in range(0, len(s.mass[2][:])):
	f.write("%s\n" % s.mass[2][i])

f.close()


########## Sets up the  x, y, and z postion arrays for the disk ##########
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
disk_centered_y[:] = [y - com_y for y in disk_centered_y]
disk_centered_z[:] = [z - com_z for z in disk_centered_z]


########## Produces data for the x, y, and z position values for the stars ##########
f = open('data_star_xyz', 'w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s %s\n" % (s.pos[4][i][0], s.pos[4][i][1], s.pos[4][i][2]))

f.close()


########## Produces data for the mass of the star particles ##########
f = open('data_star_mass', 'w')
for i in range(0, len(s.mass[4][:])):
	f.write("%s\n" % s.mass[4][i])

f.close()


########## Sets up the  x, y, and z postion arrays for the stars ##########
f2 = open('data_star_xyz')
lines = f2.readlines()

f2.close()

star_x = []
star_y = []
star_z = []

for line in lines:
	p = line.split()
	star_x.append(float(p[0]))
	star_y.append(float(p[1]))
	star_z.append(float(p[2]))

star_xm = np.array(star_x)
star_ym = np.array(star_y)
star_zm = np.array(star_z)


########## Centers the values by subtracting the center of mass ##########
star_centered_x = np.array(star_x)
star_centered_y = np.array(star_y)
star_centered_z = np.array(star_z)

star_centered_x[:] = [x - com_x for x in star_centered_x]
a = star_centered_x[0::6]
star_centered_y[:] = [y - com_y for y in star_centered_y]
b = star_centered_y[0::6]
star_centered_z[:] = [z - com_z for z in star_centered_z]


#################### VELOCITY ####################
########## Produces data for the vx, vy, and vz velocity values for the disk ##########
f = open('data_disk_vxyz', 'w')
for i in range(0, len(s.vel[2][:])):
	f.write("%s %s %s\n" % (s.vel[2][i][0], s.vel[2][i][1], s.vel[2][i][2]))

f.close()


########## Sets up the  vx, vy, and vz velocity arrays for the disk ##########
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


########## Produces data for the vx, vy, and vz velocity values for the stars ##########
f = open('data_star_vxyz', 'w')
for i in range(0, len(s.vel[4][:])):
	f.write("%s %s %s\n" % (s.vel[4][i][0], s.vel[4][i][1], s.vel[4][i][2]))

f.close()


########## Sets up the  vx, vy, and vz velocity arrays for the stars ##########
f2 = open('data_star_vxyz')
lines = f2.readlines()

f2.close()

star_vx = []
star_vy = []
star_vz = []

for line in lines:
	p = line.split()
	star_vx.append(float(p[0]))
	star_vy.append(float(p[1]))
	star_vz.append(float(p[2]))

star_pvx = np.array(star_vx)
star_pvy = np.array(star_vy)
star_pvz = np.array(star_vz)

star_vxm = np.array(star_vx)
star_vym = np.array(star_vy)
star_vzm = np.array(star_vz)


########## Centers the values by subtracting the momentum ##########
star_centered_vx = np.array(star_vx)
star_centered_vy = np.array(star_vy)
star_centered_vz = np.array(star_vz)

star_centered_vx[:] = [vx - mom_vx for vx in star_centered_vx]
star_centered_vy[:] = [vy - mom_vy for vy in star_centered_vy]
star_centered_vz[:] = [vz - mom_vz for vz in star_centered_vz]


########## Makes the transformations to cylindrical coordinates ##########
r_star = np.sqrt(star_centered_x**2 + star_centered_y**2)
theta_star = np.arctan2(star_centered_y, star_centered_x)
	
vr_star = star_centered_vx*np.cos(theta_star) + star_centered_vy*np.sin(theta_star)
vtheta_star = star_centered_vy*np.cos(theta_star) - star_centered_vx*np.sin(theta_star)


star_centered_vr = np.array(vr_star)
star_centered_vtheta = np.array(vtheta_star)


########## Plots the Vz bar graphs ##########
plt.subplot(121)
plt.hexbin(star_centered_x, star_centered_y, C=star_centered_vz, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 13', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(star_centered_x, star_centered_y, C=star_centered_vz, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 13', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vz (km/sec)', fontsize=18)

plt.show()


########## Plots the Vr bar graphs ##########
plt.subplot(121)
plt.hexbin(star_centered_x, star_centered_y, C=star_centered_vr, cmap=cm.Set1, gridsize=300, vmin=-80, vmax=80)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 13', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(star_centered_x, star_centered_y, C=star_centered_vr, cmap=cm.Set1, gridsize=300, vmin=-80, vmax=80)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 13', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vr (km/sec)', fontsize=18)

plt.show()


########## Plots the Vtheta bar graphs ##########
plt.subplot(121)
plt.hexbin(star_centered_x, star_centered_y, C=star_centered_vtheta, cmap=cm.jet_r, gridsize=300, vmin=180, vmax=240)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 13', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(star_centered_x, star_centered_y, C=star_centered_vtheta, cmap=cm.jet_r, gridsize=300, vmin=180, vmax=240)
plt.plot(a, b, '.', color='blueviolet', markersize=3, alpha=0.5)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 13', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vtheta (km/sec)', fontsize=18)

plt.show()


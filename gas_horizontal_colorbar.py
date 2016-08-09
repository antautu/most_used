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
print com_x

com_y = disk_ym_sum / disk_mass_sum
print com_y

com_z = disk_zm_sum / disk_mass_sum
print com_z


########## Centers the values by subtracting the center of mass ##########
disk_centered_x = np.array(disk_x)
disk_centered_y = np.array(disk_y)
disk_centered_z = np.array(disk_z)

disk_centered_x[:] = [x - com_x for x in disk_centered_x]
disk_centered_y[:] = [y - com_y for y in disk_centered_y]
disk_centered_z[:] = [z - com_z for z in disk_centered_z]


########## Produces data for the x, y, and z position values for the gas ##########
f = open('data_gas_xyz', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s %s\n" % (s.pos[0][i][0], s.pos[0][i][1], s.pos[0][i][2]))

f.close()


########## Produces data for the mass of the gas particles ##########
f = open('data_gas_mass', 'w')
for i in range(0, len(s.mass[0][:])):
	f.write("%s\n" % s.mass[0][i])

f.close()


########## Sets up the  x, y, and z postion arrays for the gas ##########
f2 = open('data_gas_xyz')
lines = f2.readlines()

f2.close()

gas_x = []
gas_y = []
gas_z = []

for line in lines:
	p = line.split()
	gas_x.append(float(p[0]))
	gas_y.append(float(p[1]))
	gas_z.append(float(p[2]))

gas_xm = np.array(gas_x)
gas_ym = np.array(gas_y)
gas_zm = np.array(gas_z)


########## Centers the values by subtracting the center of mass ##########
gas_centered_x = np.array(gas_x)
gas_centered_y = np.array(gas_y)
gas_centered_z = np.array(gas_z)

gas_centered_x[:] = [x - com_x for x in gas_centered_x]
a = gas_centered_x[0::6]
gas_centered_y[:] = [y - com_y for y in gas_centered_y]
b = gas_centered_y[0::6]
gas_centered_z[:] = [z - com_z for z in gas_centered_z]


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
print mom_vx

mom_vy = disk_vym_sum / disk_mass_sum
print mom_vy

mom_vz = disk_vzm_sum / disk_mass_sum
print mom_vz


########## Centers the values by subtracting the momentum ##########
disk_centered_vx = np.array(disk_vx)
disk_centered_vy = np.array(disk_vy)
disk_centered_vz = np.array(disk_vz)

disk_centered_vx[:] = [vx - mom_vx for vx in disk_centered_vx]
disk_centered_vy[:] = [vy - mom_vy for vy in disk_centered_vy]
disk_centered_vz[:] = [vz - mom_vz for vz in disk_centered_vz]


########## Produces data for the vx, vy, and vz velocity values for the gas ##########
f = open('data_gas_vxyz', 'w')
for i in range(0, len(s.vel[0][:])):
	f.write("%s %s %s\n" % (s.vel[0][i][0], s.vel[0][i][1], s.vel[0][i][2]))

f.close()


########## Sets up the  vx, vy, and vz velocity arrays for the gas ##########
f2 = open('data_gas_vxyz')
lines = f2.readlines()

f2.close()

gas_vx = []
gas_vy = []
gas_vz = []

for line in lines:
	p = line.split()
	gas_vx.append(float(p[0]))
	gas_vy.append(float(p[1]))
	gas_vz.append(float(p[2]))

gas_pvx = np.array(gas_vx)
gas_pvy = np.array(gas_vy)
gas_pvz = np.array(gas_vz)

gas_vxm = np.array(gas_vx)
gas_vym = np.array(gas_vy)
gas_vzm = np.array(gas_vz)


########## Centers the values by subtracting the momentum ##########
gas_centered_vx = np.array(gas_vx)
gas_centered_vy = np.array(gas_vy)
gas_centered_vz = np.array(gas_vz)

gas_centered_vx[:] = [vx - mom_vx for vx in gas_centered_vx]
gas_centered_vy[:] = [vy - mom_vy for vy in gas_centered_vy]
gas_centered_vz[:] = [vz - mom_vz for vz in gas_centered_vz]


########## Makes the transformations to cylindrical coordinates ##########
r_gas = np.sqrt(gas_centered_x**2 + gas_centered_y**2)
theta_gas = np.arctan2(gas_centered_y, gas_centered_x)
	
vr_gas = gas_centered_vx*np.cos(theta_gas) + gas_centered_vy*np.sin(theta_gas)
vtheta_gas = gas_centered_vy*np.cos(theta_gas) - gas_centered_vx*np.sin(theta_gas)


gas_centered_vr = np.array(vr_gas)
gas_centered_vtheta = np.array(vtheta_gas)


########## Plots the Vz bar graphs ##########
plt.subplot(121)
plt.hexbin(gas_centered_x, gas_centered_y, C=gas_centered_vz, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 10', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_centered_x, gas_centered_y, C=gas_centered_vz, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 10', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vz (km/sec)', fontsize=18)

plt.show()


########## Plots the Vr bar graphs ##########
plt.subplot(121)
plt.hexbin(gas_centered_x, gas_centered_y, C=gas_centered_vr, cmap=cm.Set1, gridsize=300, vmin=-120, vmax=120)
plt.title('Gas x vs y', fontsize=30)
plt.xlabel('x (kpc)', fontsize=28)
plt.ylabel('y (kpc)', fontsize=28)
plt.text(20, 20, 't = 10', fontsize=25)						### Make sure to change the time label ###
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_centered_x, gas_centered_y, C=gas_centered_vr, cmap=cm.Set1, gridsize=300, vmin=-120, vmax=120)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Gas x vs y', fontsize=30)
plt.xlabel('x (kpc)', fontsize=28)
plt.ylabel('y (kpc)', fontsize=28)
plt.text(20, 20, 't = 10', fontsize=25)						### Make sure to change the time label ###
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vr (km/sec)', fontsize=28)
cbar.ax.tick_params(labelsize=25)

plt.show()


########## Plots the Vtheta bar graphs ##########
plt.subplot(121)
plt.hexbin(gas_centered_x, gas_centered_y, C=gas_centered_vtheta, cmap=cm.jet_r, gridsize=300, vmin=180, vmax=240)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 10', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_centered_x, gas_centered_y, C=gas_centered_vtheta, cmap=cm.jet_r, gridsize=300, vmin=180, vmax=240)
plt.plot(a, b, '.', color='blueviolet', markersize=3, alpha=0.5)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 10', fontsize=15)						### Make sure to change the time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vtheta (km/sec)', fontsize=18)


plt.show()


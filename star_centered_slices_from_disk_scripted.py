import math
import numpy as np
import matplotlib.pyplot as plt
import glio
for num1 in range(5):
	for num2 in range(10):
		snap_name = 'snapshot_0%d%d' % (num1, num2)
		print snap_name
		s = glio.GadgetSnapshot(snap_name)
		s.load()


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
		
		
		########## Sets up the  x, y, and z postion arrays ##########
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
		star_centered_y[:] = [y - com_y for y in star_centered_y]
		star_centered_z[:] = [z - com_z for z in star_centered_z]
		
		
		########## For loop that splits up star z values ##########
		
		########## Subsampling rate ##########
		if num1 == 0 and num2 <= 7 :
			sub = 2
			print sub
		elif num1 == 0 and num2 >=8:
			sub = 6
			print sub 
		elif num1 == 1 and num2 == 0:
			sub = 6
			print sub 
		elif num1 == 1 and 1 <= num2 <= 3:
			sub = 6
			print sub 
		elif num1 == 1 and 4 <= num2 <=5:
			sub = 8
			print sub 
		elif num1 == 1 and 6 <= num2 <= 9:
			sub = 8
			print sub 
		elif num1 == 2 and 0 <= num2 <= 4:
			sub = 8
			print sub 
		elif num1 == 2 and 5 <= num2 <= 9:
			sub = 10
			print sub 
		elif num1 == 3 and 0 <= num2 <= 4:
			sub = 10
			print sub 
		elif num1 == 3 and 5 <= num2 <= 9:
			sub = 12
			print sub 
		elif num1 == 4 and num2 == 0:
			sub = 12
			print sub 

		### z > 0.3 ###
		x1 = []
		y1 = []
		
		for i in range(len(star_centered_z)):
			if star_centered_z[i] > 0.3:
				x1.append(star_centered_x[i])
				y1.append(star_centered_y[i])
		
		x1_sub = x1[0::sub]
		y1_sub = y1[0::sub]
		
		### 0.3 > z 0.2 ###
		x2 = []
		y2 = []
		
		for i in range(len(star_centered_z)):
			if 0.3 > star_centered_z[i] > 0.2:
				x2.append(star_centered_x[i])
				y2.append(star_centered_y[i])
		
		x2_sub = x2[0::sub]
		y2_sub = y2[0::sub]
		
		### 0.2 > z > 0.1 ###
		x3 = []
		y3 = []
		
		for i in range(len(star_centered_z)):
			if 0.2 > star_centered_z[i] > 0.1:
				x3.append(star_centered_x[i])
				y3.append(star_centered_y[i])
		
		x3_sub = x3[0::sub]
		y3_sub = y3[0::sub]
		
		### 0.1 > z 0.0 ###
		x4 = []
		y4 = []
		
		for i in range(len(star_centered_z)):
			if 0.1 > star_centered_z[i] > 0.0:
				x4.append(star_centered_x[i])
				y4.append(star_centered_y[i])
		
		x4_sub = x4[0::sub]
		y4_sub = y4[0::sub]
		
		### 0.0 > z -0.1 ###
		x5 = []
		y5 = []
		
		for i in range(len(star_centered_z)):
			if 0.0 > star_centered_z[i] > -0.1:
				x5.append(star_centered_x[i])
				y5.append(star_centered_y[i])
		
		x5_sub = x5[0::sub]
		y5_sub = y5[0::sub]
		
		### -0.1 > z > -0.2 ###
		x6 = []
		y6 = []
		
		for i in range(len(star_centered_z)):
			if -0.1 > star_centered_z[i] > -0.2:
				x6.append(star_centered_x[i])
				y6.append(star_centered_y[i])
		
		x6_sub = x6[0::sub]
		y6_sub = y6[0::sub]
		
		### -0.2 > z -0.3 ###
		x7 = []
		y7 = []
		
		for i in range(len(star_centered_z)):
			if -0.2 > star_centered_z[i] > -0.3:
				x7.append(star_centered_x[i])
				y7.append(star_centered_y[i])
		
		x7_sub = x7[0::sub]
		y7_sub = y7[0::sub]
		
		### z < -0.3 ###
		x8 = []
		y8 = []
		
		for i in range(len(star_centered_z)):
			if star_centered_z[i] < -0.3:
				x8.append(star_centered_x[i])
				y8.append(star_centered_y[i])
		
		x8_sub = x8[0::sub]
		y8_sub = y8[0::sub]
		
		
		########## Plots x vs y gas position graph for specific z values ##########
		
		### z > 0.3 ###
		plt.suptitle('Subsampled star z values for t = %d%d' % (num1, num2), fontsize=28)							### Make sure to change time label ###
		plt.subplot(241)
		plt.plot(x1_sub, y1_sub, '.', markersize=3, alpha=0.3)
		plt.title('z > 0.3', fontsize=18)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### 0.3 > z > 0.2 ###
		plt.subplot(242)
		plt.plot(x2_sub, y2_sub, '.', markersize=3, alpha=0.3)
		plt.title('0.3 > z > 0.2', fontsize=18)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### 0.2 > z > 0.1 ###
		plt.subplot(243)
		plt.plot(x3_sub, y3_sub, '.', markersize=3, alpha=0.3)
		plt.title('0.2 > z > 0.1', fontsize=18)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### 0.1 > z > 0.0 ###
		plt.subplot(244)
		plt.plot(x4_sub, y4_sub, '.', markersize=3, alpha=0.3)
		plt.title('0.1 > z > 0.0', fontsize=18)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### 0.0 > z > -0.1 ###
		plt.subplot(245)
		plt.plot(x5_sub, y5_sub, '.', markersize=3, alpha=0.3)
		plt.title('0.0 > z > -0.1', fontsize=18)
		plt.text(-35, 37, 'y (kpc)', fontsize=22, rotation='vertical')
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### -0.1 > z > -0.2 ###
		plt.subplot(246)
		plt.plot(x6_sub, y6_sub, '.', markersize=3, alpha=0.3)
		plt.title('-0.1 > z > -0.2', fontsize=18)
		plt.text(25, -35, 'x (kpc)', fontsize=22)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### -0.2 > z > -0.3 ###
		plt.subplot(247)
		plt.plot(x7_sub, y7_sub, '.', markersize=3, alpha=0.3)
		plt.title('-0.2 > z > -0.3', fontsize=18)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		### z < -0.3 ###
		plt.subplot(248)
		plt.plot(x8_sub, y8_sub, '.', markersize=3, alpha=0.3)
		plt.title('z < -0.3', fontsize=18)
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		plt.grid()
		
		plt.show()
		
		

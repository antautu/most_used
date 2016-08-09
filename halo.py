import numpy as np 
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_040')
s.load()

f = open('data_halo_xyz', 'w')
for i in range(0,len(s.pos[1][:])):
	f.write("%s %s %s\n" % (s.pos[1][i][0], s.pos[1][i][1], s.pos[1][i][2]))

f.close()

f2 = open('data_halo_xyz')
lines = f2.readlines()
f2.close()

halo_x = []
halo_y = []
halo_z = []

for line in lines:
	p = line.split()
	halo_x.append(float(p[0]))
	halo_y.append(float(p[1]))
	halo_z.append(float(p[2]))

halo_px = np.array(halo_x)
halo_py = np.array(halo_y)
halo_pz = np.array(halo_z)

#plt.plot(halo_px, halo_py, '.', markersize=3, alpha=0.05)
#plt.title('Halo x vs y', fontsize=30)
#plt.xlabel('x (kpc)', fontsize=25)
#plt.ylabel('y (kpc)', fontsize=25)
#plt.xticks(fontsize=15)
#plt.yticks(fontsize=15)
#plt.text(170, 175, 't = 40', fontsize=18)					### Make sure to change time label ###
#plt.axis([-200, 200, -200, 200])
#plt.gca().set_aspect('equal', adjustable='box')
#plt.grid()
#plt.show()


plt.plot(halo_px, halo_py, '.', markersize=2, alpha=0.2)
plt.title('Halo x vs z', fontsize=30)
plt.xlabel('x (kpc)', fontsize=25)
plt.ylabel('z (kpc)' , fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.text(85, 90, 't = 15', fontsize=18)							### Make sure to change time label ###
plt.axis([-100, 100, -100, 100])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()
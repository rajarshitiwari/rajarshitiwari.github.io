#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt




soft = ['Language', 'Linux/HPC', 'Machine\nlearning', 'Visualize', 'Simulation', 'Tools']
soft.reverse()

texts = [
    ['FORTRAN', 'Python3', 'Julia', 'C++', '', ''],
    ['zsh/bash', 'Linux admin', 'openmp/MPI', 'Cuda/GPU', 'slurm', ''],
    ['Tensorflow', 'Pytorch', 'mxnet', 'scikit', '', ''],
    ['Matplotlib', 'Gnuplot', 'asymptote', 'VESTA', '', ''],
    ['Monte-Carlo', 'Modelling', 'ase/pymatgen', 'AIMS', 'VASP', 'qiskit'],
    ['MS office', 'Mathematica', 'emacs', 'vscode', 'latex', '']
    ]

texts.reverse()
skill = [
    [8, 7, 6, 5, 0, 0],
    [8, 8, 8, 7, 7, 0],
    [7, 6, 5, 5, 0, 0],
    [8, 8, 8, 6, 0, 0],
    [9, 9, 8, 8, 7, 5],
    [6, 6, 8, 6, 8, 0]
    ]
skill.reverse()
texts = np.array(texts).T
skill = np.array(skill, dtype=float).T

for t in texts:
    print(t, len(t))

def get_rectangle1(h_val, v_val, h_shift):
    x, y, h = h_val, v_val, h_shift
    verts = list(zip([-x + h, x + h, x + h, -x + h, -x + h], [-y, -y, y, y, -y]))
    return verts
#                                                                                                                                                                           
def get_rectangle2(h_val, v_val, h_shift):
    x, y, h = h_val, v_val, h_shift
    verts = list(zip([0. + h, x + h, x + h, 0. + h, 0. + h], [0., 0., y, y, 0.]))
    return verts
#                                                                                                                                                                            


v_val = 1.0
h_val = 3
h_shift = 0
v_val, h_val, h_shift = 1.8, 3.6, 0.0


verts0 = get_rectangle1(h_val, v_val, h_shift)
#cmap = plt.cm.get_cmap('Spectral_r')
cmap = plt.cm.get_cmap('plasma')

plt.figure(figsize=(15,6))
plt.subplots_adjust(left=0.11, right=0.95, top=0.99, bottom=0.01)
plt.xlim(-0.5, 5.5)
plt.ylim(-0.5, 5.5)
for i in range(6):
    for j in range(6):
        print(texts[i, j])
        plt.scatter(i, j, s=24500, c=skill[i, j], marker=verts0, vmin=0, vmax=10, cmap=cmap)
        bbox = dict(boxstyle="round", lw=0.5, ec=cmap(skill[i, j]), fc='white', alpha=0.3)
        plt.text(i, j, s=texts[i, j], fontsize=21, ha='center', va='center', bbox=bbox)

plt.yticks(np.arange(6), soft, fontsize=21, fontname='Sans Serif')
plt.tick_params('y',  size=0)
plt.xticks([])
cax = plt.axes([0.952, 0.01, 0.03, 0.98])
cax.tick_params(labelsize=15)
plt.colorbar(cax=cax, ticks=np.arange(1,10))

plt.text(0.25, 3, "Confidence", rotation='vertical', color='white', fontsize=18)
plt.savefig('skills.png')

---
title: Rajarshi Tiwari's Curriculum Vitae
layout: default
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# Dr. Rajarshi Tiwari

## Basic information

``````{grid}
:gutter: 2

````{grid-item}
:outline:
:columns: 9
```{table}
|Rajarshi Tiwari                 |
|--                              |
|Indian National                 |
|DOB: April 30, 1984. Married    |
|Resident in Ireland for 10 years|
|Condensed matter, Quantum & HPC Computing, Machine Learning|
```
````
````{grid-item}
:columns: 3
```{image} ./rajr_cv.jpg
    :alt: photo
    :width: 200px
    :align: right
```
````
``````


```````{card} Social and Web profiles


``````{grid}
:gutter: 3 3 3 3
`````{grid-item-card} Email
:columns: 4
rajarshi.tiwari@ichec.ie tiwarir@tcd.ie
`````
`````{grid-item-card} Homepage
:columns: 4
:link: https://rajarshitiwari.github.io
[rajarshitiwari.github.io](https://rajarshitiwari.github.io)
`````
`````{grid-item-card} Linkedin
:columns: 4
:link: https://www.linkedin.com/in/rajarshi-tiwari/
[rajarshi-tiwari](https://www.linkedin.com/in/rajarshi-tiwari/)
`````
`````{grid-item-card} GitHub
:columns: 4
:link: https://github.com/rajarshitiwari/
[rajarshitiwari](https://github.com/rajarshitiwari/)
`````
`````{grid-item-card} Gitlab
:columns: 4
:link: https://gitlab.com/rajarshitiwari/
[rajarshitiwari](https://gitlab.com/rajarshitiwari)
`````
`````{grid-item-card} Twitter / X
:columns: 4
:link: https://twitter.com/rajr0
[rajr0](https://twitter.com/rajr0)
`````
``````
```````

## Positions and Roles
||||
|--|--|--|
|2013-2023|Research Fellow|School of Physics, CRANN and AMBER, Trinity College Dublin, Ireland|
|2023-Now|Sr. Computational Scientist|Irish Centre of High End Computing, Dublin, Ireland|

## Education
|Years|Degree| Institution|
|--   |--    |--          |
|2008-2014| PhD in Condensed Matter Physics^[1]| Harish Chandra Research Institute, Allahabad, India|
|2005-2008| MSc in Physics| Harish Chandra Research Institute, Allahabad, India|
|2002--2005| BSc in Physics and Mathematics| University of Allahabad, India|

[1]: **Thesis**: _The effect of geometrical frustration on some correlated electron systems_, Supervisor: **Prof. Pinaki Majumdar**.


## Short biography
I come from a city of Allahabad, in the state of Uttar Pradesh in India, where I got most of my education.
I did my B.Sc. from University of Allahabad, India with Physics and Mathematics as major in 2005.
Then I joined the Integrated Ph.D. (M.Sc. + Ph.D.) program at Harish-Chandra Research Institute (HRI),
Allahabad, India. I finished my MSc in Physics from HRI in 2008, and PhD in Condensed Matter Physics in 2013.
Thereafter, I joined Prof. Stefano Sanvito's research group at Trinity College, Dublin in 2013
for a year as Research Assistant, and after defending my thesis in September 2014, I continued there as
post-doctoral researcher. Currently I am a Research Fellow in the School of Physics, and work over a range of
project that overlap material science, many-body theory, high-througput DFT and machine learning.

### Computational Skills
% ![skills](./skills.png)

```{code-cell} ipython3
:tags: [remove-input]

import numpy as np
import matplotlib.pyplot as plt
#
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
def get_rectangle1(h_val, v_val, h_shift):
    x, y, h = h_val, v_val, h_shift
    verts = list(zip([-x + h, x + h, x + h, -x + h, -x + h], [-y, -y, y, y, -y]))
    return verts
#                                                    def get_rectangle2(h_val, v_val, h_shift):
    x, y, h = h_val, v_val, h_shift
    verts = list(zip([0. + h, x + h, x + h, 0. + h, 0. + h], [0., 0., y, y, 0.]))
    return verts
#                                                    v_val = 1.0
h_val = 3
h_shift = 0
v_val, h_val, h_shift = 1.8, 3.6, 0.0
verts0 = get_rectangle1(h_val, v_val, h_shift)
#cmap = plt.cm.get_cmap('Spectral_r')
cmap = plt.colormaps.get_cmap('plasma')
plt.figure(figsize=(15,6))
plt.subplots_adjust(left=0.11, right=0.95, top=0.99, bottom=0.01)
plt.xlim(-0.5, 5.5)
plt.ylim(-0.5, 5.5)
for i in range(6):
    for j in range(6):
        plt.scatter(i, j, s=24500, c=skill[i, j], marker=verts0, vmin=0, vmax=10, cmap=cmap)
        bbox = dict(boxstyle="round", lw=0.5, ec=cmap(skill[i, j]), fc='white', alpha=0.3)
        plt.text(i, j, s=texts[i, j], fontsize=21, ha='center', va='center', bbox=bbox)
#
plt.yticks(np.arange(6), soft, fontsize=21, fontname='Sans Serif')
plt.tick_params('y',  size=0)
plt.xticks([])
cax = plt.axes([0.952, 0.01, 0.03, 0.98])
cax.tick_params(labelsize=15)
plt.colorbar(cax=cax, ticks=np.arange(1,10))
_ = plt.text(0.25, 3, "Confidence", rotation='vertical', color='white', fontsize=18)
```


### Research Interests
My research insterest include solving models of electron correlation, high throughput \textit{ab-initio} simulations for material science. I also explore the use of Machine learning in these fields to expand and accelerate my research.

#### Correlated Systems, many-body models
During my Ph.D. my research interest grew around strongly correlated electronic systems, where I primarily worked on models of correlation. I love to explore magnetism, transport, frustration, disorder and their interplay in correlated electronic systems, such as transition metal Oxides, magnetic perovskites, pyrochlore systems. The phenomenology of these systems is best explored with suitably simplified models, such Hubbard model, Kondo-Lattice Model, Holstein model, Heisenberg model, and their variations/combinations depending on whether the relevant degrees of freedom are (i) itinerant electrons, (ii) localized spins, or (iii) phonons. I explore solving and analysing appropriate models of correlations through real-space based techniques like Monte-Carlo methods and Exact-Diagonalization.

#### Machine Learning in material science

After joining Trinity College Dublin, I expanded my research interests over computational materials science along with condensed-matter physics, where I explore application of machine learning in (i) solving or learning features in correlated systems and (ii) high-throughput _ab initio_
calculations. I learnt _ab-initio_ simulations tools such as VASP/FHI-AIMS to compute energetics of real systems, organize and process the data for ML applications. Here at TCD, we are also working on developing a _workflow_ to combine _ab-initio_ and ML tools to build up force fields for simulating large, disordered systems. The ICHEC-Flagship project "EuroCC-AF-3" has been quite helpful in this direction.
  
Following are the categories of ML applications I am involved with varying level of intensity -

- Exploring methods for structure property relations of materials with use of High-Throughput _ab initio_.
- Applying ML in models of many-body physics, such developing ML based lattice density functional theory for models.
- Exploring possibilities of DNNs as generative models for solving many-body problems in correlated systems.

### Computational interests

Ever since I joined my Ph.D. program back in India, computational field always intrigued me. This meant not only learning the languages and tools to do the required computations, but also learning how the hardware + software works together. I developed interest in Linux/HPC tools, by installing and exploring numerous linux distributions ranging from Ubuntu to Archlinux. I like the opportunity to play with new hardwares whenever possible.

My recent interest was exploring GPUs to accelerate some of our calculations. I secured "NVIDIA Academic Hardware Grant" last year, and had the GPUs installed in HPC machines, which boosted the group's interest. As a result, this year half of our group, and others as showed
interests and applied for the same grant for a range of projects.

We are also slowing gearing towards Quantum Computation (QC) in the area where some of our expertise may find
overlap. One of the direction we percieve could be the application of QC in solving many-body problems. However,
my current exposure is limited to some exploration of Qiskit package and a course of IBM-Quantum Fridays.
I am however interested in exploring this further.

### Teaching/training/industry

- I often co-supervise (i) summer interns (ii) final year project students and (iii) Ph.D. students in Prof. Sanvito's group over a range of problems on solving many-body models, _ab-initio_ and machine learning.
Some of the undergrads develop interest in academia and join Ph.D. programme either at Trinity with us or elsewhere.
- I have worked in past on projects partnered with Industry as AMBER researcher, such as Nokia's project for
`searching corrosion resistant metal alloys`, and recently, modelling magnetism in High Entropy Alloys.

- I coordinate with Trinity HPC team for our group's computational requirements. We have developed a local ecosystem to facilitate the necessary training, softwares, and other computational needs to younger members of the group.

- I also participate in preparing the hardware specifications and tenders of HPC systems/workstations that we purchase.

### Publications
  
- Emergence of highly bond-dependent anisotropic magnetic interactions in Sr$_4$RhO$_66$: a theoretical study, S. K. Pandey, Q. Gu, R. Tiwari, arXiv:2207.05045, 2022.

- Reactivity of transition-metal alloys to oxygen and sulfur, R. Tiwari, J. Nelson, C. Xu, and S. Sanvito, PRMaterials **5** 083801, 2021.

- Machine-learning semilocal density functional theory for many-body lattice models at zero and finite temperature, J. Nelson, R. Tiwari, and S. Sanvito, PRB **103** 245111, 2021.

- Orbital mott transition in two dimensional pyrochlore lattice, A. Saket and R. Tiwari, JPCM **32** 255601, 2020.

- Machine learning density functional theory for the hubbard model, J. Nelson, R. Tiwari, and S. Sanvito, PRB **99** 075132, 2019.

- Cr doping induced negative transverse magnetoresistance in Cd$_3$As$_2$ thin films, Y. Liu _et al_, PRB **97** 085303, 2018.

- Mott-hubbard transition and spin-liquid state on the pyrochlore lattice, N. Swain, R. Tiwari, and P. Majumdar, PRB **94** 155119, 2016.

- Spectroscopic signatures of the mott transition on the anisotropic triangular lattice, R. Tiwari and P. Majumdar, EPL **108** 27007, 2014.

- Mott transition and glassiness in the face centered cubic lattice, R. Tiwari and P. Majumdar, arXiv:1302.2922, 2013.

- The crossover from a bad metal to a frustrated mott insulator, R. Tiwari and P. Majumdar, arXiv:1301.5026, 2013.

- Noncollinear magnetic order in the double perovskites, R. Tiwari and P. Majumdar, IJMP B, **27** 1350018, 2013.

- Visualizing the mott transition, R. Tiwari and P. Majumdar, Current Science **103** 518-524, 2012.

- Exchange interactions and magnetic phases of transition metal oxides: Benchmarking advanced ab initio methods, T. Archer _et al_, PRB **84** 115114, 2011.

### References

``````{tab-set}
````{tab-item} Doctoral
```{card}
|   | Doctoral |
|---|---|
|🕵🏻 | Prof. Pinaki Majumdar |
|🏫 |Harish Chandra Research Institute, Prayagraj, UP, INDIA|
|☎️ | +91 532 2274316 |
|📧| pinaki@hri.res.in|
```
````
````{tab-item} External
```{card}
|   | External|
|---|---|
|🕵🏻 | Prof. Alessio Filippetti|
|🏫 |Dipartimento di Fisica, Università di Cagliari, Italy|
|☎️ | (+39) (070) 675 4853 |
|📧| alessio.filippetti@dsf.unica.it|
```
````
````{tab-item} Post-Doctoral
```{card}
||Post-Doctoral|
|---|---|
|🕵🏻 | Prof. Stefano Sanvito|
|🏫 |School of Physics and CRANN, Trinity College Dublin, Ireland|
|☎️ | +353 (0) 18963065 |
|📧| sanvitos@tcd.ie|
```
````
````{tab-item} Professional 1
```{card}
||Post-Doctoral|
|---|---|
|🕵🏻 | Prof. Jean-Christophe (JC) Desplat|
|🏫 |Irish Centre for High-End Computing, Dublin, Ireland|
|☎️ | +353 1 5291021 |
|📧| j-c.desplat@ichec.ie|
```
````
````{tab-item} Professional 2
```{card}
||Post-Doctoral|
|---|---|
|🕵🏻 | Dr. Venkatesh Kannan|
|🏫 |Irish Centre for High-End Computing, Dublin, Ireland|
|☎️ | +353 1 5291028 |
|📧| venkatesh.kannan@ichec.ie|
```
````
``````



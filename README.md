# Sources
`CMA Implementation
License: BSD License (BSD)
Author: Nikolaus Hansen
Maintainer: Nikolaus Hansen
https://pypi.org/project/cma/`

`CEC13 Test Function Suite 
Jane Jing Liang (email: liangjing@zzu.edu.cn) 
Last Modified on 14th Feb. 2013
https://github.com/P-N-Suganthan/CEC2013`

# Modification authors
Wojciech Rokicki,
Michał Szpunar

## Installing procedure for Ubuntu (prerequisities)
In my case it was WSL (Ubuntu 18.04).
I am using python 2.7
`sudo apt-get install python-pip`
`pip install numpy`
`pip install matplotlib`

There was a problem due to the lack of GUI (X server would be necessary) so I decided to use PowerShell instead. I would have to install MS Visual Studio in order to compile boost (v.1_72_0) dynamic libraries so i've decided to switch to Ubuntu 18.04.3 LTS.
Installing components were the same.

## Executing
Simply run `purecma_mod_sim.py` for tournament modification or `purecma_ref_sim.py` for reference cma (half winners from sorting by tfvalue).

## What could be done better?
- Multithreading
- Code optimalization
- Plotting
- Installation process (some problems with bash)
- Data backup
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
Wojciech Rokicki
Michał Szpunar

## Installing procedure for Ubuntu (prerequisities)
In my case it was WSL (Ubuntu 18.04).
I am using python 2.7
`sudo apt-get install python-pip`
`pip install cma` - not necessary, instead use repo's cma package
`pip install numpy`
`pip install matplotlib`

There was a problem due to the lack of GUI (X server would be necessary) so I decided to use PowerShell instead. I would have to install MS Visual Studio in order to compile boost (v.1_72_0) dynamic libraries so i've decided to switch to Ubuntu 18.04.3 LTS.
Installing components were the same.

To run our modification replace whole cma folder with repo's cma package.
CMA is usually installed in:
`~/.local/lib/python2.7/site-packages/cma`
#!/bin/bash
# A Simple Shell Script To Set Essential Tools Up on VM
# Wojciech Rokicki - 25/Jan/2020
# before launching give 777 perm
#
sudo apt-get update
sudo apt install vim --assume-yes
sudo apt install gcc --assume-yes
sudo apt install g++ --assume-yes
sudo apt install git --assume-yes
sudo apt install python --assume-yes
sudo apt-get install python-dev libxml2-dev libxslt-dev --assume-yes
#
cd ~
mkdir project
cd project
git init
git remote add origin https://github.com/ALHESzpuniWojro/Projekt-1.git
git pull origin master
#
cd ~
wget https://dl.bintray.com/boostorg/release/1.72.0/source/boost_1_72_0.tar.gz
tar -xvf boost_1_72_0.tar.gz
rm boost_1_72_0.tar.gz
#
# Sometimes it doesn't work. Why?
export PATH=$PATH:/home/rokwojtek/.local/bin
# echo $LD_LIBRARY_PATH aby sprawdzic czy jest
LD_LIBRARY_PATH=/usr/local/lib
export LD_LIBRARY_PATH
#
# Nie działało, nie znajdywało ścieżki
# sudo apt install python-pip
# więc postanowiłem użyć:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
#
# potem można było w końcu:
pip install scons
pip install numpy
#
# również trzeba było dodać ścieżkę do aplikacji do zmiennych środowiskowych
#
cd boost_1_72_0
sudo ./bootstrap.sh --prefix=/usr/local
sudo ./b2 install
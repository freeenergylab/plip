source /zfs/pengfeili/software/anaconda3/bin/activate openmm
python setup.py build_ext -I/zfs/pengfeili/software/anaconda3/envs/openmm/include/openbabel3/ -L/zfs/pengfeili/software/anaconda3/envs/openmm/lib
python setup.py install

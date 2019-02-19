[![Build Status](https://travis-ci.org/bsamseth/mpi4py-travis.svg?branch=master)](https://travis-ci.org/bsamseth/mpi4py-travis)
# mpi4py-travis

This is a reference repository showing how to use Travis CI with:

- [OpenMPI](open-mpi.org) with C++17 support
- [mpi4py](https://mpi4py.readthedocs.io/en/stable/) with Python 3.7

The approach is to fetch a C++17 compiler (e.g. `g++7`) and Python 3.7 with special apt-sources, then building OpenMPI from source with this compiler, which results in a C++17 compatible MPI compiler. Finally, mpi4py is installed, being told about this new MPI compiler. 

Additionally, because building MPI from source takes quite some time (10+ minutes), the installation is cached between each build. This means the MPI installation only has to be built once, and is reused the rest of the time, which saves time.

See [`.travis.yml`](.travis.yml) for the how to do this!

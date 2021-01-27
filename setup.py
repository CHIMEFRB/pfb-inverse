import os

from numpy.distutils.core import Extension, setup
from setuptools import find_packages

source = ["dgbmv.pyf"]

# Set up the libraries for building against BLAS. Either use an internal copy
# of dgbmv.f, or try and build against MKL.
if "MKLROOT" in os.environ:  # Check to see if we have MKL available
    blas_lib = [
        "mkl_rt",
        "iomp5",
        "pthread",
        "m",
    ]  # MKL libraries we need to link against
    blas_libdir = [os.environ["MKLROOT"] + "/lib/intel64"]
else:
    source += ["dgbmv.f"]
    blas_lib = []
    blas_libdir = []

use_omp = True
omp_args = ["-fopenmp"] if use_omp else []

dgbmv_ext = Extension(
    "dgbmv",
    source,
    library_dirs=blas_libdir,
    libraries=blas_lib,
    extra_compile_args=omp_args,
    extra_link_args=omp_args,
)

setup(
    name="pfb-inverse",
    version="0.1.0",
    ext_modules=[dgbmv_ext],
    packages=find_packages(),
    install_requires=["numpy", "h5py", "mpi4py", "scipy"],
    setup_requires=["numpy"]
)

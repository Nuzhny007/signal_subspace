#!/usr/bin/env python
install_requires=['numpy','scipy', 'pandas']
tests_require=['nose','coveralls']
# %%
from setuptools import find_packages
from numpy.distutils.core import setup,Extension

setup(name='signal_subspace',
      packages=find_packages(),
      version='1.0.0',
	  description='1-D & 2-D signal subspace estimation methods',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/signal_subspace',
      classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          ],
      ext_modules=[Extension(name='fortsubspace_cmpl',
                    sources=['comm.f90','filters.f90', 'covariance.f90', 'subspace.f90'],
                    f2py_options=['--quiet'],
                    extra_link_args=['-llapack'] ),

                   Extension(name='fortsubspace_real',
                    sources=['comm.f90', 'filters.f90','covariance_realsp.f90', 'subspace_realsp.f90'],
                    f2py_options=['--quiet'],
                    extra_link_args=['-llapack'])],
      install_requires=install_requires,
      extras_require={'plot':['matplotlib','seaborn'],'tests':tests_require},
      tests_require=tests_require,
      python_requires='>=3.6',
	  )


#! /usr/bin/env python

"""\
Simple set of modules to help reading HepMC files using the pyhepmc module.
Mainly provides wrapper of std::istream (expected input for HepMC swig methos)
and python generator to loop events.
"""

from distutils.core import setup, Extension
#weird need to use distutils instead of setuptools... or not?
#https://github.com/wnd-charm/wnd-charm/issues/11

## Extension definition
ext = Extension('_streamproxy', ['hepmcanalysis/streamproxy.i'],swig_opts=['-c++'])


## Setup definition
setup(name = 'hepmcanalysis',
      version = '0.0.1',
      ext_package = "hepmcanalysis",
      ext_modules = [ext],
      py_modules = [ 'hepmcanalysis.__init__','hepmcanalysis.events','hepmcanalysis._streamproxy','hepmcanalysis.streamproxy'],
      author = 'Lukas Heinrich',
      author_email = 'lukas.heinrich@cern.ch',
      description = 'simple module to easily read hepMC files via pyhepmc',
      long_description = __doc__,
      keywords = 'generator montecarlo simulation data hep physics particle',
      license = 'GPL')

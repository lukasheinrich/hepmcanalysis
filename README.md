hepmcanalysis
=============

[![DOI](https://zenodo.org/badge/22998462.svg)](https://zenodo.org/badge/latestdoi/22998462)


simple python module to have easy HepMC event loops in python. This is very light wrapper around [pyhepmc](https://pypi.python.org/pypi/pyhepmc).


Installation
------------

    git clone https://github.com/lukasheinrich/hepmcanalysis.git
    cd hepmcanalysis
    python setup.py build
    python setup.py install

Usage
------------
A complete example looping events and printing them looks like this:

    #!/usr/bin/env python

    from hepmcanalysis.events import fromfile

    def main():
        for e in fromfile('test.hepmc'):
            print 'numer of particles: {}'.format(len(e.particles()))

    if __name__ == '__main__':
        main()

example: 
http://nbviewer.ipython.org/github/lukasheinrich/hepmcanalysis/blob/master/hepmczanalysis.ipynb

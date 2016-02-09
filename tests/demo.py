#!/usr/bin/env python

from hepmcanalysis.events import fromfile

def main():
    for e in fromfile('test.hepmc'):
        print 'numer of particles: {}'.format(len(e.particles()))

if __name__ == '__main__':
    main()
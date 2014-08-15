hepmcanalysis
=============

simple python module to have easy HepMC event loops in python. This is very light wrapper around [pyhepmc](https://pypi.python.org/pypi/pyhepmc).


Installation
------------

    git clone https://github.com/lukasheinrich/hepmcanalysis.git
    cd hepmcanalysis
    python setup.py install

Usage
------------
To read in a HepMC file create a ifstream proxy to it:

    from hepmcanalysis.streamproxy import ifstream_proxy
    proxy = ifstream_proxy('./input.hepmc')

This proxy can be used as an input into the constructor of `hepmc.IO_GenEvent`:

	import hepmc
	g = hepmc.IO_GenEvent(proxy.stream())

also a python generator is provided that takes a `hepMC.IO_GenEvent` and yields events until the file is exhausted:

	from hepmcanalysis.events import events
	for i,e in enumerate(events(g)):
		#do stuff

A complete example looping events and printing them looks like this:

	#!/usr/bin/env python
	from hepmcanalysis.events import events
	from hepmcanalysis.streamproxy import ifstream_proxy
	import hepmc

	def main():
  	  proxy = ifstream_proxy('./input.hepmc')

	  g = hepmc.IO_GenEvent(proxy.stream())
	  for i,e in enumerate(events(g)):
	    print 'event #{}: number of particles in event:{}'.format(i,len(e.particles()))
	    print e

	if __name__ == '__main__':
	  main()
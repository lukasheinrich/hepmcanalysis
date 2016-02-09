import hepmc
from hepmcanalysis.streamproxy import stringstream_proxy
from hepmcanalysis.streamproxy import ostringstream_proxy
from hepmcanalysis.streamproxy import ifstream_proxy

def events(genevent):
  '''simple generator that exhausts the read_next_event of a GenEvent object'''
  ev = genevent.read_next_event()
  while ev is not None:
     yield ev
     ev = genevent.read_next_event()

def fromfile(filename):
    proxy = ifstream_proxy(filename)
    g = hepmc.IO_GenEvent(proxy.stream())
    for e in events(g):
        yield e

def fromstring(string):
    proxy = stringstream_proxy()
    proxy.write(string)
    g = hepmc.IO_GenEvent(proxy.stream())
    for e in events(g):
        yield e

def dumps(events):
    outproxy = ostringstream_proxy()
    outevent = hepmc.IO_GenEvent(outproxy.stream())
    for e in events:
        outevent.write_event(e)
    del outevent
    output =  outproxy.str()
    return output

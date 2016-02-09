import hepmc
from hepmcanalysis.streamproxy import ostringstream_proxy

def events(genevent):
  '''simple generator that exhausts the read_next_event of a GenEvent object'''
  ev = genevent.read_next_event()
  while ev is not None:
     yield ev
     ev = genevent.read_next_event()

def dumps(event):
    outproxy = ostringstream_proxy()
    outevent = hepmc.IO_GenEvent(outproxy.stream())
    outevent.write_event(event)
    del outevent
    output =  outproxy.str()
    return '\n'.join(output.split('\n')[3:-2])    

from hepmcanalysis.events import events
from hepmcanalysis.streamproxy import ifstream_proxy
import hepmc

def readhepmc(hepmcfile):
  proxy = ifstream_proxy('./input.hepmc')
  g = hepmc.IO_GenEvent(proxy.stream())
  return events(g)

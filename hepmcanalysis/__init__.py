from hepmcanalysis.events import events
from hepmcanalysis.streamproxy import ifstream_proxy
import hepmc

def readhepmc(hepmcfile):
  proxy = ifstream_proxy(hepmcfile)

  g = hepmc.IO_GenEvent(proxy.stream())

  for e in events(g):
    yield e
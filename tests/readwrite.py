from hepmcanalysis.events import events,dumps,fromfile

for e in fromfile('test.hepmc'):
    print dumps(e)


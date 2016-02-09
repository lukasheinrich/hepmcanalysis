from hepmcanalysis.events import events,dumps,fromfile, fromstring

print 'single event'
print dumps([fromfile('test.hepmc').next()])

eventstring = dumps([fromfile('test.hepmc').next()])
print dumps([e for e in fromstring(eventstring)]) == eventstring

print 'many events'
print dumps([e for e in fromfile('test.hepmc')])


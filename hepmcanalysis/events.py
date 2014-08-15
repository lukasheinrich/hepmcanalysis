def events(genevent):
  '''simple generator that exhausts the read_next_event of a GenEvent object'''
  ev = genevent.read_next_event()
  while ev is not None:
     yield ev
     ev = genevent.read_next_event()
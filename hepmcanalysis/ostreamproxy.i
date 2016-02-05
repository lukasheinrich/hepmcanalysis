%module streamproxy
 /**
 * Simple class to expose std::streams in the python
 * interface.  works around some issues with trying to directy
 * the file stream objects
 */
%{
#include "streamproxy.h" //include in _wrap.cxx
%}

%include "streamproxy.h"

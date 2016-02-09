#ifndef OSTRINGSTREAMPROXY
#define OSTRINGSTREAMPROXY
#include <sstream>
#include <iostream>

//taken from http://stackoverflow.com/a/18879140/286382
class ostringstream_proxy {
    public:
        ostringstream_proxy(): m_ostr(){
            // no op
        }
        virtual ~ostringstream_proxy(){
            // no op
        }
        std::string str(){
          return m_ostr.str();
        }

        std::ostream& stream(){
            return m_ostr;
        }
        // TBD: do I want to  add additional stream manipulation functions?
   private: 
        std::ostringstream m_ostr;
};
#endif

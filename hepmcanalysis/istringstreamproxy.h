#ifndef STRINGSTREAMPROXY
#define STRINGSTREAMPROXY
#include <sstream>
#include <iostream>

//taken from http://stackoverflow.com/a/18879140/286382
class stringstream_proxy {
    public:
        stringstream_proxy(): m_str(){
            // no op
        }
        virtual ~stringstream_proxy(){
            // no op
        }
        
        void write(const std::string& input){
          m_str << input;
        }
        
        std::string str(){
          return m_str.str();
        }

        std::istream& stream(){
            return m_str;
        }
        // TBD: do I want to  add additional stream manipulation functions?
   private: 
        std::stringstream m_str;
};
#endif

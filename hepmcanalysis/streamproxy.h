#ifndef IFSTREAMPROXY
#define IFSTREAMPROXY
#include <fstream>
//taken from http://stackoverflow.com/a/18879140/286382
class ifstream_proxy {
    public:
        ifstream_proxy(): m_istr(){
            // no op
        }
        ifstream_proxy(const char* fname): m_istr(){
					open(fname);
        }
        virtual ~ifstream_proxy(){
            // no op
        }
        void open(const char* fname ){
            m_istr.close(); 
            m_istr.open( fname, std::ifstream::in|std::ifstream::binary) ;
        }
        std::istream& stream(){
            return m_istr;
        }
        // TBD: do I want to  add additional stream manipulation functions?
   private: 
        std::ifstream m_istr;
};
#endif

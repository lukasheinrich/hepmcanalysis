#ifndef OFSTREAMPROXY
#define OFSTREAMPROXY
#include <fstream>
//taken from http://stackoverflow.com/a/18879140/286382
class ofstream_proxy {
    public:
        ofstream_proxy(): m_ostr(){
            // no op
        }
        ofstream_proxy(const char* fname): m_ostr(){
					open(fname);
        }
        virtual ~ofstream_proxy(){
            // no op
        }
        void open(const char* fname ){
            m_ostr.close(); 
            m_ostr.open( fname, std::ofstream::out|std::ifstream::binary) ;
        }
        std::ostream& stream(){
            return m_ostr;
        }
        // TBD: do I want to  add additional stream manipulation functions?
   private: 
        std::ofstream m_ostr;
};
#endif

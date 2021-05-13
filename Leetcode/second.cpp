class Solution {
public:
    string defangIPaddr(string address) {
        string d="";
        for( char c:address)
            (c == '.') ? d += "[.]" :
                     d += c;
        return d;
        
    }
};
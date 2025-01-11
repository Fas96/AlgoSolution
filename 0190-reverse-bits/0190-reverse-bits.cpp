class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
         string binary = bitset<32>(n).to_string(); 
        reverse(binary.begin(), binary.end()); 
        return bitset<32>(binary).to_ulong();
    }
};
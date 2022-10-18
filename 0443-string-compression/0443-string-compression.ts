function compress(chars: string[]): number {
    let compressed = "";
    let count = 1;
    for (let i = 1; i < chars.length; i++) {
        if (chars[i] == chars[i - 1]) {
            count++;
        } else {
            compressed += chars[i - 1];
            if (count > 1) {
                compressed += count;
            }
            count = 1;
        }
    }
  
    //last character count
    compressed += chars[chars.length - 1];
    if (count > 1) {
        compressed += count;
    }
    //modifying the input array
    for (let i = 0; i < compressed.length; i++) {
        chars[i] = compressed[i];
    }
 
    return compressed.length;
};
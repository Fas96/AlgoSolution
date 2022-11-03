function longestPalindrome(words: string[]): number {
      let unpaired = new Map<string, number>();  
    let length = 0;   
    let loneSymmCount = 0;   
    for (let i = 0; i < words.length; ++i) {
 
        if (words[i][0] === words[i][1]) {
            const count = unpaired.get(words[i]) || 0;

            
            if (count === 1) {
                length += 4;
                unpaired.set(words[i], 0);
                loneSymmCount--;

              
            } else {
                unpaired.set(words[i], 1);
                loneSymmCount++;
            }
 
        } else {

           
            const reversal = `${words[i][1]}${words[i][0]}`;
            const reversalCount = unpaired.get(reversal) || 0;
            if (reversalCount >= 1) {
                unpaired.set(reversal, reversalCount - 1);
                length += 4;

               
            } else {
                const count = unpaired.get(words[i]) || 0;
                unpaired.set(words[i], count + 1);
            }
        }
    }

    length += loneSymmCount > 0 ? 2 : 0;
    return length ;

};
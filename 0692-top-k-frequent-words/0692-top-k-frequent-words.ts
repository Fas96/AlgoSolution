
function topKFrequent(words: string[], k: number): string[] {
   let result: string[] = [];
    
    let map: Map<string, number> = new Map();
    
    for (let word of words) {
        map.set(word, (map.get(word) || 0) + 1);
    }
    
    let wordsA: string[] = Array.from(map.keys());
    
    wordsA.sort((w1, w2) => map.get(w1) == map.get(w2) ? w1.localeCompare(w2) : map.get(w2) - map.get(w1));
    
    for (let i = 0; i < k; i++) {
        result.push(wordsA[i]);
    }
    return result;

};
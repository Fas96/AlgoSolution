function groupAnagrams(strs: string[]): string[][] {

     if(strs==null || strs.length==0) return [];
    let map = new Map();
    for(let str of strs){
        let key = str.split("").sort().join("");
        if(!map.has(key)){
            map.set(key,[]);
        }
        map.get(key).push(str);
    }
    return Array.from(map.values());
};
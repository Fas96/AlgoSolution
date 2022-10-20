function intToRoman(num: number): string {
     let roman: string = "";
    let map: Map<number, string> = new Map();
    map.set(1, "I");
    map.set(4, "IV");
    map.set(5, "V");
    map.set(9, "IX");
    map.set(10, "X");
    map.set(40, "XL");
    map.set(50, "L");
    map.set(90, "XC");
    map.set(100, "C");
    map.set(400, "CD");
    map.set(500, "D");
    map.set(900, "CM");
    map.set(1000, "M");
    let keys: number[] = Array.from(map.keys());
    keys.sort((a, b) => b - a);
    while (num > 0) {
        for (let i = 0; i < keys.length; i++) {
            if (num >= keys[i]) {
                num -= keys[i];
                roman += map.get(keys[i]);
                break;
            }
        }
    }
    return roman;
};
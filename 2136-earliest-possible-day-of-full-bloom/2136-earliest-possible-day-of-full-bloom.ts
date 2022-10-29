 

function earliestFullBloom(plantTime: number[], growTime: number[]): number {
     const temp = plantTime.map((v, i) => [v, growTime[i]]);
    temp.sort((a, b) => b[1] - a[1]);
    let max = 0;
    let cum = 0;
    for (let i = 0; i < temp.length; i++) {
        max = Math.max(max, cum + temp[i][0] + temp[i][1]);
        cum = cum + temp[i][0];
    }
    return max;

};
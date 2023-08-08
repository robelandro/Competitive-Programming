'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = require("fs");
process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString = '';
let inputLines = [];
let currentLine = 0;
process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});
process.stdin.on('end', function () {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});
function readLine() {
    return inputLines[currentLine++];
}
/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */
function countingValleys(steps, path) {
    let valleys = 0;
    let currentLevel = 0;
    let oldLevel = 0;
    for (let char of path) {
        currentLevel = (char === 'U') ? currentLevel + 1 : currentLevel - 1;
        // console.log(`${char} | Current: ${currentLevel} | Old: ${oldLevel}`);
        if (currentLevel === 0 && oldLevel < 0) {
            valleys++;
        }
        oldLevel = currentLevel;
    }
    return valleys;
}
function main() {
    const ws = (0, fs_1.createWriteStream)(process.env['OUTPUT_PATH'] || './');
    const steps = parseInt(readLine().trim(), 10);
    const path = readLine();
    const result = countingValleys(steps, path);
    ws.write(result + '\n');
    ws.end();
}

#!/usr/bin/node

const process = require('process');
const args = process.argv;

function nextBiggest (arr) {
  let max = 1; let result = 1;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr]; // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }

  return result;
}
console.log(nextBiggest(args));

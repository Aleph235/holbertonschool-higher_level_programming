#!/usr/bin/node

const process = require('process');
const args = process.argv;

const x = Number(args[2]);

function factorial (b) {
  if (b === 0 || isNaN(b)) {
    return 1;
  } else {
    return b * factorial(b - 1);
  }
}

console.log(factorial(x));

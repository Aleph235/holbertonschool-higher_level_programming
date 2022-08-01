#!/usr/bin/node

const process = require('process');
const args = process.argv;

const x = Number(args[2]);
const y = Number(args[3]);
function add (a, b) {
  return a + b;
}
console.log(add(x, y));

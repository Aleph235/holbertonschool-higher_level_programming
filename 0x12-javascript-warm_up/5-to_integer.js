#!/usr/bin/node

const process = require('process');
const args = process.argv;

const x = Number(args[2]);

if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}

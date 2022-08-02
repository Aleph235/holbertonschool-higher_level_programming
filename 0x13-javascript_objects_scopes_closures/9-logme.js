#!/usr/bin/node
let clicker = 0;
exports.logMe = function (item) {
  console.log('%d: %s', clicker, item);
  clicker++;
};

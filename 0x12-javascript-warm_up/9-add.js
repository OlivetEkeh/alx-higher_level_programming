#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function addition (a, b) {
  console.log(a + b);
}

addition(a, b);
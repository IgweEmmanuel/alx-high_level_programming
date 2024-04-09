#!/usr/bin/node
const [,, ...x] = process.argv;

let i = 0;

if (isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(x)) {
    console.log('C is fun');
    i++;
  }
}

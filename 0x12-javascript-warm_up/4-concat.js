#!/usr/bin/node
const [,, ...argv] = process.argv;

if (argv[0] && argv[1]) {
  console.log(argv[0] + ' is ' + argv[1]);
} else {
  console.log('');
}

#!/usr/bin/node
// This displays the content of a file

const fs = require('node:fs');
const [, , filepath, text] = process.argv;

fs.writeFile(filepath, text, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
  // console.log('Text written to file');
});

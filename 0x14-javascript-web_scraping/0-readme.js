#!/usr/bin/node
// This displays the content of a file

const fs = require('node:fs');
const { resolve } = require('path');
const [, , filepath] = process.argv;
const newpath = resolve(process.cwd(), filepath);

fs.readFile(newpath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

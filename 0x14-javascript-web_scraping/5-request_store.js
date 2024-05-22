#!/usr/bin/node
// gets content and store in a file

const request = require('request');
const fs = require('node:fs');
const [, , url, fp] = process.argv;

request(url).pipe(fs.createWriteStream(fp));

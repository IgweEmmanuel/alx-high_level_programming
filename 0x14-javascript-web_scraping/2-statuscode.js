#!/usr/bin/node
// Display status code of a GET HTTP method

const request = require('request');
const [, , url] = process.argv;

request(url, (err, response) => {
  if (err) console.error(err);
  console.log('code: ' + response.statusCode);
});

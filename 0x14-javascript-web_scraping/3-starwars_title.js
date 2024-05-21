#!/usr/bin/node
// star wars title fetcher using id through the api

const request = require('request');
const [, , id] = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const ps = JSON.parse(body);
    console.log(ps.title);
  } else {
    console.error(error);
  }
});

#!/usr/bin/node

const dict = require('./101-data').dict;

const invertedDict = {};

for (const userId in dict) {
    const occurrence = dict[userId];
    if (!(occurrence in invertedDict)) {
        invertedDict[occurrence] = [];
    }
    invertedDict[occurrence].push(userId);
}

console.log(invertedDict);

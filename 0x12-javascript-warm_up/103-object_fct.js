#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

for (let i = 1; i <= 3; i++) {
  myObject.value++;
  if (myObject.value > 12) {
    myObject.incr = function () {
      this.value++;
    };
  }
  console.log(myObject);
}

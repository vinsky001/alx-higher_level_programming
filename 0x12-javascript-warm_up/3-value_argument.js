#!/usr/bin/node

const [arg] = process.argv.slice(2); // ignores the last 2  argumentspassed //

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}

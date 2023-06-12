#!/usr/bin/node

const args = process.argv.slice(2);
/*
 * process.argv array are the path to the Node.js executable
 * Slice - .slice(2) to extract only the arguments provided by the user, excluding the first two elements
 */

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

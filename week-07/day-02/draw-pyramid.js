'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

var star = '+'
var empty = '/'

for (let i = 0; i <= lineCount; i ++) {
    console.log(" ".repeat(lineCount - i) + "*" + "*".repeat(i+i) ) 
}
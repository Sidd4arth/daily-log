//synchronus
// var a= wait(1);

const fs = require("fs"); //importing lib

const contents = fs.readFileSync("a.txt", "utf-8");
console.log(contents); 
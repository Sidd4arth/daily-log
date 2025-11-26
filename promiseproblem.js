// //create the promised verison of
// //fs.readFile
// //fs.writeFile
// //cleanFile


const fs=require("fs");
function readTheFile(r){
    fs.readFile("a.txt", "utf-8",function(err, data)){
        r(data);
    }
}

function readFile(filename)
{
    //read filename and returns its value
    return new Promise();
}
const p = readFile();
function callback(contents) {
    console.log(contents);
}

p.then(callback);
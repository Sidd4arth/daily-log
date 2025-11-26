//return something in future

//setTime(fn, 3000);

// calllback based approach
//promise based approach
//eventual completion or failure of an asyn operation and its resultiing value
/*
function main()
{

}
setTimeout(main,3000); //callback the main fucntion after 3sec
*/
//promised version:

function setTimeoutPromised(ms){
    return new Promise(resolve=>setTimeout(resolve, ms));
    //returns an object // instance of the promise class !
} 
    function callback()
    {
        console.log("3 sec have passed");
    }

setTimeoutPromised(3000).then(callback);

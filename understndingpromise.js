function random (resolve)  //resolve is also a fucntion
{   
    //resolve(); // calls resolve without any asyn,
    setTimeout(resolve, 3000); // eventual completion after 3 sec 
    
}

let p = new Promise(random);///suppose to return eventually (as defination of promise class says:)


function callback()
{
    console.log("Promise succeded");
}

p.then(callback);
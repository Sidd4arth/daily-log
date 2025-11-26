//sum of no. from 1 to n
function sumto(n){
    let sum=0;
    for(let i =1;i<=n;i++){
        sum=sum+i;
    }
    return sum;
}

//taking input n:
let n=parseInt(prompt("Enter a number"));
let result = sumto(n);
console.log(result);
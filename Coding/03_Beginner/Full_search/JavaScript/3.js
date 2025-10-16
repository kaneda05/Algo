const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const N = Number(input[0]);
const V = Number(input[1]);
const A = input.slice(2).map(Number);

let flag = false;
let asn = -1
for (let i = 0; i < N; i++){
    if (A[i] == V){
        ans = i
        flag = true
    }
}

if (flag){
    console.log(ans);
}else{
    console.log(-1);
}
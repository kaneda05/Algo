const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const N = Number(input[0]);
const V = Number(input[1]);
const A = input.slice(2).map(Number);

for (let i = 0; i<N; i++){
    if(A[i] == V){
        console.log("Yes");
        process.exit();
    }
}

console.log("No")
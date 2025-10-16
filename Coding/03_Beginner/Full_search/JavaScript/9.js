const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();
const N = Number(input);

let flag = true;

if (N>=2){
    for (let i = 2; i < N; i++){
        if (N % i == 0){
            flag = false;
            break;
        }
    }
}else{
    flag = false;
}

console.log(flag ? "Yes" : "No");
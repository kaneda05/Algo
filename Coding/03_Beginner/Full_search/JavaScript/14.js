const fs = require("fs");
const S = fs.readFileSync(0, "utf8").trim();

let cnt = 0;
for (let i = 0; i < S.length - 1; i++){
    if (S[i] == S[i+1]){
        cnt++;
    }
}

console.log(cnt);
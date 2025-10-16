const fs = require("fs");
const [S, c] = fs.readFileSync(0, "utf8").trim().split("\n");

let found = false;
for (let i = 0; i < S.length; i++){
    if (S[i] == c){
        found = true;
        break;
    }
}

console.log(found ? "Yes" : "No");
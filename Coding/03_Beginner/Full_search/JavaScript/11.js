const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();
const N = parseInt(input, 10);

let cnt = 0;
for (let i = 1; i <= N; i++) {
  if (N % i == 0) {
    cnt++;
  }
}

console.log(cnt);
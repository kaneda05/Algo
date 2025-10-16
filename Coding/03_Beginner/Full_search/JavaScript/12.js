const fs = require("fs");
const [A, B] = fs.readFileSync(0, "utf8").trim().split(" ").map(Number);

let N = Math.min(A, B);
let ans = 1;

for (let i = 1; i <= N; i++) {
  if (A % i === 0 && B % i === 0) {
    ans = i;
  }
}

console.log(ans);

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const [N, M] = input;
let A = input.slice(2, 2 + N);
let B = input.slice(2 + N);

let cnt = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (A[i] > B[j]) cnt++;
  }
}

console.log(cnt);

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const [N, M, K] = input;
let A = input.slice(3, 3 + N);
let B = input.slice(3 + N);

let cnt = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (A[i] + B[j] == K) cnt++;
  }
}

console.log(cnt);

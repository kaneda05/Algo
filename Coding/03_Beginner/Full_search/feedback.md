# 全探索

## 各言語ごとのメモ

### Python

---

### C++
|問題|コード|
|:--:|:--:|
|[文字 c が含まれるか](https://algo-method.com/tasks/226)|[コード]()|

- `(char xx : xx)`
```c++
for (char ch : S){
    if (ch == c[0]){
        found = true;
        break;
        }
```
---

### Java
|問題|コード|
|:--:|:--:|
|[文字 c が含まれるか](https://algo-method.com/tasks/226)|[コード]()|

- `charAt()`
```java
for (int i = 0; i < S.length(); i++){
    if (S.charAt(i) == c.charAt(0)){
        found = true;
        break;
    }
}
```
---

### Javascript

|問題|コード|
|:--:|:--:|
|[素数判定](https://algo-method.com/tasks/222)|[コード]()|

```javascript
console.log(flag ? "Yes" : "No");
```

---

### Ruby

|問題|コード|
|:--:|:--:|
|[整数Vの場所](https://algo-method.com/tasks/216)|[コード]()|
|[増加箇所の個数](https://algo-method.com/tasks/215)|[コード]()|
|[素数判定](https://algo-method.com/tasks/222)|[コード]()|
|[文字 c が含まれるか](https://algo-method.com/tasks/226)|[コード]()|


- `each`
- `each_with_index`
- `(1...N).each do |i|`
- `S.each_char do |ch|`

```ruby
# Aはリスト
A = gets.split.map(&:to_i)
A.each do |x|
```

```ruby
# Aはリスト
A = gets.split.map(&:to_i)
A.each_with_index do |x, i|
```

```ruby
# Aはリスト
A = gets.split.map(&:to_i)
(1...N).each do |i|
    if A[i] > A[i-1]
```

```ruby
puts flag ? "Yes" : "No"
```

```ruby
S = gets.chomp
c = gets.chomp
found = false

S.each_char do |ch|
    if ch == c
        found = true
        break
    end
end
```
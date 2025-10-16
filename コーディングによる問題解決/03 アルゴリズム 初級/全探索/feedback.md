# 各言語ごとのメモ

## Python

## C++

## Java

## Javascript

## Ruby

|問題|コード|
|:--:|:--:|
|[整数Vの場所](https://algo-method.com/tasks/216)|[コード]()|
|[増加箇所の個数](https://algo-method.com/tasks/215)|[コード]()|

- `each`
- `each_with_index`
- `(1...N).each do |i|`

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
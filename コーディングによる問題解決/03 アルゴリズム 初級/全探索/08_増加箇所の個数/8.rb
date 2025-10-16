N = gets.to_i
A = gets.split.map(&:to_i)

cnt = 0
(1...N).each do |i|
    if A[i] > A[i-1]
        cnt += 1
    end
end

puts cnt
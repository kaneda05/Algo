N = gets.to_i
A = gets.split.map(&:to_i)

maxA = A.max
cnt = 0

A.each do |x|
    if x == maxA
        cnt += 1
    end
end

puts cnt
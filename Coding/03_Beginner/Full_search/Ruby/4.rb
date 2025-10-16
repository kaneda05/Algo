N = gets.to_i
A = gets.split.map(&:to_i)

cnt = 0

A.each do |x|
    if x > 0
        cnt += 1
    end
end

puts cnt
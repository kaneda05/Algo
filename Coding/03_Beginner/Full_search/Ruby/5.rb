N = gets.to_i
A = gets.split.map(&:to_i)

ans = -1

A.each do |x|
    if x > ans
        ans = x
    end
end

puts ans
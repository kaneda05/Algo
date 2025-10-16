N, V = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)

flag = false
ans = -1

A.each_with_index do |x, i|
    if x == V
        ans = i
        flag = true
    end
end

if flag
    puts ans
else
    puts -1
end
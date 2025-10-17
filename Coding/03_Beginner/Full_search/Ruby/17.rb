N = gets.to_i
A = gets.split.map(&:to_i)
cnt = 0

A.each do |x|
    if x >= 2
        flag = true
        (2...x-1).each do |j|
            if x % j == 0
                flag = false
                break
            end
        end
    end
    if flag
        cnt += 1
    end
end

puts cnt
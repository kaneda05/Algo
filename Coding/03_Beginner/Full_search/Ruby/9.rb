N = gets.to_i
flag = true

if N >= 2
    (2...N).each do |i|
        if N % i == 0
            flag = false
            break
        end
    end
else
    flag = false
end

puts flag ? "Yes" : "No"
N, M = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
B = gets.split.map(&:to_i)

cnt = 0
A.each do |a|
    B.each do |b|
        if a > b
            cnt += 1
        end
    end
end

puts cnt
N, V = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)

cnt = 0
A.each do |x|
    if x == V
        cnt += 1
    end
end
    
puts cnt
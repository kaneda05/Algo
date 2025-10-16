A, B = gets.split.map(&:to_i)
N = [A, B].min
ans = 0

(1..N).each do |i|
    if A % i == 0 && B % i == 0
        ans = i
    end
end

puts ans
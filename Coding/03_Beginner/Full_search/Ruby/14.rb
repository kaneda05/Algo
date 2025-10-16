S =gets.chomp
cnt = 0

(0...S.length - 1).each do |i|
    if S[i] == S[i+1]
        cnt += 1
    end
end

puts cnt
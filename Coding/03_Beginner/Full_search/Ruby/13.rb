S = gets.chomp
c = gets.chomp
found = false

S.each_char do |ch|
    if ch == c
        found = true
        break
    end
end

puts found ? "Yes" : "No"
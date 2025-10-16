N, V = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)

A.each do |x|
    if x == V
        puts "Yes"
        exit()
    end
end
    
puts "No"
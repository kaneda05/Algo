N = gets.to_i
cnt = 0

(1..N).each do |i|
  if i % 2 != 0 && i % 3 != 0 && i % 5 != 0
    cnt += 1
  end
end

puts cnt
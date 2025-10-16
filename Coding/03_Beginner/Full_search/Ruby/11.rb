N = gets.to_i
cnt = 0

(1..N).each do |i|
  if N % i == 0
    cnt += 1
  end
end

puts cnt
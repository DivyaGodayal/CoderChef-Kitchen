class Solutuon
	def fizz_buzz(n)
		arr = []
		(1..n).each do |i|
			if i%15 == 0
				arr << "FizzBuzz"
			elsif i%5 == 0
				arr << "Buzz"
			elsif i%3 == 0
				arr << "Fizz"
			else
				arr << i.to_s
			end
		end
		arr
	end
end


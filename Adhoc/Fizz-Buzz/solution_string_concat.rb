class Solutuon
  def fizz_buzz(n)
    str = ""
    (1..n).each do |i|
      if i%15 == 0
        str += "FizzBuzz"
      elsif i%5 == 0
        str += "Buzz"
      elsif i%3 == 0
        str += "Fizz"
      else
        str += i.to_s
      end
    end
    str
  end
end

Solutuon.new.fizz_buzz(15)

  
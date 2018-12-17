
twoDigits = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
singleDigit = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
tens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
class Solution:
    def smallBucket(self, string):
        if string < 10:
            return singleDigit[string]
        elif string < 20:
            return tens[string]
        elif string % 10 != 0:
            return "{} {}".format(twoDigits[string/10], singleDigit[string%10])
        else:
            return twoDigits[string/10]

    def recurse(self, num):
        if num == 0:
            return ""

        string_version = str(num)

        next_str = ""
        ans = ""
        if num < 1e2:
            return self.smallBucket(num)
        elif num < 1e3:
            next_str = self.recurse(int(string_version[-2:]))
            ans = self.recurse(int(string_version[:-2])) + " Hundred"
        elif num < 1e6:
            next_str = self.recurse(int(string_version[-3:]))
            ans = self.recurse(int(string_version[:-3])) + " Thousand"
        elif num < 1e9:
            next_str = self.recurse(int(string_version[-6:]))
            ans = self.recurse(int(string_version[:-6])) + " Million"
        else:
            next_str = self.recurse(int(string_version[-9:]))
            ans = self.recurse(int(string_version[:-9])) + " Billion"

        if next_str:
            ans += " " + next_str

        return ans


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        return self.recurse(num)
        

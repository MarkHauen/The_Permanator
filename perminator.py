import sys

def applyCapPattern(word, pattern):
   wordArr = list(word)
   for i in range(0, len(word)):
       if pattern[i] == '1':
           wordArr[i] = wordArr[i].upper()
   return ''.join(wordArr)

def allPatterns(w):
   return [bin(x).replace("0b", "").zfill(len(w)) for x in range(0, int('1' * len(w), 2) + 1)]

def main(word):
   x = [print(applyCapPattern(word, x)) for x in allPatterns(word)]
   print(len(x))

if __name__ == '__main__':
   main(sys.argv[1])

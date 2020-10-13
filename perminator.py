import sys

word = sys.argv[1]
l = len(word)

def applyCapPattern(word, pattern):
   wordArr = list(word)
   for i in range(0, l):
       if pattern[i] == '1':
           wordArr[i] = wordArr[i].upper()
   return ''.join(wordArr)

def allPatterns():
   return [bin(x).replace("0b", "").zfill(l) for x in range(0, int('1' * l, 2) + 1)]

def main():
   x = [applyCapPattern(word, x) for x in allPatterns()]
   for z in x:
       print(z)
   print(len(x))

if __name__ == '__main__':
   main()

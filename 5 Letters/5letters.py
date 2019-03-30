#selects the 5 characters-long words and writes them in the solo5.txt file
print ("Selecting 5 characters long words")
filepath = 'dictionary.txt'
solo = open ('solo5.txt', 'w')
with open(filepath) as fp:
   line = fp.readline()
   while line:
       if len(line) == 6:
           solo.write(format( line.strip()))
           solo.write("\n")
       line = fp.readline()
print ("DONE, closing files")
fp.close()
solo.close()
print ("Files closed\n")

#searches between the solo5.txt the palindrome words and writes the in palindrome.txt
print ("Searching palindromes in the 5 characters long words")
filepath = 'solo5.txt'
pali = open ('palindrome.txt', 'w')
with open(filepath) as fp:
   line = fp.readline()
   while line:
       if str(line[0:5]) == str(line[0:5])[::-1]:
           pali.write(format( line.strip()))
           pali.write("\n")
       line = fp.readline()
print ("DONE, closing files")
pali.close()
fp.close()
print ("Files closed\n")

#from the solo5.txt picks the words which exist backwards and writes them in reversables.txt
print ("Searching reversables words")
uno = open ('solo5.txt', 'r')
due = open ('solo5.txt', 'r')
inverty = open ('reversables.txt','w')
luno = uno.readline()
ldue = due.readline()
while luno:
    while ldue:
        if luno[0:5] == ldue[0:5][::-1]:
            inverty.write(format(luno.strip()))
            inverty.write("\n")
        ldue = due.readline()
    due.seek(0, 0)
    ldue = due.readline()
    luno = uno.readline()
print ("DONE, closing files")
uno.close()
due.close()
inverty.close()
print ("Files closed\n")

# picking from reversables.txt and palindrome.txt bruteforces the sator squares and verifies them
# next they are printed on the screen
print ("Sator Square Bruteforcing")
uno = open ('reversables.txt', 'r')
due = open ('reversables.txt', 'r')
pali = open('palindrome.txt', 'r')

luno = uno.readline()
ldue = due.readline()
lpali = pali.readline()

while luno:
 while ldue:
  while lpali:
   if lpali[0] == luno[2]:
    if lpali[1] == ldue[2]:
     if luno[1] == ldue[0]:
      if luno[3] == ldue[4]:
       print ("--------")
       print (luno [0:5])
       print (ldue [0:5])
       print (lpali [0:5])
       print (ldue[0:5][::-1])
       print (luno[0:5][::-1])
   lpali = pali.readline()
  pali.seek (0, 0)
  lpali = pali.readline()
  ldue = due.readline()
 due.seek (0, 0)
 ldue = due.readline()
 luno = uno.readline()

print ("\nDONE, closing files")
uno.close()
due.close()
pali.close()
print ("Files closed\n")

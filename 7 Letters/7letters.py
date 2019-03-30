#selects the 7 characters-long words and writes them in the solo7.txt file
print "Selecting 7 characters long words"
filepath = 'dictionary.txt'
solo = open ('solo7.txt', 'w')
with open(filepath) as fp:
   line = fp.readline()
   while line:
       if len(line) == 8:
           solo.write(format( line.strip()))
           solo.write("\n")
       line = fp.readline()
print "DONE, closing files"
fp.close()
solo.close()
print "Files closed\n"

#searches between the solo7.txt the palindrome words and writes the in palindrome.txt
print "Searching palindromes in the 7 characters long words"
filepath = 'solo7.txt'
pali = open ('palindrome.txt', 'w')
with open(filepath) as fp:
   line = fp.readline()
   while line:
       if str(line[0:7]) == str(line[0:7])[::-1]:
           pali.write(format( line.strip()))
           pali.write("\n")
       line = fp.readline()
print "DONE, closing files"
pali.close()
fp.close()
print "Files closed\n"

#from the solo7.txt picks the words which exist backwards and writes them in reversables.txt
print "Searching reversables words"
uno = open ('solo7.txt', 'r')
due = open ('solo7.txt', 'r')
inverty = open ('reversables.txt','w')
luno = uno.readline()
ldue = due.readline()
while luno:
    while ldue:
        if luno[0:7] == ldue[0:7][::-1]:
            inverty.write(format(luno.strip()))
            inverty.write("\n")
        ldue = due.readline()
    due.seek(0, 0)
    ldue = due.readline()
    luno = uno.readline()
print "DONE, closing files"
uno.close()
due.close()
inverty.close()
print "Files closed\n"

# picking from reversables.txt and palindrome.txt bruteforces the sator squares and verifies them
# next they are printed on the screen
print "Sator Square Bruteforcing"
uno = open ('reversables.txt', 'r')
due = open ('reversables.txt', 'r')
tre = open ('reversables.txt', 'r')
pali = open('palindrome.txt', 'r')

luno = uno.readline()
ldue = due.readline()
ltre = tre.readline()
lpali = pali.readline()

while luno:
    while ldue:
        while ltre:
            while lpali:
             if lpali[0] == luno[3]:
              if lpali[1] == ldue[3]:
               if lpali[2] == ltre[3]:
                if luno[1] == ldue [0]:
                 if luno[2] == ltre [0]:
                  if ldue[2] == ltre[1]:
                   if luno[4] == ltre[6]:
                    if luno[5] == ldue[6]:
                     if ldue[4] == ltre[5]:
                         print ("--------")
                         print (luno [0:7])
                         print (ldue [0:7])
                         print (ltre [0:7])
                         print (lpali [0:7])
                         print (ltre [0:7][::-1])
                         print (ldue[0:7][::-1])
                         print (luno[0:7][::-1])
             lpali = pali.readline()
            pali.seek (0, 0)
            lpali = pali.readline()
            ltre = tre.readline()
        tre.seek (0, 0)
        ltre = tre.readline()
        ldue = due.readline()
    due.seek (0, 0)
    ldue = due.readline()
    luno = uno.readline()

print "\nDONE, closing files"
uno.close()
due.close()
pali.close()
print "Files closed\n"

'''
सभी popular programming languages की तरह python भी file handling के लिए support provide करती है। इसके लिए python में कई methods available है।

Python के द्वारा file handling ability provide किये जाने की कई advantages होते है।

आप disk पर available files को access और modify कर सकते है।
बहुत सारा data जिसे manually insert किया जाना संभव नहीं होता है तो उसे directly file से input के रूप में read किया जा सकता है।
बहुत सारा data जिसे की screen पर देखा जाना संभव नहीं है आसानी से file में store किया जा सकता है और उसे बाद में analyse किया जा सकता है।

obj = open(‘file’,’mode’)     #Opens a file in given mode
    modes:-
    r= read
    w= write
    a= append
    rb = read binary
    wb = write binary


fileObj.read(size-in-bytes)    #reads given number of bytes

readline()
यह method file में से एक बार में एक ही line read करता है। Line string के रूप में read की जाती है और उसके आखिर में automatically new line character (n) add कर दिया जाता है।

write()
    यह method argument के रूप में string को लेता है और उसे file में write करता है। इसके बाद यह method characters की सँख्या return करता है जो की file में write किये गए है।

    fileObj.write(‘content-to-write’)   #write passed given string to file

'''

# Python code to illustrate read() mode
file = open("file.text", "r")
print (file.read())

# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print (file.read(5))


# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

# Python code to illustrate append() mode
file = open('geek.txt','a')
file.write("This will add this line")
file.close()

# Python code to illustrate split() function
with open("file.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)


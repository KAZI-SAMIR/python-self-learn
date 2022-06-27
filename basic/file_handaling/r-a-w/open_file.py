
#f = open('file.txt')
with open('file.txt') as f:

 txt = f.read().splitlines()
                    #f.read() #f.read(10)
     	 	    #_readline()_: read only the first line
		    #_readlines()_: read all the text line
		    #all the lines as a list is using _splitlines()_:

 print(type(txt))
 print(txt)
 f.close()

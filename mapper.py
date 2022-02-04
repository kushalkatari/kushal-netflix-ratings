import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) ==2) : 
    title,userscore = datalist

    # print intermediate key-value pairs to standard output
    print(userscore,"\t",1)

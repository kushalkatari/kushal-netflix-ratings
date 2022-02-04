import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) ==2) : 
    title,user rating score = datalist

    # print intermediate key-value pairs to standard output
    print(user rating score,"\t",1)

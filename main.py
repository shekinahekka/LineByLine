def readingLines():
    fileName= input("Enter the file name of the file: ")
    with open(fileName, 'r') as a:
        count=0
        while True:
          count += 1
          line = a.readline()
 
          if not line:
            break
          print("Line{}: {}".format(count, line.strip()))
    with open(fileName, 'r') as a:
        count=0
        for line in a:
          count += 1
          print("Line{}: {}".format(count, line.strip()))
          data_a = a.read()
    
    print("Data in " + fileName + ": " + data_a)

readingLines()
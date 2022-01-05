

def count_batteries_by_usage(cycles):
  lowCount,mediumCount,highCount = 0,0,0

  for each_element in cycles:
        if each_element <=400:
            lowCount == each_element
            lowCount+=1 
            print("Lowcounts of battery are") 
            print(lowCount) 
        elif (each_element>=401 and each_element<=919): 
            mediumCount == each_element
            mediumCount+=1 
            print("mediumCount of battery are") 
            print(mediumCount)
        elif (each_element>919): 
            highCount == each_element
            highCount+=1 
            print("highCount of battery are") 
            print(highCount)         

  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
 
  print("Done counting :)")

if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()

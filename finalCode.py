# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today we will be doing data analysis on the sales of over 16,500 video games
# We will use this data set from kaggle: https://www.kaggle.com/gregorut/videogamesales

# Here is the question we are trying to answer: Which game publisher dominates the global video game market?
# How about the North American, European, and Japan markets?

# This information could be useful in many different ways. If I wanted to invest in a game publisher, and
# the European market is expected to outgrow the others, it would be useful knowing which game publisher
# dominates that market.

# First lets download that data set as a .csv. It may be downloaded as a zip, so pull it out of the zip
# Next lets import it. I will show you how to do this on repl, as we did it on pycharm last time.
# Next to the files section there is 3 dots, click it and go to upload file. Select the data set.
# Now we can import pandas and read the csv file.


import pandas as pd
dataset = pd.read_csv(r'C:\Users\matth\Downloads\vgsales.csv')
# For repl.it:   dataset = pd.read_csv(r'vgsales.csv')
print(dataset)

# Now that it is imported, there are many different ways to accomplish the task. Basically we look at each
# game and find the game publisher. Then we add up that games sales to the game publishers total sales.

# There are many ways we can approach this method, but we will do something similar to what we did last week with the
# girls and boys shoes.

# First lets make a list of all the game publishers. Each element in the list will be a another list, 2D array,
# that way we can put a counter variable next to the game publisher that will hold the running total.
# [[microsoft, 12220], [ubisoft, 99877],...] This way we can access the element easier and have some organization

# However, there are many game publishers so it would take a while. We can just make an empty list, and add a game
# publisher every time a new game publisher is discovered. If it is already in the list, we just add the sales.

publishers = []

# Now we want to traverse each row (game), and add its sales/publisher to the list. After we are done traversing, we should have an array of all the game publishers with thier total global sales

for i in range(len(dataset)):                                     #1
  row = dataset.iloc[i]                                 #1
  publisher = row[5]                                  #1
  globalSales = row[10]                         #1
  northAmericaSales = row[6]                                                                                # 4
  europeanSales = row[7]                                                                                       #4
  japanSales = row[8]                                                                                         #4
  isInArrayAlready = False                                                                  #2
  for i in publishers:                                  #1
    if i.__contains__(publisher):                                 #1
      i[1] += globalSales                                 #1
      i[2] += northAmericaSales                                                                                     #4
      i[3] += europeanSales                                                                                     #4
      i[4] += japanSales                                                                                      #4
      isInArrayAlready = True                                                                 #2
  if(not isInArrayAlready):                    #2
    publishers.append([publisher, globalSales, northAmericaSales, europeanSales, japanSales])                 #4

  #publishers.append([publisher, globalSales])                                                 2


#final = pd.DataFrame(publishers, columns=["Publisher", "Total Sales"])           #3
final = pd.DataFrame(publishers, columns=["Publisher", "Total Sales", "North America Sales", "European Sales", "Japan Sales"])
final = final.sort_values("Total Sales", ascending = False)                     #3
print(final)                                  #3
topTen = final.iloc[0:10]                                 #3
print(topTen)                                 #3

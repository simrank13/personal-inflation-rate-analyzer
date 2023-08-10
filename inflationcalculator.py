#use constant to convert decimal into percentage
PERCENTAGE = 100

#prompt user to enter year to calculate personal interest for
personalInterest = int(input('Please enter the year that you want to calculate the personal interest rate for: '))

#prompt user to enter number of expense categories
numCategories = int(input('Please enter the number of expenditure categories: '))

# initialize and declare prevYear and interest variable as 0
#prompt user to enter expenses of previous year and year of interest numCategories number of times in a loop
prevYear=0
interest = 0
for i in range(numCategories):
    i += numCategories
    prevYear += float(input('Please enter expenses for previous year: '))
    interest += float(input('Please enter expenses for year of interest: '))

#inflation rate equation that will calculate inflation rate
infRate = ((interest - prevYear) / interest) * PERCENTAGE

#print the inflation rate
print(f'Personal inflation rate for {personalInterest} is {infRate:.1f}% ')

#determine the type of inflation
#if inflation rate is less than 3 percents, its low
#if inflation rate is greater than 3 and less then 5, its moderate
#if inflation rate is greater than 5 but less than 10, its high
#if inflation rate is greater than 10, then its hyper
if infRate < 3:
    print('Type of Inflation: Low')
elif infRate > 3 and infRate < 5:
    print('Type of Inflation: Moderate')
elif infRate > 5 and infRate < 10:
    print('Type of Inflation: High')
else:
    print('Type of Inflation: Hyper')
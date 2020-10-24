## RAINFALL STATISTICS
import sys

def main():
    month_names = ['January' ,'Febuary' ,'March' ,'April' ,'May' ,'June' ,'July' ,'August' ,'September' ,'Ocotber' ,'November' ,'December']

    num_months = 12
    rain_list = []
    count = 0

    while count <= num_months:
        count += 1

        for month in month_names:
            monthly_rain = float(input("Please enter the rainfall amount for " + month + ": "))
            
            rain_list.append(monthly_rain)
            count += 1

    if count > 12:
        total_rain = sum(rain_list)
        average_rain = total_rain / len(rain_list)
        max_rain = max(rain_list)
        min_rain = min(rain_list)
        print('_'*75)
        print('Total:',total_rain,'\n', 'Average:',average_rain,'\n', 'Highest:',max_rain,'\n', 'Lowest:',min_rain)
        print('_'*75)
        sys.exit()

    else:
        print("ERROR")
        sys.exit()

main()

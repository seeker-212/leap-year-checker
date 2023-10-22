



def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
           if year % 400 == 0:
               print('Leap Year')
           else:
               print('Not Leap Year')
        else:
            print("Leap Year")
    else:
        print("Not leap Year")

is_leap_year(2000)
print("Hollywood Movie Rating Guide")

quit = 0
one = 0
two = 0
three = 0
four = 0
five = 0
attempts = 0

star_value = int(input("Enter a star from 1 to 5, 1 is the lowest and 5 is the highest, or 0 to quit: "))

while star_value != quit:
  if(star_value < 1 or star_value > 5):
    
    attempts = attempts + 1
    if attempts == 1:
      input(f"Attempt: {attempts}")
      star_value = int(input("Invalid input. Enter a star from 1 to 5, 1 is the lowest and 5 is the highest, or 0 to quit: "))
    elif attempts == 2:
      input(f"Attempts: {attempts}")
      star_value = int(input("Invalid input. Enter a star from 1 to 5, 1 is the lowest and 5 is the highest, or 0 to quit: "))
    elif attempts == 3:
      input(f"Attempts: {attempts}")
      input(f"Wait for 5 minutes to rate again in this account. Next, please.")
      star_value = 0
      
  else:
    star_value = int(input("Enter a star from 1 to 5, 1 is the lowest and 5 is the highest, or 0 to quit: "))
    if star_value == 1:
      one += 1
    elif star_value == 2:
      two += 1
    elif star_value == 3:
      three += 1
    elif star_value == 4:
      four += 1
    elif star_value == 5:
      five += 1

total_ratings = one + two + three + four + five
# * In the expression (one + 2 * two + 3 * three + 4 * four + 5 * five), you're adding up the weighted sum of all the ratings. For example, 2 * two means that the number of "two-star" ratings is multiplied by 2 to give them a higher weight. Similarly, 3 * three means that the number of "three-star" ratings is multiplied by 3 to give them an even higher weight, and so on.
average_rating = (one + 2 * two + 3 * three + 4 * four + 5 * five) / total_ratings if total_ratings > 0 else 0

print("Average star rating for the movie:")
print("Five star:", five)
print("Four star:", four)
print("Three star:", three)
print("Two star:", two)
print("One star:", one)
print("Average rating:", average_rating)

print("Thank you for using the Hollywood Movie Rating Guide!")
# Hollywood Movie Rating Guide

Instructions: 
  A. Design a program for the Hollywood Movie Rating Guide, which can be installed in a kiosk in theaters. Each theater patron guides featured indicating the number of stars that the patron awards to the guide's featured movie of the week. If a user enters a star value that does not fall in the correct range, reprompt the user continuously until a correct value is entered. The program executes continuously until the theater manager enters a negative number to quit. At the end of the program, display the average star rating for the movie.

  B. Modify the movie-rating program so that a user gets three tries to enter a valid rating. After three incorrect entries, the program issues an appropriate message and continues with a new user.

Pseudocode:




            BEGIN
              DECLARE quit = 0
              DECLARE one = 0
              DECLARE two = 0
              DECLARE three = 0
              DECLARE four = 0
              DECLARE five = 0
              DECLARE attemps = 0

              <!-- WHILE  -->

              PRINT "Enter a star from 1 to 5, 1 is the lowest and 5 is the highest"
              INPUT star_value

              WHILE star_value is not equal to quit

                IF star_value is not equals to range



                  attemps = attemps + 1
                  IF attempts equals to 1
                    PRINT "ATTEMPT" concatenate with the current attempt
                    PRINT "Enter a star from 1 to 5, 1 is the lowest and 5 is the highest"
                    INPUT star_value
                  ELSE IF attempts equals to 2
                    PRINT "ATTEMPT" concatenate with the current attempt
                    PRINT "Enter a star from 1 to 5, 1 is the lowest and 5 is the highest"
                    INPUT star_value
                  ELSE IF attempts equals to 3
                    PRINT "ATTEMPT" concatenate with the current attempt
                    PRINT "Wait for 5 minutes to rate again in this account. Next, please."
                    DECLARE star_value equals to 0 - to end the loop

                ELSE

                  IF star_value equals to 1
                    one = one + 1
                  ELSE IF star_value equals to 2
                    two = two + 1
                  ELSE IF star_value equals to 3
                    three = three + 1
                  ELSE IF star_value equals to 4
                    four = four + 1
                  ELSE IF star_value equals to 5
                    five = five + 1
                  ENDIF 

                ENDIF

              ENDWHILE

              DECLARE total_ratings = one + two + three + four + five
              DECLARE average_rating = (one + 2 * two + 3 * three + 4 * four + 5 * five) / total_ratings if total_ratings > 0 else 0
              PRINT "Average of star rating for a movie "
              PRINT "Movie: John Wick 4 ratings "
              PRINT "Five star: " five
              PRINT "Four star: " four
              PRINT "Three star: " three
              PRINT "Two star: " two
              PRINT "One star: " one
              PRINT "Average rating:" average_rating
              
            END
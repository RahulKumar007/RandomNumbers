# RandomNumbers
Using linear congruential generator algo to generate numbers which are 73% biased to higher numbers.


Inner Process
1.> First we obtain the lower bound, upper bound and total numbers to be generated from the user.

2.> We then call the parallel() function which then uses threads to call further 2 functions lower() and higher() which generate lower and higher numbers respectively.

3.> lower() function specifically generates only 27% of the total numbers (less than the middle element).

4.> higher() function generates 73% of the numbers (greater than the middle element). 

5.> lower() and higher() both call the random() function which uses lcg algo to generate and return a random number which is then modified according to the function called. i.e. converted to lower in lower() and higher in higher().

6.> The lcg algo used in the random function is defined by the recurrence relation:

          X_n+1=(aX_n+c)  X_n+1=(aX_n+c) 
          where  X X is the sequence of pseudorandom values, and
          m , 0 < m  – the "modulus"
          a , 0 < a < m – the "multiplier"
          c , 0 <= c < m – the "increment"
          X_0 , 0 <= X_0 < m – the "seed" or "start value"


Example

          Enter the lower bound :
          1
          Enter the upper bound : 
          10
          Enter the length of the series : 
          100
          The random number series is : 

          4 , 1 , 1 , 4 , 2 , 1 , 3 , 3 , 4 , 4 , 2 , 2 , 3 , 2 , 4 , 5 , 1 , 2 , 2 , 3 , 4 , 2 , 2 , 4 , 1 , 2 , 4 , 10 , 6 , 7 , 6 ,           9 , 8 , 9   , 7 , 10 , 8 , 8 , 6 , 8 , 9 , 7 , 7 , 6 , 10 , 6 , 7 , 7 , 8 , 7 , 7 , 9 , 9 , 10 , 6 , 10 , 7 , 6 , 9 , 7 , 6 ,           9 , 10 , 6 , 6 , 8 ,   6 , 7 , 9 , 9 , 6 , 8 , 7 , 8 , 9 , 6 , 8 , 6 , 6 , 9 , 8 , 6 , 10 , 6 , 6 , 9 , 10 , 9 , 8 , 9 , 6 ,           9 , 9 , 9 , 9 , 9 , 7 , 8 , 8 ,   6 ,

          Process finished with exit code 0

Total 27 lower and 73 greater numbers.


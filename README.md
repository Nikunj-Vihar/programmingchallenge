# programmingchallenge
Problem statement : Given a matrix of N*M, and R as repetition count find the number in the matrix that is repeated R times.

Steps :
                - Get the bounds of the matrix from the user (values for N and M). 
                - Get the values for the matrix from the user (values for a[0][0] to a[n-1][m-1]).
                - Get the repetition count from the user (value for R).
                - Find the number in the matrix which is repeated R times. 
                - Display the number to the user. 
                
Sample :
                matrix[N][M] =     {{1, 2, 1, 1}, 
                                   {2, 2, 2, 2}, 
                                   {3, 5, 50, 3}, 
                                   {4, 40, 49, 41},
                                   {14, 140, 249, 341}}; 

                R = 5
                Output = 2           
                Reason = 2 is repeated 5 times in the matrix. 
                
                R = 3
                Output = 1           
                Reason = 1 is repeated 3 times in the matrix. 

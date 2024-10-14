# AlMamaari_Alaiham    December 2023    
'''
Simulates a theater's ticket sales for two seating categories (Band A and Band B).
Calculates the revenue generated from a **Full House** and a **Part House** seating arrangement.
Computes the break-even point for both seating arrangements and provides detailed row-by-row analysis for the Part House.
'''


def input_func():
    production_cost = int(input("Enter the production cost: "))
    Band_A_cost = int(input("Enter the price of a band A seat: "))
    Band_B_cost = int(input("Enter the price of a band B seat: "))
    return production_cost , Band_A_cost , Band_B_cost

# Function to initialise a 4x5 Full House array.
def FH_array_func():
    Full_house_array =  [ [1] * 5 for i in range(4) ]
    return Full_house_array

# Function to initialise a 4x5 Part House array.
def PH_array_func():
    import random
    Part_house_array =  [ [1] * 5 for i in range(4) ]
    for row in range(4):   #iterate throught the 4 rows
        for col in range(5):  #for each element in row:
            Part_house_array[row][col] = random.randint(0, 1)   # assign 1 or 0 randomly
    return Part_house_array
    

# Function to calculate revenue and seats sold for Band A and Band B in Full House.
def FH_Band_process_func(Full_house_array,Band_A_cost,Band_B_cost):
    #Band A:
    Sum_Band_A_FH = 0
    for row in Full_house_array[:2]:  #only first 2 rows (Band A)
        for col in row:
            Sum_Band_A_FH = Sum_Band_A_FH + col  #get the sum of seats booked
            Band_A_revenue_FH = Sum_Band_A_FH * Band_A_cost
    #Band B:
    Sum_Band_B_FH = 0
    for row in Full_house_array[-2:]:   # last 2 rows (Band B)
        for col in row:
            Sum_Band_B_FH = Sum_Band_B_FH + col
            Band_B_revenue_FH = Sum_Band_B_FH * Band_B_cost
    
    return Sum_Band_A_FH ,Band_A_revenue_FH ,Sum_Band_B_FH ,Band_B_revenue_FH


# Function to calculate total revenue and break-even point for Full House
def FH_total_process_func(Band_A_revenue_FH ,Band_B_revenue_FH ,production_cost):
    import math  # to round revenue up
    Total_revenue_FH = Band_A_revenue_FH + Band_B_revenue_FH  #total for full house
    Break_even_FH = math.ceil(production_cost / Total_revenue_FH)  # find break-even and round num up.

    return  Total_revenue_FH ,Break_even_FH


# Function to calculate revenue and seats sold for Band A and Band B in Part House.
def PH_Band_process_func(Part_house_array,Band_A_cost,Band_B_cost):
    #Band A:
    Sum_Band_A_PH = 0
    for row in Part_house_array[:2]:   #first 2 rows
        for col in row:
            Sum_Band_A_PH = Sum_Band_A_PH + col
            Band_A_revenue_PH = Sum_Band_A_PH * Band_A_cost

    #Band B:
    Sum_Band_B_PH = 0
    for row in Part_house_array[-2:]:   #last 2 rows
        for col in row:
            Sum_Band_B_PH = Sum_Band_B_PH + col
            Band_B_revenue_PH = Sum_Band_B_PH * Band_B_cost

    return Sum_Band_A_PH ,Band_A_revenue_PH ,Sum_Band_B_PH ,Band_B_revenue_PH


# Function to calculate total revenue and break-even point for Part House.
def PH_total_process_func(Band_A_revenue_PH ,Band_B_revenue_PH ,production_cost):
    import math
    Total_revenue_PH = Band_A_revenue_PH + Band_B_revenue_PH   #total for part house
    Break_even_PH = math.ceil(production_cost / Total_revenue_PH)   #find break-even and round num up.
    
    return Total_revenue_PH ,Break_even_PH


# Function to output num of seats sold, total revenue, and break-even for Full house.
def FH_output_func(production_cost , Band_A_cost , Sum_Band_A_FH ,  Band_B_cost , Sum_Band_B_FH ,Total_revenue_FH ,Break_even_FH):
    print("\nThe production cost:","£",production_cost,"\n")
    print("-Full house revenue: ")
    print("  Band_A:","num of seats sold at £",Band_A_cost,"per seat: ",Sum_Band_A_FH)
    print("  Band_B:","num of seats sold at £",Band_B_cost,"per seat: ",Sum_Band_B_FH)
    print("  Total Revenue: ","£",Total_revenue_FH)
    print("  Number of shows to break-even:",Break_even_FH)

# Function to output num of seats sold, total revenue, and break-even for Part house.
def PH_output_func(Band_A_cost , Sum_Band_A_PH ,  Band_B_cost , Sum_Band_B_PH ,Total_revenue_PH ,Break_even_PH):
    print("-Part house revenue: ")
    print("  Band_A:","num of seats sold at £",Band_A_cost,"per seat: ",Sum_Band_A_PH)
    print("  Band_B:","num of seats sold at £",Band_B_cost,"per seat: ",Sum_Band_B_PH)
    print("  Total Revenue: ","£",Total_revenue_PH)
    print("  Number of shows to break-even:",Break_even_PH)


# Function to output Full House and Part House seating plans.  
def seating_output_func(Full_house_array , Part_house_array ):
    print("\n-Full house seating plan:")
    for row in Full_house_array:
        for element in row:
            print(element,end=" ")  #space after each element
        print()  #new line for new row.
        
    print("\n-Part house seating plan:")
    for row in Part_house_array:
        for element in row:
            print(element,end=" ")
        print()

# Function to analyze rows in Part House.
def PH_rows_analysis_func(Part_house_array , Band_A_cost ,Band_B_cost):
    print("\n-Part house rows analysis: ")
    #for the first 2 rows (Band A):
    row_num = 1  #to be used to indicate row number
    
    for row in Part_house_array[:2]:   #take the first 2 rows (Band A)
        Sum_row_Band_A = 0   # sum of that row is initially 0  , after 1st row calculated, reset to 0
    
        for col in row:  #calculate that row only
            Sum_row_Band_A = Sum_row_Band_A + col    #add 1 if seat is booked , 0 if not
            Band_A_row_revenue = Sum_row_Band_A * Band_A_cost
        #output for the current row:    
        print("num of seats in row ",row_num,"is:",Sum_row_Band_A)
        print("income from row ",row_num,"is:","£",Band_A_row_revenue)
        print()
        row_num = row_num +1    
    #For the last 2 rows (Band B):
    row_num = 3
    for row in Part_house_array[-2:]:   #take the last 2 rows (Band B)
        Sum_row_Band_B = 0 # sum of that row is initially 0  , after 1st row calculated, reset to 0
        for col in row:  #iterate through row
            Sum_row_Band_B = Sum_row_Band_B + col
            Band_B_row_revenue = Sum_row_Band_B * Band_B_cost
        #output for the current row: 
        print("num of seats in row ",row_num,"is:",Sum_row_Band_B)
        print("income from row ",row_num,"is:","£",Band_B_row_revenue)
        print()
        row_num = row_num +1


# Main function to control the flow of the program.
def main():
    #get inputs from user:
    production_cost , Band_A_cost , Band_B_cost = input_func()
    #initialise FH and PH arrays:
    Full_house_array = FH_array_func()
    Part_house_array = PH_array_func()
    #Process for FH:
    Sum_Band_A_FH ,Band_A_revenue_FH ,Sum_Band_B_FH ,Band_B_revenue_FH = FH_Band_process_func(Full_house_array,Band_A_cost,Band_B_cost)
    Total_revenue_FH ,Break_even_FH = FH_total_process_func(Band_A_revenue_FH ,Band_B_revenue_FH ,production_cost)
    #Process for PH:
    Sum_Band_A_PH ,Band_A_revenue_PH ,Sum_Band_B_PH ,Band_B_revenue_PH = PH_Band_process_func(Part_house_array,Band_A_cost,Band_B_cost)
    Total_revenue_PH ,Break_even_PH = PH_total_process_func(Band_A_revenue_PH ,Band_B_revenue_PH ,production_cost)
    #Outputs for FH and PH:
    FH_output_func(production_cost , Band_A_cost , Sum_Band_A_FH , Band_B_cost , Sum_Band_B_FH ,Total_revenue_FH ,Break_even_FH)
    PH_output_func( Band_A_cost , Sum_Band_A_PH , Band_B_cost , Sum_Band_B_PH ,Total_revenue_PH ,Break_even_PH)
    # output FH,PH seatings + PH rows analysis:
    seating_output_func(Full_house_array , Part_house_array )
    PH_rows_analysis_func(Part_house_array , Band_A_cost ,Band_B_cost)

# Execute the main function to start the program.
main()



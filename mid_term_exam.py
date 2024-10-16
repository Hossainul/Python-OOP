class Star_Cinema:
    _hall_list = []

    def entry_hall(self,hall):
        Star_Cinema._hall_list.append(hall)
       
    
class Hall(Star_Cinema):
    def __init__(self,row,cols,hall_no):
        self._row = row
        self._cols = cols
        self.__hall_no = hall_no
        self.seats = {}
        self.show_list = []

        self.entry_hall(self)

    @property
    def hall_no(self):
        return self.__hall_no

    def entry_show(self,id,movie_name,time):
        self.id = id
        self.movie_name = movie_name
        self.time = time 

        show =(id,movie_name,time)
        self.show_list.append(show)

        seats_for_show = [["0" for _ in range(self._cols)] for _ in range(self._row)]
        self.seats[id] = seats_for_show

    def seats_book(self,show_id,row,cols):
        if show_id in self.seats:
            if((row >= 0 and row < self._row) and (cols >= 0 and cols < self._cols)):
                if(self.seats[show_id][row][cols] == '1'):
                    print("This seat is already booked !\n Please try another one.")
                else:
                    self.seats[show_id][row][cols] = '1'
                    print(f'You booked {row} x {cols} seat successfully!')
            else :
                print('invalid row or column')
       

    def view_show_list(self):
        for show in self.show_list:
            print(f'Show id : {show[0]} Movie Name: {show[1]} Time : {show[2]}')


    def view_available_seats(self,show_id):
        self.show_id = show_id

        if(show_id in self.seats):
            for i in range(self._row):
                for j in range(self._cols):
                    print(self.seats[show_id][i][j],end = " ")
                print('\n')
        else:
            print('You entered wrong show id')




sony = Star_Cinema()

hall_1 = Hall(7,8,1)
hall_2 = Hall(5,6,2)
hall_3 = Hall(4,5,3)

hall_1.entry_show(101,'Joker 2','12.00 pm')
hall_1.entry_show(102,'Joker 3','13.00 pm')
hall_1.entry_show(103,'Joker 4','14.00 pm')

hall_2.entry_show(105,'spider Man','14.00 pm')
hall_3.entry_show(104,'Spider man away from home','14.00 pm')


type = True
while(type):
    print("Here is your all options :")
    print("Option 1 : All running show")
    print("Option 2 : All available seats")
    print("Option 3 : seats booking")
    print("Option 4 : Exit")
    
    ch = int(input("Enter your Option : \n"))

    if(ch == 1):
        if Star_Cinema._hall_list:
            for hall in Star_Cinema._hall_list:
                print(f'\nHere all moive list in the hall no: {hall.hall_no}:')
                hall.view_show_list()
                print()

    elif(ch == 2):
        movie_id = int(input("Enter your movie id : \n"))
        isfound = False
        if Star_Cinema._hall_list:
            for hall in Star_Cinema._hall_list:
                if movie_id in hall.seats:
                    print(f'All available seats for show id: {movie_id}')
                    hall.view_available_seats(movie_id)
                    isfound = True
                    break
            if(isfound == False):
                print("Invalid movie id !")
        else:
            print("No hall list exist!")
    elif(ch == 3):
        print("For booking Cinema tickes you need to give me following information :")
        howMany = int(input("How many tickest you want to buy ?!\n"))
        i = 1

        while(howMany > 0):
           print(f"Enter your {i} seats informations: ")
           show_id = int(input("Enter your show id : \n"))
           rowNo = int(input("Enter your row number : \n"))
           colNo = int(input("Enter your column number : \n"))

           isfound = False
           if Star_Cinema._hall_list:
                for hall in Star_Cinema._hall_list:
                    if show_id in hall.seats:
                        hall.seats_book(show_id,rowNo-1,colNo-1)
                        isfound = True
                        break
                if(isfound == False):
                    print("Invalid movie id !")

           howMany-=1
           i+=1
    else:
        type = False


            
                    
                
       

         
               



   
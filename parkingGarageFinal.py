class ParkingGarage():
    
    def __init__(self, tickets, parkingSpaces, currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets
        
        
        
    def makeChoice(self):
        toPark = input('Hello! Would you like to park, pay, or leave?')
        if toPark.lower() == 'park':
            self.takeTicket()
        elif toPark.lower() == 'pay':
            self.payForParking()
        elif toPark.lower() == 'leave':
            self.leaveGarage()
        elif toPark.lower() == 'quit':
            return
        
    def takeTicket(self):    
        if self.parkingSpaces == []:
            print("Sorry we're full at the moment, please come back later!")
            return
        usedTicket = self.tickets.pop(0)
        self.parkingSpaces.remove(usedTicket)
        self.currentTickets[usedTicket] = 'not paid'
        print(f'Available tickets: {self.tickets}')
        print(f'Available spaces: {self.parkingSpaces}')
        print(f' Ticket status:{self.currentTickets}')
        
        
    def payForParking(self):
        parking = input('Where are you parked?')
        if (self.currentTickets[int(parking)]) != '':
            input('Press anything for payment')
            self.currentTickets[int(parking)] = 'paid'
            print('Thank you for the payment! You have 15 Minutes to exit the garage!')
            print(self.tickets, self.parkingSpaces, self.currentTickets)
            
            
            
    def leaveGarage(self):
        parked = int(input('Where were you parked?'))
        if self.currentTickets[parked] == 'paid':
            if parked in self.parkingSpaces: 
                print("You have already left the garage.")
                return
            print('Goodbye, thank you!')
            returnedTicket = self.tickets.append(parked)
            self.parkingSpaces.append(parked)
            print(self.tickets, self.parkingSpaces, {})
        elif self.currentTickets[parked]=='not paid':
            print("Hey you haven't paid sucka! You ain't allowed to leave! Please pay first.")
            
            
car = ParkingGarage([1,2,3,4,5],[1,2,3,4,5],{})
while(1!=0):
    car.makeChoice()
#3 levels 
# A,B, C
# each level two lls car and bike

#vehicle parking= dict({'A':c,b, "B":c,b}, "C":c,b)

#capacity: 300 vehicles: each level 50 cars, 50 bikes
#cases
# order: C , B, A

# vehicle:  new node: [info,link]: link to the parking lot

class Park_Lot:
    def __init__(self,level,car_capacity,bike_capacity):
        self.level = level
        self.car_capacity=car_capacit


class Node:
    def __init__(self,data): #vehicle
        self.data=data
        self.link=None
class LinkedList:
    def __init__(self,head):
        self.head=head
    
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end="--->")
            temp=temp.link
        print("STOP")

first_car=Node(["Car","AS01DM0703",7.0])
second_car=Node(["Car","AS01E1234",8.0])
third_car=Node(["Car","AS01F0909",6.0])

first_car.link=second_car
second_car.link=third_car

ll=LinkedList(first_car)

#deletion of linked list


ll.print_list()

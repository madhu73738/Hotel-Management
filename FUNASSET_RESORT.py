
#IMPORTING MODULES 
import sys
import time

#Greetings
print('\t\t Welcome to FUNASSETS')
print('Here you get everything as good as heavens!\nWe provide you with the finest luxuries ever ')
name=(input("What's your name sir/mam: ")).capitalize()
msg='Well, so lets get started '+name

# Using typewriter effect
for i in msg :
 print(i,end='',flush=True)
 time.sleep(0.1)
print('')

# Resort Tour
print('Get to know our Resort better with a Resort Tour\n Our resort situated on the gorgeous Marine Drive, The Funasset offers you fabulous views of the ocean')

#Menu
print("""You can check out for the following:
      1. Room Tour 
      2. Room Facilities
      3. Resort Amenities
      4. Resort's Assistance
      5. Fooding or Meals
      6. Collaborated Tourism 
      7. Location or Address
      8. Exit  """)                               
menu_int=int(input('ENTER SERIAL NO. : '))

while menu_int!=8:
    if menu_int==1:       #Room Tour           
        print("""
          The Funasset is inside Europe's tallest building. With amazing Funasset service, seriously luxurious accommodations and some great drinking and dining, it's a perfect place for a  luxurious adventure.
          Spend a few nights in an Iconic City View Room and it had just that, iconic city views of India's biggest landmarks.

          Its also in a great location, just across the river from the Tower of Silence and Tower Bridge and with a Tube stop right underneath, it's easy to get to anywhere in the city within a few minutes.
          For a stay in April, the rooms, called Iconic City View Room because of the amazing view and because it's on a high floor.""")
        menu_int=int(input('Looking what else we got?\nENTER SERIAL NO. FROM THE MENU: '))

    elif menu_int==2:       #Room Facilities
    
        print("""_____Hotel Facilities & Guest Service_____

    ***Hotel Facilities***
    
    01.Spa
    02.Semi open & outdoor restaurant
    03.Poolside bar
    04.Car parking
    05.Swimming pool/Jacuzzi
    06.Public computer
    07.Disable rooms & Interconnecting rooms
    08.24 Hour security
    09.Outside catering service
    10.100 Seating capacity restaurant
    11.150 Capacity outdoor terrace
    12.45 Seating conference room
    13.35 Seating private air-conditioning dining room
    14.Water purification system
    15.Sunset boat trip
    16.Gift shop
    
    ***Guest Service***

    01.24-Hour room service
    02.Free wireless internet access
    03.Complimentary use of hotel bicycle
    04.Laundry service
    05.Tour & excursions
    06.24 Hour concierge
    07.Meeting facilities
    08.E-Bike & horse cart rental
    09.Airport transfers
    10.Babysitting on request
    11.24-Hour doctor on call""")
        menu_int=int(input('Looking what else we got?\nENTER SERIAL NO. FROM THE MENU: '))

    elif menu_int==3:       #Resort Amenities
        print("""THE FREE FACILITIES OF THE FUNASSET RESORT ARE:         
        1. 24 Hour security
        2. Car parking
        3. 100 Seating capacity restaurant
        4. 150 Capacity outdoor terrace
        5. 45 Seating conference room
        6. 35 Seating private air-conditioning dining room
        7. Water purification system
        8. Public computer
        9. Semi open & outdoor restaurant""")
        print('''SOME OF THE CHARGED FACILITIES OF THE FUNASSET RESORT:        
        1. Spa---->500/-
        2. Swimming pool/Jacuzzi---->200/-
        3. Poolside bar---->400/-
        4. Outside catering service---->100/-
        5. Gift shop---->1000/-
        6. Sunset boat trip---->500/-
        7. Disable rooms & Interconnecting rooms---->100/-
        8. Save and Exit''')
        
        m=int(input("Do you want to purchase from charged facilites:enter your choice[if yes type 1 and if no type 0 ]:" ))
        if(m==1):
            print("here we go")
            cart=0
            while(True!=8):
                d=int(input("enter your choice:"))
                if(d==1):
                    print("you have ordered spa")
                    price=500 
                    cart=cart+price
                    print("Your current total is:",cart,"\n")
                elif(d==2): 
                    print("you have ordered Swimming pool/Jacuzzi")
                    price=200
                    cart=cart+price
                    print("Your current total is::",cart,"\n")
                elif(d==3):
                    print("you have ordered Poolside bar")
                    price=400
                    cart=cart+price
                    print("Your current total is:",cart,"\n")
                elif(d==4):
                    print("you have ordered Outside catering service")
                    price=100
                    cart=cart+price
                    print("Your current total is:",cart,"\n")
                elif(d==5):
                    print("you have ordered Gift shop ")
                    price=1000
                    cart=cart+price
                    print("Your current total is:",cart,"\n")
                elif(d==6):
                    print("you have ordered Sunset boat trip")
                    price=500
                    cart=cart+price
                    print("Your current total is:",cart,"\n")
                elif(d==7):
                    print("you have ordered Disable rooms & Interconnecting rooms")
                    price=100
                    cart=cart+price
                    print("Your current total is:",cart,"\n")
                elif(d==8):
                    print("You will get all the ordered facilities and free facilities!thank you :)")
                    print("Your total amount is: ",cart,"\n")
                    break
                else:
                    print("please enter your choice from the menu")

        menu_int=int(input('Looking what else we got?\nENTER SERIAL NO. FROM THE MENU: '))

        
    elif menu_int==4:       #Resort's Assistance
            print("""We have the following rooms for you:-
         1.Double Room -          A room with the facility of double bed. 
                                  There are two king size bed.
                                  It is equipped with adequate furniture such as dressing table 
                                  and a writing table, a TV, and a small fridge.
                                  PRICE=RS 5000/-
         2.Deluxe Room -          It is well furnished. 
                                  Some amenities are attached bathroom, a dressing table,
                                  a bedside table, a small writing table, a TV, and a small fridge.
                                  The floor is covered with carpet and most suitable for small families.
                                  PRICE=RS 8000/-
         3.Studio Room -          They are twin adjacent rooms.
                                  A living room with sofa, coffee table and chairs, and a bedroom.
                                  It is also equipped with fan/air conditioner, a small kitchen corner,
                                  and a dining area. 
                                  The furniture is often compact.
                                  PRICE=RS 12000/-         
         4.Penthouse Suite Room - Luxurious than the regular suite.
                                  It is provided with the access to terrace space above the suite. 
                                  It is aloof from crowd and provides abird’s eye view of the city. 
                                  It has all the amenities and structure similar to a regular suite.
                                  PRICE=RS 15000/-
         5. Exit""")
        
            x=int(input("Enter Your Choice Please->"))
            if x>4 or x<1:
                print('Thank you!')
                sys.exit()
            n=int(input("For How Many Nights Did You Stay:"))
            cart=0
            if(x==1):
                print ("you have opted for DOUBLE ROOM")
                cart=1000*n
            elif (x==2):
                    print ("you have opted for DELUXE ROOM")
                    cart=2000*n
            elif (x==3):
                    print ("you have opted for STUDIO ROOM")
                    cart=3000*n
            elif (x==4):
                    print ("you have opted for PENTHOUSE SUITE ROOM")
                    cart=4000*n
            elif (x==5):
                    print("you exit from the reception")
        

            print ("your room rent is =",cart,"\n",'Thank you!')
            menu_int=int(input('Looking what else we got?\nENTER SERIAL NO. FROM THE MENU: '))

    elif menu_int==5:       #Fooding or Meals
    
            print("""   1. BREAKFAST.
              2. LUNCH.
              3. DINNER.""")
            menu_choice=int(input("ENTER THE SERIAL NUMBER:"))
            cart=0                                                        #BILL CART
            if menu_choice==1:                                  #BREAKFAST
                                                              #BREAKFAST CHOICES
                     menu_brek="""   VEG:                                      
            1. BREAD.
            2. JAM.
            3. BANANA.
            4. JUICE.
            NON-VEG:
            1. BREAD.
            2. EGG.
            3. BANANA.
            4. JUICE.
             """
                     print(menu_brek)                                    #PRINT BREAKFAST CHOICES
                     print("""   PRESS 1 FOR VEG. 
                   PRESS 2 FOR NON-VEG.
                   PRESS 3 FOR NONE.""")
                     brek_choice=int(input("ENTER YOUR CHOICE:"))
                     if brek_choice==1:                                       #VEG BRASKFAST 
                       print("YOUR BILL IS 200rs")
                       cart+=200
                     elif brek_choice==2:                                     #NON-VEG BREAKFAST
                       print("YOUR BILL IS 250rs")
                       cart+=250
                     elif brek_choice==3:                                    #NONE BREAKFAST
                       print("YOUR HAVE PURCHASED NONE")
                       cart+=0
                                                             #print(cart)

                                                              #LUNCH CHOICES 
            elif menu_choice==2:
                menu_lunch="""       
                VEG:                                
             1. RICE.
             2. VEG DAL.
             3. MIX VEG.
             4. SHAHI PANEER.
             5. SWEETS.
             6. CURDS.
        NON-VEG:
             1. RICE.
             2. VEG DAL.
             3. CHICKEN GRAVY.
             4. SHAHI PANEER.
             5. SWEETS.
             6. CURDS.
            """
                print(menu_lunch)                                     #PRINT LUNCH OPTIONS                          
                print("""  PRESS 1 FOR VEG.   
        PRESS 2 FOR NON-VEG.
        PRESS 3 FOR NONE.""")
                lunch_choice=int(input("ENTER YOUR CHOICE:"))
                if lunch_choice == 1:                                    #VEG LUNCH
                    print("YOUR BILL IS OF 450rs")
                    cart+=450
                elif lunch_choice==2:                                    #NON-VEG LUNCH
                    print("YOUR BILL IS OF 550rs")
                    cart+=550
                else:
                    print("YOU HAVE PURCHASED NOTHING")                 #NONE LUNCH
                    cart+=0
                    print(cart)

                                                          #DINNER CHOICES
            
            elif menu_choice==3:
             menu_dinner="""  
              VEG:
             1. RICE.
             2. VEG DAL.
             3. MIX VEG.
             4. ROTI.
             5. PANEER.
             6. SWEETS.
              NON-VEG:
             1. RICE.
             2. VEG DAL.
             3. CHICKEN GRAVY.
             4. PANEER.
             5. ROTI.
             6. SWEETS.
            """
            print(menu_dinner)                                    #PRINT DINNER OPTIONS
            print("""    PRESS 1 FOR VEG. 
        PRESS 2 FOR NON-VEG.
        PRESS 3 FOR NONE.""")
        
            dinner_choice=int(input("ENTER YOUR CHOICE:"))
            if dinner_choice == 1:                                  #VEG DINNER
                print("YOUR BILL IS OF 450rs")
                cart+=450
            elif dinner_choice==2:                                  #NON-VEG DINNER
                print("YOUR BILL IS OF 550rs")
                cart+=550
            else:
                print("YOU HAVE PURCHASED NOTHING")                 #NONE DINNER 
                cart+=0 
            print(cart)
            menu_int=int(input('Looking what else we got?\nENTER SERIAL NO. FROM THE MENU: '))
        
    elif menu_int==6:       #Collaborated Tourism
            print(''' WELCOME TO FUNASSET
           TOURIST DEPARTMENT

    From England and France to Italy and Germany, European countries are full of vibrant cities known for their museums,restaurants,nightlife and architecture.So,it comes as no suprise that deciding which spots are the best places to visit in Europe can be difficult.
    That's why Funassets considered the highlights of each destination-as well as user votes and expert opinions-to round up the best vacation destinations in Europe.Check the list given below:
        
     1.PARIS: Paris is filled with highly regarded museums,monuments and churches. You could easily spend your entire vacation admiring iconic sights like the Eiffel Tower,wandering through exhibits at the Louvre and strolling through the beautiful green space admiring flowers at Luxembourg Gardens.Still,you should save some time for people watching and munching on fresh croissants at sidewalk cafes during the day. Once the sun sets,sit down for a decadent French meal with amazing wine

     2.ROME: Rome is a can't-miss spot on your trip of Europe. The aroma of fresh Italian cooking wafts through the alleys, and historical sites stand proudly at every turn. No visit to Italy's capital woulb be complete without checking out the Colosseum,St.Peter's Basillica, the Sistine Chapel and the aweinspiring Trevi Foundation. If you have additional time, venture beyond the main sights to the Roman Forum, Trastevere and the Spanish Steps.

     3.LONDON: Exploring the world-class British Museum,seeing a musical in the West End,touring the Tower of London at a local pub are all part of the London bucket list experience. However, London's high hotel prices can make budget travelers cringe. To save money, book your accommodations far in advance or consider Funasset tourism services for an memorable experience.

     4.AMSTERDAM: There's more to Amsterdam than its notorious "coffee shops" and Red Light District. Spend the day biking through the city's stylish streets before exploring noteworthy museums, such as the Anne Frank House. Plan a picnic in Vondelpark for lunch, or opt for a boat tour along the city's many canals when it's time to rest your feet.Friendly locals and affordable Funasset resort keep bringing travelers back,especially, during the warmer months.

     ''')
            print("TRAVELLING COST")
            print("A.Transportation cost......Rs.61,600| B.Flights..........Rs.42,000")
            print("C.Food....................Rs.10'350 | D.Visa Charges.....Rs.6000  ")
            menu_int=int(input('Looking what else we got?\nENTER SERIAL NO. FROM THE MENU: '))
        

    elif menu_int==7:       #Location or Address 
            print("LOCATION OF FUNASSETS")
            print('''ADDRESS : Via Serlas 27 St. Moritz 7500

          WHY YOU SHOULD STAY HERE?
          Well, 
          -Located in a well maintained & secured place.
          -Police and government officials are always on duty.
          -Mesmerizing view of the ocean.
          ''')
            menu_int=int(input('ENTER SERIAL NO. : '))

    else: #Exit
                print('Thank you! Visit again...')
                sys.exit()
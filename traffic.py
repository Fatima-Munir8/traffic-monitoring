def details():  #details of vehicles  in function
    vehicle=[{"id":"1","type":"car","speed":"78","emergency":"True"}, # vehicle list containing multiple dictionaries about details of vehicle
             {"id":"2","type":"car","speed":"78","emergency":"False"},
             {"id":"3","type":"truck","speed":"90","emergency":"False"},
             {"id":"4","type":"bike","speed":"78","emergency":"False"},
             {"id":"5","type":"truck","speed":"45","emergency":"True"},
             {"id":"6","type":"bike","speed":"55","emergency":"False"},
             {"id":"7","type":"bike","speed":"70","emergency":"False"},
             {"id":"2","type":"car","speed":"68","emergency":"False"}]
    return vehicle  #returning the list
def speed_check(): # function to check the speed 
    car=0 #car variable to count cars violations
    bike=0 #bike variable to count cars violations
    truck=0 #truck variable to count cars violations
    vehicles=details()  #details function called
    for v in vehicles:  # for loop to go through every vehicle
        if v["emergency"]=="True":# if to check emergency
            continue #skip vehicle in case of emergency
        speed=int(v["speed"]) # convert speed to int 
        if v["type"]=="car": #check if vehicle is car and check speed
            if 60 < speed <= 70: 
                print("warning to id:",v["id"])
                car+=1 # increase car violation
            elif 70 < speed <= 80:
                print("fine to id:",v["id"])
                car+=1
            elif speed>80:
                print("heavy fine to id:",v["id"])
                car+=1
        elif v["type"]=="bike": #check if vehicle is car and check speed
            if 50 < speed <= 60:
                print("warning to id:",v["id"])
                bike+=1 # increase bike violation
            elif 60 < speed <= 70:
                print("fine to id:",v["id"])
                bike+=1
            elif speed>70:
                print("heavy fine to id:",v["id"])
                bike+=1
        elif v["type"]=="truck":  #check if vehicle is truck and check speed
            if 40 < speed <= 50:
                print("warning to id:",v["id"])
                truck+=1  # increase truck violation
            elif 50 < speed <= 60:
                print("fine to id:",v["id"])
                truck+=1
            elif speed>60:
                print("heavy fine to id:",v["id"])
                truck+=1
    return car,bike,truck #return each violation

def display(): # display function 
    car,bike,truck=speed_check() # speed function called
    total_violation=car+bike+truck # total violation
    vehicles = details() #details function called
    violations = () # store violated IDs in tuple
    for v in vehicles: # for loop to go through every vehicle
        if v["emergency"] == "True": # if to check emergency
            continue 
        speed = int(v["speed"]) # convert speed to int 
        # condition statement to check the vehicle which violated most and store its id
        if (v["type"] == "car" and speed > 60) or \
           (v["type"] == "bike" and speed > 50) or \
           (v["type"] == "truck" and speed > 40):
            violations = violations + (v["id"],)
    # variables to store count and max occuring id
    max_id = None
    max_count = 0
    for i in violations: # for loop to go through violation
        if violations.count(i) > max_count:  #id count more than count
            max_count = violations.count(i) # count replaced with violation count
            max_id = i # show id of most violated vehicle
# display the summary
    print("summary:")
    print("total violations:", total_violation)
    print("highest violated vehicle:", max_id)
    if car>bike and car>truck: # condition to check which vehicle type violated most
        print("highest violated vehicle type: car")
    elif bike>car and bike>truck:
        print("highest violated vehicle type: bike")
    else:
        print("highest violated vehicle type: truck")
display()
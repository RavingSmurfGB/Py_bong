import datetime, random, winsound, time



set_hours = [10, 19] # This will set the hours you want the script to work betw
sound_time_list = [] # This will be the list of time to make the sound
sound_iterations = 5 # Defines how many times we want the sound to happen.
logging = True # Enables/Disables Logging
log_file = "logging.txt"
added_to_list = None
previous_date = datetime.datetime.now().date()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Generate time list
spacing = 10    # in minutes
time_list = [str(i*datetime.timedelta(minutes=spacing)) for i in range(24*60//spacing)]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Logging
datetime.date.today().strftime("%d/%m/%Y")
def jprint(*value): # Accepts all variable types
    if logging == True:

        value_str = ''.join(value)# The value is given to us as a tuple, we use this to convert it   
        print(value_str)
        output = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") , " -- " , value_str, "\n"
        output_str = ''.join(output) # Output is also made in to a tuple so we convert it back again
        
        with open(log_file, 'a') as the_file:
            the_file.write(output_str)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Random code
# This function will generate a list of times, there will be no duplicate times and times cannot be in the same hour.
#
# Variables:
#   duplcate - Used to represent if a the time chosen is in sound_time_list
#   choice - the randomly chosen time from time_list
#   hour - is a concoction of choice, represents only the hour value
#   set_hours - a list of two times for when a sound event time should be chosen
#   sound_time_list - the final output list of the times chosen
def random_times():
    global added_to_list
    duplicate = False # We reset duplicate to be False
    choice = random.choice(time_list)
    if choice[1] == ":":
        hour = choice[0]
    else:
        hour = choice[0] + choice[1]


    if int(hour) >= set_hours[0] and int(hour) <= set_hours[1]: # If the hour of the chosen time is greater than the start hour of set_hours and is less than the end hour of set_hours then do:

        for items in sound_time_list: # Iterates through each item in sound_time_list
            if hour in items: # If the hour selectedis found in items 
                duplicate = True # Duplicate is True


        if duplicate != True: # If a duplicate wad not found
            added_to_list = "True"
            sound_time_list.append(choice) # Appends the time choice to the list
    else: 
        added_to_list = "False"

    sound_time_list_str = ', '.join(sound_time_list) # Converts the sound_time_list to string
    jprint("Time chosen - " , choice, " // Hour Chosen - ", hour , " // Added to list - ", added_to_list ," // Soundlist on this iteration  = " , sound_time_list_str )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main
jprint(" ")
jprint("Startup ")
while len(sound_time_list) < sound_iterations: # when the length of the list is smaller than the amount of sound iterations we want
    random_times()

sound_time_list_str = ', '.join(sound_time_list) # Converts the sound_time_list to string
jprint("Full list output : ", sound_time_list_str)

#need to have main check for the time, once every 30 seconds then when 


while True:
    
    current_time = datetime.datetime.now().strftime("%H:%M") # We get the  current time but only the hours and minutes
    current_time = current_time + ":00"

    # Date Cecking
    #   We use this to determine if the date has changed and we should generate a new list of times
    current_date = datetime.datetime.now().date()
    if current_date != previous_date:
        sound_time_list = []
        while len(sound_time_list) < sound_iterations: # when the length of the list is smaller than the amount of sound iterations we want
            random_times()
        sound_time_list_str = ', '.join(sound_time_list) # Converts the sound_time_list to string
        jprint("Full list output : ", sound_time_list_str) # We print the full list output
    
    previous_date = current_date

    # Time checking
    #   We use this every 60 seconds to see if the current time matches what is in the sound time list, if it does then we play the sound
    if current_time in sound_time_list: # If the current time is found in the item from sound_time_list:
        jprint(current_time , " - it activated!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        winsound.PlaySound("Bellatrix.wav", winsound.SND_FILENAME) # Will play the sound given
        time.sleep(2)
        winsound.PlaySound("Bellatrix.wav", winsound.SND_FILENAME) # Will play the sound given
        time.sleep(58)
        
    else:
        time.sleep(60)
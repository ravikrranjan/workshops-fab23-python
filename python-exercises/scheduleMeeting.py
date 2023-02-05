
#~^ scheduleMeeting(..) should take a start time (in 24-hour format as a string "hh:mm") and                                                                                                    
#~^  a meeting duration (number of minutes)                                                                                                                                                     
#~^ It should return true if the meeting falls entirely within the work day (according to the times specified in dayStart and dayEnd); return false if the meeting violates the work day bounds.

import re

dayStart = "07:30"
dayEnd = "17:45"

def scheduleMeeting(startTime:str, durationMinutes):
    refStr =  re.match("/^(\d{1,2}):(\d{2})$/", startTime)
    print("refStr:", refStr, "startTime: ",startTime, durationMinutes, type(startTime), type(durationMinutes))
    #~! TODO


scheduleMeeting("6:00", "30")

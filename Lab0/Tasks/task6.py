day ="saturday"
match day.lower :
    case "Monday":
     print("It's the start of the work week")
    case "Wednesday" :
     print("It's mid week already ")
    case "Friday":
      print("Almost weekend")
    case "Saturday" | "Sunday" :
      print("Weekend time")
    case _:
     print("Just another day")


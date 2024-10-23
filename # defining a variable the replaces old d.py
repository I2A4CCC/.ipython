# defining a variable the replaces old dates with new dates
def date_replacer(date, old_date, new_date):
    if date.endswith(old_date):
        length = len(old_date)
        new_date1 = date[:-length] + date[-length:].replace(old_date, new_date)
        return new_date1
    return date

print(date_replacer("We have a meeting at June 23", "June 23", "August 20"))
print(date_replacer("In septemeber 30th, there is going to be a meeting", "October 1", "septemebr 2"))

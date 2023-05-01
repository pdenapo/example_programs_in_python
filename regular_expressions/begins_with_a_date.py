import re

my_string = "31/12/2022 is the end of the year."
pattern = r"^\d{2}/\d{2}/\d{4}"  # regex pattern for date in the format dd/mm/yyyy
match = re.match(pattern, my_string)

if match:
    print("The string begins with a date in the format dd/mm/yyyy")
else:
    print("The string does not begin with a date in the format dd/mm/yyyy")

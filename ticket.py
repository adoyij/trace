# ticket function creation
# ticket id,
# title
# category
# urgency
# no of cases
# priority

def create_ticket():

    title = input("title: ")

    if not title.strip():
        print("\ntitle can not be empty")
        return

    if len(title) < 4:
        print("\ntitle must be at least 4 character")
        return

    valid_category = ["hardware","software","network","others"]
    category = input("category: ")
    if not category.strip():
        print("\ncategory can not be emty\n")
        return

    if category.lower().strip() not in valid_category:
        print("\ninvalid category option")
        return

    no_of_cases = int(input("no of cases "))

    valid_urgency = ["high","medium","low",]
    urgency = input("urgency  ")

    if urgency == "high" and no_of_cases >= 10:
        priority = "critical"
    if urgency == "high" or no_of_cases >= 10:
        priority = "high"
    if urgency == "low" and no_of_cases <= 7:
        priority = "medium"
    if urgency == "low" or no_of_cases <= 3:
        priority = "low"

    print(f"priority: {priority}")
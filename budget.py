class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        header = self.name.center(30, "*")
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"

        return f"{header}\n{items}Total: {format(self.get_balance(), '.2f')}"    

    ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']
        return total

    def check_funds(self, amount):
        if self.get_balance() - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


def create_spend_chart(categories):
    # empty list to store total spent in each category
    total_spent = []
    name = []
    for category in categories:
        name.append(category.name)
        # get total spent in each category
        for item in category.ledger:
            category_spent = 0
            # get total spent in each category
            if item['amount'] < 0:
                category_spent += -(item['amount'])
        total_spent.append(category_spent)
    
    # percentage spent in each category rounded to nearest 10
    percentage_spent = []
    for spent in total_spent:
        temp = int(spent * 100 // sum(total_spent))
        temp = temp // 10 * 10
        percentage_spent.append(temp)

    # create chart
    head = "Percentage spent by category\n"

    one_hundred = "100| "
    ninety = " 90| "
    eighty = " 80| "
    seventy = " 70| "
    sixty = " 60| "
    fifty = " 50| "
    forty = " 40| "
    thirty = " 30| "
    twenty = " 20| "
    ten = " 10| "
    zero = "  0| "

    for index, percent in enumerate(percentage_spent):
        if percent >= 100:
            one_hundred += "o  "
        else:
            one_hundred += "   "
        if percent >= 90:
            ninety += "o  "
        else:
            ninety += "   "
        if percent >= 80:
            eighty += "o  "
        else:
            eighty += "   "
        if percent >= 70:
            seventy += "o  "
        else:
            seventy += "   "
        if percent >= 60:
            sixty += "o  "
        else:
            sixty += "   "
        if percent >= 50:
            fifty += "o  "
        else:
            fifty += "   "
        if percent >= 40:
            forty += "o  "
        else:
            forty += "   "
        if percent >= 30:
            thirty += "o  "
        else:
            thirty += "   "
        if percent >= 20:
            twenty += "o  "
        else:
            twenty += "   "
        if percent >= 10:
            ten += "o  "
        else:
            ten += "   "
        if percent >= 0:
            zero += "o  "
        else:
            zero += "   "

    # create dashes
    dashes = "    "
    for i in range(len(zero) - 4):
        dashes += "-"

    chart = f"{head}{one_hundred}\n{ninety}\n{eighty}\n{seventy}\n{sixty}\n{fifty}\n{forty}\n{thirty}\n{twenty}\n{ten}\n{zero}\n{dashes}\n"

    # create names
    max_length = 0
    for i in name:
        if len(i) > max_length:
            max_length = len(i)
    
    for i in range(max_length):
        chart += "     "
        for j in name:
            if i >= len(j):
                chart += "   "
            else:
                chart += f"{j[i]}  "
        if i < max_length - 1:
            chart += "\n"

    return f"{chart}"
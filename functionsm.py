
def menu():
    print("1:breakfast")
    print("2.lunch")


def handle_selection(selected_value): 
    if selected_value == 1:
        print("You have selected breakfast")
        print("1. Burger-5000UGX")
        print("2.Fried chicken-7000UGX")
        print("3.toast-6000UGX")
        Choice = int(input("choose a breakfast item(1-3):"))
        if Choice == 1:
            print("You selected Burger - 5000UGX")
            total = 5000
        elif Choice == 2:
            print("you selected fried chicken - 7000UGX") 
            total = 7000
        elif Choice == 3:
            print("you selected toast - 6000UGX") 
            total = 6000
        else:
            print("invalid breakfast item selection.")   
            
    elif selected_value == 2:
        print("You hve selected lunch")
        print("1.matooke and gnuts-4000UGX")
        print("2.rice and peas-6000UGX")
        print("3.posho and beef-3000UGX")
        Choice = int(input("choose a lunch from(1-3):"))
        if Choice == 1:
            print("you selected matooke and gnuts-4000UGX")
            print("great choice")
            total = 4000
        if Choice == 2:
            print("you selected rice and peas-6000UGX")
            total = 6000
        if Choice == 3:
            print("you selected posho and beef- 3000UGX")
            total = 3000
        else:
            print("Invalid lunch item selection.")

    
    else:
        print("please enter the correct selection")
        #show total after valid selection
        print(f"Total bill:{total}UGX")

def main():
    print ("menu():")
    print ("1.Breakfast")
    print ("2.Lunch")
    selected_value = int(input("please make a choice: "))
    handle_selection(selected_value)
main()    


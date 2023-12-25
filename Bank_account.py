import random

# Initialize variables and dictionaries
count = 0
Compte = {}        # Dictionary to store accounts and their balances
Client = {}        # Dictionary to store customer numbers and passwords
ClientCompte = {}  # Dictionary to map account numbers to customer numbers

# Function to add a new account
def AjouterCompte(count, Balance=0):
    numcl = count
    numc = str(count) + str(random.randint(0, 100))
    mpc = str(random.randint(1000, 9999))
    Compte[numc] = Balance
    Client[numcl] = mpc
    ClientCompte[numc] = numcl
    print("The account was created with the customer number: ", numcl, " and account number: ", numc,
          " and the password: ", mpc)

# Function to delete an account
def SupprimerCompte(numc):
    del Compte[numc]
    del Client[ClientCompte[numc]]
    del ClientCompte[numc]

# Function to deposit money into an account
def Deposer(numcl, arg):
    for key, valeur in ClientCompte.items():
        if numcl == valeur:
            Compte[key] += arg

# Function to withdraw money from an account
def Retirer(numcl, arg):
    for key, valeur in ClientCompte.items():
        if numcl == valeur:
            if Compte[key] >= arg:
                Compte[key] = Compte[key] - arg
            else:
                print("you don't have enough money              ")

# Function to modify a customer's password
def modifierMPClient(numcl, NMP):
    Client[numcl] = NMP

# Main program loop
while True:
    print("Main Menu:")
    print("1. Bank officer")
    print("2. Bank customer")
    print("3. To leave")

    choixp = input("Choose an option (1/2/3): ")

    # Bank officer menu
    if choixp == '1':
        while True:
            print("Bank Agent Menu:")
            print("1. Add an account")
            print("2. Delete an account")
            print("3. Back")

            choixag = input("Choose an option (1/2/3): ")

            if choixag == '1':
                count += 1
                AjouterCompte(count)

            elif choixag == '2':
                numcl = input("Account number to delete: ")
                SupprimerCompte(numcl)
                print("Account deleted successfully.")

            elif choixag == '3':
                break

            else:
                print("Invalid choice. Please choose a valid option.")

    # Bank customer menu
    elif choixp == '2':
        while True:
            print("Bank Customer Menu:")
            print("1. Change the password")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Back")

            choixc = input("Choose an option (1/2/3/4): ")

            if choixc == '1':
                while True:
                    numcl = int(input("Type customer number: "))
                    nmp = str(input("Type new password: "))
                    if numcl in Client:
                        break
                    else:
                        print("Account is not defined")

                modifierMPClient(numcl, nmp)

            elif choixc == '2':
                while True:
                    numcl = int(input("Type customer number: "))
                    if numcl in Client:
                        break
                    else:
                        print("Account is not defined")

                arg = int(input("Type money "))
                Deposer(numcl, arg)
                print("Deposit successfully completed.")

            elif choixc == '3':
                while True:
                    numcl = int(input("Type customer number: "))
                    if numcl in Client:
                        break
                    else:
                        print("Account is not defined")
                arg1 = int(input("Type money "))
                Retirer(numcl, arg1)
                print("Withdrawal completed successfully.")

            elif choixc == '4':
                break

            else:
                print("Invalid choice. Please choose a valid option.")

    # Exiting the program
    elif choixp == '3':
        print("Bye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
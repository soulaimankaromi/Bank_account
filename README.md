# Bank_account
We want to create a Python application allowing the management of bank accounts in a bank:
• A bank account is defined by a unique identifier of the holder, the account number and its balance
• Two basic operations are possible on your account: deposit and withdraw money
• No overdraft facility is authorized (i.e. the balance of an account cannot be negative)
• The actors in this application are: the bank agent and a customer. Each customer has a secret code to access their account. We suppose that
each customer has only one account
Note:
• the customer number is incremental
• The account number is an integer formed by the number of its owner and a random number between 0 and 100
Example: If the customer number is 5 then their account number is for example: 556 (where 5 is the customer number and 56 is a random number between 0 and
100)
Through a menu of choices, this application offers the agent the following functionalities:
1. Add an Account
2. Delete an Account
• Through a menu of choices this application offers a customer the following functionalities:
1. Change your password
2. View your balance
3. Deposit a sum of money
4. Withdraw a sum of money
Hint: Use the Python dictionary data structure for account and customer management
Example :
• The Account dictionary associates its balance with each Account number
Example: Account={56:200, 20:360} means that the balance of account number 56 is 200Dh and the balance of account number 20 is 360Dh
• The Customer dictionary which associates each customer number with its secret code
Example: Client={1: ''566'', 2:''836''} means that the secret code of client number 1 is equal to 566 and the secret code of client number 2 is equal to 836
• The ClientCompte dictionary associates each customer number with its account number
Example: CustomerAccount {56:1,20:2} means that the account number of customer 56 is 1 and the account number of customer 20 is 2
1. We consider Customer, Account and CustomerCount the dictionaries used for account management. Define the following functions relating to the bank agent:
• addClient (numCl, MPC, numC, BalanceC) such as: numCl is the number of the new customer, MPC is his secret code, numC is the number of his account and
BalanceC is the initial balance of his account
• DeleteClient (numC) such that numC is the number of the account to be deleted
2. Define the following functions relating to a bank customer (identify the parameters of these functions)
• Modify MPClient: allowing you to modify a client's password
• Deposit: allowing you to deposit a sum of money into an account
• Withdraw: allowing you to withdraw a sum of money from an account
3. Define the lambda function generateAccountNum to generate the account number of a customer from the number of this customer
4. 

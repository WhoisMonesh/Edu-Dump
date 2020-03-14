from pages.accountDetails import AccountDetail
from pages.EDUDUMP import EDUDUMP

print('''


88888888888 88888888ba,   88        88  
88          88      `"8b  88        88  
88          88        `8b 88        88  
88aaaaa     88         88 88        88  
88"""""     88         88 88        88  
88          88         8P 88        88  
88          88      .a8P  Y8a.    .a8P  
88888888888 88888888Y"'    `"Y8888Y"'   
                                        
                                        
                                                          
88888888ba,   88        88 88b           d88 88888888ba   
88      `"8b  88        88 888b         d888 88      "8b  
88        `8b 88        88 88`8b       d8'88 88      ,8P  
88         88 88        88 88 `8b     d8' 88 88aaaaaa8P'  
88         88 88        88 88  `8b   d8'  88 88""""""'    
88         8P 88        88 88   `8b d8'   88 88           
88      .a8P  Y8a.    .a8P 88    `888'    88 88           
88888888Y"'    `"Y8888Y"'  88     `8'     88 88           
                                                          
                                                          


''')

print("|=================================|")
print("|                                 |")
print("|    PLEASE USE  VPN              |")
print("|                                 |")
print("|                                 |")
print("|                                 |")
print("|                        @Matrix  |")
print("|=================================|")

email = input("Enter your email (do not enter Fake) : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
EDUDUMP = EDUDUMP(info, email)
EDUDUMP.start_process()

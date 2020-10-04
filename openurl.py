import webbrowser
while True:
    choice = input("'url' for URL and if want to open using 'name'-  ")
    if choice == 'url':
        open_s = input("Enter the URL- ")
        webbrowser.open(open_s)
    elif choice == 'name':
        open_s = input("Name of Website- ")    
        open_s = "www."+open_s+".com"
        webbrowser.open(open_s)
    else:
        print (f"{choice} is not Valid, Enter Valid Choice")    

      


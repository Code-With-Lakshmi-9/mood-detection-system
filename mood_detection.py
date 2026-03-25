print("Welcome To Mood Detection And Suggestion System❤️")

print("1.Happy😊")
print("2.Sad☹️")
print("3.Angry😠")
print("4.Anxious/Worried😥")
print("5.Tired🥱")
print("6.Bored😒")
print("7.Confident😎")
print("8.Lonely💔")

choose = input("Enter the Number you Feel now : ")

if choose == "1":
    print("\nYou Feel like : 'Joy','excitement','Contentment' 😇.")
    ans = input("\nEnter 'yes'........ : ")
    if ans.lower() == "yes" :
            print("\n1.Do something creative and productive 😇.")
            print("\n2.Share your happiness  📤.")
            print("\nEnjoy your happiness 🎉.")   
    else:
            print("\nInvalid Choice , Please Restart the Program!!")

elif choose == "2":
    print("\nYou feel like : 'Low Energy','Crying','Loneliness' 🥺.")
    
    ans = input("\nEnter 'yes'....... :")
    if ans.lower() == "yes":
            print("\n1.Listen to Music 🎵.")
            print("\n2.Watch Something Comforting 📱.")
            print("\n3.Give Yourself Time ⌚.")    
    elif ans.lower()=="no" :
            print("\nIt's Okay to feel Sad sometimes 😢 !!!")    
    else:
            print("\nInvalid Choice , Please Restart the Program!!")
          


elif choose =="3":
    print("\nYou feel like : 'Frustration','Irritation','Tension'😨.")
    
    ans = input("\nEnter 'yes' ........ :")
    if ans.lower() == "yes":
            print("\n1.Take a deep breath 😌.")
            print("\n2.Step away from the situation ✅.")
            print("\n3.Do Physical Activity-\nlike Walking or Exercise 🏃.")
            
    elif ans.lower()=="no":
            print("\nTake a deep breathe before you React 🤔.")
            
    else:
            print("\nInvalid Choice , Please Restart the Program!!")
            

elif choose == "4":
    print("\nYou feel like : 'Nervousness','Overthinking','Fear' 😨. ")
    
    ans = input("\nEnter 'yes'........ :")
    if ans.lower()=="yes":
            print("\n1.Practice Deep Breathing 🧘‍♀️.")
            print("\n2.Break problems into small steps ⛓️‍💥.")
            print("\n3.Avoid overthinking-\nFocus on what you can control 😌.")
    elif ans.lower()=="no":
            print("\nThis feeling will pass ❤️.")       
    else:
            print("\nInvalid Choice , please restart the program!!")
          

elif choose =="5":
    print("\nYou feel like : 'Low Energy','Lack of Focus'🙃yes.")
    
    ans = input("\nEnter 'yes' ....... :")
    if ans.lower()=="yes":
            print("\n1.Get proper Sleep 😴.")
            print("\n2.Take short Breaks ⛓️‍💥.")
            print("\n3.Eat Healthy Food and Stay Hydrated 💧.")
    elif ans.lower()=="no":
            print("\nRest is not Waste of Time ⌚.")
            
            
    else:
            print("\nInvalid Choice , Please Restart the Program!!")
        

elif choose =="6":
    print("\nYou feel like : 'No Interest','Lack of Motivation' 😟.")
    
    ans=input("\nEnter 'yes' .......")
    if ans.lower()=="yes":
            print("\n1.Try something new 🆕-")
            print("\nLike hobby,game,learning 📖.")
            print("\n2.Get small goals 🚩.")
            print("\n3.Change your environment 🌳.")
    elif ans.lower()=="no":
            print("\nCuriosity can turn Boredom into Fun 😜.")
            
    else:
            print("\nInvalid Choice , Please Restart the Program!!")
            
        


elif choose =="7":
    print("\nYou feel like : 'Strong Belief in Yourself' 💪.")
    
    ans=input("\nEnter 'yes' ........ :")
    if ans.lower()=="yes":
            print("\n1.Taking on Challenges-\nLike Help Others 👍.")
            print("\n2.Keep Improving your Skills 📈.")
    elif ans.lower()=="no":
            print("\nBelieve in Yourself! 🫡.")
            
            
    else:
            print("\nInvalid Choice , Please Restart the Program!!")
        

elif choose =="8":
    print("\nYou are feel like : 'Disconnected to People or Alone' 😔.")
    ans=input("enter yes or no")
    if ans.lower()=="yes":
            print("\n1.Call or Message a Friend 📞.")
            print("\n2.Join a Group or Community 🧑‍🤝‍🧑.")
            print("\n3.spend Time with Family or Friends ⌚.")
    elif ans.lower()=="no":
            print("\nYou are not Alone , Even if it feels that Way 😇.")
    else:
            print("\nInvalid Choice , Please Restart the Program!!")

while True:
           
            restart = input("\nDo you want to try again? (yes/no): ")
    
            if restart.lower() == "yes":
                continue
            else:
                print("\nTake care 😊")
                break

print("no mood is 'bad'🤗 - every mood is normal.\nthe key is understanding it and responding in a healthy way🗝️.")


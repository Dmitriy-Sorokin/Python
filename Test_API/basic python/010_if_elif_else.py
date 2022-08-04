# age = 25
# name = 'Jo'
#
# if age == 25 or name == "Jo":
#     print('Me 25 old years and my name is Jo')
# else:
#     print("Me < 25 old years")

# name = 'Jo'
#
# if 'J' in name == "Jo":
#     print('Me 25 old years and my name is Jo')
# else:
#     print("Me < 25 old years")

pin = 1234
print("Write please pin")
user_pin = int(input())

if pin == user_pin:
    print("Sum?")
else:
    print('Error write correct pin, You have two attempts left')
    user_pin = int(input())
    if pin == user_pin:
        print("Sum?")
    else:
        print('Error write correct pin, You have one attempts left')
        user_pin = int(input())
        if pin == user_pin:
            print("Sum?")
        else:
            print('You cart blocked, please call bank')

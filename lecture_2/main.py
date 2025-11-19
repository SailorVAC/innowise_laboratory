from datetime import datetime



def generate_profile(age):
    if age>=0 and age<=12:
        return "Child"
    elif age>=13 and age<=19:
        return "Teenager"
    elif age>=20:
        return "Adult"
def input_info():
    user_name=input('Enter your full name: ')
    current_age = datetime.now().year - int(input('Enter your birth year: '))
    hobbies=[]
    while(True):
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby=='stop':
            break
        hobbies.append(hobby)
    life_stage=generate_profile(current_age)
    return {'Name': user_name,'Age': current_age,'Life stage': life_stage,'Hobbies':hobbies}
def show_info(user_profile):   
    print('','---','Profile Summary:',sep='\n')
    for key in user_profile:
        if key=='Hobbies':
            if len(user_profile[key])>0:
                print(f'Favorite Hobbies ({len(user_profile[key])})')
                for hobby in user_profile[key]:
                    print(f'- {hobby}')
            else: 
                print("You didn't mention any hobbies")
            continue
        print(f'{key}: {user_profile[key]}')
    print('---')



if __name__ == "__main__":
    show_info(input_info())



# Reusing code with our first useful function
def input_patient_data():
## Use this example for defensive programming later
    print('Enter patients name:')
    name = input()
    
    print('Enter patients age:')
    age = input()
    
    print('Enter patients weight:')
    weight = input()
    
    print ('Enter if the patient was inflammated:')
    is_inflammated = input()
    
    print(name, age, weight, is_inflammated)
    # Different ways of returning values (multiple returns, dictionary or a list)
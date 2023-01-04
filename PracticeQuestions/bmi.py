''' Calculate BMI by this program '''
# info used: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm
def BMI():
    print("Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.")
    h = float(input("Please enter your height in m: "))
    w = float(input("Please enter your weight in kg: "))
    print('%.2f'%(weight/height**2))
    '''
    BMI Categories:
    Underweight = <18.5
    Normal weight = 18.5–24.9
    Overweight = 25–29.9
    Obesity = BMI of 30 or greater
    '''
    if bmi<=18.5:
        print('Underweight')
    elif bmi<=24.9:
        print('Normal Weight')
    elif bmi<=29.9:
        print('Overweight')
    elif bmi>=30:
        print('Obesity')

BMI()

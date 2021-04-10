from exercise import Exercise

GENDER = "male"
WEIGHT = 95   # Kg
HEIGHT = 180  # cm
AGE = 26

workout = Exercise(gender=GENDER, weight=WEIGHT, height=HEIGHT, age=AGE)

def main():

    query = input("Enter the exercise you just had: ")

    workout.post_new_row(query)

if __name__ == '__main__':
    main()
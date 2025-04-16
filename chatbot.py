import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot response patterns
# Define chatbot response patterns
pairs = [
    ['(hi|hello|hey)', ['Hi there! How can I assist you today?']],
    ['(what is your name|your name|name)', ['I am Zoro, your calorie and diet assistant.']],
    ['(how can you help|your purpose)', ['I can calculate your daily calorie needs and recommend foods based on your goal or health conditions.']],
    ['(calculate calories|I want to lose weight|I want to gain weight|weight gain|weight loss)', [f'Sure please enter your details',lambda: calculate_calories()]],  # Calls function dynamically
    ['(ok|thank you|bye)', ['You’re welcome! Have a great day!']],
    ['(bye|exit|quit)', ['Goodbye! Stay healthy and take care!']]
]

# Function to calculate calories and provide food recommendations
def calculate_calories():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        age = int(input("Enter your age: "))
        sex = input("Enter your sex (male/female): ").strip().lower()
        goal = input("What is your goal? (weight gain/weight loss/maintenance): ").strip().lower()

        # Activity level options
        print('''Choose your activity level:
        1. Sedentary (little or no exercise)
        2. Lightly active (light exercise 1-3 days per week)
        3. Moderately active (moderate exercise 3-5 days per week)
        4. Very active (hard exercise 6-7 days per week)
        ''')
        activity = int(input("Enter your activity level (1-4): "))

        # Activity multipliers
        activity_multipliers = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725}

        # Calculate BMR
        if sex == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif sex == 'female':
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            return "Invalid input for sex."

        # Calculate TDEE (Total Daily Energy Expenditure)
        tdee = bmr * activity_multipliers.get(activity, 1.2)

        # Adjust TDEE based on goal
        if goal == 'weight gain':
            tdee += 500
        elif goal == 'weight loss':
            tdee -= 500

        return f"Your daily calorie requirement is approximately {tdee:.2f} calories."

    except ValueError:
        return "Invalid input. Please enter numbers where required."


# Function to get chatbot response
def get_chatbot_response(user_input):
    for pattern, responses in pairs:
        if nltk.re.match(pattern, user_input):
            return responses[0]
    if "calculate" in user_input or "calories" in user_input:
        return calculate_calories()
    return "I'm not sure how to respond to that. Try asking something else."

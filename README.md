# My Portfolio

Welcome to my GitHub portfolio! I'm a passionate developer with experience in various technologies. Below are some of my notable projects, courses, certificates, and recommended books.

## Projects

<details>
<summary>Click to expand Python code</summary>

```python
print("Welcome to the Guess the Number game!")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    if guess == num:
        print(f'CONGRATULATIONS! YOU WON! IT TOOK YOU ONLY {len(guesses)} GUESSES!')
        break
              
    guesses.append(guess)
              
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
              
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
```
</details>



- [Project 2](#): Description of Project 2
- [Project 3](#): Description of Project 3

## Courses
- [The Complete Python Bootcamp From Zero to Hero in Python](https://www.udemy.com/course/complete-python-bootcamp/)
- [Course 2](#): Description of Course 2
- [Course 3](#): Description of Course 3

## Certificates
- [Certificate 1](#): Description of Certificate 1
- [Certificate 2](#): Description of Certificate 2
- [Certificate 3](#): Description of Certificate 3

## Books I've Read
- [Modern Game Testing](https://www.google.co.uk/books/edition/Modern_Game_Testing/IEDHEAAAQBAJ?hl=en&gbpv=0) by Nikolina Finska
- [Book 2](#): Description of Book 2
- [Book 3](#): Description of Book 3

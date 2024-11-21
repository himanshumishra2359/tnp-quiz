
print('Welcome to The Quiz Game')
print('-'*40)


topics = [
    {
        "topic": "System Design",
        "data": [
            {
                "question": "What is a microservice architecture?",
                "options": [
                    "A single large application",
                    "A collection of small, independent services",
                    "A type of database",
                    "A cloud storage solution"
                ],
                "answer": "A collection of small, independent services"
            },
            {
                "question": "Which protocol is commonly used for communication between microservices?",
                "options": ["HTTP", "FTP", "SMTP", "IMAP"],
                "answer": "HTTP"
            },
            {
                "question": "What is the purpose of a message queue in system design?",
                "options": [
                    "To store large amounts of data",
                    "To manage communication between distributed systems",
                    "To provide a user interface",
                    "To handle authentication"
                ],
                "answer": "To manage communication between distributed systems"
            },
            {
                "question": "What is the CAP theorem in distributed systems?",
                "options": [
                    "Consistency, Availability, Partition Tolerance",
                    "Concurrency, Accuracy, Performance",
                    "Capacity, Accessibility, Persistence",
                    "Control, Authentication, Privacy"
                ],
                "answer": "Consistency, Availability, Partition Tolerance"
            }
        ]
    },
    {
        "topic": "Data Structures",
        "data": [
            {
                "question": "What is the time complexity of inserting an element at the beginning of a linked list?",
                "options": ["O(n)", "O(1)", "O(log n)", "O(n^2)"],
                "answer": "O(1)"
            },
            {
                "question": "Which data structure uses the principle of Last In, First Out (LIFO)?",
                "options": ["Stack", "Linked List", "Queue", "Hash Table"],
                "answer": "Stack"
            },
            {
                "question": "What is the main advantage of using a hash table?",
                "options": ["Fast access to elements", "Better memory utilization", "Easier sorting", "Fixed size"],
                "answer": "Fast access to elements"
            },
            {
                "question": "Which of the following data structures is used to implement a priority queue?",
                "options": ["Queue", "Graph", "Heap", "Stack"],
                "answer": "Heap"
            }
        ]
    },
    {
        "topic": "DBMS",
        "data": [
            {
                "question": "Which of the following is a type of NoSQL database?",
                "options": ["Relational Database", "Graph Database", "Flat File", "Spreadsheet"],
                "answer": "Graph Database"
            },
            {
                "question": "What is a foreign key in a database?",
                "options": [
                    "A key that uniquely identifies each record in a table",
                    "A key used to link two tables together",
                    "A key that allows duplicate records",
                    "A key used to store large amounts of data"
                ],
                "answer": "A key used to link two tables together"
            },
            {
                "question": "Which SQL statement is used to update data in a database?",
                "options": ["INSERT", "SELECT", "UPDATE", "DELETE"],
                "answer": "UPDATE"
            },
            {
                "question": "What is normalization in database design?",
                "options": [
                    "The process of organizing data to reduce redundancy",
                    "The process of backing up data",
                    "The process of indexing data",
                    "The process of encrypting data"
                ],
                "answer": "The process of organizing data to reduce redundancy"
            }
        ]
    },
    {
        "topic": "OOPs",
        "data": [
            {
                "question": "Which of the following is a benefit of encapsulation?",
                "options": ["Improved code readability", "Reduced code size", "Increased security", "Faster execution"],
                "answer": "Increased security"
            },
            {
                "question": "What is polymorphism in OOP?",
                "options": [
                    "The ability to create multiple classes",
                    "The ability to process objects differently based on their data type",
                    "The ability to hide data",
                    "The ability to inherit from multiple classes"
                ],
                "answer": "The ability to process objects differently based on their data type"
            },
            {
                "question": "Which of the following is an example of inheritance in OOP?",
                "options": [
                    "A class inheriting methods and properties from another class",
                    "A class defining private data members",
                    "A class implementing multiple interfaces",
                    "A class containing static methods"
                ],
                "answer": "A class inheriting methods and properties from another class"
            },
            {
                "question": "What is abstraction in OOP?",
                "options": [
                    "Hiding the implementation details and showing only the functionality",
                    "Combining data and methods into a single unit",
                    "Allowing multiple inheritance",
                    "Using pointers to access data"
                ],
                "answer": "Hiding the implementation details and showing only the functionality"
            }
        ]
    }
]

users = {}

def startQuiz():
    score = 0
    i = 1
    for topic in topics:
        print(f'Press {i} to choose {topic["topic"]}')
        i += 1
    choice = int(input("Enter your choice: "))
    questions = topics[choice - 1]["data"]
    for question in questions:
        print("-"*40)
        print(question["question"])
        for index, option in enumerate(question["options"]):
            print(f'{index + 1}. {option}')
        answer = int(input("Enter your answer: "))
        if (question["options"][answer - 1] == question["answer"]):
            score += 1
            print("Correct answer")
        else:
            print("Wrong answer")
            print("Correct answer is", question["answer"])
    print(f'Your score is {score}/{len(questions)}')


def playGame():
    startQuiz()
    playAgain = input("Do you want to play again? (yes/no): ")
    if (playAgain == "yes"):
        startQuiz()
    else:
        print("Thank you for playing")


def signIn():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if type(username) != str or type(password) != str:
        print("Invalid input")
        signIn()
    if (username in users.keys() and users[username] == password):
        print("You have successfully signed in")
        print("-"*40)
        startQuiz()
    else:
        print("Invalid username or password")
        print("Or You need to sign up first")
        main()

def signUp():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users[username] = password
    print("You have successfully signed up")
    print("-"*40)
    playGame()

def main():
    print("Press 1 to sign in")
    print("Press 2 to sign up")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        main()
    
    if (int(choice) == 1):
        signIn()
    elif (int(choice) == 2):
        signUp()
    else:
        print("Invalid choice")
        main()

main()
import random
import datetime


def generate_dict(list_name):
    keys = []
    values = []

    # Key assignment
    for item in list_name[::3]:
        keys.append(item)

    # Value assignment
    for item in list_name[1::3]:
        values.append(item)

    # Dictionary assignment
    return dict(zip(keys, values))


def save_answers(ratings_dict):
    print("\nSaving your answers...")

    x = datetime.datetime.now()
    timestamp = x.strftime("%b%d-%H%M%S")

    f = open(f"job-ratings-{timestamp}.txt", "w", encoding='utf-8')
    sorted_titles = sorted(ratings_dict.keys(), key=lambda x: x.lower())
    sorted_ratings = sorted(ratings_dict.items(), key=lambda x: x[1], reverse=True)

    f.write("Sorted by job title: \n")
    for title in sorted_titles:
        user_rating = ratings_dict[title]
        f.write(f'{title}: {user_rating}\n')

    f.write("\nSorted by highest-rated: \n")
    for title in sorted_ratings:
        f.write(f'{title[0]}: {title[1]}\n')

    print("Completed.")
    f.close()


ratings_help = """
    Things to type:
    Rating  - A number between 1 and 10, can be decimals
    Help/H  - View this help list again
    Desc/D  - Repeat the job title and description
    Skip/S  - To move onto the next job without rating
    Exit    - To end your suffering
    """
try:
    f = open(r"comp-sci-jobs.txt", "r", encoding='utf-8')
except FileNotFoundError:
    print("Hey, put the text file with all the jobs in the same folder as the .exe!")
    input("Press enter to close the window and fix your mistakes >:(")
    quit()
original_list = f.read().splitlines()
f.close()

# TODO: Ability to continue from a given filename?
print('Welcome to the most prestigious job-rating thing ever!')
print(ratings_help)

selection = input("Would you like to randomize the list of jobs? (Alphabetized by default): ").lower()
if selection == 'y' or selection == 'yes':
    randomize = True
else:
    randomize = False

Jobs = generate_dict(original_list)
job_titles = list(Jobs.keys())
if randomize:
    random.shuffle(job_titles)

ratings_dict = {}
userInput = ''

for title in job_titles:
    rating = 0
    if userInput == 'exit':
        break

    print('\n' + title)

    while not 1 <= rating <= 10:
        userInput = input("Rating: ").lower()

        if userInput.startswith("h"):
            print(ratings_help)
            continue
        elif userInput.startswith("d"):
            print(Jobs[title] + '\n')
            continue
        elif userInput.startswith("s"):
            break
        elif "exit" in userInput:
            break

        try:
            rating = float(userInput)

            if not 1 <= rating <= 10:
                print("It has to be between 1 and 10 >:(")
            else:
                ratings_dict[title] = rating

        except ValueError:
            print("Invalid response, type 'help' for more information.")

save_answers(ratings_dict)
input("Press enter to close the window.")

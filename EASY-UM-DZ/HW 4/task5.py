def get_grade(rating: int):
    if 2 <= rating <= 3:
        print('Плохо. Марш учиться!')
    elif 4 <= rating <= 5:
        print('Молодец! Можешьотдохнуть.')

if __name__ == "__main__":
    rating = int(input("Что получил по математике?\n"))
    print(get_grade(rating))
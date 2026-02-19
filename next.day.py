
def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score, 100)

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("apna name likh mc : ")
    name2 = input("tu bhi apna name likh : ")

    score = friendship_score(name1, name2)

    print(f"\n {score}")

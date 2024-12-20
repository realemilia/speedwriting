import random
import time

def get_random_text():
    texts = ["The quick brown fox jumps over the lazy dog.","Python is an amazing programming language.","Speed typing tests are fun and educational.","Practice makes perfect.","Just imagine how wonderfull you are !!"]
    return random.choice(texts)

def typing_test():
    print("Welcome to the Speed Typing Test!")
    text = get_random_text()
    print("\nType the following text as fast as you can:")
    print(f"\n{text}\n")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_per_minute = len(text.split()) / (time_taken / 60)
    
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")
    
    if user_input == text:
        print("Congratulations! You typed the text correctly.")
    else:
        print("Oops! There were some errors in your typing.")

if __name__ == "__main__":
    typing_test()

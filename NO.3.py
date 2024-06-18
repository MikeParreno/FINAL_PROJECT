import time

def calculate_wpm(words, time_taken):
  """Calculates words per minute based on word count and time."""
  minutes = time_taken / 60
  return len(words.split()) / minutes

def display_typing_test(text):
  """Displays the text, times the user's input, and calculates results."""
  print("Get ready to type!")
  start_time = time.time()
  user_input = input(text)
  end_time = time.time()

  time_taken = end_time - start_time
  words = text.split()
  correct_words = 0
  for i, word in enumerate(words):
    if user_input.split()[i] == word:
      correct_words += 1

  accuracy = (correct_words / len(words)) * 100
  wpm = calculate_wpm(text, time_taken)

  print("\n--- Results ---")
  print(f"Time taken: {time_taken:.2f} seconds")
  print(f"Words typed: {len(user_input.split())}")
  print(f"Correct words: {correct_words}")
  print(f"Accuracy: {accuracy:.2f}%")
  print(f"Typing speed: {wpm:.2f} WPM")



text = 'I want to be a tutubu na walang tinatagong bato na nangaling sa lupa na tinuka ng manok:  '

display_typing_test(text)

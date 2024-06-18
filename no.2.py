def take_quiz():
  """Presents a quiz with questions from a file and tracks the score."""
  score = 0
  questions_file = 'file.txt'
  # Open the question file and iterate through each line
  with open(questions_file, 'r') as file:
    for line in file:
      question, answer = line.strip().split('|')  # Split by '|' delimiter
      print(question)
      user_answer = input("Enter your answer (or 'skip' to continue): ").lower()
      if user_answer == 'skip':
        continue
      if user_answer == answer.lower():
        print("Correct!")
        score += 1
      else:
        print(f"Incorrect. The correct answer is: {answer}")

  print("\n--- Quiz Summary ---")
  print(f"You answered {score} out of {len(open(questions_file).readlines())} questions correctly.")

# Start the quiz
take_quiz()

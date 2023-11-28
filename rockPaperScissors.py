import random

# Allows user to input a choice, and CPU randomly selects one.
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  CPU_choice = random.choice(options)

  choices = {
    "player": player_choice,
    "CPU": CPU_choice
  }
  return choices


# Compares the choices and prints the winner.
def check_win(player, CPU):
  
# string concatenation
# print("You chose " + player + ", CPU chose " + CPU)
  if player not in ["rock", "paper", "scissors"]:
    return f"You entered... {player}. Is this a mistake or do you think you're being clever?"
# f-strings are like JS template literals.
  print(f"You chose {player}, CPU chose {CPU}.")
  if player == CPU:
    return "It's a tie!"
    
# player chooses rock
  elif player == "rock":
    if CPU == "scissors":
      return "Rock smashes scissors. You win!"
    else:
      return "Paper covers rock. You lose."
      
# player chooses paper
  elif player == "paper":
    if CPU == "rock":
      return "Paper covers rock. You win!"
    else:
      return "Scissors cuts paper. You lose."
      
# player chooses scissors 
  elif player == "scissors":
    if CPU == "paper":
      return "Scissors cuts paper. You win!"
    else:
      return "Rock smashes scissors. You lose."



choices = get_choices()
result = check_win(choices["player"], choices["CPU"])
print(result)
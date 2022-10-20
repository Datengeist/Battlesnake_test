import random
import typing


# info is called when you create your Battlesnake on play.battlesnake.com
def info() -> typing.Dict:
  print("INFO")

  return {
    "apiversion": "1",
    "author": "Datengeist",  # TODO: Your Battlesnake Username
    "color": "#00e6e6",  # TODO: Choose color
    "head": "default",  # TODO: Choose head
    "tail": "default",  # TODO: Choose tail
  }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
  print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
  print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

  is_move_safe = {"up": True, "down": True, "left": True, "right": True}

  # We've included code to prevent your Battlesnake from moving backwards
  my_head = game_state["you"]["body"][0]  # Coordinates of your head

  for body in game_state["you"]["body"]:
    if body["x"] == my_head["x"] - 1 and body["y"] == my_head["y"]:
      is_move_safe["left"] = False

    if body["x"] == my_head["x"] + 1 and body["y"] == my_head["y"]:
      is_move_safe["right"] = False

    if body["y"] == my_head["y"] - 1 and body["x"] == my_head["x"]:
      is_move_safe["down"] = False

    if body["y"] == my_head["y"] + 1 and body["x"] == my_head["x"]:
      is_move_safe["up"] = False

  # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
  #board_width = game_state['board']['width']
  #board_height = game_state['board']['height']
  if my_head["x"] == 10:
    is_move_safe["right"] = False
  if my_head["x"] == 0:
    is_move_safe["left"] = False
  if my_head["y"] == 10:
    is_move_safe["up"] = False
  if my_head["y"] == 0:
    is_move_safe["down"] = False

  # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
  # my_body = game_state['you']['body']

  # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
  # opponents = game_state['board']['snakes']

  # Are there any safe moves left?
  safe_moves = []
  for move, isSafe in is_move_safe.items():
    if isSafe:
      safe_moves.append(move)

  if len(safe_moves) == 0:
    print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
    return {"move": "down"}

  # Choose a random move from the safe ones
  next_move = random.choice(safe_moves)

  # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
  # food = game_state['board']['food']

  print(f"MOVE {game_state['turn']}: {next_move}")
  return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
  from server import run_server

  run_server({"info": info, "start": start, "move": move, "end": end})

import turtle
import random
import time

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("🚗 Car Race Simulator")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# --- Start Screen ---
def start_screen():
    start_text = turtle.Turtle()
    start_text.hideturtle()
    start_text.color("black")
    start_text.penup()
    start_text.goto(0, 0)
    start_text.write("Press ENTER to Start the Race!", align="center", font=("Arial", 24, "bold"))
    screen.listen()
    screen.onkey(start_text.clear, "Return")  # Clear text on Enter key
    screen.onkey(lambda: None, "Return")  # Dummy to exit wait loop
    turtle.mainloop()  # Wait for Enter

# Comment out this line if you don't want to pause before race
# start_screen()

# --- Create Cars ---
def create_car(color, y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(-350, y)
    return t

car_names = ["Lightning", "Storm", "Blaze"]
car_colors = ["red", "blue", "green"]
start_y = [100, 50, 0]
cars = [create_car(car_colors[i], start_y[i]) for i in range(3)]
fuel_levels = [100 for _ in range(3)]
fuel_bars = []

# --- Create Fuel Bars ---
def create_fuel_bar(y):
    bar = turtle.Turtle()
    bar.hideturtle()
    bar.penup()
    bar.goto(250, y)
    bar.pendown()
    bar.color("black")
    bar.forward(100)
    return bar

def update_fuel_fill(index, fuel_percent):
    fill = fuel_fills[index]
    fill.clear()
    fill.penup()
    fill.goto(250, start_y[index] - 10)
    fill.color("green" if fuel_percent > 30 else "orange" if fuel_percent > 10 else "red")
    fill.begin_fill()
    fill.setheading(0)
    fill.forward(fuel_percent)
    fill.setheading(90)
    fill.forward(10)
    fill.setheading(180)
    fill.forward(fuel_percent)
    fill.setheading(270)
    fill.forward(10)
    fill.end_fill()

# Draw bars and fills
for y in start_y:
    create_fuel_bar(y)
fuel_fills = [turtle.Turtle() for _ in range(3)]
for f in fuel_fills:
    f.hideturtle()
    f.speed(0)

# --- Race Logic ---
finish_x = 300

print("🏁 Race Starts!")

while True:
    for i in range(3):
        if fuel_levels[i] <= 0:
            continue

        # Turbo Boost
        if random.random() < 0.2 and fuel_levels[i] >= 20:
            step = random.randint(20, 30)
            fuel_levels[i] -= 20
        else:
            step = random.randint(5, 15)
            fuel_levels[i] -= random.randint(5, 10)

        cars[i].forward(step)

        # Update fuel bar
        fuel_percent = max(0, (fuel_levels[i]))
        update_fuel_fill(i, fuel_percent)

        if cars[i].xcor() >= finish_x:
            winner = car_names[i]
            print(f"\n🏆 {winner} WINS THE RACE!")
            winner_turtle = turtle.Turtle()
            winner_turtle.hideturtle()
            winner_turtle.color("black")
            winner_turtle.penup()
            winner_turtle.goto(0, -150)
            winner_turtle.write(f"{winner} Wins!", align="center", font=("Arial", 28, "bold"))
            turtle.done()
            exit()

    time.sleep(0.3)

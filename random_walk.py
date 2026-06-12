import numpy as np
import matplotlib.pyplot as plt

#main
#introduction()
#random_walk_simulation()
#analysis()
#conclusion()
points = 0

# Parameters
num_steps = 1200
start_value = 100  # Often used as a starting stock price
mu = 0             # Mean (drift)
sigma = 1          # Volatility (standard deviation)



for i in range(1,7):


    # Equation step: Generate continuous epsilon_t
    epsilon = np.random.normal(loc=mu, scale=sigma, size=num_steps)

# Equation step: y_t = y_{t-1} + epsilon_t
    random_walk = np.cumsum(epsilon) + start_value
    steps = np.arange(1201)

    plt.figure()
# Plot results
    plt.plot(steps[0:1001], random_walk[0:1001], color='blue')
    plt.title("Continuous (Gaussian) Random Walk")
    plt.xlabel("Steps")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show(block=False)

    prediction = input("What is your prediction for the future price? " )
    #split_idx = 1000
    #plt.plot(random_walk[0:1001], color='blue')
    plt.plot(steps[1000:1200], random_walk[1000:1200])
    #plt.grid(True)
    #plt.show()

    while prediction != "up" and prediction != "down":
        prediction = input("Invalid prediction. Please enter 'up' or 'down'. ")


    #color code up and down
    final_change = random_walk[1199] - random_walk[1000]
    #actual_direction = "up" if final_change < 0 else "down"


    if final_change > 0:
        actual = "up"
        plt.plot(steps[1000:1200], random_walk[1000:1200], color='green')
    else:    
        actual = "down"
        plt.plot(steps[1000:1200], random_walk[1000:1200], color='red')    

    if prediction.lower() == actual:
        print("Correct! The price went", actual)
        points += 1
    else:    print("Incorrect. The price went", actual)


    plt.grid(True)
    plt.show(block=False)

    print("Your score is:", points)
    input("Press Enter for next challenge...")
    plt.close('all')  # Destroys the window so the next round starts with a clean screen


print("\n=====================================")
print(f"GAME OVER! Your final score: {points}/6")
if points >= 4:
    print("Incredible. You beat the system!")
else:
    print("Market efficiency wins. It's truly a random walk!")






#if prediction.lower() == actual_direction:
 #   print("Correct! The price went", actual_direction)
#else:    print("Incorrect. The price went", actual_direction)   
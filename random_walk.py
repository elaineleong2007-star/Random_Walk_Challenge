import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

#main

def blank():
    input("")

def introduction():
    #print("Are you actually looking at a trend, or just chasing ghosts in the data? Take the challenge and see if you can actually beat the market—or if the market beats you.")
    #blank = input("")
    #print("\nThis project tackles the ultimate trading debate: Is the stock market a goldmine of predictable patterns, or is it just a chaotic random walk where asset prices move purely by chance?")
    #blank = input("")
    #print('\nWe are going to use a Python simulation to test the brutal reality of the Efficient Market Hypothesis (EMH). We will analyze the apparent futility of reading charts, and see how ruthlessly market efficiency swallows up new information before you can even click "buy."')
    #blank = input("")
    print("\n\n")
    print("======================================================================\n")
    print("     Beat the Market? Prove It. Can you outsmart the random walk ?\n")
    print("======================================================================")
    print("\nThink you can beat the stock market? Professional traders spend millions")
    print("trying to find patterns in financial charts. But economists argue it’s a trap,")
    print("proving that price charts are nothing more than a RANDOM WALK, meaning asset")
    print("prices move purely by chance, like successive rolls of a dice.")
    print("\nAccording to the Efficient Market Hypothesis (EMH), trying to outsmart the")
    print("system is a lesson in FUTILITY. Thanks to extreme MARKET EFFICIENCY, millions")
    print("of investors react to news instantly, leaving zero 'hidden patterns' behind.")
    print("\nAre you actually spotting a trend in this simulation, or just chasing ghosts")
    print("in the data? Take the challenge and see if you can beat the odds.")
    print("\n")
    print("------------------------------------------------------------------")
    print("\nFrom the chart, what is your prediction for the next 200 days' price movement? " )
    input("Press ENTER if you dare to challenge the market...")
#conclusion()


# Parameters
num_steps = 1200
start_value = 100  # Often used as a starting stock price
mu = 0             # Mean (drift)
sigma = 1
          # Volatility (standard deviation)
points = 0


def random_walk_simulation():
    
    global points
    for i in range(1,11):


        # Equation step: Generate continuous epsilon_t
        epsilon = np.random.normal(loc=mu, scale=sigma, size=num_steps)

    # Equation step: y_t = y_{t-1} + epsilon_t
        random_walk = np.cumsum(epsilon) + start_value
        steps = np.arange(1201)

        plt.figure()
    # Plot results
        plt.plot(steps[0:1001], random_walk[0:1001], color='blue')
        plt.title("Continuous (Gaussian) Random Walk")
        plt.xlabel("Days")
        plt.ylabel("Value")
        plt.grid(True)
        plt.show(block=False)


        
        prediction = input("Write 'up' if you think the price will go up, or 'down' if you think it will go down. ")
        prediction = prediction.lower()
        
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
        plt.grid(True)
        plt.show(block=False)


        if prediction.lower() == actual:
            print("Correct! The price went", actual)
            points += 1
        else:    print("Incorrect. The price went", actual)
        


        plt.grid(True)
        plt.show(block=False)

        print("Your score is:", points)
        input("Press Enter for next challenge...")
        plt.close('all')  # Destroys the window so the next round starts with a clean screen



def analysis():
    final_points = points
    print("\n=====================================")
    print("\nPrediction Report:")
    print(f"GAME OVER! Your final score: {final_points}/10")
    if final_points >= 6:
        print("Incredible. You beat the system!")
    else:
        print("Market efficiency wins. It's truly a random walk!")

def conclusion():
    print("\n\n==================================================================")
    print("                       PROJECT CONCLUSION                         ")
    print("==================================================================")
    print("\nWhile the simulation may demonstrate the apparent futility of")
    print("predicting a random walk, we must acknowledge that chart price analysis is not")
    print("entirely useless in the real world.")
    print("\nThis program is ultimately only a simulation of the Random Walk theory build on math.")
    print("\nIn actual financial markets, asset prices aren't driven solely on computer math,")
    print("they are driven by people. Human behavior introduces emotional biases, herd")
    print("mentalities, overnight panics, and massive structural waves.")
    print("\nWhile Efficient Market Hypothesis theory assumes absolute rationality, human psychology")
    print("leaves footprints on real charts that active traders exploit every single day.")
    print("\nFinal Takeaway: Math says it's impossible. But the market is govern by human behavior.")
    print("\n==================================================================")

if __name__ == "__main__":
   
    introduction()
    random_walk_simulation()
    analysis()
    conclusion()




#if prediction.lower() == actual_direction:
 #   print("Correct! The price went", actual_direction)
#else:    print("Incorrect. The price went", actual_direction)   
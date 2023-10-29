import subprocess
import threading
NUMBER_OF_RUNS = 1000
NUMBER_OF_THREADS = 10
# Define the shell command you want to run
command = "python3 play.py"  # Replace this with your desired shell command

# Run the command and capture the output
player1Count = 0
player2Count = 0
timeConstrained = 0

threads = []

def run_command(thread_num):
    global NUMBER_OF_THREADS, NUMBER_OF_RUNS
    global player1Count
    global player2Count
    global timeConstrained

    for i in range(int(NUMBER_OF_RUNS/NUMBER_OF_THREADS)):

        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            # print(f"{i+1}%\tP1: {player1Count} - P2: {player2Count}\r", end="")
            if "Uh oh." in output:
                timeConstrained += 1 

            if "Player 2 wins!" in output:
                player2Count += 1
            elif "Player 1 wins!":
                player1Count += 1
            else:
                print("BROKEN")
                exit(1)
            print(f"P1: {player1Count} - P2: {player2Count} - TC: {timeConstrained}\r", end="")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.returncode}\n{e.output}")

for i in range(NUMBER_OF_THREADS):
    thread = threading.Thread(target=run_command, args=(i,))
    threads.append(thread)
    thread.start()

# while player1Count + player2Count < NUMBER_OF_RUNS:


for thread in threads:
    
    thread.join()
print(f"P1: {player1Count} - P2: {player2Count} - TC: {timeConstrained}")
       



# Import the necessary modules
import time

# Store the current time
start_time = time.time()

# Main loop
while True:
    # Calculate the elapsed time
    elapsed_time = int(time.time() - start_time)
    # Calculate hours, minutes and seconds
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = (elapsed_time % 3600) % 60
    # Print out the clock
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    # Pause for 1 second
    time.sleep(1)
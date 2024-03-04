import time
import winsound

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Alarm ringing...")
            for _ in range(5):  # Repeat the sound 5 times
                winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            break
        time.sleep(1)  # Check the time every second

def main():
    print("Welcome to the Alarm Clock!")
    print("Enter the alarm time in HH:MM:SS format:")
    alarm_time = input(">> ")

    # Validate the input time format
    try:
        time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")
        return

    print("Enter the path to the sound file (wave format):")
    sound_file = input(">>")

    set_alarm(alarm_time, sound_file)

if __name__ == "__main__":
    main()

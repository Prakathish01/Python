# Alarm Clock

import time ,datetime,pygame
def set_timer(alarm_time):
    print(f"Alarm set for {alarm_time}")
    alarm_sound = "Ex61a_alarmClock.mp3"

    is_running = True
    while is_running:
        present = datetime.datetime.now().strftime("%H:%M:%S")
        print(present)
        if alarm_time == present:
            print("Wake UP!!")
            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play(-1)
            while True:
                stop = input("Enter 'stop' to off the alarm :").strip().lower()
                if stop =="stop":
                    pygame.mixer.music.stop()
                    print("Alarm stopped")
                    break
                else:
                    print("Invalid Input,Enter 'stop' to off the alarm!!")
            is_running = False
        time.sleep(1)
if __name__ == "__main__":
    time_ = input("Enter the time for alarm(HH:MM:SS): ")
    set_timer(time_)

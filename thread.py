import time
import threading

def dog_walk(firstName, lastName):
    time.sleep(8)
    print(f"take out {firstName} {lastName} for a walk")

def take_thrash_out():
    time.sleep(2)
    print("take out the trash")

def do_homework():
    time.sleep(4)
    print("do your homework")

chore1 = threading.Thread(target=dog_walk , args=("Scooby", "boo"))
chore1.start()

chore2 = threading.Thread(target=take_thrash_out)
chore2.start()

chore3 = threading.Thread(target=do_homework)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all the tasks are completed")
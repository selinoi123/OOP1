from datetime import datetime
class Timer:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.started_at = datetime.now()

    def __str__(self):
        return f"Timer '{self.name}' set for {self.duration} minutes (started at : {self.started_at.strftime('%H:%M:%S')})"

    def __repr__(self):
        return f"Timer ({repr(self.name)}, {self.duration})"

    def __del__(self):
        print(f"Timer'{self.name}' has been deleted.")


timer1 = Timer("Workout", 45)
timer2 = Timer("Meditation", 10)

print(timer1)
print(repr(timer2))

timer1.paused = False
print(timer1.paused)
del timer1.paused

timers = [timer1, timer2]
for i in timers:
    print(repr(i))
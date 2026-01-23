class Animal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
    def describe(self):
        print("Animal Physical Characteristics:")
        print(f"Arm length: {self.arm_length}")
        print(f"Leg length: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {self.has_tail}")
        print(f"Is furry: {self.is_furry}")
def main():
    my_favorite_animal = Animal(
        arm_length=0.3,
        leg_length=0.5,
        num_eyes=2,
        has_tail=True,
        is_furry=True
    )
    my_favorite_animal.describe()
if __name__ == '__main__':
    main()
import random
# from .trans_permut import transposition as otp


class create_otp:
    '''
    interger : 0-9
    upper case : 65-91
    lower case : 97-123
    symbol : @ # _ .
    '''

    def generate_otp(self):
        # symbol = ['@', '#', '_', '.']
        generated_otp = ""

        # Generating different type of character and merging it . . .
        for i in range(2):
            generated_otp += chr(random.randint(65, 90))
            generated_otp += chr(random.randint(97, 122))
            generated_otp += str(random.randint(0, 9))

        # generated_otp = otp.transposition(generated_otp)
        print(generated_otp)
        return generated_otp

    def unit_test(self):
        first = self.generate_otp()
        counter = 0
        least = 0
        while first != least:
            least = self.generate_otp()
            counter = counter + 1
            print(counter)
        print("%s==%s" % (first, least))
        print("counter==", counter)


if __name__ == "__main__":
    create_otp()

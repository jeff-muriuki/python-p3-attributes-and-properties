APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug"
]

class Dog:

    def __init__(self, name='Unknown', breed= 'Unknown'):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
            
        else:
            print("Name must be string between 1 and 25 characters.")
            

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
            
        else:
            print("Breed must be in list of approved breeds.")
            
# Test the Dog class
if __name__ == "__main__":
    # Test empty string name
    dog1 = Dog("Buddy", "Labrador")
    
    # Expected Output: Name must be string between 1 and 25 characters.

    # Test non-str
    dog2= Dog("Charlie", "Mastiff")
    # Expected Output: Name must be string between 1 and 25 characters.

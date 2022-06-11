import os
import shutil

class Mover:

    def __init__(self):
        
        # Source Folder to watch
        self.source = os.listdir(f'/home/{os.getlogin()}/Downloads')

        # Windows downloads path --> C:\Users\YourUserName\Downloads

        # List of possible destinations
        self.destinations = [os.listdir('/home/chris/Downloads/Pictures'),os.listdir('/home/chris/Downloads/Movies'),
        os.listdir('/home/chris/Downloads/Games')]

        self.jpg = 0
        self.zip = 0
        self.iso = 0
        self.rar = 0
        self.png = 0
        self.file_totals = 0

    def mover(self):
        count = 0

        for i in self.source:
            result = self.source[count].split('.')
            # Remove before production prints the split results of all the files in the directory
            print(result[-1])

            if result[-1] == 'jpg':

                self.jpg += 1
                self.file_totals += 1
                
                source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                destination = f'/home/{os.getlogin()}/Downloads/Pictures/{self.source[count]}'

                shutil.move(source, destination)

                #Remove before production
                print(source)
                print(destination)

                count += 1

            elif result[-1] == 'zip':

                self.zip += 1
                self.file_totals += 1

                source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                destination = f'/home/{os.getlogin()}/Downloads/Games/{self.source[count]}'

                shutil.move(source, destination)
                
                count += 1

            elif result[-1] == 'rar':

                self.rar += 1
                self.file_totals += 1

                source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                destination = f'/home/{os.getlogin()}/Downloads/Games/{self.source[count]}'

                shutil.move(source, destination)
                
                count += 1

            elif result[-1] == 'iso':

                self.iso += 1
                self.file_totals += 1

                source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                destination = f'/home/{os.getlogin()}/Downloads/Games/{self.source[count]}'

                shutil.move(source, destination)

                count += 1

            elif result[-1] == 'png':

                self.png += 1
                self.file_totals += 1

                source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                destination = f'/home/{os.getlogin()}/Downloads/Pictures/{self.source[count]}'

                shutil.move(source, destination)

                count += 1

            else:
                self.file_totals += 1
                count += 1

# Remove before production
test = Mover()
print(test.mover())

print(test.source)
print(test.destinations[0])
print(test.destinations[1])
print(test.destinations[2])
print(test.jpg)
print(test.zip)
print(test.rar)
print(test.png)
print(test.file_totals)
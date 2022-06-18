import os
import shutil

from sys import platform

class Mover:

    def __init__(self):
        
        # Source Folder to watch

        self.source = ''
        
        # Checks to see what os is running and sets the path appropriately

        if platform == "linux":

            self.source = os.listdir(f'/home/{os.getlogin()}/Downloads')

            paths = [
                'Pictures','Movies','Documents','Games'
            ]

            count = 0

            for i in paths:

                if os.path.exists(f'/home/{os.getlogin()}/Downloads/{paths[count]}') == True:

                    count += 1

                else:

                    os.mkdir(f'/home/{os.getlogin()}/Downloads/{paths[count]}')

                    count += 1

        elif platform == 'win32':

            self.source = os.listdir(f'C:\\Users\\{os.getlogin()}\\Downloads\\')

            paths = [
                'Pictures','Movies','Documents','Games'
            ]

            count = 0

            for i in paths:

                if os.path.exists(f'C:\\Users\\{os.getlogin()}\\Downloads\\{paths[count]}') == True:

                    count += 1

                else:

                    os.mkdir(f'C:\\Users\\{os.getlogin()}\\Downloads\\{paths[count]}')

                    count += 1

        else:

            self.source = os.listdir(f'/home/{os.getlogin()}/Downloads')

            paths = [
                'Pictures','Movies','Documents','Games'
            ]

            count = 0

            for i in paths:

                if os.path.exists(f'/home/{os.getlogin()}/Downloads/{paths[count]}') == True:

                    count += 1

                else:

                    os.mkdir(f'/home/{os.getlogin()}/Downloads/{paths[count]}')

                    count += 1


        # List of possible destinations

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

            def osChecker(fileType):

                if platform == 'linux':

                    source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                    destination = f'/home/{os.getlogin()}/Downloads/{fileType}/{self.source[count]}'

                    shutil.move(source, destination)

                elif platform == 'win32':

                    source = f'C:\\Users\\{os.getlogin()}\\Downloads\\{self.source[count]}'
                    destination = f'C:\\Users\\{os.getlogin()}\\Downloads\\{fileType}\\{self.source[count]}'

                    shutil.move(source, destination)

                else:

                    source = f'/home/{os.getlogin()}/Downloads/{self.source[count]}'
                    destination = f'/home/{os.getlogin()}/Downloads/{fileType}/{self.source[count]}'

                    shutil.move(source, destination)

            if result[-1] == 'jpg':

                self.jpg += 1
                self.file_totals += 1
                
                osChecker('Pictures')

                count += 1

            elif result[-1] == 'jpeg':

                osChecker('Pictures')

                count += 1

            elif result[-1] == 'zip':

                self.zip += 1
                self.file_totals += 1

                osChecker('Games')
                
                count += 1

            elif result[-1] == 'rar':

                self.rar += 1
                self.file_totals += 1

                osChecker('Games')
                
                count += 1

            elif result[-1] == 'iso':

                self.iso += 1
                self.file_totals += 1

                osChecker('Games')

                count += 1

            elif result[-1] == 'png':

                self.png += 1
                self.file_totals += 1

                osChecker('Pictures')

                count += 1

            elif result[-1] == 'csv':

                osChecker('Documents')

                count += 1

            elif result[-1] == 'SRT':

                osChecker('Movies')

                count += 1

            elif result[-1] == 'AC3-EVO':

                osChecker('Movies')

                count += 1

            elif result[-1] == 'XviD-EVO':

                osChecker('Movies')

                count += 1

            else:
                self.file_totals += 1
                count += 1

# Remove before production
test = Mover()
test.mover()

print(test.source)
print(test.jpg)
print(test.zip)
print(test.rar)
print(test.png)
print(test.file_totals)
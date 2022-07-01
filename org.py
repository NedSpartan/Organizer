import os
import shutil

from sys import platform

class Mover:

    def __init__(self):
        
        # Source Folder to watch

        self.source = ''
        
        # Checks to see what os is running and sets the source path appropriately

        if platform == "linux":

            self.source = os.listdir(f'/home/{os.getlogin()}/Downloads')

            paths = [
                'Pictures','Movies','Documents','Games','Applications'
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
                'Pictures','Movies','Documents','Games','Applications'
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
                'Pictures','Movies','Documents','Games','Applications '
            ]
            
            # Checks to see if destination folders exist in the downloads folder and if not creates them. 

            count = 0

            for i in paths:

                if os.path.exists(f'/home/{os.getlogin()}/Downloads/{paths[count]}') == True:

                    count += 1

                else:

                    os.mkdir(f'/home/{os.getlogin()}/Downloads/{paths[count]}')

                    count += 1

        self.file_totals = 0

    def mover(self):
        
        count = 0

        for i in self.source:

            result = self.source[count].split('.')

            def move(fileType):

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
            
            # Different extensions endings after split should go in this list

            self.extensionsApplications = [
                'deb','exe','dmg','zip','7zip','rar','32','64','flatpakref'
            ]

            self.extensionsPictures = [
                'jpeg','png','gif','pdf','eps','ai','psd','tiff','raw','jpg','kdc','pcd','dcr','dcs','hdp',
                'bmp'
            ]

            self.extensionsDocuments = [
                'doc','docx','html','css','c','py','blend','js','ps','indd','xps','dwf','dwfx','xls','xlsx',
                'txt'
            ]

            self.extensionsMovies = [
                'mpeg','divx','mp4','mkv','flak','flv'
            ]

            # Logic to determine where the the files are moved to

            if result[-1] in self.extensionsApplications:

                move('Applications')

                count += 1

            elif result[-1] in self.extensionsPictures:

                move('Pictures')

                count += 1

            elif result[-1] in self.extensionsDocuments:

                move('Documents')

                count += 1

            elif result[-1] in self.extensionsMovies:

                move('Movies')

                count += 1

            else:

                self.file_totals += 1

                count += 1

                print(result[-1])

if __name__ == '__main__':

    mover = Mover()

    mover.mover()

    print(mover.file_totals)
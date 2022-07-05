from random import choice

class MP3Player():
    def __init__(self,track_list = list()):
        self.track_list = track_list
        self.volume = 100
        self.state = True
        self.playing_song = ""
    
    def choose_aSong(self):
        counter = 1
        for i in self.track_list:
            print(f"{counter}) {i}")
            counter += 1
        while True:
            try:
                play = int(input("Write a number for playing a song : "))
                break
            except:
                print("Write as a number!!")
        while play < 1 or play > len(self.track_list):
            while True:
                try:
                    play = int(input("Write a number between 1 and %s for playing the song you choose! : "%(len(self.track_list))))
                    break
                except:
                    print("Write as a number!!")
        self.playing_song = self.track_list[play-1]

    def random_song(self):
        self.playing_song = choice(self.track_list)

    def add_aSong(self):
        artist = input("Write a artist : ")
        song = input("Write a song that belongs to the {}: ".format(artist))
        self.track_list.append(artist + " && " + song)

    def delete_aSong(self):
        counter = 1
        for i in self.track_list:
            print("{}) {}".format(counter,i))
            counter += 1
        while True:
            try:
                delete = int(input("Write the song you want to delete : "))
                break
            except:
                print("Write as a number!!")
        while delete < 1 or delete > len(self.track_list):
            while True:
                try:
                    delete = int(input("Write a number between 1 and %s for delete the song you choose! : "%(len(self.track_list))))
                    break
                except:
                    print("Write as a number!!")
        if self.playing_song == self.track_list[delete-1]:
            self.playing_song = ""
        self.track_list.pop(delete-1)

    def volume_up(self):
        if self.volume == 100:
            pass
        else:
            self.volume += 10

    def volume_down(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 10

    def exit(self):
        self.state = False
    
    def show_menu(self):
        print("""\n     ***** MP3 Player *****
Track List : {}

The Playing Song : {}

Sound Volume : {}

1- Choose a Song
2- Choose a Random Song
3- Add a Song
4- Delete a Song
5- Volume Up
6- Volume Down
7- Exit
""".format(self.track_list,self.playing_song,self.volume))

    def choice(self):
        while True:
            try:
                choice = int(input("Write your choice : "))
                break
            except:
                print("Write as a number!!")
        while choice < 1 or choice > 7:
            while True:
                try:
                    choice = int(input("Write your choice between 1 and 7. Again! : "))
                    break
                except:
                    print("Write as a number!!")
        return choice

    def run(self):
        self.show_menu()
        choose = self.choice()

        if choose == 1:
            self.choose_aSong()

        if choose == 2:
            self.random_song()

        if choose == 3:
            self.add_aSong()
        
        if choose == 4:
            self.delete_aSong()

        if choose == 5:
            self.volume_up()

        if choose == 6:
            self.volume_down()
        
        if choose == 7:
            self.exit()

mp3player = MP3Player()
while mp3player.state:
    mp3player.run()
print("\n   Logged OUT !!\n")
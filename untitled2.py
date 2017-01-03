from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,
              text = "Adjective: "
              ).grid(row = 1, column = 0, sticky = W)
        self.adj1_ent = Entry(self)
        self.adj1_ent.grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = "Adjective:"
              ).grid(row = 2, column = 0, sticky = W)
        self.adj2_ent = Entry(self)
        self.adj2_ent.grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = "Noun:"
              ).grid(row = 3, column = 0, sticky = W)
        self.noun1_ent = Entry(self)
        self.noun1_ent.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = "Noun:"
              ).grid(row = 4, column = 0, sticky = W)
        self.noun2_ent = Entry(self)
        self.noun2_ent.grid(row = 4, column = 1, sticky = W)

        Label(self,
              text = "Noun:"
              ).grid(row = 5, column = 0, sticky = W)
        self.noun3_ent = Entry(self)      
        self.noun3_ent.grid(row = 5, column = 1, sticky = W)
        
        Label(self,
              text = "Game: "
              ).grid(row = 1, column = 2, sticky = W)
        self.game1_ent = Entry(self)
        self.game1_ent.grid(row = 1, column = 3, sticky = W)
        
        Label(self,
              text = "Noun: "
              ).grid(row = 2, column = 2, sticky = W)
        self.noun4_ent = Entry(self)
        self.noun4_ent.grid(row = 2, column = 3, sticky = W)  
        
        Label(self,
              text = "Verb: "
              ).grid(row = 3, column = 2, sticky = W)
        self.verb1_ent = Entry(self)
        self.verb1_ent.grid(row = 3, column = 3, sticky = W)
        
        Label(self,
              text = "Verb: "
              ).grid(row = 4, column = 2, sticky = W)
        self.verb2_ent = Entry(self)
        self.verb2_ent.grid(row = 4, column = 3, sticky = W)
         
        Label(self,
              text = "Noun: "
              ).grid(row = 5, column = 2, sticky = W)
        self.noun5_ent = Entry(self)
        self.noun5_ent.grid(row = 5, column = 3, sticky = W)
        
        Label(self,
              text = "Verb: "
              ).grid(row = 6, column = 2, sticky = W)
        self.verb3_ent = Entry(self)
        self.verb3_ent.grid(row = 6, column = 3, sticky = W)
        
        Label(self,
              text = "Noun: "
              ).grid(row = 1, column = 4, sticky = W)
        self.noun6_ent = Entry(self)
        self.noun6_ent.grid(row = 1, column = 5, sticky = W)
        
        Label(self,
              text = "Plant: "
              ).grid(row = 2, column = 4, sticky = W)
        self.plant1_ent = Entry(self)
        self.plant1_ent.grid(row = 2, column = 5, sticky = W)
       
        Label(self,
              text = "Body part: "
              ).grid(row = 3, column = 4, sticky = W)
        self.bp1_ent = Entry(self)
        self.bp1_ent.grid(row = 3, column = 5, sticky = W)
        
        Label(self,
              text = "Place: "
              ).grid(row = 4, column = 4, sticky = W)
        self.place1_ent = Entry(self)
        self.place1_ent.grid(row = 4, column = 5, sticky = W)
        
        Label(self,
              text = "Verb: "
              ).grid(row = 5, column = 4, sticky = W)
        self.verb4_ent = Entry(self)
        self.verb4_ent.grid(row = 5, column = 5, sticky = W)
        
        Label(self,
              text = "Adjective: "
              ).grid(row = 6, column = 4, sticky = W)
        self.adj3_ent = Entry(self)
        self.adj3_ent.grid(row = 6, column = 5, sticky = W)
       
        Label(self,
              text = "Noun: "
              ).grid(row = 6, column = 0, sticky = W)
        self.noun7_ent = Entry(self)
        self.noun7_ent.grid(row = 6, column = 1, sticky = W)
        
        Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 8, column = 4, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 8, column = 0, columnspan = 4)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        adj1 = self.adj1_ent.get()
        adj2 = self.adj2_ent.get()
        noun1 = self.noun1_ent.get()
        noun2 = self.noun2_ent.get()
        noun3 = self.noun3_ent.get()
        game1 = self.game1_ent.get()
        noun4 = self.noun4_ent.get()   
        verb1 = self.verb1_ent.get()  
        verb2 = self.verb2_ent.get()  
        noun5 = self.adj1_ent.get()
        verb3 = self.adj2_ent.get()
        noun6 = self.noun1_ent.get()
        plant1 = self.noun2_ent.get()
        bp1 = self.noun3_ent.get()
        place1 = self.game1_ent.get()
        verb4 = self.noun4_ent.get()   
        adj3 = self.verb1_ent.get()  
        noun7 = self.verb2_ent.get() 
 
        story = "A vacation is when you take a trip to some  "
        story += adj1
        story += " place with your "
        story += adj2
        story += " family. "
        story += " Usually you go to some place that is near a "
        story += noun1
        story += " or up on a "
        story += noun2 + ". "
        story += "A good vacation place is one where you can ride "
        story += noun3
        story += " or play "
        story += game1
        story += " or go hunting for "
        story += noun4 + ". "
        story += "I like to spend my time "
        story += verb1
        story += " or "
        story += verb2 + "."
        story += " When parents go on a vacation, they spend their time eating three "
        story += noun5
        story += " a day, and fathers play golf, and mothers sit around "
        story += verb3 + "."
        story += "Last summer, my little brother fell in a "
        story += noun6
        story += "and got poison "
        story += plant1
        story += " all over his "
        story += bp1 + "."
        story += " My family is going to go "
        story += place1
        story += " and I will practice "
        story += verb4 + ". "
        story += "Parents need vacations more than kids because parents are always very "
        story += adj3
        story += " trying to make enough "
        story += noun7
        story += " to pay for the vacation."
                                 
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

def main():
    root = Tk()
    root.title("Mad Lib")
    app = Application(root)
    root.mainloop()

main()


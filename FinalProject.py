#Name: Lingling Wang, Ruixin Li, Xiaohan Zhao
#Final Project


import tkinter as tk
import os
import time
from PIL import ImageTk, Image


class Test:
    def __init__(self):
        self.root = tk.Tk() #build the tkinter
        self.root.title("Search Engine") #name it Search Engine
        self.root.geometry("800x600") #set the size of the frame
        self.text = tk.Label(
            self.root, text="WHY WOMEN CODE", font=("Arial", 30), fg=("#ffd02e")
        ) #a label that represents our group :)
        self.text.grid(row=0, column=2, padx=20) #position of the label
        self.path = "/Users/linglingwang/desktop/ANTEATER.jpeg" #insert the picture (might need to change path on your side though
        self.img = Image.open(self.path) #open the picture
        self.resized = self.img.resize((300, 250)) #set size to fit the frame
        self.my_img = ImageTk.PhotoImage(self.resized) 
        self.l1 = tk.Label(self.root, image=self.my_img) #insert the anteater to our program
        self.l1.grid(row=2, column=2) #set position of the image
        self.entry = tk.Entry(
            self.root, width=40, highlightbackground="#005ab0", highlightcolor="#005ab0"
        ) #set entry frame and color
        self.entry.grid(row=4, column=2, padx=10) #set postion of entry frame
        self.button = tk.Button(self.root, text="submit", command=self.changeTXT) #set the submit button
        self.button.grid(row=4, column=3, padx=20) #set the position of the button
        self.result = tk.Text(self.root, height=80, width=80) #set the result frame
        self.result.grid(row=6, column=2, padx=20) #set the position of the result frame
        self.root.mainloop()

    def changeTXT(self):
        full_name_text_list = [] #save filesname and filestext together
        files_name = [] #save the names to this list
        files_text = [] #save the each textword to this list

        files_time = [] #save the time for each files

        match_word = [] #save the matched word to this list 
        match_filename = [] #save the matched files name to this list without repetition

        filelist = os.listdir(os.getcwd()) #get the files and text
        for files in filelist:
            try:
                with open(files, "r") as file: #open the files to read
                    for line in file: #read each line
                        for word in line.split():
                            lower_word = word.lower() #convert the word to lower case
                            files_name.append(files) #append to the file name list
                            files_text.append(lower_word) #append to the file text list
            except:
                pass

        full_name_text_list.extend(list(a) for a in zip(files_name, files_text)) #join the two list

        user_check = self.entry.get().lower() #convert the lower input

        for x in full_name_text_list: 
            if user_check in x: #check if the user's input in the whole list
                match_word.append(x[0]) #if it is, append the files name to a matching list

        for y in match_word: 
            if y not in match_filename: #check if there is any filesname show up twich
                match_filename.append(y) #only append the filesname once

        user_count = 0 
        for z in match_filename:
            start = time.time() #starting time
            if user_count < 1: #dealing with the first one's timing issue
                mid = time.time() #get the each's files time here
                converted = "{:.8f}".format(float(str(mid - start))) #convert to have no scientific notation
                files_time.append(converted) #appen the convereted number to the files time
                mid_before = mid #save the current time for next time use
                user_count = user_count + 1 #go to the next element

            else:
                mid = time.time() 
                converted = "{:.8f}".format(float(str(mid - mid_before)))
                files_time.append(converted)
                mid_before = mid

        count = 0 #to get the files time at specific round under for loop

        for i in match_filename:
            self.result.insert(tk.END, f"· {files_time[count]} {i}\n") #get the result
            count += 1 


if __name__ == "__main__":
    app = Test()

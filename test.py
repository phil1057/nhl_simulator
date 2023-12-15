import tkinter as tk
import time

def update_timer():
    global countdown_seconds
    if countdown_seconds > 0:
        mins, secs = divmod(countdown_seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        countdown_seconds -= 1
        time.sleep(1)  # Pause execution for 1 second
        update_timer()
    else:
        timer_label.config(text="Countdown finished!")

# Create tkinter window
root = tk.Tk()
root.title("Countdown Timer")

# Initial countdown time in seconds
countdown_seconds = 60  # Replace this with your desired countdown time

# Create and place a label to display the timer
timer_label = tk.Label(root, font=("Arial", 24), text="")
timer_label.pack(padx=20, pady=20)

# Start the countdown
update_timer()

# Start the tkinter main loop
root.mainloop()
"""
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Page Change Example")

        # Create a container to hold different pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store different pages
        self.pages = {}

        # Create and add multiple pages
        for PageClass in (PageOne, PageTwo, PageThree):
            page = PageClass(self.container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show the initial page with initial variable
        initial_variable = "Initial information"
        self.show_page(PageThree, initial_variable)

    def show_page(self, page_to_show, info=None):
        # Show the requested page with information
        page = self.pages[page_to_show]
        page.tkraise()
        if hasattr(page, "receive_info"):
            page.receive_info(info)



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Page One", font=("Arial", 18))
        self.label.pack(pady=20)
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Go to Page Two", command=self.go_to_page_two)
        self.button.pack()

    def go_to_page_two(self):
        info_to_send = self.entry.get()  # Get information from Entry widget
        self.controller.show_page(PageTwo, info_to_send)




class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Page Two", font=("Arial", 18))
        self.label.pack(pady=20)
        self.display_info = tk.Label(self, text="")
        self.display_info.pack()
        self.button = tk.Button(self, text="Go to Page Three", command=self.go_to_page_three)
        self.button.pack()

    def receive_info(self, info):
        self.display_info.config(text=f"Received Info: {info}")

    def go_to_page_three(self):
        self.controller.show_page(PageThree)




class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Page Three", font=("Arial", 18))
        self.label.pack(pady=20)
        self.button = tk.Button(self, text="Go to Page Two", command=self.go_to_page_two)
        self.button.pack()

    def go_to_page_two(self):
        self.controller.show_page(PageTwo)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    """
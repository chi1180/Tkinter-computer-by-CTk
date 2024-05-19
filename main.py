
import customtkinter

class SimpleComputer(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simple Computer")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green") # themes: "blue", "green", "dark-blue"

        self.current = 0
        self.term = 0
        self.option = 1

        btn_size = 70
        btn_padding = 5
        font = customtkinter.CTkFont(size = 24)

        btn_count = 0
        for r in range(3):
            for c in range(3):
                btn_count += 1

                customtkinter.CTkButton(
                    self,
                    text = str(btn_count),
                    command = lambda num = btn_count: self.key(num),
                    width = btn_size,
                    height = btn_size,
                    font = font
                ).grid(row = 3 - r, column = c, padx = btn_padding, pady = btn_padding)

        option_s = [ "+", "-", "*", "/" ]
        for i in range(len(option_s)):
            btn_count += 1

            customtkinter.CTkButton(
                self,
                text = option_s[i],
                command = lambda num = btn_count: self.key(num),
                width = btn_size,
                height = btn_size,
                font = font
            ).grid(row = i + 1, column = 3, padx = btn_padding, pady = btn_padding)

        customtkinter.CTkButton(
            self,
            text = "0",
            command = lambda: self.key(0),
            width = btn_size,
            height = btn_size,
            font = font
        ).grid(row = 4, column = 0, padx = btn_padding, pady = btn_padding)

        customtkinter.CTkButton(
            self,
            text = "=",
            command = lambda: self.key(14),
            width = btn_size,
            height = btn_size,
            font = font
        ).grid(row = 3, column = 4, padx = btn_padding, pady = btn_padding)

        customtkinter.CTkButton(
            self,
            text = "C",
            command = lambda: self.key(15),
            fg_color = "red",
            text_color = "black",
            width = btn_size,
            height = btn_size,
            font = font
        ).grid(row=1, column=4, padx = btn_padding, pady = btn_padding)

        entry = self.entry = customtkinter.CTkEntry(
            self,
            width = 400,
            height = btn_size / 2,
            font = font
        )
        entry.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 10)

    def key(self, num):
        if num > 9:
            if num < 14:
                self.term = self.current
                self.current = 0
                self.option = num - 9
            elif num == 14 and self.term:
                if self.option == 1:
                    self.current = self.term + self.current
                elif self.option == 2:
                    self.current = self.term - self.current
                elif self.option == 3:
                    self.current = self.term * self.current
                elif self.option == 4:
                    self.current = (self.term + 0.0) / (self.current + 0.0)

                self.term = 0

            elif num == 15:
                self.term = self.current = 0
        else:
            self.current = self.current * 10 + num

        self.entry.delete(0, customtkinter.END)
        self.entry.insert(0, str(self.current))

def main():
    app = SimpleComputer()
    app.mainloop()

if __name__ == '__main__':
    main()


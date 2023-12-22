# main module used for the execution of the system
# includes the main screen

import tkinter
import generator


def main():
    def show_password(large, special_cht, num, cap_letters):
        # definition of the second screen to show the password

        pass_root = tkinter.Toplevel()
        pass_root.title('Password')
        pass_root.geometry("400x225")

        if large is None or large == 0:
            pass_root.destroy()

        password_frame = tkinter.Frame(pass_root)
        password_frame.pack()

        # invocation of the function that generates the password

        password = generator.generate(large, special_cht, num, cap_letters)

        # password window definition

        success_message = tkinter.Label(password_frame, text='The password was generated correctly', justify='center',
                                        font=20).grid(row=0, column=1)

        password_label = tkinter.Label(password_frame, text=password, justify='center').grid(row=1, column=1)

        exit_button = tkinter.Button(password_frame, text='Exit', justify='center', command=pass_root.destroy) \
            .grid(row=2, column=0, pady=20)
        save_button = tkinter.Button(password_frame, text='Save', justify='center') \
            .grid(row=2, column=1, pady=20)
        copy_button = tkinter.Button(password_frame, text='Copy', justify='center') \
            .grid(row=2, column=2, pady=20)

    # definition of the root screen witch contains the components
    root = tkinter.Tk()
    root.title('Password Generator')
    root.geometry("400x225")

    options_frame = tkinter.Frame(root)
    options_frame.pack()

    # tittle configuration
    tittle_label = tkinter.Label(options_frame, text='Password Generator',
                                 justify='center', font=20).grid(row=0, column=1)

    # options configuration
    comment_label = tkinter.Label(options_frame, text='Please select every item to config the password')\
        .grid(row=1, column=1)

    special_value = tkinter.BooleanVar()
    cb_special = tkinter.Checkbutton(options_frame, variable=special_value).grid(row=2, column=0, pady=2)
    special_label = tkinter.Label(options_frame, text='Special character', justify='left').grid(row=2, column=1, pady=2)

    number_value = tkinter.BooleanVar()
    cb_numbers = tkinter.Checkbutton(options_frame, variable=number_value).grid(row=3, column=0, pady=2)
    numbers_label = tkinter.Label(options_frame, text='Numbers', justify='left').grid(row=3, column=1, pady=2)

    capital_value = tkinter.BooleanVar()
    cb_capital = tkinter.Checkbutton(options_frame, variable=capital_value).grid(row=4, column=0, pady=2)
    capital_label = tkinter.Label(options_frame, text='Capital letters', justify='left').grid(row=4, column=1, pady=2)

    large_int = tkinter.IntVar()
    large_label = tkinter.Label(options_frame, text='Large: ').grid(row=5, column=0, pady=2)
    large_txt = tkinter.Entry(options_frame, width=5, textvariable=large_int).grid(row=5, column=1, pady=2)

    acceptation_button = tkinter.Button(options_frame, text='Generate', justify='center',
                                        command=lambda: show_password(large_int.get(), special_value.get(), number_value.get(), capital_value.get()))\
        .grid(row=6, column=1, pady=20)
    cancel_button = tkinter.Button(options_frame, text='Cancel', justify='center', command=root.destroy)\
        .grid(row=6, column=2, pady=20)

    root.mainloop()


if __name__ == '__main__':
    # control condition to execute the main wrapper function
    main()

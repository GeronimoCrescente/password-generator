# main module used for the execution of the system
# includes the main screen
import tkinter
import generator


def main():
    # definition of the root screen witch contains the components
    root = tkinter.Tk()
    root.title('Password Generator')
    root.geometry("400x500")

    #
    options_frame = tkinter.Frame(root)
    options_frame.pack()

    # tittle configuration
    tittle_label = tkinter.Label(options_frame, text='Password Generator',
                                 justify='center', font=20).pack()

    # options configuration
    comment_label = tkinter.Label(options_frame, text='Please select every item to config the password').pack()
    large_label = tkinter.Label(options_frame, text='Select').pack()
    # large_txt = tkinter

    root.mainloop()


if __name__ == '__main__':
    # control condition to execute the main wrapper function
    main()

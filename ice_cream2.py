import easygui
flavor = easygui.enterbox("What is your favorite ice cream falvor?",
default = 'Vanilla')

easygui.msgbox("You entered " + flavor)
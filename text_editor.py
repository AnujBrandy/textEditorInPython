#very basic text editor
#python built in tkinter module

from Tkinter import *
from tkFileDialog import *

fileName = "Default"

def newFile( ) :
    global fileName
    fileName = "untitled"
    text.delete( 0.0 , END )

def saveFile( ) :
    global fileName
    t = text.get( 0.0, END )
    f = open( fileName, "w" )
    f.write( t )
    f.close( )

def saveAs( ) :
    f = asksaveasfile( mode = 'w' , defaultextension = '.txt' )
    t = text.get( 0.0 , END )
    try :
        f.write( t.rstrip( ) )
    except :
        showerror( title = "oops!" , message = "unable to save file .. " )

def openFile( ) :
    f = askopenfile( mode = 'r' )
    t = f.read( )
    text.delete( 0.0 , END )
    text.insert( 0.0 , t )

root = Tk( )
root.title( "My python text editor" )
root.minsize( width = 400 , height = 400 )
root.maxsize( width = 400 , height = 400 )

text = Text( root , width = 400 , height = 400 )
text.pack( )

menubar = Menu( root )
filemenu = Menu( menubar )

filemenu.add_command( label = "New" , command = newFile )
filemenu.add_command( label = "Open" , command = openFile )
filemenu.add_command( label = "Save" , command = saveFile )
filemenu.add_command( label = "Save as" , command = saveAs )
filemenu.add_separator( )
filemenu.add_command( label = "Quit" , command = root.quit )
menubar.add_cascade( label = "File" , menu = filemenu )

root.config( menu = menubar )
root.mainloop( )
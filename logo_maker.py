import sys


WELCOME = '''\n
___________________________________________
|                                         |
| L e w P o r t ' s   L o g o   M a k e r | <--- Title
|                            It's mental! | <--- Sub-Title
|_________________________________________|
\n'''

def get_text():
    '''
    The user can input the main title and 
    sub-title of their logo.
    '''
    print(WELCOME)
    title = input("Your Title: ")
    sub = input("Sub-Title: ")
    return title, sub
    
def make_spaced_title(title):
    '''
    make the title have a space between each character (but not subtitle)
    '''
    spaced_title = ''
    for i in title:
        spaced_title += (i + ' ')
    return spaced_title[:-1]

def logo(title="This is the title", sub="this is the subtitle"):
    '''
    convert the text to a fancy logo and return it as a string
    '''
    spaced_title = make_spaced_title(title)
    title_width = len(spaced_title) if len(sub) < len(spaced_title) else len(sub)
    top = "_" * (title_width + 4)
    middle = "|" + (" " * (title_width + 2)) + "|"
    title_line = "| " +spaced_title + " " * (title_width - len(spaced_title)) + " |"
    sub_line = "| " + " "*(title_width - len(sub)) + sub + " |"
    bottom = "|" + "_"*(title_width + 2) +"|"
    return f'''{top}
{middle}
{title_line}
{sub_line}
{bottom}'''

if __name__ == "__main__":
    try:
        logo = logo(*get_text())
    except KeyboardInterrupt:
	    print("\nYou killed the program!")
	    sys.exit(0)
    if '-w' in sys.argv:
        '''
	add a -w flag in the terminal if you want to pre-format it in
	mono font for pasting into whatsapp to annoy toby
	'''
        logo = f"""```{logo}```"""
    print(f"\n{logo}")


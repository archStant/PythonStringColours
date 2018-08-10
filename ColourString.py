helpString = '''\033[1mSyntax:
\033[0mcs.colour(inputString, colour=Default, bold=False, underline=False, invert=False)

\033[1mCurrently supported colours:\033[0m
\033[31mRed           \033[91mBright-red
\033[33mYellow        \033[93mBright-yellow
\033[32mGreen         \033[92mBright-green
\033[34mBlue          \033[94mBright-blue
\033[35mMagenta       \033[95mBright-magenta
\033[36mCyan          \033[96mBright-cyan
\033[30mBlack         \033[90mBright-black
\033[37mWhite         \033[97mBright-white\033[0m
Default

\033[1mExample usage:\033[0m
cs.colour("Something went very wrong!", "bright-red")
--> \033[91mSomething went very wrong!\033[0m

cs.colour("This could be a filename", "blue", bold=True)
--> \033[34;1mThis could be a filename\033[0m

cs.colour("Just to underline my point", underline=True)
--> \033[4mJust to underline my point\033[0m

cs.colour("Let\'s go all in!", "bright-yellow", bold=True, underline=True, invert=True)
--> \033[93;1;4;7mLet\'s go all in!\033[0m
\033[0m'''

colourCodes = {
    'RED':'\033[31',
    'YELLOW':'\033[33',
    'GREEN':'\033[32',
    'BLUE':'\033[34',
    'BLACK':'\033[30',
    'WHITE':'\033[37',
    'MAGENTA':'\033[35',
    'CYAN':'\033[36',
    'BRIGHT-RED':'\033[91',
    'BRIGHT-YELLOW':'\033[93',
    'BRIGHT-GREEN':'\033[92',
    'BRIGHT-BLUE':'\033[94',
    'BRIGHT-BLACK':'\033[90',
    'BRIGHT-WHITE':'\033[97',
    'BRIGHT-MAGENTA':'\033[95',
    'BRIGHT-CYAN':'\033[96'
    # 'DEFAULT':'\033['
}

def colour(inputString='', colour='Default', bold=False, underline=False, invert=False):
    if inputString == '':
        print(helpString)
        return
    if not type(colour) == str:
        print('''\033[33mError: Wrongly typed cs.colour()
Colour is of %s but should be of <type \'str\'>
To get help and a full list of colours, call cs.colour() with no arguments\033[0m''' % (str(type(colour))))
        return inputString
    if not type(bold) == bool:
        print('''\033[33mError: Wrongly typed cs.colour()
Bold is of %s but should be of <type \'bool\'>
To get help and a full list of colours, call cs.colour() with no arguments\033[0m''' % (str(type(bold))))
        return inputString
    if not type(underline) == bool:
        print('''\033[33mError: Wrongly typed cs.colour()
Underline is of %s but should be of <type \'bool\'>
To get help and a full list of colours, call cs.colour() with no arguments\033[0m''' % (str(type(underline))))
        return inputString
    if not type(invert) == bool:
        print('''\033[33mError: Wrongly typed cs.colour()
Invert is of %s but should be of <type \'bool\'>
To get help and a full list of colours, call cs.colour() with no arguments\033[0m''' % (str(type(invert))))
        return inputString
    capCol = colour.upper()
    colourCode = colourCodes.get(capCol, '\033[')
    prefix = colourCode + ';1'*bold + ';4'*underline + ';7'*invert + 'm'
    return prefix + inputString + '\033[0m'

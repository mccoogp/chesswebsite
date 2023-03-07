
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
alpha = "abcdefgh"
import piece as Piece
from Chess import Super_king, Forward
global chess 
global which
which = "superking"
chess = Super_king()




def pic(spot, piece):
    if piece.lower() == "p":
        name = "pawn"
    elif piece.lower() == "b":
        name = "bishop"
    elif piece.lower() == "n":
        name = "knight"
    elif piece.lower() == "r":
        name = "rook"
    elif piece.lower() == "q":
        name = "queen"
    elif piece.lower() == "k":
        name = "king"
    else:
        return 'https://raw.githubusercontent.com/mccoogp/chesswebsite/main/empty.png'
    
    if piece.isupper():
        color = "white"
    else:
        color = "black"
    
    return f'https://raw.githubusercontent.com/mccoogp/chesswebsite/main/{name}-{color}.png'

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/setup/super")
def start_super():
    global chess
    global which
    chess = Super_king()
    which ="superking"
    return redirect(url_for("board", color = "white1", setup = "0000K00000PPPP0000000000000000000000000000000000pppppppprnbqkbnr"))
    
@app.route("/setup/forward")
def start_forawrd():
    global chess
    global which
    chess = Forward()
    
    return redirect(url_for("board", color = "white1", setup = "RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr"))


@app.route("/board/<color>/<setup>")
def board(color, setup):

    inputs = []
    for i in range(len(setup)):
        inputs.append(pic(i, setup[i]))
    return render_template("firstbutton.html", link = "/board/" + color + "/" + setup, text1 = "Click the piece you want to move!",
                           a1 = inputs[0], b1 = inputs[1], c1 = inputs[2], d1 = inputs[3], e1 = inputs[4], f1 = inputs[5], g1 = inputs[6], h1 = inputs[7],  
                           a2 = inputs[8], b2 = inputs[9], c2 = inputs[10], d2 = inputs[11], e2 = inputs[12], f2 = inputs[13], g2 = inputs[14], h2 = inputs[15], 
                           a3 = inputs[16], b3 = inputs[17], c3 = inputs[18], d3 = inputs[19], e3 = inputs[20], f3 = inputs[21], g3 = inputs[22], h3 = inputs[23],
                           a4 = inputs[24], b4 = inputs[25], c4 = inputs[26], d4 = inputs[27], e4 = inputs[28], f4 = inputs[29], g4 = inputs[30], h4 = inputs[31],
                           a5 = inputs[32], b5 = inputs[33], c5 = inputs[34], d5 = inputs[35], e5 = inputs[36], f5 = inputs[37], g5 = inputs[38], h5 = inputs[39],
                           a6 = inputs[40], b6 = inputs[41], c6 = inputs[42], d6 = inputs[43], e6 = inputs[44], f6 = inputs[45], g6 = inputs[46], h6 = inputs[47],
                           a7 = inputs[48], b7 = inputs[49], c7 = inputs[50], d7 = inputs[51], e7 = inputs[52], f7 = inputs[53], g7 = inputs[54], h7 = inputs[55],
                           a8 = inputs[56], b8 = inputs[57], c8 = inputs[58], d8 = inputs[59], e8 = inputs[60], f8 = inputs[61], g8 = inputs[62], h8 = inputs[63])

@app.route("/board/<color>/<setup>/<spot>")
def clicked(color, setup, spot):
    inputs = []
    for i in range(len(setup)):
        inputs.append(pic(i, setup[i]))
    return render_template("firstbutton.html", link = "/board/" + color + "/" +  setup + "/" + spot, text1 = "Click the square you want to move to!",
                           a1 = inputs[0], b1 = inputs[1], c1 = inputs[2], d1 = inputs[3], e1 = inputs[4], f1 = inputs[5], g1 = inputs[6], h1 = inputs[7],  
                           a2 = inputs[8], b2 = inputs[9], c2 = inputs[10], d2 = inputs[11], e2 = inputs[12], f2 = inputs[13], g2 = inputs[14], h2 = inputs[15], 
                           a3 = inputs[16], b3 = inputs[17], c3 = inputs[18], d3 = inputs[19], e3 = inputs[20], f3 = inputs[21], g3 = inputs[22], h3 = inputs[23],
                           a4 = inputs[24], b4 = inputs[25], c4 = inputs[26], d4 = inputs[27], e4 = inputs[28], f4 = inputs[29], g4 = inputs[30], h4 = inputs[31],
                           a5 = inputs[32], b5 = inputs[33], c5 = inputs[34], d5 = inputs[35], e5 = inputs[36], f5 = inputs[37], g5 = inputs[38], h5 = inputs[39],
                           a6 = inputs[40], b6 = inputs[41], c6 = inputs[42], d6 = inputs[43], e6 = inputs[44], f6 = inputs[45], g6 = inputs[46], h6 = inputs[47],
                           a7 = inputs[48], b7 = inputs[49], c7 = inputs[50], d7 = inputs[51], e7 = inputs[52], f7 = inputs[53], g7 = inputs[54], h7 = inputs[55],
                           a8 = inputs[56], b8 = inputs[57], c8 = inputs[58], d8 = inputs[59], e8 = inputs[60], f8 = inputs[61], g8 = inputs[62], h8 = inputs[63])

def setboard(setup):
    board=[]
    for i in range(8):
        temp= []
        for j in range(8):
            piece = setup[j+8*i]
            if piece.isupper():
                white = True
            else:
                white = False
            if piece.lower() == "p":
                piece = Piece.Pawn(white)
            elif piece.lower() == "b":
                piece = Piece.Bishop(white)
            elif piece.lower() == "n":
                piece = Piece.Knight(white)
            elif piece.lower() == "r":
                piece = Piece.Rook(white)
            elif piece.lower() == "q":
                piece = Piece.Queen(white)
            elif piece.lower() == "k":
                piece = Piece.King(white)
            else:
                piece = None
            temp.append(piece)
        board.append(temp)
    return board

def unpack(board):
    setup = ""
    for row in board:
        for piece in row:
            if piece:
                if piece.color:
                    setup+= str(piece.name).upper()
                else:
                    setup += str(piece.name).lower()
            else:
                setup += "0" 
    return str(setup)


def translate(s):
    """
    Translates traditional board coordinates of chess into list indices
    """
    try:
        row = int(s[1])
        col = s[0]
        if row < 1 or row > 8:
            print(s[0] + "is not in the range from 1 - 8")
            return None
        if col < 'a' or col > 'h':
            print(s[1] + "is not in the range from a - h")
            return None
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return (row-1, dict[col])
    except:
        print(s + "is not in the format '[letter][number]'")
        return None

@app.route("/board/<color>/<setup>/<spot>/<nexts>")
def moved(color, setup, spot, nexts):
    #test
    chess.board.board = setboard(setup)
    if color == "white1":
        chess.turn = 1
    elif color == "white2":
        chess.turn = 2
    else:
        chess.turn = False
    chess.move(translate(spot), translate(nexts))
    setup = unpack(chess.board.board)
    print(chess.turn)
    if chess.turn == 1:
        newturn = "white1"
        loss = "white"
        for i in setup:
            if i == "K":
                loss = False
    elif chess.turn == 2:
        newturn = "white2"
        loss = "white"
        for i in setup:
            if i == "K":
                loss = False
    else:
        newturn = "black"
        loss = "black"
        for i in setup:
            if i == "k":
                loss = False
    if not loss:
        return redirect(url_for("board", color = newturn, setup = setup))
    else:
        return redirect(url_for("end", color = loss, setup = setup))

@app.route("/end/<color>/<setup>")
def end(color, setup):

    inputs = []
    for i in range(len(setup)):
        inputs.append(pic(i, setup[i]))
    return render_template("end.html", color = color.title(),
                           a1 = inputs[0], b1 = inputs[1], c1 = inputs[2], d1 = inputs[3], e1 = inputs[4], f1 = inputs[5], g1 = inputs[6], h1 = inputs[7],  
                           a2 = inputs[8], b2 = inputs[9], c2 = inputs[10], d2 = inputs[11], e2 = inputs[12], f2 = inputs[13], g2 = inputs[14], h2 = inputs[15], 
                           a3 = inputs[16], b3 = inputs[17], c3 = inputs[18], d3 = inputs[19], e3 = inputs[20], f3 = inputs[21], g3 = inputs[22], h3 = inputs[23],
                           a4 = inputs[24], b4 = inputs[25], c4 = inputs[26], d4 = inputs[27], e4 = inputs[28], f4 = inputs[29], g4 = inputs[30], h4 = inputs[31],
                           a5 = inputs[32], b5 = inputs[33], c5 = inputs[34], d5 = inputs[35], e5 = inputs[36], f5 = inputs[37], g5 = inputs[38], h5 = inputs[39],
                           a6 = inputs[40], b6 = inputs[41], c6 = inputs[42], d6 = inputs[43], e6 = inputs[44], f6 = inputs[45], g6 = inputs[46], h6 = inputs[47],
                           a7 = inputs[48], b7 = inputs[49], c7 = inputs[50], d7 = inputs[51], e7 = inputs[52], f7 = inputs[53], g7 = inputs[54], h7 = inputs[55],
                           a8 = inputs[56], b8 = inputs[57], c8 = inputs[58], d8 = inputs[59], e8 = inputs[60], f8 = inputs[61], g8 = inputs[62], h8 = inputs[63])

@app.route("/user/<name>")
def hello_world(name):
    if name == "home":
        return redirect(url_for("home"))
    return f"<p>Hello, {name}!</p>"


if __name__ == '__main__':
    app.run(host ='0.0.0.0')

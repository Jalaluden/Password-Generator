from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intex.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['user_choice']
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    result = determine_winner(user_choice, computer_choice)

    return render_template('intex.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

def determine_winner(player, computer):
    if player == computer:
        return 'It\'s a tie!'
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')
    ):
        return 'You win!'
    else:
        return 'You lose!'

if __name__ == '__main__':
    app.run(debug=True)
    

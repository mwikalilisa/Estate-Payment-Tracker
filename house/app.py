from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the Excel data once at the start
data = pd.read_excel('house_owners.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        house_number = int(request.form.get('house_number').strip())
        print(f"User input house number (as int): {house_number}")

        # Assuming house numbers in the DataFrame are integers
        record = data[data['house_number'] == house_number]

        if record.empty:
            return "No records found for the given house number."
        else:
            payment_details = record[['Date', 'payments']].to_dict(orient='records')
            return render_template('results.html', payment_details=payment_details)
        


    except ValueError:
        return "Invalid house number. Please enter a valid number.", 400

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An internal error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)

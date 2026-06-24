from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Future Lawyer Guide for Teens</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                margin: 0;
                padding: 0;
            }

            header {
                background-color: #1f4e79;
                color: white;
                text-align: center;
                padding: 30px;
            }

            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
            }

            .card {
                background: white;
                padding: 20px;
                margin: 20px 0;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }

            h2 {
                color: #1f4e79;
            }

            footer {
                background-color: #1f4e79;
                color: white;
                text-align: center;
                padding: 15px;
                margin-top: 30px;
            }

            ul, ol {
                line-height: 1.8;
            }
        </style>
    </head>
    <body>

        <header>
            <h1>⚖️ Future Lawyer Guide for Teenagers</h1>
            <p>Everything you should know if you want to study law.</p>
        </header>

        <div class="container">

            <div class="card">
                <h2>Why Study Law?</h2>
                <p>
                    Law helps people understand their rights, solve problems,
                    and promote justice. Lawyers can work in courts,
                    businesses, government, and many other fields.
                </p>
            </div>

            <div class="card">
                <h2>Important Skills</h2>
                <ul>
                    <li>Reading and writing</li>
                    <li>Critical thinking</li>
                    <li>Research skills</li>
                    <li>Public speaking</li>
                    <li>Problem-solving</li>
                    <li>Communication</li>
                </ul>
            </div>

            <div class="card">
                <h2>Subjects to Focus On</h2>
                <ul>
                    <li>English</li>
                    <li>History</li>
                    <li>Government / Civics</li>
                    <li>Social Studies</li>
                    <li>Debate and Public Speaking</li>
                </ul>
            </div>

            <div class="card">
                <h2>Steps to Become a Lawyer</h2>
                <ol>
                    <li>Finish high school.</li>
                    <li>Attend university.</li>
                    <li>Apply to law school.</li>
                    <li>Earn a law degree.</li>
                    <li>Pass the required legal exams.</li>
                    <li>Start practicing law.</li>
                </ol>
            </div>

            <div class="card">
                <h2>Activities for Teenagers</h2>
                <ul>
                    <li>Join a debate club.</li>
                    <li>Read about famous court cases.</li>
                    <li>Volunteer in your community.</li>
                    <li>Practice writing essays.</li>
                    <li>Follow current events and news.</li>
                </ul>
            </div>

            <div class="card">
                <h2>Helpful Advice</h2>
                <p>
                    Start developing strong study habits now.
                    Read often, stay curious, and practice speaking
                    confidently. These skills will help you succeed in law.
                </p>
            </div>

        </div>

        <footer>
            <p>© 2026 Future Lawyer Guide</p>
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
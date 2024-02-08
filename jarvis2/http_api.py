from flask import Flask, request, jsonify
from app import PersonalAssistant

app = Flask(__name__)
assistant = PersonalAssistant()


@app.route('/command', methods=['POST'])
def get_command():
    data = request.json
    command = data.get('command')

    # Determine the command and execute the corresponding method.
    # This is a very basic example and real implementation might require more complex parsing.
    if "event" in command.lower():
        assistant.add_event(command)
        return jsonify({"message": "Event added!"})
    elif "relationship" in command.lower():
        assistant.add_relationship(command)
        return jsonify({"message": "Relationship added!"})
    # Continue with other cases...


if __name__ == '__main__':
    app.run(debug=True)

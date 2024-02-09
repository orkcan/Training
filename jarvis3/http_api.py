from flask import Flask, request, jsonify
from app import PersonalAssistant

app = Flask(__name__)
assistant = PersonalAssistant()


@app.route('/command', methods=['POST'])
def get_command():
    data = request.json
    command = data.get('command')

    search_phrases = ["search for", "find out", "look up", "i want to know about", "can you tell me about", "who is",
                      "what is"]
    for phrase in search_phrases:
        if phrase in command:  # check if any of the search_phrases are in the user command
            search_query = command.replace(phrase, "").strip()  # separate the actual query
            results = assistant.bing_search(search_query)  # search using the query
            return jsonify({"message": f"Found {len(results)} results for your search!", "search_results": results})

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





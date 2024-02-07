import speech_recognition as sr
from jarvis_decision_tree import JarvisDecisionTree, DecisionTreeBranch, visualize_decision_tree

class JarvisInteractiveApp:
    def __init__(self):
        self.user_profile = {
            "age": None,
            "profession": None,
            "recently_married": None,
            "years_in_nl": None,
            "has_adhd": None,
            "interests": [],
            "exercise_frequency": None,
            "sleep_hours": None
        }

        self.decision_tree = JarvisDecisionTree(self.user_profile)
        self.recognizer = sr.Recognizer()

    def get_user_profile(self):
        print("Let's create your user profile. Answer the following questions:")
        self.user_profile["age"] = self.get_voice_input("What is your age? ")
        self.user_profile["profession"] = self.get_voice_input("What is your profession? ")
        self.user_profile["recently_married"] = self.get_yes_no_input("Have you recently been married?")
        self.user_profile["years_in_nl"] = int(self.get_voice_input("How many years have you been in the Netherlands? "))
        self.user_profile["has_adhd"] = self.get_yes_no_input("Do you have ADHD?")

        interests = self.get_voice_input("Enter your interests (comma-separated): ")
        self.user_profile["interests"] = [interest.strip() for interest in interests.split(",")]

        self.user_profile["exercise_frequency"] = int(self.get_voice_input("How often do you exercise per week? "))
        self.user_profile["sleep_hours"] = int(self.get_voice_input("How many hours do you sleep per night? "))

    def adapt_decision_tree(self):
        age_branch = DecisionTreeBranch(
            condition_function=lambda profile: age_condition(profile, 30, 40),
            action_function=lambda profile: print("You are in the 30-40 age range.")
        )
        recently_married_branch = DecisionTreeBranch(
            condition_function=recently_married_condition,
            action_function=remind_about_marriage_action
        )
        nl_integration_branch = DecisionTreeBranch(
            condition_function=lambda profile: years_in_nl_condition(profile, 1),
            action_function=provide_nl_integration_support_action
        )

        age_branch.add_subbranch(recently_married_branch)
        recently_married_branch.add_subbranch(nl_integration_branch)

        self.decision_tree.add_branch(age_branch)

    def visualize_tree(self):
        visualize_decision_tree(self.decision_tree, filename="interactive_decision_tree")

    def get_voice_input(self, prompt):
        with sr.Microphone() as source:
            print(prompt)
            audio_data = self.recognizer.listen(source, timeout=5)

        try:
            text = self.recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio. Please repeat.")
            return self.get_voice_input(prompt)

    def get_yes_no_input(self, prompt):
        response = self.get_voice_input(f"{prompt} (say yes or no)")
        return response.lower() == "yes"

    def run_jarvis(self):
        self.adapt_decision_tree()
        self.visualize_tree()
        self.decision_tree.analyze_and_respond()

# Instantiate and run the JarvisInteractiveApp
if __name__ == "__main__":
    jarvis_app = JarvisInteractiveApp()
    jarvis_app.get_user_profile()
    jarvis_app.run_jarvis()

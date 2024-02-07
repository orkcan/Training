from datetime import datetime, timedelta
import random

class JarvisDecisionTree:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.branches = []

    def analyze_and_respond(self):
        for branch in self.branches:
            branch.analyze_and_respond(self.user_profile)

    def add_branch(self, branch):
        self.branches.append(branch)

class DecisionTreeBranch:
    def __init__(self, condition_function, action_function):
        self.condition_function = condition_function
        self.action_function = action_function
        self.subbranches = []

    def analyze_and_respond(self, user_profile):
        if self.condition_function(user_profile):
            self.action_function(user_profile)
            for subbranch in self.subbranches:
                subbranch.analyze_and_respond(user_profile)

    def add_subbranch(self, subbranch):
        self.subbranches.append(subbranch)

def age_condition(user_profile, min_age, max_age):
    user_age = user_profile["age"]
    return min_age <= user_age <= max_age

def profession_condition(user_profile, target_profession):
    return user_profile["profession"].lower() == target_profession.lower()

def recently_married_condition(user_profile):
    return user_profile["recently_married"]

def years_in_nl_condition(user_profile, min_years):
    return user_profile["years_in_nl"] >= min_years

def has_adhd_condition(user_profile):
    return user_profile["has_adhd"]

# ... Add more condition functions as needed

def remind_about_marriage_action(user_profile):
    print("Congratulations on your recent marriage! Don't forget to plan a special date night.")

def provide_nl_integration_support_action(user_profile):
    print("Welcome to the Netherlands! Need help with local integration?")

def check_daily_activities_action(user_profile):
    print("Let's review your daily activities and schedule.")

# ... Add more action functions as needed

# Example usage of the enhanced decision tree
if __name__ == "__main__":
    user_profile = {
        "age": 31,
        "profession": "electronics and communication engineer",
        "recently_married": True,
        "years_in_nl": 2,
        "has_adhd": True
    }

    decision_tree = JarvisDecisionTree(user_profile)

    # Define branches and subbranches
    age_branch = DecisionTreeBranch(condition_function=lambda profile: age_condition(profile, 30, 40),
                                    action_function=lambda profile: print("You are in the 30-40 age range."))
    recently_married_branch = DecisionTreeBranch(condition_function=recently_married_condition,
                                                action_function=remind_about_marriage_action)
    nl_integration_branch = DecisionTreeBranch(condition_function=lambda profile: years_in_nl_condition(profile, 1),
                                               action_function=provide_nl_integration_support_action)

    # Add subbranches to the main branches
    age_branch.add_subbranch(recently_married_branch)
    recently_married_branch.add_subbranch(nl_integration_branch)

    # Add the main branches to the decision tree
    decision_tree.add_branch(age_branch)

    # Analyze and respond
    decision_tree.analyze_and_respond(user_profile)

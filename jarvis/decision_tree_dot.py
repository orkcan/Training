from graphviz import Digraph

def visualize_decision_tree(decision_tree, filename="decision_tree"):
    dot = Digraph(comment="Jarvis Decision Tree")
    node_counter = 0

    def visualize_branch(branch, parent_node=None):
        nonlocal node_counter

        current_node = str(node_counter)
        node_counter += 1

        # Add node for the current branch
        dot.node(current_node, label=branch.condition_function.__name__)

        # Connect to the parent node if applicable
        if parent_node is not None:
            dot.edge(parent_node, current_node)

        # Add subbranches recursively
        for subbranch in branch.subbranches:
            visualize_branch(subbranch, current_node)

    for main_branch in decision_tree.branches:
        visualize_branch(main_branch)

    # Save the dot file and render it to a PNG image
    dot.render(filename, format="png", cleanup=True)

# Example usage
if __name__ == "__main__":
    user_profile = {
        "age": 31,
        "profession": "electronics and communication engineer",
        "recently_married": True,
        "years_in_nl": 2,
        "has_adhd": True
    }

    decision_tree = JarvisDecisionTree(user_profile)

    age_branch = DecisionTreeBranch(condition_function=lambda profile: age_condition(profile, 30, 40),
                                    action_function=lambda profile: print("You are in the 30-40 age range."))
    recently_married_branch = DecisionTreeBranch(condition_function=recently_married_condition,
                                                action_function=remind_about_marriage_action)
    nl_integration_branch = DecisionTreeBranch(condition_function=lambda profile: years_in_nl_condition(profile, 1),
                                               action_function=provide_nl_integration_support_action)

    age_branch.add_subbranch(recently_married_branch)
    recently_married_branch.add_subbranch(nl_integration_branch)

    decision_tree.add_branch(age_branch)

    visualize_decision_tree(decision_tree)

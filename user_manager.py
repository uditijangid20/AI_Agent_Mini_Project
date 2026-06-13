# user_manager.py — duplicate code example
users = []

def add_user_to_list(name, email):
    user = {"name": name, "email": email}
    users.append(user)
    print(f"User {name} added.")

def register_new_user(name, email):
    # DUPLICATE: same logic as add_user_to_list
    user = {"name": name, "email": email}
    users.append(user)
    print(f"User {name} added.")

add_user_to_list("Alice", "alice@test.com")
register_new_user("Bob", "bob@test.com")
print("thankyou for your response")

import ollama
import software_a
import software_b
import software_c

MODEL = "gemma4:31b-cloud"


def ask_agent(number, iteration, history):

    prompt = f"""
You are controlling three tools which operate numbers.

Tools:
software_a = double number
software_b = subtract 3
software_c = square root

Rules:
- number < 20       -> software_a
- 20 <= number <=50 -> software_c
- number > 50       -> software_b

Current Number: {number}

Current Iteration: {iteration}

History:
{history}

IMPORTANT:
When iteration reaches 10,
reply ONLY:

stop

Otherwise choose the correct tool.

Reply with only one word:

software_a
software_b
software_c
stop
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0
        }
    )

    return (
        response["message"]["content"]
        .strip()
        .lower()
        .split()[0]
    )


def execute(tool, number):

    if tool == "software_a":
        return software_a.run(number)

    if tool == "software_b":
        return software_b.run(number)

    if tool == "software_c":
        return software_c.run(number)

    return number


def run_agent():

    number = float(input("Enter a starting number: "))

    history = []
    iteration = 0

    print("\nAI Agent Started\n")

    while True:

        iteration += 1

        print(
            f"\n--- Iteration {iteration} | Current number: {number} ---"
        )

        decision = ask_agent(
            number,
            iteration,
            "\n".join(history[-5:])
        )

        print(f"[Gemma] Decision: {decision}")

        if decision == "stop":
            print("\nAgent decided to stop.")
            print(f"Final Number: {number}")
            break

        old_number = number

        number = execute(decision, number)

        history.append(
            f"{old_number} -> {decision} -> {number}"
        )

        print(f"Result: {number}")


if __name__ == "__main__":
    run_agent()
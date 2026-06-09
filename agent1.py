import ollama
import software_a, software_b, software_c

MODEL = "gemma4:31b-cloud"
TOOLS = {"software_a": software_a.run, "software_b": software_b.run, "software_c": software_c.run}

def ask_agent(number, iteration):
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": f"""
You control three tools for numbers.
software_a=double, software_b=subtract 3, software_c=square root
Rules: <20→software_a, 20-50→software_c, >50→software_b
Number: {number} | Iteration: {iteration}/10
Reply ONE word (software_a/software_b/software_c/stop). Reply 'stop' at iteration 10.
"""}],
        options={"temperature": 0}
    )
    return response["message"]["content"].strip().lower().split()[0]

def run_agent():
    number = float(input("Enter a starting number: "))
    iteration = 0

    while True:
        iteration += 1
        decision = ask_agent(number, iteration)
        print(f"Iteration {iteration} | Number: {number} | Decision: {decision}")

        if decision == "stop":
            print(f"Final Number: {number}")
            break

        number = TOOLS[decision](number)

run_agent()
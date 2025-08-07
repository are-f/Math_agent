from guardrail import is_math_query
from database_search import run_math_tutor

def main():
    detailed_mode = False
    
    while True:
        query = input("Ask me a question (or type 'exit'): ").strip()
        if query.lower() == "exit":
            break

        if is_math_query(query):
            response = run_math_tutor(query,detailed_mode)
            print(response)
            feedback = input( "Was the response up to your expectation? Answer in Yes or NO : " ).strip()
            if feedback.lower() in ["yes"]:
                detailed_mode = False
            else:
                print("I'll try to explain more clearly from now on....")
                detailed_mode = True
        else:
            print("Sorry, I can only help with math-related queries.")

if __name__ == "__main__":
    main()

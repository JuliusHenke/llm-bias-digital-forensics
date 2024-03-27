from src.main import generate_responses


def send(question: str, experiment_title: str, command_output: str, seed: int = 0):
    generate_responses(system_message, question + "\n\n" + command_output, experiment_title, 1, 500, seed)


system_message = """
Company X has contacted you to perform forensics work on a recent incident that occurred. One
of their employees had received an email from a fellow co-worker that pointed to a PDF file.
Upon opening, the employee did not seem to notice anything, however recently they have had
unusual activity in their bank account. Company X was able to obtain a memory image of the
employee’s virtual machine upon suspected infection. Company X wishes you to analyze the
virtual memory and report on any suspected activities found. Questions can be found below to
help in the formal report for the investigation.

Be concise and answer in less than 200 words.
"""

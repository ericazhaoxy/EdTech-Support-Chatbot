import tkinter as tk
from src.rule_based.bot import create_chatbot, get_response

def main():
    chatbot = create_chatbot()

    root = tk.Tk()
    root.title("EdTech Support Chatbot")

    chat_log = tk.Text(root, height=20, width=60)
    chat_log.pack(padx=10, pady=10)
    chat_log.insert(tk.END, "Bot: Hi! Ask me something.\n")

    user_entry = tk.Entry(root, width=60)
    user_entry.pack(padx=10, pady=(0, 10))

    def respond():
        user_input = user_entry.get()
        if not user_input.strip():
            return
        response = get_response(chatbot, user_input)
        chat_log.insert(tk.END, f"You: {user_input}\n")
        chat_log.insert(tk.END, f"Bot: {response}\n")
        user_entry.delete(0, tk.END)

    send_button = tk.Button(root, text="Send", command=respond)
    send_button.pack(pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    main()
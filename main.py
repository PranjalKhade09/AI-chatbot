import tkinter as tk
from tkinter import scrolledtext
from chatbot import GetAnswer

# ---------------- Send Message ----------------
def send_message():

    user_message = entry.get().strip()

    if user_message == "":
        return

    # First message -> switch to chat view
    if not chat_visible[0]:

        heading.pack_forget()
        subheading.pack_forget()

        chat_area.pack(
            padx=20,
            pady=20,
            fill=tk.BOTH,
            expand=True
        )

        input_frame.pack_forget()

        input_frame.pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=20,
            pady=20
        )

        chat_visible[0] = True

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: " + user_message + "\n\n", "user")

    answer = GetAnswer(user_message)

    chat_area.insert(tk.END, "Bot: " + answer + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

    chat_area.see(tk.END)


# ---------------- Clear Chat ----------------
def clear_chat():

    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.config(state=tk.DISABLED)

    chat_area.pack_forget()

    input_frame.pack_forget()

    heading.pack(pady=(120, 10))
    subheading.pack()

    input_frame.pack(pady=30)

    chat_visible[0] = False


# ---------------- Main Window ----------------
root = tk.Tk()

root.title("AI College Chatbot")

root.geometry("1100x700")

root.configure(bg="white")


# ---------------- Heading ----------------
heading = tk.Label(
    root,
    text="Hi! How can I help you today?",
    font=("Segoe UI", 30, "bold"),
    bg="white",
    fg="black"
)

heading.pack(pady=(120, 10))


# ---------------- Sub Heading ----------------
subheading = tk.Label(
    root,
    text="Ask me anything about Dr. D. Y. Patil Polytechnic",
    font=("Segoe UI", 16),
    bg="white",
    fg="gray"
)

subheading.pack()


# ---------------- Chat Area ----------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Segoe UI", 13),
    state=tk.DISABLED,
    bg="white",
    fg="black",
    relief="flat"
)

chat_area.tag_config(
    "user",
    foreground="#0B57D0",
    font=("Segoe UI", 13, "bold")
)

chat_area.tag_config(
    "bot",
    foreground="#202124",
    font=("Segoe UI", 13)
)

chat_area.pack_forget()

chat_visible = [False]


# ---------------- Input Frame ----------------
input_frame = tk.Frame(root, bg="white")

input_frame.pack(pady=30)


# ---------------- Entry ----------------
entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 15),
    width=70,
    relief="solid",
    bd=1,
    bg="#F7F7F8"
)

entry.pack(
    side=tk.LEFT,
    ipadx=10,
    ipady=10,
    padx=(0, 10)
)

entry.bind("<Return>", lambda event: send_message())


# ---------------- Send Button ----------------
send_btn = tk.Button(
    input_frame,
    text="➜",
    font=("Arial", 18),
    bg="black",
    fg="white",
    relief="flat",
    width=3,
    command=send_message
)

send_btn.pack(side=tk.LEFT)


# ---------------- Clear Button ----------------
clear_btn = tk.Button(
    input_frame,
    text="Clear",
    font=("Segoe UI", 11, "bold"),
    bg="#E53935",
    fg="white",
    relief="flat",
    command=clear_chat
)

clear_btn.pack(side=tk.LEFT, padx=10)


# ---------------- Footer ----------------
footer = tk.Label(
    root,
    text="Dr. D. Y. Patil Polytechnic AI Chatbot",
    font=("Segoe UI", 10),
    fg="gray",
    bg="white"
)

footer.pack(side=tk.BOTTOM, pady=5)


root.mainloop()
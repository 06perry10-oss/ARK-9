"""ARK-9 RC4 — free desktop chat application.

No subscriptions, paid tiers, license keys, or feature paywalls.
Built-in responses run locally and require no API key.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime


APP_NAME = "ARK-9"
VERSION = "RC4"


class ARK9App:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APP_NAME} {VERSION} — Free")
        self.root.geometry("960x650")
        self.root.minsize(700, 450)
        self._build_ui()
        self._add_message(
            "ARK-9",
            "Welcome to ARK-9 RC4!\n"
            "Your chat app is ready. ARK-9 is completely free, "
            "with no subscriptions, license keys, or locked features.\n"
            "Type /help to see commands."
        )

    def _build_ui(self):
        menu = tk.Menu(self.root)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="Save chat transcript...", command=self._save_transcript)
        file_menu.add_command(label="Clear chat", command=self._clear)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menu.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menu, tearoff=False)
        help_menu.add_command(label="Commands", command=self._show_help)
        help_menu.add_command(label="About ARK-9", command=self._about)
        menu.add_cascade(label="Help", menu=help_menu)
        self.root.configure(menu=menu)

        header = ttk.Frame(self.root, padding=12)
        header.pack(fill="x")

        ttk.Label(
            header, text=APP_NAME, font=("Segoe UI", 19, "bold")
        ).pack(side="left")
        ttk.Label(header, text=VERSION).pack(side="left", padx=8)
        ttk.Label(
            header, text="100% FREE", foreground="#16833b",
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", padx=12)

        self.status = ttk.Label(header, text="Ready")
        self.status.pack(side="right")

        main = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        main.pack(fill="both", expand=True)

        self.chat = tk.Text(
            main, wrap="word", state="disabled",
            font=("Segoe UI", 11), padx=12, pady=12,
            borderwidth=1, relief="solid"
        )
        self.chat.pack(fill="both", expand=True)

        controls = ttk.Frame(main, padding=(0, 10, 0, 0))
        controls.pack(fill="x")

        self.entry = ttk.Entry(controls, font=("Segoe UI", 11))
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self._send_event)
        self.entry.focus_set()

        ttk.Button(controls, text="Send", command=self._send).pack(
            side="left", padx=(8, 0)
        )
        ttk.Button(controls, text="Save chat", command=self._save_transcript).pack(
            side="left", padx=(8, 0)
        )
        ttk.Button(controls, text="Clear", command=self._clear).pack(
            side="left", padx=(8, 0)
        )

        footer = ttk.Label(
            self.root,
            text="ARK-9 RC4 • Free forever • No paid features",
            anchor="center"
        )
        footer.pack(fill="x", padx=12, pady=(0, 8))

    def _add_message(self, sender, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.chat.configure(state="normal")
        self.chat.insert("end", f"[{timestamp}] {sender}:\n{message}\n\n")
        self.chat.configure(state="disabled")
        self.chat.see("end")

    def _send_event(self, _event):
        self._send()
        return "break"

    def _send(self):
        message = self.entry.get().strip()
        if not message:
            return

        self.entry.delete(0, "end")
        self._add_message("You", message)
        command = message.lower().strip()

        if command in {"/help", "help"}:
            response = (
                "Available commands:\n"
                "/help  — show this help\n"
                "/time  — show your local time\n"
                "/version  — show the app version\n"
                "/free  — show the free-software policy\n"
                "/clear  — clear the conversation\n"
                "/about  — show app information"
            )
        elif command in {"/time", "time", "what time is it"}:
            response = f"Local time: {datetime.now().strftime('%H:%M:%S')}"
        elif command in {"/version", "version"}:
            response = f"You are running {APP_NAME} {VERSION}."
        elif command in {"/free", "free", "cost", "price"}:
            response = (
                "ARK-9 is 100% free. There are no paid plans, "
                "subscriptions, license keys, premium editions, "
                "or locked features."
            )
        elif command in {"/about", "about"}:
            response = (
                f"{APP_NAME} {VERSION}\n"
                "A completely free Python desktop chat application."
            )
        elif command == "/clear":
            self._clear()
            return
        elif command in {"hi", "hello", "hey"}:
            response = f"Hello! {APP_NAME} {VERSION} is ready."
        else:
            response = (
                f"ARK-9 received: {message}\n\n"
                "This starter build uses local built-in responses; "
                "it does not connect to an online AI service."
            )

        self._add_message("ARK-9", response)
        self.status.configure(text="Online")

    def _clear(self):
        self.chat.configure(state="normal")
        self.chat.delete("1.0", "end")
        self.chat.configure(state="disabled")
        self._add_message("ARK-9", "New conversation started.")
        self.status.configure(text="Ready")
        self.entry.focus_set()

    def _save_transcript(self):
        content = self.chat.get("1.0", "end-1c")
        if not content.strip():
            messagebox.showinfo("Save chat", "There is no chat to save yet.")
            return

        path = filedialog.asksaveasfilename(
            title="Save ARK-9 chat transcript",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not path:
            return

        try:
            with open(path, "w", encoding="utf-8") as transcript:
                transcript.write(f"{APP_NAME} {VERSION} chat transcript\n")
                transcript.write("=" * 42 + "\n\n")
                transcript.write(content)
            self.status.configure(text="Transcript saved")
            messagebox.showinfo("Save chat", "Chat transcript saved successfully.")
        except OSError as error:
            messagebox.showerror("Save failed", f"Could not save the transcript:\n{error}")

    def _show_help(self):
        messagebox.showinfo(
            "ARK-9 Commands",
            "Commands you can type in the chat:\n\n"
            "/help  - Show commands\n"
            "/time  - Show local time\n"
            "/version  - Show version\n"
            "/free  - Explain the free policy\n"
            "/clear  - Start a new conversation\n"
            "/about  - About ARK-9"
        )

    def _about(self):
        messagebox.showinfo(
            "About ARK-9",
            "ARK-9 RC4\n\n"
            "A completely free desktop chat application.\n\n"
            "No subscriptions. No paid plans. No license keys. "
            "No premium editions. No locked features.\n\n"
            "Built-in responses run locally and need no API key."
        )


def main():
    root = tk.Tk()
    try:
        ttk.Style(root).theme_use("vista")
    except tk.TclError:
        pass
    ARK9App(root)
    root.mainloop()


if __name__ == "__main__":
    main()

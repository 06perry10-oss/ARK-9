"""ARK-9 RC3 — completely free desktop chat application.

No subscriptions, paid tiers, license keys, or feature paywalls.
The built-in responses run locally and require no API key.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


APP_NAME = "ARK-9"
VERSION = "RC3"


class ARK9App:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APP_NAME} {VERSION} — Free")
        self.root.geometry("900x600")
        self.root.minsize(700, 450)
        self._build_ui()
        self._add_message(
            "ARK-9",
            "Welcome to ARK-9 RC3!\n"
            "ARK-9 is completely free. There are no subscriptions, "
            "paid plans, license keys, or locked features."
        )

    def _build_ui(self):
        header = ttk.Frame(self.root, padding=12)
        header.pack(fill="x")

        ttk.Label(
            header, text=APP_NAME, font=("Segoe UI", 18, "bold")
        ).pack(side="left")
        ttk.Label(header, text=VERSION).pack(side="left", padx=8)

        free_label = ttk.Label(
            header, text="100% FREE", foreground="#16833b",
            font=("Segoe UI", 10, "bold")
        )
        free_label.pack(side="left", padx=12)

        self.status = ttk.Label(header, text="Ready")
        self.status.pack(side="right")

        main = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        main.pack(fill="both", expand=True)

        self.chat = tk.Text(
            main, wrap="word", state="disabled",
            font=("Segoe UI", 11), padx=12, pady=12
        )
        self.chat.pack(fill="both", expand=True)

        controls = ttk.Frame(main, padding=(0, 10, 0, 0))
        controls.pack(fill="x")

        self.entry = ttk.Entry(controls)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self._send_event)
        self.entry.focus_set()

        ttk.Button(controls, text="Send", command=self._send).pack(
            side="left", padx=(8, 0)
        )
        ttk.Button(controls, text="Clear", command=self._clear).pack(
            side="left", padx=(8, 0)
        )
        ttk.Button(controls, text="About", command=self._about).pack(
            side="left", padx=(8, 0)
        )

    def _add_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M")
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
        text = message.lower()

        if text in {"hi", "hello", "hey"}:
            response = "Hello! ARK-9 RC3 is online and completely free."
        elif "version" in text:
            response = f"You are running {APP_NAME} {VERSION}."
        elif "free" in text or "cost" in text or "price" in text:
            response = (
                "ARK-9 is 100% free. There are no paid plans, "
                "subscriptions, license keys, or premium features."
            )
        elif "help" in text:
            response = (
                "Try hello, version, help, status, time, or ask whether "
                "ARK-9 is free. The built-in chat works locally."
            )
        elif "status" in text:
            response = "Status: Online • RC3 • Free edition"
        elif text in {"time", "what time is it"}:
            response = f"Local time: {datetime.now().strftime('%H:%M:%S')}"
        else:
            response = f"ARK-9 received: {message}"

        self._add_message("ARK-9", response)
        self.status.configure(text="Online")

    def _clear(self):
        self.chat.configure(state="normal")
        self.chat.delete("1.0", "end")
        self.chat.configure(state="disabled")
        self._add_message("ARK-9", "Chat cleared.")
        self.status.configure(text="Ready")

    def _about(self):
        messagebox.showinfo(
            "About ARK-9",
            "ARK-9 RC3\n\n"
            "A completely free desktop chat application.\n\n"
            "No subscriptions. No paid plans. No license keys. "
            "No premium editions. No locked features.\n\n"
            "All included features are available at no cost."
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

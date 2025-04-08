# 🧾 CLI Contact Book

A dead-simple, terminal-based Contact Manager in Python.  
No GUI. No fluff. Just pure functionality: add, view, search, edit, and delete contacts stored locally in a JSON file.

---

## 🛠 Features

- 📝 Add new contacts  
- 📄 View all contacts  
- 🔍 Search by name or phone  
- ✏️ Edit existing contacts  
- 🗑️ Delete contacts  
- 💾 Contacts saved in `storage.json`

---

## 🚀 Getting Started

### 🔧 1. Clone the repo
```bash
git clone https://github.com/rev2607/CLI-Contact-Book.git
cd CLI-Contact-Book
```

### ▶️ 2. Run the app
```bash
python contact_book.py
```

## 🧪 Sample Menu
```
--- Contact Book Menu ---
1. Add Contact
2. View All Contacts
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit
```

## 📁 File Structure
```
.
├── contact_book.py    # CLI interaction and main loop
├── contact_manager.py # Core logic and data persistence
└── storage.json       # Contact data (auto-created if missing)
```

## 📦 Dependencies
None. 100% built on Python's standard library:
* `json`
* `os`
* `builtins`

No need to install anything.

## 👨‍🔧 Built By
A developer who prefers clarity over complexity. Designed to be extendable, maintainable. Fork it, ship it, make it yours.

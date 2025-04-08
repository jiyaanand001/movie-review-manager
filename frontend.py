import tkinter as tk
from tkinter import messagebox
import backend

backend.create_tables()

def add_movie():
    backend.add_movie(title_entry.get(), director_entry.get(), genre_entry.get())
    messagebox.showinfo("Added", "Movie added!")

def add_review():
    backend.add_review(review_movie_entry.get(), int(rating_entry.get()), comment_entry.get())
    messagebox.showinfo("Added", "Review added!")

def show_movies():
    listbox.delete(0, tk.END)
    movies = backend.view_movies()
    for movie in movies:
        listbox.insert(tk.END, f"{movie[1]} by {movie[2]} ({movie[3]})")

def show_reviews():
    listbox.delete(0, tk.END)
    reviews = backend.view_reviews(review_movie_entry.get())
    for r in reviews:
        listbox.insert(tk.END, f"⭐ {r[0]}: {r[1]}")

def search_movies():
    listbox.delete(0, tk.END)
    results = backend.search_movies(search_entry.get())
    for r in results:
        listbox.insert(tk.END, f"{r[1]} by {r[2]} ({r[3]})")

root = tk.Tk()
root.title("🎬 Movie Review Manager")

tk.Label(root, text="Title").grid(row=0, column=0)
tk.Label(root, text="Director").grid(row=1, column=0)
tk.Label(root, text="Genre").grid(row=2, column=0)

title_entry = tk.Entry(root)
director_entry = tk.Entry(root)
genre_entry = tk.Entry(root)

title_entry.grid(row=0, column=1)
director_entry.grid(row=1, column=1)
genre_entry.grid(row=2, column=1)

tk.Button(root, text="Add Movie", command=add_movie).grid(row=3, column=0, columnspan=2, pady=5)

tk.Label(root, text="Movie (for review)").grid(row=4, column=0)
tk.Label(root, text="Rating (1-5)").grid(row=5, column=0)
tk.Label(root, text="Comment").grid(row=6, column=0)

review_movie_entry = tk.Entry(root)
rating_entry = tk.Entry(root)
comment_entry = tk.Entry(root)

review_movie_entry.grid(row=4, column=1)
rating_entry.grid(row=5, column=1)
comment_entry.grid(row=6, column=1)

tk.Button(root, text="Add Review", command=add_review).grid(row=7, column=0, columnspan=2, pady=5)

tk.Button(root, text="Show All Movies", command=show_movies).grid(row=8, column=0)
tk.Button(root, text="Show Reviews", command=show_reviews).grid(row=8, column=1)

tk.Label(root, text="Search").grid(row=9, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=9, column=1)
tk.Button(root, text="Search Movies", command=search_movies).grid(row=10, column=0, columnspan=2)

listbox = tk.Listbox(root, width=60)
listbox.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()

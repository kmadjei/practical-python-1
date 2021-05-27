# access the OS module for u
import os

# os.environ.setdefault() gets  and sets the environment variables
# for the Host, the database, and other variables for running the app
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "LFhVT4kBlE")

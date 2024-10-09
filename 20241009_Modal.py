""""
modal run 20241009_Modal.py
✓ Initialized. View run at https://modal.com/apps/tinchung41/main/ap-wCabxWqrrWKYYyoByezXqS
✓ Created objects.
├── 🔨 Created mount /home/tinchung/Documents/GitHub/Mamba-LLM-project/20241009_Modal.py
└── 🔨 Created function square.
This code is running on a remote worker!
the square is 1764
Stopping app - local entrypoint completed.
✓ App completed. View run at https://modal.com/apps/tinchung41/main/ap-wCabxWqrrWKYYyoByezXqS
"""
import modal

app = modal.App("example-get-started")


@app.function()
def square(x):
    print("This code is running on a remote worker!")
    return x**2


@app.local_entrypoint()
def main():
    print("the square is", square.remote(42))

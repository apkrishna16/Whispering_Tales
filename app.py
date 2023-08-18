from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form.get("prompt") 
        generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
        generated_text =  generator(prompt, max_length=100, do_sample=True, temperature=0.9)[0]["generated_text"]
        return render_template("index.html", prompt=prompt, generated_text=generated_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

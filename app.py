from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
  return (
      "DevSecOps Security Scanner. Application is running successfully. "
      "Security scanning is integrated into the CI/CD pipeline."
  )


@app.route("/search")
def search():
  query = request.args.get("q", "")
  return f"Search query: {query}"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
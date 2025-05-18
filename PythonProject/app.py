from flask import Flask, render_template, request

app = Flask(__name__)

# Simple Q&A dictionary
QA_PAIRS = {
    "What is content creation?": "Content creation is the process of producing digital material such as videos, articles, and social media posts.",
    "What is SEO?": "SEO stands for Search Engine Optimization. It's the process of improving your content's visibility on search engines.",
    "How to start content writing?": "Begin by choosing a niche, understanding your audience, and practicing regularly.",
    "What tools help content creators?": "Canva, Grammarly, Notion, Google Docs, and ChatGPT are popular tools.",
    "What makes content engaging?": "Relevant, clear, well-structured, and visually appealing content engages audiences.",
    "What is a content calendar?": "A content calendar helps plan and schedule content publishing in advance.",
    "What's the ideal blog length?": "Usually 1000–2000 words, but it depends on your topic and audience.",
    "What platforms are best for creators?": "YouTube, Instagram, LinkedIn, TikTok, and Medium are popular platforms.",
    "What is content marketing?": "It's a marketing strategy focused on creating and distributing valuable content to attract a target audience.",
    "What are types of content?": "Blog posts, videos, infographics, podcasts, eBooks, and social media posts.",
    "How do I grow my audience?": "Be consistent, understand your audience, provide value, and interact with followers.",
    "How often should I post?": "At least once a week, but frequency depends on platform and audience.",
    "What is a CTA?": "A CTA (Call to Action) is a prompt that tells users what to do next (e.g., 'Subscribe now').",
    "What is repurposing content?": "Turning one piece of content (like a blog post) into other formats (e.g., video, infographic).",
    "What is plagiarism?": "Plagiarism is copying someone else's content without permission or credit.",
    "How to check grammar?": "Use tools like Grammarly, Hemingway, or built-in spell checkers.",
    "What is content strategy?": "A content strategy defines what, where, when, and how you will publish your content.",
    "What skills do content creators need?": "Writing, SEO, marketing, creativity, video editing, and analytics.",
    "What is a niche?": "A niche is a specific area of interest or expertise you focus your content on.",
    "What is evergreen content?": "Evergreen content stays relevant and valuable for a long time."
}

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    user_question = ""
    if request.method == "POST":
        user_question = request.form.get("question", "")
        answer = QA_PAIRS.get(user_question.strip(), "Sorry, I don't have an answer for that question.")
    return render_template("index.html", answer=answer, questions=QA_PAIRS.keys(), user_question=user_question)

if __name__ == '__main__':
    app.run(debug=True)

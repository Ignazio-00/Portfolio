from unicodedata import name
from flask import Blueprint, flash, redirect, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db
from website.models import User

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/index")
@login_required
def index():
    return render_template("index.html", user=current_user)

@views.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")

        if not text:
            flash("Post cannot be empty", category="error")
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created!", category="success")
            return redirect(url_for("views.index"))
    posts = Post.query.all()
    return render_template("create_post.html", user=current_user, posts=posts)

# Check if Person is authorized to delete post via id
@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id).first

    if not post:
        flash("Post does not exist.", category="error")
    elif current_user.id != post.id:
        flash("Permission do delete post denied.", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted.", category="success")

    return redirect(url_for("views.index"))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("User does not exist.", category="error")
        return redirect(url_for("views.index"))

    posts = Post.query.filter_by(author=user.id).all()
    return render_template("posts.html", user=current_user, posts=posts, username=username)




from crypt import methods
from unicodedata import name
from flask import Blueprint, flash, redirect, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from importlib_metadata import method_cache

from website.auth import login
from .models import Post, User, Comment
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

@views.route("/postings", methods=["GET", "POST"])
@login_required
def postings():
    posts = Post.query.all()
    print(posts)
    return render_template("postings.html", user=current_user, posts=posts)

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

    posts = user.posts
    return render_template("posts.html", user=current_user, posts=posts, username=username)

@views.route("/create-comment/<post_id>", methods=["POST"])
@login_required
def create_comment(post_id):
    text = request.form.get("text")

    if not text:
        flash("Comment cannot be empty.", category="error")
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash("Post does not exist.", category="error")
        
    return redirect(url_for("views.index"))

@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash("Comment does not exist.", category="error")
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash("You do not have permission to delete this comment.", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()
    
    return redirect(url_for("views.index"))

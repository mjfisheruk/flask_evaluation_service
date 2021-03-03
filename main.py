from flask import request
from marshmallow import Schema, fields, ValidationError

from app import app
from data import comment


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


@app.route("/comments", methods=["GET"])
def get_comments():
    return {"comments": comments_schema.dump(comment.list())}


@app.route("/comments", methods=["POST"])
def create_comment():
    try:
        data = comment_schema.load(request.json)
    except ValidationError as err:
        return err.messages, 422
    comment.add(text=data["text"])
    return comment_schema.dump(comment), 201


@app.route("/comments/<int:comment_id>", methods=["GET"])
def show_comment(comment_id):
    c = comment.find_by_id(comment_id)
    if c is None:
        return {}, 404
    return comment_schema.dump(c)


@app.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    c = comment.find_by_id(comment_id)
    if c is None:
        return {}, 404
    try:
        data = comment_schema.load(request.json)
        comment.update(comment_id, text=data["text"])

    except ValidationError as err:
        return err.messages, 422
    return {}, 204


if __name__ == "__main__":
    app.run(debug=True)

from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Comment(id={self.id}, text={self.text})"


if __name__ == "__main__":
    # This file can be run directly to create the DB schema
    db.create_all()


def list():
    return Comment.query.all()


def add(text):
    comment = Comment(text)
    db.session.add(comment)
    db.session.commit()
    return comment


def find_by_id(comment_id):
    return Comment.query.get(comment_id)


def update(comment_id, text):
    comment = Comment.query.find(comment_id)
    comment.text = text
    db.session.commit()
    return comment

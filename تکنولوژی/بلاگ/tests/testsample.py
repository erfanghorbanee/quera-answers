from datetime import timedelta

from blog.models import *
from django.test import TestCase
from django.utils import timezone
from django.utils.timezone import datetime


class SampleTest(TestCase):
    def test_1_create_author(self):
        Author.objects.create(name="meysam1")
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get(id=1).name, "meysam1")

    def test_2_create_blog_post(self):
        a1 = Author.objects.create(name="meysam1")
        dt = datetime.now(timezone.utc)
        BlogPost.objects.create(author=a1, title="t1", body="b1")
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(BlogPost.objects.get(id=1).author, a1)
        self.assertEqual(BlogPost.objects.get(id=1).title, "t1")
        self.assertEqual(BlogPost.objects.get(id=1).body, "b1")
        self.assertLessEqual(
            BlogPost.objects.get(id=1).date_created - dt, timedelta(seconds=3)
        )

    def test_3_create_comment(self):
        a1 = Author.objects.create(name="meysam1")
        p1 = BlogPost.objects.create(author=a1, title="t1", body="b1")
        p2 = BlogPost.objects.create(author=a1, title="t2", body="b2")
        self.assertEqual(BlogPost.objects.count(), 2)
        Comment.objects.create(blog_post=p1, text="commenttt")
        Comment.objects.create(blog_post=p1, text="commenttt")
        Comment.objects.create(blog_post=p2, text="commenttt")
        Comment.objects.create(blog_post=p2, text="commenttt")
        self.assertEqual(Comment.objects.count(), 4)
        self.assertEqual(Comment.objects.get(id=1).text, "commenttt")
        self.assertEqual(Comment.objects.get(id=1).blog_post, p1)
        self.assertEqual(Comment.objects.get(id=2).text, "commenttt")
        self.assertEqual(Comment.objects.get(id=2).blog_post, p1)

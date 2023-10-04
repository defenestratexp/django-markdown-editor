# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Nonagon Media", description="N9N Test Case", wiki="Post Body")
        self.assertEqual(post.title, "Nonagon Media")
        self.assertEqual(post.description, "N9N Test Case")
        self.assertEqual(post.wiki, "Post Body")

from tortoise.contrib.test import TestCase

from app.models.article import Article


class TestCreateAriticle(TestCase):

    async def test_create_article(self) -> None:

        # Given
        author = "test_author"
        title = "test_title"
        body = "test_content"

        # When
        await Article.create(id="test_id", author=author, title=title, body=body)
        await Article.get_one_by_id()

        # Then
        article = await Article.get(title=title)
        assert article.author == author
        assert article.title == title
        assert article.body == body

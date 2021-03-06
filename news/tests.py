from django.test import TestCase
from .models import Category
from .forms import CategoryForm
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):

    def test_category_string_gives_back_category_name(self):
        user = User.objects.create(username='Brian')
        category = Category.objects.create(category_name='Test String', category_author=user)
        self.assertEqual(str(category), 'Test String')

    def test_approve_category_set_to_false(self):
        user = User.objects.create(username='Brian')
        category = Category.objects.create(category_name='Test String', category_author=user)
        self.assertFalse(category.approve_category)

class TestCategoryForm(TestCase):

    def test_category_name_must_be_entered(self):
        form = CategoryForm({'category_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['category_name'][0], 'This field is required.')

class TestViews(TestCase):

    def test_retrieve_category_list(self):
        page = self.client.get('/categories')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'categories.html')

    def test_retrieve_add_category_html(self):
        page = self.client.get('/category/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_category.html')

    def test_retrieve_edit_category_html(self):
        user = User.objects.create(username='Brian')
        category = Category.objects.create(category_name='Test String', category_author=user)
        page = self.client.get(f'/category/edit/{category.id}')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'edit_category.html')

    def test_category_edited(self):
        user = User.objects.create(username='Brian')
        category = Category.objects.create(category_name='Test String', category_author=user)
        page = self.client.post(f'/category/edit/{category.id}', {'category_name': 'Category Name Edited'})
        self.assertRedirects(page, '/categories')
        edited_category = Category.objects.get(id=category.id)
        self.assertEqual(edited_category.category_name, 'Category Name Edited')

    def test_delete_category(self):
        user = User.objects.create(username='Brian')
        category = Category.objects.create(category_name='Test String', category_author=user)
        page = self.client.get(f'/category/delete/{category.id}')
        self.assertRedirects(page, '/categories')
        remaining_categories = Category.objects.filter(id=category.id)
        self.assertFalse(remaining_categories)
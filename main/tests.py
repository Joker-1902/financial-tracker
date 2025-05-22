from django.test import TestCase
from .models import Transaction, Categories
from django.utils import timezone
from django.contrib.auth.models import User

class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Categories.objects.create(name='Продукты')
    def test_can_create_objects(self):
        transaction = Transaction.objects.create(
            user=self.user,
            type='Expense',
            date=timezone.now().date(),
            amount=100.50,
            category = self.category,
            description = 'Купи молоко и хлеб'
        )
        self.assertIsNotNone(transaction.id)
        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.type, 'Expense')
        self.assertEqual(transaction.amount, 100.50)
        self.assertEqual(transaction.date, timezone.now().date())
        self.assertEqual(transaction.category, self.category)
        self.assertEqual(transaction.description, 'Купи молоко и хлеб')



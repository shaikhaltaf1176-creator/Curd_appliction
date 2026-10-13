from django.test import TestCase
from django.urls import reverse

from .models import Entry


class EntryListViewTests(TestCase):
    def test_get_displays_form_and_saved_entries(self):
        entry = Entry.objects.create(
            name='Alex Example',
            email='alex@example.com',
            message='A saved message',
        )

        response = self.client.get(reverse('entry_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alex Example')
        self.assertContains(response, 'A saved message')
        self.assertContains(response, 'entry-search')
        self.assertContains(response, 'Save this moment')
        self.assertIn('form', response.context)

    def test_post_saves_entry_and_shows_success_feedback(self):
        response = self.client.post(
            reverse('entry_list'),
            {
                'name': 'Sam Example',
                'email': 'sam@example.com',
                'message': 'Hello there',
            },
            follow=True,
        )

        self.assertRedirects(response, reverse('entry_list'))
        self.assertContains(response, 'Your entry has been saved.')
        self.assertTrue(
            Entry.objects.filter(
                name='Sam Example',
                email='sam@example.com',
                message='Hello there',
            ).exists()
        )

    def test_invalid_post_does_not_save_entry(self):
        response = self.client.post(
            reverse('entry_list'),
            {'name': '', 'email': 'not-an-email', 'message': ''},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].errors)
        self.assertEqual(Entry.objects.count(), 0)

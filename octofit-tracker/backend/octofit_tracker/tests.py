from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team_name='Marvel')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.team_name, 'Marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

    def test_activity_creation(self):
        Activity.objects.create(username='testuser', type='run', duration=30)
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        Workout.objects.create(username='testuser', name='Morning Cardio', description='desc', duration=40)
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        Leaderboard.objects.create(team_name='Marvel', score=100)
        self.assertEqual(Leaderboard.objects.count(), 1)

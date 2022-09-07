from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates room_type"

    def handle(self, *args, **options):
        room_type = [
            "hotel",
            "motel",
            "guest house",
            "apt",
            "share house",
            "villa",
            "hostel",
        ]
        for r in room_type:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(room_type)} Room-type created!"))
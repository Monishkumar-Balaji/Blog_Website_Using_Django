from typing import Any
from blog.models import Post , Category
from django.core.management.base import BaseCommand
import random
 
class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args:Any , **options: Any):
        #Deleting existing data
        Post.objects.all().delete()
        
        titles = [
    "The Whispering Shadows",
    "Dancing with Fireflies",
    "The Last Clockmaker",
    "Echoes of a Forgotten Song",
    "Beneath the Neon Sky",
    "The Paper Moon Café",
    "Where the Rivers Run Backwards",
    "A Symphony of Silent Stars",
    "The Librarian's Secret",
    "Midnight in the Garden of Algorithms",
    "The Boy Who Spoke to Clouds",
    "The Cat Who Knew Too Much",
    "Lost in the Labyrinth of Time",
    "The Coffee Shop at the Edge of Reality",
    "The Girl Who Collected Echoes",
    "When the Maps Stopped Making Sense",
    "The Astronaut's Terrestrial Diary",
    "The Book of Vanishing Colors",
    "How to Fold Time Like Origami",
    "The Museum of Broken Memories"
]

        contents = [
    "How I Taught My Smart Fridge to Write Haiku",
    "The Secret Life of Abandoned Shopping Carts",
    "Why Your Plants Are Probably Judging You",
    "Baking Pi: A Mathematician's Guide to Pastry",
    "The Underground Society of Nighttime Bicycle Couriers",
    "Decoding the Hidden Patterns in Coffee Stains",
    "What If the Moon Was Made of Cheese? A Scientific Approach",
    "The Accidental Discovery of Invisible Street Art",
    "When My To-Do List Started Writing Back",
    "The Physics of Perfect Pizza Dough Throwing",
    "How to Build a Time Machine from Spare Parts",
    "The Algorithm That Predicted My Cat's Mood Swings",
    "Lost Cities Found in Google Maps",
    "Why Do We Dream in Binary? A Programmer's Theory",
    "The Mysterious Case of the Disappearing WiFi Signal",
    "Secret Societies of Your Local Public Transport",
    "How I Became a Professional Cloud Watcher",
    "The Untold History of Forgotten Keyboard Shortcuts",
    "When AI Starts Writing Poetry: A Case Study",
    "The Hidden Messages in Library Due Date Stamps"
]

        img_urls = [
    "https://picsum.photos/id/10/800/400",  # Forest
    "https://picsum.photos/id/11/800/400",  # Mountains
    "https://picsum.photos/id/12/800/400",  # Ocean cliff
    "https://picsum.photos/id/13/800/400",  # Northern lights
    "https://picsum.photos/id/14/800/400",  # Urban bridge
    "https://picsum.photos/id/15/800/400",  # City at night
    "https://picsum.photos/id/16/800/400",  # Rainy street
    "https://picsum.photos/id/17/800/400",  # Vintage building
    "https://picsum.photos/id/18/800/400",  # Lighthouse
    "https://picsum.photos/id/19/800/400",  # Sunset field
    "https://picsum.photos/id/20/800/400",  # Mountain lake
    "https://picsum.photos/id/21/800/400",  # Foggy road
    "https://picsum.photos/id/22/800/400",  # Woman portrait
    "https://picsum.photos/id/23/800/400",  # Man in black & white
    "https://picsum.photos/id/24/800/400",  # Pasta dish
    "https://picsum.photos/id/25/800/400",  # Coffee beans
    "https://picsum.photos/id/26/800/400",  # Breakfast spread
    "https://picsum.photos/id/27/800/400",  # Couple hiking
    "https://picsum.photos/id/28/800/400",  # Cocktails
    "https://picsum.photos/id/29/800/400"  
    ]

        categories = Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title = title, content = content , img_url =  img_url,category = category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
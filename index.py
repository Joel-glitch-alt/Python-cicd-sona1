# index.py
import json
import logging
from datetime import datetime
from random import randint, choice
from typing import List, Dict, Any

# Configure logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Dummy data for simulation
USERS = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Charlie", "role": "guest"},
]

POSTS = [
    {"id": 1, "user_id": 1, "title": "Welcome", "content": "Hello world!"},
    {"id": 2, "user_id": 2, "title": "Second Post", "content": "Another day..."},
]

# Utility functions
def generate_random_number(min_val=0, max_val=100):
    """Generate a random integer between min_val and max_val."""
    result = randint(min_val, max_val)
    logger.debug(f"Generated random number: {result}")
    return result

def current_timestamp():
    """Return current datetime as ISO string."""
    ts = datetime.now().isoformat()
    logger.debug(f"Current timestamp: {ts}")
    return ts

# User management
def get_user_by_id(user_id: int):
    logger.debug(f"Getting user by id: {user_id}")
    for user in USERS:
        if user["id"] == user_id:
            logger.debug(f"User found: {user}")
            return user
    logger.debug("User not found")
    return None

def add_user(name: str, role: str):
    new_id = max(user["id"] for user in USERS) + 1
    new_user = {"id": new_id, "name": name, "role": role}
    USERS.append(new_user)
    logger.info(f"Added user: {new_user}")
    return new_user

# Post management
def get_posts_by_user(user_id: int):
    logger.debug(f"Getting posts for user id: {user_id}")
    user_posts = [post for post in POSTS if post["user_id"] == user_id]
    logger.debug(f"Posts found: {user_posts}")
    return user_posts

def add_post(user_id: int, title: str, content: str):
    new_id = max(post["id"] for post in POSTS) + 1
    new_post = {"id": new_id, "user_id": user_id, "title": title, "content": content}
    POSTS.append(new_post)
    logger.info(f"Added post: {new_post}")
    return new_post

# Simulate API handlers
def api_get_user(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        return {"error": "User not found"}, 404
    return user, 200

def api_create_user(data: Dict[str, Any]):
    if "name" not in data or "role" not in data:
        return {"error": "Missing fields"}, 400
    user = add_user(data["name"], data["role"])
    return user, 201

def api_get_user_posts(user_id: int):
    posts = get_posts_by_user(user_id)
    return posts, 200

def api_create_post(data: Dict[str, Any]):
    if "user_id" not in data or "title" not in data or "content" not in data:
        return {"error": "Missing fields"}, 400
    user = get_user_by_id(data["user_id"])
    if user is None:
        return {"error": "User does not exist"}, 400
    post = add_post(data["user_id"], data["title"], data["content"])
    return post, 201

# Data Processing Classes
class DataProcessor:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data

    def filter_by_key_value(self, key: str, value: Any) -> List[Dict[str, Any]]:
        logger.debug(f"Filtering data by {key}={value}")
        filtered = [item for item in self.data if item.get(key) == value]
        logger.debug(f"Filtered data: {filtered}")
        return filtered

    def summarize_counts(self, key: str) -> Dict[Any, int]:
        summary = {}
        for item in self.data:
            k = item.get(key)
            if k in summary:
                summary[k] += 1
            else:
                summary[k] = 1
        logger.debug(f"Summary counts for {key}: {summary}")
        return summary

class PostStatistics:
    def __init__(self, posts: List[Dict[str, Any]]):
        self.posts = posts

    def total_posts(self) -> int:
        total = len(self.posts)
        logger.debug(f"Total posts: {total}")
        return total

    def average_title_length(self) -> float:
        if not self.posts:
            return 0
        avg = sum(len(post["title"]) for post in self.posts) / len(self.posts)
        logger.debug(f"Average title length: {avg}")
        return avg

    def longest_post(self) -> Dict[str, Any]:
        if not self.posts:
            return {}
        longest = max(self.posts, key=lambda p: len(p["content"]))
        logger.debug(f"Longest post: {longest}")
        return longest

# Example of long function to increase lines
def big_data_simulation():
    result = []
    for i in range(100):
        user_id = choice([user["id"] for user in USERS])
        title = f"Generated Post {i}"
        content = "x" * randint(20, 100)
        post = add_post(user_id, title, content)
        result.append(post)
    logger.info(f"Generated {len(result)} posts")
    return result

# Main execution block
if __name__ == "__main__":
    logger.info("Starting script...")

    # Create a new user
    new_user = add_user("David", "user")
    logger.info(f"New user created: {new_user}")

    # Create some posts
    posts_created = big_data_simulation()

    # Get user posts
    user_posts = get_posts_by_user(new_user["id"])
    logger.info(f"Posts for new user: {user_posts}")

    # Data processing example
    processor = DataProcessor(posts_created)
    user_post_counts = processor.summarize_counts("user_id")
    logger.info(f"Post counts by user: {user_post_counts}")

    # Post statistics
    stats = PostStatistics(posts_created)
    logger.info(f"Total posts: {stats.total_posts()}")
    logger.info(f"Average title length: {stats.average_title_length()}")
    logger.info(f"Longest post: {stats.longest_post()}")

    logger.info("Script finished.")
